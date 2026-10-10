---
tipo: procedimento
id: PRC-GOV-001
status: proposta
---
# Gestão de incidentes de IA

## Gatilhos
Fatos inventados, violação de marca, envio sem autorização, acesso inadequado, ação destrutiva, inconsistências em registros ou descumprimento de políticas.

## Severidade
- **S1 — Baixa:** erro em rascunho sem impacto externo. Corrigir e registrar lição.
- **S2 — Média:** reincidência ou erro externo reversível. Suspender execução autônoma da operação afetada; exigir revisão.
- **S3 — Alta:** exposição de dados, comprometimento financeiro, fraude, ação irreversível ou envio não autorizado de alto impacto. Bloquear acesso **via administrador humano**, preservar evidências e conduzir investigação.

## Resposta
1. Conter risco conforme permissões reais disponíveis.
2. Preservar fatos e registros imutáveis quando possível.
3. Verificar impacto, destinatários e clientes envolvidos.
4. Identificar causa, política aplicável e controles falhos.
5. Definir correção, responsável, prazo e teste de regressão.
6. Reabrir autonomia apenas após validação humana.

Modelo: [[07-Templates/Incidente-TEMPLATE]]
