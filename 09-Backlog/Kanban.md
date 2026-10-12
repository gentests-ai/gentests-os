---
tipo: kanban
versao: 1.2.0
status: acompanhamento
revisado_em: 2026-10-12
---
# Kanban — GenTests OS

> Quadro de acompanhamento documental. Status reconciliados em 12/10/2026 com a main `15846c547f8e18e8e0c16ec85def5f9b74f1c0f7` e registros GitHub consultados. O GitHub é a fonte oficial; atualização local do Obsidian depende de sincronização comprovada.
>
> “Em andamento” registra avanço parcial comprovado, sem afirmar agente executando neste instante. “Em validação” indica pendência documental, não aceite nem teste em curso. A fazer pode significar implantação não comprovada. Aprovação, implantação e conclusão são distintas.

## Quadro dos cards GOS

| A fazer | Em andamento | Em validação | Aguardando aprovação | Bloqueado | Concluído |
|---|---|---|---|---|---|
| [GOS-006](Cards/GOS-006.md) | [GOS-005](Cards/GOS-005.md) | [GOS-004](Cards/GOS-004.md) | [GOS-003](Cards/GOS-003.md) | [GOS-017](Cards/GOS-017.md) | [GOS-001](Cards/GOS-001.md) |
| [GOS-007](Cards/GOS-007.md) | [GOS-010](Cards/GOS-010.md) | [GOS-009](Cards/GOS-009.md) |   |   | [GOS-002](Cards/GOS-002.md) |
| [GOS-008](Cards/GOS-008.md) | [GOS-011](Cards/GOS-011.md) |   |   |   |   |
|   | [GOS-012](Cards/GOS-012.md) |   |   |   |   |
|   | [GOS-013](Cards/GOS-013.md) |   |   |   |   |

## Estado e próxima ação

| Card | Estado | Evidência/limite | Próximo passo |
|---|---|---|---|
| [GOS-001](Cards/GOS-001.md) | Concluído — escopo v1.1 | Organização inicial preservada; não comprova sincronização do vault local. | Manter histórico; não reabrir por alerta isolado de metadado. |
| [GOS-002](Cards/GOS-002.md) | Concluído — criação e preparação do repositório | Consulta à API em 12/10/2026 confirmou private=true e visibility=private; .gitignore e fluxo de PR existem. Este status não certifica MFA, backup ou segurança completa. | Segurança, tokens e backup continuam nos cards próprios. |
| [GOS-003](Cards/GOS-003.md) | Aguardando aprovação | POL-001 continua proposta; POL-003 v1.2.1 integrada é explicitamente não homologada. | Direção deliberar a homologação aplicável; decisões pontuais não aprovam toda a Constituição. |
| [GOS-004](Cards/GOS-004.md) | Em validação documental | Diretório, arquitetura e contratos já foram definidos como propostas. Homologação e capacidade operacional não estão comprovadas. | Governança consolidar validação dos papéis; Direção decidir aprovação quando aplicável. |
| [GOS-005](Cards/GOS-005.md) | Em andamento — preparação parcial | POL-003 e guardas do piloto existem; #47 registra preparação bloqueada. Não há prova de implantação universal dos limites nas ferramentas. | Engenharia/Infra comprovar controles apenas no ambiente e escopo autorizados. |
| [GOS-006](Cards/GOS-006.md) | A fazer — implantação não comprovada | Não foi localizada evidência suficiente de cofre configurado, MFA e recuperação testada nas fontes consultadas. Falta de evidência não prova inexistência. | Infra apresentar evidências sem divulgar credenciais. |
| [GOS-007](Cards/GOS-007.md) | A fazer — implantação não comprovada | Não foi localizada comprovação de cofre, rotação e gestão de tokens por serviço. Permissões de um conector não comprovam gestão de credenciais. | Infra verificar gestão no recurso autorizado, sem alterar permissões. |
| [GOS-008](Cards/GOS-008.md) | A fazer — backup não comprovado | Não foi localizada evidência de backup no Drive com restauração testada. Versionamento GitHub não substitui esse critério. | Infra comprovar backup e restauração, ou propor revisão do escopo à Direção. |
| [GOS-009](Cards/GOS-009.md) | Em validação — pendências de marca | Existe atividade formal de verificação de identidade; o registro de ativos ainda deixa a segunda assinatura pendente. Não foi comprovada validação integral nos templates e campanhas. | Marketing consolidar evidências do escopo; Direção decide marca/publicação. |
| [GOS-010](Cards/GOS-010.md) | Em andamento — desenho documental | Contratos, processo de inspeção e registros existem. Inspeção X9 não equivale à auditoria completa dos agentes nem comprova revisão periódica de amostras. | Auditor verificar amostras e cobertura; não duplicar a inspeção X9. |
| [GOS-011](Cards/GOS-011.md) | Em andamento — cobertura parcial | Há checagem de Wikilinks, pré-revisão determinística e testes de guardas. CI aprovado no escopo existente não certifica contratos, políticas ou todos os limites. | QA mapear cobertura faltante dos critérios; reutilizar evidências sem repetir testes antigos. |
| [GOS-012](Cards/GOS-012.md) | Em andamento — desenho de consulta | Fontes e regras de consulta estão documentadas; integração automática e consulta restrita a políticas aprovadas não foram comprovadas ponta a ponta. | Engenharia/Infra comprovar integração autorizada; não confundir consulta manual com agente acionado. |
| [GOS-013](Cards/GOS-013.md) | Em andamento — protótipo parcial | Existe pré-revisão determinística e testes locais definidos. Contrato continua proposta; classificador completo, bloqueio em fluxo real e auditoria de amostras não foram comprovados. Mesma identidade entre agentes não representa independência humana. | Validador/QA verificar critérios restantes no escopo autorizado; Direção decidir homologação. |
| [GOS-017](Cards/GOS-017.md) | Bloqueado — original da segunda assinatura pendente | Registro de ativos e #38 mantêm a segunda assinatura sem arquivo canônico identificado. Não reconstruir nem substituir o ativo por inferência. | Marketing obter o original e confirmar finalidade com a Direção antes dos testes. |

