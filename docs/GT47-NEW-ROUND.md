# GTS-47: preparar uma nova rodada

Este procedimento não resolve a tentativa anterior. Aceita uma tentativa bloqueada
ou uma troca concluída cujos pareceres passaram na validação de integridade. Arquiva sua fila exatamente
como está, preserva `gt47-budget.json` e cria uma tarefa identificada por rodada
em um commit diferente. Não apagar claims ou reexecutar o run antigo.

## Preparação sem IA

Após revisão e merge desta mudança em main, manter `GT47_GROQ_ENABLED=false`.
Manter Actions orçamento USD 0 / Stop usage Yes e Groq no plano Free.
Abrir **12 - GTS47 Nova rodada (sem IA)** e executar **Run workflow** na main:

- `round_id`: `pilot-round-02`
- `expected_id`: `cc83d5def2d9a0c5f2f918964568e695467130ff9083062deca00157c4aadcc9`

O ID acima é o observado na tentativa antiga: se a fila mudou, o workflow
recusa a substituição. Não alterar o ID para contornar um erro sem inspecionar
qual tarefa está ativa. Uma tarefa em andamento sem bloqueio e um resultado
concluído não verificável são recusados. O workflow valida main offline, usa a mesma concorrência
do piloto e não recebe chave de provedor. Apenas arquiva e prepara a fila.
Uma execução bem-sucedida retorna `round_prepared` e `provider_calls=0`.

O arquivo `gt47-archive/<expected_id>.json` preserva a tentativa bloqueada.
A nova fila registra `round_id`, `previous_task_id`, commit e uma tarefa com
prefixo de rodada; a reserva antiga continua contando no orçamento global.
Arquivo histórico incompatível, fila inesperada, commit igual ou identidade de
nova chamada já reservada impedem a preparação. Se houver resultado de gravação
incerto, inspecionar a fila e o arquivo antes de qualquer nova execução.

## Validação limitada com Groq Free

Antes de habilitar, confirmar `round_prepared`, arquivo histórico correspondente
e reserva antiga intacta. Confirmar também plano Free e controles de custo.
Então habilitar `GT47_GROQ_ENABLED=true` e executar o workflow **09 - GTS47
Groq ENG-QA** na main: ele avança somente uma etapa. O agendamento também pode
avançar a fila; ambos compartilham concorrência e reservas.

Verificar `qa_pending` e parecer de Engenharia persistido. QA só pode avançar
após o intervalo mínimo de 300 segundos; consome o parecer de Engenharia do
mesmo commit. Ao obter `completed`, verificar ambos os resultados e voltar
`GT47_GROQ_ENABLED=false`. Não alterar main nem o arquivo da tarefa durante o
piloto limitado, para evitar enfileiramento de outra tarefa pelo QG Email.

Em qualquer falha, pausar e inspecionar o novo diagnóstico. Não reexecutar
chamada incerta nem limpar reservas. `ready_for_human_review` é parecer, não
aprovação humana. Esta mudança não faz chamadas Groq ou OpenAI por si só.
