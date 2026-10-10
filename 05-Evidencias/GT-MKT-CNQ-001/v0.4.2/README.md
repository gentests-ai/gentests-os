# GT-MKT-CNQ-001 v0.4.2 — evidências focais

**Revalidação independente focal solicitada. Sem autorização para distribuição.**

PDF: [Guia Executivo v0.4.2](../../../comercial/GT-MKT-CNQ-001-Guia-Executivo-v0.4.2.pdf). [Tratamento GT-MKT-CNQ-007](../../../comercial/GT-MKT-CNQ-007-Tratamento-REV-MKT-CNQ-007.md). [Manifesto com hashes](manifest-v0.4.2.json). [Autocheck](checks-v0.4.2.json). [Estruturas e anotação lidas pela API PDF.js](pdfjs-reader-api.json).

| Página | PNG principal — Poppler 150 DPI | Segundo motor — MuPDF | Comparação histórica | Simulação móvel |
|---|---|---|---|---|
| 1 | [page-1.png](page-1.png) | [mupdf-1.png](mupdf-1.png) | [comparison-1.png](comparison-1.png) | [mobile-simulation-1.png](mobile-simulation-1.png) |
| 2 | [page-2.png](page-2.png) | [mupdf-2.png](mupdf-2.png) | [comparison-2.png](comparison-2.png) | [mobile-simulation-2.png](mobile-simulation-2.png) |
| 3 | [page-3.png](page-3.png) | [mupdf-3.png](mupdf-3.png) | [comparison-3.png](comparison-3.png) | [mobile-simulation-3.png](mobile-simulation-3.png) |
| 4 | [page-4.png](page-4.png) | [mupdf-4.png](mupdf-4.png) | [comparison-4.png](comparison-4.png) | [mobile-simulation-4.png](mobile-simulation-4.png) |
| 5 | [page-5.png](page-5.png) | [mupdf-5.png](mupdf-5.png) | [comparison-5.png](comparison-5.png) | [mobile-simulation-5.png](mobile-simulation-5.png) |

Executor inspecionou individualmente as cinco páginas principais e as cinco simulações derivadas de MuPDF: sem colisões, palavras fragmentadas ou texto cortado no PDF. P.3: colunas e valores legíveis; p.4: sequência 1–7, continuações e acentos corretos; p.5: CTA, URL e referências legíveis. Não é aprovação independente.

As simulações são imagens matemáticas de viewport de 390 px: painel esquerdo ajusta a largura; os outros dois mostram zoom 200% e deslocamento horizontal. **Não são capturas de leitor ou de telefone físico.** Ao ajustar toda a largura, o corpo tem cerca de 7,87 px e fica pequeno; com zoom 200%, cerca de 15,73 px. A página A4 mantém layout fixo e exige navegação horizontal. Não declarar experiência móvel responsiva/reflow validada.

## Reproduzir

Python 3.12.14; instalar as versões no manifesto: `reportlab==4.4.9`, `pypdf==6.10.0`, `PyMuPDF==1.26.6`, `Pillow==12.3.0` (conferir versão efetiva no manifesto); Poppler 26.05.0 para equivalência dos PNGs.

```bash
python scripts/build_cnq_v042.py comercial/GT-MKT-CNQ-001-Guia-Executivo-v0.4.1.pdf /tmp/cnq-v042.pdf
sha256sum /tmp/cnq-v042.pdf
python scripts/verify_cnq_v042.py /tmp/cnq-v042.pdf comercial/GT-MKT-CNQ-001-Guia-Executivo-v0.4.1.pdf /tmp/cnq-evidencias
```

Fontes em `scripts/fonts/cnq/`, com licença; guardas de hash da entrada e igualdade de texto normalizado. Duas gerações locais deram o mesmo binário/hash. O verificador gera PNGs dos dois motores, simulações e autocheck; os comparativos são os PNGs históricos v0.4.1 lado a lado com os novos, reduzidos proporcionalmente para visão geral. O PDF.js 5.6.205 leu as cinco árvores e a anotação, cujo `overlaidText` é exatamente a URL visível; isso **não equivale a clique na interface**.

## Limites e fechamento focal

Área clicável corrigida e contém integralmente a caixa da URL; URI correta; destino HTTP 200 em 10/10/2026, 20:38:15 UTC / 17:38:15 BRT. **Clique em leitor PDF não executado**: navegador remoto recusou `file://` por política de URL; nenhuma tentativa de contornar a restrição. A chamada comercial permanece igual; sem teste/envio de formulário.

Estrutura marcada, idioma pt-BR, fontes incorporadas e ToUnicode, títulos, parágrafos, listas com Lbl/LBody, tabelas, link associado à anotação e cinco marcadores implementados. Sem certificação PDF/UA, validador especializado ou teste de leitor de tela. Tabelas preservam rótulos existentes sem inserir novos cabeçalhos; testar leitura assistiva e reflow no leitor escolhido.

**Uma única revalidação:** recomputar hash; inspecionar páginas 1–5; verificar numeração; clicar a URL em leitor PDF e conferir destino sem enviar formulário; verificar leitura assistiva/ordem semântica e registrar limites. Ciência, finanças e textos históricos fora do escopo. Direção decide eventual alternativa HTML semântica; não implementada nem publicada nesta rodada.
