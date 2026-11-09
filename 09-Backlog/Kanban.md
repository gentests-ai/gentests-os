---
tipo: kanban
versao: 1.2.2
status: acompanhamento
revisado_em: 2026-11-09
---
# Kanban — GenTests OS

> Quadro de acompanhamento documental. Status reconciliados em 12/10/2026 com a main `15846c547f8e18e8e0c16ec85def5f9b74f1c0f7` e registros GitHub consultados. O GitHub é a fonte oficial; atualização local do Obsidian depende de sincronização comprovada.
>
> “Em andamento” registra avanço parcial comprovado, sem afirmar agente executando neste instante. “Em validação” indica pendência documental, não aceite nem teste em curso. A fazer pode significar implantação não comprovada. Aprovação, implantação e conclusão são distintas.

## Quadro dos cards GOS

| A fazer | Em andamento | Em validação | Aguardando aprovação | Bloqueado | Concluído |
|---|---|---|---|---|---|
| [GOS-006](Cards/GOS-006.md) | [GOS-005](Cards/GOS-005.md) |   | [GOS-003](Cards/GOS-003.md) |   | [GOS-001](Cards/GOS-001.md) |
| [GOS-007](Cards/GOS-007.md) | [GOS-010](Cards/GOS-010.md) |   |   |   | [GOS-002](Cards/GOS-002.md) |
| [GOS-008](Cards/GOS-008.md) | [GOS-011](Cards/GOS-011.md) |   |   |   | [GOS-004](Cards/GOS-004.md) |
|   | [GOS-012](Cards/GOS-012.md) |   |   |   | [GOS-009](Cards/GOS-009.md) |
|   | [GOS-013](Cards/GOS-013.md) |   |   |   | [GOS-017](Cards/GOS-017.md) |

## Estado e próxima ação

| Card | Estado | Evidência/limite | Próximo passo |
|---|---|---|---|
| [GOS-001](Cards/GOS-001.md) | Concluído — escopo v1.1 | Organização inicial preservada; não comprova sincronização do vault local. | Manter histórico; não reabrir por alerta isolado de metadado. |
| [GOS-002](Cards/GOS-002.md) | Concluído — criação e preparação do repositório | Consulta à API em 12/10/2026 confirmou private=true e visibility=private; .gitignore e fluxo de PR existem. Este status não certifica MFA, backup ou segurança completa. | Segurança, tokens e backup continuam nos cards próprios. |
| [GOS-003](Cards/GOS-003.md) | Aguardando aprovação | POL-001 continua proposta; POL-003 v1.2.1 integrada é explicitamente não homologada. | Direção deliberar a homologação aplicável; decisões pontuais não aprovam toda a Constituição. |
| [GOS-004](Cards/GOS-004.md) | Concluído — contextos e contratos homologados | A Direção confirmou alteração, revisão e homologação dos contratos hoje, incluindo autonomia e permissões específicas. Aprovação documental atendida; não equivale a ativação automática ou acesso segregado. | Reconciliar metadados documentais com as versões/decisões já homologadas, sem novo ciclo de aprovação. |
| [GOS-005](Cards/GOS-005.md) | Em andamento — autorização contratual atendida | A Direção confirmou autonomia e permissões nos contratos específicos. Não há nova aprovação contratual pendente neste card. O objetivo original também inclui aplicação técnica dos limites; implantação universal não foi comprovada pela confirmação. | Comprovar aplicação dos controles nas ferramentas no escopo autorizado; preservar limites dos contratos homologados. |
| [GOS-006](Cards/GOS-006.md) | A fazer — implantação não comprovada | Não foi localizada evidência suficiente de cofre configurado, MFA e recuperação testada nas fontes consultadas. Falta de evidência não prova inexistência. | Infra apresentar evidências sem divulgar credenciais. |
| [GOS-007](Cards/GOS-007.md) | A fazer — implantação não comprovada | Não foi localizada comprovação de cofre, rotação e gestão de tokens por serviço. Permissões de um conector não comprovam gestão de credenciais. | Infra verificar gestão no recurso autorizado, sem alterar permissões. |
| [GOS-008](Cards/GOS-008.md) | A fazer — backup não comprovado | Não foi localizada evidência de backup no Drive com restauração testada. Versionamento GitHub não substitui esse critério. | Infra comprovar backup e restauração, ou propor revisão do escopo à Direção. |
| [GOS-009](Cards/GOS-009.md) | Concluído — marca e assinaturas confirmadas pela Direção | A Direção confirmou conclusão das alterações de marca e assinaturas de e-mail. Esse ato corrige a pendência de acompanhamento; não representa teste visual novo desta conversa nem autorização geral de distribuição. | Reconciliar referências dos ativos finais no registro existente, sem reabrir aprovação concluída. |
| [GOS-010](Cards/GOS-010.md) | Em andamento — desenho documental | Contratos, processo de inspeção e registros existem. Inspeção X9 não equivale à auditoria completa dos agentes nem comprova revisão periódica de amostras. | Auditor verificar amostras e cobertura; não duplicar a inspeção X9. |
| [GOS-011](Cards/GOS-011.md) | Em andamento — cobertura parcial | Há checagem de Wikilinks, pré-revisão determinística e testes de guardas. CI aprovado no escopo existente não certifica contratos, políticas ou todos os limites. | QA mapear cobertura faltante dos critérios; reutilizar evidências sem repetir testes antigos. |
| [GOS-012](Cards/GOS-012.md) | Em andamento — desenho de consulta | Fontes e regras de consulta estão documentadas; integração automática e consulta restrita a políticas aprovadas não foram comprovadas ponta a ponta. | Engenharia/Infra comprovar integração autorizada; não confundir consulta manual com agente acionado. |
| [GOS-013](Cards/GOS-013.md) | Em andamento — contrato do Validador homologado | A Direção confirmou homologação do Validador na alteração dos contratos. A homologação contratual está atendida. Implantação completa, classificador QG-L/M/H, bloqueio em fluxo real e auditoria de amostras continuam sem comprovação nesta inspeção; não solicitar novamente homologação do contrato. | Verificar somente critérios técnicos restantes. A confirmação não permite inferir aprovação isolada de toda a política QG-001 ou independência humana. |
| [GOS-017](Cards/GOS-017.md) | Concluído — assinaturas confirmadas pela Direção | A Direção confirmou conclusão das assinaturas de e-mail. O bloqueio de negócio é retirado; o registro de ativos consultado ainda declara original pendente. Trata-se de rastreabilidade documental a reconciliar, não nova aprovação exigida. | Atualizar futuramente o registro existente com os arquivos/versões finais efetivos; não inventar links, hashes ou resultados de renderização. |

