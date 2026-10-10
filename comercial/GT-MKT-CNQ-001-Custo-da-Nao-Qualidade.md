---
id: GT-MKT-CNQ-001
tipo: estudo-comercial-evidencias
versao: 0.2.0
status: proposta
estado_documental: em-validacao
data: 2026-10-10
responsavel_elaboracao: agente-executor
parecer_origem: REV-MKT-CNQ-001
aprovador: Direcao
aprovacao: pendente
publicacao: bloqueada
---
# O custo invisível da não qualidade de software — v0.2.0

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

### 2.1 Regras e unidade de registro
Unidade de análise: **um incidente único**, ID estável em sistema de incidentes, com período, serviço, severidade, papéis, horas, dados financeiros e fontes. Adotar **custo econômico gerencial** ou **saída de caixa**, nunca somar ambos. Horas de colaborador CLT podem representar custo econômico imputado, não gasto incremental; somente horas extras ou fornecedor adicional comprovado entram como caixa incremental. Taxas administrativas, impostos, encargos e benefícios já integrantes de uma taxa horária integral **não serão adicionados novamente**. Custo-hora deve ser apurado pela área financeira: (remuneração + encargos patronais + benefícios + custos de contratação atribuíveis)/horas produtivas coerentes, com mês e regime; os valores da simulação abaixo são arbitrários, **não equivalem a salários de mercado**.

| Rubrica | Valor ilustrativo | Premissa / fonte exigida em uso real | Classificação e regra anti-duplicidade |
|---|---:|---|---|
| Desenvolvimento | 12h × R$120 = **R$1.440** | Apontamento único por pessoa/tarefa; custo-hora integral aprovado | Custo econômico imputado; não somar “atraso do projeto” se calculado pelas mesmas horas |
| QA | 6h × R$90 = **R$540** | Registro de reteste/reprodução e taxa gerencial | Custo econômico imputado; não duplicar horas de engenharia |
| Suporte | 4h × R$70 = **R$280** | Tickets e alocação de tempo por incidente | Custo econômico imputado; não lançar outra vez em despesas de atendimento |
| Serviço externo emergencial | **R$600** | Exemplo de nota fiscal exclusiva do incidente | Desembolso incremental; excluir se já rateado no custo-hora |
| Créditos/estornos concedidos | **R$900** | Exemplo de conciliação/estorno líquido efetivamente concedido | Desembolso ou receita líquida sacrificada; não somar receita bruta original dos mesmos clientes |
| Transações efetivamente não recuperáveis | **R$1.000** | Exemplo de margem de contribuição líquida perdida, reconciliação de pedidos | Oportunidade econômica; não somar faturamento bruto nem créditos/estornos relativos ao mesmo evento |
| **Total ilustrativo, econômico misto** | **R$4.760** | Premissas simuladas, nunca observadas | R$2.260 de horas imputadas + R$1.500 de desembolsos/ajustes + R$1.000 de oportunidade, desde que eventos independentes |

**Importante:** os R$2.500 são deliberadamente divididos em R$600 + R$900 + R$1.000. São **eventos hipotéticos distintos**, não documentação financeira de cliente. Se a origem da perda não for comprovável ou houver sobreposição, marcar **não mensurado** e excluir do total. A base de caixa incremental do exemplo corresponde somente aos R$1.500, se efetivamente desembolsados; já o custo gerencial combinado é R$4.760. Estornos podem requerer tratamento contábil específico e não devem ser classificados automaticamente como caixa sem verificação. Tributos incidentes sobre serviços vendidos pela GenTests **não fazem parte deste exemplo** nem se assume qualquer alíquota brasileira. O exemplo não demonstra resultado de implantação de QA.

### 2.2 Fórmulas
`Custo gerencial por incidente = Σ(horas únicas × custo-hora integral) + desembolsos/ajustes distintos + margem de contribuição líquida perdida não sobreposta`.

`Custo mensal ilustrativo = custo médio por incidente × quantidade de incidentes elegíveis no período`.

`Custo prevenção = despesas incrementais de prevenção + esforço imputado exclusivamente à iniciativa` (reportar separadamente caixa/econômico).

