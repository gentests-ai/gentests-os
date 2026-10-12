# GenTests Quality Intelligence
**Discovery de Produto — v0.2**

**Responsável:** 📦 Produto — AGT-PROD  
**Solicitante:** 👑 Direção GenTests.ai  
**Data:** 12/10/2026  
**Estado:** Consolidação documental concluída — aprovação conceitual pendente  
**Base:** Discovery v0.1 + parecer consultivo QA “ADEQUADO COM AJUSTES”  
**Natureza:** Planejamento, sem autorização de implementação

## 1. Visão e público-alvo

Desenvolver uma inteligência especializada em qualidade de software capaz de compreender requisitos, questionar incoerências, antecipar riscos e auxiliar profissionais de QA a decidir o que realmente precisa ser testado.

**Usuários iniciais:** QAs, QA Leads, Tech Leads e Product Owners.  
**Compradores potenciais:** gestores de Engenharia, Qualidade e Tecnologia.

O produto complementa decisões humanas. Não substitui o QA nem aprova requisitos ou testes automaticamente.

## 2. Problema e diferencial

Requisitos ambíguos, conflitos entre regras, dependências negligenciadas e regressões pouco direcionadas geram retrabalho e exposição a defeitos.

**Diferencial proposto:** ir além da geração de casos de teste, produzindo uma análise crítica, priorizada e rastreável, capaz inclusive de concluir:

**“Esta regra precisa ser esclarecida antes que determinados testes possam ser definidos.”**

A superioridade sobre ferramentas genéricas é uma hipótese comercial e técnica, sujeita à avaliação comparativa.

## 3. Capacidades e roadmap preservados

| Etapa | Escopo |
|---|---|
| **MVP** | Análise inteligente de um card, testabilidade, ambiguidades, riscos e recomendação justificada, com revisão humana |
| **I1 — Seleção por alteração** | Seleção de testes existentes por mudança, PR ou diff autorizado, considerando dependências e riscos; evolução de contexto de Jira, bugs, incidentes e alterações paralelas |
| **I2 — Execução exploratória** | Navegação orientada por IA em ambiente autorizado, com resultados e evidências |
| **I3 — Automação contínua** | Testes por PR, E2E críticos no deploy, smoke seguro pós-deploy e regressão periódica em homologação |
| **I4 — Inteligência de fluxo** | Impedimentos, tempos de espera, dependências, gargalos organizacionais e avaliação da eficácia das melhorias |

A atuação preventiva desde a criação e refinamento de cards no Jira permanece na visão do produto, mas **não é dependência do MVP**.

A análise futura de históricos, incidentes, cards relacionados, conflitos paralelos, PRs, código e diffs exigirá acesso autorizado e identificação das fontes. Informação histórica relacionada não prova defeito na alteração atual.

## 4. MVP recomendado

**MVP: Análise Inteligente de Cards**

### Entradas

- Descrição do card.
- Critérios de aceite existentes.
- Contexto de negócio e regras conhecidas.
- Dependências e restrições informadas manualmente.

### Resultado da análise

**A. Avaliação de testabilidade — P0-01**

Classificação obrigatória:

| Classificação | Significado | Comportamento esperado |
|---|---|---|
| **Testável** | Há informação suficiente para definir resultados esperados dos comportamentos relevantes | Recomendar cenários com resultados esperados fundamentados |
| **Parcialmente testável** | Algumas regras permitem cenários definidos, mas outras exigem esclarecimento | Separar cenários fundamentados dos condicionais ou pendentes |
| **Dependente de esclarecimento** | Falta regra essencial ou existe contradição que impede definir o resultado esperado da parte central | Priorizar perguntas e riscos; não definir cenários definitivos para o comportamento indefinido |

Uma inconsistência relevante não implica necessariamente bloquear todo o card: partes independentes podem continuar testáveis.

**B. Achados rastreáveis — P0-02**

Cada achado relevante deve conter:

- Referência ao trecho original do requisito ou indicação explícita da informação ausente.
- Classificação: **fato extraído**, **inconsistência demonstrável**, **hipótese de risco** ou **pergunta pendente**.
- Justificativa.
- Consequência potencial.
- Incerteza ou limitação da análise, quando aplicável.

Um fato descrito no card não equivale a comportamento comprovado no sistema. Uma hipótese não pode ser apresentada como defeito confirmado.

**C. Priorização acionável — P0-03**

