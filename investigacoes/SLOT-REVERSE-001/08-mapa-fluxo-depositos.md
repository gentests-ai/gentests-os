# 08 — Mapa do fluxo de depósitos PIX

**Projeto:** SLOT-REVERSE-001  
**Missão:** 002 — Frente G  
**Sistema declarado:** PGW.bet  
**Modalidade:** PIX  
**Ambiente:** produção — investigação exclusivamente observacional  
**Status:** INICIAL — fluxo ainda não observado  
**Frentes:** G1/AGT-AUD (#152) e G2/AGT-ENG (#153)  
**Data de abertura:** 09/11/2026 (BRT)

## 1. Objetivo e regra de evidência
Mapear a jornada desde a solicitação de depósito até a apresentação do estado final, histórico e saldo. Este documento é um mapa de coleta, não uma afirmação de que o fluxo interno foi observado. Distinguir sempre:
- **Fato observado:** evidência direta, com origem e data.
- **Informação declarada:** texto de interface/termo/atendimento, sem validação independente.
- **Hipótese:** explicação ainda não comprovada.
- **Não verificável:** depende de backend, banco, PSP ou registro não acessível.

## 2. Fluxo lógico a investigar
Solicitação de depósito → apresentação de valor/instruções → geração e exibição do QR Code/copia-e-cola → eventual pagamento no banco do titular → confirmação pelo arranjo/PSP → atualização do estado na plataforma → eventual crédito no saldo → registro no histórico/comprovante.

**Atenção:** esta sequência é um modelo de investigação. Não confirma que a PGW.bet usa essa arquitetura, esse provedor ou esses estados. O fluxo real deve ser preenchido apenas com evidência.

## 3. Pontos de observação

| Etapa | Pergunta | Evidência aceitável | Estado |
|---|---|---|---|
| Solicitação | Quais valores e regras são apresentados? | Termos/tela pública autorizada, data e contexto | Não observado |
| QR Code | Qual valor, beneficiário e validade são exibidos? | Tela sanitizada; não compartilhar payload integral | Não observado |
| Pagamento | Existe comprovante legítimo já disponível do titular? | Comprovante redigido, somente se fornecido voluntariamente | Não coletado |
| Confirmação | Que estado a plataforma apresenta? | Captura sanitizada e timestamp | Não observado |
| Crédito | Há evidência de saldo antes/depois sem nova operação? | Registro próprio autorizado, sem induzir transação | Não observado |
| Histórico | O registro corresponde à operação? | Histórico sanitizado | Não observado |
| Expiração/cancelamento | Que estado final é exibido? | Termos ou ocorrência natural já existente | Não observado |
| Atendimento | Como uma ocorrência legítima é tratada? | Protocolo/resposta com dados pessoais removidos | Não observado |

## 4. Matriz obrigatória
| ID | Cenário | Responsável primário | Estado inicial |
|---|---|---|---|
| PIX-001 | Solicitação de depósito | AGT-AUD + AGT-ENG | Não observado |
| PIX-002 | QR Code gerado | AGT-AUD + AGT-ENG | Não observado |
| PIX-003 | Pagamento legítimo | AGT-AUD | Não coletado; sem pagamento experimental |
| PIX-004 | Confirmação | AGT-AUD + AGT-ENG | Não observado |
| PIX-005 | Crédito | AGT-AUD + AGT-ENG | Não observado |
| PIX-006 | Histórico | AGT-AUD + AGT-ENG | Não observado |
| PIX-007 | Expiração | AGT-AUD + AGT-ENG | Não observado |
| PIX-008 | Cancelamento | AGT-AUD + AGT-ENG | Não observado |
| PIX-009 | Divergência | AGT-AUD | Não observada |
| PIX-010 | Atendimento | AGT-AUD | Não coletado |

## 5. Limites
Nenhum pagamento experimental, repetido ou manipulado; nenhuma tentativa de gerar crédito sem pagamento; nenhuma falsificação; nenhuma conta de terceiro; nenhuma chamada manual a endpoint privado; nenhuma alteração de requisição ou notificação; nenhum bypass. Não provocar expiração, duplicidade ou falha. Não registrar QR payloads, tokens, dados bancários ou identificadores completos.

## 6. Registro de atualização
Cada inclusão deve indicar autor/frente, data/hora BRT, cenário PIX, fonte, evidência sanitizada, classificação e limitações. G1 e G2 devem registrar suas observações independentemente; divergências permanecem abertas até revisão cruzada.

## 7. Estado atual
Não há, neste registro inicial, evidência primária de depósito PIX, beneficiário, PSP, taxas, limites, validade de QR Code, confirmação, crédito ou estorno. Nenhuma vulnerabilidade foi confirmada.