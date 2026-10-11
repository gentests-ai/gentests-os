---
tipo: processo
id: GT-HANDOFF-001
versao: 0.1.0
status: proposta
responsavel: Governança
missao: GT-GOV-CHANGE-001
issue: https://github.com/gentestsai-sudo/gentests-os/issues/55
---
# GT-HANDOFF-001 — Encaminhamento de missões (PROPOSTA)

> **Não homologado:** este documento propõe um fluxo e não concede permissões, não altera contratos, não autoriza merge ou publicação. Parecer: [REV-GOV-CHANGE-001](https://github.com/gentestsai-sudo/gentests-os/issues/55#issuecomment-6111725634).

## Regra central
Toda etapa concluída, bloqueada ou devolvida exige **GT-HANDOFF-001 preenchido pelo agente remetente**. O **Orquestrador Central único** verifica prontidão e determina a rota; o destinatário confirma **ACEITO** ou **DEVOLVIDO**, com motivo. **A Direção não escolhe destinatários operacionais**, mas delibera sobre atos reservados. Até a automação da [[03-Processos/Despacho-Automatico-de-Agentes|issue #47]], a CEO atua apenas como gatilho/transporte manual da mensagem pronta, quando o canal exigir.

## Estados separados (não intercambiáveis)
- **Missão:** registrada → refinamento → pronta → em execução → aguardando verificação → correção / aguardando decisão → entrega autorizada → conferência final → encerrada; bloqueada ou cancelada com motivo e responsável.
- **Etapa:** proposta → despachada → aguardando aceite → aceita → em execução → concluída com evidência; devolvida ou bloqueada com dono e ação.
- **Eventos distintos:** texto preparado ≠ registro GitHub ≠ agente realmente acionado ≠ aceite de entrada ≠ aprovação técnica ≠ autorização Direção ≠ entrega ≠ encerramento.
- **Sem aprovação por silêncio:** falta de aceite gera acompanhamento do Orquestrador, nunca avanço tácito.

## Procedimento resumido
1. Orquestrador tria a issue canônica, confere DoR, referências, prioridade, arquivos/IDs/PRs concorrentes, responsável e permissão aplicável.
2. Orquestrador gera e registra despacho preenchido para o destinatário especializado conforme matriz aprovada; na ausência de rota, mantém ownership e resolve conflito.
3. Transporte/acionamento efetivo é verificado separadamente. Enquanto a automação #47 não existir, a Direção pode apenas encaminhar a mensagem pronta, sem redefinir rota.
4. Destinatário responde ACEITO/DEVOLVIDO. Em devolução informa requisito faltante, dono e próxima ação. Aceite não é parecer ou aprovação.
5. Especialista executa **apenas ações autorizadas**, registra resultados reais, testes executados/não executados, versões, evidências e riscos.
6. Especialista preenche retorno pelo [[07-Templates/GT-HANDOFF-001-TEMPLATE]] com próximo destinatário proposto. Orquestrador confirma rota e as verificações/decisões aplicáveis.
7. Só encerrar missão com DoD, evidências, aprovações expressas cabíveis, riscos residuais atribuídos e registro na issue.

## Interfaces de exemplo (a detalhar na correção focal)
| Origem | Próximo destino candidato | Entrada mínima | Retorno |
|---|---|---|---|
| Produto | UX/UI ou Engenharia | requisitos, critérios de aceite, restrições, issue | dúvida de requisito → Produto |
| Executor | QA, depois Revisor Independente quando exigido | commit/PR, escopo, evidências, testes e limitações | defeito → Executor |
| Marketing | revisão de conteúdo/marca, depois Comercial | artefato, guia de marca, canal, evidências | ajuste → Marketing; publicação só com autorização aplicável |

Estas rotas **não substituem POL-003 nem habilitação efetiva**: [[00-Constituicao/Matriz-de-Permissoes]]. QA, validação, auditoria e revisão independente não se substituem automaticamente.

## Bloqueios para implantação (REV-GOV-CHANGE-001)
- **REV-GOV-01:** reconciliar papel × ação × autoridade × incompatibilidades × substituto autorizado com issue #53, distinguindo regras escritas e permissões efetivas.
- **REV-GOV-02:** anexar tabela versionada de transições e eventos, incluindo indisponibilidade, aceite, devolução, timeout de acompanhamento, entrega parcial, múltiplas revisões e liberação de WIP.
- **REV-GOV-03:** provar gate de arquivos/IDs/PRs concorrentes com testes positivos/negativos, falso positivo, severidades, comando/commit/saídas.
- **REV-GOV-04–06:** exemplos detalhados de DoR/DoD, piloto com baseline real e teste de independência/substitutos por missão.
- **GT-WIP-001** e **Agile Coach** ainda são candidatos; nenhuma ativação por esta nota.

## Integração futura
A [issue #47](https://github.com/gentestsai-sudo/gentests-os/issues/47) poderá implementar transporte automático idempotente, confirmação de entrega e aceite, observabilidade e tratamento de falhas. Comentário na issue **não aciona** sozinho uma conversa de agente.

## Referências
- [Issue #55 — proposta da Governança](https://github.com/gentestsai-sudo/gentests-os/issues/55#issuecomment-6111681091)
- [Parecer independente e ressalvas](https://github.com/gentestsai-sudo/gentests-os/issues/55#issuecomment-6111725634)
- [[07-Templates/GT-HANDOFF-001-TEMPLATE]]
- [[02-Agentes/Indice-de-Agentes]]
