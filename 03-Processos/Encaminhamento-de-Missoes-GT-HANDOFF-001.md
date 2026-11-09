---
tipo: processo
id: GT-HANDOFF-001
versao: 0.2.2
status: proposta
responsavel: Governança
missao: GT-GOV-CHANGE-001
issue: https://github.com/gentestsai-sudo/gentests-os/issues/55
---
# GT-HANDOFF-001 — Encaminhamento de missões (PROPOSTA v0.2.2)

> **Não homologado.** Este desenho não concede acessos, não altera POL-003, contratos ou hierarquia, não autoriza merge, publicação, piloto, GT-WIP-001, Agile Coach ou automação #47. Base: [Governança v0.2.0](https://github.com/gentestsai-sudo/gentests-os/issues/55#issuecomment-6111790899) e [REV-GOV-CHANGE-002](https://github.com/gentestsai-sudo/gentests-os/issues/55#issuecomment-6111890108).

## Proposta focal #86 — roteamento federado e reuso de evidências (pendente de homologação)

**Diretriz arquitetural da Direção:** não existe Orquestrador Central. Dentro da missão, do escopo autorizado e das permissões efetivas, especialistas encaminham diretamente ao próximo especialista competente e registram o evento na issue canônica. O responsável atual conserva a responsabilidade até a entrega ser comprovada e o destinatário aceitar explicitamente. O Scrum Master observa o fluxo e atua somente por exceção — impedimento, atraso, falha, ping-pong, conflito ou ausência de progresso — sem ownership global, fila central, triagem universal ou despacho obrigatório. Esta proposta documental não cria privilégios nem altera POL-003.

**Transições distintas:** preparar, registrar, entregar de fato, receber, ACEITAR, executar, validar, autorizar, integrar e encerrar. GitHub não entrega mensagem automaticamente a outro chat ChatGPT; sem canal operacional efetivo, fornecer mensagem integral copiável e registrar entrega/aceite como PENDENTE até prova.

**Memória de evidências, sem sistema paralelo:** reutilizar na issue evidências existentes com fonte, natureza (relato da Direção, captura/transcrição, leitura autenticada, execução técnica), data/período, escopo, limites e gatilho de rechecagem. Novo pedido só quando houver mudança material, período de uso diferente, contradição, novo risco ou gate que exija estado live; apontar campo faltante e por quê. Falta de acesso à UI não invalida relato existente nem prova condição técnica ainda não observada. **Bloquear apenas a ação de risco**, liberando trabalhos independentes autorizados; um budget US$0 com Stop usage não garante isoladamente custo futuro zero.

**Reconciliação documental #86:** as seções 1, 2, 3 e 7 abaixo trazem a proposta de fluxo horizontal, condicionada à revisão competente, autoridade vigente e homologação aplicável. Nenhuma permissão é criada por este texto.

## 1. Regra central e fonte da autoridade

