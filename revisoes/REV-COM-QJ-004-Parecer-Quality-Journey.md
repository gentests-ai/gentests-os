---
id: REV-COM-QJ-004
tipo: parecer-independente
versao: 1.0.0
status: parecer-emitido
data: 2026-10-10
repositorio: gentestsai-sudo/gentests-os
pr_execucao: 3
sha_revisado: 985e47531aa134cf1970281fd5eb51020eb2da32
resultado: APROVADO COM RESSALVAS PARA EVOLUCAO
homologacao_comercial: nao
autorizacao_piloto: nao
---

# REV-COM-QJ-004 — Revalidação focal Quality Journey v3.2

## Parecer executivo
**APROVADO COM RESSALVAS PARA EVOLUÇÃO DOCUMENTAL. NÃO APROVADO PARA DISTRIBUIÇÃO VISUAL, COMERCIALIZAÇÃO OU PILOTO.** As fichas dos cinco serviços tornaram-se executáveis como propostas delimitadas. Separação de aquisição/execução e monitoramento gerencial são suficientes para planejar medição; não provam custo, margem ou sustentabilidade real. Alternativas comerciais e institucionais foram preservadas sem homologação implícita. Há **sobreposição visual confirmada no PNG do slide 2, terceiro cartão**, que deve ser corrigida antes de circulação.

