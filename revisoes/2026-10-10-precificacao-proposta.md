---
id: GT-PRC-REV-20261010
type: revisao-precificacao
versao: 0.2.0
status: proposta
date: 2026-10-10
owner: direcao
approval: pendente
source_catalog: https://drive.google.com/file/d/1RI-UDm9iXxfWbzEBhVs_6fmRdf32z95z/view
source_pricing: https://docs.google.com/document/d/1lrW3yzt3Cpa_va7WiSLmXwDI3NZ43wx-D0WE9mzcQMA/edit
source_finance: https://docs.google.com/document/d/14or94GuueTRNCJ4M-MIEKLAVMKIWa0Th6BsdySbSScM/edit
crm: https://docs.google.com/spreadsheets/d/151zLp3akkkbdeA6D44EOAsefT9gjygvv0ZMsGRZ3WV0/edit
tags: [pricing, quality, commercial, financial, traceability]
---

# Revisão controlada de precificação — 10/10/2026

> Análise original preservada. Perguntas e gates abaixo devem ser lidos com o adendo final. Plano canônico: [[04-Decisoes/PLN-COM-001-Primeiras-Vendas-GenTests]]; decisão: [[04-Decisoes/Primeiro-PIX-Homologacao-Comercial]].


> **Status: PROPOSTA — não homologado.** Não altera catálogo nem autoriza novos preços. Códigos de artefato A01–A09 são os identificadores já existentes no catálogo. O ID desta revisão é temporário e deve ser conciliado ao registro/índice do vault no Obsidian antes da publicação.

## Origem e motivo
Solicitação da direção: conciliar catálogo comercial de 09/10/2026 com política de precificação e dados financeiros de 10/10/2026; quantificar riscos de margem; preservar a rastreabilidade do GenTests OS. O README do repositório estabelece que documentos em proposta não estão aprovados, exigindo aprovação expressa para alterações de políticas.

## Matriz de escopo e divergências

| Serviço | Preço catálogo v1 | Prazo | Escopo já registrado | Divergência |
|---|---:|---|---|---|
| QA Express | R$ 690 | 2 dias úteis | até 5 páginas públicas OU 1 jornada simples; A01 simplificado, A02 resumido, A03, A04 quando aplicável, A05 sintético | Política nova usa 6h × R$150 = R$900 *somente componente de mão de obra*; orçamento sem compatibilização |
| Auditoria Funcional | R$ 1.800 | 4 dias úteis | até 3 jornadas; critérios recebidos, risco, fluxos principais/alternativos; A01,A02,A03,A04,A05,A07 | Política nova fala em diagnóstico de processos e riscos a 12h/R$1800, mas não é necessariamente o mesmo produto; não substituir escopo |
| Auditoria de Processos QA | R$ 2.900 | 5 dias úteis | entrevistas + 1 fluxo de entrega; requisitos, aceite, governança, métricas e observabilidade; A01,A05,A06,A09 | Política usa 20h/R$3000 para revisão estratégica, com escopo distinto; exigir estimativa por tarefas |

## Premissas e margem preliminar
Dados: remuneração PJ recente R$12.120/mês; 40h/semana habituais; referência bruta equivalente R$69,92/h (aproximada). **Esse valor não é custo empregatício contábil**, mas um indicador de custo de oportunidade. Preço-hora comercial experimental: R$150/h; não é simultaneamente custo de execução e margem pretendida.

Para simulação apenas: DAS = 6% sobre preço (não confirmado por tipo de serviço); custos incrementais + rateio = R$50 Express / R$100 Funcional / R$150 Processos; não incluir novamente toda contabilidade/ChatGPT. Fórmula: sobra = preço - (preço × 6%) - (horas × R$69,92) - custos atribuídos. Margem gerencial = sobra/preço. Reserva de tecnologia de 10% é distribuição **posterior** sobre resultado disponível, não despesa na fórmula.

| Serviço | Horas cenário enxuto | Sobra enxuta | Margem enxuta | Horas cenário pesado | Sobra pesada | Margem pesada |
|---|---:|---:|---:|---:|---:|---:|
| QA Express R$690 | 4h | R$318,92 | 46,2% | 8h | R$39,24 | 5,7% |
| Auditoria Funcional R$1800 | 12h | R$752,96 | 41,8% | 20h | R$193,60 | 10,8% |
| Auditoria Processos QA R$2900 | 20h | R$1.177,60 | 40,6% | 32h | R$338,56 | 11,7% |

Esses resultados são **margens gerenciais ilustrativas**, não lucro fiscal. Não incluem todos os custos de prospecção, ociosidade, incidentes ou risco tributário. Se usássemos R$150/h como custo-alvo de entrega, o QA Express consumiria R$600 em apenas 4h, antes de R$41,40 de imposto hipotético e R$50 de custos: resultado **-R$1,40**. Os preços não são homologáveis ainda.