A apresentação principal deve destacar, preferencialmente, **até três riscos ou testes decisivos**, acompanhados do motivo e da próxima ação recomendada ao QA.

**Exceção:** testes e controles obrigatórios efetivamente conhecidos devem ser preservados, mesmo quando excederem três itens.

Cenários adicionais podem aparecer como secundários quando necessários, sem incentivar volume desproporcional.

**D. Raciocínio de QA — P1-01**

Conforme o contexto, a análise deve considerar:

- Estados e transições.
- Valores-limite.
- Falhas e comportamentos excepcionais.
- Dependências funcionais e técnicas.
- Integrações e regressão.

A ausência de informações para analisar uma dessas dimensões deve gerar uma ressalva ou pergunta pertinente, não uma regra inventada.

**E. Classificação qualitativa — P1-03**

Riscos devem indicar **impacto**, **probabilidade qualitativa quando justificável** e **confiança da avaliação**.

Sem base suficiente, usar expressões como “probabilidade não estimável com os dados fornecidos” ou “baixa confiança”. Não gerar probabilidades numéricas sem evidência.

### Saída mínima

Resumo do requisito; classificação de testabilidade; principais achados; até três prioridades decisivas; cenários fundamentados; cenários condicionais ou pendentes; perguntas ao PO; riscos residuais; decisões humanas; relatório rastreável.

### Exclusões mantidas

Sem integração obrigatória com Jira/GitHub, acesso a repositórios de clientes, histórico automatizado, navegador exploratório, execução de testes, CI/CD, aprovação de deploy, gestão de impedimentos ou integração corporativa.

Dados do MVP demonstrativo serão exclusivamente sintéticos. A utilização de modelo de IA e seus custos, privacidade e condições operacionais ainda dependem de análise de viabilidade.

## 5. Jornada principal

**Inserir card → analisar → classificar testabilidade → revisar riscos e perguntas → priorizar → QA decide → exportar relatório.**

Exemplo preservado do v0.1: alteração do endereço de entrega de um pedido.

A IA deve questionar restrições após despacho, recálculo de frete, autorização e tratamento de falha. Se essas regras não estiverem disponíveis, deve separar o que é testável do que depende de esclarecimento.

O QA pode aceitar, alterar ou rejeitar recomendações, mantendo a distinção entre sugestão da IA e decisão humana.

**Nenhum cenário é declarado executado.**

## 6. Requisitos funcionais e critérios de aceite revisados

| ID | Requisito | Critério de aceite |
|---|---|---|
| **RF-M01** | Receber card e contexto opcional | Validar entradas obrigatórias; informar insuficiência de dados; não consultar fontes externas não autorizadas |
| **RF-M02** | Identificar problemas de testabilidade | Localizar contradições, ambiguidades e lacunas; separar fatos, inconsistências, hipóteses e perguntas; apontar trecho-fonte ou ausência de informação |
| **RF-M03** | Classificar e justificar riscos | Informar impacto, probabilidade qualitativa quando fundamentável, confiança e consequência potencial; não produzir precisão fictícia |
| **RF-M04** | Recomendar e priorizar testes | Destacar até três prioridades principais, preservar obrigatórios conhecidos, justificar seleção e riscos residuais; contemplar estados, limites, falhas, dependências, integração e regressão quando pertinentes |
| **RF-M05** | Permitir revisão humana | QA pode editar, selecionar ou descartar recomendações sem perder origem e decisão final |
| **RF-M06** | Gerar relatório rastreável | Registrar entrada, versão da análise, testabilidade, achados, evidências textuais, prioridades, perguntas, riscos residuais e decisões; marcar testes como não executados |
| **RF-M07 — novo** | Classificar testabilidade do card | Retornar exatamente uma das três classificações; explicar a classificação; impedir resultados esperados definitivos quando a regra correspondente for contraditória ou insuficiente |

### Critérios transversais de aceite

**CA-01 — Contradições:** perante critérios de aceite incompatíveis, a IA deve identificar a divergência e não escolher unilateralmente uma das regras como verdadeira.

**CA-02 — Evidência:** achados devem ser ligados ao texto fornecido ou explicitamente identificados como hipótese, inferência ou informação ausente.

**CA-03 — Priorização:** a análise principal deve ser acionável e concisa, preservando controles obrigatórios conhecidos mesmo além do limite preferencial de três prioridades.

