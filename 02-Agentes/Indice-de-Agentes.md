---
tipo: indice
status: proposta
versao: 0.3.0
---

# Diretório canônico de agentes — proposta de reformulação

Fonte de nomes e fronteiras: [Arquitetura de papéis](Arquitetura-de-Papeis.md) e [Arquitetura de agentes, runtime e governança](Arquitetura-de-Agentes-Runtime-e-Governanca.md). Este índice distingue os 14 agentes atualmente catalogados do novo perfil Tech Lead proposto. A inclusão documental não comprova criação, ativação, homologação ou concessão de acessos.

| Nome canônico / chat principal | ID | Contrato | Responsabilidade |
|---|---|---|---|
| 🧭 Scrum Master (antigo AirCaster) | AGT-SM | [Contrato](Scrum-Master/Contrato-Agente-Scrum-Master.md) | Saúde operacional, detecção e resolução inicial de impedimentos, encaminhamento e escalonamento por exceção |
| 📦 Produto | AGT-PROD | [Contrato](Produto/Contrato-Agente-Produto.md) | Necessidades e requisitos |
| 🎨 UX/UI | AGT-UXUI | [Contrato](UX-UI/Contrato-Agente-UX-UI.md) | Jornadas e interfaces |
| 💻 Engenharia | AGT-ENG | [Contrato](Engenharia/Contrato-Agente-Executor-Tecnico.md) | Software e integrações |
| 🧠 Tech Lead / Head Técnico (proposto) | AGT-TL | [Contrato](Tech-Lead/Contrato-Agente-Tech-Lead.md) | Direção técnica, arquitetura, padrões de engenharia, risco sistêmico, mentoria, review de PR, conflitos e integração |
| 🛠️ Infraestrutura | AGT-INFRA | [Contrato](Infraestrutura/Contrato-Agente-Infraestrutura.md) | Ambientes e operação |
| 🤝 Comercial | AGT-COM | [Contrato](Comercial/Contrato-Agente-Comercial.md) | Oportunidades e relacionamento autorizado |
| 📣 Marketing | AGT-MKT | [Contrato](Marketing/Contrato-Agente-Marketing.md) | Conteúdo e comunicação |
| 💰 Financeiro | AGT-FIN | [Contrato](Financeiro/Contrato-Agente-Financeiro.md) | Viabilidade, custos, precificação, recebíveis e conciliação sob autorização |
| 🧪 QA | AGT-QA | [Contrato](QA/Contrato-Agente-QA.md) | Riscos e testes |
| ✅ Validador | AGT-VAL | [Contrato](Validador/Contrato-Agente-Validador.md) | Critérios de aceite e gates |
| 🔎 Auditor | AGT-AUD | [Contrato](Auditor/Contrato-Agente-Auditor.md) | Efetividade e conformidade dos controles |
| 👁️ X9 — Sentinela de Qualidade Documental | AGT-X9 | [Contrato](X9/Contrato-Agente-X9.md) | Detecção de inconsistências documentais |
| ⚖️ Governança | AGT-GOV | [Contrato](Governanca/Contrato-Agente-Governanca.md) | Regras e autoridade |
| 🔄 Processos | AGT-PROC | [Contrato](Processos/Contrato-Agente-Processos.md) | Procedimentos e interfaces |

## Estado e identidade
Os 14 agentes atualmente catalogados permanecem sujeitos aos respectivos estados de aprovação e comprovação operacional. AGT-TL é uma inclusão proposta e não deve ser contado como agente ativo até existir decisão, contrato aprovado, identidade operacional, permissões e Evals aplicáveis. Direção/CEO é autoridade humana, não agente.

Revisor Independente é função atribuída por missão a especialista sem participação conflitante; não criar agente permanente duplicado. Agile Coach permanece candidato não ativado.

Nomes antigos de Engenharia (Executor Técnico/Executor do Site) são aliases de busca; o caminho histórico `Engenharia/Contrato-Agente-Executor-Tecnico.md` é preservado para compatibilidade. Executor é também função genérica do autor de qualquer entrega, não um agente adicional.

## Leitura documental por agente
Antes de iniciar ou retomar missão, consultar nesta ordem: (1) instruções e autorizações vigentes; (2) contrato do próprio papel; (3) POL-002, POL-003, SEC-AI-001 e quality gates aplicáveis; (4) processos pertinentes; (5) issue/PR canônicas e HEAD atual; (6) [GT-EXEC-001](../docs/GT-EXEC-001-Continuidade-Execucao.md). A ordem é de consulta, não altera a precedência de autoridade. Validar status e versões; documento integrado não se torna automaticamente regra aprovada nem instrução carregada no chat.

## Regra transversal de execução e autocheck
Aplicar a seção “executar e verificar antes de transferir” do GT-EXEC-001. O agente deve esgotar atividades úteis, permitidas e executáveis no escopo antes de um handoff. Autocheck não substitui QA/parecer independente quando exigido e não amplia alçada.

## Interfaces e regras comuns
Consultar contratos, políticas e registros atuais antes de agir. Usar [GT-HANDOFF-001](../03-Processos/Encaminhamento-de-Missoes-GT-HANDOFF-001.md) somente considerando sua condição de proposta e as divergências registradas na arquitetura consolidada. A comunicação horizontal não depende de aprovação rotineira do Scrum Master.

**Arquitetura e Evals:** [GT-ARCH-AGENTS-001](Arquitetura-de-Agentes-Runtime-e-Governanca.md) e [GT-EVAL-CORE-001](../docs/GT-EVAL-CORE-001-Matriz-de-Evals.md) são propostas para auditoria, não comprovação de implementação.

**Head Técnico:** [Contrato](Tech-Lead/Contrato-Agente-Tech-Lead.md) · [Contexto operacional](Tech-Lead/Contexto-Operacional-AGT-TL.md) · [Matriz de autoridade](Tech-Lead/Matriz-Autoridade-e-Escalonamento-AGT-TL.md). Aplicar também o princípio transversal [Excelência Enxuta — 5S](../00-Constituicao/Excelencia-Enxuta-5S.md). Os três artefatos são propostas complementares: mandato, contexto e limites de decisão. A delegação para executar merges elegíveis sem autorização individual da Direção depende de alteração formal e homologação da POL-003, branch protection, checks, segregação de funções, permissões efetivas e Evals. Nenhum desses documentos concede privilégios.
