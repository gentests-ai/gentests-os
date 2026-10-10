# BUG-MKT-CNQ-001 — Verificação geométrica focal da anotação v0.4.3

Data: 2026-10-10. Prioridade: **P0**. Issue canônica: [#45](https://github.com/gentestsai-sudo/gentests-os/issues/45). Encaminhamento: [#6103028528](https://github.com/gentestsai-sudo/gentests-os/issues/45#issuecomment-6103028528).

## Identidade da amostra técnica

- Arquivo extraído pelo conector GitHub: `comercial/GT-MKT-CNQ-001-Guia-Executivo-v0.4.3.pdf`, commit imutável `2cd3f69939655894dc9fa4ba348488aae92fd82c`.
- **796.103 bytes** decodificados de base64; Git blob SHA-1 **`e3c152d733e322cbba3dcdce0b4775cb1dea7fe6`**.
- SHA-256 **declarado no pacote**, não recomputado nesta verificação: `0d667a4f7e77aae5fa26dd1aef3c007ebf1ce3ce1d7026acd6e70edbafac4b8a`. Identidade do arquivo efetivamente aberto no iPhone **não demonstrada**.

## Geometria reprodutível

Inspeção estrutural direta do PDF v0.4.3 confirma que a **página 5** possui `/Annots [21 0 R]`, anotação `/Subtype /Link`, `/S /URI`, URI codificada para `https://gentests-site.pages.dev/`, retângulo PDF `[43.5, 321.6172, 235.416, 334.6172]`, `/Rotate 0` e páginas `/MediaBox [0 0 595 842]`.

A caixa do texto da URL já medida nos checks da **v0.4.2** é `[44, 507.8828125, 234.9319916, 519.8828125]` com origem superior; convertendo para origem inferior, altura 842: **`[44, 322.1171875, 234.9319916, 334.1171875]`**. O script/checks v0.4.3 registra igualdade pixel a pixel das páginas 2–5 em relação à v0.4.2, o que permite a comparação **documental**. A anotação contém a caixa do texto com margens esquerda **0,500 pt**, inferior **0,500 pt**, direita **0,484 pt**, superior **0,500 pt**. Não foi identificado deslocamento geométrico pela análise disponível.

[Ver diagrama de sobreposição](link-rect-versus-text-v043.svg) — **esquema de coordenadas**, não PNG extraído do PDF e não prova de clique.

## Reprodução e hipótese

**Reprodução manual relatada pela Direção:** dois leitores no iPhone (pré-visualizador GitHub e Adobe), com 2–3 toques sem acionamento percebido. A gravação prévia comprova abertura/navegação e URL visível, mas não revela coordenadas físicas dos toques. **Nenhum clique novo foi executado pelo Executor nesta rodada**; não há navegador/Adobe iOS controlável nem arquivo local autenticado por SHA nesta sessão. Tentativa de baixar PDF do GitHub no ambiente de renderização resultou em erro de conexão, impedindo render de página 5 com área desenhada sobre o PNG. O diagrama SVG registra apenas a geometria verificada, sem fingir screenshot.

**Resultado:** falha funcional observada/relatada pela Direção em dois leitores; **causa raiz desconhecida**, sem evidência de deslocamento do retângulo. Possibilidades remanescentes: comportamento específico dos visualizadores, modo de pré-visualização, interação/anotações PDF e/ou divergência do arquivo no dispositivo. Não atribuir causa sem teste discriminatório.

**Decisão de alteração:** **não gerar v0.4.4 sem defeito intrínseco comprovado**. Correção especulativa não satisfaria o critério da Direção e poderia introduzir regressão. Preservar layout, logo e textos aprovados.

## Próximo gate mínimo

1. Conferir hash do arquivo **real** aberto no iPhone e versões do iOS/Adobe; diferenciar pré-visualização GitHub de PDF local.
2. Reproduzir toque em arquivo baixado localmente no Adobe Acrobat Reader e, se possível, em leitor adicional; capturar resultado sem dados pessoais.
3. Somente quando identificado defeito do PDF (ou evidência forte de falha multiplataforma intrínseca), corrigir anotação/área de link, produzir **v0.4.4** e hash, registrar diferenças e realizar clique real antes/depois.
4. Encaminhar somente deltas ao Revisor Independente; PR #4 aberta e Draft; sem publicação/merge/campanhas. VoiceOver segue inconclusivo.

**Horas reais de retrabalho:** não medidas. Registro único na issue #45, sem RNC ou bug paralelo.
