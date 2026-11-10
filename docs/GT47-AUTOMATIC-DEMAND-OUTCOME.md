# GTS-47: decisão automática da demanda no piloto

Diretriz da usuária em 2026-10-12: a conclusão normal da demanda não deve ficar
pendente de revisão humana obrigatória; os agentes precisam encaminhar, devolver
e finalizar dentro do escopo autorizado. Primeiro implementar o caminho feliz;
o retorno para ajustes será definido depois.

Neste piloto de pareceres, `completed` continua indicando que Engenharia e QA
terminaram a troca. O resultado da demanda é separado:

| Resultado | Condição |
| --- | --- |
| Em andamento | Troca ainda não terminou |
| Finalizada automaticamente | Ambos os pareceres salvos no mesmo commit e QA favorável |
| Ajustes necessários | Ambos salvos e QA recomenda `needs_changes` |
| Resultado não verificado | Handoff ausente, inválido ou commit/agente divergente |

Novos pareceres usam `ready_for_finalization` em vez de exigir revisão humana.
O valor histórico `ready_for_human_review` permanece legível como recomendação
favorável. Registros anteriores não são reescritos; a apresentação calcula o
resultado a partir dos pareceres. Novos avanços QA persistem `demand_outcome`.
A rodada 03 tem QA `needs_changes`: troca concluída, demanda com ajustes
necessários. Nenhuma aprovação favorável será inventada para fechar o piloto.

O registro final de tarefa definido pelo GT-HANDOFF-001 v0.3.0 é uma obrigação documental transversal para os agentes. No piloto GTS-47, ele não substitui os pareceres de Engenharia/QA, a conferência de commit/agente nem a evidência específica de transferência exigida pelo fluxo. A ausência de registro obrigatório torna a saída documental incompleta; isso não prova, por si só, falha de runtime ou transferência não realizada.

A finalização da demanda não concede permissão de execução técnica, merge,
deploy, mensagem externa ou gasto. Flags de autorização técnica permanecem
false. Nenhum retry, reset de claim ou retorno automático foi introduzido.

## Catálogo para evolução

A fonte de papéis é [o índice canônico](../02-Agentes/Indice-de-Agentes.md).
Há 14 papéis documentados; isso não comprova implementação de todos os agentes.
Engenharia e QA são apenas a dupla operacional deste piloto. Scrum Master (atuação por exceção), Produto, UX/UI, Infraestrutura, Comercial,
Marketing, Financeiro, Validador, Auditor, X9, Governança e Processos mantêm
as fronteiras de seus contratos. Não há Orquestrador Central como papel ativo.
A evolução do caminho feliz completo deve distinguir recebimento, aceite,
encaminhamento, retorno, validação pelos papéis pertinentes e encerramento.
Não transformar QA em aprovador universal ou duplicar o papel do Validador.

Validação desta mudança: testes de QA favorável, ajustes, commit divergente e
resumo sem bloqueio humano obrigatório. Nenhuma nova inferência foi feita.
