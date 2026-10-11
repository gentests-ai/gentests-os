---
tipo: processo
id: PRC-FIN-001
versao: 0.1.0
status: proposta
responsavel: Financeiro
aprovador: Direcao
---
# PRC-FIN-001 — Gestão financeira enxuta

## Objetivo
Garantir viabilidade econômica e rastreabilidade de preço, orçamento, faturamento, recebimento, conciliação e resultado por projeto, sem duplicar o pipeline comercial.

## Fluxo e responsabilidades
1. **Oportunidade:** Comercial entrega ID, escopo preliminar, expectativa do cliente e condições propostas. Não presumir venda fechada.
2. **Dimensionamento:** responsável técnico informa esforço, capacidade, dependências e riscos; todas as estimativas são hipóteses até aprovação.
3. **Precificação:** Financeiro calcula custos diretos/indiretos pertinentes, tributos estimados e margem de contribuição; apresenta cenários e premissas rastreáveis. Não confundir markup, lucro líquido e margem.
4. **Decisão:** Direção aprova preço, desconto, condições, orçamento e eventual compromisso. Comercial só envia proposta conforme autorização específica e processo comercial.
5. **Contratação e transferência:** somente após aceite contratual comprovado são registrados marcos de faturamento e responsáveis. Não criar cópias desnecessárias dos dados pessoais do CRM.
6. **Faturamento e cobrança:** Financeiro prepara dados e documentos; emissão/envio reais dependem de autorização, ferramenta habilitada e validação contábil/fiscal aplicável.
7. **Recebimento e conciliação:** registrar separadamente previsão, documento emitido, vencimento, valor efetivamente recebido, taxas e pendências, usando comprovante/registro bancário autorizado; status de mensagem não comprova pagamento.
8. **Análise:** acompanhar rentabilidade real e desvios por projeto, registrar causa e melhoria; evitar números fabricados e alegações de retorno sem comprovação.

## Registros mínimos
ID da oportunidade/projeto; cliente conforme necessidade e acesso mínimo; escopo; versão da proposta; preço aprovado; composição resumida de custos; premissas de impostos; aprovação e data; marcos; documentos emitidos; vencimentos; recebimentos efetivos e comprovantes referenciados; pendências e responsável. Financeiro guarda informações financeiras em fonte autorizada a definir, e Comercial mantém o registro único da oportunidade; não replicar dados sensíveis no Obsidian.

## Indicadores
- Receita contratada, faturada e efetivamente recebida (separadas).
- Contas a receber e vencidas.
- Despesa prevista e realizada por projeto.
- Margem de contribuição estimada versus realizada, quando houver dados suficientes.
- Fluxo de caixa previsto e realizado, com período e fonte.

Sem valor observado ou fonte confiável, indicar “não apurado”, nunca zero inventado.

## Controles e exceções
- Cada ação externa sensível demanda aprovação explícita da Direção e permissões reais.
- Não emitir documento fiscal sem verificação de enquadramento, retenções e requisitos aplicáveis por responsável competente.
- Aplicar [[00-Constituicao/Quality-Gates/QG-001-Politica]] conforme risco e [[00-Constituicao/SEC-AI-001-Seguranca-Confiabilidade-Agentes]] para segurança.
- Mudanças em preços/condições aprovados exigem nova deliberação; não sobrescrever histórico.
- Erros de conciliação ou evidência insuficiente devem ser registrados e escalados, sem compensações silenciosas.

## Interface
[[03-Processos/PRC-COM-001-Processo-Comercial]] conduz o funil, proposta e contrato; [[02-Agentes/Financeiro/Contrato-Agente-Financeiro]] define atribuições financeiras; a Direção decide compromissos. Este processo não altera ofertas já existentes ou libera ações comerciais.

## Pendências de implantação
Definir fonte autorizada dos registros financeiros, responsável por emissão fiscal, integração contábil, competências e comprovantes de autorização. Não afirmar que sistemas ou integrações já existem.

## Status
Proposta documental, sem homologação e sem criação de permissões técnicas.
