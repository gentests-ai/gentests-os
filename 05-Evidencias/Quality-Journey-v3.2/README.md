# Quality Journey v3.2 — evidências para revisão independente

Arquivo-fonte: [PPTX exato](../../comercial/apresentacoes/GenTests_Apresentacao_Comercial_Quality_Journey_v3_2_Revisao_Interna.pptx). Tratamento: [GT-COM-QJ-004](../../comercial/GT-COM-QJ-004-Tratamento-REV-COM-QJ-003.md).

[Manifesto e SHA-256](render-manifest.json). Dez PNGs completos, 1280×720, produzidos por importação read-only do PPTX com `@oai/artifact-tool`; nenhum salvamento/reexportação do original. Os PNGs não são aprovação visual nem substituem inspeção do binário em PowerPoint. No slide 2, terceiro cartão, há proximidade/sobreposição entre título e corpo na projeção; confrontar com o programa original. O hash do arquivo-fonte foi conferido antes/depois e deve ser conferido pelo novo revisor.

## Slides

- [slide-01](slide-01.png)
- [slide-02](slide-02.png)
- [slide-03](slide-03.png)
- [slide-04](slide-04.png)
- [slide-05](slide-05.png)
- [slide-06](slide-06.png)
- [slide-07](slide-07.png)
- [slide-08](slide-08.png)
- [slide-09](slide-09.png)
- [slide-10](slide-10.png)

## Verificação/reprodução

1. Baixar o PPTX e os PNGs sem edição e conferir `sha256sum` contra o manifesto.
2. Abrir o PPTX em PowerPoint, conferir texto, legibilidade, alinhamento e fronteiras comerciais; observar especialmente o terceiro cartão do slide 2.
3. Para reproduzir esta projeção, usar Node com `@oai/artifact-tool` disponível e executar `node render.mjs /caminho/arquivo.pptx /caminho/saida`. A renderização não altera a fonte. Fontes/versão do renderer podem alterar pixels; os hashes identificam a projeção desta rodada, não todas as projeções possíveis.
4. Registrar parecer independente com versão/hash examinados. Havendo edição pelo autor, exigir novo arquivo/hash/renderização; não substituir silenciosamente o binário auditado.

## Site observado

[Snapshot de inventário](site-inventory.json): HTML público coletado em 10/10/2026 16:59:35 UTC. URLs, resoluções, textos, links e hashes de HTML preservados. Quatro páginas distintas pela navegação. Robots/sitemap responderam HTML de fallback da home; não usar como prova de inventário completo. Sem interação/envio de formulário, publicação ou auditoria completa de páginas não vinculadas. Mapas candidatos e decisões em GT-COM-QJ-004 §7.
