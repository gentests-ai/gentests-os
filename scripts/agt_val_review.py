#!/usr/bin/env python3
"""AGT-VAL v0.2: parecer preliminar explicável. Sem IA externa, sem envios e sem aprovação."""
import json
import re
import sys
from pathlib import Path
from scripts.validate_commercial_email import validate

ROOT = Path(__file__).resolve().parents[1]
CLAIMS = re.compile(r"\b(?:\d+(?:[.,]\d+)?\s*%|garantimos|garantia|certificado|certificação|clientes atendidos|case comprovado)\b", re.I)
DANGEROUS = re.compile(r"\b(?:senha|password|token|api[_ -]?key|secret)\s*[:=]\s*\S+", re.I)

def review(data):
    findings = []
    def add(code, severity, description, evidence):
        findings.append({"id":code,"severidade":severity,"descricao":description,"evidencia":evidence})
    for issue in validate(data):
        add("QG-ESTRUTURA","alta",issue,"pré-validação técnica")
    body = str(data.get("corpo",""))
    if DANGEROUS.search(body):
        add("QG-SEGREDO","critica","Possível segredo no corpo do e-mail","detector heurístico, exige revisão")
    if CLAIMS.search(body) and not data.get("evidencias_alegacoes"):
        add("QG-ALEGACAO","alta","Alegação de resultado ou credencial exige comprovação","trecho suspeito no corpo")
    if not data.get("assinatura_arquivo_oficial"):
        add("QG-MARCA","media","Arquivo oficial da assinatura não identificado","registro de ativos da marca")
    if data.get("assinatura_arquivo_oficial") and not data.get("evidencia_renderizacao"):
        add("QG-RENDER","media","Renderização da assinatura não comprovada","falta evidência de teste visual")
    if not data.get("revisao_semantica_independente"):
        add("QG-SEMANTICA","media","Alinhamento à missão, visão e valores ainda não revisado","revisão independente pendente")
    critical = any(f["severidade"]=="critica" for f in findings)
    return {
      "id_artefato":data.get("id"),"versao":data.get("versao"),"classificacao":data.get("risco"),
      "agente":"AGT-VAL (pré-revisão determinística v0.2)",
      "resultado":"BLOQUEADO" if critical else "CORRECAO_NECESSARIA" if findings else "NAO_VERIFICAVEL",
      "achados":findings,
      "autorizacao_humana":"PENDENTE",
      "pode_enviar":False,
      "limitacoes":["Não é revisão semântica por IA","Não prova fidelidade visual de assinaturas","Não atesta fonte por mera presença de URL","Nunca autoriza envio"]
    }

if __name__=="__main__":
    item=json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(json.dumps(review(item),ensure_ascii=False,indent=2))
    # Falhas no conteúdo geram diagnóstico; sem falhas, o parecer continua não verificável.
    sys.exit(1 if any(x["severidade"] in ("critica","alta") for x in review(item)["achados"]) else 0)
