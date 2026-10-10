---
id: GT-MKT-CNQ-003
tipo: tratamento-parecer
versao: 0.3.0
status: proposta
parecer_origem: REV-MKT-CNQ-002
aprovacao_direcao: pendente
publicacao: bloqueada
---
# GT-MKT-CNQ-003 — Tratamento de REV-MKT-CNQ-002

**NÃO PUBLICAR.** Nenhum achado encerrado unilateralmente. Parecer da branch `review/parecer-cnq-002` preservado. PR #4 em draft.

| Achado | Correção | Evidência (arquivo/seção) | Resultado/pendência |
|---|---|---|---|
| CNQ-01 / CNQ32-01 (alto) | Separados horas imputadas (R$2.260), serviço externo (R$600), ajuste de receita (R$900) e oportunidade (R$1.000). Total econômico hipotético R$4.760; caixa **indeterminado**. Não mais declarar R$1.500 como caixa. Chaves e deduplicação especificadas. | GT-MKT-CNQ-001 v0.3, §2.1–2.2 | Aritmética 2.260+600+900+1.000=4.760 verificada. Necessária revisão contábil sobre evento real antes de uso. |
| CNQ-03 / CNQ32-02 (médio) | Coortes de releases, maturação D+30 candidata, 95%/90%/90% limiares candidatos, regras de reabertura/duplicação e denominadores constantes. | GT-MKT-CNQ-001 v0.3, §4.1–4.2 | Regra reproduzível, mas faltam piloto real, controle e revisão independente. |
| CNQ-04 (alto) | PDF de 3 páginas com resumo executivo e exemplo, registrado na PR e recuperado novamente do GitHub para conferir bytes PDF. | `comercial/GT-MKT-CNQ-001-Custo-da-Nao-Qualidade-v0.3.0.pdf`, commit `e6263dd3f64b93007504683641e199fbefe520bc`, blob `690fd6935257852c9fbf3e4402678508b991a731`, SHA-256 `eea18583b8c5e4d58a2f4a44f16915ee5d04f31d6c375c5e4e0473ab99cba213`, 7776 bytes, 3 páginas | **PENDENTE:** renderização de todas as páginas e inspeção visual independente em celular/desktop; PDF usa texto extraível básico, mas **não é PDF/UA nem PDF marcado** e não passou avaliação assistiva. Não declarar achado resolvido. PDF é **resumo executivo** do Markdown, não reprodução integral. |
| CNQ-05 (médio) | Mantidas ressalvas de governança, CTA condicionado, PR #3 em proposta, sem preço/oferta/resultado garantido. | GT-MKT-CNQ-001 v0.3 §§5–6, PDF p.3 | Direção ainda deve decidir e homologar eventual campanha. |
| CNQ-02 (preservado) | Bibliografia CISQ/NIST/Boehm e limites históricos mantidos | GT-MKT-CNQ-001 §1 | A verificar não regressão pelo revisor |
| CNQ-06 (preservado) | Cenários 1/3/6 e R$2.260/R$4.760/R$7.260 mantidos, anualização condicional | GT-MKT-CNQ-001 §3; PDF p.2 | Conjunto hipotético; coluna alta não é previsão |
| CNQ-07 (preservado) | Mensagens CTO/engenharia/finanças e CTA neutro | GT-MKT-CNQ-001 resumo e §5; PDF p.1 | Acessibilidade e eficácia comercial ainda não validadas |
| CNQ-08 (preservado) | Versão 0.3, status proposta, bloqueios e referências | Front matter e este tratamento | Sem merge e sem publicação |

## Quality Gates realizados
- [x] Leitura integral de REV-MKT-CNQ-002; parecer do revisor não alterado.
- [x] Soma do exemplo: 1440+540+280+600+900+1000 = 4760.
- [x] Consistência da sensibilidade: 1/3/6 × 2260/4760/7260, e 3×4760×12=171360.
- [x] Conferido no GitHub o PDF efetivo: assinatura PDF-1.4, final %%EOF, 3 objetos Page, tamanho e SHA-256 sobre bytes obtidos novamente.
- [ ] Renderização e inspeção por página em celular/desktop.
- [ ] Conformidade de acessibilidade PDF: tagging, ordem semântica, contraste em dispositivo, validação assistiva.
- [ ] Revisão independente da versão v0.3 e validação contábil de dados reais.
- [ ] Aprovação expressa Direção.

**Manifesto PDF:** exportação autônoma de **resumo executivo de 3 páginas** elaborado com o mesmo exemplo numérico e premissas do Markdown v0.3. O documento Markdown é a fonte integral de evidências. PDF **não reproduz** bibliografia, todas as tabelas ou protocolo na íntegra; ambas as versões têm mesma tese, advertências e exemplos. Fonte PDF sem gráficos/imagens externas.

**Quality Gate final: BLOQUEADO para divulgação**. Documento apto somente a revisão de conteúdo; CNQ-04 ainda possui impedimentos de verificação visual e acessibilidade.