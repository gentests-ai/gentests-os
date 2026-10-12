# GT47: evidência remota de recuperação sem IA — 12/10/2026

**Estado:** ensaio isolado concluído; homologação independente pendente.
Produção continua desligada, PR #101 Draft, sem merge. Não é prova de
inferência Groq ou execução autônoma de correções. Zero chamadas de IA;
as respostas e contagens de tokens dos pareceres são sintéticas.

O usuário autorizou seguir com o ensaio remoto. A entrada foi o workflow
registrado `GT47 T06 Offline Tests`, ID 382155281, despachado na branch do PR.
Código do controller fixado no SHA offline aprovado
`c6ffa661be39a793bcdd43ab226fd4770453cba7`. A adaptação do wrapper passou por
actionlint e CI; os SHAs específicos de cada run estão no snapshot JSON.
Não foram recebidos/consumidos secrets Groq/HF nem alteradas as variables de
produção. O código de preflight só recebeu flags locais ao processo.

## Resultados observados

| Aceite | Evidência real e resultado |
|---|---|
| CT01 faixa ocupada >10 min | [Seed/ocupação 38281515152](https://github.com/gentestsai-sudo/gentests-os/actions/runs/38281515152) segurou a faixa de concurrency por 660s; job no runner `1000000693` de 14h02m10s a 14h13m19s BRT. O [run sobrevivente ENG 38281595335](https://github.com/gentestsai-sudo/gentests-os/actions/runs/38281595335) retomou no runner `1000000701`, com **672s** entre seed persistido e submissão ENG sintética. |
| CT02 substituição pendente | Durante a ocupação, [38281576660](https://github.com/gentestsai-sudo/gentests-os/actions/runs/38281576660) ficou pendente e foi **cancelado** ao chegar 38281595335. O sobrevivente processou a tarefa preservada; somente uma ENG no journal. O cancelado não recebeu runner (`runner_id=0`). |
| CT03 SIGTERM e reconciliação | [Seed 38281519913](https://github.com/gentestsai-sudo/gentests-os/actions/runs/38281519913), [interrupção 38281599849](https://github.com/gentestsai-sudo/gentests-os/actions/runs/38281599849), depois [retomada 38281815134](https://github.com/gentestsai-sudo/gentests-os/actions/runs/38281815134). `timeout --signal=TERM 30s` encerrou o processo após reserva/journal. O runner novo `1000000696` retornou **failure/exit 2 esperado**, com diagnóstico persistido `reserved_without_matching_result`. Ledger/journal permaneceram em uma reserva/submissão, sem replay. O run de interrupção foi success porque suas asserções confirmaram o SIGTERM e a necessidade de reconciliação. |
| CT04 ENG → QA e intervalo | [Tentativa antecipada 38282812796](https://github.com/gentestsai-sudo/gentests-os/actions/runs/38282812796) retornou `waiting/cooldown`, sem nova reserva/submissão. [QA 38283325197](https://github.com/gentestsai-sudo/gentests-os/actions/runs/38283325197), no runner `1000000703`, concluiu **336s após ENG**, estado `completed`, duas submissões (ENG/QA), `approval_granted=false`. |
| CT05 fila vazia, sem validação pesada | [38281980099](https://github.com/gentestsai-sudo/gentests-os/actions/runs/38281980099) executou a CLI de produção `--inspect` sobre branch de ensaio inexistente. Preflight `idle`, job de consulta cerca de 4s; `offline-tests` e `heavy-validation-if-ready` ficaram **skipped**, sem runner. Não houve instalação ou suíte. Trata-se do preflight e gate do wrapper de teste; o workflow periódico de produção continua desligado. |
| CT06 persistência e conclusão sem replay | Runners seed `1000000693`, ENG `1000000701` e QA `1000000703` consultaram a mesma branch `gt47-recovery-qa-20261012-busy001`. Após concluir, [38283435410](https://github.com/gentestsai-sudo/gentests-os/actions/runs/38283435410) retornou idle; continuaram duas reservas/submissões e 8.000 tokens **reservados sinteticamente**, sem nova chamada. |

Datas/horários do quadro em America/Sao_Paulo; o snapshot conserva timestamps
UTC originais e epochs do ledger. O intervalo conservador é entre reservas;
336s também satisfaz a distância entre as submissões sintéticas observadas.

## Artefatos e limites

Snapshot redigido de APIs GitHub, jobs/runners e refs de teste:
[GT47-RECOVERY-REMOTE-EVIDENCE.json](evidence/GT47-RECOVERY-REMOTE-EVIDENCE.json).
Inclui todos os runs iniciais/finais, inclusive falhas de preparação; não
omitir outcomes negativos nem confundir failure esperado com check aprovado.
Branches `gt47-recovery-qa-20261012-001`, `...-busy001` e `...-kill001` foram
preservadas para a revisão. A branch de produção `gt47-advisory-state` não
foi criada/modificada pelo ensaio.

As primeiras tentativas falharam antes da preparação válida. A chamada
reutilizável não iniciou o job; a entrada direta iniciou, mas recebeu erro
HTTP na criação do estado. Inicializar a ref de estado da branch padrão, sem
copiar alterações de workflows do PR, permitiu prosseguir com `contents:write`,
sem ampliar ACL/credenciais. O controller de tarefa continuou pinado em c6ffa66.
Não foi atribuída causa mais específica à falha inicial de carregamento.

O GET de logs completos foi bloqueado pelo proxy deste ambiente. Evidência
obtida por run/job APIs, refs, journal e asserções do harness; URLs permitem
revisão direta dos logs no GitHub. O domínio de download de logs foi salvo
aditivamente no rascunho do ambiente, sem aplicação/publicação confirmada.
Isso não impede a leitura do snapshot e não prova conteúdo de logs não lidos.

`reported_billable`/`run_duration_ms` vêm da API de timing; vários totais
retornaram zero. **Não são promessa de custo zero nem leitura de billing.**
`run_duration_ms` pode incluir espera em fila. Para duração efetiva do runner,
usar os timestamps do job com `runner_id>0`; o hold consumiu cerca de 11 min.

O caso CT01 demonstra ocupação de uma faixa de concurrency e recuperação
posterior em runner distinto, não indisponibilidade global do GitHub ou de
um runner self-hosted. A perda de oportunidade/substituição foi realmente
observada. O provedor foi sintético e não houve timeout/interrupção real do
Groq. Não concluir que chave, plano, rate limits ou inferência real estão
validados; esses permanecem pré-requisitos de um piloto separado.

**Próxima etapa:** QA focal revisa artefatos, IDs de runs e delta dos wrappers.
Não inferir autorização de ativação/merge do sucesso do ensaio. A produção
permanece desligada até decisão aplicável e condições verificadas.
