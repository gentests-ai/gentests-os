---
id: GT-MKT-CNQ-001
tipo: estudo-comercial-evidencias
versao: 0.1.0
status: proposta
estado_documental: em-revisao
data: 2026-10-10
responsavel_elaboracao: agente-executor
aprovador: Direcao
aprovacao: pendente
---
# O custo invisível da não qualidade de software

> **PROPOSTA INTERNA — NÃO PUBLICAR, NÃO DISTRIBUIR.**
> Peça educacional/candidata de marketing. Não cria oferta, não homologa preços, não modifica site, CRM, catálogo nem políticas.

## Tese e limites
A ausência de boas práticas de qualidade pode ampliar retrabalho, incidentes e perdas operacionais. Nem todo defeito é evitável e não se pode prometer economia sem baseline, medição e acordo de escopo.

## Evidências
1. **CISQ 2022:** US$ 2,41 trilhões estimados como custo de baixa qualidade de software nos EUA em 2022; US$ 1,52 trilhão em dívida técnica acumulada, métrica distinta e **não somável automaticamente** ao custo anual. Fonte: https://www.it-cisq.org/the-cost-of-poor-quality-software-in-the-us-a-2022-report/
2. **NIST 2002:** relatório estimou US$ 59,5 bilhões/ano em impactos de infraestrutura inadequada de testes nos EUA e US$ 22,2 bilhões/ano de benefício potencial no cenário viável analisado. Estudo histórico; não extrapolar para empresas brasileiras. Fonte: https://samate.nist.gov/docs/econImpactSumm.v23.pdf
3. **Boehm & Basili 2001:** crescimento do custo de correção ao longo do ciclo depende do tipo de projeto; em certos contextos pode chegar à ordem de 100x, mas para sistemas pequenos não críticos os autores registram valores próximos a 5x. **Proibido comunicar multiplicador fixo universal.** Fonte: https://www.cs.umd.edu/~basili/publications/journals/J81.pdf

## Estrutura de custo por incidente
Custo = horas de engenharia × custo-hora integral + horas de QA × custo-hora integral + horas de suporte × custo-hora integral + despesas externas comprovadas + impacto financeiro comprovável não contabilizado nos itens anteriores.

**Ilustração hipotética:** engenharia: 12h × R$120 = R$1.440; QA: 6h × R$90 = R$540; suporte: 4h × R$70 = R$280; outras perdas distintas: R$2.500. **Total = R$4.760/incidente**. A 3 ocorrências/mês: R$14.280/mês, R$171.360/ano sob hipótese de frequência estável. **Não é observação real, preço ou economia alcançável.**

## Diagnóstico sugerido
1. Definir recorte autorizado e responsáveis;
2. coletar baseline de 30–90 dias conforme dados disponíveis;
3. classificar incidentes por severidade, origem e momento de detecção;
4. registrar horas e custos com premissas explícitas e sem dupla contagem;
5. priorizar prevenção nos requisitos, testes por risco e observabilidade;
6. acompanhar indicadores antes/depois sem atribuição causal indevida.

Indicadores candidatos: taxa de escape, incidentes por severidade, horas de retrabalho, MTTR, custo do incidente, retorno de demandas, critérios de aceite verificáveis.

## Texto de divulgação candidato
**Quanto custa descobrir um bug tarde demais?** O custo de uma falha vai além da correção: inclui investigação, testes, suporte, interrupções e possíveis impactos sobre clientes. Estudos históricos e macroeconômicos ajudam a dimensionar o problema, mas o custo real depende dos dados da sua operação. A GenTests.ai propõe abordar qualidade desde os requisitos, priorizando riscos e medindo os resultados.

**CTA sujeito a aprovação:** “Sua empresa sabe quanto custa descobrir defeitos tarde demais? Converse com a GenTests.ai sobre como avaliar os custos da não qualidade no seu contexto.”

## Gate de revisão independente
- [ ] Conferir cada alegação contra fonte primária e contexto;
- [ ] Validar se o uso de dados históricos é proporcional e transparente;
- [ ] Avaliar cálculo e prevenção de dupla contagem;
- [ ] Validar aderência de posicionamento à Quality Journey vigente;
- [ ] Revisar ortografia, acessibilidade, layout e identidade da marca;
- [ ] Aprovação expressa da Direção antes de divulgação ou execução de campanha.

**Dependência:** Quality Journey v3.2 e conflito de oferta/campanha permanecem em validação na PR #3. Este documento não antecipa decisões da direção.
