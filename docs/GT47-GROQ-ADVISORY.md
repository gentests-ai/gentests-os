# GT47: Engenharia → QA com Groq, após validação offline

Implementação opt-in de pareceres, modelo `openai/gpt-oss-120b`. Não chama
OpenAI ou Hugging Face. Não altera o piloto sintético desabilitado nem os
gates T04/T05/T08. O modelo recebe tarefa e evidência de testes como dados;
não pode executar ferramentas, editar arquivos, aprovar, fazer merge ou deploy.
Engenharia propõe uma solução; QA avalia a proposta. Não é execução autônoma
de correções nem homologação independente humana. Testes verdes demonstram
checks executados, não a solução semântica da tarefa.

## Fluxo

Após integrar o workflow na branch padrão, uma alteração revisada na main
pode conter `gt47-advisory-task.txt`, com objetivo/escopo/critérios em texto
curto e sem segredos. O pipeline geral deve passar no mesmo SHA. O novo
workflow reexecuta suíte completa e links somente para enfileirar uma tarefa
nova, em job sem segredos, e confirma
checkout limpo. Não importa artefatos executáveis de runs de PRs/forks.

`gt47-advisory-task.example.txt` é um exemplo inerte, não enfileirado.
Copiar/adaptar para `gt47-advisory-task.txt` em uma mudança revisada define
a primeira tarefa; o sistema não toma a descrição da issue como tarefa ou
autorização automaticamente. O escopo deve caber no limite de contexto com
o parecer de Engenharia; um resumo excessivo também bloqueia o passo de QA.

Se o SHA já foi substituído na main, o evento antigo é rejeitado. Se o arquivo
de tarefa não existe, nenhuma tarefa é enfileirada. O controlador executa
somente código da main; o `workflow_run` aceita somente push bem-sucedido da
main deste repositório. Modelo, destino HTTPS e perfis ENG/QA são fixos.

O job posterior, com credenciais, reserva orçamento persistente ANTES de
enviar uma única chamada. A resposta de Engenharia é persistida e QA fica
pendente. Um run agendado posterior encaminha a QA, sem esperar cinco minutos
com runner ocupado. O agendamento a cada cinco minutos é melhor esforço do
GitHub: não garante latência. `workflow_dispatch` apenas avança uma fila
existente; não enfileira uma tarefa ou prova aprovação.

Labels `gt47-agent:AGT-ENG` / `gt47-agent:AGT-QA` continuam identificando
destinos no planner existente. Este pipeline encadeia as etapas diretamente,
sem aplicar/reaplicar labels e sem esperar que eventos gerados por
`GITHUB_TOKEN` iniciem outro workflow. Estado observável: `engineering_pending`
→ `qa_pending` → `completed` (somente pareceres). A recomendação de IA nunca
é autorização. Nenhum comentário automático é publicado.

## Consulta periódica e recuperação

Runs periódicos/manuais começam com `--inspect`: somente leitura de fila e
orçamento, sem dependências, suíte, reserva, escrita ou credencial Groq. Fila
vazia/completa retorna `idle`; cota/intervalo retorna `waiting` com `retry_at`;
reserva sem resultado retorna `manual_reconciliation_required`. Somente
`ready` libera o job de avanço. As validações pesadas são exclusivas do
enfileiramento de uma tarefa no SHA validado. A consulta ainda aloca um runner
leve e usa checkout/API GitHub; não é custo zero nem ausência total de runs.

Erros com resultado incerto produzem diagnóstico persistente e exit 2; espera
por cota produz exit 0 e pode ser retomada. Após SIGTERM, mesmo sem diagnóstico
gravado, a reserva durável sem resposta é detectada pela próxima consulta.
Não remover a reserva nem repetir chamada incerta. Reconciliar recibos,
resultado do provedor e SHA antes de qualquer intervenção no estado.

## Limites e persistência

- Teto global dos dois agentes: **40 chamadas e 160.000 tokens reservados em
  janela móvel de 24 horas**, não reset arbitrário à meia-noite. Não controla
  clientes externos que também usem a mesma conta Groq.
