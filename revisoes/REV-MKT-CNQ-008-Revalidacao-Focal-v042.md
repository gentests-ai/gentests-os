# REV-MKT-CNQ-008 — Revalidação focal v0.4.2

Data: 2026-10-10. Base: PR #4, commit `17c9f8bf645fe75aaba083bad0be8c96440575f8`. Escopo exclusivo: tipografia, legibilidade, hiperlink, acessibilidade e regressão da numeração.

**Resultado: APROVADO COM RESSALVAS DOCUMENTAIS; NÃO AUTORIZADO PARA DISTRIBUIÇÃO.** Evidências automatizadas são positivas, mas clique real, leitor assistivo e dispositivo móvel físico não foram testados. Não há certificação PDF/UA. Não se reabrem conteúdo, ciência ou finanças.

## Matriz focal

| Item | Resultado | Evidência e limite |
|---|---|---|
| Tipografia e incorporação | Resolvido documentalmente, verificação parcial independente | `checks-v0.4.2.json`: corpo 12pt nas 5 páginas; DejaVuSans e Bold com FontFile2 e ToUnicode. Render PNG da página 4 visualizado diretamente pelo revisor: texto legível, sem sobreposição aparente. Demais páginas constam no pacote mas não foram inspecionadas individualmente nesta sessão. |
| Legibilidade | Parcialmente resolvido | Autocheck sem spans sobrepostos/cortados nas 5 páginas. Simulação 390px: 7,87px no ajuste à largura, 15,73px a 200%, com pan horizontal; experiência móvel real não validada. |
| Hiperlink | Parcialmente resolvido | `checks-v0.4.2.json`: anotação contém integralmente caixa visível; URI `https://gentests-site.pages.dev/`; HTTP 200 declarado. PDF.js API leu anotação. **Clique em interface de leitor não executado.** |
| Acessibilidade | Parcialmente resolvido | Lang pt-BR, marked PDF, Document/Sect/H1/H2/P/L/LI/Lbl/LBody/Table/TR/TD/Link e outline declarados nos checks e PDF.js. Tabelas sem TH; leitor de tela, ordem assistiva e PDF/UA não validados. |
| Numeração | Resolvido visualmente na página 4 | PNG `page-4.png` inspecionado diretamente: sequência 1–7, sem prefixo –41, sem colisão ou corte. |

## Identidade e limitações
Manifesto: `comercial/GT-MKT-CNQ-001-Guia-Executivo-v0.4.2.pdf`, 67.317 bytes, SHA-256 declarado `44a2cae3dcb8706fb0674b8140a6e8a29edd9688bc6782c9f945dfdcf277b60e`. **Não recomputado independentemente**, pois binário não foi transferido ao ambiente local. Evidências consultadas: `05-Evidencias/GT-MKT-CNQ-001/v0.4.2/README.md`, `manifest-v0.4.2.json`, `checks-v0.4.2.json`, `pdfjs-reader-api.json`, `page-4.png`.

## Encerramento e pendências
O defeito de numeração está visualmente encerrado; incorporação de fontes, estrutura semântica e anotação do link têm evidência técnica positiva, mas não substituem validação de usuário final. **Não declarar aprovação visual integral das cinco páginas nesta sessão**, porque apenas a página 4 foi inspecionada diretamente pelo revisor. O material permanece sem autorização de publicação. Se a Direção exigir encerramento de acessibilidade/uso em leitores reais, executar teste focal do link, navegação assistiva e experiência móvel; avaliar HTML semântico como alternativa proporcional. Não realizar nova auditoria de ciência, finanças ou textos. PR #4 permanece Draft e sem merge.
