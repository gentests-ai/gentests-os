# GT-MKT-CNQ-009 — Execução dos três testes práticos autorizados

Data: 2026-10-10. Autorização restrita: [DEC-MKT-CNQ-20261010-001 / issue #35](https://github.com/gentestsai-sudo/gentests-os/issues/35). Baseline: PR #4, commit `66567810a376d9dba0b665aed06c63e8d8b4a537`. Parecer anterior: [REV-MKT-CNQ-009 / PR #34](https://github.com/gentestsai-sudo/gentests-os/pull/34). **Este registro não atesta execução de testes práticos indisponíveis.**

| ID | Ambiente/ferramenta disponível | Procedimento executado | Resultado | Evidência | Defeito / risco residual |
|---|---|---|---|---|---|
| TP-01 — clique real no link da p.5 | Conector GitHub permite recuperar o PDF, mas **não disponibiliza interface de leitor PDF clicável nesta sessão** | Conferência do parecer e evidências anteriores; **não houve clique real em leitor PDF** | **NÃO EXECUTADO** | `checks-v0.4.2.json` e `pdfjs-reader-api.json` registram URI e anotação, mas não clique; [README v0.4.2](README.md) | Destino por clique não comprovado; nenhum defeito novo confirmado |
| TP-02 — leitura assistiva | **Sem NVDA/VoiceOver operável e sem controle de leitor de tela nesta sessão** | Conferência documental de idioma/tags/outline já registrados; **sem navegação assistiva real** | **NÃO EXECUTADO** | `checks-v0.4.2.json`; parecer REV-MKT-CNQ-009 | Ordem efetiva, listas, tabelas (TD sem TH) e navegação não validadas; PDF/UA não comprovado |
| TP-03 — celular físico | **Sem dispositivo físico acessível ao executor nesta sessão** | Não houve abertura em aparelho nem teste de rotação, zoom ou toque no link; simulações existentes **não substituem** teste real | **NÃO EXECUTADO** | `mobile-simulation-1.png` a `mobile-simulation-5.png` apenas como material de referência | Legibilidade em tela pequena, orientação, gestos e toque não comprovados |

## Síntese

- **Defeitos materiais novos:** nenhum confirmado, pois os três testes práticos não puderam ser realizados.
- **Status:** execução documental da matriz concluída, mas **gate prático permanece aberto**. Nenhum dos três testes pode receber APROVADO.
- **Recomendação à Direção:** providenciar ambiente de leitor PDF com interface clicável, tecnologia assistiva operável e telefone físico, ou deliberar expressamente sobre riscos residuais sem afirmar aprovação dos testes. Encaminhar à revisão independente focal **somente quando houver resultados práticos novos**. Não reabrir hash/inspeção visual já encerrados no REV-MKT-CNQ-009.
- **Restrições observadas:** PDF inalterado, PR #4 aberta/Draft, sem merge, publicação, distribuição, campanha, captação, site, CRM, preços, contratos ou políticas.
