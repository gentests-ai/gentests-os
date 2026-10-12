# GT-AI-DISPATCH-001 — T05 Cloudflare MOCK (ENG-04)

**Somente offline/determinístico.** Simula interfaces, **não** usa Cloudflare Workers AI, Qwen3, Durable Objects, GitHub Actions como runtime do agente ou inferência real. Reutiliza `scripts/gt_dispatch_sim.py` e sua fixture autorizadora **fictícia** da T04-A; todo consumo, token e request ID são sintéticos.

## Arquitetura simulada
`evento sintético` → `authorize() T04-A, scope/generation/expiry/revocation` → `kill switch + teto fictício` → `FakeDurableObject SQLite local` → `FakeWorkersAI determinístico` → `SHA-256 de resultado` → `estado done/reconciliation`.

O futuro runner GitHub Actions seria **finito**, não processo sempre ligado. O contrato da inferência fake retorna `text`, `request_id: fake-...`, `tokens_fictitious` e `cost_fictitious_units`. Para falhas `401/429/500/503/timeout`, devolve erro sintético, **não** faz retry ou chamada externa. Em timeout o efeito é incerto e exige reconciliação humana.

O controlador usa `BEGIN IMMEDIATE` SQLite local, chave `repo+issue+mission+stage+generation+corpus_sha` derivada da base T04-A, estado leased/done/uncertain, token fence numérico e expiração. Reserva concorrente ativa bloqueia. **Lease expirado vira uncertain e NÃO é reatribuído automaticamente**: isso é fail-closed, **não** uma implementação completa de renewal/fencing distribuído. Hash validado só quanto ao formato, sem recomputação do corpo já salvo.

**Fronteiras de confiança:** campo `authorization` é fixture fictícia, não assinatura de Direção; textos de entrada são dados e não comandos. Nenhuma interface `publish/merge/deploy`; GitHub continua fonte canônica externa, sem escrita pelo mock. Não há integração com Workers AI, Durable Objects, AuthN, IAM, API, storage remoto ou orçamento real.

## Testes próprios
Na raiz do repositório, com Python 3 e biblioteca padrão:

```sh
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 -m unittest discover -s tests -p 'test_gt_cloudflare_mock.py' -v
```

Regressão T04-A de 16 testes é preservada e descoberta pelo padrão `test_*.py`. Testes mock cobrem sucesso/replay, disputa de lease, fence obsoleto, lease vencido, timeout/401/429/5xx, corrupção lógica, autorização fictícia, kill switch, orçamento, input malicioso inerte e nenhuma interface de publicação. **CT-20–32 são apenas referências de comportamento SIMULADO; testes cloud/IA/autenticação/revisão humana não foram executados.**

## Gates de evolução futura
Confirmar contrato real da API/modelo, elegibilidade/cotas e tratamento de dados, autorização assinada/validada fora do LLM, exclusão mútua remota transacional com geração/fencing durável, reconciliador de efeitos, isolamento e allowlists, kill switch real e auditoria; QA focal e aprovação da Direção antes de qualquer operação externa. Nenhum benchmark, latência ou disponibilidade com PC desligado demonstrados.

**Reversão:** PR não integrado pode ser fechado e branch descartada por operação autorizada; `main` não deve mudar. Bancos SQLite de testes são temporários e fictícios. **Sem merge, deploy, gastos ou uso de serviços.**

## ENG-05 — correção QA-03-A01/A02 (11/10/2026)

- `complete(k, fence, text, now)` agora recebe tempo de referência determinístico **obrigatório**, verificando `state`, `fence` e prazo com timezone dentro da mesma transação SQLite local. Antes do vencimento: permite; no instante exato ou depois: bloqueia e marca `uncertain` para reconciliação, mesmo sem `reserve` intermediária. Deadline ausente/inválido/sem fuso também bloqueia; o relógio **não é autenticado** e não fornece lease distribuído.
- `FakeWorkersAI.infer` só retorna `ok=True` se `failure is None`. Erros conhecidos continuam tipados; qualquer erro não reconhecido, inclusive valores de tipo não textual, vira `unexpected_failure`, efeito `unknown`, sem retry. A pipeline bloqueia e deixa checkpoint `uncertain`, não `done`.
- `attempted`, `spent` e `kill_switch` seguem argumentos de **simulação sem persistência/autoridade financeira real** (QA-03-L01, fora de escopo desta correção). Nenhum Worker, API, serviço, secret, consumo real, AuthN remota ou deploy.
