---
id: REV-MKT-CNQ-003
tipo: parecer-revisao-independente
versao: 0.1.0
status: emitido
resultado: aprovado-com-ressalvas-documentais
publicacao: bloqueada
data: 2026-10-10
revisor: ChatGPT-GPT-6
pr: 4
commit_revisado: 14d4fbf6bc7e48dfd6a070419de3a3cecd2cab43
documento_blob: bfe8d423eb1344911e3777be369f7a6ffc09ae45
tratamento_blob: 2ef454033f69169cb6fe7483e80532756a045a81
pdf_blob: 690fd6935257852c9fbf3e4402678508b991a731
parecer_anterior: REV-MKT-CNQ-002
---
# REV-MKT-CNQ-003 — Parecer de fechamento GT-MKT-CNQ-001 v0.3.0

**Decisão:** APROVADO COM RESSALVAS quanto ao **conteúdo técnico e documental**; **NÃO AUTORIZADO PARA PUBLICAÇÃO**. Restou um gate específico de inspeção visual/acessibilidade do PDF, além da autorização da Direção. O documento principal não exige outra revisão integral se apenas o PDF for alterado sem mudar alegações, números ou texto técnico.

## Escopo fechado e evidências

- PR #4 (draft): https://github.com/gentestsai-sudo/gentests-os/pull/4, branch `review/custo-nao-qualidade-v0-1`, commit `14d4fbf6bc7e48dfd6a070419de3a3cecd2cab43`.
- Fonte: `comercial/GT-MKT-CNQ-001-Custo-da-Nao-Qualidade.md` v0.3.0 (blob `bfe8d423eb1344911e3777be369f7a6ffc09ae45`); tratamento `comercial/GT-MKT-CNQ-003-Tratamento-REV-MKT-CNQ-002.md` (blob `2ef454033f69169cb6fe7483e80532756a045a81`).
- PDF presente: `comercial/GT-MKT-CNQ-001-Custo-da-Nao-Qualidade-v0.3.0.pdf`, blob `690fd6935257852c9fbf3e4402678508b991a731`. O executor informa 7776 bytes, 3 páginas e SHA-256 `eea18583b8c5e4d58a2f4a44f16915ee5d04f31d6c375c5e4e0473ab99cba213`. A leitura pelo conector GitHub confirmou o arquivo e sua identidade por blob, mas **o SHA-256 declarado e a renderização de páginas não foram verificados independentemente nesta sessão**. A estrutura PDF visível contém três objetos Page, fonte Type1 Helvetica, textos e avisos. Ausência de estrutura /StructTreeRoot e de marcadores de conteúdo acessível indica que não se demonstrou PDF marcado; o executor igualmente declara ausência de conformidade PDF/UA.
- O PDF é um **resumo de 3 páginas**, não a totalidade da fonte Markdown: esta distinção é aceitável quando comunicada, e foi declarada no tratamento.
- Parecer anterior REV-MKT-CNQ-002 e proposta GT-GOV-QG-ENC-001 consultados como referências; a última ainda não é política vigente. Preservada separação de execução/revisão/Direção.

## Matriz de revalidação

