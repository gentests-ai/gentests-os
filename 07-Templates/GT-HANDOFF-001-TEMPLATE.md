---
tipo: template
id: GT-HANDOFF-001
versao: 0.2.1
status: proposta
missao: GT-GOV-CHANGE-001
---
# GT-HANDOFF-001 — Modelo de despacho e retorno (PROPOSTA v0.2.1)

> Não homologado, não concede permissão, não cria acionamento e não autoriza merge. `tipo: template` diferencia este artefato do `tipo: processo` com o mesmo ID. [Processo proposto](../03-Processos/Encaminhamento-de-Missoes-GT-HANDOFF-001.md) · [issue #55](https://github.com/gentestsai-sudo/gentests-os/issues/55) · [REV-02](https://github.com/gentestsai-sudo/gentests-os/issues/55#issuecomment-6111890108).

**Uso:** preencher dados reais; para campo condicional não pertinente, `N/A — [motivo]`. **Não** declarar verificado, entregue, aceito ou autorizado por presunção. Este formulário de trabalho é referência; a seção final **precisa ser substituída por mensagem integral sem placeholders no envio efetivo**.

## Adaptação proposta #86 — handoff direto e evidência reutilizável

**Pendente de homologação:** o remetente especialista poderá apontar como destino diretamente outro especialista competente, se a missão, o contrato, a autorização e o acesso efetivo permitirem; não declarar 'destino confirmado pelo Orquestrador' quando não ocorreu. Identificar **rota direta autorizada** ou **rota com ORQ por exceção**, com fundamento/link. ORQ mantém visão consolidada na issue, sem retransmissão obrigatória.

**Antes de pedir dados novamente**, referenciar evidência da própria issue (link, tipo: relato/captura/API/teste, data, alcance, validade e gatilho de rechecagem). Se insuficiente, declarar apenas o campo faltante, motivo e ato específico bloqueado, deixando outras etapas avançarem. Não equiparar budget US$0 a custo futuro garantido. Acionamento, entrega, aceite e execução exigem provas independentes mesmo em handoff direto.

## 1. Identidade e owners
- **mission_id:** [ID]; **handoff_id:** [ID único]; **event_id:** [ID do evento]; **version:** [versão deste evento/handoff].
- **Instante ISO8601/fuso:** [AAAA-MM-DDTHH:MM:SS-03:00]; **origem/ator:** [identidade real]; **tipo:** [execução/QA/etc.]; **prioridade:** [valor].
- **Rota:** [horizontal autorizada / ORQ por exceção]; **destino definido pelo remetente:** [papel, competência e fundamento]; **confirmação pelo ORQ:** [N/A em rota horizontal / intervenção comprovada].
- **Responsável atual:** [identidade e função]; **próximo responsável:** [identidade/função ou PENDENTE]; **owner de bloqueio/fila:** [identidade ou N/A com motivo].
- **Estado da missão:** [estado]; **estado da etapa:** [estado]; **transição anterior → seguinte:** [estados ou PENDENTE].
- **Issue canônica:** [URL]; **PR/commit/artefato/versão-base:** [links/SHA ou N/A justificado].

## 2. Transporte, recebimento e aceite — registros distintos
| Marco | Estado | Evidência / instante / responsável |
|---|---|---|
| Mensagem preparada | SIM/NÃO/PENDENTE | [conteúdo e ator] |
| Registrada no GitHub | SIM/NÃO/PENDENTE | [link do evento; não presume acionamento] |
| Acionamento/entrega efetiva | COMPROVADO/NÃO/PENDENTE/ERRO | [canal, prova e instante] |
| Recebida pelo destinatário | CONFIRMADO/NÃO/PENDENTE | [identidade/evidência] |
| Aceite de entrada | **ACEITO / DEVOLVIDO / AGUARDANDO** | [declaração explícita, identidade, hora/link] |

**Devolução:** [motivo, requisito, dono, próxima ação, prazo se definido]. **Erro/silêncio:** [tentativa, dono da recuperação/escalonamento e prova]; nunca inferir aceite. Aceite de entrada não aprova mérito.

## 3. Objetivo, DoR, escopo e decisão
- **Objetivo observável:** [resultado esperado].
- **DoR:** [requisitos, fontes canônicas, critérios verificáveis, dependências, condição de bloqueio].
- **Ações autorizadas individualmente:** [ação → autoridade competente → registro/prova → escopo/limite/validade].
- **Ações proibidas:** [restrições]; **permissão efetiva confirmada?:** [SIM + evidência / NÃO / NÃO VERIFICADO].
- **Fonte de autoridade:** POL-003, delegação válida e permissão real; [issue #53](https://github.com/gentestsai-sudo/gentests-os/issues/53) ainda não concede novos poderes.
- **Concorrência:** [arquivos, IDs canônicos, PRs/heads, owner de integração, impacto, bloqueio/aviso ou N/A justificado].
- **Ação reservada à Direção:** [objeto/decisão expressa necessária e evidência ou N/A justificado].

## 4. Resultado, verificações e DoD
- **Resultado real:** [PENDENTE DE EXECUÇÃO no despacho / entregas concretas no retorno]; **commits/artefatos:** [SHA/URL].
- **Testes feitos:** [comando, ambiente, SHA, saída, exit code e evidência de cada teste; ou NENHUM — motivo].
- **Testes não feitos:** [teste, motivo, consequência e dono; N/A justificado somente se cabível].
- **QA:** [identidade, parecer/evidência/status ou N/A justificado]; **Validação:** [idem]; **Auditoria:** [idem]; **Revisão Independente:** [idem].
- **Dispensas de verificações obrigatórias:** [qual gate, quem autorizou, justificativa, evidência; ou N/A].
- **Independência:** [author_id, executor_id, qa_id, validator_id, auditor_id, reviewer_id, approver_id; conflitos de identidade/participação e habilitação efetiva].
- **Substituição:** [substituto, competência/permissão, independência, motivo e aprovação válida; ou N/A].
- **Bloqueios/risco residual:** [causa, impacto, owner e próxima ação; ou N/A justificado].
- **DoD etapa:** [critérios e evidências]; **DoD missão:** [gates ainda pendentes, decisão, integração real, encerramento ou NÃO ENCERRADA].

## 5. WIP, transferência e destino seguinte
- **WIP do executor:** [ativo / candidato à liberação / liberado, com evidência].
- **Critério de liberação:** evidências completas + entrega e ACEITO expressos do próximo agente, ou assunção excepcional de fila pelo ORQ sem aceite fictício + nenhum retrabalho ativo; [provas].
- **Atenção:** fila assumida não implica aceite do próximo especialista; regra GT-WIP-001 ainda é proposta.
- **Próximo responsável e ação inequívoca:** [papel, entrega, critério de aceite].
- **Destino alternativo:** [identidade habilitada e condição, ou BLOQUEADO].
- **Ciência rastreável do ORQ:** [parecer/evento na issue; notificação, leitura e incorporação somente quando comprovadas]; sem retransmissão obrigatória por rotina.
- **Ação solicitada à Direção:** [somente transporte manual / decisão especificada / N/A].
- **Condição para avançar:** [evidência futura]; **condição para encerrar missão:** [todas as etapas e autorizações demonstradas].

## 6. Checklist de saída
- [ ] Identidade de evento/handoff, versão, instante, owners, estados e links reais completos.
- [ ] Rota direta autorizada ou exceção fundamentada; entrega e ACEITO comprovados ou PENDENTE, sem confirmação fictícia pelo ORQ.
- [ ] DoR/DoD e cada autorização por ação conferidos; sem permissão inferida.
- [ ] Resultados, comandos/exit codes e verificações não realizadas declarados.
- [ ] QA, Validação, Auditoria e Revisão Independente tratados distintamente; conflito/substituto e dispensa registrados.
- [ ] WIP e bloqueios com donos; etapa não confundida com missão encerrada.
- [ ] **Mensagem final integral, endereçada, preenchida e copiável**, sem placeholders ou links isolados, incluída.
- [ ] Parecer relevante disponível ao ORQ na issue; prestação de contas exclusiva ao ORQ somente quando não houver destinatário operacional seguinte.

## 7. GT-HANDOFF-001 — Mensagem final integral pronta para copiar (OBRIGATÓRIA)

**Na emissão efetiva, substituir todo o bloco abaixo por dados verdadeiros e uma mensagem única, sem colchetes de preenchimento.** Na conversa, preferir bloco de escrita copiável ou um único bloco de código Markdown; em GitHub/Obsidian publicar o texto integral selecionável. Um resumo, tabela ou link **não** satisfaz o DoD. O remetente não atribui ACEITO nem entrega a terceiro sem prova.

```markdown
# GT-HANDOFF-001 — MENSAGEM PRONTA PARA ENCAMINHAR
**DESTINO:** [AGENTE DESTINATÁRIO CONFIRMADO]
**AÇÃO:** [EXECUTAR OU ACEITAR/DEVOLVER ESTA SOLICITAÇÃO]
**Missão:** [mission_id] | **Handoff:** [handoff_id] | **Evento/versão:** [event_id / version]
**Origem:** [ator] | **Data/hora/fuso:** [timestamp]
**Rota:** [direta autorizada / ORQ por exceção] | **Destino:** [especialista e competência]
**Responsável atual/próximo:** [donos] | **Prioridade:** [prioridade]
**Missão:** [estado] | **Etapa:** [estado e transição]
**Preparado/registrado/acionado/recebido/aceito:** [cinco estados distintos, evidências ou PENDENTE]
**Issue, PR, commit e fontes:** [referências reais]
## Objetivo e DoR
[resultado específico, insumos conferidos, lacunas e dependências]
## Escopo e autoridade
[atos permitidos e prova de cada autorização; ações vedadas; POL-003/#53 se relevante]
## Entregáveis, execução e verificações
[resultados reais ou PENDENTE; testes feitos com resultado/exit code e não feitos com motivo; QA, validação, auditoria e revisão independentes e dispensas]
## Riscos, ownership e WIP
[bloqueios/donos/ação, conflitos/substituições, transferência e condição de liberar WIP]
## DoD e próximo passo
[condição observável de conclusão, próxima ação, responsável, alternativa, retorno, decisões reservadas e condição real para encerrar a missão]
**Aceite requerido:** responder ACEITO ou DEVOLVIDO com motivo e evidência. Não presumir acionamento nem aceite.
```

**Regra horizontal:** remetente e destinatário seguem diretamente conforme autoridade vigente; ORQ acompanha pareceres pela issue e intervém por exceção. Novo despacho do ORQ é exigido apenas quando ele assume efetivamente o encaminhamento. **Exceção justificada:** quando não houver próxima especialidade, a mensagem integral pode limitar-se à prestação de contas/endereço Orquestrador, explicitando por que não há despacho operacional seguinte. Na fase manual, Direção só transporta o texto, não redige nem escolhe destino.

**Referências:** [[03-Processos/Encaminhamento-de-Missoes-GT-HANDOFF-001]] · [issue #55](https://github.com/gentestsai-sudo/gentests-os/issues/55).

## Modelo enxuto de transferência operacional — proposta #53

Para rotas simples já autorizadas, preferir **uma mensagem única**, sem preencher todos os campos do modelo extensivo. O formato abaixo substitui a obrigatoriedade operacional de reproduzir o formulário completo; utilizar campos adicionais apenas por risco ou gate aplicável. Até homologação, esta é proposta de simplificação, não dispensa de controle vigente.

```markdown
**Destino:** [agente competente] | **Missão:** [issue canônica]
**Objetivo e ação:** [entrega concreta solicitada]
**Autorização vigente:** [referência, escopo e limites]
**Evidências:** [PR/SHA/testes e ressalvas pertinentes]
**Responsável e próximo passo:** [dono, critério de aceite]
**Transporte/aceite:** [comprovado com evidência ou pendente; nunca presumido]
**Risco/gate:** [bloqueio material ou nenhum identificado]
```

A ciência do Orquestrador ocorre pelo registro canônico; não requer novo despacho. Ação ordinária já coberta não exige reaprovação. Revisões independentes e operações protegidas mantêm seus gates.
