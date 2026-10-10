---
id: GT-PRC-REV-20261010
type: revisao-precificacao
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