## Sensibilidade tributária
Antes de confirmar PGDAS-D, fator R quando aplicável e código da NFS-e, simular também DAS de 15,5%. A variação de 6% para 15,5% reduziria a sobra em R$65,55 (Express), R$171 (Funcional) e R$275,50 (Processos), mantendo demais premissas. Nenhum cenário determina regime jurídico/fiscal real.

## Análise de impacto
- Catálogo Comercial Pacotes 2026: preservar v1; abrir decisão de preço/escopo por SKU e aprovar antes de editar.
- Política de Precificação v1: marcar cenários como hipóteses, explicar diferença entre preço-hora e custo de oportunidade.
- CRM abas Precificacao/Metas_Financeiras: ferramenta gerencial em rascunho; inserir flag PENDENTE HOMOLOGAÇÃO; conferir se cálculo conta margem e contingência uma só vez.
- Propostas comerciais: não cotar QA Express novo valor até aprovação; propostas personalizadas devem usar ofertas e condições aprovadas.
- Artefatos: QA Express A01/A02/A03/A04/A05; Funcional A01/A02/A03/A04/A05/A07; Processos A01/A05/A06/A09. Garantir alinhamento entre contrato, evidências e aceitação.
- IA e tecnologia: ChatGPT Plus R$99/mês, contabilidade R$109/mês; ratear só parcela atribuível. Business/API são planejamento futuro. Fundo MacBook Pro R$30 mil, capital de giro e contratações são metas condicionadas a fluxo de caixa, não despesas diretas já incorridas.
- Governança: não armazenar extratos pessoais, dados bancários, CPF ou documentos societários completos no vault.

## Critérios para homologação
1. Contador informa anexo, alíquota efetiva da receita de cada serviço e forma de emissão da NFS-e.
2. Estimativa detalhada e temporizada para cada artefato, revisão, reuniões e comunicação.
3. Estimar custos de IA, rateio e limites de retrabalho; margem alvo aprovada pela direção.
4. Executar piloto mensurando horas, aceitação, qualidade e despesas.
5. Documentar decisão de manter/alterar preço com versão, justificativa, aprovador e data.
6. Sincronizar link da decisão na nota Obsidian existente e conferir backlinks para catálogo, política, CRM e artefatos.
7. Somente após aprovação, modificar catálogo e propostas.

## Decisões pendentes
- Manter QA Express a R$690 com escopo mais restrito ou reposicionar preço? A definir com custo medido.
- Qual margem mínima aprovada? Pendente.
- Quanto tempo de execução real para cada pacote? Pendente.
- Qual o arquivo índice oficial e o formato de IDs no vault Obsidian completo? Não confirmado na versão atual do repositório.

## Trilha de evidências
Fontes: Catálogo Comercial Pacotes 2026 (Drive), Política de Precificação (Drive), Planejamento Financeiro e Roadmap (Drive), CRM (Sheets), contrato social e guias fornecidos em conversa. Não copiar documentos sensíveis para GitHub. Revisão criada em branch, sujeito a PR e homologação.


## Adendo de 10/10/2026 — Condições de lançamento e faturamento (PROPOSTA)
Solicitação da direção: priorizar primeiro cliente pagante, aceitando redução deliberada de margem com controle de custo, sem promover aprovação automática de preço. Campanha experimental limitada aos primeiros **3 clientes**, condicionada à homologação individual antes de ofertar.

| Oferta | Catálogo de 09/10 | Condição de lançamento proposta | Redução |
|---|---:|---:|---:|
| QA Express | R$690 | R$490 | R$200 (29,0%) |
| Auditoria Funcional | R$1.800 | R$1.490 | R$310 (17,2%) |
| Auditoria de Processos QA | R$2.900 | R$2.490 | R$410 (14,1%) |

Atenção: premissas gerais anteriores de margem foram calculadas com preços de catálogo, **não** com promoções. Antes de ofertar, recalcular impostos e cenários de horas pelo preço promocional e fixar tetos de esforço. Recomenda-se não cobrar abaixo de custos diretos, tributos e remuneração imputada à execução. Se não houver margem, reduzir escopo autorizado ou rejeitar oferta.

### Faturamento proposto
**Fonte preexistente:** o Catálogo Comercial de 09/10/2026 já contém regra **sugerida** de pagamento de **50% na aprovação e 50% na entrega**, além de marcos alternativos em projetos complexos; esta revisão propõe torná-la **padrão a homologar**, não declara aprovação preexistente. Para três propostas promocionais:

