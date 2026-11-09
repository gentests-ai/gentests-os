---
id: GT-GOV-004
tipo: plano-de-controles-pos-homologacao
versao: 0.1.0
status: proposta
data: 2026-10-10
implementacao_autorizada: nao
---
# GT-GOV-004 — Plano de Controles e Pendências Pós-Homologação

> **Checklist de evidências futuras, não declaração de controles instalados.** Complementa GT-GOV-003; nenhuma permissão, workflow, política ou sistema foi alterado. Fonte: GT-GOV-001/002 PR #6; REV-GOV-001 PR #7; REV-GOV-002 PR #10. Não reabrir auditoria histórica encerrada.

## 1. Legenda e regras
Estados: **verificado** = evidência técnica concreta, datada e replicável do controle real; **não verificado** = configurações ou testes não inspecionados; **pendente de implementação** = diferença técnica confirmada por prova, com decisão/planejamento autorizado. Não usar 'pendente de implementação' para inferir ausência sem acesso. Um arquivo de workflow existente prova existência do arquivo, não eficácia da proteção. Atualmente os controles administrativos abaixo estão **não verificados** nesta atividade; são propostas de checagem futura. Não anexar secrets, dados de cliente ou capturas com tokens.

## 2. Matriz enxuta de verificação técnica futura

| ID/prioridade | Controle e situação atual | Dono candidato | Evidência positiva, negativa e critério de aceite | Dependência |
|---|---|---|---|---|
| CT-01 P0 | Branch protection/rulesets: **não verificado** | Infra + revisor independente | export/captura com repo, branch, data, proteção contra force push/bypass; ensaio autorizado de bloqueio de push direto | DEC-GOV3-07; POL-003 |
| CT-02 P0 | Merge e revisores obrigatórios: **não verificado** | Infra + Governança | regra real de revisores distintos, status checks requeridos, impedimento de self-approval; teste negativo de PR sem revisão e positivo autorizado | QG-001, SEC-AI-001; aprovação para teste |
| CT-03 P0 | Agentes/conectores/permissões: **não verificado** | Infra + Auditor | inventário por identidade/conta/ferramenta, escopo efetivo, expiração; tentativa de ação fora do escopo é negada; sem autoelevação | POL-003 e decisão da Direção |
| CT-04 P0 | Tokens/segredos/menor privilégio: **não verificado** | Infra + responsável segurança | permissões efetivas, segredo em mecanismo adequado, rotação e revogação comprovadas por registro sanitarizado; leitura restrita, write negado quando não autorizado | POL-004, SEC-AI-001 |
| CT-05 P0 | Workflows/Actions/runners: **não verificado** | Infra + QA/Auditor | revisão dos gatilhos, `pull_request_target`, pinagem de dependências, permissões mínimas de `GITHUB_TOKEN`, isolamento de runner, tratamento de PR não confiável, sem secrets; ensaios autorizados | CT-01–04; PR técnico distinto |
| CT-06 P1 | Registro de operações e trilha de decisões: **não verificado operacionalmente** | Governança + Auditor | evento com ator, ação, objeto, data, SHA, autorização e resultado real; amostra cruzada com GitHub; evento não autorizado = incidente | GOV-01, SEC-AI-001 |
| CT-07 P1 | Backup e recuperação Git/Obsidian/Drive/CRM: **não verificado** | Infra + donos dos sistemas | inventário de fontes, política de retenção, backup autorizado e restauração testada de amostra sintética, com RPO/RTO a decidir | DEC-GOV3-06; ownership |
| CT-08 P0 | Exposição de dados, logs e incidentes: **não verificado** | Segurança + Infra | classificação e acesso, retenção/descarte aprovados, inspeção de log sem segredo, simulação controlada de triagem e revogação | POL-004, SEC-AI-001 |
| CT-09 P1 | Integridade CRM Sheets e referência Git/Drive: **não verificado** | Comercial + Governance | ID único, dono, acesso, detecção de duplicata e reconciliação manual documentada; nunca pressupor sincronismo | DEC-GOV3-06/08 |
| CT-10 P1 | Alias PRC-COM-001: **pendente de decisão documental; sem implementação** | Governança | Direção aprova ID/alias; PR posterior atualiza somente ID proposto e backlinks com revisão, sem apagar histórico | DEC-GOV3-08 |
| CT-11 P1 | Gate de encerramento e regressão de revisão: **não verificado operacionalmente** | Orquestrador + Auditor | amostra de entrega com aceite, parecer proporcional, decisão efetiva e fechamento; sem homologação por checkbox nem auditoria duplicada | DEC-GOV3-04/07 |
| CT-12 P2 | Amostragem complementar de contratos/anexos: **não verificado fora do escopo** | Auditor | amostra baseada em risco de documentos/ativos vinculados a ação real; registrar escopo e limitações | GOV-13 |

