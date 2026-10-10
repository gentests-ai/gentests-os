#!/usr/bin/env python3
"""Pré-checagem técnica de rascunhos. Não substitui AGT-VAL nem aprovação humana."""
import json
import re
import sys
from pathlib import Path

REQUIRED = ("id", "tipo", "risco", "status", "assunto", "corpo", "origem_destinatario", "fontes", "versao", "responsavel")
CLAIM = re.compile(r"(?:\b\d+(?:[.,]\d+)?\s*%|\bgarant(?:imos|ia|ido)|\b(?:triplicamos|dobramos))", re.IGNORECASE)

def validate(data):
    issues = []
    for key in REQUIRED:
        if not data.get(key):
            issues.append(f"Campo obrigatório ausente: {key}")
    if data.get("tipo") != "email_comercial":
        issues.append("Tipo incompatível")
    if data.get("risco") not in {"QG-M", "QG-H"}:
        issues.append("Email externo exige no mínimo QG-M")
    if data.get("enviado"):
        issues.append("Piloto não admite envio")
    if data.get("aprovacao_envio"):
        issues.append("Piloto não admite registrar aprovação de envio")
    if CLAIM.search(data.get("corpo", "")) and not data.get("evidencias_alegacoes"):
        issues.append("Alegação quantitativa ou garantia sem evidência específica")
    return issues

if __name__ == "__main__":
    path = Path(sys.argv[1])
    data = json.loads(path.read_text(encoding="utf-8"))
    errors = validate(data)
    print(json.dumps({"artefato": data.get("id"), "prechecagem": "PENDENTE" if errors else "SEM_BLOQUEIOS_TECNICOS", "observacoes": errors, "aprovado": False}, ensure_ascii=False, indent=2))
    sys.exit(bool(errors))
