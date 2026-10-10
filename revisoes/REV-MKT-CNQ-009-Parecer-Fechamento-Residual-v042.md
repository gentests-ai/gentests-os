---
id: REV-MKT-CNQ-009
tipo: parecer-independente-focal
data: 2026-10-10
objeto: GT-MKT-CNQ-001-v0.4.2
pr_execucao: 4
commit_revisado: 66567810a376d9dba0b665aed06c63e8d8b4a537
resultado: integridade-e-visual-confirmados-com-limites
distribuicao_autorizada: nao
---
# REV-MKT-CNQ-009 — Parecer focal do fechamento residual v0.4.2

**Resultado: FAVORÁVEL AO FECHAMENTO DOCUMENTAL DOS ITENS DE INTEGRIDADE E INSPEÇÃO VISUAL DAS PÁGINAS 1, 2, 3 E 5. DISTRIBUIÇÃO NÃO AUTORIZADA.**

## Fontes e método
Inspecionada a matriz `05-Evidencias/GT-MKT-CNQ-001/v0.4.2/GT-MKT-CNQ-008-Fechamento-Residual.md` no commit `66567810a376d9dba0b665aed06c63e8d8b4a537`, seu README e **abertas visualmente, de forma independente**, as quatro imagens PNG versionadas `page-1.png`, `page-2.png`, `page-3.png`, `page-5.png` do mesmo commit. PR #4 confirmada aberta/Draft. Não reavaliados página 4, cálculos, conteúdo, método científico ou PDF/UA.

## Matriz de resultados
| Item | Conclusão independente | Evidência e limite |
|---|---|---|
| SHA-256 / binário | **EVIDÊNCIA DOCUMENTAL SUFICIENTE PARA FECHAMENTO FOCAL** | Matriz relata duas implementações independentes, Python hashlib e GNU sha256sum, previamente verificadas por três vetores conhecidos, convergindo em `44a2cae3dcb8706fb0674b8140a6e8a29edd9688bc6782c9f945dfdcf277b60e`, tamanho 67.317 bytes e Git blob `b254e8e615299d1435a31f6dc1fe8285cf32dc7f`. Nesta revisão, o hash **não foi recomputado novamente sobre os bytes do PDF**; confirma-se a consistência e suficiência do registro técnico, não uma terceira execução. |
| Página 1 | **CONFIRMADA VISUALMENTE** | Imagem PNG inspecionada: título, subtítulo, lista, margens e rodapé legíveis, sem colisões. |
| Página 2 | **CONFIRMADA VISUALMENTE** | Imagem PNG inspecionada: três seções legíveis, margens e separadores preservados. |
| Página 3 | **CONFIRMADA VISUALMENTE** | Imagem PNG inspecionada: colunas, valores e ressalvas separados e legíveis; aritmética não reavaliada. |
| Página 5 | **CONFIRMADA VISUALMENTE** | Imagem PNG inspecionada: CTA, URL, fontes e ressalvas legíveis; aparência não demonstra clique. |
| Correspondência PNG/PDF | **EVIDÊNCIA DOCUMENTAL SUFICIENTE** | Matriz relata PNGs re-renderizados com Poppler e byte-idênticos aos versionados, com hashes individuais. A re-renderização não foi repetida nesta revisão; nenhuma divergência encontrada na inspeção das imagens versionadas. |
| Divergência JavaScript anterior | **CAUSA NÃO DETERMINADA; NÃO BLOQUEIA INTEGRIDADE** | Dois verificadores independentes concordam; não atribuir causa ao algoritmo, ferramenta ou corrupção sem evidência. |
| Clique real no hiperlink | **NÃO EXECUTADO** | Nenhum leitor PDF com clique real foi utilizado; anotações/HTTP não substituem. |
| Leitura assistiva | **NÃO EXECUTADA** | Ordem de leitura, tabelas e navegação por leitor de tela não comprovadas; não alegar PDF/UA. |
| Telefone físico | **NÃO EXECUTADO** | Simulação de viewport não substitui dispositivo/leitor real; PDF A4 pode exigir zoom e pan. |

## Parecer e encaminhamento
Não foi identificado defeito visual material nas quatro páginas inspecionadas nem contradição documental nas evidências técnicas de hash. A inspeção visual é independente; os testes de hashing e re-renderização são verificações **executadas e registradas pelo Executor**, analisadas documentalmente pelo Revisor. Não declarar que o Revisor reproduziu esses testes. A página 4 permanece encerrada conforme parecer anterior, sem reabertura.

**Recomendo à Direção reconhecer como encerradas documentalmente a integridade e a inspeção visual das páginas 1,2,3,5, sem liberar distribuição.** Manter PR #4 aberta e Draft. Deliberar se/como prover ambiente para (a) clique real no PDF, (b) leitura assistiva, (c) experiência em telefone físico, ou aceitar formalmente limites residuais conforme governança aplicável; não converter ausência de teste em aprovação. Não solicitar nova auditoria integral, regeneração do PDF ou mudança de conteúdo sem defeito comprovado. Nenhum merge, site, CRM, campanha, captação, contratos, preços ou políticas alterados.
