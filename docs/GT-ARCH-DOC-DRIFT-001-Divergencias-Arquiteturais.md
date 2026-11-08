---
tipo: auditoria-documental
id: GT-ARCH-DOC-DRIFT-001
versao: 0.1.0
status: pendente-de-reconciliacao
responsavel: Governanca
data: 2026-11-08
---

# GT-ARCH-DOC-DRIFT-001 — Divergências documentais de arquitetura

> Inventário inicial de conflitos encontrados ao comparar a decisão atual da Direção com a documentação da main. Não altera políticas aprovadas nem autoriza implementação. Usar como roteiro de reconciliação e auditoria.

## Decisão atual a preservar

- Não existe orquestrador central.
- Agentes especializados encaminham tarefas diretamente entre si.
- Scrum Master atua por exceção: detecta, tenta resolver impedimentos operacionais, encaminha ao especialista e escala à Direção quando necessário.
- Tech Lead é especialista técnico responsável por review, robustez, conflitos e preparação/execução de merge conforme autoridade vigente.
- Agentes podem executar tarefas diferentes simultaneamente.
- 14 agentes atuais são configuração inicial; quantidade e hierarquia devem ser configuráveis.

## Divergências identificadas

| Fonte | Texto/risco encontrado | Tratamento necessário |
|---|---|---|
| [GT-HANDOFF-001](../03-Processos/Encaminhamento-de-Missoes-GT-HANDOFF-001.md) | Seção 1 mantém “Orquestrador Central único” com ownership global, apesar de seção anterior descrever handoff direto como proposta. | Reconciliar a proposta com decisão horizontal; remover ownership global e definir ownership por tarefa/execução, com remetente/destinatário e Scrum Master por exceção. |
| [GT-HANDOFF-001](../03-Processos/Encaminhamento-de-Missoes-GT-HANDOFF-001.md) | Tabela de papéis, estados e transições ainda atribui triagem, fila, aceite/fechamento ao Orquestrador. | Reescrever estados e transições sem agente central; preservar entrega, recebimento, aceite, execução e conclusão como eventos distintos. |
| [GT-HANDOFF-001 Template](../07-Templates/GT-HANDOFF-001-TEMPLATE.md) | Há adaptação proposta para handoff direto, mas referências a ORQ ainda podem permanecer. | Revisar template para registro de agente de origem/destino, evidência, aceite e próxima ação, sem confirmação central rotineira. |
| [Matriz de Permissões / POL-003](../00-Constituicao/Matriz-de-Permissoes.md) | Há linha de responsabilidade “Planejar e distribuir — Orquestrador Central”. | Não editar como simples documentação: requer decisão normativa da Direção e revisão de Governança. Substituir por autonomia horizontal e atuação de Scrum Master por exceção, se aprovado. |
| [GT-EXEC-001](GT-EXEC-001-Continuidade-Execucao.md) | Usa “Orquestração consulta estado real...” como papel transversal. | Ajustar para acompanhamento operacional do Scrum Master e responsabilidade dos agentes por suas próprias tarefas/handoffs. |
| [GT47-AUTOMATIC-DEMAND-OUTCOME](GT47-AUTOMATIC-DEMAND-OUTCOME.md) | Catálogo descreve “14 papéis” e inclui Orquestrador como papel atual. | Atualizar catálogo para Scrum Master, registrar Tech Lead como proposto e não contar como ativo até ativação comprovada. |
| [Entrega Técnica e Infraestrutura](../03-Processos/Entrega-Tecnica-e-Infraestrutura.md) | Texto de reconciliação ainda diz que Orquestrador mantém fila/rota. | Atualizar interface técnica para comunicação horizontal e Scrum Master por exceção, preservando os limites de Engenharia/Infra. |
| [Arquitetura de Papéis](../02-Agentes/Arquitetura-de-Papeis.md) | A proposta já descreve Scrum Master sem roteamento obrigatório, mas ainda preserva termos históricos e decisões antigas no histórico. | Manter histórico; atualizar somente seções operacionais vigentes e sinalizar claramente o que é histórico/supersedido. |

## Conflito de autoridade — Tech Lead e merge

A responsabilidade pretendida para o Tech Lead inclui review, resolução de conflitos e merge. A POL-003 consultada reserva atualmente à Direção a autorização de merge em PRs.

A reconciliação exige:
1. decisão expressa da Direção sobre delegação ou manutenção da autorização;
2. segregação entre autoria, review técnico, QA/validação e autorização;
3. branch protection e permissões técnicas coerentes;
4. critérios objetivos para bloqueio e merge;
5. trilha de auditoria e Evals.

Até a decisão, o contrato AGT-TL permanece proposta e não concede permissão de merge.

## Fonte de verdade e banco operacional

O GitHub é a fonte canônica do conhecimento versionado: documentos, contratos, decisões, issues, PRs e evidências. Não assumir que ele é o banco transacional do runtime. Claims, leases, heartbeats, fencing e isolamento multi-tenant exigem persistência e operações atômicas adequadas; a escolha tecnológica permanece pendente de investigação.

## Ordem recomendada de reconciliação

1. Confirmar com a Direção a versão vigente da arquitetura e o status das políticas.
2. Governança reconciliar POL-003 e textos normativos que ainda nomeiam Orquestrador como responsável por distribuição.
3. Processos reconciliar GT-HANDOFF-001 e seu template.
4. Atualizar GT-EXEC-001, catálogo da Missão 47 e processo técnico.
5. Atualizar links, índices, aliases históricos e changelog.
6. Executar verificação de links, consistência de metadados e busca residual por termos operacionais antigos.
7. Solicitar revisão independente e registrar decisão final.

## Critérios de encerramento

- Nenhum documento operacional vigente atribui ownership global ou despacho obrigatório a um orquestrador.
- Referências históricas permanecem identificadas como históricas, sem apagar rastreabilidade.
- Cada handoff registra origem, destino, estado, evidência, aceite e próxima ação.
- O Scrum Master resolve impedimentos operacionais dentro da alçada e escala em sequência.
- Tech Lead está descrito sem conflito de autoridade não resolvido.
- A documentação separa decisão, proposta, implementação e comprovação.
