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

## Bloqueio localizado e continuidade global

Aplicar [GT-EXEC-001 — Bloqueio localizado, continuidade global](../docs/GT-EXEC-001-Continuidade-Execucao.md#bloqueio-localizado-continuidade-global): revisão ou autorização pendente impede apenas a ação dependente. Após registrar dono, evidência e condição de desbloqueio, prosseguir nas demais atividades independentes autorizadas. Não confundir gate legítimo de merge com paralisação de toda a missão nem reabrir PR integrada sem razão material.

## Regra global de registro final de tarefa — proposta

Todo agente catalogado neste índice e qualquer agente futuro deve emitir, ao encerrar uma tarefa delimitada, um HANDOFF integral no modelo GT-HANDOFF-001, mesmo quando não houver transferência para outro agente. Aplicar aos estados CONCLUÍDA, BLOCKED, INTERROMPIDA, CANCELADA e TRANSFERIDA. O relatório deve registrar trabalho real, artefatos/arquivos/contratos/commits/PRs afetados, verificações e evidências, itens não executados, riscos, estado final e próxima ação/responsável.

A obrigação é de encerramento de tarefa, não de checkpoint: não gerar um HANDOFF completo a cada commit, teste ou ação intermediária enquanto a mesma tarefa continua. Relatório de conclusão sem transferência não altera ownership e não exige aceite fictício; transferência real continua sujeita a transporte comprovado e aceite explícito. Conclusão da tarefa não equivale a aprovação, merge, deploy ou encerramento da missão.

Fonte e modelo: [GT-HANDOFF-001 — Processo](../03-Processos/Encaminhamento-de-Missoes-GT-HANDOFF-001.md) e [Template](../07-Templates/GT-HANDOFF-001-TEMPLATE.md). O estado desses documentos permanece proposta até homologação; esta referência não cria permissão, autonomia, canal de transporte ou implementação no runtime.

## Interfaces e regras comuns

**Execução eficiente:** aplicar também a seção [GT-EXEC-001 — Execução eficiente da demanda](../docs/GT-EXEC-001-Continuidade-Execucao.md#execucao-eficiente-da-demanda--diretriz-registrada-em-12102026), mantendo handoffs horizontais, revisão final por QA/Revisor distinto conforme a diretriz e finalização automática condicionada a critérios/evidências. Isso não cria passagem pelos 14 papéis nem autoriza atos reservados.
Consultar contratos, políticas e registros atuais antes de agir. Usar [GT-HANDOFF-001](../03-Processos/Encaminhamento-de-Missoes-GT-HANDOFF-001.md) somente considerando sua condição de proposta e as divergências registradas na arquitetura consolidada. A comunicação horizontal não depende de aprovação rotineira do Scrum Master.

**Arquitetura e Evals:** [GT-ARCH-AGENTS-001](Arquitetura-de-Agentes-Runtime-e-Governanca.md) e [GT-EVAL-CORE-001](../docs/GT-EVAL-CORE-001-Matriz-de-Evals.md) são propostas para auditoria, não comprovação de implementação.

**Head Técnico:** [Contrato](Tech-Lead/Contrato-Agente-Tech-Lead.md) · [Contexto operacional](Tech-Lead/Contexto-Operacional-AGT-TL.md) · [Matriz de autoridade](Tech-Lead/Matriz-Autoridade-e-Escalonamento-AGT-TL.md). Aplicar também o princípio transversal [Excelência Enxuta — 5S](../00-Constituicao/Excelencia-Enxuta-5S.md). Os três artefatos são propostas complementares: mandato, contexto e limites de decisão. A diretriz operacional expressa da Direção de 09/11/2026 delega ao Head Tech Lead a integração de PRs tecnicamente elegíveis por padrão, salvo bloqueante material muito grave. Isso não permite bypass de checks, segurança, segregação, permissões efetivas ou atos reservados. POL-003 continua proposta e não concede ACL/RBAC nem substitui controles reais.
