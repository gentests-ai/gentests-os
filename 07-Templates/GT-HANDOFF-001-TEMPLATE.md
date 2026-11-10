---
tipo: template
id: GT-HANDOFF-001
versao: 0.3.0
status: proposta
missao: GT-GOV-CHANGE-001
---
# GT-HANDOFF-001 — Modelo obrigatório de conclusão de tarefa e transferência (PROPOSTA v0.3.0)

> Não homologado, não concede permissão, não cria acionamento e não autoriza merge. `tipo: template` diferencia este artefato do `tipo: processo` com o mesmo ID. [Processo proposto](../03-Processos/Encaminhamento-de-Missoes-GT-HANDOFF-001.md) · [issue #55](https://github.com/gentestsai-sudo/gentests-os/issues/55) · [REV-02](https://github.com/gentestsai-sudo/gentests-os/issues/55#issuecomment-6111890108).

**Uso:** preencher dados reais; para campo condicional não pertinente, `N/A — [motivo]`. **Não** declarar verificado, entregue, aceito ou autorizado por presunção. Este formulário de trabalho é referência; a seção final **precisa ser substituída por mensagem integral sem placeholders no envio efetivo**.

## Adaptação proposta #86 — handoff direto e evidência reutilizável

**Diretriz de fluxo:** o remetente identifica diretamente o especialista competente conforme missão, contrato, autorização e acesso efetivo. Não existe confirmação por Orquestrador Central. O Scrum Master só é envolvido por exceção diante de impedimento, atraso, falha, conflito ou ping-pong; não recebe ciência rotineira nem mantém visão/ownership global.

**Antes de pedir dados novamente**, referenciar evidência da própria issue (link, tipo: relato/captura/API/teste, data, alcance, validade e gatilho de rechecagem). Se insuficiente, declarar apenas o campo faltante, motivo e ato específico bloqueado, deixando outras etapas avançarem. Não equiparar budget US$0 a custo futuro garantido. Acionamento, entrega, aceite e execução exigem provas independentes mesmo em handoff direto.

## 1. Identidade e owners
- **mission_id:** [ID]; **handoff_id:** [ID único]; **event_id:** [ID do evento]; **version:** [versão deste evento/handoff].
- **Instante ISO8601/fuso:** [AAAA-MM-DDTHH:MM:SS-03:00]; **origem/ator:** [identidade real]; **tipo:** [execução/QA/etc.]; **prioridade:** [valor].
- **Rota:** [horizontal autorizada / exceção operacional ao Scrum Master]; **destino definido pelo remetente:** [papel, competência e fundamento]; **intervenção do Scrum Master:** [N/A ou ocorrência comprovada].
- **Responsável atual:** [identidade e função]; **próximo responsável:** [identidade/função ou PENDENTE]; **responsável pelo bloqueio:** [identidade ou N/A com motivo].
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
- **Critério de liberação:** evidências completas + entrega comprovada e ACEITO expresso do próximo especialista + nenhum retrabalho ativo; [provas]. Não há assunção de fila pelo Scrum Master nem aceite presumido.
- **Atenção:** a atribuição de responsável por bloqueio não implica aceite do próximo especialista; regra GT-WIP-001 ainda é proposta.
- **Próximo responsável e ação inequívoca:** [papel, entrega, critério de aceite].
- **Destino alternativo:** [identidade habilitada e condição, ou BLOQUEADO].
- **Atuação do Scrum Master:** [N/A ou exceção, evidência, tentativas e resultado].
- **Ação solicitada à Direção:** [decisão reservada especificada / N/A].
- **Condição para avançar:** [evidência futura]; **condição para encerrar missão:** [todas as etapas e autorizações demonstradas].

## 6. Checklist de saída
- [ ] Identidade de evento/handoff, versão, instante, owners, estados e links reais completos.
- [ ] Rota horizontal autorizada; entrega e ACEITO comprovados ou PENDENTE, sem confirmação fictícia por agente central.
- [ ] DoR/DoD e cada autorização por ação conferidos; sem permissão inferida.
- [ ] Resultados, comandos/exit codes e verificações não realizadas declarados.
- [ ] QA, Validação, Auditoria e Revisão Independente tratados distintamente; conflito/substituto e dispensa registrados.
- [ ] WIP e bloqueios com donos; etapa não confundida com missão encerrada.
- [ ] **Mensagem final integral, endereçada, preenchida e copiável**, sem placeholders ou links isolados, incluída.
- [ ] Parecer relevante registrado na issue canônica para os responsáveis e verificadores pertinentes; sem destinatário central obrigatório.

## 7. Registro final obrigatório — mensagem integral pronta para copiar

**Obrigatório para qualquer agente, dos 14 papéis catalogados ou futuro, ao concluir, bloquear, interromper, cancelar ou transferir uma tarefa delimitada.** O relatório de conclusão não implica mudança de ownership. Não emitir a cada checkpoint ou passo interno enquanto a tarefa continua em execução.

- Em CONCLUSÃO/BLOCKED/INTERROMPIDA/CANCELADA, preencher o modelo e indicar destinatário como responsável pela missão/owner da issue; aceite de transferência = N/A — sem transferência de ownership.
- Em TRANSFERÊNCIA, identificar o próximo agente competente e manter as exigências de transporte comprovado e aceite explícito ACEITO/DEVOLVIDO.
- Separar estado da tarefa, estado da etapa e estado da missão. Concluir uma tarefa não significa concluir a missão, aprovar qualidade, autorizar merge ou efetuar deploy.
- Substituir todos os campos por dados reais. Campos não aplicáveis devem conter N/A e justificativa. Não deixar colchetes, inventar evidências ou declarar testes não executados como aprovados.

### 7.1 Modelo integral

```markdown
HANDOFF — [MISSÃO / TAREFA]

[Natureza: CONCLUSÃO | BLOCKED | INTERROMPIDA | CANCELADA | TRANSFERÊNCIA]

Origem: [AGENTE / ID]
Destinatário: [PRÓXIMO AGENTE OU OWNER DA MISSÃO]
Ciência: [PAPÉIS PERTINENTES OU N/A]
Projeto: [IDENTIFICADOR]
Repositório: [OWNER/REPO OU N/A]
Issue: [NÚMERO/LINK OU N/A]
PR: [NÚMERO/TÍTULO OU N/A]
Commit de referência: [SHA OU N/A]
Entregável: [ARTEFATO/VERSÃO]
Prioridade: [VALOR]
Estado da tarefa: [CONCLUÍDA / BLOCKED / INTERROMPIDA / CANCELADA]
Estado da missão: [ESTADO REAL, SEM INFERIR ENCERRAMENTO]

⸻

1. CONTEXTO E OBJETIVO

[Objetivo, escopo, critérios de aceite e contexto necessário.]

2. TRABALHO EXECUTADO

[O que foi efetivamente realizado, decisões tomadas e resultado observado.]

3. ARTEFATOS E ALTERAÇÕES

[Arquivos, contratos, schemas, configurações, documentos, código, links, commits e PRs afetados. Declarar expressamente quando nada foi alterado.]

4. VALIDAÇÃO E EVIDÊNCIAS

[Testes/verificações realizados, ambiente/versão/commit, resultado e links de evidência. Informar testes não realizados e motivo.]

5. PENDÊNCIAS, LIMITES E RISCOS

[O que ficou pendente, riscos residuais, dependências, restrições e responsável por cada item.]

6. ESTADO FINAL

[Estado da tarefa e da etapa. Diferenciar entrega produzida, validação, aprovação, integração e encerramento da missão.]

7. PRÓXIMA AÇÃO

Responsável: [AGENTE/OWNER OU N/A]
Ação: [PRÓXIMA AÇÃO CONCRETA OU N/A]
Condição para avançar: [CRITÉRIO/EVIDÊNCIA]
Condição para encerrar a missão: [CRITÉRIOS/GATES PENDENTES]

8. TRANSFERÊNCIA E ACEITE

[Se houver transferência: destinatário, canal, prova de entrega e estado ACEITO/DEVOLVIDO/AGUARDANDO.
Se não houver: N/A — não houve transferência de ownership; o responsável permanece [IDENTIDADE].]

REGISTRO: [LINK DO REGISTRO CANÔNICO OU PENDENTE — MOTIVO]
PRÓXIMA AÇÃO FORMAL: [AÇÃO E RESPONSÁVEL]

Fim do handoff — [AGENTE DE ORIGEM].
```

### 7.2 Regra de aceite

O destinatário só responde ACEITO ou DEVOLVIDO quando houver transferência real. No relatório de conclusão sem transferência, não se exige aceite fictício; o registro é dirigido ao owner da missão e preserva o estado real. Silêncio nunca é aceite.

## Modelo enxuto de transferência operacional — proposta #53

Para rotas simples já autorizadas, a mensagem abaixo pode ser usada como aviso de transporte ou resumo de encaminhamento. **Ela não substitui o registro final integral obrigatório da seção 7**, inclusive quando a tarefa termina em transferência. Campos do modelo integral não aplicáveis recebem N/A justificado; não se dispensa a rastreabilidade. Até homologação, esta é proposta documental, não cria canal de transporte ou permissão.

```markdown
**Destino:** [agente competente] | **Missão:** [issue canônica]
**Objetivo e ação:** [entrega concreta solicitada]
**Autorização vigente:** [referência, escopo e limites]
**Evidências:** [PR/SHA/testes e ressalvas pertinentes]
**Responsável e próximo passo:** [dono, critério de aceite]
**Transporte/aceite:** [comprovado com evidência ou pendente; nunca presumido]
**Risco/gate:** [bloqueio material ou nenhum identificado]
```

Os registros canônicos ficam disponíveis aos responsáveis e verificadores pertinentes; não há ciência ou despacho central obrigatório. Ação ordinária já coberta não exige reaprovação. Revisões independentes e operações protegidas mantêm seus gates.