## Frentes atuais fora do planejamento inicial GOS

Links para registros existentes, sem criar missões ou cartões duplicados. Não representam inventário completo do portfólio.

| Frente | Estado comprovado na consulta | Registro canônico |
|---|---|---|
| Despacho automático | Missão aberta; preparação integrada e bloqueada; operação ponta a ponta não comprovada | [#47](https://github.com/gentestsai-sudo/gentests-os/issues/47) |
| Configuração sintética | Issue criada; PR #82 Draft aberta, não integrada na consulta | [#81](https://github.com/gentestsai-sudo/gentests-os/issues/81) · [PR #82](https://github.com/gentestsai-sudo/gentests-os/pull/82) |
| Mission Control | Especificação MVP em issue aberta; não representa produto implantado | [#58](https://github.com/gentestsai-sudo/gentests-os/issues/58) |
| Guia Executivo — hiperlink | Bug registrado e issue aberta; resolução não inferida de inspeção documental | [#45](https://github.com/gentestsai-sudo/gentests-os/issues/45) |
| Matriz de permissões | Proposta integrada, não homologada; reconciliação em issue aberta | [#53](https://github.com/gentestsai-sudo/gentests-os/issues/53) |
| Handoffs horizontais / Processos | Correções documentais preparadas; PR #141 aberto, revisão e integração pendentes; contratos de outros domínios encaminhados | [#137](https://github.com/gentests-ai/gentests-os/issues/137) · [PR #141](https://github.com/gentests-ai/gentests-os/pull/141) · [#138 Governança](https://github.com/gentests-ai/gentests-os/issues/138) · [#139 Engenharia](https://github.com/gentests-ai/gentests-os/issues/139) · [#140 Infraestrutura](https://github.com/gentests-ai/gentests-os/issues/140) |
| Quality Intelligence | Discovery v0.2 e plano técnico documentados; implementação não inferida | [[produtos/GT-QI-001/GT-QI-001-Discovery-Produto-v0.2]] · [[produtos/GT-QI-001/GT-QI-ENG-POC-01-Plano-Tecnico]] |

## Histórico e manutenção

A v1.1 usava “Agora / Próxima / Depois” como ordem de prioridade; isso não demonstrava execução. As fases originais dos cards foram preservadas como histórico, sem repriorização nesta atualização. GOS-001 permanece concluído no escopo original; GOS-002 registra somente criação/preparação do repositório privado. GOS-004, GOS-009 e GOS-017 foram concluídos pela confirmação expressa da Direção, registrada abaixo. Os demais não foram concluídos por mera existência de documentos.

Responsáveis originais permanecem nos cards. Próximos passos são pendências, não despachos enviados ou aceitos. Atualizar card e quadro juntos quando nova evidência mudar o estado. Critérios existentes sem comprovação permanecem desmarcados. Esta atualização não homologa políticas ou contratos, não concede acesso e não autoriza merge.

**Inspeção:** conversa consultiva Agile Coach, solicitada pela Direção; não representa ativação de novo agente canônico. **Acompanhamento de fluxo:** Scrum Master por exceção, diante de impedimentos, atrasos, falhas ou conflitos. Responsáveis dos cards mantêm ownership e encaminham diretamente aos especialistas competentes; não existe coordenação central obrigatória.

[[INICIO|Centro de comando]] · [[CHANGELOG|Histórico do vault]]

## Correção após confirmação da Direção

[Declaração registrada na PR #83](https://github.com/gentestsai-sudo/gentests-os/pull/83#issuecomment-6120555144): contratos revisados e homologados em 12/10/2026, autonomia/permissões nos contratos específicos, marca e assinaturas concluídas e Validador homologado. Não pedir novamente essas aprovações. GOS-005/GOS-013 permanecem parciais somente pelos objetivos técnicos adicionais, não pela homologação dos contratos. GOS-003 preserva pendência distinta de aprovação global da Constituição; não inferir homologação de POL-001/QG-001 por analogia.

Na consulta de 12/10/2026, contrato do Validador e registro de ativos na main ainda continham textos antigos. A declaração da Direção é registrada com sua proveniência; metadados e referências finais precisam de reconciliação documental sem reabrir aprovação. Não inventar versões, arquivos, hashes ou testes. PR #83 teve merge confirmado pela API, realizado pela Direção conforme informado nesta conversa; esta correção posterior requer integração separada.
