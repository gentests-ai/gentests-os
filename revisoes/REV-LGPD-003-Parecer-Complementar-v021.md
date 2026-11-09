---
id: REV-LGPD-003
tipo: parecer-complementar-independente
versao: 1.0.0
status: parecer-emitido
data: 2026-10-10
escopo: GT-LGPD-001-v0.2.1
pr_execucao: 16
sha_revisado: a5267ac594074bc1fc1d2c0e13b8815f78b36403
decisao_origem: DEC-LGPD-20261010-001
resultado: APTO-PARA-ENCERRAMENTO-DOCUMENTAL-COM-RESSALVA-EDITORIAL
publicacao_autorizada: nao
---
# REV-LGPD-003 — Revalidação focal do delta GT-LGPD-001 v0.2.1

## Resumo executivo
**APTO PARA ENCERRAMENTO DOCUMENTAL COM RESSALVA EDITORIAL, sujeito à Direção.** O delta de v0.2.1 respeita a [DEC-LGPD-20261010-001, PR #21](https://github.com/gentestsai-sudo/gentests-os/pull/21): entrega do material GT-MKT-CNQ-001 prioritariamente por **e-mail mínimo**, finalidade de marketing opcional, independente, desmarcada e revogável. Não se constatou regressão alta ou crítica no escopo documental inspecionado. Não existe autorização de implementação, coleta, testes reais, campanha, publicação ou merge.

Método: confronto de `revisoes/GT-LGPD-001-Diagnostico-Privacidade.md`, `GT-LGPD-002-Politica-Privacidade-Proposta.md`, `GT-LGPD-003-Controles-Operacionais.md` e `GT-LGPD-004-Requisitos-Captacao-Leads.md`, todos v0.2.1 no SHA `a5267ac594074bc1fc1d2c0e13b8815f78b36403`, com a decisão no SHA `a8d4abc6c0e4f213f2d7f1ac0dbc211688cc4710`, PRs [#18](https://github.com/gentestsai-sudo/gentests-os/pull/18) e [#20](https://github.com/gentestsai-sudo/gentests-os/pull/20). Revisão somente da alteração arquitetural: não reabre o exame completo v0.2.0.

## LGPD-REV-01 a LGPD-REV-07

| ID | Situação focal | Evidência | Pendência fora do aceite documental |
|---|---|---|---|
| LGPD-REV-01 | **Resolvido documentalmente, preservado** | GT-LGPD-001 §§8/11 preserva checklist controlador, canal, fornecedores, países e transferência | Comprovação de identidade jurídica e papéis |
| LGPD-REV-02 | **Resolvido documentalmente** | GT-LGPD-001 §§9/11 distingue bases **candidatas** para entrega, marketing e contato; GT-LGPD-004 §8 separa finalidades | Parecer jurídico, decisão da Direção por finalidade |
| LGPD-REV-03 | **Resolvido documentalmente, preservado** | GT-LGPD-003 §7 mantém cenários de prazo ANPD/pessoa de pequeno porte | Elegibilidade real e aplicação legal |
| LGPD-REV-04 | **Resolvido documentalmente, preservado** | GT-LGPD-004 §6 mantém especificações de ajuste do site/formulário e §8 descreve nova landing page | Implantação futura com autorização e teste |
| LGPD-REV-05 | **Resolvido documentalmente** | GT-LGPD-003 §§8–9 distingue fila de entrega, Gmail, CRM, preferências, supressão e backups, com descarte e prova pendentes | Prazos, capacidade real de eliminação e revisão jurídica |
| LGPD-REV-06 | **Resolvido documentalmente, com ressalva editorial não bloqueante** | GT-LGPD-004 §§7–8 compara os modelos e dá precedência ao e-mail; download direto limitado a contingência | Uniformizar referência histórica à preferência por download direto nas seções antigas |
| LGPD-REV-07 | **Resolvido documentalmente, preservado** | Referências da ANPD e comunicação de incidentes mantidas em GT-LGPD-003 §7 | Conferir vigência antes da operação |

Os 7/7 já haviam sido resolvidos documentalmente no REV-LGPD-002; o delta não introduz novo impedimento ao encerramento desse alcance.

## Testes de consistência da decisão e da jornada
- **Decisão/limite:** GT-LGPD-004 §8 e GT-LGPD-001 §11 citam a DEC-LGPD-20261010-001 e preservam explicitamente as proibições de implantação/coleta/publicação/merge.
- **Solicitação e minimização:** e-mail obrigatório apenas para envio do material; campos adicionais exigem justificativa; aviso contextual antes da coleta.
- **Separação de finalidades:** material entregue mesmo sem opção promocional; marketing com opção distinta, desmarcada e revogável; não criar lead de campanha a partir de um pedido isolado do PDF.
- **Preferências/erros/retenção:** GT-LGPD-003 §9 especifica prova mínima da escolha, retirada/supressão, tratamento de cópias e backups, falha de entrega e descarte; não inventa prazo ou garantia do fornecedor. `enviado` não significa entregue/aberto/lido.
- **Bases legais:** candidatas e condicionadas a necessidade, enquadramento e aprovação jurídica. Não presumir consentimento para marketing pela entrega.
- **Terceiros:** controlador, operadores, FormSubmit/Gmail/Cloudflare/Sheets, subprocessadores, países e eventuais mecanismos de transferência são tópicos de verificação, não fatos homologados.
- **LP-01 a LP-12:** GT-LGPD-004 §8.2 mantém doze cenários **sintéticos futuros**; LP-02/03 condicionados à oferta de marketing e LP-11 ao inventário real; não há execução alegada.
- **Contingência:** download direto permanece alternativa, não arquitetura prioritária.

## Ressalva editorial específica
**REV-LGPD-003-R01 / Baixa, não bloqueante:** GT-LGPD-004 §1 ainda traz “Alternativa preferencial de menor risco” para o download direto; §5 conserva `DEC-LP-01` como escolha aparentemente pendente, e GT-LGPD-001 §6 contém códigos DEC-LGPD-02/04 históricos que podem ser confundidos com a decisão atual DEC-LGPD-20261010-001. O §8 de GT-LGPD-004 e §11 de GT-LGPD-001 corrigem expressamente a precedência. Recomenda-se consolidar referências históricas e evitar reutilização ambígua de códigos **em próxima manutenção**, sem reabrir o diagnóstico nem alterar documentos nesta revisão.

Não há demonstração de defeito operacional: a landing page e o fluxo não foram implementados nesta atividade. Não transformar a ressalva em nova aprovação jurídica obrigatória.

## Pendências jurídicas/institucionais e encaminhamento
Direção e jurídico deverão definir controlador, canal para titulares e eventual enquadramento de pequeno porte; bases legais por finalidade; prestadores, contratos, papel, transferência internacional e mecanismo quando aplicável; retenção, supressão, exclusão e responsáveis; proteção de dados e evidências de erro/abuso. Em seguida caberão autorizações **específicas e distintas** para implementar, testar com dados sintéticos e publicar, com parecer independente posterior.

**Recomendação:** Orquestrador pode registrar **encerramento documental focal v0.2.1** e encaminhar as pendências à Direção sem nova auditoria integral. O parecer não homologa política de privacidade, base jurídica ou controle técnico, não permite lista de leads, envio, merge ou publicação. PR #16 permanece sob autorização de merge separada.

Referências: [Execução PR #16](https://github.com/gentestsai-sudo/gentests-os/pull/16); [Parecer PR #18](https://github.com/gentestsai-sudo/gentests-os/pull/18); [Revalidação v0.2.0 PR #20](https://github.com/gentestsai-sudo/gentests-os/pull/20); [Direção PR #21](https://github.com/gentestsai-sudo/gentests-os/pull/21).
