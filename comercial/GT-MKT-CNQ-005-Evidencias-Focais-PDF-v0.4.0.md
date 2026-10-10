---
id: GT-MKT-CNQ-005
tipo: evidencias-focais-pdf-v040
versao: 0.1.0
status: inspecao-visual-bloqueada-por-transferencia-do-binario
data: 2026-10-10
parecer_origem: REV-MKT-CNQ-005
distribuicao_autorizada: nao
merge_autorizado: nao
---
# GT-MKT-CNQ-005 — Evidências focais do PDF Executivo v0.4.0

> **NÃO PRONTO PARA REVALIDAÇÃO VISUAL INDEPENDENTE.** Este relatório registra o que foi comprovado e distingue expressamente o que ainda não pôde ser executado. Não declarar layout aprovado, defeitos visuais ou versão acessível sem inspeção real.

## 1. Artefato preservado e integridade

- Fonte: [PR de execução #4](https://github.com/gentestsai-sudo/gentests-os/pull/4), branch `review/custo-nao-qualidade-v0-1`; arquivo **não modificado** `comercial/GT-MKT-CNQ-001-Guia-Executivo-v0.4.0.pdf`.
- Commit do PDF examinado pelo parecer: `d87fdfb46a5467067fa7cb53ccbdcffe1341f270`.
- Git blob SHA-1 retornado pelo conector: `68c0dcbb6102f2a3de561f11d83776f9862c1897`.
- **SHA-256 do PDF original:** `7db1aa3b3d3fda0dea907dbe85550d98940bbae9cd05d8b87fc09440d5f66e8b`.
- Método: leitura integral `base64` pelo conector GitHub do **commit exato**, decodificação em memória em bytes e cálculo SHA-256 por implementação JavaScript SHA-256 (FIPS 180-4); tamanho decodificado: **13.680 bytes**. Assinaturas observadas: `%PDF-1.4` e `%%EOF`. **Recomendado conferência cruzada** do SHA-256 por `sha256sum` no arquivo baixado na futura etapa de renderização; não confundir SHA do Git com SHA-256.

## 2. Estrutura verificada sem renderização

Inspeção de tokens do PDF decodificado (não é auditoria PDF/UA): cinco objetos `/Type /Page`; cinco `/MediaBox [0 0 595 842]` (A4 aproximado em pontos). Foi identificado **um marcador `/Subtype /Link`** e dois tokens `/URI`, com URL textual `https://gentests-site.pages.dev/`. Isso **não comprova** clique funcional nem visibilidade do CTA no layout. Não foram localizados marcadores literais `/Lang`, `/StructTreeRoot` ou `/MarkInfo`; forte evidência de ausência de semântica/tagging, sujeita à validação por ferramenta especializada e leitura assistiva. Existência de texto selecionável, contraste, ordem de leitura e descrição de imagens **não verificados**.

## 3. Matriz de evidência visual obrigatória

| Página | Binário no Git | PNG individual do PDF exato | Layout, card, recorte, margens e contraste | Celular e desktop |
|---|---|---|---|---|
| 1 | preservado | **NÃO GERADO** | **NÃO VERIFICADO** | **NÃO VERIFICADO** |
| 2 | preservado | **NÃO GERADO** | **NÃO VERIFICADO** | **NÃO VERIFICADO** |
| 3 | preservado | **NÃO GERADO** | **NÃO VERIFICADO** | **NÃO VERIFICADO** |
| 4 | preservado | **NÃO GERADO** | **NÃO VERIFICADO** | **NÃO VERIFICADO** |
| 5 | preservado | **NÃO GERADO** | **NÃO VERIFICADO** | **NÃO VERIFICADO** |

**Bloqueio real desta rodada:** o binário foi acessado dentro da integração GitHub, mas a transferência para o ambiente separado de renderização não esteve disponível. A tentativa de obtenção direta do GitHub por HTTP no ambiente de arquivos não funcionou (erro de resolução de rede). **Nenhuma inspeção visual foi executada.** Não afirmar que o documento contém (ou não contém) cortes/sobreposições sem imagens.

## 4. Complemento necessário para levantar o bloqueio
1. Disponibilizar o PDF **exatamente binário** de 13.680 bytes por upload montável ao ambiente de renderização; confirmar SHA-256 `7db1aa3b3d3fda0dea907dbe85550d98940bbae9cd05d8b87fc09440d5f66e8b` antes do trabalho.
2. Gerar individualmente PNGs de páginas 1–5, idealmente `pdftoppm -f 1 -l 5 -png -r 180`, registrar programa, versões, hash e dimensões.
3. Inspecionar individualmente recorte de texto, margens, caixas, contrastes, alinhamento, sobreposição, links e CTA; registrar recortes de defeitos reais com localização, página e severidade.
4. Inspecionar visualização em larguras móveis e desktop sem interpolar como teste assistivo; se defeito comprovado, alterar apenas a fonte pertinente e emitir PDF com nova versão/hash/renderizações.
5. Validar texto/ordem de leitura, idioma, árvore de tags, leitura assistiva e link anotado. Considerar versão HTML semântica e responsiva **somente como proposta** quando necessária, sem autorizar publicação.

## 5. Resultado e restrições
**Status: evidência parcial (hash/contagem/indicadores estruturais) e bloqueio do gate visual.** Não satisfaz os critérios do REV-MKT-CNQ-005 para revalidação visual; não declarar “pronto” nem pedir aprovação visual sem renders. Conteúdo técnico-financeiro anteriormente revisado fica preservado; PDF original não foi modificado. Não houve merge, divulgação, campanha, captação, edição de preços, contratos, CRM, site ou implementação.
