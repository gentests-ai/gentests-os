---
id: GT-PROD-CNB-001
produto: GT-PROD-CNB-001
tipo: visao-produto
versao: 0.1.0
status: proposta
estado_documental: em-validacao
data: 2026-10-10
timezone: America/Sao_Paulo
responsavel: Produto
elaborado_por: Agente de Produto
aprovador: Direcao
validacao_independente: pendente
implementacao: nao-autorizada
publicacao: bloqueada
---

# Calculadora de Custo da Não Qualidade de Software

**Entrega documental para revisão independente.** Não implementa calculadora, altera site, ativa dados, contrata serviços, faz merge ou autoriza ação comercial. Fonte canônica: esta pasta no gentests-os. ID CNB solicitado pela Direção preservado; CNQ continua sendo a identificação do guia.

## Visão e proposta de valor

Ferramenta gratuita que organiza as premissas de um incidente e calcula seu impacto econômico gerencial estimado, com memória de cálculo, parcelas não mensuradas e projeções condicionais. Permite discutir prioridades de qualidade com dados compreensíveis; não mede automaticamente perdas reais, não audita documentos e não calcula ROI de consultoria.

| Persona | Dor e tarefa | Valor oferecido |
|---|---|---|
| CTO/gestor de tecnologia de SaaS brasileiro | Precisa explicar impacto de incidentes além do ticket | Decomposição econômica transparente para discussão com finanças |
| Liderança de engenharia/QA | Horas dispersas entre investigação, correção e reteste | Registro de esforço único e orientação contra dupla contagem |
| Produto/operação/suporte | Créditos e cancelamentos sem conciliação com retrabalho | Separação entre recursos, despesas, ajustes e oportunidade |
| Financeiro como participante | Recebe totais chamados incorretamente de prejuízo/caixa | Premissas explícitas, naturezas segregadas e limites |

Personas são hipóteses de produto, não entrevistas realizadas. Validação proposta: observar cinco participantes voluntários em sessões autorizadas com exemplos fictícios; avaliar se conseguem explicar natureza, ausências e projeção. Quantidade é plano exploratório, não amostra estatística.

## Objetivos e limites comerciais

Apoiar descoberta orgânica e conversas qualificadas, complementando GT-MKT-CNQ-001. Conversão desejada: uso útil → consulta ao guia → pedido voluntário de contato → qualificação humana no CRM existente. Solicitar relatório não é autorização de prospecção; opt-in não é oportunidade qualificada. Não anunciar diagnóstico gratuito, desconto, oferta QA Express, preço, economia garantida ou equipe fictícia.

PLN-COM-001 0.2.0 mantém orçamento adicional zero e capacidade limitada; esta solicitação autoriza especificar o produto, não muda cronograma ou oferta do plano. Direção deve decidir esforço máximo e prioridade antes da implementação. Indicadores não herdam metas numéricas do funil de prospecção.

## Escopo proposto

- **MVP núcleo:** um incidente representativo; horas únicas por função; despesa emergencial, ajuste de receita e margem não recuperável distintos; resultado na tela; projeção mensal e anual; memória de cálculo e impressão local; exemplo explícito do guia; texto metodológico acessível.
- **MVP opcional condicionado:** envio do relatório por e-mail, projetado em detalhe, sem bloquear uso da calculadora; ativação depende de fornecedor, orçamento, bases, retenção e testes. Sua ausência não pode ser escondida como funcionalidade pronta.
- **Evoluções:** vários incidentes, distribuição de severidade, sensibilidade definida pelo usuário e importação local sanitizada.
- **Fora do escopo:** integrações Jira/produção/financeiro, login, upload de comprovantes, dados de clientes/pessoas, IA para preencher perdas, benchmarking setorial, inferência de churn/reputação, ROI, caixa, contabilidade, prevenção acrescida ao custo de falha, publicação e campanhas.

## Entregáveis e rastreabilidade

| Documento | Conteúdo |
|---|---|
| [Especificação funcional](Especificacao-Funcional.md) | Campos, regras RN, fórmulas e precisão |
| [Interface e jornada](Interface-Jornada.md) | Telas, estados, SEO, relatório e privacidade |
| [Arquitetura técnica](Arquitetura-Tecnica.md) | Contratos propostos, tecnologias, custos e eventos |
| [Aceite e testes](Aceite-Testes.md) | Matriz rastreável e resultados esperados sintéticos |
| [Backlog e decisões](Backlog-Riscos-Decisoes.md) | MVP, evoluções, dependências, risco e gates |

## Fontes efetivamente consultadas em 10/10/2026

