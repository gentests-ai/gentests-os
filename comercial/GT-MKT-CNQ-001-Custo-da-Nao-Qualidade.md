---
id: GT-MKT-CNQ-001
tipo: estudo-comercial-evidencias
versao: 0.3.0
status: proposta
estado_documental: em-validacao
data: 2026-10-10
responsavel_elaboracao: agente-executor
parecer_origem: REV-MKT-CNQ-002
aprovador: Direcao
aprovacao: pendente
publicacao: bloqueada
---
# O custo invisível da não qualidade de software — v0.3.0

> **PROPOSTA INTERNA • NÃO PUBLICAR • NÃO DISTRIBUIR COMERCIALMENTE.** Documento educacional submetido a revisão independente. Não estabelece oferta, diagnóstico gratuito, economia garantida, campanha, preços, políticas ou serviços homologados. Parecer original preservado na branch `review/parecer-cnq-001`. PR #4 permanece draft.

## Resumo executivo
**Para CTO:** falhas tardias mobilizam desenvolvimento, QA, suporte e operação; a oportunidade é medir quais riscos podem ser antecipados. **Para engenharia:** critérios de aceite verificáveis, testes por risco, instrumentação e análise de escapes ajudam a direcionar o esforço. **Para finanças:** o custo relevante precisa de memória de cálculo auditável, separação entre desembolso e oportunidade e análise de sensibilidade. **Não se afirma que uma empresa brasileira tenha o mesmo comportamento de estudos americanos ou que o investimento em QA produza ROI automático.**

## 1. Fontes primárias: alegação permitida, contexto e limites

| ID | Referência bibliográfica e localização | Abordagem / geografia / unidade | Uso autorizado e limitações |
|---|---|---|---|
| F1 | CISQ, *The Cost of Poor Software Quality in the US: A 2022 Report*, Consortium for Information & Software Quality, 2022, Sumário Executivo; https://www.it-cisq.org/wp-content/uploads/sites/6/2022/11/CPSQ-Report-Nov-22-2.pdf | Estimativas macroeconômicas agregadas para os EUA, com categorias/pressupostos próprios da modelagem; US$, ano de referência 2022 | **Ao menos US$ 2,41 trilhões** de custo anual estimado; aproximadamente US$ 1,52 trilhão é estoque estimado de dívida técnica, **não somável** automaticamente ao fluxo anual. Não extrapolar a empresa individual ou Brasil. |
| F2 | RTI International para NIST, *The Economic Impacts of Inadequate Infrastructure for Software Testing*, Planning Report 02-3, maio 2002, resumo executivo, https://www.nist.gov/document/report02-3pdf | Estudos de caso nos setores de transporte/manufatura e serviços financeiros com extrapolação macroeconômica aos EUA; US$/ano | Estimou US$ 59,5 bilhões anuais de impacto ligado à infraestrutura insuficiente de testes e redução **potencial** de US$ 22,2 bilhões sob cenário tecnicamente factível, **não benefício realizado**. Histórico, escopo mais estreito que 'toda não qualidade'. |
| F3 | Barry Boehm; Victor R. Basili, “Software Defect Reduction Top 10 List”, *IEEE Computer*, v.34 n.1, janeiro de 2001, pp. 135–137 (item relativo a custo de correção), https://www.cs.umd.edu/~basili/publications/journals/J81.pdf | Síntese de evidências/experiência em projetos distintos, e não estimativa universal nem experimento da GenTests.ai; razão de custos de defeitos | Custo posterior **pode** ser muito maior (até ordem de 100:1 em contextos citados), mas sistemas menores não críticos apresentam contraexemplos próximos a 5:1. Não apresentar 100× como constante, nem comparar diretamente amostras/datas. |

**Nota científica:** custos de prevenção e falhas evitadas devem ser comparados no mesmo escopo. Estudos de 2001/2002 são históricos. Para mensagem comercial, preferir “detectar antecipadamente pode reduzir retrabalho” em vez de prometer percentual de economia.

