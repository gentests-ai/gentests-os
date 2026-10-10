---
id: GT-PROD-CNB-001-FUN
produto: GT-PROD-CNB-001
tipo: especificacao-funcional
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

# Especificação funcional e regras de negócio

Referência metodológica: README/fontes e CNQ-01. Todas as escolhas de UX, precisão, limites e decomposição abaixo são propostas de engenharia para deliberação, não fórmulas financeiras novas homologadas.

## 1. Unidade, proveniência e preenchimento

**RF-01:** um incidente representativo identificado apenas por código local gerado (ex.: INC-LOCAL-1). Reabertura pertence ao mesmo incidente; registrar só esforço adicional. Incidentes diferentes não são somados no MVP. Defeito e incidente não são unidades intercambiáveis: frequência é de incidentes únicos do mesmo perfil, não de tickets/bugs.

Cada grupo oferece estado explícito `informado`, `hipotetico`, `desconhecido` ou `nao_aplicavel`; valores vazios começam desconhecidos. Zero é valor informado somente quando digitado/confirmado; N/A exige escolha explícita. Origem informada é declaração do usuário, **não auditada**. Hipotético é cenário assumido, inclusive exemplo do guia. Calculado é um valor derivado, que preserva a origem dos operandos. A UI mostra ambos: “Calculado · com valores informados” ou “Calculado · contém hipóteses”. Nunca classificar número digitado como perda comprovada.

**RF-02:** iniciar vazio, sem médias de mercado ou frequência padrão. “Carregar exemplo fictício do guia” é ação explícita; confirma substituição de dados já preenchidos e marca todos os operandos hipotéticos. Restaurar/limpar remove o estado em memória após confirmação quando houver preenchimento; não envia dados.

## 2. Dicionário de entradas

| ID/campo | Tipo/unidade e obrigatoriedade | Validação e ajuda |
|---|---|---|
| IN-01 modo | estimativa própria / exemplo fictício | Estimativa própria inicial; exemplo só por ação explícita |
| IN-02 papel do bloco de horas | enum dev, QA, suporte, operação/outro técnico | Três blocos dev/QA/suporte iniciais; operação opcional; papel não impõe salário |
| IN-03 horas únicas | decimal h, até 2 casas; obrigatório se bloco ativo | 0 a 10.000 h/bloco; horas-pessoa agregadas já deduplicadas, não duração do incidente × tamanho da equipe |
| IN-04 custo-hora integral | BRL/h até 2 casas; obrigatório se horas >0 | 0 a R$100.000/h; taxa zero com horas >0 requer confirmação “custo zero informado”; desconhecido impede valorar o bloco |
| IN-05 esforço/atividade | orientação fixa por papel | Investigar/corrigir/retestar/retrabalho compõem horas, não novos multiplicadores; sem texto livre ou pessoa |
| IN-06 confirmação de unicidade de horas | sim / não sei | Incluir horas somente se sim; não sei deixa parcela fora do total conciliado e visível como não mensurada |
| IN-07 despesa externa incremental | BRL, até 2 casas, opcional | 0 a R$1 bilhão; confirmar não incluída na taxa/contrato fixo; só parcela atribuível ao incidente |
| IN-08 ajuste líquido de receita | BRL, até 2 casas, opcional | Mesmo limite; crédito/estorno líquido atribuível. Não presumir desembolso |
| IN-09 margem líquida não recuperável | BRL, até 2 casas, opcional | Mesmo limite; usuário informa margem já apurada com financeiro. Não aceitar faturamento bruto como margem |
| IN-10 reconciliação de efeitos | referência local anônima de evento/transação e confirmação de distinção | Referências internas geradas/selecionadas, sem número real de pedido ou cliente; parcelas ligadas ao mesmo evento ficam bloqueadas até resolver overlap |
| IN-11 frequência mensal | inteiro incidentes/mês, opcional | 0 a 100.000; mesma classe/perfil do incidente e origem informada/hipotética; ausente = mês/ano não calculáveis |
| IN-12 horizonte | fixo 12 meses no MVP | Exibir hipótese de custo e frequência constantes; não receita/custo anual observado |
| IN-13 indisponibilidade | opcional: duração decimal em h até 2 casas | 0 a 744 h para referência mensal; degradação parcial pode ser informada em nota fixa. Não monetiza nem soma ao total |
| IN-14 estado e origem de cada grupo | enums citados no §1 | Não aceitar estado informado/hipotético sem operandos válidos |
| IN-15 e-mail / marketing | apenas fluxo opcional de relatório | Fora do cálculo; especificado em Interface-Jornada |

Limites são proteção de entrada e domínio do MVP, não máximos econômicos universais. Exceder produz erro “fora do limite desta ferramenta”, sem truncar ou saturar; ampliar exige revisão. Até 4 blocos de horas; uma parcela por natureza não horária no MVP. Para despesas múltiplas, usuário concilia soma externamente e informa agregado sem upload. Referências locais orientam conciliação, não provam distinção documental.

**RN-01 parsing:** aceitar pt-BR inequívoco: `1.234,56` ou `1234,56`; inteiro sem agrupamento também. Não aceitar ponto decimal, expoente, hexadecimal, infinito, NaN, negativos, sinais, texto, símbolos colados ou mais de 2 casas. Campo já indica unidade; erro sugere exemplo válido. Agrupamento precisa de blocos de três dígitos. Remover só espaços externos; `1,234` é inválido. Não converter vazio em zero. O futuro endpoint deve aplicar as mesmas regras sobre representações canônicas, sem confiar no cliente.