| Fonte e referência imutável | Estado observado e uso |
|---|---|
| [Guia Executivo v0.4.1](https://github.com/gentestsai-sudo/gentests-os/blob/86121f4c1273a02c58f66ffa12af444a90b7abb0/comercial/GT-MKT-CNQ-001-Guia-Executivo-v0.4.1.pdf) | PDF recuperado e texto das cinco páginas extraído; SHA-256 declarado na PR #4 e recomputado na preparação. Conteúdo metodológico; não alegar nova aprovação visual |
| [Modelo CNQ-01 / documento 0.3.0](https://github.com/gentestsai-sudo/gentests-os/blob/86121f4c1273a02c58f66ffa12af444a90b7abb0/comercial/GT-MKT-CNQ-001-Custo-da-Nao-Qualidade.md) | Proposta; regras de conciliação e projeção; não extrapolar estudos macroeconômicos |
| [PR #4](https://github.com/gentestsai-sudo/gentests-os/pull/4) | Draft em 86121f4; revalidação visual pendente, distribuição não autorizada |
| [GT-LGPD-001 a 004 v0.2.1](https://github.com/gentestsai-sudo/gentests-os/tree/a5267ac594074bc1fc1d2c0e13b8815f78b36403/revisoes) | Quatro arquivos lidos integralmente; entrega e marketing separados, controles e pendências; sem comprovação de conformidade operacional |
| [DEC-LGPD-20261010-001 / PR #21](https://github.com/gentestsai-sudo/gentests-os/pull/21) e [encerramento / PR #22](https://github.com/gentestsai-sudo/gentests-os/pull/22) | Direcionamento registrado: guia por e-mail prioritário; adendos LGPD lidos. Encerramento documental não autoriza operação |
| [PLN-COM-001 v0.2.0](https://github.com/gentestsai-sudo/gentests-os/blob/a4c3f7606747f29acb6e11928889f962355c3ab7/04-Decisoes/PLN-COM-001-Primeiras-Vendas-GenTests.md) | Proposta integrada à main; CRM canônico, orçamento e capacidade; preços pendentes |
| [Governança main](https://github.com/gentestsai-sudo/gentests-os/tree/a4c3f7606747f29acb6e11928889f962355c3ab7/00-Constituicao) | POL-001–004 1.0.0, QG-001 0.1.0, SEC-AI-001 0.1.0 e GOV-5S-001 0.1.0 lidos; todos proposta |
| [GT-GOV-003 / PR #12](https://github.com/gentestsai-sudo/gentests-os/pull/12) | Pacote consultado para separar decisão, norma e configuração; não homologa políticas |
| [Site main](https://github.com/gentestsai-sudo/gentests-site/tree/fe4af7cd49f4d7446feb27519ec4f427e1c2c399) | README, contato.html e styles.css consultados; HTML/CSS/JS, FormSubmit→Gmail, noindex. Leitura main observada, não inspeção do deploy |
| [Site PR #1](https://github.com/gentestsai-sudo/gentests-site/pull/1) | Metadados em 04219e1 consultados; correções em draft, não incorporar silenciosamente como já publicadas |

Hash do PDF de referência: `646554cfdba296457af7d0bdc4b50783f2fe44a2841970fce48692a989f5038a`.
AGENTS.md na raiz dos dois repositórios não localizado (404). A busca de código do conector não retornou resultados; documentos não integrados foram localizados pelas PRs/branches e lidos em seus refs. Não foi realizada auditoria integral dos repositórios.

Fontes públicas técnicas e normativas, consultadas na preparação:
- [Cloudflare Pages: limites](https://developers.cloudflare.com/pages/platform/limits/) e [Functions: preços](https://developers.cloudflare.com/pages/functions/pricing/).
- [Cloudflare Email Service](https://developers.cloudflare.com/email-service/): envio transacional em beta; envio grátis a destinos verificados não prova gratuidade para visitantes arbitrários. Preço específico de envio não confirmado.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/): referência de acessibilidade.
- [LGPD, art. 8, Senado](https://normas.leg.br/?urn=urn%3Alex%3Abr%3Afederal%3Alei%3A2018-08-14%3B13709%21art8): consulta da regra de consentimento; texto geral depende de JS e Planalto apresentou bloqueio. Matriz jurídica deriva dos GT-LGPD lidos; base definitiva continua pendente de jurídico/Direção.

## Gate e histórico

Classificação proposta QG-H pelo componente financeiro e futura operação com dados pessoais; revisão independente e decisão humana conforme alcance solicitado. Esta entrega é preparação, não parecer. Versão 0.1.0: primeira especificação documental; nenhuma implementação/teste de produto realizado.