**CA-04 — Profundidade:** quando estados, limites, falhas, dependências ou integrações forem relevantes, pelo menos os riscos materiais identificáveis nessas dimensões devem ser contemplados ou explicitamente sinalizados como não verificáveis.

**CA-05 — Incerteza:** ausência de regra, histórico ou evidência deve aparecer como limitação; não autoriza inventar probabilidade, comportamento, incidente ou integração.

**CA-06 — Controle humano:** sugestões podem ser modificadas ou rejeitadas; nenhuma resposta da IA representa execução, aprovação funcional ou liberação automática.

**CA-07 — Falha segura:** erro de processamento ou saída incompleta deve ser sinalizado, sem declaração artificial de análise concluída.

## 7. Conjunto sintético de referência — P1-02

Os cinco cards abaixo foram fornecidos no parecer consultivo do QA. **Os textos e gabaritos são preservados como referência para avaliação futura; não representam testes executados.**

### SYN-QI-01 — Cancelamento de pedidos
**Categoria:** Contradição

**Texto do card:**

“Permitir cancelar pedidos pagos até 24 horas após a compra. CA1: cancelamento permitido somente antes da separação. CA2: cancelamento permitido inclusive após a expedição.”

**Gabarito esperado:** detectar a contradição entre prazo e estado do pedido; sinalizar que não há regra inequívoca; perguntar qual condição prevalece e como funciona o estorno. Priorizar testes nas transições entre separado, expedido e cancelado, além do limite de 24 horas. Não inventar que o cancelamento pós-expedição é permitido ou proibido.

### SYN-QI-02 — Webhook de pagamento
**Categoria:** Risco negligenciado

**Texto do card:**

“Ao receber o evento de pagamento aprovado, atualizar o pedido para pago e liberar o produto. O provedor poderá reenviar eventos ou entregá-los fora de ordem.”

**Gabarito esperado:** destacar idempotência, concorrência e eventos fora de ordem como riscos prioritários; recomendar duplicação do mesmo evento e chegada de um evento antigo após um novo. Questionar validação da origem e regras de transição. Não assumir que existe assinatura ou mecanismo de deduplicação sem essa informação.

### SYN-QI-03 — Dashboard operacional
**Categoria:** Não testabilidade

**Texto do card:**

“O dashboard deve abrir rapidamente e exibir informações atualizadas em tempo real, mantendo uma experiência fluida.”

**Gabarito esperado:** apontar “rapidamente”, “tempo real” e “fluida” como critérios não verificáveis; solicitar limites de tempo, frequência ou latência de atualização, condições de medição e comportamento em falhas. Propor exemplos de critérios mensuráveis, sem apresentar valores sugeridos como requisitos aprovados.

### SYN-QI-04 — Alteração de e-mail
**Categoria:** Dependências e regressão

**Texto do card:**

“Permitir alterar o e-mail do usuário. Esse dado é utilizado para login, notificações e contato de faturamento. Outro card da mesma release altera o contrato de integração do campo `email` para `primary_email`.”

**Gabarito esperado:** identificar os três consumidores, o risco de incompatibilidade de contrato e a possibilidade de dados divergentes entre serviços. Priorizar teste de integração/regressão envolvendo alteração, autenticação e propagação. Perguntar sobre confirmação do novo endereço, compatibilidade durante a release e tratamento de atualização parcial. Não alegar que o diff real foi analisado.

### SYN-QI-05 — Remoção de etiquetas
**Categoria:** Regras insuficientes

**Texto do card:**

“Permitir que o usuário remova uma etiqueta utilizada em contatos. CA1: após remover, ela deve desaparecer da tela. Algumas etiquetas também são usadas em automações.”

**Gabarito esperado:** perceber que “remover” pode significar desvincular do contato ou excluir globalmente; questionar o impacto nas automações, autorização e histórico. Destacar risco de efeito colateral, mas não afirmar que a remoção deve apagar históricos ou interromper automações. Suspender a definição dos testes destrutivos até esclarecimento.

### Protocolo futuro de avaliação

Para cada card, comparar a análise produzida com o gabarito previamente estabelecido e registrar:

| Critério | O que avaliar |
|---|---|
| Detecção de riscos críticos | Reconhecimento do principal risco ou inconsistência esperado |
| Omissões críticas | Regras contraditórias, dependências e riscos relevantes não identificados |
| Falsos positivos | Afirmações, regras ou defeitos inventados |
| Justificativas | Relação verificável entre trecho, inferência e consequência |
| Priorização | Pertinência das escolhas e preservação de controles obrigatórios |
| Utilidade ao QA | Clareza da próxima ação e esforço real necessário para revisar a análise |

