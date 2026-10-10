---
id: REV-MKT-CNQ-002
tipo: parecer-revisao-independente
versao: 0.1.0
status: emitido
resultado: aprovado-com-ressalvas-documentais-bloqueado-para-divulgacao
data: 2026-10-10
revisor: ChatGPT-GPT-6
pr: 4
head_revisado: 33de0137182fa76d78100a54b5c56a85a708f81d
documento_blob: 67d8eaab358225f9c8a64684ef85ff0a10dcf791
tratamento_blob: fe08a15c9489f0351add3bf7270aeb19d5ca7c1c
parecer_anterior: REV-MKT-CNQ-001
aprovacao_direcao: pendente
publicacao: bloqueada
---
# REV-MKT-CNQ-002 — Reavaliação independente do custo da não qualidade v0.2.0

**Resultado: APROVADO COM RESSALVAS para a evolução documental; NÃO APROVADO PARA DIVULGAÇÃO.** Quatro achados resolvidos no texto/documentação, três parcialmente resolvidos e um não resolvido. Não confundir parecer de revisão com aprovação institucional.

## Evidências e limites

- PR #4 https://github.com/gentestsai-sudo/gentests-os/pull/4, commit examinado `33de0137182fa76d78100a54b5c56a85a708f81d`, draft, 2 arquivos modificados: `comercial/GT-MKT-CNQ-001-Custo-da-Nao-Qualidade.md` (v0.2.0, blob `67d8eaab358225f9c8a64684ef85ff0a10dcf791`); `comercial/GT-MKT-CNQ-002-Tratamento-REV-MKT-CNQ-001.md` (blob `fe08a15c9489f0351add3bf7270aeb19d5ca7c1c`). PDF não consta entre os arquivos alterados.
- Referência anterior REV-MKT-CNQ-001 na branch `review/parecer-cnq-001`. Quality Journey v3.2 e tratamento GT-COM-QJ-003, PR #3, permanecem em proposta, sem legitimar preço, campanha, catálogo ou oferta.
- Referências primárias conferidas: CISQ (https://www.it-cisq.org/the-cost-of-poor-quality-software-in-the-us-a-2022-report/); relatório RTI/NIST de 2002, sumário executivo, Tabela ES-4 (https://www.nist.gov/document/report02-3pdf); Boehm & Basili, IEEE Computer jan/2001, p.135, item ONE (https://www.cs.umd.edu/~basili/publications/journals/J81.pdf).
- Não examinados: PDF final, dados de cliente, modelo contábil assinado, missão/visão/valores aprovados nem validações de acessibilidade do binário. Adesão temática não representa homologação dessas políticas, que permanecem em proposta.

## Matriz de revalidação (oito achados)

| ID | Estado | Severidade atual | Evidência (arquivo/seção) | Risco residual e ação objetiva |
|---|---|---|---|---|
| CNQ-01 | **Parcialmente resolvido** | **Alto** | GT-MKT-CNQ-001 §2.1–2.2: R$600 serviço externo, R$900 créditos/estornos, R$1.000 margem de contribuição e R$2.260 horas, soma correta R$4.760; GT-MKT-CNQ-002 linha CNQ-01 | 'R$1.500 desembolsos/ajustes' não é sinônimo de R$1.500 saída de caixa incremental; descontos/estornos podem ser devolução, redução de contas a receber ou receita sacrificada. Separar caixa efetivamente pago, reversão de receita e oportunidade, reconciliar por transação e evitar contar crédito e margem da mesma venda. No exemplo, declarar caixa indeterminado sem natureza comprovada; construir subtotais conceitualmente homogêneos. |
| CNQ-02 | **Resolvido** | — | GT-MKT-CNQ-001 §1 F1–F3: cita título, ano, limites, geografia e fontes. CISQ 'ao menos' US$2,41 tri e dívida técnica US$1,52 tri distinta; NIST US$59,5 bi e potencial US$22,2 bi; Boehm/Basili 100:1 contextual e 5:1 contraexemplo | Fontes históricas e macromodelos não são prova de ROI em cliente do Brasil. Preservar ressalvas e evitar transformar multiplicadores em claims universais. |
| CNQ-03 | **Parcialmente resolvido** | **Médio** | GT-MKT-CNQ-001 §4: ficha, denominadores, custo prevenção e avisos de causalidade; GT-MKT-CNQ-002 linha CNQ-03 | Taxa de escape sujeita a atraso de descoberta/maturação e diferenças na captura. Definir coorte de releases, janela de observação, casos reabertos/duplicados e mínimos de completude, critérios de volume/seleção; para MTTR apontar convenção exata (time-to-restore) e observação de indisponibilidades parciais; pactuar custo normalizado antes/depois. |
| CNQ-04 | **Não resolvido** | **Alto** | PR #4 lista apenas os dois Markdown; §6 e tratamento CNQ-04 declaram PDF local, mas não fornecem binário versionado | Sem PDF efetivo, não é possível verificar SHA-256 contra bytes, páginas, cortes, contraste, fontes, links, leitura móvel, texto extraível, estrutura de acessibilidade e idioma. Executor deve anexar PDF **exato** em commit/PR com caminho, SHA-256 calculado do binário versionado, manifesto de origem, páginas renderizadas e evidência de inspeção humana mobile/desktop. Não declarar aprovado por hash ou relato. |
| CNQ-05 | **Parcialmente resolvido** | **Médio** | GT-MKT-CNQ-001 §5–6 e cabeçalho: CTA exploratório, nenhuma oferta/campanha/diagnóstico gratuito, PR #3 pendente | Adequação textual satisfeita; ainda falta decisão da Direção e confronto com posicionamento/catálogo efetivamente aprovados e futura peça externa. Proibir disparo, publicação e oferta até gate. |
| CNQ-06 | **Resolvido** | — | GT-MKT-CNQ-001 §3: matriz 1/3/6 incidentes × R$2.260/R$4.760/R$7.260 com contas certas; R$171.360/ano condicionado | Cenários não têm probabilidade, nem limite de confiança, e devem continuar ilustrativos. Não publicar a coluna alta sem premissa evidente. |
| CNQ-07 | **Resolvido no texto** | — | GT-MKT-CNQ-001 resumo executivo e §5: mensagens CTO/engenharia/finanças, headline/dor/evidência/método/limite/CTA | A eficácia comercial e qualidade da apresentação final continuam não demonstradas; experiência real depende de teste posterior autorizado e revisão visual CNQ-04. |
| CNQ-08 | **Resolvido no documento** | — | GT-MKT-CNQ-001 front matter e §6; GT-MKT-CNQ-002: versão 0.2.0, status proposta, aprovação pendente, bloqueio expresso, referência ao parecer | Cabe atualizar PR #4 com status real da v0.2.0 e links de evidência quando chegar PDF; não mudar estado de aprovação. |

## Novos achados

- **CNQ32-01 — Médio, consistência conceitual financeira:** §2.1 prescreve 'adotar custo econômico gerencial ou saída de caixa, nunca somar ambos' e depois intitula R$4.760 'total ilustrativo, econômico misto'. A soma pode servir como custo econômico abrangente **se** as categorias forem disjuntas, mas o enunciado precisa definir um ponto de vista gerencial único, exibindo separadamente subtotais de horas, desembolsos reais, ajustes de receita e oportunidade; não apresentar híbrido como fluxo de caixa ou custo contábil.
- **CNQ32-02 — Baixo, operacionalização de métricas:** §4 sugere incidentes críticos por '1.000 deploys ou 100 mil transações' e 'escape rate' por defeitos confirmados antes+depois. São métricas candidatas, não mutuamente comparáveis; a escolha do denominador deve corresponder ao objetivo/serviço, coorte e volume, com janela e critérios de maturação publicados.

## Verificação técnico-financeira

- §2: horas 1440+540+280 = 2260; 600+900+1000=2500; total ilustrativo 4760. Aritmética correta, não evidência financeira real.
- §3: cenários 1/3/6 × (2260/4760/7260) corretos; 4760×3×12=171360 correto sob estabilidade dos pressupostos.
- Fontes científicas autênticas, corretamente contextualizadas na v0.2.0. O NIST quantifica infraestrutura de testes, não o universo de defeitos; CISQ é agregado dos EUA; Boehm/Basili diferenciam sistemas e arquitetura. Evitar alegações causais ou de economia contratual.
- Uso no Brasil demanda taxas reais de custo-hora, conciliação contábil, privacidade de dados, baseline e validação pelo responsável financeiro.

## Posicionamento, governança e qualidade editorial

Resumo por persona é mais claro; CTO: risco/incidentes; engenharia: critérios/escape; finanças: rastreabilidade/custo. CTA contido e educacional, sem oferta de serviço específica. Risco reputacional se número hipotético aparecer como economia, dado de mercado brasileiro ou promessa de resultado. Material tem texto legível em Markdown, mas nenhuma conclusão sobre diagramação, navegação do PDF, contrastes e acessibilidade até inspeção do binário.

O README da base destaca que documentos com `status: proposta` não estão aprovados e aprovação humana é obrigatória. Os princípios mencionados em Quality Journey (evidências, risco, qualidade desde requisitos, eficiência sustentável) são compatíveis; missão/visão/valores, GQF/5S ainda em proposta nos registros examinados. Aderência definitiva depende de aprovação formal da Direção.

## Encaminhamento obrigatório ao executor (v0.3.0 ou rodada de evidências)

1. **Prioridade alta CNQ-04:** colocar PDF exato na PR #4 ou outra PR formalmente vinculada; indicar caminho, commit, SHA-256 verificado do arquivo GitHub, fonte da exportação, renders de todas páginas, inspeção visual mobile/desktop e checklist de acessibilidade (texto extraível, ordem de leitura, contraste, links, idioma/títulos e alt quando aplicável). Solicitar reavaliação independente do PDF.
2. **Prioridade alta CNQ-01 / CNQ32-01:** reclassificar corretamente R$900 de créditos/estornos e conceito de caixa; separar perdas e recursos, subtotais gerenciais versus caixa, demonstrar exclusão por IDs de evento/transação.
3. **Prioridade média CNQ-03 / CNQ32-02:** definir maturação de coortes, critérios de dados completos, denominadores escolhidos por recorte e custo normalizado no tempo.
4. **CNQ-05:** não antecipar Quality Journey/serviços, não publicar até autorização expressa Direção. Atualizar PR e vínculos para v0.2.0/parecer.
5. Preservar as ressalvas científicas, a sensibilidade hipotética, o CTA não vinculante e os avisos de status proposta.

**Quality gate: aprovado com ressalvas SOMENTE como avanço documental. REPROVADO PARA DIVULGAÇÃO**, aguardando evidências e aprovação expressa. Não houve merge, correção do material do executor, envio comercial ou publicação. Este parecer é técnico, não laudo contábil/jurídico.
