---
id: GT-MKT-CNQ-007
tipo: tratamento-focal-tipografia-link-acessibilidade
versao: 0.1.0
versao_artefato: 0.4.2
status: revalidacao-focal-com-limitacoes-de-teste
data: 2026-10-10
responsavel_elaboracao: Codex-executor
parecer_origem: REV-MKT-CNQ-007
pr_execucao: 4
pr_parecer: 27
distribuicao_autorizada: nao
merge_autorizado: nao
---
# GT-MKT-CNQ-007 — Tratamento focal do Guia Executivo v0.4.2

**CORREÇÕES IMPLEMENTADAS; REVALIDAÇÃO INDEPENDENTE FOCAL SOLICITADA, COM LIMITAÇÕES DE TESTE DECLARADAS. SEM AUTORIZAÇÃO PARA DISTRIBUIÇÃO.** O clique em leitor PDF, teste assistivo e telefone físico não foram concluídos pelo executor. Não apresentar este registro como autocheck de interface completo ou aprovação final.

## Referências e preservação

[REV-MKT-CNQ-007 / PR #27](https://github.com/gentestsai-sudo/gentests-os/pull/27), [parecer no commit 1ba9767](https://github.com/gentestsai-sudo/gentests-os/blob/1ba9767431a848ccbb14b434238bf1c9cbd9ac6e/revisoes/REV-MKT-CNQ-007-Parecer-Revalidacao-v041.md). Entrada: commit `86121f4c1273a02c58f66ffa12af444a90b7abb0`, [PDF v0.4.1](GT-MKT-CNQ-001-Guia-Executivo-v0.4.1.pdf), SHA-256 `646554cfdba296457af7d0bdc4b50783f2fe44a2841970fce48692a989f5038a`. [GT-MKT-CNQ-006](GT-MKT-CNQ-006-Tratamento-REV-MKT-CNQ-006.md) e demais controles permanecem históricos.

Todas as palavras, números, pontuação, valores, ressalvas, fontes científicas e CTA do PDF foram preservados, comprovados por extração normalizada por página em pypdf e MuPDF; só espaços de composição, tipografia e recursos internos do PDF mudaram. Não houve nova auditoria ou alteração financeira/científica, de metodologia, preços, contratos, CRM, site ou políticas. Versões anteriores não substituídas. CNQ-VIS-006-01 e CNQ-INTEGRIDADE-006-04 permanecem encerrados no alcance da revisão anterior; verificação de regressão não os reabre.

## Tratamento dos três achados

| Achado | Correção pelo executor e evidência | Estado para revisão |
|---|---|---|
| CNQ-REG-007-01 — alta | Fontes DejaVu Sans regular/negrito incorporadas, mapeamento Unicode e avanço por métricas da própria fonte. Corpo de 10,5 para 12 pt; títulos, linhas, paleta e cinco páginas preservados. Colunas financeiras antes compostas por espaços agora alinhadas por coordenadas. Cinco páginas inspecionadas em Poppler e nas projeções MuPDF, sem defeito tipográfico conhecido. | Implementado, candidato a encerramento independente; a experiência móvel sem zoom permanece limitada. |
| CNQ-LINK-006-03 | Retângulo PDF `[43.5 321.6171875 235.416015625 334.6171875]`, caixa do texto integralmente contida com 0,5 pt de margem. URI e texto visível coincidem; API PDF.js confirma `overlaidText`; HTTP 200. | Parcial: falta clique real em leitor PDF; não presumir funcionamento da interface a partir de HTTP/API. |
| CNQ-A11Y-006-02 | PDF 1.7 com Lang pt-BR, MarkInfo, StructTreeRoot/ParentTree, ordem de leitura, H1/H2/P, listas L/LI/Lbl/LBody, Table/TR/TD, Link/OBJR, ToUnicode, título, navegação e artefatos de cabeçalho/rodapé. API PDF.js conseguiu ler as cinco árvores. | Parcial: melhoria proporcional implementada; validação assistiva, leitura de tabelas, reflow e eventual PDF/UA ainda pendentes. Nenhuma conformidade declarada. |

## Causa e correção reproduzível

A v0.4.1 referencia Helvetica/Helvetica-Bold Base14 sem incorporar os programas de fonte. No mesmo ambiente, MuPDF apresenta espaçamento normal enquanto Poppler reproduz os defeitos apontados nas cinco páginas. A divergência evidencia dependência de substituição/renderização de fontes; não atribuir um bug específico ao gerador original, que não consta da branch. A solução incorpora as fontes usadas e elimina essa dependência. Não apenas mudar o renderizador ou substituir imagens antigas.

[Gerador](../scripts/build_cnq_v042.py) reconstrói os comandos de apresentação a partir dos textos/coordenadas da v0.4.1, protegida por hash. Preserva geometria A4 595×842 pt, paleta, hierarquia, quebras e conteúdo. [Fontes e licença](../scripts/fonts/cnq/LICENSE.txt) versionadas; [verificador](../scripts/verify_cnq_v042.py) e [procedimento](../05-Evidencias/GT-MKT-CNQ-001/v0.4.2/README.md). Duas gerações deram bytes idênticos.

## Identidade e inspeção

[PDF v0.4.2](GT-MKT-CNQ-001-Guia-Executivo-v0.4.2.pdf): **67.317 bytes**, cinco páginas. SHA-256: `44a2cae3dcb8706fb0674b8140a6e8a29edd9688bc6782c9f945dfdcf277b60e`.

[Manifesto](../05-Evidencias/GT-MKT-CNQ-001/v0.4.2/manifest-v0.4.2.json) registra hashes, tamanhos, versões e dimensões. [Cinco PNGs principais e evidências complementares](../05-Evidencias/GT-MKT-CNQ-001/v0.4.2/README.md): Poppler 26.05.0 / 150 DPI / 1240×1755 px; segundo motor MuPDF 1.26.6; comparativos antes/depois; simulação móvel por página; [autocheck](../05-Evidencias/GT-MKT-CNQ-001/v0.4.2/checks-v0.4.2.json); [leitura da API PDF.js](../05-Evidencias/GT-MKT-CNQ-001/v0.4.2/pdfjs-reader-api.json).

| Página | Inspeção do executor |
|---|---|
| 1 | Título, subtítulo, acentos e quatro tópicos íntegros; sem colisão ou fragmentação. |
| 2 | Títulos e três blocos completos; espaçamento consistente. |
| 3 | Valores e fórmulas preservados; três colunas de recursos e duas de efeitos alinhadas; ressalvas legíveis. |
| 4 | Marcadores 1–7 sem “–41”; recuos dos itens 6/7, acentos e ressalvas íntegros. |
| 5 | Título, CTA, URL e fontes completos; área do link restrita à linha da URL, sem abranger chamada adjacente. |

Verificação geométrica: zero blocos de texto cortados pela página e zero interseções entre caixas de spans acima da tolerância de 0,3 pt. Inspeção visual complementa esses checks; eles não provam sozinhos ausência de defeitos de glifos.

Simulações de 390 px inspecionadas nas cinco páginas: ajuste da largura resulta em corpo de aproximadamente 7,87 px, pequeno para leitura confortável; zoom 200% oferece aproximadamente 15,73 px, com deslocamento horizontal. **Não houve telefone físico nem UI de leitor móvel.** O PDF A4 não oferece experiência responsiva comprovada. Não esconder esse limite com declaração genérica de “mobile aprovado”.

## Hiperlink: evidência e pendência

Área contém a caixa detectada por MuPDF; PDF.js reconhece URL e texto sobreposto iguais. GET do destino em **10/10/2026, 20:38:15 UTC / 17:38:15 BRT**, retornou **HTTP 200**, URL `https://gentests-site.pages.dev/`, título “GenTests | Qualidade de software que protege a experiência do cliente”. Sem navegação de formulário/captação.

O navegador remoto recusou a abertura do PDF local porque seu protocolo `file://` é bloqueado pela política de URL. Não foi contornada a restrição. **Não há evidência de clique real em leitor; esta etapa segue pendente** para a mesma revalidação focal. API/GET não são substitutos desse teste.

## Acessibilidade: implementação proporcional e alternativa

A estrutura efetiva foi implementada no próprio PDF e reconhecida por outro parser, sem criar produto HTML. Etiquetas de lista separadas de corpos e link associado à anotação; tabelas preservam rótulos aprovados, sem acrescentar cabeçalhos editoriais. Falta validação de leitura de tabelas, navegação por teclado, leitor de tela e reflow no leitor escolhido. Sem execução de veraPDF/PAC nem declaração PDF/UA; tags presentes não são certificação.

**Recomendação submetida à Direção, antes de qualquer implementação:** autorizar ou rejeitar uma futura alternativa HTML semântica com o mesmo conteúdo aprovado, títulos, listas e tabelas acessíveis, sem formulário/captação/publicação nesta etapa. Benefício esperado: leitura responsiva sem pan e melhor compatibilidade assistiva; custo/arquitetura e canal exigem decisão específica. Nenhum HTML foi implementado ou publicado nesta rodada. Direção pode optar por manter PDF marcado e financiar sua validação assistiva especializada antes da distribuição.

## Separação de responsabilidades e gate

1. **Concluído pelo executor:** reconstrução tipográfica, incorporação de fontes, aumento do corpo, alinhamento da tabela, retângulo do link, marcação/idioma/navegação, preservação de textos, numeração, duas gerações iguais, imagens e autocheck local.
2. **Pendências técnicas de teste:** clique em leitor PDF; UI móvel/dispositivo real; leitura assistiva, tabelas/reflow e validador especializado se necessária conformidade. Não marcar achados de link/acessibilidade como integralmente resolvidos.
3. **Direção exclusivamente:** eleger alternativa HTML/arquitetura ou validação especializada; aceitar limites de canal; autorizar merge, distribuição/publicação e eventual captura. Sem decisão presumida.
4. **Revisor independente:** uma única revalidação focal de tipografia/legibilidade nas cinco páginas, link, acessibilidade e regressão 1–7; registrar fechamento individual ou residual. Não reabrir conteúdos históricos sem novo risco material.

PR #4 deve permanecer **aberta e Draft, sem merge**. Histórico íntegro; sem site, distribuição, captação, CRM ou alteração de políticas/contratos. A evidência explícita e a concentração nos três deltas aplicam qualidade e excelência enxuta, sem expansão para redesign ou nova auditoria.