| ID | Resultado | Severidade residual | Evidência | Risco/ação |
|---|---|---|---|---|
| CNQ-01/CNQ32-01 | **Resolvido** | Baixo | GT-MKT-CNQ-001 §§2.1–2.2; tratamento §matriz | Quatro rubricas segregadas: recursos R$2.260 + externo R$600 + ajuste receita R$900 + oportunidade R$1.000 = R$4.760; não há alegação de caixa R$1.500. Exigir caso real, reconciliação e contabilidade antes de apresentar resultado de cliente. |
| CNQ-03/CNQ32-02 | **Resolvido** | Baixo | Documento §§4.1–4.2 | Coortes de releases implantadas, maturação D+30, duplicidade/reabertura, mínimos candidatos 95%/90%/90%, denominadores fixos, N/A e fatores de confusão. Piloto é requisito de aplicação real, não bloqueia conteúdo educacional. |
| CNQ-04 | **Parcialmente resolvido** | **Alto somente para pacote público/visual** | PR #4 inclui PDF blob identificado; tratamento CNQ-04 | Binário acessível; falta comprovar SHA-256 independente, renderização de 3 páginas, contraste, corte, leitura em celular/desktop, ordem assistiva/semântica; PDF não é marcado/PDF-UA. Providenciar evidências e, se a peça for oferecida como acessível, corrigir estrutura e submeter teste assistivo. Não reabrir Markdown inteiro. |
| CNQ-05 | **Resolvido tecnicamente** | Decisão da Direção pendente | Documento §§5–6, status proposta; PDF p.3 | CTA exploratório, sem preço/campanha ou promessa; PR #3 permanece em proposta. Autorização de publicação independente do aceite técnico. |
| CNQ-02 | **Sem regressão / resolvido** | Baixo | Documento §1, F1–F3 | CISQ EUA 2022 fluxo anual US$2,41 tri, dívida estoque US$1,52 tri; NIST 2002 cenário potencial; Boehm/Basili multiplicador contextual. Não expandir claims. |
| CNQ-06 | **Sem regressão / resolvido** | Baixo | Documento §3, PDF p.2 | 1/3/6 × R$2.260/R$4.760/R$7.260 conferem; 3×R$4760×12=R$171360 condicional. |
| CNQ-07 | **Sem regressão textual / resolvido em conteúdo** | Validação visual dependente CNQ-04 | Resumo executivo e §5; PDF p.1 | Mensagens CTO, engenharia, finanças e cautelas preservadas. Inspeção visual separada. |
| CNQ-08 | **Resolvido** | Baixo | Front matter, tratamento, PR draft | Versão 0.3, parecer anterior, status proposta e publicação bloqueada. PR body ainda menciona v0.1/PDF ausente: atualização de metadados recomendada sem reabrir entrega. |

## Revisão financeira e científica

12×120+6×90+4×70=R$2.260; +600+900+1000=R$4.760. O total é **impacto econômico gerencial hipotético e condicionado**, não fluxo de caixa nem receita comprovadamente perdida. As chaves `incident_id`, `transaction_id` e `ledger_entry_id` permitem conciliação e descarte de sobreposição, sujeitas a acesso autorizado e minimização. Cenários de sensibilidade conferidos: R$2.260/4.760/7.260 para 1; ×3 = R$6.780/14.280/21.780; ×6 = R$13.560/28.560/43.560; 12 meses×3×R$4.760 = R$171.360. Não demonstram ROI.

Fundamentação científica preservada com referências primárias CISQ 2022, NIST/RTI 2002 e Boehm/Basili 2001, seus limites geográficos, cronológicos e metodológicos. Não usar as cifras como benchmark do Brasil.

## PDF — limite de inspeção

**Confirmado:** presença no diff de PR #4, conteúdo PDF legível pelo conector, 3 referências a Page, exemplos e advertências equivalentes em essência ao Markdown, Helvetica usada em corpo e títulos, ausência aparente de tags estruturais e reconhecimento do executor de que não é PDF/UA. **Não confirmado por teste efetivo:** SHA-256 byte a byte independente, visualização de todas páginas, renderização em diferentes telas, contrate perceptível, ausência de cortes, ordem de leitura assistiva, conformidade PDF/UA. Não alegar teste realizado. A exclusão de detalhes bibliográficos e protocolo é inerente a um resumo; acrescentar ligação rastreável ao estudo completo se for divulgado.

**Critério de fechamento do gate CNQ-04:** (1) baixar binário versionado e comparar SHA-256 publicado; (2) renderizar as 3 páginas e inspecionar cortes, hierarquia, margens e contraste; (3) teste de leitura em largura de tela móvel/desktop, texto extraível, links e idioma; (4) avaliar acesso por tecnologia assistiva e corrigir marcação se exigido para a distribuição pretendida; (5) arquivar evidência e emitir *atestado de fechamento apenas desse gate*. Não exigir quarta auditoria científica, financeira ou editorial se estas fontes não sofrerem alterações.

## Decisão e encaminhamento

**Nenhum impedimento técnico substancial remanescente no Markdown.** Um impedimento de evidência/verificação visual e acessibilidade afeta a distribuição do PDF; a aprovação expressa da Direção permanece necessária. O texto científico/financeiro pode ser considerado tecnicamente concluído em escopo interno, sem transformar proposta em política ou conteúdo liberado.

Solicitar ao executor apenas pacote de evidências e eventual correção de acessibilidade do PDF; atualização descritiva da PR é baixa prioridade. Encerrar em seguida o gate visual por revisão focada; não fazer nova revisão geral por melhorias opcionais. Nenhum merge, publicação ou alteração dos arquivos do executor foi realizado neste parecer.
