ACEITO — Avaliação consultiva concluída

# 🧪 Parecer QA — GenTests Quality Intelligence

Avaliação: ADEQUADO COM AJUSTES.

O Discovery v0.1 apresenta uma direção correta para o MVP: analisar requisitos, antecipar riscos e ajudar o QA a decidir o que merece atenção. A proposta não precisa crescer em funcionalidades agora; precisa ficar mais exigente quanto à qualidade do raciocínio e à capacidade de reconhecer o que ainda não pode ser concluído.

A recomendação é preservar o escopo de análise de cards e acrescentar critérios objetivos que diferenciem inteligência preventiva de uma geração genérica de testes.

## 1. Pontos fortes que devem ser preservados

O Discovery já contempla os elementos certos:

- Análise de ambiguidades, contradições e lacunas dos requisitos.
- Priorização de riscos e seleção justificada de cenários, sem incentivo ao volume.
- Perguntas ao PO e recomendações de critérios de aceite.
- Rastreabilidade entre fonte, requisito, risco, teste sugerido e decisão humana.
- Entrada manual de contexto, sem obrigar integração Jira/GitHub no primeiro protótipo.

O maior potencial de economia está em reduzir retrabalho de refinamento e escolha de testes, não em produzir uma lista que o QA precisará revisar integralmente.

## 2. Lacunas e ajustes por prioridade

| Prioridade     | Ajuste recomendado                                                                      | Por que importa                                                                   |
| -------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| P0 — MVP       | Classificar o card como testável, parcialmente testável ou dependente de esclarecimento | Impede que a IA transforme requisitos incoerentes em testes aparentemente válidos |
| P0 — MVP       | Exigir referência textual e justificativa de cada achado relevante                      | Reduz invenções, repetição de alertas genéricos e falsos positivos                |
| P0 — MVP       | Priorizar até 3 riscos ou testes decisivos, com exceção para controles obrigatórios     | Torna a recomendação acionável e evita relatórios extensos                        |
| P1 — MVP       | Tornar explícita a análise de estados, limites, falhas, dependências e regressão        | Aproxima o raciocínio de um QA experiente                                         |
| P1 — Avaliação | Comparar resultado da IA com gabarito humano definido antes da execução                 | Permite medir omissões críticas e utilidade, não apenas fluência textual          |

Uma melhoria importante no RF-M03: probabilidade não deve receber precisão numérica fictícia. Sem histórico suficiente, o produto deve classificá-la como estimativa qualitativa, indicando baixa confiança ou informação insuficiente.

Também recomendo diferenciar quatro situações no resultado: fato extraído do card, inconsistência demonstrável, hipótese de risco e pergunta pendente. Essa distinção é fundamental para evitar falsas certezas.

## 3. Cinco cards sintéticos para avaliação futura

Os cinco cards abaixo são fictícios. As expectativas são gabaritos de referência para avaliar a qualidade das recomendações do MVP, não testes funcionais já executados.

SYN-QI-01 — Cancelamento de pedidos

Contradição

Texto do card

“Permitir cancelar pedidos pagos até 24 horas após a compra. CA1: cancelamento permitido somente antes da separação. CA2: cancelamento permitido inclusive após a expedição.”

Gabarito esperado: detectar a contradição entre prazo e estado do pedido; sinalizar que não há regra inequívoca; perguntar qual condição prevalece e como funciona o estorno. Priorizar testes nas transições entre separado, expedido e cancelado, além do limite de 24 horas. Não inventar que o cancelamento pós-expedição é permitido ou proibido.

SYN-QI-02 — Webhook de pagamento

Risco negligenciado

Texto do card

“Ao receber o evento de pagamento aprovado, atualizar o pedido para pago e liberar o produto. O provedor poderá reenviar eventos ou entregá-los fora de ordem.”

Gabarito esperado: destacar idempotência, concorrência e eventos fora de ordem como riscos prioritários; recomendar duplicação do mesmo evento e chegada de um evento antigo após um novo. Questionar validação da origem e regras de transição. Não assumir que existe assinatura ou mecanismo de deduplicação sem essa informação.

SYN-QI-03 — Dashboard operacional

Não testabilidade

Texto do card

“O dashboard deve abrir rapidamente e exibir informações atualizadas em tempo real, mantendo uma experiência fluida.”

Gabarito esperado: apontar “rapidamente”, “tempo real” e “fluida” como critérios não verificáveis; solicitar limites de tempo, frequência ou latência de atualização, condições de medição e comportamento em falhas. Propor exemplos de critérios mensuráveis, sem apresentar valores sugeridos como requisitos aprovados.

SYN-QI-04 — Alteração de e-mail

Dependências e regressão

Texto do card

“Permitir alterar o e-mail do usuário. Esse dado é utilizado para login, notificações e contato de faturamento. Outro card da mesma release altera o contrato de integração do campo `email` para `primary_email`.”

