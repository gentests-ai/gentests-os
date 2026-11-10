---
tipo: processo
id: GT-HANDOFF-001
versao: 0.4.0
status: proposta-para-revisao
responsavel: Governança Documental
---
# GT-HANDOFF-001 — Conclusão de tarefa e transferência de responsabilidade (PROPOSTA v0.4.0)

> **Não homologado.** Esta versão corrige a proposta v0.3.0 integrada pela PR #155. Não altera contratos individuais, POL-003, permissões, runtime, hierarquia nem autoriza merge/deploy/publicação. A PR #155 permanece no histórico; esta é uma proposta corretiva posterior.

## 1. Objetivo e princípio

Padronizar dois eventos diferentes sem confundi-los:

- **HANDOFF DE CONCLUSÃO:** registra o resultado de uma tarefa delimitada. É obrigatório no encerramento da tarefa, mesmo sem troca de responsável. Não transfere ownership e não exige aceite fictício.
- **HANDOFF DE TRANSFERÊNCIA:** formaliza a passagem real da responsabilidade de uma tarefa/etapa para outro agente. Preserva os controles de rastreabilidade, transporte, recebimento, aceite e WIP do processo v0.2.2.

**Princípio normativo:** a conclusão registra o que foi entregue. A transferência estabelece quem passa a responder pela continuidade do trabalho. Uma coisa não substitui a outra.

A regra aplica-se aos agentes existentes e futuros, quando este processo for homologado e incorporado à hierarquia documental. A obrigação é por tarefa delimitada, não por commit, teste, checkpoint ou microatividade.

## 2. Modelo de estados: três dimensões independentes

Não reutilizar um único campo para representar tarefa, natureza do HANDOFF e transporte.

### 2.1 Estado da tarefa

| Estado | Significado |
|---|---|
| EM_ANDAMENTO | Trabalho ativo; ownership permanece com o responsável atual |
| CONCLUÍDA | Critérios de aceite da tarefa atendidos e evidenciados |
| BLOQUEADA | Impedimento material impede avançar a tarefa; registrar causa, dono e condição de desbloqueio |
| INTERROMPIDA | Execução cessou antes de atender os critérios, sem decisão de cancelamento |
| CANCELADA | Encerramento por decisão de autoridade competente, com motivo e impacto |

**TRANSFERIDA não é estado de conclusão da tarefa.** A transferência é um evento de ownership. Antes do aceite, a tarefa permanece EM_ANDAMENTO ou BLOQUEADA e o remetente continua responsável. Após ACEITO explícito, o responsável atual passa ao destinatário; a tarefa segue EM_ANDAMENTO ou BLOQUEADA conforme a condição real.

### 2.2 Natureza do HANDOFF

- CONCLUSÃO: registro final de tarefa, sem transferência de ownership.
- TRANSFERÊNCIA: evento de passagem real de responsabilidade, com destinatário identificado.

Um mesmo ciclo de trabalho pode ter um HANDOFF DE TRANSFERÊNCIA e, posteriormente, um HANDOFF DE CONCLUSÃO emitido pelo novo responsável. Não marcar a transferência como conclusão da tarefa.

### 2.3 Ciclo de vida do HANDOFF

| Estado | Significado |
|---|---|
| PREPARADO | Conteúdo redigido; ainda não registrado nem entregue |
| REGISTRADO | Evidência publicada no registro canônico; não prova transporte |
| ACIONADO | Mensagem enviada por canal autorizado; prova do envio registrada |
| RECEBIDO | Destinatário confirmou recebimento |
| ACEITO | Destinatário aceitou explicitamente a responsabilidade delimitada |
| DEVOLVIDO | Destinatário recusou/devolveu com motivo, lacuna e próxima ação |

Estados de transporte são aplicáveis a TRANSFERÊNCIA. Para CONCLUSÃO, registrar PREPARADO/REGISTRADO conforme o canal disponível; recebimento e aceite de transferência são N/A — não houve transferência de ownership. Nunca inferir entrega ou aceite a partir de comentário, label, silêncio ou presença do texto no GitHub.

## 3. Quando emitir

Emitir HANDOFF DE CONCLUSÃO quando a tarefa delimitada atingir um estado terminal: CONCLUÍDA, BLOQUEADA, INTERROMPIDA ou CANCELADA. Se a tarefa for repassada para continuidade, emitir HANDOFF DE TRANSFERÊNCIA; o remetente também pode registrar o resultado da sua própria etapa, mas não declarar a tarefa concluída se os critérios globais ainda não foram atendidos.

Não emitir HANDOFF integral a cada checkpoint, commit, teste, correção ou subtarefa interna enquanto a mesma tarefa permanece EM_ANDAMENTO. Atualizações intermediárias podem ser sintéticas e proporcionais, sem substituir o registro final.

A tarefa deve ter sido delimitada antes da execução por objetivo, escopo, entregável e critérios de aceite. Se a fronteira não estiver clara, o agente registra a ambiguidade e solicita definição ao responsável pela missão; não cria encerramentos artificiais.

## 4. Conteúdo obrigatório do HANDOFF DE CONCLUSÃO

