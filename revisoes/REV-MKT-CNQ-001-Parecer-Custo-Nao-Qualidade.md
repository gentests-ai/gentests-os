---
id: REV-MKT-CNQ-001
tipo: parecer-revisao-independente
versao: 0.1.0
status: emitido
resultado: reprovado-para-divulgacao
data: 2026-10-10
revisor: ChatGPT-GPT-6
pr_origem: 4
commit_revisado: 53fcafc96d8540860b582c4c612076ab84b8cfcf
blob_revisado: a12d1c057a0093b28ac084bd925b1d4b4787bb28
documento_origem: comercial/GT-MKT-CNQ-001-Custo-da-Nao-Qualidade.md
aprovacao_direcao: pendente
---
# REV-MKT-CNQ-001 — Parecer independente: custo da não qualidade

**Resultado: REPROVADO PARA DIVULGAÇÃO da versão 0.1.0.** A tese central é tecnicamente plausível e os três valores de estudos e as contas do exemplo estão corretos. A reprovação se refere à prontidão institucional/comercial, não a fraude ou erro matemático identificado. Não há autorização de marketing, preço, oferta ou publicação.

## Escopo, rastreabilidade e limitações

PR #4: https://github.com/gentestsai-sudo/gentests-os/pull/4 (draft; um Markdown no diff), commit de origem `53fcafc96d8540860b582c4c612076ab84b8cfcf`; documento GT-MKT-CNQ-001 v0.1.0, blob `a12d1c057a0093b28ac084bd925b1d4b4787bb28`. Confronto documental com o tratamento Quality Journey v3.2 GT-COM-QJ-003 e REV-COM-QJ-002 da PR #3. Não foram examinados dados reais de clientes, contabilidade brasileira, campanhas publicadas nem o PDF final (PR #4 declara que PDF foi produzido separadamente e não versionado); portanto não se certifica a legibilidade, a acessibilidade visual ou efeitos comerciais. Referências de governança ainda em proposta não são normas aprovadas.

## Verificação das fontes

- **CISQ:** site oficial afirma *at least* US$ 2,41 trilhões para custo de baixa qualidade de software nos EUA em 2022 e aproximadamente US$ 1,52 trilhão de dívida técnica acumulada. O segundo indicador é estoque, não parcela anual a somar ao primeiro. https://www.it-cisq.org/the-cost-of-poor-quality-software-in-the-us-a-2022-report/ . Relatório: https://www.it-cisq.org/wp-content/uploads/sites/6/2022/11/CPSQ-Report-Nov-22-2.pdf . Recomenda-se preservar "ao menos" e explicar natureza/modelagem e abrangência econômica.
- **NIST:** RTI para NIST, *The Economic Impacts of Inadequate Infrastructure for Software Testing*, Planning Report 02-3, maio/2002, estimou US$ 59,5 bi anuais e US$ 22,2 bi de **redução potencial** sob cenário factível, a partir de estudos de transporte/manufatura e serviços financeiros com extrapolação à economia dos EUA. Não é benefício realizado e não mede toda não qualidade de software. Fonte oficial estável: https://www.nist.gov/document/report02-3pdf . O link samate do documento original pode ter disponibilidade variável.
- **Boehm e Basili:** *Software Defect Reduction Top 10 List*, IEEE Computer, jan/2001, pp. 135–137: diferença de custo pós-entrega versus requisitos/projeto "often" de 100:1, com contraexemplo de 5:1 em pequenos sistemas não críticos e mitigação por boa arquitetura. Não comunicar regra fixa universal nem retorno medido de serviço da GenTests. https://www.cs.umd.edu/~basili/publications/journals/J81.pdf .

Conclusão científica: a detecção precoce **pode** reduzir custo de correção e retrabalho, mas efeito depende do contexto; investimento preventivo também tem custo, e benefícios não são automaticamente causais nem garantidos.

## Validação financeira

12 × 120 = R$ 1.440; 6 × 90 = R$ 540; 4 × 70 = R$ 280; + R$ 2.500 = **R$ 4.760/incidente**. × 3 = **R$ 14.280/mês**; × 12 = **R$ 171.360/ano**, com ocorrência e composição constantes. Aritmética correta. Dados inteiramente hipotéticos; o resultado não é economia comprovada ou projeção de retorno de contratação.

## Matriz de achados