**Fontes e método:** [PR #3](https://github.com/gentestsai-sudo/gentests-os/pull/3), commit `985e47531aa134cf1970281fd5eb51020eb2da32`; `comercial/GT-COM-QJ-004-Tratamento-REV-COM-QJ-003.md`, `revisoes/REV-COM-QJ-003-Parecer-Quality-Journey.md`, `05-Evidencias/Quality-Journey-v3.2/README.md`, `render-manifest.json`, `site-inventory.json`, dez PNGs exibidos na revisão. Inspeção visual independente dos dez PNGs e comparação textual. **Não houve abertura do binário original no PowerPoint, recálculo independente de SHA-256 ou verificação de equivalência de renderização PowerPoint:** hash `b228419977c3267a6b3696a25c40886fc9ffce6ff9ab0d5791750d6661760a48` foi conferido apenas no manifesto e na declaração do executor. Testes automáticos anteriores não são aceite comercial, fiscal ou visual.

## Reavaliação individual
| ID | Classificação | Evidência e extensão | Residual |
|---|---|---|---|
| QJ31-01 | **Resolvido documentalmente** | GT-COM-QJ-004 §2.1–2.6 especifica insumos quantitativos, limites, revisão, devolutiva, aceite e alterações por serviço. | Capacidade real e cláusulas contratuais ainda requerem validação |
| QJ31-02 | **Parcialmente resolvido** | §3 decompõe R$20/40/80, separa pré-venda e execução, detalha ociosidade e modelo de apropriação por comprovante; valores são expressamente hipotéticos. | Custo real, tributos, método de alocação, margem e teto de subsídio não comprovados |
| QJ31-03 | **Resolvido documentalmente, decisão pendente** | §5 preserva campanhas A/B/C e faixas incompatíveis; avisos de conflito em fontes preexistentes; sem substituir catálogo/decisão. | Escolha comercial e aprovação pela Direção |
| QJ31-04 | **Parcialmente resolvido — correção visual necessária** | PPTX exato referenciado e dez PNGs versionados com manifesto. Visualização direta do `slide-02.png`: título “Decisões sem evidências” invade/inicia contato com corpo (“Sem informações confiáveis...”); o defeito existe na projeção fornecida. | Autor deve corrigir layout e gerar novo binário/hash/PNG; conferir abertura no PowerPoint antes de aprovar distribuição |
| QJ31-05 | **Resolvido no alcance estático** | §7 e `site-inventory.json` registram quatro páginas, URLs, textos e propostas condicionadas. | Dinâmica/commit do site não verificados; publicação separada |
| QJ31-06 | **Mantido resolvido apenas documentalmente** | Encerramento anterior preservado, sem novos indícios materiais contrários. | Nenhuma reabertura |
| QJ32-01 | **Resolvido documentalmente** | §2 registra limites concretos, critérios de bloqueio e mudança para todos os cinco serviços. | Aplicação depende de proposta/contrato aprovado |
| QJ32-02 | **Resolvido** | §2.2: QA Start não executa testes, acessa ambiente, reproduz falhas nem realiza auditoria; artefato do piloto explicita exclusão. | Garantir mesma fronteira em materiais externos após autorização |
| QJ32-03 | **Resolvido como proposta, decisão pendente** | §8 confronta MVV GitHub e documento institucional, recomenda redação candidata sem promover proposta a política. | Direção escolhe versão oficial |
| QJ32-04 | **Resolvido no plano de inventário/migração** | §7 associa textos efetivamente levantados nas quatro páginas às alternativas; não efetuou mudanças no site. | QA de migração somente se aprovada e implementada |
| QJ32-05 | **Resolvido documentalmente** | Metadados atuais da PR #3 identificam a rodada v3.2/artefatos; a PR continua aberta e sem merge. | Merge sujeito a decisão humana |

## Executabilidade dos serviços
- **QA Start — Descobrir:** até uma página de relato + cinco páginas de documentos e três capturas; nota até duas páginas, alinhamento 20 min, devolutiva 10 min e revisão 15 min. Nenhuma execução de testes ou navegação exploratória. Aceite pela rastreabilidade de fontes, hipóteses, lacunas e prioridades. Escopo candidato executável documentalmente.
- **QA Focus — Investigar:** uma jornada até seis passos, cinco cenários, um perfil/ambiente/navegador desktop, sandbox autorizado; relatórios, bloqueios, não inclusão de reteste pós-correção. Complexidade e capacidade devem ser aferidas antes da cotação.
- **QA Evolution — Planejar:** um fluxo/equipe, até três pessoas, duas entrevistas, cinco amostras/20 páginas, até três indicadores; plano com ações prioritárias e limites explícitos; não inclui execução.
- **QA Implementation — Implementar:** não se apresenta como pacote universal; requer ficha por item, escopo, custo, competência, aceite, dependência, handoff e rollback. Sem ficha completa, não cotar.
- **QA Excellence — Sustentar:** ciclo candidato de 30 dias, até três indicadores, duas reuniões, relatório e limites de resposta/ajuste documental; horas contratadas e baseline verificável necessários para comparação. Sem operação 24x7 implícita.

Regra comum: silêncio não é aceite; falhas imputáveis ao executor não se transformam em cobrança automática; bloqueio e mudança exigem decisão pactuada. São boas proteções documentais, sujeitas a validação contratual.

## Financeiro e piloto
A abertura de custos (§3) diferencia custos tecnológicos incrementais e fixos não humanos, e exclui dupla apropriação da mesma despesa. R$69,92/h é remuneração imputada, não custo contábil provado. R$20/40/80 e o adicional R$50 são sensibilidades; 6%/15,5% não são alíquotas validadas do CNPJ. Nenhuma receita realizada ou CAC real foi demonstrado. O modelo de esforço por segmento, apropriação única de despesas e resultado gerencial é adequado **para medição futura**.

Piloto Start §4: 150 minutos candidatos, alerta aos 120 minutos, estresse 210 minutos, uma entrega, nenhuma continuação automática; métricas de esforço, retrabalho, valor percebido, prazo e resultado. **Margem de stress do cenário de 2,5h/R$290/R$20 + R$50:** R$27,80 a 6% e R$0,25 a 15,5%. Exceder para 3,5h gera resultados negativos. Alíquotas e composição não confirmadas, logo não há base para autorizar subsídio nem afirmar viabilidade. Diretor(a) precisa deliberar preço, margem mínima, teto de perda, capacidade e contrato antes do piloto.

## Visual PPTX e comunicação
Renderizações 1–10 foram visualizadas diretamente. Slide 2, cartão 03, apresenta sobreposição do título em duas linhas com a primeira linha do texto descritivo. **Achado VIS-QJ-004-01 / Médio, obrigatório corrigir antes da circulação da apresentação.** Inspecionar no PowerPoint nativo, ajustar espaçamento/altura ou tamanho de fonte no arquivo-fonte pelo executor, gerar novo hash e re-renderizar o slide afetado; revalidar leitura. Nos demais PNGs não observei sobreposição igualmente evidente; isso não é certificação pixel a pixel de PowerPoint. Slides indicam preço em definição (não preço homologado), exemplo ilustrativo no 6 e convite de pré-venda no 10. Nenhuma aprovação visual total até reparo e inspeção do arquivo original.

## Campanha, site, MVV e controles institucionais
§5 preserva campanha antiga, catálogo anterior e Journey como propostas alternativas, sem equiparar QA Express a Start. §7 entrega inventário de quatro páginas e roteiro de migração; snapshot pontual não verifica funcionalidades nem versão do repositório de site. §8 propõe conciliação entre dois textos de missão/visão/valores sem autoproclamar vigência. Boa aderência conceitual a integridade, transparência, qualidade desde a origem, dados/evidências, 5S e inovação responsável. Direção define referência institucional canônica.

## Ações mínimas para encerramento focal
1. **Executor — correção obrigatória visual:** corrigir sobreposição do slide 2 no PPTX-fonte; fornecer PPTX novo, SHA-256 e renderização; obter inspeção visual no PowerPoint.
2. **Executor — sem retrabalho redundante:** preservar fichas operacionais, alternativas, inventário e fechamento QJ31-06; consolidar somente rastreabilidade do delta visual.
3. **Direção — decisões exclusivas:** referência MVV; A/B/C campanha, portfólio, regular/promocional; preço/escopo dos serviços, limites e capacidade; margem mínima e orçamento do piloto; eventual integração/publicação.
4. **Contábil/jurídico:** confirmar tributação, custos apropriáveis, requisitos de contrato, aceite, alterações, privacidade e responsabilidade antes de venda.
5. **Revisor:** reavaliar somente novo PPTX/renderização e eventual alteração material; não abrir nova auditoria geral.

**Resultado do gate:** documentação comercial suficientemente estruturada para uma futura deliberação informada, mas **não autorizada para distribuição, cotação, piloto ou merge**. PR #3 deve permanecer aberta e sem merge até decisão expressa da Direção. Nenhuma alteração no CRM, site ou contratos; sem homologação de preços.
