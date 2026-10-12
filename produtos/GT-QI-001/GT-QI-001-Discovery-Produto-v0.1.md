# GenTests Quality Intelligence
**Nome provisório — Discovery de Produto v0.1**

**Estado:** PROPOSTA PARA AVALIAÇÃO DA DIREÇÃO  
**Data:** 12/10/2026  
**Responsável:** 📦 Produto — AGT-PROD  
**Escopo:** planejamento, sem implementação ou autorização operacional.

## 1. Visão e público-alvo

Transformar requisitos e mudanças de software em decisões de qualidade rastreáveis, utilizando IA e critérios de risco para apoiar o trabalho de profissionais de QA.

**Público inicial:** QAs, QA Leads, Tech Leads e Product Owners de equipes de desenvolvimento de produtos digitais, especialmente squads SaaS com entregas frequentes.

**Comprador potencial:** liderança de Engenharia, Qualidade ou Tecnologia.

**Proposta de valor:** menos tempo gasto identificando cenários pouco relevantes; maior atenção a falhas críticas, ambiguidades e riscos negligenciados.

O produto complementa o julgamento humano. Não substitui o QA nem declara uma funcionalidade aprovada automaticamente.

## 2. Problema e diferenciação

**Problema:** requisitos chegam incompletos, testes são frequentemente escolhidos por hábito, mudanças paralelas criam riscos não percebidos e equipes gastam esforço com regressões extensas sem justificar sua necessidade.

**Diferencial proposto:** combinar quatro elementos no mesmo fluxo:

- Interpretação de requisitos e identificação de lacunas.
- Priorização de riscos de negócio e técnicos.
- Recomendação e seleção justificada de cenários.
- Rastreabilidade entre requisito, risco, teste e decisão humana.

A diferenciação comercial ainda é uma hipótese a validar com usuários. Não há benchmark concorrencial concluído nem resultado de produtividade comprovado.

## 3. Evolução por incrementos

| Incremento | Capacidade | Resultado |
|---|---|---|
| **MVP** | Análise inteligente de cards | Riscos, ambiguidades, cenários e seleção justificada |
| **I1** | Seleção inteligente por mudança/PR | Identificar testes existentes relevantes e lacunas de cobertura |
| **I2** | Execução exploratória orientada por IA | Navegar em homologação, investigar comportamentos e registrar evidências |
| **I3** | Automação integrada ao ciclo | Testes por PR, E2E críticos no deploy, smoke seguro pós-deploy e regressão periódica em homologação |
| **I4** | Inteligência de fluxo e melhoria contínua | Impedimentos, dependências, gargalos e eficácia de ações corretivas |

Os incrementos representam uma ordem candidata, não cronograma ou autorização de execução. Monitoramento de pessoas e pontuação individual de produtividade ficam fora da proposta.

## 4. MVP recomendado — Análise inteligente de um card

**Escopo:** uma interface simples em que o usuário informa um card, solicita análise e recebe um plano de qualidade editável e rastreável.

**Entradas:**
- Descrição do card.
- Critérios de aceite existentes, quando disponíveis.
- Contexto e regras de negócio conhecidos.
- Dependências e restrições informadas manualmente.

**Saída do produto:**
1. Resumo interpretado do comportamento solicitado.
2. Ambiguidades, contradições e informações ausentes.
3. Riscos classificados por impacto, probabilidade estimada e incerteza.
4. Cenários sugeridos: positivos, negativos, limites, integrações e regressão, quando pertinentes.
5. Seleção prioritária dos testes, com justificativa e riscos residuais.
6. Perguntas ao PO/negócio e sugestões de critérios de aceite.
7. Relatório exportável com fonte, versão da análise, decisões e alterações humanas.

As classificações são recomendações. O sistema deve distinguir informação do card de hipótese da IA e nunca inventar histórico de bugs, dependências ou evidência de teste.

**Experiência mínima:** uma tela de entrada, uma tela de resultado e exportação Markdown/JSON. Não é necessário dashboard, banco corporativo, gestão de usuários empresariais ou integração com Jira/GitHub no MVP.

**Exclusões explícitas:** execução automatizada, navegador exploratório, leitura real de PR, acesso a repositórios de clientes, análise histórica automática, geração obrigatória de scripts, agendamento, aprovação de deploy e gestão de impedimentos.

**Justificativa:** o MVP permite demonstrar qualidade de raciocínio e utilidade prática antes de assumir a complexidade e os riscos de execução remota, ambientes, dados de clientes e automação E2E.

## 5. Jornada principal

**Card sintético → análise da IA → revisão pelo QA → plano priorizado → relatório.**

Exemplo demonstrativo:

**Card:** “Permitir alterar o endereço de entrega de um pedido.”

O sistema deve identificar perguntas como:
- Alterações são permitidas depois do despacho?
- O novo CEP modifica o frete?
- Quem pode alterar o endereço?
- O que acontece se a atualização falhar?

**Riscos propostos:** envio ao destino errado, cobrança inconsistente, alteração indevida e divergência entre pedido e logística.

**Testes priorizados:** alteração dentro da janela permitida; bloqueio após despacho; recalcular frete quando necessário; impedir alteração sem autorização; recuperar-se de falha de atualização.

Cada teste aponta para o requisito, risco ou hipótese que o originou. Regras não informadas permanecem pendentes de confirmação.

O QA pode aceitar, editar, acrescentar ou descartar sugestões e registrar o motivo. Nenhum teste é apresentado como executado.

