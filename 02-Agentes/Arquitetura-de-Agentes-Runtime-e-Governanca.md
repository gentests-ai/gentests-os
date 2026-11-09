---
tipo: arquitetura
id: GT-ARCH-AGENTS-001
versao: 0.1.0
status: proposta-para-auditoria
responsavel: Direcao
data: 2026-11-08
---

# Arquitetura de agentes, runtime, coordenação e Evals

> **Documento de consolidação para revisão arquitetural independente.** Registra decisões de direção e requisitos propostos. Não comprova implementação, não ativa agentes, não concede permissões e não substitui políticas aprovadas.

## 1. Decisões arquiteturais vigentes

1. **Não existe orquestrador central.** A arquitetura não deve introduzir um agente único responsável por receber, distribuir, autorizar e coordenar todas as tarefas. Esse desenho foi abandonado por gerar latência e gargalo.
2. **Handoffs são horizontais.** Agentes especializados encaminham tarefas diretamente ao próximo agente competente, conforme contratos, Actions, permissões e gates.
3. **Agentes são definidos por especialidade.** Não há classes fixas de “executor” e “revisor”. Cada agente possui perfil, competência, escopo e contrato; pode executar etapas diferentes conforme sua especialização.
4. **Scrum Master atua por exceção.** Monitora saúde operacional, detecta atrasos, violações de contrato, ping-pong e impedimentos. Não intermedeia o fluxo normal.
5. **Tech Lead é o Head Técnico.** É a referência de alto nível para direção técnica, arquitetura, padrões de engenharia, risco sistêmico, qualidade estrutural, mentoria técnica, review de PR e integração. Atua por competência e criticidade, sem coordenar centralmente a equipe.
6. **Escala não pode ser codificada como número fixo.** Os 14 agentes atuais são a configuração inicial. A plataforma deve permitir organizações com 100+ agentes, especialidades e hierarquias configuráveis.
7. **Concorrência legítima é permitida.** Agentes podem executar tarefas distintas ao mesmo tempo. A exclusividade protege apenas a tarefa/recurso que não pode ser disputado.

## 2. Modelo de agentes e organização

Cada agente deve ter identidade estável e metadados configuráveis:
- agent_id e nome canônico;
- especialidade e competências;
- contrato e versão;
- permissões efetivas e limites;
- disponibilidade/estado operacional;
- relações organizacionais opcionais (líder, equipe, área);
- histórico de missões e handoffs.

A hierarquia é uma configuração organizacional, não um mecanismo de despacho central. Uma empresa pode configurar relações de liderança e escalonamento sem obrigar toda tarefa a percorrer a hierarquia.

O runtime não deve assumir que todos os agentes pertencem a uma única estrutura fixa. Deve suportar múltiplas organizações/tenants, com isolamento de dados, configuração e permissões.

## 3. Transferência direta de tarefas (handoff)

O agente de origem seleciona o próximo agente por competência/rota autorizada e encaminha diretamente. O Scrum Master não precisa aprovar cada transferência.

Toda Action de handoff deve registrar, no mínimo:
- event_id, mission_id, task_id, execution_id e handoff_id;
- agente de origem e agente de destino;
- especialidade/razão do encaminhamento;
- estado anterior e estado proposto;
- resumo do trabalho realizado;
- artefatos, commits, resultados e evidências;
- pendências, riscos e limitações;
- próxima ação esperada;
- instante, versão do contrato e correlação com issue/PR;
- confirmação de entrega, recebimento e aceite, quando o transporte suportar esses estados.

**Fim da participação de um agente precisa ser explícito.** Registrar se concluiu sua etapa, se transferiu responsabilidade, para quem transferiu e se o destino aceitou. “Comentário publicado”, “label alterado” ou “mensagem preparada” não equivalem, isoladamente, a entrega, aceite ou conclusão.

Estados distintos devem permanecer distintos: preparado → enviado → entregue → recebido → aceito/devolvido → em execução → etapa concluída → handoff seguinte ou missão concluída. Não presumir transporte automático entre chats quando o canal não existir.

## 4. Runtime, concorrência e persistência

O runtime deve suportar múltiplos agentes e execuções concorrentes sem impor um agente coordenador.

