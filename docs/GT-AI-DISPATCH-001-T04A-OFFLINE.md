# GT-AI-DISPATCH-001 — ENG-02 / preparação T04-A

**Somente simulação offline.** Não é agente autônomo, serviço, autenticação de usuário ou executor GitHub Actions. Não usa rede, API, modelo, tokens, bibliotecas de terceiros ou dados reais.

Executar na raiz do repositório (Python 3, biblioteca padrão):

```sh
python3 -m unittest discover -s tests -p 'test_gt_dispatch_sim.py' -v
python3 scripts/gt_dispatch_sim.py --fixture tests/fixtures/gt_dispatch_event.json --db /tmp/gt-dispatch-synthetic.sqlite --now 2026-10-11T20:00:00Z
```

O primeiro comando cobre autorização fictícia válida, ausente, revogada, expirada, escopo/geração, operação proibida, replay, restart e checkpoint corrompido. O segundo grava SQLite local em caminho informado pelo operador; repetição responde `duplicate`, e reserva interrompida exige reconciliação humana (`pending_requires_reconciliation`). Resultados `blocked` terminam com exit code 2 na CLI. A fixture é fictícia e sua aprovação não representa assinatura/autenticação da Direção.

## Limites e evolução condicionada

- SQLite é checkpoint **local** e não coordena runners distintos nem fornece lease/fencing distribuído. Antes de nuvem: reserva atômica compartilhada (CAS/transação), lease com token de fencing monotônico, timeouts, reconciliação de efeitos externos, revisão de acesso e autenticação real da decisão fora do LLM.
- O código não chama rede, lê documentação corporativa, dispara runner, cria PR ou executa ferramentas do modelo. A saída é hash determinístico de resposta sintética. Não implementa publicação remota nem retomada automática de estado ambíguo; bloqueio seguro é intencional.
- Futuro kill switch externo ao modelo: revogação e bloqueio de novos disparos revalidado antes de cada efeito; orçamento/cota e privilégio técnico comprovados antes de Action/API.
- PR Draft **não aberto**: workflows `pull_request` podem disparar e a cota/billing/hard stop efetivos não estão comprovados. Não alterar workflows para contornar o gate.
- Reversão: descartar branch técnica sem merge; nenhuma alteração na `main`. Banco SQLite descartável fora da trilha Git.

**Autocheck** não equivale a QA/cloud/CT-01–32. Revisão e merge permanecem pendentes de autorização aplicável.

## ENG-03 — correção focal QA-01 (11/10/2026)

- A01: `stage` restringido a `simulate`; `authorization` fictícia passa a comparar, por tipo e valor exatos, `repo, issue, mission, stage, generation, corpus_sha` da entrada. Isso **não** é assinatura nem autenticação humana.
- A02: um checkpoint só é reconhecido como `duplicate` quando `status=done` e `output_hash` é uma cadeia hexadecimal SHA-256 em minúsculas de 64 caracteres. Hash nulo, vazio, inválido ou estado desconhecido resulta em bloqueio para reconciliação. **Não há prova de integridade criptográfica do conteúdo armazenado**, pois a saída não é recuperada para recomputação.
- A03: tipos exatos nos campos de identidade (`issue` e `generation` inteiros não booleanos), campos textuais não vazios e corpus SHA fictício hexadecimal em minúsculas de 40 caracteres.
- Regressão offline: 10 testes originais + 6 grupos novos (subtestes de identidade, tipos e corrupção lógica), sem execução cloud, API, Actions, QA independente ou piloto T05.
- Gate anterior persiste: PR Draft bloqueado por falta de comprovação de Actions/billing/custo incremental R$ 0.
