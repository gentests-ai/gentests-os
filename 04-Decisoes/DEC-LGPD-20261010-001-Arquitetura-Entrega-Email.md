---
id: DEC-LGPD-20261010-001
tipo: registro-de-decisao-direcao
versao: 1.0.0
status: direcionamento-documental-autorizado
data: 2026-10-10
decisor: Direcao-GenTests.ai
origem: manifestacao-expressa-da-direcao-no-chat
objeto: GT-LGPD-001-DEC-LGPD-02
captacao_autorizada: nao
implementacao_autorizada: nao
publicacao_autorizada: nao
merge_autorizado: nao
---
# DEC-LGPD-20261010-001 — Priorização documental de entrega de material por e-mail

## Manifestação expressa da Direção

> "Como Direção da GenTests.ai, para a atividade GT-LGPD-001, determino que seja priorizada a arquitetura de entrega do material por e-mail com coleta mínima e finalidade de marketing separada. Esta decisão é apenas de direcionamento documental, não autoriza publicação, coleta ou implementação. Registre a decisão e os próximos encaminhamentos."

**Origem:** decisão fornecida pela Direção na conversa de 10/10/2026. Este arquivo é o registro versionado da manifestação, não assinatura externa nem prova de controles implementados.

## Decisão e limites

- **DEC-LGPD-02 — direcionamento documental definido:** priorizar o desenho da entrega do PDF educativo GT-MKT-CNQ-001 por e-mail, com dados mínimos necessários à entrega, preferencialmente apenas endereço de e-mail.
- **Finalidade de entrega ≠ finalidade promocional.** Planejar transparência para o envio solicitado e um opt-in de marketing **independente, opcional, não pré-marcado**, com registro de preferência e forma de oposição/revogação. O envio do guia não pode depender do aceite a marketing.
- Não definir por presunção a base legal de entrega, marketing ou prospecção: conservar candidatas e justificativa para validação jurídica e decisão específica. Não presumir que o e-mail coletado para entregar o guia esteja autorizado para campanhas.
- Download direto permanece **alternativa de contingência**, sem adoção automática nem substituição da prioridade determinada; pode ser avaliado se houver impedimento material da arquitetura de e-mail.
- **Fora da autorização:** implementação, formulários, captação de e-mails, envio real, edição/deploy de site, criação de listas no CRM, integração com fornecedores, processamento de dados de titulares, publicação de política, mudança de credenciais, contratação, gastos ou merge.

## Referências documentais

- [PR #16 — GT-LGPD-001 a GT-LGPD-004](https://github.com/gentestsai-sudo/gentests-os/pull/16), parecer analisou commit `48993e09b04e554f0724640f5b0265d8dcd71883`.
- [PR #18 — REV-LGPD-001](https://github.com/gentestsai-sudo/gentests-os/pull/18), parecer `revisoes/REV-LGPD-001-Parecer-Independente-Privacidade.md`, commit `e75bcdade4f7f69eb17ba29560459e28a3e365c9`.
- Material comercial: GT-MKT-CNQ-001 na PR #4; revisão e publicação são etapas independentes.
- POL-004, SEC-AI-001 e pacote GT-GOV-003: status normativos não homologados automaticamente por esta decisão.

## Encaminhamentos autorizados exclusivamente como documentação

1. **Executor 1, PR #16:** incorporar esta decisão no tratamento focal LGPD-REV-01 a 07, com foco na alternativa de e-mail, sem alterar o site. Modelar jornada: solicitação explícita → aviso contextual → captura mínima → entrega → exclusão/retenção conforme regra a deliberar; marketing é escolha separada.
2. Elaborar matriz finalidade/operação/dados/base legal *candidata*, incluindo prova, opt-in/opt-out, supressão, retenção, erros de entrega, abuso e exclusão; registrar validações jurídicas necessárias.
3. Fazer checklist factual, sem preencher dados não conhecidos: controlador e canal, fornecedores, papéis, subprocessadores, países, transferências internacionais, mecanismos aplicáveis e condições reais. Tratar FormSubmit, Gmail, Cloudflare, Google Sheets apenas conforme uso efetivo comprovável.
4. Manter os LP-01 a LP-12 como testes sintéticos **propostos**, com cobertura de fluxo de entrega sem marketing, aceite promocional opcional, retirada da preferência, falhas e dados inesperados; **nenhuma execução autorizada** por esta decisão.
5. **Revisor independente:** posteriormente validar somente o delta documental e riscos materiais, sem autorizar operação.
6. **Direção:** decidir em atos futuros controlador/canal, bases legais por fluxo, fornecedores/transferências, prazo de retenção e responsáveis, orçamento se houver, e somente depois autorizações específicas de implementação, testes técnicos, publicação, coleta e merge.

**Estado de governança:** direcionamento de arquitetura documental **decidido**; conformidade operacional, homologação jurídica e publicação **pendentes**. Preservar PRs #16/#18 sem merge.