## 3. Fórmulas preservadas e memória

**RN-02:** cada bloco elegível `R_i = horas_unicas_i × custo_hora_integral_i`.
**RN-03:** `R = soma R_i`; `E = despesa externa incremental distinta`; `A = ajuste líquido de receita distinto`; `O = margem de contribuição líquida não recuperável distinta`.
**RN-04:** `T = R + E + A + O`, somente parcelas elegíveis não sobrepostas. Esta é a fórmula gerencial CNQ-01 do guia. O total é condicionado à conciliação do usuário, não valor comprovado.
**RN-05:** `M = T × N`; `Y = M × 12`, com N incidentes mensais do mesmo perfil e T/N constantes. São projeções nominais, sem inflação, desconto, impostos, juros, probabilidades ou significância. N não é medição automática de recorrência.
**RN-06:** não fornecer ROI, retorno, caixa incremental ou resultado contábil. Não somar custo de prevenção ao custo de falha. Não aplicar fatores 10×/100× por fase de detecção.

Precisão proposta: representar horas em centésimos de hora e taxas/valores em centavos, como inteiros decimais; multiplicar sem ponto flutuante binário. Arredondar cada bloco R_i a centavos por half-up (`(horas_centésimos × taxa_centavos + 50) div 100`); somar parcelas já arredondadas. M/Y multiplicam T em centavos por inteiros, sem novo arredondamento intermediário. Exibir BRL pt-BR e memória que explique o arredondamento. Subtotal por incidente deve ser ≤R$10 bilhões e projeção anual ≤R$1 trilhão; exceder bloqueia resultado e orienta avaliação específica. Usar inteiro seguro ou BigInt/decimal, nunca deixar overflow silencioso.

## 4. Ausências, conflitos e apresentação

**RN-07:** grupo desconhecido, invalidado ou com sobreposição não entra na soma; mostrar motivo, quantidade de grupos excluídos e “Subtotal estimado das parcelas mensuradas — estimativa incompleta”. Nunca apresentar esse subtotal como custo integral. Não publicar intervalo estatístico ou “mínimo comprovado”.

**RN-08:** todos desconhecidos/N/A sem parcela informada → nenhum resultado monetário (“Informe ao menos uma parcela”); todos conhecidos explicitamente zero → R$0,00 para parcelas consideradas, sem concluir ausência de impacto reputacional. N/A confirmado é exclusão de escopo, não custo mensurado zero; relatório lista N/A.

**RN-09:** conflito em horas/efeitos impede **total completo**; subtotal não conflitante ainda pode ser mostrado com aviso. Para duas parcelas ligadas ao mesmo evento (ex.: ajuste e oportunidade), excluir ambas até usuário remover uma ou declarar e conciliar parcelas incrementais distintas. Mudanças invalidam a confirmação afetada; o sistema não escolhe automaticamente a maior para inflar custo.

**RN-10:** salários já incluídos no custo-hora não são lançados outra vez; tempo de investigação/retrabalho não soma novamente ao bloco de dev/QA. Serviço de fornecedor incluído na taxa/contrato fica fora. Crédito da mesma venda não recuperável não soma à margem da mesma transação sem parcela distinta conciliada.

**RN-11:** indisponibilidade é contexto. Horas do time durante outage já entram em R. SLA/crédito entra em A ou E conforme natureza validada; margem de vendas não recuperadas entra em O se distinta. Não usar receita/hora × downtime como perda automática. Receita adiada/recuperada não é oportunidade perdida. Churn, reputação, produtividade de cliente, multa potencial e estoque de dívida técnica são impactos “não monetizados” no MVP, sem valores padrão ou inclusão genérica em T. Futuras rubricas exigem análise financeira e versão metodológica.

**RF-03 resultado:** quatro naturezas segregadas, T ou subtotal, M/Y quando N válido, memória por linha, origens, excluídos e limites. Se T incompleto, M/Y também recebem “Projeção apenas das parcelas mensuradas”. N desconhecido → M/Y “não calculável”, não zero. N=0 → projeções R$0,00 pela hipótese, preservando T do incidente. Um incidente real isolado não prevê doze meses.

**RF-04 atualização:** edição marca resultado anterior “desatualizado” e desabilita relatório; recalcular após validação explícita. Resultado mantém snapshot imutável de entradas/estados/metodologia; nunca mistura novas entradas com total anterior.

## 5. Exemplo canônico para demonstração

| Parcela | Cálculo/hipótese | Resultado |
|---|---|---:|
| Dev | 12h × R$120 | R$1.440 |
| QA | 6h × R$90 | R$540 |
| Suporte | 4h × R$70 | R$280 |
| Recursos | soma das horas únicas | R$2.260 |
| Externo | evento distinto | R$600 |
| Ajuste | cliente A fictício | R$900 |
| Oportunidade | margem da venda do cliente B fictício | R$1.000 |
| T | eventos distintos hipotéticos | R$4.760 |
| M | T × 3 incidentes/mês | R$14.280 |
| Y | M × 12 | R$171.360 |

Todas as origens hipotéticas; fontes de evidência não anexadas. Exemplo não equivale a receita perdida ou caixa de R$4.760. Não é benchmark nem economia proporcionada pela GenTests.ai.
