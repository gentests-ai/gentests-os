# GT-AI-DISPATCH-001 — ENG-20 / prova offline em duas etapas

**Estado:** pacote sintético submetido a PR Draft, sem merge ou execução cloud.

## Execução

```sh
PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py' -v
PYTHONPATH=. python -m scripts.gt_dispatch_two_stage_offline --fixture tests/fixture_eng20.json --db demonstration.sqlite
```

**Isolamento:** stdlib Python + SQLite. Nenhuma API, LLM, chamada GitHub, subprocesso, credencial, ação externa, rede ou IAM.

**Mecanismo:** um processo local finito com handlers determinísticos especializados `AGT-ORQ` e `AGT-ENG` inspirados nos contratos em proposta da main (não são duas contas nem dois chats autônomos). Resultado ORQ é transmitido diretamente ao ENG pelo processo, persistindo hash de saída ORQ igual ao hash da entrada ENG. O estado é conservado num SQLite local; sem segunda ação humana.

**Proteções:** allowlist única `synthetic_diagnostic` e `simulate:synthetic`, schema/validação exata, sequência fixa sem laço, chave `run_id` única, colisões negadas, `uncertain` em falhas, ausência de retries automáticos, saída e evidências por etapa.

**Limites:** não integra G3/T04b auth real, não valida a assinatura externa/JWT no novo runner, não contém motor remoto de execução, não emite despachos para chats ChatGPT, GitHub Issues ou agentes vivos. Uma prova de mecânica offline não demonstra disponibilidade com computador desligado, execução autônoma cloud, independência humana ou custos efetivos em cloud. Antes de cloud deve-se integrar gates de autorização/identidade existentes e testar de novo o delta.

**Publicação:** autorizada exclusivamente em branch isolada e um PR Draft, incluindo os dois checks existentes; merge e deploy não autorizados. Não alterar workflows.

**Referências:** issue #47, PR #68 (merge `19061ae04d18c011133cb14e8fcc5921f56a9969`), PR #70 (merge `03e9632838d65100f273aae4862da419e8379562`), diretriz funcional #6118047148, autorização #6118282791.