**Nota:** referências a "pendente" nos documentos históricos não demonstram que controles técnicos estejam ausentes. Evidência de negativa deve usar teste seguro, com autorização e sem risco a operação.

## 3. Ordem de execução pós-decisão (não autorizada agora)

**Lote A — Deliberação normativa:** Direção resolve GT-GOV-003 P0, incluindo POL-003; a versão exata aprovada e exceções são registradas no sistema canônico. Não mudar YAML antes da decisão.

**Lote B — Inventário técnico de maior risco:** Infra coleta provas CT-01–05/08; Auditor verifica separação e testabilidade. Lacuna confirmada vira plano técnico próprio, sem concessão automática de acesso.

**Lote C — Continuidade e integridade:** CT-06/07/09/10/11; definir dono de cada fonte, política de backup e critérios de restauração. Renomeação/alias em PR distinto com preservação de referências.

**Lote D — Aperfeiçoamentos posteriores:** CT-12, integração futura, CI/Evals, qualidade funcional do site, comercial e precificação em fluxos próprios. Nenhuma dependência não relacionada deve bloquear homologação exclusivamente documental; ações sensíveis permanecem impedidas sem controle e autorização.

## 4. Critérios de aceite por controle

Toda verificação futura registra `control_id`, política/versionamento associado, fonte (URL/identificador seguro), owner, data, método, configuração observada, resultado positivo/negativo, lacuna, decisão e revisor distinto. Evidência privada com acesso mínimo e retenção aprovada; nunca copiar segredo para o repositório. Classificar cada componente como verificado/não verificado/pendente de implementação **somente com prova**. Desvio crítico suspende atividade afetada imediatamente, com registro e escalonamento à Direção. Para remover bloqueio: correção autorizada, nova evidência e parecer proporcional.

## 5. Limites de trabalho e antirredundância

- Reusar registro de decisões, gestão de RNC, PR, parecer e checklist já existentes; não criar segundo framework ou agente.
- Máximo de duas correções automáticas malsucedidas antes de escalar, conforme SEC-AI-001 ainda em proposta.
- O diagnóstico GT-GOV-001 v0.2 foi apto a encerramento documental no REV-GOV-002; não exigir reinspeção integral.
- Este plano não bloqueia a decisão sobre política em si, mas **não autoriza operações sensíveis**, publicação, compra, contrato, merge ou implantação sem decisão humana e efetividade pertinente.
- Não implementar automação de Evals nesta atividade.

## 6. Aprovações e pendências
A Direção deve decidir homologação de políticas, papel e limites de autonomia, sistema canônico, orçamentos/cronograma de checagens e autorização de cada inspeção que implique teste de segurança. Campos: `decisor`, `data`, `objeto/versao`, `escopo`, `decisao`, `comprovante` — todos **PENDENTES**. Auditor independente deve realizar revisão focal do GT-GOV-003/004 e verificar classificação sem converter proposta em implementação.
