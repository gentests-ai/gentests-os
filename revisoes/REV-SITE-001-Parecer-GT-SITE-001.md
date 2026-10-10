---
tipo: parecer-revisao-independente
id: REV-SITE-001
versao: 1.0.0
status: parecer-emitido
data: 2026-10-10
revisor: Agente Revisor Independente
artefato: GT-SITE-001
repositorio_site: gentestsai-sudo/gentests-site
pr_site: 1
sha_revisado: 9d524ad783701998070cfb5e85624255f09b7ebe
decisao: APROVADO COM RESSALVAS PARA EVOLUCAO
homologacao_producao: NAO AUTORIZADA
---

# REV-SITE-001 — Parecer independente sobre GT-SITE-001

## 1. Escopo, método e limitações
Revisão estática do diff da PR [gentests-site #1](https://github.com/gentestsai-sudo/gentests-site/pull/1), SHA `9d524ad783701998070cfb5e85624255f09b7ebe`, comparado à base `fe4af7cd49f4d7446feb27519ec4f427e1c2c399`; leitura dos cinco arquivos alterados, das referências do GenTests OS na branch main e da documentação de execução. **Nenhum teste de navegador, envio efetivo, Lighthouse ou varredura dinâmica foi executado pelo revisor.** Ausência de teste não equivale a aprovação.

Regras de Missão/Visão/Valores e QG-001/QG-CORE/QG-STR-001 da governança estão atualmente como **proposta**, e são referências de análise, não políticas homologadas. A decisão comercial `04-Decisoes/Primeiro-PIX-Homologacao-Comercial.md` também está em proposta, sem preço público aprovado. Não houve merge, deploy ou modificação no código do site.

## 2. Resultado geral
**APROVADO COM RESSALVAS PARA EVOLUÇÃO DOCUMENTAL/TÉCNICA. NÃO APROVADO PARA HOMOLOGAÇÃO DE PRODUÇÃO.** O executor tratou prudentemente três riscos de comunicação e registrou bloqueios, mas o fluxo comercial essencial não foi testado e permanecem decisões de privacidade e lançamento pendentes. Não foi confirmada regressão funcional em execução; não se pode excluí-la sem navegador.

## 3. Matriz SITE-001 a SITE-010

| ID | Resultado | Evidência e conclusão | Condição de aceite |
|---|---|---|---|
| SITE-001 | Bloqueio justificado | `index.html`, `solucoes.html`, `contato.html`, `quem-somos.html`, `obrigado.html`: meta noindex,nofollow mantida; README condiciona remoção ao lançamento. | Decisão de lançamento e regressão SEO antes de alterar; não remover nesta PR sem aprovação |
| SITE-002 | Parcial / Alto | `contato.html:96-100`: `_captcha` passou de false a true; `contato.html:188-194` comunica dependência externa. Alteração de atributo **não é evidência de antispam efetivo** ou envio recebido. | Teste autorizado de CAPTCHA mobile/desktop, ativação FormSubmit, recebimento, falha e retenção |
| SITE-003 | Tratado preventivamente; decisão pendente | `solucoes.html`: retirada de “A partir de R$ 690”, substituído por confirmação comercial; `04-Decisoes/Primeiro-PIX-Homologacao-Comercial.md` aponta alternativas R$690/R$890 sem homologação. | Homologação de escopo/preço e revisão de conteúdo antes de anúncio público |
| SITE-004 | Parcial / Médio | `obrigado.html:34`: mensagem atual não garante recebimento, inclusive por acesso direto. **Lacuna nova de UX**: pede contato por e-mail mas não oferece link mailto na área principal. | Implementar CTA de e-mail e teste do redirecionamento após sucesso/falha; não confundir redirect com confirmação de entrega |
| SITE-005 | Bloqueado / Alto | `contato.html` coleta dados pessoais e encaminha ao FormSubmit; aviso não substitui avaliação LGPD. | Informação transparente sobre operador/fornecedor, finalidades, retenção, direitos e eventual transferência; revisão responsável |
| SITE-006 | Não verificável | `index.html` e demais páginas usam símbolo PNG e wordmark textual; assets oficiais referenciados no Drive via `01-Empresa/Identidade-Visual.md`. Sem comparação binária/visual. | Comparação visual, contraste, tamanhos, marca e aprovação |
| SITE-007 | Pendente não bloqueante para evolução; bloqueante ao lançamento | Metadados OG/canonical não foram acrescentados; noindex preservado. | Definir domínio e metadados antes de indexação pública |
| SITE-008 | Pendente / Médio | `solucoes.html` mantém três ofertas; nomes e delimitações não foram conciliados com catálogo homologado. | Decisão documentada de portfólio, capacidades, escopo e claims |
| SITE-009 | Sem novo defeito comprovado | `quem-somos.html` não foi modificado; diferencia pessoa humana e agentes de IA. | Revisão editorial e aprovação institucional de títulos/capacidades |
| SITE-010 | Pendente condicionado ao domínio | `contato.html` mantém `_next=https://gentests-site.pages.dev/obrigado.html`; domínio provisório ainda em uso. | Parametrizar/testar mudança quando houver domínio definitivo |

## 4. Achados adicionais e correções recomendadas
- **REV-SITE-001-A01 — Alto — deficiência de evidências do fluxo comercial.** Não existe teste real de submissão, recebimento, CAPTCHA e erros; não declarar homologado. **Correção obrigatória antes de publicação, não bloqueia esta etapa documental.**
- **REV-SITE-001-A02 — Médio — CTA de fallback incompleto.** `obrigado.html:34` orienta envio por e-mail sem disponibilizar link direto nessa seção; adicionar `mailto:gentests.ai@gmail.com` e revalidar. **Correção recomendada na próxima rodada.**
- **REV-SITE-001-A03 — Médio — inconsistência documental confirmada.** `docs/GT-SITE-001-Tratamento-Auditoria.md:12` afirma que nenhum Quality Gate específico foi localizado. Existem `00-Constituicao/Quality-Gates/QG-001-Politica.md`, `QG-CORE-Obrigatorio.md` e `QG-STR-001-Disciplina-Estrategica.md`. **Corrigir a referência, preservando o status proposta.**
- **REV-SITE-001-A04 — Médio — legenda de confirmação pouco adequada à jornada.** A frase “Confira o status do seu contato” sugere consulta de status, mas não existe status transacional consultável; preferir “Orientações sobre sua solicitação”, com mensagem clara de limitação. **Melhoria editorial não bloqueante da evolução.**
- **REV-SITE-001-A05 — Alto — privacidade ainda não verificada.** Fornecedor externo e coleta de dados requerem avaliação de conformidade antes de produção. Não afirmar ilegalidade ou violação concreta sem avaliação.

## 5. Avaliação das mudanças
- **Preço removido:** apropriado sob incerteza documental. Não homologar preço alternativo por inferência e não declarar que valor anterior era necessariamente errado; sua aprovação não foi demonstrada.
- **CAPTCHA habilitado:** escolha plausível, porém sem prova de benefício líquido; validar bloqueio de spam, acessibilidade, desafio mobile e impacto na conversão.
- **Confirmação revisada:** reduz promessa indevida, porém não oferece recibo; um redirecionamento não confirma entrega à caixa postal. Preferível instrução de contingência clara.
- **Regressões:** nenhuma comprovada em execução; risco de fricção maior no formulário e de desalinhamento comercial na página sem preços.
- **Governança:** sem autoaprovação, mudanças limitadas e decisões pendentes explicitadas. A referência ausente aos QGs exige correção.

## 6. Quality Gates e decisão
Classificação de risco **QG-H como referência proposta**: mudanças relacionadas a captação de dados, comunicação pública e eventual publicação em produção. Evidência estática e rastreabilidade de diff: **atendidas parcialmente**. Validação funcional, privacidade, aprovação comercial/identidade e autorização humana: **pendentes**. Resultado de gate de produção: **não verificável/bloqueado para publicação**.

## 7. Próximo passo objetivo (evitar ciclos indefinidos)
Solicitar ao executor **uma única rodada focalizada** em A02–A04 e ajustes documentais. Validar em preview isolado: desktop/mobile, navegação com teclado, formulário teste autorizado, antispam, redirecionamento e evidência de recebimento; registrar ambiente, passo, resultado esperado/observado e evidência. Direção decide LGPD, domínio, identidade, preços/portfólio e liberação de indexação. Revisor reavalia somente mudanças e testes desta rodada. Não realizar merge ou deploy automático.

## 8. Fontes
- [PR #1 — site](https://github.com/gentestsai-sudo/gentests-site/pull/1)
- [Tratamento](https://github.com/gentestsai-sudo/gentests-site/blob/fix/site-001-auditoria-controlada-20261010/docs/GT-SITE-001-Tratamento-Auditoria.md)
- [Relatório de testes e publicação](https://github.com/gentestsai-sudo/gentests-site/blob/fix/site-001-auditoria-controlada-20261010/docs/GT-SITE-001-Relatorio-Testes-e-Publicacao.md)
- [GenTests OS](https://github.com/gentestsai-sudo/gentests-os)
