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

**Registro histórico pré-integração:** a correção foi desenvolvida e validada na PR #136. O status Draft descrito nas atualizações contemporâneas foi superado pela integração posterior à `main`; os checks offline T06/T07/T08 e Markdown passaram no HEAD revisado `8f9a185631c292b7f6f9b9825b7bae6d3d67b9b0`. A integração do código não criou refs reais nem configurou endpoint, secret ou ACL.


## Estado consolidado após integração — 09/11/2026

- PR #134 integrou a correção do checkout do controlador de recovery e a preservação das evidências históricas.
- PR #135 integrou o fail-closed do ledger T06: ausência da branch/ledger de produção exige reconciliação; não há reinicialização silenciosa de orçamento nem reenvio automático após resultado incerto.
- PR #136 integrou o fence persistente one-shot T08 e o endurecimento do transporte HTTPS. No HEAD validado, as suítes T06 (100), T07 (10) e T08 (30) passaram; Markdown também passou. O rehearsal pesado permaneceu SKIPPED.
- O código continua opt-in e inerte por padrão. Não há endpoint de executor configurado, consumidor/runtime conectado, credenciais ou chave de recibo implantadas. Nenhuma execução ponta a ponta real foi demonstrada.
- O gate de proteção operacional das namespaces `gt47-claims` e `gt47-executor-started` continua aberto. A consulta administrativa de branch protection/rulesets retornou 403; portanto, não é possível afirmar que as proteções estão ativas nem que estão ausentes.
- A revisão focal registrada pelo Head Tech Lead não substitui revisão independente por identidade segregada. Não tratar CI verde como aprovação independente.
- A consulta atual ao contexto de deploy Vercel retornou `teams: []`; não há projeto/time Vercel acessível nesta conexão para identificar ou inspecionar um executor existente. Nenhum projeto foi criado.

## Próxima ação técnica

O próximo avanço útil não é adicionar outro mock ou workflow sintético. É identificar um serviço executor real já disponível ou, após decisão de arquitetura e alçada, provisionar um serviço mínimo com endpoint HTTPS autenticado, autorização out-of-band, recibos assinados, persistência de estado e kill switch. Antes de qualquer invocação real, Infra deve confirmar plano/custo, IAM, secrets, proteção das refs e efeitos de triggers; QA independente deve testar dois runs distintos e os cenários de replay, timeout e revogação.


## Avaliação de candidato de runtime — Cloudflare Workers (09/11/2026)

A pesquisa documental atualizada indica que Cloudflare é tecnicamente viável para um piloto pequeno, mas a conta e a elegibilidade desta organização ainda não foram verificadas. Portanto, isto é uma seleção de arquitetura candidata, não autorização de provisionamento.

- **Gateway:** um Cloudflare Worker HTTPS, sem domínio/rota pública customizada inicialmente; validar token GitHub OIDC por JWKS com issuer, audience, repository_id, repository, workflow_ref, workflow_sha, ref, event_name, actor_id, run_id e run_attempt. Não confiar em claims de aplicação que o GitHub OIDC não emite; decision_id, issue, recurso e contexto devem ser dados do corpo vinculados à decisão Ed25519 assinada.
- **Estado:** Durable Object com SQLite para serializar authorize, revoke, reserva, fence, recibos e kill switch. A documentação informa armazenamento transacional/fortemente consistente por objeto; cada missão deve ter chave/instância isolada e retenção explícita.
- **Inferência:** Workers AI com modelo elegível ao Free e function calling. @cf/zai-org/glm-4.7-flash aparece como modelo ainda disponível no Free e o catálogo descreve suporte a tool calling; validar na conta/modelo real antes de uso. O Worker deve executar somente ferramentas allowlisted, com schemas fechados, limites de iteração/tokens e sem permissões de merge/deploy/produção.
- **Orçamento de referência (não é leitura da conta):** Workers Free informa 100.000 requests/dia e 10 ms CPU por invocação; Workers AI informa 10.000 Neurons/dia sem custo no Free. Durable Objects com SQLite têm alocações Free documentadas, incluindo 100.000 requests/dia, 13.000 GB-s/dia, 5 milhões de rows lidas/dia, 100.000 rows gravadas/dia e 5 GB de armazenamento. Workers Paid começa em US$ 5/mês; alguns modelos exigem plano pago. Não configurar fallback pago. Os limites são compartilhados por conta e excedentes/erros dependem do plano e do modelo.
- **Autenticação de deploy:** o guia Cloudflare para GitHub Actions atualmente documenta API token + account ID para deploy via Wrangler. Isso não é necessário para desenvolvimento local e não será adicionado ao GitHub. Deploy manual pela Direção continua gate separado; não criar secret nem token.
- **Integração:** Actions pode continuar como iniciador finito e portador de OIDC de curta duração; o Worker é o gateway/executor remoto. O job de invocação deve ter somente contents:read e id-token:write, sem GITHUB_TOKEN com escrita entregue ao Worker. Se for necessária escrita GitHub, usar um fluxo separado, com escopo mínimo e revisão específica; nunca expor token amplo ao modelo.

### Correção de evidência sobre workflows existentes

A leitura direta dos YAMLs na main em 09/11/2026 corrige a afirmação antiga do ENG-16:
- .github/workflows/email-quality-gate.yml tem somente workflow_dispatch; não dispara automaticamente em abertura de PR.
- .github/workflows/markdown-check.yml tem pull_request e push para main; abrir/atualizar Draft PR aciona este check.
- O workflow sintético eng20-synthetic-issue-dispatch.yml permanece desabilitado e não será reativado.

A criação de branch/PR não equivale a deploy; o único efeito automático confirmado na PR documental #144 é o check de Markdown. A execução manual do quality gate segue limitada à autorização de testes seguros já registrada; não disparar workflow sintético.

### Conclusão técnica desta avaliação

**Candidato recomendado:** Cloudflare Worker + Durable Object SQLite + Workers AI (modelo Free com function calling), iniciado por GitHub Actions OIDC. É a opção de menor infraestrutura já alinhada ao desenho T04b, sem servidor sempre ligado e sem credencial de longa duração no runner.

**Não está pronto para ativação:** faltam confirmação da conta/plano/limites reais, criação autorizada do Worker/DO, trust store com chave pública real, validação de JWKS/claims no runtime, endpoint e recibos assinados, testes de integração em ambiente sandbox e decisão específica para deploy/primeira inferência. Nenhum recurso foi criado, nenhuma chave/token foi gerada e nenhum custo foi incorrido.

**Fontes oficiais consultadas (09/11/2026):**
- Workers limits: https://developers.cloudflare.com/workers/platform/limits/
- Workers pricing: https://developers.cloudflare.com/workers/platform/pricing/
- Workers AI pricing: https://developers.cloudflare.com/workers-ai/platform/pricing/
- Durable Objects pricing: https://developers.cloudflare.com/durable-objects/platform/pricing/
- Durable Objects SQLite: https://developers.cloudflare.com/durable-objects/api/sqlite-storage-api/
- Workers AI function calling: https://developers.cloudflare.com/workers-ai/features/function-calling/
- Workers AI model catalog: https://developers.cloudflare.com/workers-ai/models/
- GitHub Actions OIDC: https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-cloud-providers
- Cloudflare GitHub Actions deploy: https://developers.cloudflare.com/workers/ci-cd/external-cicd/github-actions/

**Estado da missão:** T04 concluída; T05 read-only homologada; T06–T08 têm preparação e correções offline integradas, mas o critério de recebimento → aceite → execução → resultado por executor realmente conectado continua **NÃO COMPROVADO**. Missão #47 permanece aberta.