## Frentes atuais fora do planejamento inicial GOS

Links para registros existentes, sem criar missões ou cartões duplicados. Não representam inventário completo do portfólio.

| Frente | Estado comprovado na consulta | Registro canônico |
|---|---|---|
| Despacho automático | Missão aberta; preparação integrada e bloqueada; operação ponta a ponta não comprovada | [#47](https://github.com/gentestsai-sudo/gentests-os/issues/47) |
| Configuração sintética | Issue criada; PR #82 Draft aberta, não integrada na consulta | [#81](https://github.com/gentestsai-sudo/gentests-os/issues/81) · [PR #82](https://github.com/gentestsai-sudo/gentests-os/pull/82) |
| Mission Control | Especificação MVP em issue aberta; não representa produto implantado | [#58](https://github.com/gentestsai-sudo/gentests-os/issues/58) |
| Guia Executivo — hiperlink | Bug registrado e issue aberta; resolução não inferida de inspeção documental | [#45](https://github.com/gentestsai-sudo/gentests-os/issues/45) |
| Matriz de permissões | Proposta integrada, não homologada; reconciliação em issue aberta | [#53](https://github.com/gentestsai-sudo/gentests-os/issues/53) |
| Quality Intelligence | Discovery v0.2 e plano técnico documentados; implementação não inferida | [[produtos/GT-QI-001/GT-QI-001-Discovery-Produto-v0.2]] · [[produtos/GT-QI-001/GT-QI-ENG-POC-01-Plano-Tecnico]] |

## Histórico e manutenção

A v1.1 usava “Agora / Próxima / Depois” como ordem de prioridade; isso não demonstrava execução. As fases originais dos cards foram preservadas como histórico, sem repriorização nesta atualização. GOS-001 permanece concluído no escopo original; GOS-002 registra somente criação/preparação do repositório privado. Os demais não foram concluídos por mera existência de documentos.

Responsáveis originais permanecem nos cards. Próximos passos são pendências, não despachos enviados ou aceitos. Atualizar card e quadro juntos quando nova evidência mudar o estado. Critérios existentes sem comprovação permanecem desmarcados. Esta atualização não homologa políticas ou contratos, não concede acesso e não autoriza merge.

**Inspeção:** conversa consultiva Agile Coach, solicitada pela Direção; não representa ativação de novo agente canônico. **Responsável pela coordenação futura:** Orquestrador Central, após encaminhamento e aceite comprovados.

[[INICIO|Centro de comando]] · [[CHANGELOG|Histórico do vault]]
