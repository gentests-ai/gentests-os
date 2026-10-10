#!/usr/bin/env python3
"""Piloto de triagem pública: Lighthouse + Playwright + axe-core + links.
Sem IA/LLM, sem prospecção, sem envio de mensagens e sem testes intrusivos.
"""
import argparse
import csv
import ipaddress
import json
import os
from pathlib import Path
import socket
import subprocess
import tempfile
import time
from urllib.parse import urljoin, urlparse, urldefrag

import requests
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports" / "triagem"
USER_AGENT = "GenTests-PilotoTriagem/0.1 (inspecao-publica-limitada)"
TIMEOUT = 15

def public_url(url):
    u = urlparse(url)
    if u.scheme not in ("http", "https") or not u.hostname or u.username or u.password:
        return False
    if u.port and u.port not in (80, 443):
        return False
    host = u.hostname.lower().rstrip(".")
    if host == "localhost" or host.endswith(".localhost"):
        return False
    try:
        addresses = socket.getaddrinfo(host, u.port or (443 if u.scheme == "https" else 80))
        return bool(addresses) and all(ipaddress.ip_address(a[4][0]).is_global for a in addresses)
    except (OSError, ValueError):
        return False

def check_links(page, base, cap=5):
    origin = urlparse(base)
    candidates = page.locator("a[href]").evaluate_all(
        """els => [...new Set(els.map(a => a.href).filter(Boolean))].slice(0, 100)"""
    )
    chosen = []
    for link in candidates:
        link = urldefrag(link).url
        u = urlparse(link)
        if u.scheme not in ("http", "https") or u.hostname != origin.hostname:
            continue
        if link == urldefrag(base).url or link in chosen or not public_url(link):
            continue
        chosen.append(link)
        if len(chosen) == cap:
            break
    broken, inconclusive = [], []
    session = requests.Session()
    session.headers["User-Agent"] = USER_AGENT
    for link in chosen:
        try:
            r = session.get(link, timeout=TIMEOUT, allow_redirects=False, stream=True)
            # Nunca seguir redirecionamentos; sites podem redirecionar para redes internas.
            if r.status_code in (404, 410):
                broken.append({"url": link, "status": r.status_code})
            elif r.status_code >= 400 or r.status_code in (301, 302, 303, 307, 308):
                inconclusive.append({"url": link, "status": r.status_code})
            r.close()
        except requests.RequestException as e:
            inconclusive.append({"url": link, "erro": type(e).__name__})
        time.sleep(0.3)
    return chosen, broken, inconclusive