Entidades conceituais mínimas:
- **Agent:** identidade, perfil, capacidades, permissões e configuração.
- **Mission:** objetivo e contexto maior.
- **Task:** unidade de trabalho, critérios, dependências e estado.
- **Execution:** tentativa concreta de execução por um agente.
- **Claim/Lease:** posse temporária de uma tarefa/recurso exclusivo.
- **Handoff:** transferência rastreável entre agentes.
- **Event/Evidence:** histórico imutável ou append-only de transições e provas.
- **Eval Run:** execução de avaliação e seu resultado.

Requisitos de coordenação:
- claim atômico para tarefas exclusivas;
- lease com expiração e renovação quando aplicável;
- heartbeat/telemetria de atividade;
- fencing/generation token para impedir escrita tardia por execução que perdeu a posse;
- idempotência de Actions e eventos;
- recuperação após timeout, crash ou perda de conectividade;
- conclusão verificável com artefato e evidência;
- execução paralela de tarefas independentes;
- limite de capacidade por agente, tenant e recurso.

Não assumir que lease, heartbeat ou fencing já estão implementados. Validar código, armazenamento e testes antes de marcar como existente.

### Fonte documental versus banco transacional

O repositório GitHub é a **fonte canônica de documentação, contratos versionados, decisões, issues, PRs e evidências de desenvolvimento**. Pode servir como ledger de auditoria documental.

GitHub não deve ser tratado automaticamente como banco transacional do runtime. Labels, comentários, arquivos e commits não substituem operações atômicas de claim/lease, compare-and-swap, transações, expiração e fencing sob concorrência. Para estado operacional em tempo real, avaliar um armazenamento transacional apropriado, com isolamento por tenant, controle de acesso, backup e recuperação.

A decisão de banco/runtime ainda está **pendente de investigação**. Não criar credenciais nem conectar sistemas externos sem autorização específica.

## 5. Scrum Master — governança operacional por exceção

O Scrum Master (AGT-SM):
- detecta tarefas paradas, atrasos e ausência de progresso;
- identifica handoffs sem confirmação, contratos descumpridos, ping-pong, ciclos e tentativas repetidas;
- classifica impedimentos por tipo, impacto, urgência e domínio;
- tenta resolver impedimentos **operacionais** dentro de suas competências e permissões;
- não substitui o agente especialista em decisões ou correções técnicas;
- se não resolver, interrompe a repetição improdutiva e encaminha ao especialista adequado;
- acompanha o bloqueio e verifica o desfecho.

### Escalonamento obrigatório

1. **Detecção:** registrar sinal, evidência, tarefa, agente(s), duração e impacto.
2. **Tentativa operacional:** realizar diagnóstico e ações simples autorizadas (ex.: esclarecer estado, corrigir metadado/rota documental, solicitar confirmação, remover duplicidade de registro), sem alterar artefato técnico ou contornar gate.
3. **Especialista:** se persistir ou exigir competência técnica, encaminhar ao agente especialista com contexto, tentativas, evidências e resultado esperado.
4. **Issue de bloqueio:** se o especialista não resolver, abrir/atualizar issue específica, com severidade, impacto, causa conhecida/hipótese, tentativas, evidências, responsável e próxima decisão.
5. **Direção:** encaminhar a issue à Direção para decisão/intervenção.

O Scrum Master não deve insistir indefinidamente, criar ciclos de encaminhamento ou manter uma tarefa em retry infinito. O limite de tentativas e tempos por severidade será definido por política operacional. Bloquear apenas o ramo afetado; atividades independentes autorizadas podem continuar.

## 6. Tech Lead — Head Técnico

O Tech Lead (proposto AGT-TL) exerce o papel de **Head Técnico de alto nível**, autoridade técnica delegada para orientar a engenharia e proteger a coerência técnica do ecossistema. Combina visão estratégica e atuação hands-on nos pontos de maior risco.

Responsabilidades:
- definir e evoluir padrões de engenharia, critérios técnicos e práticas de revisão dentro das decisões aprovadas;
- avaliar arquitetura, stack, integrações, persistência, observabilidade, desempenho, segurança e manutenibilidade;
- manter visão de dívida técnica, dependências críticas, riscos sistêmicos e saúde dos componentes;
- revisar PRs e diffs reais, emitir parecer ligado ao HEAD exato e bloquear recomendação de merge diante de achados impeditivos;
- resolver conflitos preservando alterações válidas e executando testes do resultado combinado;
- orientar e desenvolver a capacidade técnica dos agentes especializados;
- recomendar refatorações, modernizações e mitigação de riscos;
- preparar e, após conciliação normativa e gates, executar merges dentro da alçada delegada.