**Baseline comparativa:** fornecer os mesmos cinco cards, com entradas equivalentes, a um chatbot genérico com prompt padrão. Registrar condições da comparação e submeter os resultados aos mesmos critérios de avaliação.

Idealmente, o QA avaliador não deve conhecer qual saída pertence a cada solução antes da pontuação.

A futura comparação deve registrar acertos, omissões e falsos positivos, além do tempo de revisão quando medido. Não presumir superioridade da GenTests.ai nem estabelecer metas numéricas sem linha de base.

Cinco cards constituem uma amostra inicial de avaliação, não prova suficiente de prontidão comercial.

## 8. Riscos, dependências e premissas

**Riscos principais:**
- IA produzir regras ou evidências inexistentes.
- Classificar requisitos contraditórios como plenamente testáveis.
- Omitir riscos críticos enquanto gera muitos cenários secundários.
- Remover testes mandatórios para atender ao limite de concisão.
- Produzir recomendações tão genéricas que não superem um chatbot comum.
- Utilizar dados corporativos sem autorização.
- Assumir custo zero ou disponibilidade de modelos sem comprovação.

**Mitigações propostas:** fundamentação textual, classes explícitas de achado, incerteza, seleção priorizada, revisão humana, conjunto sintético de referência e avaliação comparativa.

**Dependências para eventual implementação:** estudo de viabilidade de Engenharia, escolha de modelo, comprovação de custos e privacidade, UX mínima e condições de avaliação funcional com QA.

Nenhuma dessas atividades está autorizada automaticamente por este documento.

## 9. Próximo incremento após o MVP

Preservada a recomendação do v0.1:

**I1 — Seleção Inteligente de Testes por Alteração.**

O produto evoluirá de “quais testes devem ser considerados?” para “quais testes existentes precisam ser executados diante desta mudança?”.

O primeiro estudo poderá usar alterações e catálogos de testes sintéticos. A leitura de PRs, diffs, código, histórico de bugs ou Jira reais dependerá de acesso autorizado e viabilidade específica.

Deverá justificar inclusões, exclusões, testes obrigatórios e riscos residuais.

## 10. Decisões efetivamente pendentes da Direção

1. **Aprovação conceitual** do Discovery v0.2 e manutenção do MVP de Análise Inteligente de Cards.
2. **Autorização posterior**, caso desejada, para Engenharia estudar viabilidade técnica, modelos de IA, privacidade e custos, sem implementar automaticamente.
3. **Autorização posterior** de prototipação/implementação, somente depois de conhecer viabilidade, escopo e condições de execução.

O detalhamento operacional dos critérios de avaliação, UX e arquitetura é competência das áreas especializadas quando legitimamente acionadas; não exige nova rodada documental de QA neste momento.

## 11. Referências e rastreabilidade

- Discovery de Produto v0.1 — proposta anterior de AGT-PROD.
- Parecer consultivo QA — “ADEQUADO COM AJUSTES”; cinco casos sintéticos e gabaritos preservados.
- `02-Agentes/Produto/Contrato-Agente-Produto.md` — AGT-PROD.
- `02-Agentes/QA/Contrato-Agente-QA.md` — AGT-QA.
- `03-Processos/Refinamento-Produto-UX-Handoff.md` — PRC-PROD-001.
- `03-Processos/GenTests-Quality-Framework.md` — GQF-001.
- `03-Processos/Ciclo-de-QA.md` — PRC-QA-001.
- `00-Constituicao/SEC-AI-001-Seguranca-Confiabilidade-Agentes.md` — SEC-AI-001.
- `00-Constituicao/Quality-Gates/QG-001-Politica.md` — QG-001.
- `GT-AI-DISPATCH-001`, issue #47 — iniciativa independente de despacho e orquestração, sem dependência bloqueante para este MVP.

**Limite das evidências:** os contratos, processos e políticas consultados incluem documentos em estado de proposta. A consolidação do Discovery não representa sua homologação.

**Estado da entrega:** v0.2 consolidado documentalmente pelo Produto. Não foram executados testes funcionais, revisão humana independente, desenvolvimento, integrações ou publicação. Aprovação conceitual e execução permanecem reservadas à Direção.