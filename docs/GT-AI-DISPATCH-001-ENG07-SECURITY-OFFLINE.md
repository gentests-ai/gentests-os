# ENG-07 — GOV-08 / simulação offline de autoridade e quotas

**Somente mock Python + SQLite local**, sem rede/API, Workers/DO, segredos, credenciais ou identidade humana autenticada. Autorização [Direção #6115797029](https://github.com/gentestsai-sudo/gentests-os/issues/47#issuecomment-6115797029); despacho [#6115807197](https://github.com/gentestsai-sudo/gentests-os/issues/47#issuecomment-6115807197). A Cloudflare continua **referência candidata**, não decisão operacional.

## Contratos simulados
- `FakeAuthority.verify`: lê `auth_ref` exclusivamente de um dicionário privado ao harness, compara identidade `repo,issue,mission,stage,generation,corpus_sha`, `scope`, `decision_version`, expiração e revogação. `approved:true`, texto de comentário e modelo nunca concedem autorização por si. **O harness não verifica assinaturas nem identidade humana; emissor/verificador/revogador reais não designados.**
- `LocalGate.reserve/effect`: transações `BEGIN IMMEDIATE` no **mesmo arquivo SQLite local**. Reserva 1 unidade fictícia e bloqueia replays/concorrência, contador inconsistente, quota esgotada e kill switch. Antes do efeito, revalida revogação/expiração/escopo; se falhar, marca `uncertain`, sem retry. Fence obsoleto bloqueado. Não há relógio autenticado, lease distribuído, API, ou garantia exactly-once entre serviços. A reserva é persistente apenas no banco **local** da simulação; não controla custos monetários.
- `allowed`: matriz de código de teste permite exclusivamente `future-actions-reader / contents:read`. Não cria IAM nem impede operações reais fora deste mock.

## Matriz de principal e privilégios FUTUROS — nenhuma concessão
| Papel | Principal a designar | Escopo permitido proposto | Revogação/owner | Prova ainda faltante |
|---|---|---|---|---|
| Direção/emissor | pessoa autenticada | emissão de decisão específica | Direção | identidade, trilha e versão resistente a adulteração |
| Verificador/revogador | identidades distintas | verificar/revogar decisão fora do LLM | Direção/Governança | designação, ACL, mecanismo autenticado |
| Operador | humano a designar | uma missão sintética aprovada | Direção | registro de acionamento |
| Executor Actions | job principal a designar | apenas `contents:read` de SHA permitido | Infra | token efetivo, escopo, expiração |
| Gateway Worker | serviço a designar | autenticar chamadas, chamar DO/IA autorizados | Infra | IAM/bindings e allowlist |
| Durable Object | binding futuro | transações de uma missão | Infra | capacidade, isolamento e revogação |
| Provedor de IA | conta/modelo futuro | inferência de corpus sintético | Direção/Infra | termos, limites, segredo |
| Gestor de segredos | identidade a designar | rotação e revogação | Direção/Infra | cofre, segregação, logs |
| QA/revisor | responsável a designar | verificar sem editar/merge automático | Orquestrador | separação humana demonstrada |
| Publicador/incidente | humano habilitado | publicar ou parar após autorização | Direção | mecanismo e evidência |

## Decisões GOV-08-A06 — separadas
1. Arquitetura/provedor final — PENDENTE.
2. Preparação offline e único PR Draft — AUTORIZADA em #6115797029; **merge não autorizado**.
3. Identidades/cofre, Worker/DO/workflow — PENDENTE.
4. Deploy sandbox — PENDENTE.
5. Primeira inferência real sintética — PENDENTE.
6. Cada merge/publicação/expansão — PENDENTE, decisões por objeto/versão.

## Destinos e retenção — GOV-08-A04 pendente
| Dado inteiramente fictício | Destino FUTURO | Região/retenção/descarte | Acesso |
|---|---|---|---|
| Evento, SHA, decisão de teste | GitHub runner | NÃO VERIFICADOS | a definir |
| Prompt/output sintético | Workers AI ou Groq | NÃO VERIFICADOS | a definir |
| Checkpoint/counters locais de mock | DO futuro | NÃO VERIFICADOS | a definir |
| Log/erro/consumo sanitizado | GitHub/Cloudflare | NÃO VERIFICADOS | a definir |

**R$0 integrado, conta, quotas reais, hard stop financeiro, licenciamento, finalidade, retenção, região e acesso de produção NÃO VERIFICADOS.** Os parâmetros `cap/used/killed` são dados fictícios locais, não salvaguardas reais. Falhas de consumo do provedor real seguem sem implementação.

## Verificações e reversão
Comando focal na raiz: `python3 -m unittest discover -s tests -p 'test_gt_t05_security_mock.py' -v`. Dez casos por método incluindo autenticação forjada, ausência, expiração, versão/SHA, revogação após reserva, quota, corrupção, corrida, fencing, timeout e proibições. Reutilizar histórico de QA-04 do PR #64 para partes não alteradas; CI automático existente (se PR aberto sob orçamento) executa suíte completa e Markdown, **sem equivaler a QA do delta**. Sem testes de cloud/IA.
Reversão: fechar o Draft/descartar branch **por ato autorizado**, mantendo `main` e histórico intactos.