Sua autoridade é técnica, não executiva: não altera prioridades de negócio unilateralmente, não concede permissões, não substitui especialistas de domínio e escala à Direção decisões estratégicas, irreversíveis, de alto impacto ou fora da alçada.

Tech Lead não é orquestrador, não distribui o trabalho normal e não é passagem obrigatória para toda tarefa. Não substitui QA, Validador, Auditor ou controles de segurança.

**Conflito normativo a resolver:** a POL-003 consultada reserva à Direção a autorização de merge em PRs. O objetivo é delegar ao Head Técnico a execução dos merges elegíveis sem autorização individual da Direção a cada PR, mantendo controles e escalonamento para exceções. Isso exige conciliação formal da POL-003/matriz de permissões, segregação de funções, branch protection, checks obrigatórios e permissões técnicas mínimas. Até essa decisão, o Tech Lead pode revisar, preparar e resolver conflitos em branch autorizada, mas não contornar a autorização vigente.

## 7. Gates e Actions

Actions devem aplicar contratos de entrada/saída, autorização, idempotência, rastreabilidade e transições válidas.

Gates devem verificar conforme o risco:
- identidade e permissões do agente;
- compatibilidade entre tarefa e competência;
- posse válida da execução, quando exclusiva;
- integridade do handoff e aceite do destino;
- evidências e critérios de conclusão;
- ausência de duplicidade/replay;
- segregação de autoria, revisão e aprovação quando exigida;
- autorização para merge, deploy, acesso, gasto ou ação externa;
- registro de resultado e próxima responsabilidade.

Um gate não pode ser considerado satisfeito apenas por label, comentário ou autodeclaração do agente. Falta de evidência significa **não verificável**, não conforme.

## 8. Evals como capacidade transversal

Evals devem nascer junto com cada contrato e capacidade do runtime, e executar continuamente.

Dimensões mínimas:
1. **Coordenação:** dois agentes disputando a mesma tarefa exclusiva; agentes em tarefas distintas simultâneas; concorrência em subtarefas; lease expirada; execução antiga tentando escrever; retry e replay.
2. **Handoff:** origem/destino corretos; entrega/recebimento/aceite; evidências completas; rejeição e devolução; transferência após falha de transporte.
3. **Especialização:** roteamento para o perfil correto; limites de competência; agente reconhecendo falta de capacidade; apoio técnico do Tech Lead.
4. **Scrum Master:** atraso, ausência de heartbeat, ping-pong, retry infinito, solução operacional, escalonamento ao especialista e issue encaminhada à Direção.
5. **Tech Lead:** PR com bug crítico; conflito de merge; alteração que quebra compatibilidade; testes insuficientes; risco de segurança; merge bloqueado sem autorização.
6. **Qualidade de entrega:** critérios, evidências, conclusão real, falsos positivos/negativos e regressões.
7. **Segurança e multi-tenant:** isolamento entre empresas, permissões, acesso cruzado, dados e segredos.
8. **Escala:** 14, 30, 50, 100 e cenários maiores; throughput, latência, contenção, custo e recuperação.

Tipos de Evals:
- unitários (mecanismo isolado);
- integração (Actions, agentes e persistência juntos);
- sistema (fluxos ponta a ponta e falhas simuladas);
- carga/escala;
- contínuos/regressão.

Cada Eval deve registrar versão do cenário, configuração, agentes envolvidos, ambiente, resultado esperado, resultado observado, evidências, custo/latência e decisão PASS/FAIL/BLOCKED. Evals não substituem testes de software nem revisão humana quando exigidos.

## 9. Critérios de maturidade

Uma capacidade só pode ser marcada como implementada e comprovada quando houver:
- contrato versionado;
- implementação identificada;
- testes automatizados pertinentes;
- Evals de comportamento e falhas;
- evidência de execução em ambiente definido;
- limites e permissões documentados;
- monitoramento e recuperação;
- resultado reproduzível.

Estados documentais permitidos:
- Implementado e comprovado;
- Implementado parcialmente;
- Planejado;
- Pendente de investigação;
- Bloqueado.

## 10. Auditoria arquitetural independente

