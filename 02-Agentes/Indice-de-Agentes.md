---
tipo: indice
status: proposta
versao: 0.2.0
---
# Diretório canônico de agentes — proposta de reformulação

Fonte de nomes e fronteiras: [Arquitetura de papéis](Arquitetura-de-Papeis.md). Esta proposta organiza responsabilidades futuras e não comprova implantação, homologação ou concessão de acessos.

| Nome canônico / chat principal | ID | Contrato | Responsabilidade |
|---|---|---|---|
| 🧭 Orquestrador Central | AGT-ORQ | [Contrato](Orquestrador/Contrato-Agente-Orquestrador.md) | Coordenação de missões |
| 📦 Produto | AGT-PROD | [Contrato](Produto/Contrato-Agente-Produto.md) | Necessidades e requisitos |
| 🎨 UX/UI | AGT-UXUI | [Contrato](UX-UI/Contrato-Agente-UX-UI.md) | Jornadas e interfaces |
| 💻 Engenharia | AGT-ENG | [Contrato](Engenharia/Contrato-Agente-Executor-Tecnico.md) | Software e integrações |
| 🛠️ Infraestrutura | AGT-INFRA | [Contrato](Infraestrutura/Contrato-Agente-Infraestrutura.md) | Ambientes e operação |
| 🤝 Comercial | AGT-COM | [Contrato](Comercial/Contrato-Agente-Comercial.md) | Oportunidades e relacionamento autorizado |
| 📣 Marketing | AGT-MKT | [Contrato](Marketing/Contrato-Agente-Marketing.md) | Conteúdo e comunicação |
| 💰 Financeiro | AGT-FIN | [Contrato](Financeiro/Contrato-Agente-Financeiro.md) | Análise e preparação financeira |
| 🧪 QA | AGT-QA | [Contrato](QA/Contrato-Agente-QA.md) | Riscos e testes |
| ✅ Validador | AGT-VAL | [Contrato](Validador/Contrato-Agente-Validador.md) | Critérios de aceite e gates |
| 🔎 Auditor | AGT-AUD | [Contrato](Auditor/Contrato-Agente-Auditor.md) | Efetividade e conformidade dos controles |
| 👁️ X9 — Sentinela de Qualidade Documental | AGT-X9 | [Contrato](X9/Contrato-Agente-X9.md) | Detecção de inconsistências documentais |
| ⚖️ Governança | AGT-GOV | [Contrato](Governanca/Contrato-Agente-Governanca.md) | Regras e autoridade |
| 🔄 Processos | AGT-PROC | [Contrato](Processos/Contrato-Agente-Processos.md) | Procedimentos e interfaces |

## Estado e identidade
Os contratos catalogados permanecem propostas documentais. A aprovação de cada contrato e a capacidade operacional devem ser comprovadas separadamente na decisão aplicável. Direção/CEO é autoridade humana, não agente executor.

Revisor Independente é função Modelo A atribuída por missão a especialista sem participação conflitante; não criar agente permanente duplicado. Agile Coach permanece candidato não ativado por este pacote.

Nomes antigos de Engenharia (Executor Técnico/Executor do Site) são aliases de busca; o caminho histórico `Engenharia/Contrato-Agente-Executor-Tecnico.md` é preservado para compatibilidade com PR #52. Executor é também função genérica do autor de qualquer entrega, não um agente adicional.

## Interfaces e regras comuns
Consultar contrato, políticas e registros atuais antes de agir. Usar [GT-HANDOFF-001](../03-Processos/Encaminhamento-de-Missoes-GT-HANDOFF-001.md) como referência de proposta e respeitar a autoridade efetiva. [Produto/UX](../03-Processos/Refinamento-Produto-UX-Handoff.md) mantém sua interface.

[POL-003](../00-Constituicao/Matriz-de-Permissoes.md) precisa de reconciliação na [issue #53](https://github.com/gentestsai-sudo/gentests-os/issues/53). As novas linhas do índice não ampliam privilégios. Antes de merge, reconciliar o índice concorrente dos PRs #50/#52/#54, sem perda de responsabilidades ou histórico.

Chat principal identifica especialidade; chat de atividade não cria novo agente. Não presumir envio, acionamento, aceite, independência humana ou automação a partir de nomes, comentários ou arquivos.
