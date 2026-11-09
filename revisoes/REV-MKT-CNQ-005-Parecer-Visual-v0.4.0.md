---
id: REV-MKT-CNQ-005
tipo: parecer-independente-focal
versao: 1.0.0
status: parecer-emitido-com-limitacao
data: 2026-10-10
pr_execucao: 4
commit_revisado: d87fdfb46a5467067fa7cb53ccbdcffe1341f270
artefato: comercial/GT-MKT-CNQ-001-Guia-Executivo-v0.4.0.pdf
resultado: NAO-APROVADO-PARA-DISTRIBUICAO-POR-FALTA-DE-INSPECAO-VISUAL
---
# REV-MKT-CNQ-005 — Parecer focal do guia executivo v0.4.0

## Resumo
**NÃO APROVADO PARA DISTRIBUIÇÃO NO ESTADO DE EVIDÊNCIAS DISPONÍVEL.** Não se comprova defeito visual; falta a inspeção visual obrigatória das cinco páginas. Esta restrição impede parecer favorável sobre layout, recortes, contraste, tipografia e legibilidade. Preservam-se as conclusões técnico-financeiras anteriores no que não há delta material demonstrado.

## Identificação e método
Repositório gentestsai-sudo/gentests-os, [PR #4](https://github.com/gentestsai-sudo/gentests-os/pull/4), SHA `d87fdfb46a5467067fa7cb53ccbdcffe1341f270`. Arquivo localizado no commit: `comercial/GT-MKT-CNQ-001-Guia-Executivo-v0.4.0.pdf` (13.680 bytes no Git; blob `68c0dcbb6102f2a3de561f11d83776f9862c1897`). PDF obtido pelo conector GitHub em conteúdo base64, mas **transporte para ambiente local de renderização não concluído**. Não foi gerado painel de imagens e não houve inspeção visual de qualquer página nesta rodada. **SHA-256: NÃO CALCULADO INDEPENDENTEMENTE.** O hash Git do blob não substitui SHA-256.

Consultados: `comercial/GT-MKT-CNQ-001-Custo-da-Nao-Qualidade.md` v0.3.0 (fonte preservada), `comercial/GT-MKT-CNQ-004-Tratamento-REV-MKT-CNQ-004.md`, PR #13. O próprio relatório do Executor informa explicitamente falta de renderização e inspeção visual. Não tratar checagens estruturais como aprovação estética.

## Matriz de inspeção obrigatória — evidência efetivamente disponível
| Página | Renderizada | Inspeção visual | Sobreposição/cortes/margens/legibilidade | Resultado |
|---|---|---|---|---|
| 1 | Não | Não | Não verificáveis | **NÃO VERIFICADO** |
| 2 | Não | Não | Não verificáveis | **NÃO VERIFICADO** |
| 3 | Não | Não | Não verificáveis | **NÃO VERIFICADO** |
| 4 | Não | Não | Não verificáveis | **NÃO VERIFICADO** |
| 5 | Não | Não | Não verificáveis | **NÃO VERIFICADO** |

Não afirmar que há sobreposição nem que não há. Inspeção de página individual e leitura mobile/desktop são gates ainda abertos.

## Avaliação de conteúdo e editorial
A fonte científica/financeira anterior mantém referência a CISQ/NIST/Boehm-Basili, distingue hipóteses de observações e separa impacto econômico gerencial de caixa/contabilidade; o cenário R$4.760 contém R$2.260 de horas, R$600 de serviço, R$900 de ajuste de receita e R$1.000 de oportunidade distinta. Não se apurou nova regressão material no Markdown preservado. O tratamento do Executor afirma guia executivo de cinco páginas com checklist de sete passos, CTA e link; **a apresentação desses elementos no PDF não foi confirmada visualmente**. Não certificar eficácia do título, tamanho aparente, espaçamento, sobreposição, links clicáveis ou jornada de leitura sem inspecionar o arquivo.

## Acessibilidade
**Não verificada.** O Executor informa ausência de estrutura PDF marcada e nenhuma certificação PDF/UA. Devem ser examinados tags/ordem, idioma, contraste, texto selecionável, tamanho real, links e leitura assistiva. Uma versão HTML semântica e acessível pode ser alternativa proporcional, mas não prova que este PDF seja acessível nem dispensa revisão visual do PDF caso distribuído.

## Severidades e critérios de saída
- **MKT-VIS-005-01 / Alto (bloqueio de evidência):** renderização e inspeção das cinco páginas não realizadas. Gerar PNGs individualizados a partir do binário exato, registrar dimensões, hash SHA-256 independente e matriz de revisão por página; conferir desktop/celular. Qualquer texto sobreposto prejudicando leitura, elemento cortado ou card incompleto reprova visualmente.
- **MKT-A11Y-005-02 / Médio (não verificável):** falta auditoria de acessibilidade estrutural/experiência. Testar idioma, tags/ordem de leitura, contraste/legibilidade e alternativa HTML, conforme recursos.
- **MKT-DOC-005-03 / Baixo:** o relatório do Executor já registra ausência de SHA-256; acrescentar hash e método na evidência de entrega.

Não há evidência para declarar novos defeitos visuais reais. Não exigir reescrita das análises científicas e financeiras anteriormente aprovadas sem regressão material comprovada.

## Próximo passo focal
Executor deve **somente completar evidência bloqueante**, sem alterar preços, contratos, site, CRM ou conteúdo técnico por presunção: anexar PDF exato, SHA-256 calculado, cinco renders PNG e inspeção visual com recortes/contraste, ou fornecer o arquivo por canal montável ao revisor. Se houver defeito, corrigir na fonte e gerar versão/hash/evidências novos. Revisor então emite complemento focal sobre visual, links e acessibilidade; não repetir a auditoria integral. Direção decide publicação e ativação de leads separadamente da revisão técnica.

**Restrições preservadas:** sem merge, campanha, coleta, publicação, modificação dos documentos do Executor ou autorização institucional.
