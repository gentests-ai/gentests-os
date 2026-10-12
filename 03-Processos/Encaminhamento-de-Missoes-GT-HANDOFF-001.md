---
tipo: processo
id: GT-HANDOFF-001
versao: 0.2.1
status: proposta
responsavel: Governança
missao: GT-GOV-CHANGE-001
issue: https://github.com/gentestsai-sudo/gentests-os/issues/55
---
# GT-HANDOFF-001 — Encaminhamento de missões (PROPOSTA v0.2.1)

> **Não homologado.** Este desenho não concede acessos, não altera POL-003, contratos ou hierarquia, não autoriza merge, publicação, piloto, GT-WIP-001, Agile Coach ou automação #47. Base: [Governança v0.2.0](https://github.com/gentestsai-sudo/gentests-os/issues/55#issuecomment-6111790899) e [REV-GOV-CHANGE-002](https://github.com/gentestsai-sudo/gentests-os/issues/55#issuecomment-6111890108).

## Proposta focal #86 — roteamento federado e reuso de evidências (pendente de homologação)

**Decisão da Direção registrada na [issue #86](https://github.com/gentestsai-sudo/gentests-os/issues/86):** dentro da missão, autorização e permissões efetivas já vigentes, especialistas podem **encaminhar diretamente** ao próximo especialista competente, com GT-HANDOFF-001 e evento rastreável na issue canônica. Não necessitam do Orquestrador como intermediário rotineiro. Esta cláusula é **proposta de conciliação** com a regra central abaixo e com POL-003; não cria privilégios e não entra em vigor por simples texto.

O Orquestrador mantém **ownership global**, prioridades e supervisão de exceções, acesso ao histórico integral e **síntese incremental** por missão (estado, dono, próxima ação, evidências, bloqueios e decisões), sem reler nem retranscrever todo o histórico a cada etapa. Escalar ao Orquestrador só para conflito de rota/prioridade/escopo, dependência, falha de entrega/aceite ou autoridade incerta. Decisões reservadas permanecem com a Direção.

**Transições distintas:** preparar, registrar, entregar de fato, receber, ACEITAR, executar, validar, autorizar, integrar e encerrar. GitHub não entrega mensagem automaticamente a outro chat ChatGPT; sem canal operacional efetivo, fornecer mensagem integral copiável e registrar entrega/aceite como PENDENTE até prova.

**Memória de evidências, sem sistema paralelo:** reutilizar na issue evidências existentes com fonte, natureza (relato da Direção, captura/transcrição, leitura autenticada, execução técnica), data/período, escopo, limites e gatilho de rechecagem. Novo pedido só quando houver mudança material, período de uso diferente, contradição, novo risco ou gate que exija estado live; apontar campo faltante e por quê. Falta de acesso à UI não invalida relato existente nem prova condição técnica ainda não observada. **Bloquear apenas a ação de risco**, liberando trabalhos independentes autorizados; um budget US$0 com Stop usage não garante isoladamente custo futuro zero.

**Reconciliação documental #86:** as seções 1, 2, 3 e 7 abaixo trazem a proposta de fluxo horizontal, condicionada à revisão competente, autoridade vigente e homologação aplicável. Nenhuma permissão é criada por este texto.

## 1. Regra central e fonte da autoridade

**Orquestrador Central único** mantém ownership da missão, triagem e lacunas de rota, acompanha as transferências registradas, sem confirmar rotineiramente destinos já autorizados; **não se autodespacha**. Especialista só assume execução após **ACEITO explícito**; o parecer de QA, Validação, Auditoria ou Revisor Independente não concede autorização para merge, gastos, publicação ou deploy. Direção decide os atos reservados e, no transporte manual, apenas copia a mensagem pronta, sem escolher rota. A [issue #47](https://github.com/gentestsai-sudo/gentests-os/issues/47) trata de automação futura, não implantada.

**Roteamento não é autorização.** O catálogo de papéis/rotas abaixo é candidato. Fonte de autoridade: [[00-Constituicao/Matriz-de-Permissoes|POL-003]], delegação formal vigente, permissão efetiva da ferramenta e aprovação específica para cada ato protegido; reconciliação pendente na [issue #53](https://github.com/gentestsai-sudo/gentests-os/issues/53). Quando a autoridade é ausente/ambígua: **BLOQUEADA POR AUTORIDADE**, com dono e próxima decisão. RACI ou texto de despacho não cria permissão.

| Função | Competência da rota candidata | Limite / segregação |
|---|---|---|
| Direção | Deliberação reservada, autorização por objeto | Decisão não substitui QA ou parecer técnico |
| Orquestrador | Triagem, preparo, despacho, acompanhamento e fechamento condicionado | Não executa ação técnica por presunção nem homologa sua própria proposta |
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
| Nova demanda | inexistente → registrada | Orquestrador assume triagem/DoR |
| Entrada insuficiente | registrada/refinamento → aguardando refinamento | Orquestrador indica requisito, dono e retorno; sem despacho |
| DoR satisfeito | registrada/refinamento → pronta | Responsável pela etapa/remetente aponta evidência e rota autorizada; ORQ atua na triagem inicial ou por exceção. |
| Mensagem redigida | pronta → handoff preparado | Ainda **não** registrada ou entregue |
| Registro GitHub | preparado → registrado; acionamento pendente | Comentário/issue **não é** acionamento efetivo |
| Entrega comprovada | acionamento pendente → aguardando aceite | Remetente registra prova de entrega; ORQ acompanha pela issue sem aprovar cada rota |
| ACEITO explícito | aguardando aceite → etapa aceita/em execução | Destinatário assume execução; aceite não aprova mérito |
| DEVOLVIDO explícito | aguardando aceite → devolvida/refinamento | Motivo, requisito, dono, próxima ação; sem loop infinito |
| Erro de transporte | preparado/pendente → erro de entrega | Remetente registra erro e recupera dentro da autonomia; escala ao ORQ se persistente; sem aceite fictício |
| Sem resposta | aguardando aceite → aguardando aceite escalonada | Remetente monitora e escala ORQ quando necessário; silêncio nunca é aceite |
| Impedimento do executor | em execução → bloqueada | Executor registra dono e ação; ORQ intervém em dependência ou conflito não resolvido diretamente |
| Desbloqueio | bloqueada → em execução/pronta | Rechecar DoR e autoridade |
| Entrega com evidência | em execução → etapa concluída/aguardando transferência | Remetente informa realizado/não realizado e riscos; missão continua |
| Transferência registrada | concluída → handoff pendente | Remetente identifica destinatário competente e registra evento; ORQ acompanha pela issue; destinatário ainda não aceitou |
| Verificações paralelas | em verificação → verificações parciais | QA, Validação, Auditoria e Revisão Independente, se exigidas, têm donos e pareceres próprios; gate só fecha com todos ou dispensa expressa autorizada |
| Não conformidade | em verificação → correção focal | Achados e condição de rechecagem; retorna ao executor |
| Mérito verificado | em verificação → aguardando decisão/entrega | Aprovação técnica não autoriza atos reservados |
| Decisão reservada | aguardando decisão → autorizada/devolvida/cancelada | Direção registra objeto, escopo e decisão |
| Integração real | autorizada → conferência final | Executor/Infra habilitado registra commit, publicação/deploy e evidência |
| DoD da missão | conferência final → encerrada | Orquestrador/encarregado autorizado verifica todos os gates |
| Cancelamento fundamentado | estado não final → cancelada | Autoridade competente documenta motivo, impactos e comunicação |

**Ownership:** missão, prioridades e exceções = Orquestrador; encaminhamento horizontal da etapa e comprovação do transporte = remetente; execução aceita = destinatário; parecer = verificador nomeado; decisão reservada = Direção. Todo parecer relevante deve informar objeto, HEAD/versão, resultado, evidências e responsável na issue canônica. ORQ consulta e incorpora os pareceres à síntese incremental: registro, notificação, leitura e incorporação são eventos diferentes. Toda devolução, pendência e bloqueio exige dono atual, próximo dono e próxima ação. Envio do retorno não equivale à transferência aceita.

## 3. WIP e capacidade — regra candidata não ativada

Não impor WIP 1 agora. Slot do remetente pode ser liberado quando: (a) evidências e retorno estão completos; (b) próximo especialista recebeu e **ACEITOU** expressamente, ou ORQ assumiu fila excepcional com dono explícito sem simular aceite do executor; e (c) não subsiste correção ativa com o remetente. Registro ou transporte sem aceite não libera responsabilidade por presunção. Assumir fila **não** equivale ao aceite do próximo executor/revisor. Registrar exceções P0, bloqueio externo e paralelismo independente com motivos. Sem revisor independente apto, registrar **BLOQUEADA**, nunca autoaprovação. Preservar trabalhos comerciais P0, sem bypass de gates de segurança.

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

## 7. Mensagem integral copiável — gate transversal obrigatório

Ao concluir, bloquear, devolver ou transferir uma etapa operacional, o remetente preenche [[07-Templates/GT-HANDOFF-001-TEMPLATE]] e entrega **uma única mensagem integral, preenchida e copiável, dirigida ao destinatário seguinte**, com objetivo, DoR/DoD, autoridade, limites, evidências reais, estados de transporte/aceite, próximos responsáveis e retorno. **Resultado isolado, tabela-resumo ou link não substituem a mensagem integral.** Em retorno apenas de prestação de contas ao Orquestrador, a exceção de *não haver despacho operacional direto* deve ser justificada; ainda assim fornecer prestação de contas integral. Na rota horizontal já autorizada, o remetente endereça mensagem integral diretamente ao especialista seguinte e registra o parecer para ciência rastreável do ORQ; **não depende de retorno ao ORQ e novo despacho**. ORQ prepara despacho próprio na triagem ou ao assumir exceção e não se autodespacha. A Direção apenas transporta a mensagem pronta enquanto necessário. Não marcar acionamento por comentário GitHub, aceite por silêncio, ou decisão por parecer.

**DoD da etapa:** artefato e evidências versionados; testes feitos/não feitos discriminados; bloqueios/riscos e donos; verificações obrigatórias e dispensas autorizadas; autorização da ação; mensagem integral pronta para transporte manual, ou payload técnico quando integração efetiva for autorizada; entrega/ACEITO comprovados ou pendência com dono; parecer rastreável na issue para ORQ. **DoD da missão:** pareceres e decisões exigidas, autorização separada, integração/publicação real comprovada se aplicável, pendências sob dono e encerramento expresso. Sem isso, etapa concluída ≠ missão encerrada.

## 8. Piloto e indicadores — apenas planejamento

Candidato: missão #55, somente após autorização própria. Orquestrador coleta timestamps de despacho/acionamento/aceite/execução/verificações/decisão, WIP, idade por estado, bloqueios, devoluções, lead time, throughput e colisões. **Baseline N/D (não apurada)**; piloto não executado. Uma única amostra não comprova melhoria geral. Automação, GT-WIP-001 e Agile Coach seguem não ativados.

## Referências
- [Issue #55](https://github.com/gentestsai-sudo/gentests-os/issues/55) · [Proposta Governança v0.2.0](https://github.com/gentestsai-sudo/gentests-os/issues/55#issuecomment-6111790899) · [Parecer REV-02](https://github.com/gentestsai-sudo/gentests-os/issues/55#issuecomment-6111890108)
- [Issue #53 — POL-003](https://github.com/gentestsai-sudo/gentests-os/issues/53) · [Issue #47 — automação futura](https://github.com/gentestsai-sudo/gentests-os/issues/47)
- [[07-Templates/GT-HANDOFF-001-TEMPLATE]] · [[02-Agentes/Indice-de-Agentes]]