## 2. Modelo financeiro replicável (CNQ-01)

### 2.1 Perspectiva gerencial única e conciliação dos componentes

A unidade é o **incidente único** (ID imutável). A medida principal é **impacto econômico gerencial atribuído ao incidente**: somar componentes econômicos **não sobrepostos**, mas **nunca chamar o resultado de caixa, despesa contábil, prejuízo fiscal ou receita perdida total**. Os componentes devem ser apresentados também de forma segregada. Não somar uma medida de caixa novamente ao custo econômico quando ambas representem o mesmo evento.

| Componente ilustrativo | Valor | Categoria | Evidência necessária em produção | Exclusão |
|---|---:|---|---|---|
| Desenvolvimento: 12h × R$120/h | R$1.440 | Uso de recursos / custo econômico imputado | timesheet com pessoa+período+tarefa e taxa integral de custo | Sem duplicar atraso/custo-hora em outra rubrica |
| QA: 6h × R$90/h | R$540 | Uso de recursos / custo econômico imputado | timesheet único e taxa validada | Horas não repetidas entre QA e engenharia |
| Suporte: 4h × R$70/h | R$280 | Uso de recursos / custo econômico imputado | tickets e tempo por atendente | Sem sobreposição com contrato externo |
| Serviço emergencial externo | R$600 | Despesa incremental contratada | nota fiscal, liquidação e vinculação ao incidente | Não computar se incluído em custo-hora/contrato fixo |
| Crédito comercial concedido | R$900 | **Ajuste de receita** (redução de contraprestação), não presumir caixa | ID de crédito, fatura, razão/contas a receber e conciliação | Evento de cliente e venda **distintos** da margem perdida abaixo |
| Venda cancelada e não recuperável | R$1.000 | **Margem de contribuição líquida perdida / oportunidade** | pedido cancelado, previsão plausível e custos variáveis evitados | Não somar faturamento bruto, crédito da mesma venda nem receita já estornada |
| **Total econômico ilustrativo condicionado** | **R$4.760** | **R$2.260 recursos + R$600 externo + R$900 ajuste de receita + R$1.000 oportunidade** | Documentos reconciliáveis distintos | Não equivalente a saída de caixa de R$4.760 |

**Conciliação do exemplo:** horas R$1.440 + R$540 + R$280 = **R$2.260**; despesa de terceiro R$600; ajuste de receita R$900; oportunidade R$1.000; total **R$4.760**. O crédito hipotético reduz a contraprestação de um cliente A, enquanto a oportunidade decorre da venda perdida de cliente B: **IDs diferentes**; sem prova de distinção, a rubrica sobreposta sai do total e é marcada “não mensurada”. O caixa incremental **não pode ser determinado** pelas hipóteses; pagamento do terceiro pode ser R$600 **se quitado** e crédito pode ser abatimento em fatura, não desembolso. Este material **não declara R$1.500 de caixa**.

Custo-hora integral ilustrativo não representa salário praticado, inclui encargos e benefícios apenas quando a fonte contábil confirmar a composição; não somar estes novamente. Efeito tributário e receitas em regime de competência somente após análise do financeiro responsável. É proibido usar estes números como economia obtida por cliente ou pela GenTests.ai.

**Chaves de prevenção de duplicidade:** `incident_id`, `source_event_id`, `transaction_id`, `customer_id_pseudonym`, `ledger_entry_id`, `person_id_pseudonym`, `start_ts`, `end_ts`; deduplicar por evento+transação+rubrica; vincular créditos e perdas de margem a transações diferentes ou comprovar a parcela incremental distinta; controlar horas sem sobreposição temporal por pessoa, gerar trilha de exclusões com motivo e conciliador. Sem evidência, lançar “desconhecido”, não zero.

