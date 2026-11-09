# 11 — Evidências e resultados da auditoria PIX

**Projeto:** SLOT-REVERSE-001 | **Missão:** 002 — Frente G  
**Status:** Registro aberto — sem evidências primárias anexadas  
**Issues:** G1 #152 · G2 #153

## 1. Regras de preservação
- Registrar origem, data/hora BRT, cenário PIX-00X, responsável e método de obtenção.
- Preservar original em local autorizado; anexar ao repositório somente cópia sanitizada.
- Mascarar nome, CPF/CNPJ, banco, agência, conta, chave PIX, QR payload, identificadores completos, cookies, tokens, protocolos privados e dados de terceiros.
- Não inserir comprovantes bancários integrais ou imagens contendo dados pessoais no repositório.
- Não editar a evidência original; registrar qualquer recorte/mascaramento aplicado.
- Não coletar nem armazenar credenciais, segredos ou payloads de autenticação.

## 2. Índice de evidências
| Evidência | Cenário | Frente | Data/hora BRT | Origem | Descrição | Sanitização | Referência |
|---|---|---|---|---|---|---|---|
| E-PIX-000 | PIX-001–010 | G1/G2 | 09/11/2026 | Abertura da investigação | Nenhuma evidência primária recebida até a criação do registro | N/A | Este documento |

## 3. Registro de resultados
| Cenário | Fato observado | Informação declarada | Hipótese | Não verificável / lacuna | Conclusão |
|---|---|---|---|---|---|
| PIX-001 | — | — | — | Regras e valores ainda não coletados | Pendente |
| PIX-002 | — | — | — | QR Code/beneficiário/validade não observados | Pendente |
| PIX-003 | — | — | — | Nenhum comprovante legítimo fornecido | Não coletado |
| PIX-004 | — | — | — | Confirmação não observada | Pendente |
| PIX-005 | — | — | — | Conciliação/crédito não verificados | Pendente |
| PIX-006 | — | — | — | Histórico não observado | Pendente |
| PIX-007 | — | — | — | Expiração natural/documentada não verificada | Pendente |
| PIX-008 | — | — | — | Cancelamento/estorno não verificados | Pendente |
| PIX-009 | — | — | — | Nenhuma divergência documentada | Pendente |
| PIX-010 | — | — | — | Atendimento não avaliado | Pendente |

## 4. Registro detalhado
Para cada evidência, incluir:
- ID e cenário;
- arquivo/URL ou referência controlada;
- autor/frente;
- timestamp BRT;
- método de coleta;
- descrição objetiva do que aparece;
- campos mascarados;
- integridade/proveniência conhecida;
- limitações e contexto;
- interpretação separada da observação.

## 5. Independência e revisão
G1 e G2 devem adicionar evidências de forma independente, identificando a autoria. Não substituir evidência de uma frente pela interpretação da outra. Após as coletas independentes, registrar revisão cruzada e eventuais divergências.

## 6. Estado atual
Nenhuma conclusão sobre liquidação, confirmação, crédito, duplicidade, estorno ou vulnerabilidade foi estabelecida. Este registro inicial não representa coleta em produção nem confirma qualquer comportamento do PGW.bet.

## 7. Tentativa inicial de observação pública (09/11/2026, BRT)
- **Referência:** E-PIX-001
- **Alvo:** `https://pgw13.com/?a=uq6igjhx` (URL previamente registrada na investigação).
- **Método:** tentativa de abertura por ferramenta de consulta pública, sem autenticação ou interação.
- **Resultado observado:** a ferramenta retornou erro interno de acesso e não disponibilizou conteúdo legível.
- **Classificação:** limitação de observabilidade da ferramenta; não é evidência de indisponibilidade do site, falha do fluxo PIX ou vulnerabilidade.
- **Dados de depósito:** nenhum; não houve login, solicitação de depósito, geração de QR Code ou operação financeira.
- **Fontes secundárias encontradas em busca:** resultados para domínios e marcas semelhantes (por exemplo, “WG BET”, “PGWIN” e “PGBET”) não foram atribuídos à PGW.bet, pois não demonstram vínculo com o alvo.
- **Conclusão:** coleta pública inicial inconclusiva. Para avançar, é necessária captura autorizada e sanitizada da interface correta, sem iniciar transação nem acessar endpoints privados.
