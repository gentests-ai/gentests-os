# GT47 — parecer focal de Infra / executor e persistência (12/10/2026)

**Referências:** issue #47, PR #101, T05 PASS e limites de autoridade vigentes. **Resultado:** GO para preparação/testes offline; NO-GO para ativação externa e afirmação de E2E autônomo.

## Runtime e infraestrutura mínima

- **Runtime existente:** GitHub Actions já executa testes T06 com `ubuntu-latest` e encerra o job. É runner temporário, não agente sempre conectado, não sessão ChatGPT. Reaproveitar é preferível a criar provedor de hosting antes de demonstrar necessidade.
- **Persistência local atual:** o SQLite `gt47_t06_claim_store.py` só garante exclusão mútua se múltiplas execuções usarem **o mesmo volume SQLite persistente**. Runners hospedados em Actions não compartilham esse disco; o teste local não demonstra replay entre runs.
- **Candidato de reserva distribuída:** `scripts/gt47_t06_github_claim_ledger.py` usa criação atômica de Git ref `refs/tags/gt47-claims/<sha256>` em repositório privado. O hash é derivado de repositório, missão, issue, agente e SHA fixado (não do nonce, que poderia variar entre entregas duplicadas). Cada chamada só produz intenção reservada; nunca processa IA nem envia para agente. Um conflito HTTP 422 só é classificado como replay depois de `GET` validar referência e SHA; demais falhas são bloqueadas sem retry. Mesmo com sucesso, **não há exactly-once de efeito externo**, recibo, aceite ou execução.
- **Alçada:** criar refs via GitHub API requer `Contents: write` ([documentação oficial](https://docs.github.com/en/rest/git/refs)). O código **não** concede permissão, não configura token, não está ligado a workflow e mantém `enabled=False` por padrão. Ativar exige decisão específica de acesso/escrita e checagem do impacto no repositório. Tags podem ser apagadas/reapontadas por atores com escrita; checar regras efetivas de proteção da namespace antes do uso. A criação de tags pode afetar triggers configurados; não assumir ausência de efeitos colaterais.
- **Retenção/escala:** refs criadas permanecem até exclusão; política de retenção e reconciliação operacional devem ser definidas antes de produção. Um commit por agente permite apenas uma tentativa de missão; nova geração requer evolução versionada do contrato, e nunca um nonce arbitrário.

## Conectividade real: lacuna que não se resolve com GitHub

GitHub Actions, GitHub refs, comentários, labels e o GitHub Connector permitem fila, reserva e trilha, **não** iniciam autonomamente conversas em chats do ChatGPT. O smoke OpenAI opcional da PR #101 testa resposta `READY`, não a execução de missão. Sem endpoint de executor autorizado que realmente processe tarefas e publique recibo/resultado, não existe T08 E2E real. Não declarar que acesso ao ChatGPT Plus concede API para runners.

GitHub Models foi [descontinuado em **30/07/2026**](https://github.blog/changelog/2026-07-01-github-models-is-being-fully-retired-on-july-30-2026/), portanto não é alternativa de inferência gratuita disponível. Recursos Cloudflare/Workers AI/Durable Objects existentes são mocks offline e não provam contas, créditos, elegibilidade ou infraestrutura em produção. GitHub Actions em repositório privado consome cotas conforme plano: `$0 spent` não prova custo incremental futuro igual a zero. Confirmar cotas/budget administrativo antes de ativar.

## Gate único para eventual ativação (não solicitado nesta etapa)

1. Engenharia indicar **executor efetivamente acionável** e contrato de transporte (endpoint, autenticação, resposta `received/accepted/completed`, versão, classificação de dados); não escolher provedor por suposição.
2. Infra verificar disponibilidade, plano e cobrança, IAM, segredo restrito, namespaces de refs, triggers indiretos, limite de concorrência, prazo, kill switch, recuperação de claims incertas e evidência de não cobrança antes da primeira invocação.
3. QA independente testar replay em dois runs distintos, token sem `contents:write`, payload malicioso, falha entre reserva/recibo, tempo esgotado, output não conforme e negação do executor. Somente Direção autoriza mudanças de ACL/segredos e operações externas reservadas.

**Reversão preparada:** desativar integração pelo gate em workflow/configuração autorizada; preservar refs/logs para auditoria, não apagar ou retentar claims `uncertain` automaticamente. Nenhuma operação externa ou configuração foi feita neste delta de código.

## Correção focal T08 — fencing persistente de invocação (09/11/2026)

A reserva `refs/tags/gt47-claims/<sha256>`, isoladamente, não impede que um chamador reutilize o mesmo objeto de reserva em memória e execute novamente o POST remoto. A ponte T08 agora exige uma segunda transição atômica antes do efeito externo: criação de `refs/tags/gt47-executor-started/<sha256>`, derivada da mesma identidade estável de missão/agente/commit.

Antes de submeter, o bridge:
1. valida a estrutura e a identidade da reserva;
2. relê e confirma a claim persistida no GitHub;
3. cria o fence de início uma única vez;
4. só então permite o POST ao executor.

Uma repetição com o mesmo objeto de reserva encontra o fence existente e é recusada antes de novo POST. Timeout/resultado incerto durante a criação do fence ou após sua criação não autoriza retry; exige reconciliação manual. A garantia é **no máximo uma tentativa de submissão por identidade enquanto os refs permanecerem íntegros**, não exactly-once do efeito remoto nem prova independente de execução. A namespace de claims e de fences precisa de proteção operacional contra exclusão/reapontamento antes de qualquer ativação real.

A implementação e os testes desta correção estão em PR Draft própria; ainda aguardam CI e revisão focal. Nenhum ref real foi criado nesta etapa.
