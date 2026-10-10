---
id: GT-MKT-CNQ-004
tipo: tratamento-parecer-focal
versao: 0.4.0
status: proposta
parecer_origem: REV-MKT-CNQ-004
aprovacao_direcao: pendente
publicacao: bloqueada
---
# Tratamento focal do REV-MKT-CNQ-004

**Documento interno de controle. PDF público CANDIDATO, NÃO APROVADO PARA DISTRIBUIÇÃO.** Nenhum parecer independente alterado, sem merge, campanhas, coleta de leads ou site modificado.

| Achado | Tratamento | Evidência | Validação e pendência |
|---|---|---|---|
| MKT-03 | Redigido guia executivo para leitor B2B, sem referências internas nem marcações de revisão na peça candidata; mantido aviso no documento interno | `comercial/GT-MKT-CNQ-001-Guia-Executivo-v0.4.0.pdf`, págs. 1–5 | Busca estrutural de strings internas não encontrou `NÃO PUBLICAR`, PR ou REV. Revisão editorial independente pendente |
| MKT-04 | PDF de cinco páginas, identidade tipográfica neutra **não declarada oficial** (nenhum logo inventado), blocos e números destacados, fonte base Helvetica; corpo ~10,5 pt e títulos 29–30 pt | PDF v0.4.0, commit `33dffceb2bed7c2e0a02af22b2514a48b77fd9c1`, blob Git `68c0dcbb6102f2a3de561f11d83776f9862c1897` | PDF recuperado pelo GitHub e confirmado header %PDF-1.4, 5 páginas, trailer EOF. **Renderização visual, contraste real, inspeção mobile/desktop e leitura assistiva não realizados** por indisponibilidade de transporte do PDF para ambiente gráfico. PDF não marcado, sem conformidade PDF/UA comprovada. SHA-256 do arquivo ainda precisa de verificação independente. |
| MKT-05 | Checklist de sete etapas e CTA explícito com endereço institucional existente; exemplos e limites financeiros preservados | PDF v0.4.0 págs. 3–5. URI clicável `https://gentests-site.pages.dev/` presente | Verificar clicabilidade espacial, legibilidade e utilidade em revalidação focal |

## Não regressão intencional
Texto integral científico e financeiro do Markdown `GT-MKT-CNQ-001` v0.3.0 preservado. O PDF é peça executiva derivada, não reprodução integral. Cenário R$4.760 com R$2.260 de recursos, R$600 terceiro, R$900 ajuste de receita, R$1.000 oportunidade; não classifica soma como caixa nem promete resultado. Fontes CISQ/NIST/Boehm-Basili enunciadas no PDF, bibliografia completa mantida no Markdown. PDF anterior v0.3.0 preservado no Git.

## Quality gates de execução
- [x] PDF efetivamente versionado no mesmo PR.
- [x] Integridade básica do arquivo validada por leitura de bytes do GitHub: 13680 bytes, 5 páginas, estrutura PDF-1.4 / EOF.
- [x] Presença de CTA e hyperlink URI no PDF.
- [x] Preservação do Markdown v0.3.0 e dos pareceres.
- [ ] SHA-256 do binário verificável registrado.
- [ ] Renderização PNG de todas as páginas anexada e revisada.
- [ ] Inspeção humana visual mobile/desktop, acentuação, margens e contraste.
- [ ] Validação de acessibilidade: tags estruturais, idioma, ordem de leitura, leitor de tela; ou disponibilização futura de alternativa HTML acessível.
- [ ] Revalidação focal independente e aprovação expressa da Direção.

**Situação de fechamento: entrega documental parcial.** Não atribuir resolução de MKT-04 nem pronto para divulgação até evidências visuais e de acessibilidade completas. Nenhuma publicação autorizada.