`Benefício líquido observacional = (custo normalizado baseline − custo normalizado posterior) − custo prevenção`, apenas como **diferença observada**, não efeito causal provado, quando comparabilidade e dados forem suficientes. Nunca inferir ROI em ausência de histórico, controle de mudanças e atribuição aceitável.

## 3. Sensibilidade — hipóteses sem probabilidades (CNQ-06)
O exemplo-base de **3 incidentes por mês durante 12 meses**, R$4.760 cada, equivale a **R$14.280/mês ou R$171.360/12 meses** apenas se ambos permanecerem constantes.

| Número de incidentes/mês | R$2.260/incidente (somente horas) | R$4.760/incidente (base) | R$7.260/incidente (base + R$2.500 de custos novos distintos) |
|---|---:|---:|---:|
| 1 | R$2.260/mês | R$4.760/mês | R$7.260/mês |
| 3 | R$6.780/mês | R$14.280/mês | R$21.780/mês |
| 6 | R$13.560/mês | R$28.560/mês | R$43.560/mês |

As três colunas não são percentis nem limites de confiança. A coluna alta pressupõe **R$2.500 adicionais distintos, verificáveis e não sobrepostos**; jamais somar custos inexistentes para inflar perdas. Em bases reais, incluir casos sem perda financeira, eventos extremos, tamanho dos serviços e janelas sazonais. Não há estimativa de retorno sobre contratação.

## 4. Protocolo de medição antes/depois (CNQ-03)
**Amostra e janela:** 30–90 dias é apenas sugestão inicial; fixar período suficiente para volume/estacionalidade, tipo de sistema e mudanças organizacionais. Comparar janelas equivalentes (carga/transações/releases), mesma definição de incidente e critérios de severidade; explicitar efeitos de sazonalidade, release, mudanças de instrumentação e alterações de equipe. Não excluir incidentes desfavoráveis.

**Ficha de coleta mínima:** incident_id; serviço/jornada; início/fim; janela; severidade definida; origem provável (incerta quando não comprovada); etapa de detecção; release; autor da validação; IDs de tarefas/tickets; pessoa/papel; horas únicas; taxa-hora/mês; nota/documento de desembolso; ID de transação e valor de **margem líquida**; exclusão/duplicidade; fonte; nível de confiança; iniciativa de prevenção ligada; custo preventivo; fator externo/mudança concomitante. Proteger dados pessoais; agregação e uso mediante autorização.

| Indicador | Fórmula / denominador | Fonte e interpretação |
|---|---|---|
| Escape rate | defeitos confirmados encontrados após implantação ÷ todos os defeitos confirmados encontrados antes+depois no conjunto e janela definidos | Issue tracker + release; informar cobertura e atraso de detecção; não confundir com nº absoluto |
| Incidentes críticos normalizados | incidentes Sev1/Sev2 únicos ÷ 1.000 deploys ou por 100 mil transações (escolher denominador relevante) | Incident tracker + CI/CD ou telemetria; severidade e unidade constantes |
| Retrabalho | Σ horas únicas em atividades de correção/reteste ÷ horas produtivas totais do mesmo time e período | Timesheets + tickets; não contar uma hora em dois incidentes |
| MTTR | média de (restauração confirmada − início do impacto) nos incidentes elegíveis | Monitoramento/tickets; reportar mediana e valores extremos quando possível |
| Custo por incidente | Σ custos gerenciais sem duplicidade ÷ nº de incidentes com dados suficientes | Financeiro + timesheets + incidente; publicar completude da amostra |
| Critérios verificáveis | histórias com critérios verificáveis antes do desenvolvimento ÷ histórias elegíveis iniciadas | Backlog + refinamento, amostra definida |
| Retorno ao desenvolvimento | itens devolvidos por não conformidade ÷ itens submetidos à primeira validação | Tracker, mesma definição temporal |
| Custo de prevenção | Σ horas únicas da iniciativa × taxa + despesas incrementais vinculadas | Projeto QA + financeiro; não confundir com correção de incidente |

**Avaliação:** registrar baseline, intervenção, indicadores-alvo, custo da mudança e diferenças observadas. Quando viável, usar grupo/serviço comparável, séries temporais e revisão por responsáveis. Ausência de controle ⇒ **associação**, não causalidade. Dados indisponíveis ⇒ “não mensurado”, não zero.

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