## 6. Requisitos e critérios de aceite

| ID | Requisito funcional | Critério de aceite |
|---|---|---|
| RF-M01 | Receber card em texto e contexto opcional | Dados obrigatórios validados; entradas insuficientes sinalizadas |
| RF-M02 | Identificar problemas de testabilidade | Lacunas e ambiguidades associadas ao trecho original; ausência de informação não vira fato |
| RF-M03 | Classificar riscos | Impacto, probabilidade estimada, justificativa e incerteza explícitos |
| RF-M04 | Recomendar e priorizar testes | Cada cenário vinculado a requisito/risco; preservar testes obrigatórios conhecidos; justificar exclusões |
| RF-M05 | Permitir revisão humana | QA modifica seleção sem perder a distinção entre sugestão original e decisão final |
| RF-M06 | Gerar relatório rastreável | Incluir entrada/versionamento, análise, prioridades, pendências, riscos residuais e estado “não executado” |

**Aceite transversal:** nenhuma recomendação pode conceder acesso, executar ação externa, declarar teste aprovado ou inventar evidência. Falha do modelo gera estado de erro explícito, sem apresentar análise parcial como conclusiva.

**Validação funcional futura:** usar pequeno conjunto de cards integralmente sintéticos, incluindo requisitos ambíguos, casos simples, regras conflitantes, testes mandatórios e dados insuficientes. Um QA avaliará relevância, omissões críticas, falsos positivos, clareza e tempo de revisão. As expectativas deverão ser definidas antes da medição, sem transformar a própria resposta da IA em gabarito.

## 7. Hipóteses, riscos e dependências

| Dimensão | Hipótese ou risco | Tratamento proposto |
|---|---|---|
| Valor | QA encontra lacunas úteis com menos esforço | Comparar análise humana isolada com análise assistida, medindo tempo e aceitação |
| Confiabilidade | IA pode inventar regras ou omitir riscos | Referências à entrada, incerteza explícita, checagens determinísticas e revisão humana |
| Seleção | Redução excessiva pode excluir testes críticos | Testes obrigatórios protegidos e expansão da cobertura quando houver incerteza |
| Segurança | Exposição de dados corporativos ao modelo | MVP com dados exclusivamente sintéticos; aprovação de provedor/retencão antes de uso real |
| Custos | Gratuidade e cotas de inferência não garantidas | Comparar execução local elegível e API gratuita, sem assumir R$0; escolher depois da verificação |
| Engenharia | Qualidade varia por modelo e prompt | Avaliação estruturada com casos de referência versionados |
| Comercial | Valor percebido pode não justificar compra | Demonstração a QAs/lideranças e descoberta de disposição a pagar antes de escala |

O MVP deve realmente utilizar capacidade de IA para análise semântica. Regras determinísticas podem complementar o modelo, mas não devem ser anunciadas isoladamente como inteligência generativa.

**Dependência do provedor de IA:** ainda pendente de viabilidade e autorização. Não há modelo, contrato de dados, disponibilidade de conta ou custo zero comprovados para este produto.

## 8. Reutilização de ativos oficiais

**Reutilizar como referências, sem confundir propostas com normas homologadas:**

- **GQF-001:** metodologia interna de qualidade baseada em risco e evidência; não é ainda o produto comercial.
- **PRC-QA-001 e AGT-QA:** princípios para avaliação de riscos, testabilidade e evidência.
- **SEC-AI-001 e QG-001:** segurança, confiança, separação de fatos e hipóteses, revisão proporcional.
- **DISC-QA-001 (#46) e GT-AI-LEARN-001 (PR #8):** taxonomia e abordagem de casos de avaliação controlados, quando autorizados.
- **GT-AI-DISPATCH-001 (#47):** infraestrutura de despacho candidata a integração futura, não dependência do MVP.
- **GT-MISSION-CONTROL-001 (#58):** conceitos de evidência, eventos e impedimentos reaproveitáveis em evolução posterior, sem incorporar o painel ao MVP.

As fontes citadas possuem propostas em diferentes estágios. Nenhum desses registros autoriza automaticamente implementação, integração ou publicação deste produto.

## 9. Primeiro incremento após o MVP

**I1 — Seleção inteligente de testes por alteração.**

Adicionar entrada estruturada contendo mudanças de código/funcionalidade e um catálogo pequeno de testes já existentes, inicialmente sintéticos.

O sistema deverá identificar testes obrigatórios, selecionar testes relacionados, explicar por que outros testes foram omitidos e sinalizar riscos sem cobertura.

Somente após essa validação faria sentido integrar PRs reais e, posteriormente, automatizar a execução.

Essa evolução tem relação direta com o valor do MVP: passa de “quais testes deveriam existir?” para “quais testes existentes devo executar nesta alteração?”.

## 10. Recomendação e próximo gate

**Produto recomenda aprovar conceitualmente o MVP de Análise Inteligente de Cards para avaliação de viabilidade e protótipo futuro.**

Antes de iniciar desenvolvimento, confirmar apenas três pontos: usuários e problema inicial, critérios de avaliação com QA e viabilidade de modelo com custo/privacidade aceitáveis.

**Estado:** discovery documental concluído; mérito e execução aguardam avaliação da Direção. Não foram realizados testes funcionais, implementação, integração, validação independente ou comprovação comercial.

Nenhuma issue, PR, credencial ou serviço foi criado. Não houve alteração no GitHub.