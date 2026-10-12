# GT-AI-DISPATCH-001 — ENG-10 G3 offline (Cloudflare A simulada)

**Escopo:** integração exclusivamente **fictícia**, Python padrão + SQLite local, sem Cloudflare, GitHub API, rede, credenciais, serviços, inferência, provisionamento, custo monetário, deploy ou publicação. **G4–G7 e T05 real não autorizados.** Referência financeira [#6116415804](https://github.com/gentestsai-sudo/gentests-os/issues/47#issuecomment-6116415804) de captura da Direção, não leitura direta da conta.

## Componentes e fronteiras de confiança
`FakeActionsRunner` representa execução finita com identidade `future-actions-reader` e allowlist `contents:read`; **não executa GitHub Actions**. A operação proposta Actions→Worker é apenas chamada Python local. Atores e decisão sintéticos vêm do `FakeAuthority` integrado no PR #67: dicionário de testes com `auth_ref`/identidade/escopo/versão/SHA/expiração/revogação, **não assinatura/autorização humana nem IAM real**. O `LocalGate` do PR #67 representa o Worker gateway + controlador Durable Objects num SQLite de teste com reservas transacionais, quota e kill switch fictícios. O `FakeWorkersAI` do PR #64 cria resposta e request ID determinísticos em memória **sem acessar Qwen3**.

**Correção ENG-11 / QA-07-A01:** `execute` usa agora `reserve → hook → revalidação transacional e estado intent → resposta fake → validação estrita do contrato → revalidação transacional → registro de evidência (request_id/hash/consumo fictício) + done no mesmo commit SQLite`. Revalidação de revogação, escopo, quota, kill switch e fencing ocorre **antes** da resposta; nova revalidação acontece antes de `done`. Resposta `ok=False`, nula, incompleta, tipos inválidos ou exceção deixam `uncertain`, com `retry=False`; replay é bloqueado. `reconcile` apenas lê status/evidência sem reiniciar o efeito. A evidência fictícia não autentica o provedor; no runtime G4 será preciso tratar intenção, resultado incerto entre provedores, clock, prova externa e reconciliação, **sem prometer exactly-once**.

## Casos focais
`python3 -m unittest discover -s tests -p 'test_gt_t05_g3_offline.py' -v` cobre 18 métodos (11 originais + 7 focais QA-07): sucesso sintético, replay, identidade/autorização falsificada, escopo/SHA/geração/versão, permissão mínima, revogação entre reserva/efeito, kill switch, timeout e erro desconhecido, quota fictícia, contador corrompido, fencing obsoleto, concorrência. A suíte preexistente é executada pelo workflow pré-existente `email-quality-gate.yml` no PR Draft, se os gates de Actions se mantiverem, sem rerun manual. Usar ambiente com módulos `scripts/gt_cloudflare_mock.py` e `scripts/gt_t05_security_mock.py` da main.

## Pendências, rollback e autonomia
- **G4**: identidade e autoridade autenticada fora do LLM, contrato Worker/DO, ACL, segredos, contas, região e dados sintéticos aprovados.
- **G5**: autorização específica de deploy sandbox + prova de hard stop de Actions, Worker, Workers AI/neurons, DO, logs/storage.
- **G6**: primeira inferência real de uma única missão, autorizada separadamente e com privacidade/licença/quotas aprovadas.
- **G7**: publicação e merge só mediante autorização própria da Direção e QA/validação aplicáveis.
- Reversão desta entrega: fechar PR Draft e descartar branch por ato autorizado; não mudar `main`. SQLite local de testes é temporário. O mecanismo não funciona com computador desligado de modo remoto; somente a arquitetura futura, se efetivamente implementada, poderá validar esse requisito.
