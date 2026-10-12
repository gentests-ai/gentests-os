# GT-AI-DISPATCH-001 — ENG-10 G3 offline (Cloudflare A simulada)

**Escopo:** integração exclusivamente **fictícia**, Python padrão + SQLite local, sem Cloudflare, GitHub API, rede, credenciais, serviços, inferência, provisionamento, custo monetário, deploy ou publicação. **G4–G7 e T05 real não autorizados.** Referência financeira [#6116415804](https://github.com/gentestsai-sudo/gentests-os/issues/47#issuecomment-6116415804) de captura da Direção, não leitura direta da conta.

## Componentes e fronteiras de confiança
`FakeActionsRunner` representa execução finita com identidade `future-actions-reader` e allowlist `contents:read`; **não executa GitHub Actions**. A operação proposta Actions→Worker é apenas chamada Python local. Atores e decisão sintéticos vêm do `FakeAuthority` integrado no PR #67: dicionário de testes com `auth_ref`/identidade/escopo/versão/SHA/expiração/revogação, **não assinatura/autorização humana nem IAM real**. O `LocalGate` do PR #67 representa o Worker gateway + controlador Durable Objects num SQLite de teste com reservas transacionais, quota e kill switch fictícios. O `FakeWorkersAI` do PR #64 cria resposta e request ID determinísticos em memória **sem acessar Qwen3**.

O `execute` usa `reserve → hook de falha controlada → effect/revalidação → resposta fake`. `LocalGate.effect` revalida revogação/contador e marca `uncertain` no erro; retry não é automático. **A conclusão do checkpoint ocorre antes de gerar a resposta fictícia**: este artifício é apenas demonstração de gates offline, e não ordenação válida para um efeito externo real. G4 deverá tratar intenção de efeito, resultado incerto, atomicidade entre provedores impossível e reconciliação antes de marcar `done`. Não afirmar exactly-once nem controle financeiro real.

## Casos focais
`python3 -m unittest discover -s tests -p 'test_gt_t05_g3_offline.py' -v` cobre 11 métodos: sucesso sintético, replay, identidade/autorização falsificada, escopo/SHA/geração/versão, permissão mínima, revogação entre reserva/efeito, kill switch, timeout e erro desconhecido, quota fictícia, contador corrompido, fencing obsoleto, concorrência. A suíte preexistente é executada pelo workflow pré-existente `email-quality-gate.yml` no PR Draft, se os gates de Actions se mantiverem, sem rerun manual. Usar ambiente com módulos `scripts/gt_cloudflare_mock.py` e `scripts/gt_t05_security_mock.py` da main.

## Pendências, rollback e autonomia
- **G4**: identidade e autoridade autenticada fora do LLM, contrato Worker/DO, ACL, segredos, contas, região e dados sintéticos aprovados.
- **G5**: autorização específica de deploy sandbox + prova de hard stop de Actions, Worker, Workers AI/neurons, DO, logs/storage.
- **G6**: primeira inferência real de uma única missão, autorizada separadamente e com privacidade/licença/quotas aprovadas.
- **G7**: publicação e merge só mediante autorização própria da Direção e QA/validação aplicáveis.
- Reversão desta entrega: fechar PR Draft e descartar branch por ato autorizado; não mudar `main`. SQLite local de testes é temporário. O mecanismo não funciona com computador desligado de modo remoto; somente a arquitetura futura, se efetivamente implementada, poderá validar esse requisito.
