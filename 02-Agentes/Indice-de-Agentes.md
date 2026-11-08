---
tipo: indice
status: proposta
versao: 0.2.2
---
# Diretório canônico de agentes — proposta de reformulação

Fonte de nomes e fronteiras: [Arquitetura de papéis](Arquitetura-de-Papeis.md). O papel AGT-ORQ foi sucedido por AGT-SM; o contrato antigo permanece apenas para rastreabilidade histórica. Esta proposta organiza responsabilidades futuras e não comprova implantação, homologação ou concessão de acessos.

| Nome canônico / chat principal | ID | Contrato | Responsabilidade |
|---|---|---|---|
| 🧭 Scrum Master (antigo AirCaster) | AGT-SM | [Contrato](Scrum-Master/Contrato-Agente-Scrum-Master.md) | Supervisão do fluxo, identificação, encaminhamento e escalonamento de impedimentos |
| 📦 Produto | AGT-PROD | [Contrato](Produto/Contrato-Agente-Produto.md) | Necessidades e requisitos |
| 🎨 UX/UI | AGT-UXUI | [Contrato](UX-UI/Contrato-Agente-UX-UI.md) | Jornadas e interfaces |
| 💻 Engenharia | AGT-ENG | [Contrato](Engenharia/Contrato-Agente-Executor-Tecnico.md) | Software e integrações |
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
Os contratos catalogados permanecem propostas documentais. A aprovação de cada contrato e a capacidade operacional devem ser comprovadas separadamente na decisão aplicável. Direção/CEO é autoridade humana, não agente executor.

Revisor Independente é função Modelo A atribuída por missão a especialista sem participação conflitante; não criar agente permanente duplicado. Agile Coach permanece candidato não ativado por este pacote.

Nomes antigos de Engenharia (Executor Técnico/Executor do Site) são aliases de busca; o caminho histórico `Engenharia/Contrato-Agente-Executor-Tecnico.md` é preservado para compatibilidade com PR #52. Executor é também função genérica do autor de qualquer entrega, não um agente adicional.

## Leitura documental por agente

Antes de iniciar cada missão ou retomar uma execução, consultar nesta ordem: (1) instruções e autorizações efetivamente vigentes; (2) contrato do próprio papel; (3) POL-002, POL-003, SEC-AI-001 e os quality gates aplicáveis; (4) processos pertinentes à tarefa; (5) issue/PR canônicas e HEAD atual; (6) [GT-EXEC-001 — continuidade da execução](../docs/GT-EXEC-001-Continuidade-Execucao.md). A ordem é de **consulta**, não altera a precedência de autoridade estabelecida em POL-002. Validar status e versões; documento integrado não se torna automaticamente regra aprovada ou instrução carregada no chat.

Para a missão #47, GT-EXEC-001 orienta executar as próximas atividades autorizadas na mesma resposta, sem parar em checkpoints. Não dispensa revisão independente, transporte real, autorização específica ou limites da ferramenta. Em retomadas, usar síntese canônica com decisões vigentes e evidências, além de eventos recentes; os 50 últimos comentários isolados não constituem memória integral da missão.

## Regra transversal de execução e autocheck

Aplicar a seção ["executar e verificar antes de transferir" do GT-EXEC-001](../docs/GT-EXEC-001-Continuidade-Execucao.md#principio-transversal-executar-e-verificar-antes-de-transferir): agente deve esgotar atividades úteis, permitidas e executáveis no escopo, inclusive conferir o próprio trabalho, antes de um handoff. A especialidade principal define responsabilidade e alçada, não proíbe tarefas auxiliares de validação interna. Autocheck não substitui QA/parecer independente quando exigido. Essa regra de processo não concede permissão nova.

## Interfaces e regras comuns
Consultar contrato, políticas e registros atuais antes de agir. Para aprofundamento **facultativo e pertinente ao escopo da missão**, usar o [guia de referências profissionais por especialidade](../03-Processos/Referencias-Profissionais-por-Area.md), sem substituir fontes canônicas, criar gates ou exigir leitura integral. Usar [GT-HANDOFF-001](../03-Processos/Encaminhamento-de-Missoes-GT-HANDOFF-001.md) como referência de proposta e respeitar a autoridade efetiva. [Produto/UX](../03-Processos/Refinamento-Produto-UX-Handoff.md) mantém sua interface.

[POL-003 v1.2.1 — proposta](../00-Constituicao/Matriz-de-Permissoes.md) foi integrada à main pelo PR #62, sem representar homologação ou ampliação de privilégios. A [issue #53](https://github.com/gentestsai-sudo/gentests-os/issues/53) mantém a rastreabilidade da reconciliação. Antes de integrar #52/#61, preservar o índice canônico e conciliar interfaces semânticas de #50, sem perda de responsabilidades ou histórico.

Chat principal identifica especialidade; chat de atividade não cria novo agente. Não presumir envio, acionamento, aceite, independência humana ou automação a partir de nomes, comentários ou arquivos.

**Interface técnica:** PRC-ENG-001, [proposta reconciliada de #52/#61](../03-Processos/Entrega-Tecnica-e-Infraestrutura.md), coordena Produto/UX/UI/Engenharia/QA/Infraestrutura. Presente nesta branch como proposta; não homologado por esta referência.

**Interface financeira:** [PRC-FIN-001](../03-Processos/PRC-FIN-001-Gestao-Financeira.md), proposta já presente na main, relaciona Comercial, área técnica, Financeiro e Direção, sem ampliar permissões. O contrato AGT-FIN v1.1.1 da main e POL-003 v1.2.1 preservam FIN-54-01: Financeiro não inicia, agenda ou executa pagamentos/transferências. Proposta integrada não equivale a homologação.

**Interface Comercial/Marketing:** conforme [proposta #50](https://github.com/gentestsai-sudo/gentests-os/pull/50), Marketing fornece origem/contexto; Comercial verifica duplicidade, autorização, qualifica e controla registro/seguimento no CRM, sem pipeline paralelo. Fonte única de CRM permanece proposta dependente de acesso comprovado e ratificação da Direção. Esta fronteira não autoriza contato externo.


## Decisão de papel — AGT-SM

O Scrum Master não é um orquestrador central. Não recebe toda demanda nem intermedeia cada handoff. Identifica, classifica, encaminha e escala impedimentos; acompanha o desfecho pelo registro canônico. Os agentes especialistas preservam comunicação direta e autonomia dentro de seus contratos e permissões. Ver [Contrato do Scrum Master](Scrum-Master/Contrato-Agente-Scrum-Master.md).

**Merge:** AGT-SM pode monitorar prontidão, conferir evidências/gates e encaminhar pendências. Autoridade para aceitar/autorizar/executar merge depende de decisão normativa específica e conciliação com POL-003; este índice não concede privilégios.