### 2.2 Fórmulas e perspectivas distintas
- `Impacto econômico gerencial = Σ horas únicas × custo-hora integral + serviço externo incremental + ajuste líquido de receita distinto + margem de contribuição não recuperável distinta`.
- `Caixa incremental realizado = Σ pagamentos efetivos atribuídos − recebimentos incrementais efetivos` com reconciliação bancária; **não estimável neste exemplo**.
- `Resultado contábil = apuração conforme competência, natureza das contas e conciliação pelo responsável contábil`; não igual ao gerencial automaticamente.
- `Custo de prevenção = Σ esforço preventivo exclusivo × custo-hora + despesas incrementais exclusivas`, segregando perspectiva econômica e caixa.
- `Variação observada normalizada = custo por unidade de exposição no baseline − custo por unidade de exposição na janela posterior`; antes/depois não prova causalidade nem ROI.

## 3. Sensibilidade — hipóteses sem probabilidades (CNQ-06)
O exemplo-base de **3 incidentes por mês durante 12 meses**, R$4.760 cada, equivale a **R$14.280/mês ou R$171.360/12 meses** apenas se ambos permanecerem constantes.

| Número de incidentes/mês | R$2.260/incidente (somente horas) | R$4.760/incidente (base) | R$7.260/incidente (base + R$2.500 de custos novos distintos) |
|---|---:|---:|---:|
| 1 | R$2.260/mês | R$4.760/mês | R$7.260/mês |
| 3 | R$6.780/mês | R$14.280/mês | R$21.780/mês |
| 6 | R$13.560/mês | R$28.560/mês | R$43.560/mês |

As três colunas não são percentis nem limites de confiança. A coluna alta pressupõe **R$2.500 adicionais distintos, verificáveis e não sobrepostos**; jamais somar custos inexistentes para inflar perdas. Em bases reais, incluir casos sem perda financeira, eventos extremos, tamanho dos serviços e janelas sazonais. Não há estimativa de retorno sobre contratação.

## 4. Protocolo de medição auditável (CNQ-03 / CNQ32-02)

### 4.1 Plano de amostragem pré-registrado
Antes de extrair os dados, fixar por escrito: serviço, perfil de defeito, severidade, coorte de versões **implantadas**, datas de implantação, volume/denominador e regras de inclusão. Coorte = releases implantadas entre as datas acordadas, inclusive sem defeitos. Observar cada release por **30 dias completos após sua implantação**, como ponto de partida explícito, ou outra maturação justificada e **igual** entre os períodos. Coortes ainda imaturas não entram no cálculo consolidado; reportar sua contagem à parte. Reabertura do mesmo defeito mantém ID único e horas adicionais; duplicados são ligados ao canônico; regressão tecnicamente distinta cria novo ID com justificativa. Mudanças de observabilidade devem ser registradas como fator de confusão.

**Completude mínima candidata (não política homologada):** ≥95% dos releases com data/serviço/denominador; ≥90% dos incidentes com ID, severidade, data de abertura/restauração e release associado; ≥90% dos custos incluídos com evidência de rubrica, período e trilha de conciliação. Se não atingidos, **não publicar custo médio nem comparação causal**, apresentar percentuais de ausência e análise exploratória. Volume mínimo candidato: ≥30 releases maduros por janela para taxa por release; se menor, reportar contagens brutas e intervalos sem concluir tendência. Os valores de corte exigem validação no piloto e não conferem significância estatística.

