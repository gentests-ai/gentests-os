# GT-MKT-CNQ-008 — Matriz de fechamento residual v0.4.2

Data: 2026-10-10. Escopo estritamente residual do parecer [REV-MKT-CNQ-008 / PR #32](https://github.com/gentestsai-sudo/gentests-os/pull/32). Referência de PDF: commit `17c9f8bf645fe75aaba083bad0be8c96440575f8`. **Não constitui autorização para distribuição.**

| Verificação | Resultado nesta rodada | Evidência efetiva | Limite / risco |
|---|---|---|---|
| Visual páginas 1, 2, 3 e 5 | **NÃO EXECUTADO diretamente** | PNGs já versionados `page-1/2/3/5.png` e inspeção anterior descrita no README; autocheck sem sobreposições | A inspeção direta independente solicitada ainda não foi repetida; não inferir aprovação visual |
| Página 4 | **APROVADO anteriormente, sem nova inspeção** | REV-MKT-CNQ-008 validou numeração 1–7 | Não reabrir |
| SHA-256 independente | **INCONCLUSIVO — investigar divergência** | PDF recuperado via conector GitHub do commit indicado: 67.317 bytes, Git blob `b254e8e615299d1435a31f6dc1fe8285cf32dc7f`. Primeira implementação SHA-256 em JavaScript produziu `32c05e1ca7a9ae703862f664134b2b6471458faea5f85face32ac03cc079a2f7`; manifesto declara `44a2cae3dcb8706fb0674b8140a6e8a29edd9688bc6782c9f945dfdcf277b60e`. | **Não concluir corrupção nem equivalência:** conferir algoritmo com vetores de teste e recomputar com `sha256sum` ou `hashlib` sobre binário local idêntico antes de decisão |
| Clique real no link página 5 | **NÃO EXECUTADO** | `checks-v0.4.2.json`: anotação contém texto, URI `https://gentests-site.pages.dev/`; HTTP 200 declarado anteriormente | Verificação de anotação/API e HTTP não substitui clique em leitor PDF |
| Acessibilidade assistiva | **NÃO EXECUTADO** | `checks-v0.4.2.json` e `pdfjs-reader-api.json`: Lang pt-BR, tags, outline e ToUnicode declarados; tabelas com TD sem TH | Sem leitor de tela, sem confirmação de ordem de leitura real, sem certificação PDF/UA |
| Dispositivo móvel físico | **NÃO EXECUTADO** | Simulações de 390 px já versionadas | Simulação não é telefone real; layout A4 requer zoom e pan |

## Decisão proposta à Direção

**Manter PR #4 em Draft e bloquear distribuição.** Não gerar outra versão sem defeito material comprovado. Próximo passo mínimo: (1) validar SHA-256 por ferramenta independente confiável; (2) inspecionar diretamente os PNGs das páginas 1,2,3,5; (3) clique em leitor PDF e leitura assistiva quando houver ambiente; (4) teste em telefone físico quando disponível ou aceitar expressamente a limitação, sem declarar o teste executado. Avaliar HTML semântico como alternativa, sem implantação automática. Conteúdo técnico-financeiro e página 4 fora de escopo. Nenhuma alteração em site, CRM, preços, campanhas ou política.