Gabarito esperado: identificar os três consumidores, o risco de incompatibilidade de contrato e a possibilidade de dados divergentes entre serviços. Priorizar teste de integração/regressão envolvendo alteração, autenticação e propagação. Perguntar sobre confirmação do novo endereço, compatibilidade durante a release e tratamento de atualização parcial. Não alegar que o diff real foi analisado.

SYN-QI-05 — Remoção de etiquetas

Regras insuficientes

Texto do card

“Permitir que o usuário remova uma etiqueta utilizada em contatos. CA1: após remover, ela deve desaparecer da tela. Algumas etiquetas também são usadas em automações.”

Gabarito esperado: perceber que “remover” pode significar desvincular do contato ou excluir globalmente; questionar o impacto nas automações, autorização e histórico. Destacar risco de efeito colateral, mas não afirmar que a remoção deve apagar históricos ou interromper automações. Suspender a definição dos testes destrutivos até esclarecimento.

## 4. Como medir inteligência de QA, não quantidade de respostas

Para cada um dos cinco cards, recomendo avaliar:

| Critério                   | Comportamento esperado                                               |
| -------------------------- | -------------------------------------------------------------------- |
| Detecção de risco crítico  | Identificar o principal problema previsto no gabarito                |
| Omissão crítica            | Não deixar passar contradições, dependências ou riscos obrigatórios  |
| Falso positivo             | Não inventar regras, integrações, incidentes ou defeitos             |
| Qualidade da justificativa | Relacionar cada achado ao texto fornecido e à consequência possível  |
| Priorização                | Escolher testes relevantes e explicar o que ficou fora               |
| Utilidade para QA          | Permitir que um profissional decida mais rapidamente o próximo passo |

Sugiro usar a mesma entrada em um chatbot genérico, com um prompt padrão, como baseline comparativa. O diferencial da GenTests.ai só ficará demonstrado se a análise especializada for mais pertinente, rastreável e econômica em tempo de revisão.

Os cinco cards constituem um conjunto inicial de avaliação, não evidência suficiente para afirmar que o produto está pronto para uso comercial.

## 5. Indispensável ao MVP versus evolução posterior

MVP

Análise semântica real, detecção de inconsistências, identificação de riscos, seleção justificada, perguntas de refinamento, incerteza explícita e revisão humana.

Evolução

Histórico de bugs, cards relacionados no Jira, PRs e diffs em leitura autorizada, mapeamento de dependências, seleção de testes existentes e execução automatizada.

A evolução técnica deve usar fontes externas como evidências identificáveis, com data, origem, versão e permissão de acesso. Um bug histórico relacionado aumenta a qualidade da hipótese, mas não prova que a mudança atual contém o mesmo defeito. Um diff pode indicar componentes afetados, mas não substitui verificação de comportamento. Esses limites precisam ser preservados na evolução do produto.

## 6. Conclusão para a Direção

Recomendo aprovar conceitualmente o Discovery v0.1, com os ajustes P0 incorporados antes de autorizar implementação. Manter a arquitetura e o recorte propostos por Produto, sem antecipar Jira, execução E2E ou acesso a repositórios corporativos.

O elemento mais importante do futuro framework deve ser a capacidade de declarar, com fundamento:

> “Existe uma contradição que precisa ser resolvida antes de implementar. Este é o risco mais relevante, esta é a evidência e estes são os testes que realmente importam.”

Essa é a diferença entre gerar casos de teste e apoiar decisões experientes de qualidade.

Fontes consultadas: Discovery de Produto v0.1, identificado no material disponibilizado pela Direção; [AGT-PROD](https://github.com/gentestsai-sudo/gentests-os/blob/main/02-Agentes/Produto/Contrato-Agente-Produto.md); [AGT-QA](https://github.com/gentestsai-sudo/gentests-os/blob/main/02-Agentes/QA/Contrato-Agente-QA.md); [PRC-QA-001](https://github.com/gentestsai-sudo/gentests-os/blob/main/03-Processos/Ciclo-de-QA.md); [GQF-001](https://github.com/gentestsai-sudo/gentests-os/blob/main/03-Processos/GenTests-Quality-Framework.md); [SEC-AI-001](https://github.com/gentestsai-sudo/gentests-os/blob/main/00-Constituicao/SEC-AI-001-Seguranca-Confiabilidade-Agentes.md) e [DISC-QA-001](https://github.com/gentestsai-sudo/gentests-os/issues/46). Os documentos institucionais consultados permanecem em estado de proposta quando assim identificados.

Natureza da entrega: análise documental consultiva, não teste funcional. Nenhuma issue, PR, branch, código ou integração foi criada ou modificada. Parecer destinado à Direção, para consolidação com Produto; não constitui aprovação formal nem revisão humana independente.