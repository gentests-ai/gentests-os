---
id: REV-MKT-CNQ-004
tipo: parecer-independente-focal-comercial
versao: 0.1.0
status: emitido
resultado: conteudo-tecnico-apto-pdf-lead-magnet-nao-apto
data: 2026-10-10
pr_origem: 4
commit_revisado: 14d4fbf6bc7e48dfd6a070419de3a3cecd2cab43
documento_blob: bfe8d423eb1344911e3777be369f7a6ffc09ae45
pdf_blob: 690fd6935257852c9fbf3e4402678508b991a731
aprovacao_direcao: pendente
publicacao: bloqueada
---
# REV-MKT-CNQ-004 — Fechamento focal para material educativo de captação orgânica

**Decisão: CONTEÚDO TÉCNICO APTO; PDF ATUAL NÃO APTO COMO LEAD MAGNET PÚBLICO.** Há **dois bloqueios materiais concentrados na peça comercial**: apresentação interna não convertida em artefato de público externo; ausência de proposta de valor/CTA acionável e garantia de acessibilidade visual. Correção focada, sem nova auditoria dos cálculos. Aprovação editorial posterior não autoriza coleta de e-mails, publicação, merge ou anúncio.

## Contexto e limites
PR #4 em Draft, head `14d4fbf6bc7e48dfd6a070419de3a3cecd2cab43`. Inspecionados Markdown principal GT-MKT-CNQ-001 v0.3.0, GT-MKT-CNQ-003 (tratamento) e a presença/estrutura/textos do PDF, blob `690fd6935257852c9fbf3e4402678508b991a731`. As evidências históricas REV-MKT-CNQ-002 e REV-MKT-CNQ-003 sustentam a revisão técnica anterior. Conector GitHub permitiu ler bytes do PDF (7776 bytes; 3 páginas A4, fonte Helvetica Type1 em tamanhos 9, 11, 18 pt, **sem `/StructTreeRoot`, `/Annots` ou `/URI`**). Nesta sessão **não foi possível renderizar visualmente o PDF** em desktop/móvel nem verificar independentemente SHA-256: não alegar aprovação de contraste, corte, ordem assistiva ou integridade criptográfica. Textos do PDF inspecionados por seus comandos textuais, não por imagem renderizada.

## Matriz MKT
| ID | Resultado | Evidência | Consequência |
|---|---|---|---|
| MKT-01 Qualidade técnica | **Conforme** | Markdown resumo, §§1,4; PDF páginas 1 e 3 | Conceitos preventivos e custo do retrabalho pertinentes; estudos históricos com ressalvas. |
| MKT-02 Financeiro | **Conforme** | Markdown §§2–3; PDF página 2 | 1440+540+280+600+900+1000=4760; total gerencial hipotético distinto de caixa; 3×4760×12=171360 condicional. Não é economia comprovada ou auditoria contábil. |
| MKT-03 Editorial/comercial | **Parcial / bloqueante à peça pública** | PDF p.1–3 e Markdown §5 | Texto do PDF ainda repete 'NÃO PUBLICAR', 'estudo interno', parecer/PR e aprovações pendentes. São avisos corretos em revisão, mas material deve ter **versão de distribuição própria**, após autorização, com linguagem ao leitor B2B e sem resíduos de processo interno. |
| MKT-04 Visual e acessibilidade | **Não verificável integralmente / bloqueante à peça pública** | PDF blob e fontes 9/11/18 pt, A4; não há tags estruturais ou links | Precisa renderização das 3 páginas e inspeção mobile/desktop, contraste, margens, corte, acentuação e teste básico assistivo. Corpo de 11pt e rodapé de 9pt podem comprometer leitura em telefone; sem afirmar reprovação de contraste sem imagem. |
| MKT-05 Lead magnet | **Parcial / bloqueante à finalidade** | PDF 3 páginas e texto da página 3; Markdown §5 possui CTA interno, mas PDF não contém CTA direto ou link clicável | Resumo fornece contexto e um exemplo, porém pouca utilidade prática exclusiva frente ao pedido de e-mail. Recomenda-se **um único checklist/planilha conceitual rápida** 'Como estimar o custo de 1 incidente', com campos preenchíveis no leitor ou roteiro concreto, e CTA claro para conversar; não inventar promessa de ROI ou serviço grátis. |
| MKT-06 Conformidade | **Conforme internamente / publicação pendente** | Front matter `status: proposta` e `publicacao: bloqueada`, PDF p.3 | Não há casos reais inventados/preços/ofertas homologadas; autorização da Direção e consentimento/privacidade da captura são gates específicos futuros. |

## Achados históricos
- CNQ-01/CNQ32-01, CNQ-03/CNQ32-02, CNQ-02, CNQ-06, CNQ-07 e CNQ-08: **sem regressão material identificada** no conteúdo, conforme delimitação dos pareceres anteriores.
- CNQ-04: **permanece parcial**: PDF existe no GitHub; renderização/legibilidade/acessibilidade ainda não verificadas visualmente; binário não marcado. Não solicitar auditoria contábil/tributária, nem auditoria científica completa.
- CNQ-05: governança/comercial continua dependente da Direção, sem campanha aprovada.

## Correções mínimas bloqueantes para a peça de distribuição
1. **PDF externo distinto do interno:** produzir versão orientada a CTO/liderança sem cabeçalhos de 'material interno', avisos de revisão, IDs de parecer e PR; manter internamente aviso de não publicar até aprovação e conservar exemplos hipotéticos, contexto científico e ressalvas de causalidade.
2. **Valor para o e-mail e CTA:** incluir micro-checklist de diagnóstico/autodiagnóstico de um incidente (horas por equipe, despesas incrementais, créditos, margens distintas, riscos de dupla contagem); CTA único, concreto e não enganoso, sujeito a validação da Direção; preferencialmente link verificável para página institucional, não prometer diagnóstico gratuito.
3. **Visual e acessibilidade:** disponibilizar render das 3 páginas ou PDF externo revisado; verificar legibilidade no celular, acentos, fonte, margens, contraste, links e leitura assistiva. Se disponibilizado a público geral, prover alternativa HTML/texto acessível ou PDF marcado adequadamente; não declarar PDF/UA sem prova.
4. **Rastreabilidade:** versão pública derivada da v0.3.0, registrar SHA-256, commit e correspondência de números/claims; validação focada somente do novo PDF.

## Melhorias opcionais (não bloquear)
- Renomear título para uma pergunta centrada na dor: 'Quanto custa um incidente de software para sua operação?'.
- Adicionar exemplo visual gráfico/tabela simples em vez de longos parágrafos.
- Atualizar descrição da PR #4, que ainda afirma equivocadamente que o PDF não foi versionado.
- Em etapa posterior de captura: formulário com consentimento informado, finalidade e privacidade, armazenando no CRM existente e sem campo excessivo; a auditoria da landing page pertence à PR do site e não a este documento.

## Critério final de encerramento
O Markdown v0.3.0 **não requer outra revisão técnica completa**. A **preparação comercial para captação de leads permanece bloqueada** até uma correção de saída do PDF: versão externa profissional/legível, benefício acionável e CTA correto, seguida de revisão focal visual. A Dir. deverá aprovar publicação separadamente, e captura de dados pessoais exige sua própria validação/autorização. Não há implementação nem ações externas neste parecer.