- Reserva fixa de 4.000 tokens por chamada, mesmo que o consumo real seja
  menor. Prompt limitado por tamanho conservador em UTF-8; saída limitada a
  1.024 tokens incluindo o orçamento de conclusão. Contexto acima do limite
  é rejeitado, nunca truncado sem aviso. Enviar escopo pequeno; não é revisão
  de repositório inteiro. Uso retornado excessivo/inválido exige reconciliação.
- Cinco minutos entre reservas é um limite escolhido para o piloto, não uma
  exigência confirmada do provedor. Respeita margem para 8.000 tokens/minuto.
- Sem retry de chamada externa. Timeout, erro e resposta inválida mantêm a
  reserva. Duplicatas do mesmo SHA/papel/contexto ficam bloqueadas inclusive
  depois de 24 horas. Não mudar contexto apenas para contornar erro incerto.
- Falta de cota/intervalo ANTES da reserva deixa a tarefa para o próximo run.
  Erro após reserva pode exigir reconciliação manual; agendamento não repete
  automaticamente uma inferência de resultado incerto, inclusive após 429.
- A branch `gt47-advisory-state` conserva `gt47-budget.json` e
  `gt47-current.json` entre runners. Escritas usam versionamento SHA/CAS;
  conflito de reserva é resolvido antes de chamar o modelo. Falha ao salvar
  resultado não autoriza resubmissão. Uma tarefa pendente não é sobrescrita.
- Uma tarefa global por vez. Concorrência de Actions pode substituir runs
  pendentes; a fila verdadeira é o registro persistente. Novas tarefas durante
  uma pendente falham explicitamente; não há fila ilimitada nem perda silenciosa.
- A credencial `contents:write` do job de estado também possui capacidade
  técnica de escrita no repositório; o código restringe o destino à branch de
  estado, mas isso não é ACL por branch. Revisar regras do repositório antes
  de ativar. Proteger registros contra alteração/remoção e preservar backup.
  Não apagar o ledger para "zerar cota": compromete replay e orçamento.

## Ativação: configuração ainda necessária

O workflow fica totalmente desligado sem duas variables de Actions:
`GT47_GROQ_ENABLED=true` e `GROQ_FREE_PLAN_CONFIRMED=true`. Confirmar Billing
e limites da própria conta antes de definir ambas; o programa não consegue
garantir gratuidade por inferir o plano a partir da chave. Usar uma conta no
plano gratuito, sem ativar cobrança automática. GitHub Actions também tem
suas próprias cotas; não há promessa de custo total zero.

Adicionar `GROQ_API_KEY` em Settings → Secrets and variables → Actions.
`HF_TOKEN` não autentica Groq direto. Nunca colocar valores em arquivos/chat.
Esta sessão recebeu 403 ao listar nomes de secrets/variables; existência de
`GROQ_API_KEY` não pôde ser confirmada, e nenhum segredo novo foi presumido.

A integração precisa estar revisada/integrada na main para `workflow_run`
e agendamento funcionarem. Ativação cria a branch de estado usando o SHA
validado e requer permissão real de escrita e compatibilidade com regras de
branches. Nenhuma alteração de ACL, merge, habilitação ou chamada externa foi
feita durante a implementação offline.

Parar: remover/definir `GT47_GROQ_ENABLED=false`. Preservar branch e resultados
para reconciliação. Respostas/modelo não devem ser executados como comando
ou interpretados como aprovação; a tarefa fica registrada na branch de estado.

## Validação

Na raiz, com as dependências `requirements-t04b-ci.txt` instaladas:
```sh
python -m unittest discover -s tests -p 'test_*.py'
python scripts/check_links.py
```

Os testes do novo adaptador usam armazenamento com CAS e transporte fictício,
sem segredos ou rede. Cobrem teto diário, intervalo, janela móvel, corrupção,
concorrência, replay, ausência de autorização/configuração, evidência de SHA,
conteúdo malicioso como dados, payload limitado, timeout, respostas inválidas,
perda de gravação e passagem ENG → QA. Não comprovam compatibilidade real
da API, chave, plano, ACL, workflow instalado ou inferência no provedor; um
piloto remoto explícito continua necessário após configurar os pré-requisitos.
