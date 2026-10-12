# PR #101: correções focais do parecer QA 5493411050

Estado: **NO-GO para ativação preservado**. Correções e ensaio preparado;
homologação independente e evidência remota ainda pendentes. Não reativar
o piloto, não alterar as variables de produção nem usar GROQ_API_KEY no ensaio.

## Correções implementadas

P1 economia: consulta periódica somente lê a fila/ledger. `idle`, `waiting` e
`manual_reconciliation_required` não iniciam instalação, suíte nem inferência.
Somente uma nova tarefa enfileirada exige validação completa do SHA/CI.

P1 reconciliação: classes distintas para espera e intervenção. Diagnóstico
persistido, `retry_at` para intervalo/cota; resultado incerto sai com código 2
e bloqueia inferência. SIGTERM antes da gravação do diagnóstico é reconhecido
pela reserva sem resultado. Nenhuma recuperação interpreta duplicata como
simples falta de cota.

P0 recuperação: testes novos usam processos independentes e SQLite durável.
Um processo é realmente terminado após reserva e submissão sintética; outro
processo retorna reconciliação sem nova submissão. Testes de atraso usam
relógio injetado; não provam disponibilidade ou agendamento real do GitHub.
Concorrência/substituição de runs e persistência em refs continuam exigindo
ensaio operacional. Preservação não é garantia de processamento oportuno.

## Ensaio remoto isolado, preparado e não executado

Workflow `GT47 isolated recovery rehearsal (no AI)` é manual e desligado por
default (`enable_test_writes=false`). Necessita existir na branch padrão
revisada antes de ser despachado. Não fazer merge somente para obter evidência
sem a autorização aplicável; CI offline não substitui esse ensaio.

O operador precisa autorizar o ensaio e sua permissão `contents:write`.
Grava somente uma branch `gt47-recovery-<trial>`, preservada para auditoria,
sem tocar `gt47-advisory-state`. Destino e prefixo são validados no código.
Não recebe secret Groq nem HF; usa provedor sintético fixo com journal durável
de submissões. `inference_calls=0` é uma propriedade do harness: não é prova
de inferência ou interrupção real do provedor. Regras de refs precisam permitir
a branch de ensaio; não alterar ACL para contornar erro silenciosamente.

Use `trial=qa-trial-001` (ou outro identificador novo de 8–40 caracteres
minúsculos/dígitos/hífens) e habilite apenas `enable_test_writes` do ensaio.
Não habilitar GT47_GROQ_ENABLED. Usar o MESMO trial entre as fases liga runners
novos à MESMA branch. Não reutilizar um trial de interrupção para outro caso.

| Caso | Procedimento e evidência esperada |
|---|---|
| CT01 atraso >10 min | `seed`, `hold_seconds=660`; o run segura por 11 min a faixa de concurrency do ensaio após persistir a tarefa. Enquanto ocupado, solicitar `advance`, hold=0. Ao iniciar depois, saída deve mostrar `elapsed_since_seed>=660`, `qa_pending` e uma submissão ENG. É ocupação da faixa de concurrency, não simulação de indisponibilidade de toda infraestrutura GitHub. |
| CT02 run pendente substituído | Durante o mesmo hold, solicitar dois `advance`, hold=0, com o mesmo trial. Registrar qual run pendente foi substituído/cancelado e a retomada no sobrevivente. Journal deve ter uma ENG. Não presumir substituição sem observar os estados dos runs. |
| CT03 interrupção | Novo trial: `seed` sem hold, depois `interrupt`. `timeout --signal=TERM 30s` termina processo após journal sintético. Assert automático exige exit 124, inspeção exit 2, estado de reconciliação e uma única submissão. Um novo run `advance` deve falhar com reconciliação, sem segunda submissão. Se processo não chegou ao journal antes do timeout, o ensaio falha. |
| CT04 ENG → QA | No trial normal, após ENG persistido, tentar avanço antes de 300s: `waiting` e horário de retorno. Após 300s, novo `advance`: `completed`, duas submissões (ENG/QA), nunca ENG duplicado. Agendamento não garante precisão e pode perder a janela de tentativa antecipada; registrar timestamps reais. |
| CT05 fila vazia | No workflow de produção, job `probe` deve retornar `idle` e jobs `validate/advance` ficar skipped. Provar com run de teste observado, sem habilitar inferência. O harness manual pode inspecionar trial inexistente sem criar estado, mas isso isoladamente não comprova skips do workflow de produção. |
| CT06 runners diferentes | Registrar IDs/hosts dos runs `seed`, ENG e QA, ler mesma branch de ensaio e verificar duas reservas e duas submissões. Após concluir, outro `advance` retorna idle sem incrementar journal. |

Guardar IDs/URLs, SHA, timestamps UTC/BRT, logs sem segredos, conteúdo da
branch/journal e minutos cobrados em Actions. HOLD=660 é opcional e consome
pelo menos 11 minutos de runner; não executar repetidamente. `hold_seconds`
somente aceita 0/660; máximo do job é 15 minutos. Não há tentativa de fabricar
falta de capacidade global nem de garantir que GitHub substitua run específico.

**Bloqueios para homologação:** este workflow ainda não está instalado na main,
e não há autorização inferida para merge, ativação do pipeline ou ensaio de
inferência. Evidência remota não foi produzida. QA deve revisar o delta e os
runs reais quando disponíveis; até lá, os cenários GitHub permanecem não
comprovados, mesmo que toda a suíte de processos tenha passado.
