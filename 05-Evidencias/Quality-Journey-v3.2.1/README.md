# Quality Journey v3.2.1 — correção focal do slide 2

Achado VIS-QJ-004-01 / QJ31-04 do [REV-COM-QJ-004, PR #19](https://github.com/gentestsai-sudo/gentests-os/pull/19). [Tratamento focal](../../comercial/GT-COM-QJ-005-Correcao-Focal-REV-COM-QJ-004.md).

- [PPTX corrigido](../../comercial/apresentacoes/GenTests_Apresentacao_Comercial_Quality_Journey_v3_2_1_Correcao_Focal.pptx)
- [Manifesto, SHA-256 e geometria antes/depois](render-manifest.json)
- [Slide 2 anterior](../Quality-Journey-v3.2/slide-02.png)
- [Slide 2 corrigido](slide-02.png)

Somente a geometria de duas caixas do terceiro cartão foi ajustada. Texto e fonte Aptos preservados. A única parte OOXML alterada é `ppt/slides/slide2.xml`; todas as demais partes descompactadas são idênticas. O PPTX anterior continua preservado em seu caminho original.

Dez slides foram renderizados a partir do novo binário. Os nove PNGs sem alteração são byte a byte idênticos aos anteriores: o manifesto os referencia em vez de duplicá-los. O slide 2 corrigido não apresenta a sobreposição na projeção inspecionada pelo executor.

**Sem aprovação visual independente.** Não houve abertura em PowerPoint nativo, cuja conferência permanece pendente. Verificações estruturais, geometria e importação passaram, mas não aprovam distribuição, venda ou piloto.

## Renderização e verificação

Usar [render.mjs existente](../Quality-Journey-v3.2/render.mjs), com Node e `@oai/artifact-tool` disponíveis:

```sh
node render.mjs arquivo-corrigido.pptx pasta-de-saida
sha256sum arquivo-corrigido.pptx
```

Conferir SHA-256 do binário com o manifesto. Inspecionar o slide 2 no PowerPoint e na renderização, incluindo quebra do título, distância ao corpo e limite inferior do cartão. As projeções podem variar por fontes/renderer; novo hash após qualquer edição. Revalidar somente o delta focal e eventual risco material novo, preservando os encerramentos documentais anteriores.

## Dez slides para inspeção

- [Slide 01](../Quality-Journey-v3.2/slide-01.png)
- [Slide 02](slide-02.png)
- [Slide 03](../Quality-Journey-v3.2/slide-03.png)
- [Slide 04](../Quality-Journey-v3.2/slide-04.png)
- [Slide 05](../Quality-Journey-v3.2/slide-05.png)
- [Slide 06](../Quality-Journey-v3.2/slide-06.png)
- [Slide 07](../Quality-Journey-v3.2/slide-07.png)
- [Slide 08](../Quality-Journey-v3.2/slide-08.png)
- [Slide 09](../Quality-Journey-v3.2/slide-09.png)
- [Slide 10](../Quality-Journey-v3.2/slide-10.png)