- 50% como sinal/primeira parcela na formalização contratual e antes de iniciar a execução; 50% no aceite formal de entrega delimitada por evidência e prazo de validação previsto em contrato. Definir prazo de pagamento explícito e gatilho objetivo para cobrança.
- Parcelamento diferente, antecipação integral ou serviços recorrentes: exceção só mediante aprovação específica, análise de risco de crédito e caixa; a empresa não deve financiar execução sem controle.
- Emitir NFS-e conforme regra municipal/competência e orientação contábil; **não presumir** que o momento do pagamento é o momento fiscal da emissão.
- Definir suspensão, inadimplência, cancelamento, reembolso e mudanças de escopo com advogado/contador antes de fechar modelo contratual; não impor retenção não reembolsável sem análise jurídica.
- Conferir dados de cobrança com o responsável financeiro do cliente; não inserir dados bancários em repositório público nem no Obsidian.
- Critério operacional: 'contrato aceito + pagamento de entrada comprovado' é marco de início, mas aceite de entrega e recebimento final têm status separados no CRM.

### Simulação do caixa (valores promocionais; ainda não aprovados)
QA Express R$490: 50% R$245 na contratação + R$245 na entrega.
Auditoria Funcional R$1.490: R$745 + R$745.
Auditoria de Processos QA R$2.490: R$1.245 + R$1.245.

### Próximos gates
[ ] Contador confirma alíquota efetiva, CNAE/código de serviço, NFS-e, regime de competência.
[ ] Direção decide campanha, preço por SKU, prazo da condição, limite de clientes, margem mínima e esforço máximo.
[ ] Jurídico/revisor valida cláusulas de adiantamento, cancelamento, aceite, suspensão e parcelamento.
[ ] Atualizar catálogo, modelo de proposta e CRM **somente após aprovação** e sincronizar o backlink no Obsidian.
[ ] Autorizar separadamente cada contato comercial antes de envio.

## Revisão executiva da solicitação de 10/10 — execução comercial
A direção solicitou validação tributária, contratual, homologação de preços e apresentação visual. Decisão tratada como **autorização de preparação comercial**, não confirmação técnica de tributos ou de cláusulas jurídicas ainda não revisadas. Os preços R$490 / R$1.490 / R$2.490 são a **tabela promocional escolhida comercialmente pela direção**, limitada a 3 clientes pioneiros, sujeita à validação final da margem com a tributação e o contrato definitivos antes de emissão de propostas vinculantes. O catálogo de 09/10 não foi alterado. A presente nota mantém status proposta e exige incorporação ao Vault Obsidian e revisão de PR.

### Evidência oficial consultada
- Artigo 597 do Código Civil (Lei 10.406/2002): remuneração pode ser convencionada adiantada ou parcelada. Fonte https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm
- Resolução CGSN 140/2018: classificação das receitas e fator R, quando aplicável, podem alterar o anexo; não extrapolar DAS anterior para novos serviços. Fonte https://normas.receita.fazenda.gov.br/sijut2consulta/normas.receisulta/link.action?idAto=92278&visao=compilado
- Prefeitura Curitiba NFS-e: https://servicos.curitiba.pr.gov.br/iss-curitiba-acesso-ao-sistema-emissao-da-nota-curitibana-nfs-e/601

### Entregável visual
Apresentação comercial em PowerPoint editável de 7 slides gerada em 10/10/2026, pendente de revisão visual final e publicação no Drive. Sem valores que dependam de homologação fiscal. Não alegar case ou resultado não comprovado.

### Condições mínimas do contrato comercial a revisar
Objeto/escopo; ativos autorizados; dependências e acesso; direitos sobre relatório/evidências; proteção de dados e sigilo; marcos de 50% na assinatura e 50% na entrega com aceite objetivo e prazo de contestação; limites de reteste; alteração de escopo; atrasos por parte do contratante; emissão de NFS-e em competência fiscal aplicável; cancelamento, reembolso proporcional, inadimplência e resolução de controvérsias. Não tratar como parecer jurídico.

## Consolidação — Campanha dos Três Primeiros Clientes
Cíntia esclareceu em 10/10 às 11:50–11:51 que a redução de margem visa conquistar os três primeiros clientes e solicitou campanha única e novo nome. Tabela de consolidação: R$ 490 / R$ 1.490 / R$ 2.490, três clientes no total compartilhados entre serviços. R$ 890/seis horas do plano anterior é hipótese histórica.
As perguntas anteriores sobre decidir a existência da campanha são superadas pela diretriz registrada. Estimativa total, tributação efetiva, custos e condições específicas continuam dependentes da análise atual e revisão. A consolidação não conferiu documentos contábeis completos nem certifica seus resultados.
Publicação do PPTX no Drive já registrada no [[comercial/apresentacao-comercial-v2-proposta|roteiro]]; a menção anterior a publicação pendente está desatualizada. Revisão visual permanece pendente. Binário original preservado.
Decisão: [[04-Decisoes/Primeiro-PIX-Homologacao-Comercial]]. Escopo: [[07-Templates/QA-Express-Oferta-Piloto]]. Não alterar automaticamente catálogo, Drive ou CRM. Esta é a referência financeira, não um plano comercial concorrente.