### 4.2 Indicadores com escopo/denominador coerentes
| Métrica | Fórmula reproduzível | Evidências / cuidados |
|---|---|---|
| Escape dos defeitos da coorte | defeitos confirmados vinculados à coorte descobertos **após deploy até D+30** ÷ todos os defeitos confirmados vinculados às mesmas releases encontrados até D+30, inclusive pré-deploy | Issue tracker+release_id; zero denominador = N/A; não contar descobertos após D+30 no indicador D+30; reportar atraso em separado |
| Incidentes críticos por release | incidentes Sev1/Sev2 únicos vinculados à coorte e observados D+30 ÷ releases maduras da coorte × 100 | Incident tracker+CI/CD; não trocar por transações entre períodos; para serviços transacionais, criar indicador separado por 100 mil transações expostas |
| MTTR de restauração | Σ (timestamp de restauração de serviço − início confirmado do impacto) ÷ incidentes restaurados na janela | Observabilidade + incidente; reportar mediana e censurados; degradação parcial inclui hora de início do impacto parcial segundo definição pactuada; não confundir com tempo até solução definitiva |
| Retrabalho | Σ horas corrigir/retestar, pessoa e intervalo únicos ÷ horas produtivas do mesmo time/janela | Timesheet + ticket; cobrir tarefas sem incidente e excluir sobreposição |
| Custo por incidente elegível | Σ impacto econômico comprovável e não sobreposto ÷ incidentes com dados completos elegíveis | Financeiro+tracker; publicar proporção de casos elegíveis e ausências |
| Critérios verificáveis | histórias com critérios verificáveis documentados antes do início ÷ histórias iniciadas no período | Backlog, checklist estável |
| Devolução | itens devolvidos na primeira validação ÷ itens submetidos à primeira validação | Tracker, unidade de item imutável |
| Custo de prevenção | horas exclusivas de prevenção × taxa + aquisições incrementais | Projeto+financeiro; não confundir com correções |

**Baseline vs posterior:** escolher janelas de releases maduras de exposição semelhante (volume, severidade, clientes, plataforma), normalizar custo total por 100 releases maduras ou por 100 mil transações, **sem misturar denominadores**. Registrar inflação/taxa-hora, sazonalidade, releases especiais, mudança de equipe, observabilidade e dados faltantes. Apresentar medidas absolutas, taxa, amostras e variação observada; grupo de comparação quando viável. **Associação não implica causalidade**; sem controle e completude não estimar benefício/ROI. Dados pessoais pseudonimizados, com acesso autorizado e retenção definida.

## 5. Mensagem executiva candidata (CNQ-05/07)
**Headline:** Quanto custa descobrir um defeito depois que ele afeta o cliente?
**Dor:** uma falha pode mobilizar várias equipes e gerar efeitos financeiros não capturados em um ticket de bug.
**Evidência:** estudos históricos mostram que a identificação tardia pode aumentar o esforço de correção, com forte variação por projeto.
**Método:** inventariar incidentes, registrar horas e perdas verificáveis, identificar causas e priorizar prevenção por risco.
**Limite:** números do exemplo são fictícios; economia não é garantida e investimento em prevenção também custa.
**CTA interno, sujeito à decisão da direção:** “Sua equipe já mede o retrabalho e o impacto financeiro de incidentes? Podemos conversar sobre como estruturar essa análise.” Não anunciar diagnóstico gratuito, percentual, catálogo nem preço.

**Distribuição:** rascunho para estudo em PDF, carrossel e conversa exploratória; **todos bloqueados** até revisão independente e Direção. Indicadores para experimento futuro: impressões (plataforma); cliques qualificados (UTM+analytics consentido); respostas (CRM); reuniões agendadas (CRM); datas e denominadores declarados. Nenhuma conversão presumida.

## 6. Quality gate e bloqueios
- [ ] Rever fontes primárias, páginas e contexto (CNQ-02).
- [ ] Confrontar rubricas com contabilidade/gestão financeira de caso real antes de usar externamente (CNQ-01).
- [ ] Conferir ficha, denominadores, fontes e minimização de dados (CNQ-03).
- [ ] Conferir binário PDF **exato** na PR, hash SHA-256, renderização, contraste, recorte e legibilidade celular/desktop; inspeção humana ainda requerida (CNQ-04).
- [ ] Validar hipóteses e cenários sem atribuição de probabilidades/ROI (CNQ-06).
- [ ] Validação editorial e comercial por persona (CNQ-05/07).
- [ ] Nova revisão independente e aprovação expressa da Direção (CNQ-08).

**Dependências:** PR #3, Quality Journey v3.2, permanece em proposta; não alterar `PLN-COM-001`, catálogo, site, CRM, precificação ou campanhas. **Não utilizar externamente esta peça mesmo que a PR seja tecnicamente revisada.**