def run_lighthouse(url, chrome_path, folder):
    with tempfile.TemporaryDirectory() as tmp:
        output = Path(tmp) / "lh.json"
        cmd = [
            "npx", "--no-install", "lighthouse", url,
            "--only-categories=performance,seo",
            "--output=json", f"--output-path={output}",
            "--chrome-flags=--headless --no-sandbox --disable-gpu",
            "--quiet",
        ]
        env = dict(os.environ, CHROME_PATH=chrome_path)
        try:
            p = subprocess.run(cmd, capture_output=True, text=True, timeout=150, env=env)
            if p.returncode or not output.exists():
                return None, "Lighthouse nao concluiu: " + (p.stderr or "")[-400:]
            data = json.loads(output.read_text(encoding="utf-8"))
            (folder / "lighthouse.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
            perf = data.get("categories", {}).get("performance", {}).get("score")
            return (round(perf * 100) if perf is not None else None), None
        except (subprocess.TimeoutExpired, OSError, ValueError) as e:
            return None, str(e)

def scan(url, browser, axe_source, idx):
    folder = REPORTS / f"site-{idx:02d}"
    folder.mkdir(parents=True, exist_ok=True)
    result = {
        "site": url, "status": "inconclusivo", "performance": None,
        "axe_tipos": None, "links_quebrados": None, "achados": [],
        "erros": [], "links_testados": 0
    }
    context = browser.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=1)
    page = context.new_page()
    try:
        page.goto(url, wait_until="domcontentloaded", timeout=30000)
        final_url = page.url
        if not public_url(final_url):
            raise ValueError("Redirecionamento para destino nao publico")
        page.wait_for_timeout(1200)
        page.screenshot(path=str(folder / "captura-mobile.png"), full_page=False, timeout=10000)
        page.add_script_tag(content=axe_source)
        axe = page.evaluate("""async () => await axe.run(document, {runOnly: {type:'tag', values:['wcag2a','wcag2aa','wcag21a','wcag21aa']}})""")
        violations = axe.get("violations", [])
        result["axe_tipos"] = len(violations)  # quantidade de REGRAS violadas, não elementos
        (folder / "axe.json").write_text(json.dumps({
            "url": final_url,
            "violations": [{ "id": v["id"], "impact": v.get("impact"), "nodes": len(v["nodes"]), "help": v.get("help")} for v in violations]
        }, ensure_ascii=False, indent=2), encoding="utf-8")
        chosen, broken, inconclusive = check_links(page, final_url)
        result["links_testados"] = len(chosen)
        result["links_quebrados"] = len(broken)
        (folder / "links.json").write_text(json.dumps({
            "testados": chosen, "quebrados": broken, "inconclusivos": inconclusive
        }, ensure_ascii=False, indent=2), encoding="utf-8")
        if inconclusive:
            result["erros"].append("Alguns links foram inconclusivos; redirecionamentos nao seguidos")
    except Exception as e:
        result["erros"].append(f"Playwright/axe/links: {type(e).__name__}: {str(e)[:180]}")
    finally:
        context.close()
    result["performance"], lh_error = run_lighthouse(url, browser.browser_type.executable_path, folder)
    if lh_error:
        result["erros"].append(lh_error)
    if result["performance"] is not None and result["performance"] < 50:
        result["achados"].append("Performance Lighthouse abaixo de 50")
    if result["axe_tipos"] is not None and result["axe_tipos"] >= 3:
        result["achados"].append("Pelo menos 3 tipos de violacao axe-core")
    if result["links_quebrados"] is not None and result["links_quebrados"] >= 2:
        result["achados"].append("Pelo menos 2 links internos com HTTP 404/410")
    if result["achados"]:
        result["status"] = "revisar"
    elif result["performance"] is not None and result["axe_tipos"] is not None and result["links_quebrados"] is not None:
        result["status"] = "sem_gatilhos_na_amostra"
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sites", default="sites.txt", help="Arquivo com uma URL publica por linha (maximo 10)")
    args = parser.parse_args()
    sites_file = Path(args.sites)
    if not sites_file.exists():
        parser.error("Crie sites.txt com ate 10 URLs publicas, uma por linha.")
    sites = [s.strip() for s in sites_file.read_text(encoding="utf-8").splitlines()
             if s.strip() and not s.lstrip().startswith("#")]
    if not 1 <= len(sites) <= 10:
        parser.error("Informe de 1 a 10 URLs.")
    if len(sites) != len(set(sites)):
        parser.error("Remova URLs duplicadas.")
    for url in sites:
        if not public_url(url):
            parser.error("URL invalida ou nao publica: " + url)
    axe_path = ROOT / "node_modules" / "axe-core" / "axe.min.js"
    if not axe_path.exists():
        parser.error("Instale dependencias npm: npm install --no-save lighthouse axe-core")
    REPORTS.mkdir(parents=True, exist_ok=True)
    results = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        axe_source = axe_path.read_text(encoding="utf-8")
        for i, url in enumerate(sites, 1):
            print(f"[{i}/{len(sites)}] {url}", flush=True)
            results.append(scan(url, browser, axe_source, i))
            time.sleep(2)
        browser.close()
    (REPORTS / "resultado.json").write_text(json.dumps({
        "versao": "0.1", "classificacao": "gatilho_de_revisao_nao_reprovacao",
        "amostra_links_por_site": 5, "resultados": results
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    with (REPORTS / "resumo.csv").open("w", newline="", encoding="utf-8-sig") as f:
        columns = ["site", "status", "performance", "axe_tipos", "links_quebrados", "links_testados", "achados", "erros"]
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        for r in results:
            writer.writerow({**r, "achados": " | ".join(r["achados"]), "erros": " | ".join(r["erros"])})
    print("Relatorio:", REPORTS / "resumo.csv")
    print("Nenhum contato enviado; todos os alertas exigem confirmacao.")

if __name__ == "__main__":
    main()