Solicitar parecer de arquiteto que confronte esta proposta com o repositório e runtime reais. O parecer deve separar fatos observados, inferências e recomendações e cobrir:
- ausência de orquestrador central e coerência do handoff horizontal;
- modelo de dados e concorrência;
- persistência e recuperação;
- Actions, gates, permissões e rastreabilidade;
- Scrum Master e escalonamento;
- contrato e autoridade do Tech Lead;
- Evals, segurança multi-tenant e escala;
- divergências documentais e riscos de migração.

Entregáveis: mapa da arquitetura existente, matriz requisito × implementação × evidência, riscos priorizados, decisões pendentes e plano incremental. A auditoria não deve presumir que nomes em documentação correspondem a agentes ativos.

## 11. Relação com a Missão 47

Retomar a missão a partir do estado real da issue/PR e dos commits. A PR #101 contém defeitos QA conhecidos:
- **A01:** ledger ausente ou JSON null pode ser tratado como orçamento novo, permitindo replay.
- **A02:** reserva reutilizada após timeout pode permitir segundo POST sem consumo/fencing persistente.

Esses achados permanecem bloqueantes até correção e reteste com evidência. Não reativar workflow sintético, credenciais, chamadas externas ou execução real sem a autorização específica aplicável.

Referências: [Issue #47](https://github.com/gentests-ai/gentests-os/issues/47) · [PR #101](https://github.com/gentests-ai/gentests-os/pull/101) · [GT-EXEC-001](../docs/GT-EXEC-001-Continuidade-Execucao.md) · [GT-HANDOFF-001](../03-Processos/Encaminhamento-de-Missoes-GT-HANDOFF-001.md) · [POL-003 / Matriz de permissões](../00-Constituicao/Matriz-de-Permissoes.md).

## 12. Pendências explícitas

- Revisar e reconciliar textos antigos que ainda atribuem ownership global ao Orquestrador.
- Definir contrato formal de eventos e handoff com semântica idempotente.
- Inspecionar a implementação real de claim/ledger e resolver A01/A02.
- Definir runtime e armazenamento transacional.
- Definir limites de tentativas, timeouts e severidades do Scrum Master.
- Aprovar contrato e identidade AGT-TL como Head Técnico; conciliar POL-003/matriz de permissões para delegação controlada de merges.
- Definir catálogo versionado de Evals e thresholds de aprovação.
- Projetar isolamento multiempresa e configuração de hierarquias.
- Realizar auditoria independente antes de consolidar arquitetura como aprovada.

**Status final:** proposta de arquitetura para auditoria. Não representa implementação concluída nem autorização operacional.

## 13. Diretrizes iniciais do MVP e identificadores provisórios

Decisões registradas pela Direção em 2026-11-08. Não alteram o status geral deste documento nem comprovam implementação.

### API própria

**Decisão para o MVP:** não construir uma API pública própria nem adicionar uma camada/serviço de API separado sem necessidade concreta demonstrada.

- Utilizar as interfaces internas estritamente necessárias entre painel, runtime, agentes e persistência.
- Preservar contratos claros, autenticação, autorização, isolamento, segurança, observabilidade e desempenho; a ausência de uma API pública não elimina esses requisitos.
- Diferenciar APIs de provedores externos de IA, que podem ser necessárias para consumir modelos, de uma API própria do produto.
- Reavaliar a decisão quando houver requisito real de integração externa, consumidores independentes, acesso de terceiros ou distribuição do serviço.
- Se a necessidade surgir, introduzir a interface com a menor complexidade possível, sem reconstruir o motor.

**Princípio:** não criar uma camada, serviço ou dependência apenas por convenção. A solução mais simples que atenda aos requisitos de segurança, desempenho, escala e manutenção é a preferida.

### Identificadores provisórios

- **Projeto Skynet:** codinome interno provisório da plataforma/produto.
- **Nuclia:** codinome interno provisório do motor de execução.

Os dois nomes são identificadores de trabalho, não marcas aprovadas nem declarações de disponibilidade jurídica. Não utilizar em divulgação, comercialização, registro de marca, domínio ou identidade visual definitiva. A escolha dos nomes comerciais deverá ocorrer após pesquisa de anterioridade, disponibilidade de domínio e avaliação de risco de confusão. Substituir os codinomes na documentação e nos artefatos pertinentes quando a marca definitiva for aprovada.

