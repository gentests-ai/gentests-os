---
id: GT-COM-QJ-005
tipo: tratamento-focal-visual
versao: 0.1.0
status: proposta
estado_documental: aguardando-revalidacao-independente
data: 2026-10-10
timezone: America/Sao_Paulo
responsavel_elaboracao: Codex-executor
pr_execucao: 3
pr_parecer: 19
parecer_origem: REV-COM-QJ-004
achado: VIS-QJ-004-01
aprovacao_visual: pendente
homologacao_precos: nao
autorizacao_piloto: nao
---
# GT-COM-QJ-005 — Correção focal da apresentação v3.2

## Origem e alcance

Direção solicitou corrigir somente a sobreposição do terceiro cartão do slide 2 após [REV-COM-QJ-004](https://github.com/gentestsai-sudo/gentests-os/blob/7c1ce00759a11576dba0cc83b58dce14368ec55f/revisoes/REV-COM-QJ-004-Parecer-Quality-Journey.md), blob `01ee428d41cb4b599f0855d88584cbc5e8229c0e`, PR #19. Parecer aprova evolução documental com ressalvas, sem aprovação para distribuição, comercialização ou piloto. Fonte de execução: commit `985e47531aa134cf1970281fd5eb51020eb2da32`, [PR #3](https://github.com/gentestsai-sudo/gentests-os/pull/3).

Sem reabrir escopos, financeiro, campanha, site, identidade ou decisões já examinadas. [GT-COM-QJ-004](GT-COM-QJ-004-Tratamento-REV-COM-QJ-003.md) e os pareceres anteriores permanecem intactos. **QJ31-06 continua encerrado no alcance documental**. Aplicação de 5S: intervenção mínima e reutilização das nove renderizações sem alteração; nenhum novo controle comercial paralelo. A alteração preserva a mensagem institucional, o rigor/transparência e o conteúdo previamente examinado, sem escolher formulação de missão, visão ou valores.

## Correção executada — VIS-QJ-004-01 / QJ31-04

Terceiro cartão, título “Decisões sem evidências”: ampliar altura da caixa, reposicionar o corpo abaixo do título e adequar sua altura ao espaço restante. Texto, fonte, tamanho, cor, largura e posição horizontal preservados; nenhuma promessa comercial nova.

| Caixa / parâmetro (pixels a 96 DPI) | Antes | Depois |
|---|---:|---:|
| Título: topo | 357,12 | 357,12 |
| Título: altura | 44,16 | 71,04 |
| Corpo: topo | 412,80 | 452,00 |
| Corpo: altura | 110,40 | 74,40 |

Há 23,84 pixels entre as caixas após a alteração. A inspeção do executor mostra separação legível entre título em duas linhas e corpo em três linhas na projeção fornecida. Não é declaração de aprovação independente.

Autoria de geometria com Artifact Tool; para evitar reserialização e alterações alheias ao escopo, somente as três coordenadas alteradas foram aplicadas ao pacote OOXML original. Comparação por entrada descompactada: apenas `ppt/slides/slide2.xml` mudou; todas as outras entradas e todos os textos são idênticos. Arquivo anterior preservado, sem sobrescrita.

## Binário e evidências

- [PPTX corrigido v3.2.1](apresentacoes/GenTests_Apresentacao_Comercial_Quality_Journey_v3_2_1_Correcao_Focal.pptx), **50708 bytes**, dez slides.
- SHA-256 novo: `c206916a04666fc7c0f9eed700711db9e5bbd0bb81a605ce2ad784d5b963cd44`.
- SHA-256 anterior preservado: `b228419977c3267a6b3696a25c40886fc9ffce6ff9ab0d5791750d6661760a48`.
- [Evidências atualizadas](../05-Evidencias/Quality-Journey-v3.2.1/README.md): slide 2 antes/depois, manifesto de hashes e geometria, dez slides referenciados.

Dez slides re-renderizados a partir do novo PPTX; nove PNGs sem alteração são idênticos byte a byte aos anteriores. Validação do pacote, geometria (dimensões/fonte do arquivo de referência) e importação com Artifact Tool passaram. Essas verificações não equivalem a aprovação visual, técnica comercial ou abertura em PowerPoint.

## Pendência focal e limites

**Executor concluiu a correção e sua verificação local por renderização.** Revisor independente deve conferir o novo hash e revalidar o terceiro cartão do slide 2. **Abertura/inspeção no PowerPoint nativo permanece pendente**, pois não foi executada neste ambiente; não declarar equivalência tipográfica nem aprovação de distribuição antes dessa conferência.

Não alterar ou homologar preços, contratos, CRM, site ou identidade; não iniciar piloto/comercialização. Manter decisões da direção e validações contábeis/jurídicas nos estados já registrados. Nenhum novo risco material foi identificado pela comparação focal do pacote; não emitir novo parecer independente pelo executor.

**PR #3 deve permanecer draft, aberta e sem merge até autorização expressa.** Solicitar encerramento focal de VIS-QJ-004-01/QJ31-04 pelo revisor, com as limitações acima; não inferir encerramento automático por upload.