Não há agente central responsável por todas as missões, ownership global, fila universal ou despacho obrigatório. O ownership pertence ao responsável explicitamente designado para cada tarefa/etapa. O remetente mantém a responsabilidade até comprovar a entrega e o destinatário registrar **ACEITO**; após o aceite, o destinatário assume a execução delimitada. O Scrum Master acompanha sinais do fluxo e intervém por exceção, sem substituir o responsável nem escolher rotineiramente a rota. Especialista só executa após aceite explícito e dentro de sua autorização. Parecer de QA, Validação, Auditoria ou Revisor Independente não autoriza merge, gastos, publicação ou deploy. A Direção decide atos reservados. A [issue #47](https://github.com/gentestsai-sudo/gentests-os/issues/47) trata de automação futura, não implantada.

**Roteamento não é autorização.** O catálogo de papéis/rotas abaixo é candidato. Fonte de autoridade: [[00-Constituicao/Matriz-de-Permissoes|POL-003]], delegação formal vigente, permissão efetiva da ferramenta e aprovação específica para cada ato protegido; reconciliação pendente na [issue #53](https://github.com/gentestsai-sudo/gentests-os/issues/53). Quando a autoridade é ausente/ambígua: **BLOQUEADA POR AUTORIDADE**, com dono e próxima decisão. RACI ou texto de despacho não cria permissão.

| Função | Competência da rota candidata | Limite / segregação |
|---|---|---|
| Direção | Deliberação reservada, autorização por objeto | Decisão não substitui QA ou parecer técnico |
| Scrum Master | Monitoramento da saúde do fluxo e atuação operacional por exceção | Não recebe todas as tarefas, não mantém fila/ownership global, não despacha rotineiramente, não substitui especialistas nem autoriza atos reservados |
| Comercial | Prospecção e CRM autorizado | Contato externo sob autorização; sem gasto autônomo |
| Marketing | Conteúdo e campanhas | Publicação/autoria sem autoaprovação |
| Produto | Requisitos e critério funcional | Não autoriza deploy/gasto |
| UX/UI | Proposta de interface | Revisão por pessoa/função distinta quando exigida |
| Engenharia / Executor | Código, documentação e testes internos | Não autoriza próprio merge/deploy |
| Infra | Ambiente, CI/CD e rollback autorizado | Não amplia acessos; deploy condicionado |
| Financeiro | Estimativa, conciliação e preparação | Não inicia, agenda ou executa pagamento/transferência autonomamente |
| QA | Plano/execução de testes e parecer QA | Não substitui revisão independente nem autoriza merge |
| Validação | Critério e aceite especializado quando nomeado | Não valida produção própria nem substitui Direção |
| Auditoria / X9 | Varredura de controles e rastros | Não audita trabalho próprio nem autoriza correção |
| Governança | Processo, conformidade e propostas | Não homologa proposta própria |
| Revisor Independente Modelo A | Parecer crítico independente | Não pode ser autor, executor ou aprovador do próprio objeto |
| Agile Coach (candidato) | Recomendações e métricas de fluxo | Não ativado; não despacha, encerra ou autoriza |

## 2. Contrato de eventos e transições — proposta v0.2.0

Cada evento na **issue canônica** deve conter `event_id`, `mission_id`, `handoff_id`, `version`, instante ISO 8601 com fuso, ator, dono atual, próximo dono, estado anterior/seguinte, evidência, autorização específica e PR/commit correlato. Identidade de evento/versão para idempotência é requisito futuro, **não mecanismo implementado**. Missão, etapa, transporte, aceite, parecer e decisão são estados distintos.

| Evento/condição | Transição | Ownership e gate |
|---|---|---|
| Nova demanda | inexistente → registrada | Solicitante/responsável da missão registra objetivo, responsável inicial competente, DoR, fonte e autorização aplicável; não há triagem central obrigatória |
| Entrada insuficiente | registrada/refinamento → aguardando refinamento | Responsável atual solicita diretamente ao dono da informação faltante, registrando lacuna, dono e próxima ação |
| DoR satisfeito | registrada/refinamento → pronta | Responsável atual identifica diretamente o especialista competente conforme contrato, escopo, autorização e acesso efetivo |
| Mensagem redigida | pronta → handoff preparado | Ainda **não** registrada ou entregue |
| Registro GitHub | preparado → registrado; acionamento pendente | Comentário/issue **não é** acionamento efetivo |
| Entrega comprovada | acionamento pendente → aguardando aceite | Remetente registra prova de transporte; permanece responsável até o aceite explícito do destinatário |
| ACEITO explícito | aguardando aceite → etapa aceita/em execução | Destinatário assume execução; aceite não aprova mérito |
| DEVOLVIDO explícito | aguardando aceite → devolvida/refinamento | Motivo, requisito, dono, próxima ação; sem loop infinito |
| Erro de transporte | preparado/pendente → erro de entrega | Remetente registra erro e recupera dentro da autonomia; aciona o Scrum Master por exceção se houver impedimento persistente ou conflito; sem aceite fictício |
| Sem resposta | aguardando aceite → aguardando aceite escalonada | Remetente mantém ownership e registra a pendência; aciona o Scrum Master por exceção se o atraso/impedimento exigir intervenção; silêncio nunca é aceite |
| Impedimento do executor | em execução → bloqueada | Executor registra causa, impacto, responsável e próxima ação; solicita apoio ao Scrum Master por exceção ou encaminha diretamente ao especialista competente |
| Desbloqueio | bloqueada → em execução/pronta | Rechecar DoR e autoridade |
| Entrega com evidência | em execução → etapa concluída/aguardando transferência | Remetente informa realizado/não realizado e riscos; missão continua |
| Transferência registrada | concluída → handoff pendente | Remetente identifica destinatário competente e registra evento; responsabilidade não muda até o aceite explícito do destinatário |
| Verificações paralelas | em verificação → verificações parciais | QA, Validação, Auditoria e Revisão Independente, se exigidas, têm donos e pareceres próprios; gate só fecha com todos ou dispensa expressa autorizada |
| Não conformidade | em verificação → correção focal | Achados e condição de rechecagem; retorna ao executor |
| Mérito verificado | em verificação → aguardando decisão/entrega | Aprovação técnica não autoriza atos reservados |
| Decisão reservada | aguardando decisão → autorizada/devolvida/cancelada | Direção registra objeto, escopo e decisão |
| Integração real | autorizada → conferência final | Executor/Infra habilitado registra commit, publicação/deploy e evidência |
| DoD da missão | conferência final → encerrada | Responsável pela missão ou autoridade expressamente designada confere os gates aplicáveis e registra encerramento; não há encerramento central presumido |
| Cancelamento fundamentado | estado não final → cancelada | Autoridade competente documenta motivo, impactos e comunicação |

**Ownership:** cada tarefa/etapa tem um responsável atual explicitamente registrado; o remetente responde pela entrega até o aceite; o destinatário assume a execução após ACEITO explícito; o verificador responde pelo próprio parecer; decisões reservadas pertencem à Direção. O Scrum Master não possui ownership global e acompanha somente exceções que demandem sua atuação. Todo parecer relevante informa objeto, HEAD/versão, resultado, evidências e responsável na issue canônica. Registro, notificação, leitura, entrega e aceite são eventos distintos. Toda devolução, pendência e bloqueio exige dono atual, próximo dono e próxima ação.

## 3. WIP e capacidade — regra candidata não ativada

Não impor WIP 1 agora. Slot do remetente pode ser liberado quando: (a) evidências e retorno estão completos; (b) o próximo especialista recebeu e **ACEITOU** expressamente; e (c) não subsiste correção ativa com o remetente. Não há assunção excepcional de fila pelo Scrum Master nem liberação de responsabilidade por silêncio ou registro isolado. Registro ou transporte sem aceite não libera responsabilidade por presunção. Assumir fila **não** equivale ao aceite do próximo executor/revisor. Registrar exceções P0, bloqueio externo e paralelismo independente com motivos. Sem revisor independente apto, registrar **BLOQUEADA**, nunca autoaprovação. Preservar trabalhos comerciais P0, sem bypass de gates de segurança.

## 4. DoR/DoD e devolução por interface

| Interface | DoR / motivo de devolução | DoD / próximo gate |
|---|---|---|
| Produto → UX/UI ou Engenharia | Problema, público, fluxos, regras, critérios testáveis, dependências, decisões pendentes; ambiguidade retorna a Produto | Protótipo/especificação versionada, exceções e evidências; QA/Validação conforme risco; sem autorização implícita |
| Executor → QA → Revisor Independente | PR/commit, ambiente, escopo, testes realizados e não realizados, evidência de acesso; inacessibilidade ou falta de evidência bloqueia/devolve | Parecer QA rastreável; defeitos retornam ao Executor; revisão independente recebe diff/QA e nunca é feita por autor/executor |
| Marketing → revisão → Comercial | Artefato/versão, canal/público, fontes, marca, links e testes reais; logo/link não verificável bloqueia | Revisão de conteúdo e marca por funções distintas quando cabível; correção volta a Marketing; publicação/envio com autorização específica |

Campos dispensáveis devem trazer **N/A justificado**, sem exigir commit em texto trivial nem afirmar teste não realizado como aprovado.

## 5. Verificações independentes, substituição e decisão

Para cada objeto crítico, registrar `author_id`, `executor_id`, `qa_id`, `validator_id`, `auditor_id`, `reviewer_id`, `approver_id`, com N/A justificado quando cabível. Verificar **identidade real, participação prévia e habilitação efetiva**, não apenas títulos de agentes; ninguém revisa ou valida independentemente a própria produção. QA, Validação, Auditoria e Revisão Independente são funções distintas e suas aprovações **não se substituem**. Dispensa de gate obrigatório exige autoridade/justificativa registrada. Substituto só entra com competência, permissão e independência verificadas; delegação de autoridade vai à Direção. Sem elegível, bloquear com owner e risco.

## 6. Concorrência documental — gate proposto, ainda não comprovado

Inventariar, antes da edição: arquivos e IDs canônicos, PRs abertos, versões-base, histórico, owner integrador, sobreposições semânticas, links e impactos de permissão. Precedências **propostas, não ordem de merge**:

| Fonte | Concorrência conhecida | Encaminhamento candidato |
|---|---|---|
| PRC-COM-001 / COM-APOIO-PROSPECCAO-001 | PRs #43/#50 | #43 como referência de identificação; integrador Comercial a designar |
| PRC-MKT-001 / Revisao-de-Arte.md | PRs #39/#50 | Preservar controles de #39; integrador Marketing a designar |
| Indice-de-Agentes.md | #51 incorporado, #52/#54 | #51 como baseline; integrador a designar |
| POL-003 | PRs #52/#54 e issue #53 | #53 é owner da reconciliação, sem alteração paralela |
| GT-HANDOFF-001 | issue #55 / PR #57 | Issue fonte da especificação; PR artefato draft |

**Bloqueio candidato:** duplicação inequívoca de ID canônico, perda de controle obrigatório, link obrigatório quebrado, conflito não reconciliado ou ato sem autorização. **Aviso candidato:** texto sobreposto sem colisão provada, alias histórico, metadados ou apoio editorial. `GT-HANDOFF-001` é compartilhado intencionalmente por `tipo: processo` e `tipo: template`; não classificar isso isoladamente como duplicidade. Verificar owner e serialização antes de merge. `scripts/check_links.py` e `scripts/x9_scan.py` são candidatos a ensaio; cobertura, testes positivos/negativos/falsos positivos, logs e exit codes **não comprovados por esta especificação**. Gate bloqueante não ativado.

## 7. Encaminhamento proporcional — registro único e transporte verificável

**Regra operacional proposta de simplificação (#53/#86):** registrar uma vez na issue canônica o resultado, evidência, responsável, próxima ação, risco e autorização já aplicável. Para continuidade dentro da mesma especialidade, não criar handoff, evento ou pedido de aprovação adicional. Na transferência horizontal, o remetente encaminha diretamente ao destinatário competente; não há ciência ou aprovação central obrigatória.

**Transporte proporcional:** com canal conectado e autorizado, utilizar payload estruturado e prova de entrega/ACEITO. Sem canal conectado, disponibilizar **uma única mensagem copiável suficiente para executar**, contendo destino, objetivo, escopo, fonte de autoridade existente, links de evidências, próximo passo e condição de aceite. O template extenso é opcional para casos simples; campos adicionais são exigidos somente quando o risco/gate material os demandar. Nunca presumir entrega ou aceite por comentário no GitHub.

**Reuso de autorização:** consultar decisão válida para o objeto e escopo; não pedir novamente aprovação de atividade ordinária já coberta. Atos protegidos continuam sujeitos à autorização expressa aplicável e permissão técnica efetiva. Bloquear somente o ato sem autoridade e avançar trabalho independente autorizado.

**DoD proporcional:** resultado verificável, testes realizados/não realizados relevantes, risco residual, próximo dono e próximo passo. QA e revisão independente permanecem separados quando obrigatórios. Evitar reproduzir a mesma evidência em múltiplos documentos ou devoluções sem alteração material. Pareceres ficam registrados na issue canônica para os responsáveis e verificadores pertinentes; visibilidade não significa aceite do destinatário.

## 8. Piloto e indicadores — apenas planejamento

Candidato: missão #55, somente após autorização própria. O responsável pela missão e os participantes registram timestamps de acionamento/aceite/execução/verificações/decisão, WIP, idade por estado, bloqueios, devoluções, lead time, throughput e colisões. **Baseline N/D (não apurada)**; piloto não executado. Uma única amostra não comprova melhoria geral. Automação, GT-WIP-001 e Agile Coach seguem não ativados.

## Referências
- [Issue #55](https://github.com/gentestsai-sudo/gentests-os/issues/55) · [Proposta Governança v0.2.0](https://github.com/gentestsai-sudo/gentests-os/issues/55#issuecomment-6111790899) · [Parecer REV-02](https://github.com/gentestsai-sudo/gentests-os/issues/55#issuecomment-6111890108)
- [Issue #53 — POL-003](https://github.com/gentestsai-sudo/gentests-os/issues/53) · [Issue #47 — automação futura](https://github.com/gentestsai-sudo/gentests-os/issues/47)
- [[07-Templates/GT-HANDOFF-001-TEMPLATE]] · [[02-Agentes/Indice-de-Agentes]]
