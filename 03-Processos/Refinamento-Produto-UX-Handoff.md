---
tipo: procedimento
id: PRC-PROD-001
versao: 0.1.0
status: proposta
responsavel: Produto
aprovador: Direcao
---
# PRC-PROD-001 — Refinamento Produto, UX/UI, Engenharia e QA

## Objetivo
Definir interfaces e critérios de prontidão entre Produto, UX/UI, Engenharia e QA, sem transformar cada atividade em gate burocrático nem autorizar implementação por meio desta nota.

## Fluxo enxuto
1. **Produto — descoberta e priorização:** problema, público, resultado esperado, dados disponíveis, hipóteses, dependências e limites.
2. **Produto + QA — refinamento:** regras funcionais, cenários críticos, critérios de aceite testáveis, riscos, dados e ambientes necessários.
3. **UX/UI — experiência:** jornada, estados, protótipos, acessibilidade, responsividade e padrões visuais; divergências de regras retornam a Produto.
4. **Engenharia + QA — viabilidade e qualidade:** restrições técnicas, segurança, observabilidade, estratégia de testes, estimativas como hipótese e limitações.
5. **Revisão e decisão:** aplicar [[00-Constituicao/Quality-Gates/QG-001-Politica]]; revisão independente por especialista sem participação no objeto quando exigida pelo risco; Direção delibera sobre investimento, mudança de escopo e início da execução.

As etapas podem ocorrer iterativamente e compartilhar evidências; não exigem cinco aprovações distintas.

## Matriz de responsabilidades
| Objeto | Responsável pela elaboração | Consultados | Decisão sensível |
|---|---|---|---|
| Problema, escopo, regras e prioridade | Produto | Comercial, UX/UI, QA, Engenharia | Direção |
| Jornada, protótipos, componentes e estados | UX/UI | Produto, Engenharia, QA | Direção quando houver impacto de escopo/publicação |
| Riscos, estratégia de testes e testabilidade | QA | Produto, UX/UI, Engenharia | Direção quando exigida autorização |
| Viabilidade, arquitetura e execução técnica | Engenharia | Produto, UX/UI, QA | Direção antes de implementação sensível |
| Revisão independente | Especialista designado sem conflito | Autor da entrega, Validador | Direção conforme Quality Gate |

## Pacote mínimo de handoff
- ID de iniciativa, objetivo, escopo, exclusões, versões e responsáveis.
- Regras e critérios de aceite rastreáveis; jornada/estados e protótipos aplicáveis.
- Riscos, hipóteses, limitações, dependências e decisões pendentes.
- Necessidades de acessibilidade, segurança, privacidade, ambiente e observabilidade.
- Estimativa explicitamente marcada como não aprovada até deliberação.
- Pareceres/evidências existentes e autorização humana exigida.

## Critério de pronto para implementação
Requisitos e interfaces suficientemente claros, divergências críticas resolvidas, riscos registrados, qualidade e viabilidade avaliadas, responsáveis definidos e autorização da Direção registrada. Documento, protótipo ou parecer técnico isolado não autoriza desenvolvimento, publicação ou acesso a produção.

## Restrições
Não alterar iniciativas existentes como GT-PROD-CNB-001 por consequência automática deste procedimento; preservar PRs, decisões e aprovações próprias. Não presumir testes de usabilidade ou acessibilidade executados. Este procedimento permanece proposta até homologação.
