---
id: REV-MKT-CNQ-007
tipo: parecer-independente-focal-visual
versao: 1.0.0
status: emitido
data: 2026-10-10
pr_execucao: 4
commit_revisado: 86121f4c1273a02c58f66ffa12af444a90b7abb0
resultado_cnq_vis_006_01: resolvido
resultado_distribuicao: bloqueada
aprovacao_direcao: pendente
---
# REV-MKT-CNQ-007 — Revalidação focal independente do Guia Executivo v0.4.1

**Decisão dual: CNQ-VIS-006-01 RESOLVIDO. DISTRIBUIÇÃO AINDA BLOQUEADA por novo achado visual material, identificado na inspeção dos PNGs, além de acessibilidade pendente.** Não reiniciar revisão técnica/financeira.

## Escopo e evidências
Revisados diretamente no commit `86121f4c1273a02c58f66ffa12af444a90b7abb0` o PDF v0.4.1, o PDF histórico v0.4.0, o tratamento GT-MKT-CNQ-006, o manifesto v0.4.1 e **cinco PNGs de páginas 1 a 5**, visualizados independentemente. Revisado o parecer REV-MKT-CNQ-006 da PR #26. PR #4 confirmada aberta e Draft, sem merge.

O **SHA-256 foi recalculado independentemente a partir dos bytes do PDF no GitHub**: v0.4.1 13.631 bytes, SHA-256 `646554cfdba296457af7d0bdc4b50783f2fe44a2841970fce48692a989f5038a`; v0.4.0 13.680 bytes, SHA-256 `7db1aa3b3d3fda0dea907dbe85550d98940bbae9cd05d8b87fc09440d5f66e8b`. Ambos correspondem ao manifesto. Cinco objetos /Page no binário v0.4.1. Inspeção direta do stream do objeto 12 confirmou **zero** ocorrências do prefixo literal `\\22641 ` e os sete marcadores de `1.` a `7.`, com enunciados preservados.

## Matriz focal
| ID | Severidade | Estado | Evidência e consideração |
|---|---|---|---|
| CNQ-VIS-006-01 — Prefixo “–41” | Média histórica / bloqueante antes | **RESOLVIDO** | Página 4: itens 1–7 sem prefixo; inspeção textual do objeto 12 e PNG da página 4 conferidos. |
| CNQ-INTEGRIDADE-006-04 — hash/integridade | Média histórica | **RESOLVIDO** | SHA-256 recalculado de ambos os PDFs, comprimento e páginas conferidos; manifesto consistente. |
| CNQ-REG-007-01 — sobreposição e espaçamento de glifos | **Alta para distribuição B2B**, achado material herdado | **ABERTO / BLOQUEANTE** | Nas **cinco imagens** há colisões, caracteres excessivamente espaçados e fragmentação de palavras em títulos e parágrafos. Ex.: p.1 headline e corpo; p.2 “O custo não termina”; p.3 tabela financeira; p.4 “Como estimar o custo” e itens; p.5 headline, CTA e referências. Este problema já existia nas páginas declaradas idênticas à v0.4.0; **não é regressão causada pela retirada de “–41”**. Contudo, a inspeção atual prova impacto material na legibilidade e qualidade profissional, que não pode ser ignorado para distribuição externa. |
| CNQ-LINK-006-03 — link CTA | Baixa | **Parcial / não bloqueia fechamento do item numérico** | Anotação de link presente na p.5 com `/Rect [40 290 400 330]`. Área intersecciona URL mas não recobre toda altura; destino HTTP 200 foi reportado pelo executor, não houve clique independente em leitor nativo. Deve ser corrigido/testado junto do ajuste visual, sem criar rodada isolada se possível. |
| CNQ-A11Y-006-02 — acessibilidade | Média | **PENDENTE para distribuição acessível** | PDF não tem estrutura marcada (`StructTreeRoot`) nem idioma (`Lang`); não realizado teste assistivo/PDF-UA. Alternativa HTML semântica está apenas proposta, não implementada. Evitar afirmar conformidade. |

## Inspeção de todas as páginas
| Página | Numeração | Achado visual independente |
|---|---|---|
| 1 | N/A | Fragmentação e colisão de letras em título, texto introdutório e tópicos; legibilidade afetada |
| 2 | N/A | Fragmentação nos títulos e blocos explicativos |
| 3 | N/A | Frases, cabeçalhos e linhas financeiras com espaçamento inconsistente; valores ainda decifráveis |
| 4 | **1–7 corretos** | Defeito “–41” removido; caracteres sobrepostos/espaçamento irregular persistem no título e checklist |
| 5 | N/A | CTA e fontes afetados por espaçamento/colisões; link permanece anotado, área incompleta |

**Regressão:** o executor registrou PNGs 1,2,3,5 idênticos a v0.4.0 no mesmo renderizador; revisão do conteúdo binário indica modificação concentrada na página 4. Os problemas tipográficos transversais são **anteriores**, porém só agora estão evidenciados de forma inequívoca nesta inspeção. Não houve nova análise de ciência ou finanças.

## Correção focal obrigatória, sem expansão indevida
Em **uma única rodada**, reconstruir **somente a apresentação tipográfica** do PDF público em todas as páginas com renderização correta de fonte, acentos, kerning e avanço de glifos, preservando integralmente texto, números, CTA e ressalvas; não apenas remover glifos ou aumentar tracking indiscriminadamente. Disponibilizar nova versão, fonte/gerador reproduzível sempre que possível, SHA-256, cinco PNGs e comparação visual por página. Conferir leitura da página 4, tabela da p.3 e CTA p.5. Na mesma intervenção, ajustar área de link e produzir alternativa HTML semântica se a Direção eleger esse caminho; caso contrário, validar solução acessível antes da distribuição. Não realizar nova auditoria financeira/científica. Revalidação posterior **apenas de tipografia/legibilidade, link e solução de acessibilidade**.

## Governança e resultado
A correção CNQ-VIS-006-01 **pode ser encerrada individualmente**. Não é correto fechar o gate visual/global de distribuição: **CNQ-REG-007-01** é impedimento material demonstrado diretamente nas imagens, não melhoria estética opcional. A versão v0.4.1 permanece **NÃO APTA À DISTRIBUIÇÃO**. PR #4 aberta, Draft e sem merge. Publicação, captação de leads, alterações de site/políticas e autorização comercial continuam exclusivas da Direção.