Usar o template integral e preencher com dados reais:
1. Identificação da tarefa/missão, origem, responsável atual e destinatário/owner da missão.
2. Objetivo, escopo e critérios de aceite definidos para a tarefa.
3. Estado final da tarefa e da missão, em campos separados.
4. Trabalho efetivamente executado e não executado.
5. Arquivos, contratos, schemas, configurações, artefatos, commits, PRs e links afetados — ou declaração expressa de que nada foi alterado.
6. Testes/verificações realizados, ambiente/versão/commit, resultados e evidências.
7. Testes/verificações não realizados, motivo, consequência e responsável pela pendência.
8. Riscos residuais, bloqueios, dependências e restrições.
9. Próximo responsável, próxima ação concreta e condição objetiva para avançar.
10. Situação do registro: publicado, pendente ou indisponível, com justificativa.

Campos não aplicáveis recebem “N/A” com justificativa. Não inventar destinatário, commit, PR, teste, evidência, aceite, autorização ou resultado. Não incluir segredos ou dados sensíveis desnecessários.

## 5. Controles obrigatórios do HANDOFF DE TRANSFERÊNCIA

A modalidade de transferência **não reduz nem substitui** o modelo de rastreabilidade anterior. Preservar, no mínimo:

- Identificadores únicos: mission_id, task_id, execution_id, handoff_id, event_id e versão;
- data/hora ISO 8601 com fuso, ator/origem, destinatário e autoridade/owner da missão;
- objetivo, DoR, escopo, prioridade, critérios de aceite e fonte de autoridade;
- responsável atual, próximo responsável, ownership, estado da tarefa/etapa e transição proposta;
- artefatos, issue, PR, commit, versão-base, evidências e verificações;
- riscos, pendências, dependências, bloqueios e WIP;
- autorização e permissão efetiva por ato protegido;
- prova de acionamento/entrega, confirmação de recebimento e aceite explícito ACEITO ou devolução DEVOLVIDO;
- condição de continuidade, próxima ação e destino alternativo, quando aplicável.

O remetente mantém ownership até o destinatário aceitar explicitamente. Se não houver canal autorizado, produzir mensagem integral copiável e marcar acionamento/recebimento/aceite como PENDENTE. A mensagem preparada ou registrada no GitHub não libera WIP nem transfere responsabilidade.

### 5.1 Transições de transferência

1. PREPARADO → REGISTRADO: registrar evento no canal canônico.
2. REGISTRADO → ACIONADO: enviar por canal autorizado e guardar prova.
3. ACIONADO → RECEBIDO: confirmação verificável do destinatário.
4. RECEBIDO → ACEITO: declaração explícita do destinatário, com identidade e instante.
5. RECEBIDO → DEVOLVIDO: motivo, requisito faltante, responsável e próxima ação.
6. DEVOLVIDO → PREPARADO: corrigir a lacuna e gerar nova versão/evento, mantendo histórico.
7. Falha/silêncio: ownership permanece com remetente; registrar tentativa, impacto e escalonamento por exceção. Silêncio nunca é aceite.

O aceite transfere apenas a responsabilidade delimitada e não significa aprovação técnica, aceite de QA, autorização administrativa, merge, deploy ou encerramento da missão.

## 6. Ownership, autoridade e segregação

- Conclusão sem transferência: ownership não muda; aceite de transferência = N/A.
- Transferência real: ownership só muda após ACEITO explícito.
- Bloqueio: registrar responsável pelo bloqueio, condição de desbloqueio e atividades independentes que podem continuar.
- Pareceres de QA, Validação, Auditoria e Revisão Independente permanecem distintos.
- Roteamento não é autorização. Permissões efetivas e atos reservados continuam regidos por POL-003 e decisões válidas.
- O Scrum Master atua por exceção; não é destinatário obrigatório nem owner global.
- Conclusão de tarefa, conclusão de etapa, aprovação, integração e encerramento de missão são eventos distintos.

## 7. Registro e fonte canônica

Registrar o HANDOFF integral na issue/PR canônica ou no artefato de evidência indicado pela missão, quando houver permissão de escrita. Se não houver acesso/canal autorizado, entregar a mensagem integral pronta para copiar e declarar REGISTRO PENDENTE. GitHub é registro documental, não transporte automático entre chats nem ledger transacional de runtime.

## 8. Critérios de aceite desta proposta

- As duas modalidades estão separadas e não se substituem.
- Nenhum HANDOFF DE CONCLUSÃO altera ownership ou exige aceite de transferência.
- Toda transferência preserva identificadores, ownership, WIP, rastreabilidade, transporte e aceite explícito.
- Estados de tarefa, natureza do HANDOFF e ciclo de vida são dimensões independentes.
- TRANSFERIDA não mascara tarefa concluída nem antecipa ownership.
- Há critério objetivo para encerrar tarefa e evitar handoffs por checkpoint.
- Os contratos individuais foram inventariados e conflitos/necessidades de conciliação registrados.
- Runtime e enforcement são verificados separadamente; documentação não é prova de execução.

## 9. Estado de implementação

**DOCUMENTAL / PROPOSTA.** Esta PR corrige os artefatos de processo e template e inclui auditoria de compatibilidade. Não altera os contratos individuais nem implementa enforcement no runtime. A homologação depende de revisão por Governança, QA e autoridade competente, seguida da conciliação contratual e da validação técnica.

## Referências
- PR #155 — versão v0.3.0 integrada; correção proposta nesta PR.
- Base histórica recuperada: processo e template v0.2.2 no commit anterior à PR #155.
- [Índice de agentes](../02-Agentes/Indice-de-Agentes.md)
- [Arquitetura de agentes/runtime](../02-Agentes/Arquitetura-de-Agentes-Runtime-e-Governanca.md)
