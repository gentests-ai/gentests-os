---
id: GT-MKT-CNQ-006
tipo: tratamento-focal-numeracao-pdf
versao: 0.1.0
versao_artefato: 0.4.1
status: pronto-para-revalidacao-visual-final
data: 2026-10-10
timezone: America/Sao_Paulo
responsavel_elaboracao: Codex-executor
parecer_origem: REV-MKT-CNQ-006
pr_execucao: 4
pr_parecer: 26
distribuicao_autorizada: nao
merge_autorizado: nao
---
# GT-MKT-CNQ-006 — Correção focal do checklist do Guia Executivo

**PRONTO PARA REVALIDAÇÃO VISUAL FINAL — SEM AUTORIZAÇÃO PARA DISTRIBUIÇÃO.** Não é parecer independente, certificação de acessibilidade ou autorização da Direção.

## 1. Referência e fronteira

[Parecer REV-MKT-CNQ-006](https://github.com/gentestsai-sudo/gentests-os/blob/7a7da503f297c2a7d42cba137cc2058722b4d849/revisoes/REV-MKT-CNQ-006-Parecer-Inspecao-PNG-v040.md), PR #26, blob `17cd98ea3c5921e08686b86f75eb9b1572bb8b4d`. [PR de execução #4](https://github.com/gentestsai-sudo/gentests-os/pull/4), head de entrada `5ad36aa63f06d1e8a867351e0b2aba5372f43520`. [Controle anterior GT-MKT-CNQ-005](GT-MKT-CNQ-005-Evidencias-Focais-PDF-v0.4.0.md) preservado como histórico; o bloqueio anterior de transporte/renderização não se aplica a esta rodada, que dispõe dos bytes e das imagens verificadas.

Não reabrir ciência, cálculo financeiro ou conteúdo editorial aprovado. Markdown técnico v0.3.0, PDF v0.4.0 e controles anteriores intactos. Nenhuma modificação de preços, contratos, CRM, site, políticas ou campanhas.

## 2. Causa localizada e correção — CNQ-VIS-006-01

No PDF original, página 4, objeto **12 0 obj** (`/Contents`), sete comandos de texto `Tj` contêm o prefixo literal PDF `\22641 ` antes dos marcadores 1 a 7. Em WinAnsi, a sequência octal `\226` corresponde ao travessão curto e é seguida pelos caracteres literais `41`; portanto “–41” já está gravado no conteúdo, não é apenas um artefato do PNG.

O gerador original não está versionado na árvore examinada. Não atribuir uma causa específica de programação sem o código. Foi localizada a **formatação responsável no stream de texto** e criada correção reproduzível [scripts/fix_cnq_checklist_v040.py](../scripts/fix_cnq_checklist_v040.py), com guarda do SHA-256 da fonte e verificação dos sete itens.

Remover somente as sete ocorrências do prefixo; atualizar `/Length`, xref e startxref para manter o PDF válido. Todos os outros objetos permanecem idênticos byte a byte, incluindo fontes, cores, posições, hiperlink e chamada comercial. A extração textual da página 4 corresponde exatamente ao original menos os prefixos. Nos itens 6 e 7, a continuação de linha mantém seu recuo original; não reconstruir o checklist ou mudar seus enunciados.

## 3. Binário, identidade e evidências

- [PDF novo v0.4.1](GT-MKT-CNQ-001-Guia-Executivo-v0.4.1.pdf), **13.631 bytes**, cinco páginas, PDF 1.4.
- SHA-256 novo: `646554cfdba296457af7d0bdc4b50783f2fe44a2841970fce48692a989f5038a`.
- [PDF histórico v0.4.0](GT-MKT-CNQ-001-Guia-Executivo-v0.4.0.pdf), 13.680 bytes; SHA-256 conferido nesta rodada: `7db1aa3b3d3fda0dea907dbe85550d98940bbae9cd05d8b87fc09440d5f66e8b`.
- [Cinco imagens e manifesto](../05-Evidencias/GT-MKT-CNQ-001/v0.4.1/README.md): hashes individuais, método, numeração, regressão, hiperlink e limitações.

O binário novo está disponibilizado junto das projeções por links verificáveis, para que o revisor recompute seu hash. Isso atende à entrega de evidência de CNQ-INTEGRIDADE-006-04 pelo executor, sem presumir que a conferência independente já ocorreu.

## 4. Inspeção e regressão visual

Renderizados os dois PDFs com `pdftoppm` **26.05.0**, `-r 150 -png`; cinco PNGs novos, **1240×1755 px**, examinados individualmente.

| Página | Resultado da inspeção do executor | Comparação com v0.4.0 |
|---|---|---|
| 1 — Abertura | Hierarquia e conteúdo preservados; regressão rápida sem diferença introduzida | PNG idêntico byte a byte |
| 2 — Impacto | Blocos e margens preservados; regressão rápida sem diferença introduzida | PNG idêntico byte a byte |
| 3 — Financeiro | Números, ressalvas e layout preservados; não refeita análise financeira | PNG idêntico byte a byte |
| 4 — Checklist | Sete itens numerados de 1 a 7 sem “–41”; enunciados completos e espaçamento vertical preservado | Única página visualmente alterada |
| 5 — Próximos passos | CTA, fontes, ressalvas e layout preservados; regressão rápida | PNG idêntico byte a byte |

Não afirmar equivalência universal entre renderizadores, aprovação visual independente, legibilidade em dispositivo real ou conformidade assistiva a partir destas imagens. O revisor deve examinar especialmente a página 4 e eventuais diferenças materiais; esta rodada não constitui redesign das páginas restantes.

## 5. Hiperlink e chamada comercial — CNQ-LINK-006-03

Página 5 preserva a chamada “Conheça a GenTests.ai e entre em contato:” e o convite para conversar sobre identificação de riscos, retrabalho e indicadores. Não acrescentar diagnóstico gratuito, preço, economia garantida, formulário de captação ou promessa de ROI. A ressalva de ausência de garantia permanece intacta.

Verificação estrutural com pypdf/PyMuPDF: uma anotação `/Subtype /Link`, ação `/URI`, destino `https://gentests-site.pages.dev/`. Consulta read-only em **10/10/2026 20:17:25 UTC / 17:17:25 America/Sao_Paulo** retornou **HTTP 200**, URL final igual e título “GenTests | Qualidade de software que protege a experiência do cliente”. Isso comprova acesso HTTP naquele instante, não funcionamento do formulário ou disponibilidade futura.

**Limitação herdada encontrada na checagem espacial:** anotação PDF `[40,290,400,330]`; na coordenada superior de PyMuPDF, `[40,512,400,552]`. A caixa do texto da URL é aproximadamente `[44,505.71,189.33,520.14]`. A área anotada intersecta a faixa inferior e contém o centro da URL, mas não cobre toda a altura do texto extraído. Não declarar toda a URL como área clicável perfeita. O retângulo foi preservado nesta solicitação exclusiva de numeração; revisor/direção podem deliberar eventual ajuste focal posterior. Não houve clique em leitor PDF nativo nem envio de formulário. Evidência no manifesto.

## 6. Acessibilidade semântica e alternativa HTML — CNQ-A11Y-006-02

`pdfinfo`: **Tagged: no**. Catalog sem `/StructTreeRoot`, `/MarkInfo` ou `/Lang`; texto extraível em todas as páginas. Ausência de tags/idioma não foi corrigida: fazê-lo adequadamente seria outra intervenção além da numeração, e não bastaria adicionar `/Lang` para tornar o PDF acessível. Sem validação PDF/UA, teste com leitor de tela, navegação de teclado ou ordem lógica assistiva. Fontes Base14 Helvetica/Helvetica-Bold sem incorporação; aparência pode variar conforme visualizador. Não certificar acessibilidade visual ou semântica.

**Avaliação da alternativa HTML (proposta, não implementada nem publicada):** viável e proporcional para leitura responsiva, seleção/refluxo e navegação semântica, desde que derive do texto executivo aprovado, mantendo todos os números/limites. Não substituir aprovação por escolher HTML.

| Componente | Requisito candidato para futura implementação | Validação necessária |
|---|---|---|
| Documento | `lang="pt-BR"`, título, um `h1`, `main`, hierarquia `h2/h3`, link de salto e ordem DOM de leitura | Inspeção de estrutura e leitor de tela |
| Checklist | Lista ordenada nativa `ol/li` de sete itens, sem prefixos decorativos; continuação dentro do mesmo item | Numeração anunciada corretamente e texto íntegro |
| Exemplo financeiro | Tabela nativa com legenda e cabeçalhos `th/scope`, componentes/categorias e ressalvas na mesma sequência | Associação célula/cabeçalho e comparação com texto aprovado |
| Link/CTA | Link nativo descritivo com foco visível e área acionável adequada; mesma URL aprovada | Teclado, leitura assistiva e destino |
| Apresentação | Refluxo, zoom, espaçamento ajustável e contraste verificado; não usar imagens de texto como conteúdo principal | Testes responsivos e critérios WCAG aplicáveis, sem declarar conformidade antes deles |
| Governança | Sem formulário, rastreamento ou coleta adicionados; fonte/versão e revisão independente antes de disponibilização | Aprovação da Direção e gates de privacidade/publicação próprios |

Recomendação: submeter a alternativa HTML semântica como caminho futuro à Direção, com revisão e teste assistivo próprios. **Nenhuma página, política, site ou coleta foi alterada.**

## 7. Devolução focal e responsabilidades

**Executor:** correção numérica concluída, cinco PNGs e hashes disponibilizados, regressão e verificação de link/CTA registradas. Os testes estritos de parsing e comparação não aprovam divulgação.

**Revisor:** recomputar SHA-256 do PDF novo, inspecionar página 4 e regressão das demais; avaliar o residual espacial do link e a limitação semântica sem reabrir ciência/finanças já aprovadas. Encerramento de CNQ-VIS-006-01 depende desse parecer.

**Direção:** eventual ajuste de área clicável, alternativa acessível e decisões de distribuição/captação continuam separadas. Nenhum parecer ou CI autoriza automaticamente publicação.

**PR #4 permanece draft, aberta e sem merge.** Resultado desta execução: **PRONTO PARA REVALIDAÇÃO VISUAL FINAL — SEM AUTORIZAÇÃO PARA DISTRIBUIÇÃO**.
