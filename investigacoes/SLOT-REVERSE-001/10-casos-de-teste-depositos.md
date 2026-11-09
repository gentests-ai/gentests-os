# 10 — Casos de teste observacionais de depósitos PIX

**Projeto:** SLOT-REVERSE-001 | **Missão:** 002 — Frente G  
**Status:** Casos definidos; execução pendente de evidência autorizada  
**Ambiente:** produção real — sem transações experimentais

## Regras gerais
Os casos abaixo são roteiros de observação, não autorização para movimentar dinheiro. Não criar depósitos para testar, não pagar QR Code, não repetir pagamentos, não manipular valores, não provocar expiração/cancelamento, não usar contas de terceiros e não alterar tráfego. Utilizar apenas informação pública, registros preexistentes legitimamente disponíveis ou evidência voluntariamente fornecida e sanitizada pelo titular. Se a observação exigir ação financeira, interromper e marcar como não verificável nesta missão.

## Casos

| ID | Cenário / objetivo | Procedimento permitido | Evidência | Resultado esperado a verificar | Status |
|---|---|---|---|---|---|
| PIX-001 | Solicitação de depósito | Consultar regras/tela acessível sem concluir operação | Valor, regras e identificador mascarado, se exibido | Valor e condições coerentes com termos | Pendente |
| PIX-002 | QR Code gerado | Observar somente registro já existente/autorizado; não pagar | Valor, beneficiário e validade exibidos; payload ocultado | Dados apresentados claros e consistentes | Pendente |
| PIX-003 | Pagamento legítimo | Analisar comprovante de pagamento já ocorrido, fornecido voluntariamente e redigido | Comprovante bancário sanitizado | Valor, data e destinatário comparáveis à operação | Não coletado |
| PIX-004 | Confirmação | Observar estado de operação preexistente, sem induzir pagamento | Estado e timestamp da plataforma | Estado compatível com evidência disponível | Pendente |
| PIX-005 | Crédito | Comparar registro próprio preexistente de saldo, sem gerar nova transação | Antes/depois sanitizado, se disponível | Crédito corresponde à operação confirmada | Pendente |
| PIX-006 | Histórico | Consultar histórico próprio autorizado | Registro mascarado | Valor, estado e referência consistentes | Pendente |
| PIX-007 | Expiração | Consultar política/documentação ou ocorrência natural já expirada | Texto de validade e estado final | Expiração e mensagem coerentes com regra publicada | Pendente |
| PIX-008 | Cancelamento | Consultar política ou ocorrência já cancelada naturalmente | Estado, data e mensagem sanitizados | Cancelamento não contradiz pagamento/crédito | Pendente |
| PIX-009 | Divergência | Comparar evidências preexistentes de titularidade própria | Diferença documentada sem dados sensíveis | Divergência identificada e tratada sem inferência precipitada | Pendente |
| PIX-010 | Atendimento | Avaliar protocolo legítimo existente ou canal público, sem simular fraude | Resposta/protocolo redigido | Orientação rastreável e tratamento consistente | Pendente |

## Modelo de execução por caso
- Data/hora BRT:
- Agente/frente:
- Fonte e contexto:
- Pré-condições já existentes:
- Passos observacionais:
- Evidência (referência ao documento 11):
- Resultado observado:
- Classificação: fato / declaração / hipótese / não verificável
- Limitações:
- Conclusão: confirmado / inconclusivo / não reproduzido / não aplicável

## Critérios de interrupção
Interromper quando a próxima etapa exigir pagamento, autenticação não autorizada, acesso a dados de terceiros, endpoint privado, manipulação de requisição, engenharia social, bypass ou exposição de segredo. Registrar a lacuna sem tentar contorná-la.