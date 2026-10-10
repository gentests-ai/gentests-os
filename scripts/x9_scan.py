#!/usr/bin/env python3
"""X9: verificações documentais determinísticas, somente leitura, sem RNC automática."""
from pathlib import Path
import re
import json
from datetime import datetime, timezone

root = Path(__file__).resolve().parents[1]
notes = [p for p in root.rglob("*.md") if ".git" not in p.parts]
ids = {}
findings = []
for path in notes:
    rel = path.relative_to(root).as_posix()
    content = path.read_text(encoding="utf-8")
    header = re.match(r"\A---\s*\n(.*?)\n---", content, flags=re.S)
    if not header:
        continue  # notas antigas sem frontmatter não são falhas por si
    meta = header.group(1)
    mid = re.search(r"^id:\s*['\"]?([^\s'\"]+)", meta, flags=re.M)
    if mid:
        code = mid.group(1)
        ids.setdefault(code, []).append(rel)
    status = re.search(r"^status:\s*(.+)$", meta, flags=re.M)
    if status and status.group(1).strip() in {"concluido", "concluído", "aprovado"}:
        if not re.search(r"^(?:aprovado_por|evidencia|evidência|commit_validacao):\s*\S+", meta, flags=re.M):
            findings.append({"arquivo":rel,"tipo":"REVISAR_EVIDENCIA", "detalhe":"Status final no frontmatter sem campo explícito de aprovação/evidência; confirmar manualmente."})
for code, files in sorted(ids.items()):
    if len(files)>1 and code not in {"RNC-AAAA-NNN", "GOS-XXX"}:
        findings.append({"arquivos":files,"tipo":"ID_DUPLICADO","detalhe":f"ID repetido: {code}"})
report={"verificacao":"AGT-X9 (regras determinísticas, sem IA)","gerado_em":datetime.now(timezone.utc).isoformat(),"documentos":len(notes),"alertas":findings,"limitacoes":["Não analisa verdade de afirmações nem conformidade semântica","Alertas exigem revisão humana/AGT-VAL","Nenhuma RNC criada automaticamente"]}
out=root/"x9-report.json"
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"X9: {len(notes)} documentos, {len(findings)} alertas indicativos")
for item in findings:
    print(item)
