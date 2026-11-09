---
id: REV-MKT-CNQ-006
tipo: parecer-complementar-independente-visual
versao: 1.0.0
status: parecer-emitido
data: 2026-10-10
artefato: GT-MKT-CNQ-001-Guia-Executivo-v0.4.0.pdf
base_de_evidencia: ZIP fornecido pela Direcao com cinco PNGs e manifesto
resultado: CORRECAO_FOCAL_OBRIGATORIA
distribuicao_autorizada: nao
---
# REV-MKT-CNQ-006 — Inspeção visual focal das cinco páginas v0.4.0

## Resultado executivo
**NÃO APROVADO PARA DISTRIBUIÇÃO — DEFEITO EDITORIAL CONFIRMADO NA PÁGINA 4.** A inspeção independente das cinco imagens PNG do pacote `GT-MKT-CNQ-v040-evidencias-visuais(1).zip` confirmou contaminação visual da numeração do checklist com o prefixo indevido `–41` antes dos números 1 a 7. É defeito objetivo de qualidade editorial, que compromete a percepção profissional do material destinado à captação B2B. Recomenda-se somente a correção focal, regeneração das páginas pertinentes e nova inspeção.

## Fonte, identidade e limites
- PR original de execução [#4](https://github.com/gentestsai-sudo/gentests-os/pull/4); parecer precedente [#25](https://github.com/gentestsai-sudo/gentests-os/pull/25).
- Manifesto incluído no ZIP: PDF original declarado com 13.680 bytes e SHA-256 `7db1aa3b3d3fda0dea907dbe85550d98940bbae9cd05d8b87fc09440d5f66e8b`; método indicado `pdftoppm -r 150 -png`.
- **O PDF original não foi fornecido dentro do ZIP. Portanto o SHA-256 do PDF foi lido do manifesto, não calculado independentemente nesta rodada.** Cinco PNGs reais foram descompactados, examinados e têm dimensão 1240x1755 px; arquivos individuais disponíveis no pacote. A correspondência criptográfica dessas projeções ao PDF original precisa de conferência independente com o binário.
- Não foi feita avaliação com leitores de tela nem certificação PDF/UA; inspecionar marcação semântica e idioma no binário ou disponibilizar HTML acessível como alternativa.

## Matriz visual página a página

| Página | Inspeção feita | Resultado | Evidência/correção |
|---|---|---|---|
| 1 — Abertura | PNG inspecionado | Sem sobreposição/corte relevante visível | Hierarquia título/subtítulo clara. Revisar legibilidade móvel do corpo/rodapé no PDF definitivo |
| 2 — O impacto | PNG inspecionado | Sem sobreposição/corte relevante visível | Três blocos bem separados, margens preservadas |
| 3 — Exemplo financeiro | PNG inspecionado | Sem sobreposição/corte relevante visível | Valores e ressalva hipotética legíveis na projeção, sujeito a verificação de zoom móvel |
| 4 — Checklist | PNG inspecionado | **DEFEITO CONFIRMADO — Médio, bloqueante para distribuição** | Prefixo `–41` aparece sete vezes antes dos marcadores 1 a 7 (exemplo `–41 1. Registre horas...`). Corrigir geração da lista, sem alterar conteúdo conceitual |
| 5 — Próximos passos | PNG inspecionado | Sem sobreposição/corte relevante visível | CTA com URL aparente `https://gentests-site.pages.dev/`, sem comprovação de link clicável ou destino funcional |

**Critério visual aplicado:** nenhum elemento essencial evidentemente cortado ou card incompleto nas cinco projeções; não se observaram blocos sobrepostos que inviabilizem leitura fora da lista contaminada. Inspeção de PNG estático não verifica interatividade, zoom real em aparelho nem ordem de leitura do PDF.

## Achados
1. **CNQ-VIS-006-01 / Médio, bloqueante para distribuição:** prefixo estranho repetido na numeração da página 4. Ajustar especificamente o componente/gerador do checklist; produzir PDF corrigido, novo SHA-256, renderizar cinco páginas e revalidar, com foco na p.4 e regressão rápida nas demais.
2. **CNQ-A11Y-006-02 / Médio, não verificável:** PDF sem validação independente de marcação, ordem de leitura, idioma, contraste técnico e leitor assistivo. Uma versão HTML semântica pode ser solução proporcional, sem afirmar que o PDF esteja conforme PDF/UA.
3. **CNQ-LINK-006-03 / Baixo, não verificável:** a URL de contato é visível em imagem, mas PNG não prova anotação de hiperlink clicável nem disponibilidade do destino. Conferir no PDF.
4. **CNQ-INTEGRIDADE-006-04 / Médio, evidência pendente:** hash do PDF apenas declarado no manifesto; verificar de modo independente a identidade binária quando arquivo PDF for disponibilizado junto às projeções.

## Conteúdo e governança
Mantêm-se as conclusões científicas/financeiras das revisões anteriores no alcance aprovado. Não há sinal nos PNGs de promessas de ROI realizado ou de estudos internos fabricados. Não aprovar publicação ou campanha: qualidade técnica, identidade, LGPD e coleta requerem autorizações próprias. Este parecer não altera preços, site, CRM, contratos, políticas ou material do executor.

## Próximo passo
Pedir **uma rodada focal de correção do prefixo da lista**, com PDF substituto versionado, hash, PNGs de todas as páginas e teste simples de hiperlink; revisor compara sobretudo página 4 e eventuais diferenças inesperadas. Acessibilidade semântica permanece uma verificação separada para distribuição e não deve ser inferida de imagens. PR de execução sem merge até decisão da Direção.