| ID | Severidade | Evidência | Risco/impacto | Correção e aceite |
|---|---|---|---|---|
| CNQ-01 | **Alto** | 'Estrutura de custo': R$ 2.500 'outras perdas distintas', sem itens ou memória de cálculo; custos-hora não fundamentados. | Dupla contagem entre salários, suporte, receitas perdidas, penalidades e despesas externas; baixa replicabilidade brasileira. | Decompor os R$ 2.500 por rubrica, evento, premissa, fonte e regra de não sobreposição; separar custo contábil, custo econômico imputado e caixa; esclarecer carga tributária/encargos como hipótese, sem atribuí-los à empresa real. |
| CNQ-02 | **Médio** | 'Evidências' traz números corretos sem explicitar técnicas/limites de extrapolação do NIST e natureza agregada do CISQ; cita Boehm/Basili sem título/página. | Uso como autoridade universal e perda de credibilidade com CTO/CFO. | Tabela de referência: autoria, título, ano, página/tabela, amostra ou abordagem, geografia, unidade, limite e afirmação autorizada; incluir endereço NIST alternativo oficial e distinguir 'ao menos' CISQ. |
| CNQ-03 | **Médio** | 'Diagnóstico sugerido' baseline 30–90 dias e indicadores não definem denominador, fontes, custo de prevenção ou critério de comparabilidade. | Comparações antes/depois confundidas com causalidade e retorno/ROI presumido. | Ficha de medição: identificador de incidente, janela, severidade, etapa de origem/detecção, horas únicas por papel, despesas, efeitos mensuráveis, critérios de exclusão, denominadores, custo da intervenção e fatores externos; 30–90 dias apenas janela candidata. |
| CNQ-04 | **Alto** | PR #4 contém somente Markdown e declara PDF gerado fora da PR, não versionado. | Não é possível homologar layout, contraste, cortes, fontes, links, acessibilidade ou conformidade visual para publicação. | Adicionar binário exato a uma PR apropriada, hash SHA-256, relação com versão textual, renderização por página e inspeção humana em celular e desktop; reavaliar visuais. |
| CNQ-05 | **Médio** | 'Texto de divulgação candidato' menciona GenTests mas não operacionaliza a distinção entre análise de custo e serviço vendido; PR #3 ainda mantém oferta/precificação em proposta. | CTA pode sugerir diagnóstico/resultado contratado ou antecipar Quality Journey ainda não aprovada. | Enquadrar claramente conteúdo educacional e conversa exploratória, sem promessa de economia, diagnóstico gratuito, preços ou etapas homologadas; submeter cópia final à decisão comercial da Direção. |
| CNQ-06 | **Médio** | Valor anual apresentado com frequência mensal fixa, sem apresentar amplitude ou ilustração alternativa de incidentes. | Leitor pode confundir extrapolação hipotética com orçamento ou economia anual garantida. | Exibir hipótese '3 incidentes/mês durante 12 meses' junto do valor e adicionar sensibilidade por frequência/custo, sem atribuir probabilidade arbitrária. |
| CNQ-07 | **Baixo** | Texto claro porém orientado a evidência técnica; faltam hierarquia visual, mensagem para CFO e versão resumida executiva verificável. | Menor retenção e conversão em LinkedIn; nenhum dado demonstrado de leads. | Criar roteiro de peça: dor operacional, cálculo transparente, limites, como medir, CTA neutro; subtítulos claros, linguagem acessível, tabelas legíveis; medir impressões, cliques qualificados, respostas e reuniões sem prometer conversão. |
| CNQ-08 | **Baixo** | Metadados marcam status proposta/aprovação pendente; PR draft. | Risco de divulgação antes da decisão se forem usados materiais soltos. | Preservar cabeçalho 'NÃO PUBLICAR', vincular revisão e versionamento; aprovação expressa antes de externalização. |

**Crítico: 0; Alto: 2; Médio: 4; Baixo: 2.** Achados são impeditivos para saída comercial na versão revisada; não identificamos infração de publicação já consumada.

## Avaliação comercial e riscos

Tese 'quanto custa descobrir tarde?' é relevante para CTOs e engenharia (retrabalho, disponibilidade, desempenho de entrega). Para CFO/financeiro, preferência por custo controlável, valores auditáveis, custo de oportunidade explicitado e risco de prejuízo sem inferir causalidade. **Risco reputacional alto** se usar '100x' universal, transformar CISQ/NIST em dado brasileiro atual ou insinuar ganhos garantidos. **Risco financeiro médio/alto** se um modelo ilustrativo virar diagnóstico comercial sem fontes e sem regra antidupla contagem. **Risco de governança alto** se campanha mencionar catálogo, preços ou estágio Quality Journey não aprovado.

O documento não contradiz a v3.2: ambos priorizam qualidade desde requisitos, evidências, risco, limites de escopo e independência de contratação. A Quality Journey v3.2 permanece em proposta; não tratá-la como oferta ativa. O material CNQ pode posicionar-se como educação e ponto de partida para conversa, não como ficha de serviço aprovada.

## Encaminhamento executor — v0.2.0

1. Resolver **CNQ-01** com planilha/tabela auditável de rubricas, sem duplicidade, e contraste caixa versus custo econômico.
2. Resolver **CNQ-02** com ficha bibliográfica rastreável das três fontes, amostras, datas e restrições (CISQ mínimo, NIST cenário, Boehm 5x/100x contextual).
3. Resolver **CNQ-03 e CNQ-06** com indicadores operacionalizados, exemplo de sensibilidade e fórmula que distinga custo de intervenção e benefício *medido*.
4. Resolver **CNQ-04** com PDF/PPTX efetivo e evidências de renderização, mais testes de acessibilidade/legibilidade.
5. Resolver **CNQ-05 e CNQ-07** com mensagem executiva por persona e CTA sem promessa/oferta antecipada.
6. Preservar **CNQ-08** e documentar dependências com PR #3; submeter para nova revisão independente e aprovação expressa da Direção.

**Gate:** documentação apta a nova revisão após correções; **NÃO APROVADA para LinkedIn, site, e-mail, apresentação externa, campanhas ou envio a prospectos**. Este parecer não constitui certificação contábil, científica formal ou aprovação jurídica. Revisor não modificou a fonte, não fez merge e não publicou campanha.
