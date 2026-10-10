# GT-MKT-CNQ-001 v0.4.1 — evidências da correção focal

**PRONTO PARA REVALIDAÇÃO VISUAL FINAL — SEM AUTORIZAÇÃO PARA DISTRIBUIÇÃO.**

[Parecer REV-MKT-CNQ-006 — PR #26](https://github.com/gentestsai-sudo/gentests-os/pull/26); [tratamento desta rodada](../../../comercial/GT-MKT-CNQ-006-Tratamento-REV-MKT-CNQ-006.md).

- [Novo PDF v0.4.1](../../../comercial/GT-MKT-CNQ-001-Guia-Executivo-v0.4.1.pdf)
- [PDF histórico v0.4.0 preservado](../../../comercial/GT-MKT-CNQ-001-Guia-Executivo-v0.4.0.pdf)
- [Manifesto: SHA-256, deltas, regressão e link](manifest-v0.4.1.json)

## Cinco PNGs individuais do PDF corrigido

- [Página 1](page-01.png)
- [Página 2](page-02.png)
- [Página 3](page-03.png)
- [Página 4](page-04.png)
- [Página 5](page-05.png)

Renderização `pdftoppm -r 150 -png`, versão 26.05.0, imagens 1240×1755. Cinco páginas inspecionadas pelo executor. Página 4: somente remoção dos sete prefixos “–41”; restantes: PNGs byte a byte idênticos à v0.4.0 renderizada no mesmo ambiente. Não equivale a revisão independente ou teste em leitor PDF móvel.

## Reprodução mínima

[Corretor versionado](../../../scripts/fix_cnq_checklist_v040.py) requer Python e pypdf. Sua entrada é estritamente o SHA-256 auditado da v0.4.0; rejeita outra versão.

```sh
python scripts/fix_cnq_checklist_v040.py comercial/GT-MKT-CNQ-001-Guia-Executivo-v0.4.0.pdf arquivo-corrigido.pdf numbering-delta.json
sha256sum arquivo-corrigido.pdf
pdftoppm -r 150 -png arquivo-corrigido.pdf page
```

O corretor modifica apenas o stream da página 4 (objeto 12), seu comprimento e os offsets xref/startxref. Todos os outros objetos são idênticos. O gerador original não está versionado na branch examinada; esta é correção da formatação efetivamente gravada, não alegação de reparo do gerador ausente.

## Link e acessibilidade

Anotação URI na página 5 preservada; centro da URL fica na área clicável; destino respondeu HTTP 200 na consulta registrada. Retângulo herdado não cobre toda a altura do texto extraído. Não houve clique em visualizador nativo nem teste de formulário.

PDF sem tags, árvore estrutural ou idioma declarado; extração de texto funciona, mas não prova ordem semântica, navegação por títulos/tabelas ou conformidade PDF/UA. Não houve teste com leitor de tela. Alternativa HTML semântica foi avaliada no tratamento, sem implementação/publicação. Nenhuma distribuição, captação ou mudança de site autorizada.
