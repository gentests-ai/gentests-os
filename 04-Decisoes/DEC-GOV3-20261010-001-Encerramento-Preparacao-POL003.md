---
id: DEC-GOV3-20261010-001
tipo: registro-de-deliberacao-direcao
versao: 1.0.0
status: decisao-expressa-delimitada
data: 2026-10-10
decisor: Direcao-GenTests.ai
origem: manifestacao-expressa-da-direcao-no-chat
objeto: GT-GOV-003-GT-GOV-004
aprovacao_nove_politicas: nao
autorizacao_merge: nao
autorizacao_implementacao: nao
---
# DEC-GOV3-20261010-001 — Deliberação sobre preparação documental da governança mínima

## Manifestação da Direção

> "Aceito o encerramento da preparação documental e autorizo preparar uma versão revisada de POL-003, sem homologar automaticamente as nove políticas. Quanto ao GT-GOV-004: manter apenas como backlog, sem execução técnica. Registre esta decisão de forma rastreável e preserve aprovações e merges como atos distintos."

**Fonte primária:** manifestação expressa da Direção da GenTests.ai nesta conversa em 10/10/2026. O texto acima preserva o conteúdo da autorização comunicada; este registro Git é a transcrição documental para rastreabilidade, sem alegar assinatura eletrônica ou autenticação fora desta conversa.

## Escopo preciso e consequências

| Objeto | Decisão | Efeito permitido | Efeito não autorizado |
|---|---|---|---|
| GT-GOV-003, preparação da governança mínima, PR #12, commit `ce6fe14c8fc8c3842d75239fdbd4fb4a690d29b1` | **Aceito o encerramento da preparação documental** | Classificar a *fase de preparação* como encerrada, registrar REV-GOV-003 e encaminhar próxima frente | Não homologar automaticamente POL-001/002/003/004, QG-001/CORE/STR, SEC-AI-001 ou GOV-5S-001 |
| POL-003 v1.0.0, `00-Constituicao/Matriz-de-Permissoes.md` | **Autorizada a preparação de versão revisada** | Elaborar em branch/PR próprios proposta que explicite Orquestrador, Executor e Revisor, com segregação e sem autoaprovação; revisão independente proporcional | Não considerar POL-003 vigente/revisada/aprovada, não alterar permissões de sistemas, não executar a proposta, não conceder autonomia |
| GT-GOV-004, plano de controles pós-homologação, PR #12 | **Somente backlog** | Preservar CT-01–CT-12 como planejamento e pendências | Não autorizar inspeções ativas, testes de segurança, configuração de GitHub, workflows, IAM, backup ou alterações técnicas |
| PRs #12, #14, #15 e futuras propostas | **Sem decisão de merge** | Manter histórico, pareceres e revisão independente | Não executar merge, publicação ou mudança de status institucional por decorrência desta autorização |

## Evidências documentais

- [GT-GOV-003/004 — PR #12](https://github.com/gentestsai-sudo/gentests-os/pull/12), commit examinado `ce6fe14c8fc8c3842d75239fdbd4fb4a690d29b1`.
- [REV-GOV-003 — PR #14](https://github.com/gentestsai-sudo/gentests-os/pull/14), parecer `revisoes/REV-GOV-003-Parecer-Homologacao-Minima.md`, commit `11efd4f6aca4971ac5bca69cba094855aef44f7e`.
- [REV-GOV-003 — PR #15](https://github.com/gentestsai-sudo/gentests-os/pull/15), parecer `revisoes/REV-GOV-003-Parecer-Homologacao-Governanca-Minima.md`, commit `9f31ee607c70235817b03f572d7aea6a8adbd1bb`. Ambos pareceres possuem o mesmo ID `REV-GOV-003` em arquivos distintos; divergência **documental** a reconciliar sem apagar registros ou presumir segunda homologação.
- Histórico anterior: [REV-GOV-001 #7](https://github.com/gentestsai-sudo/gentests-os/pull/7), [REV-GOV-002 #10](https://github.com/gentestsai-sudo/gentests-os/pull/10).

## Próximos passos sem autorização implícita

1. **Executor designado:** elaborar texto candidato da POL-003 em PR próprio, preservando POL-003 v1.0.0 até aprovação; distinguir poderes de coordenar, executar, revisar, auditar e autorizar.
2. **Revisor independente:** revisar somente delta do texto proposto e riscos de conflito/permissão; não substituir deliberação da Direção.
3. **Direção:** deliberar expressamente sobre cada política por ID/versão/escopo/vigência e, separadamente, sobre eventual merge e implementação técnica.
4. **Orquestrador:** acompanhar os trabalhos e reconciliar os IDs duplicados dos dois pareceres REV-GOV-003 sem reabrir auditoria ampla. A duplicidade `PRC-COM-001` permanece backlog documental posterior.
5. **GT-GOV-004:** permanece inativo, sem executor técnico autorizado nesta deliberação.

**Nota de status:** o registro desta decisão em branch/PR documental não altera a `main` nem a vigência das normas. Encerrar a fase de preparação é diferente de homologar a Constituição.
