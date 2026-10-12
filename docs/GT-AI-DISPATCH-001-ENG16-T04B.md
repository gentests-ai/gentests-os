# ENG-16 — pacote local de construção T04b, sem execução cloud

## Situação e autorização

Autorização de construção condicional: https://github.com/gentestsai-sudo/gentests-os/issues/47#issuecomment-6117696178 . Base: decisão de desenho #6117689079, ENG-15 #6117663683, INFRA-06 #6117620568. Não constitui deploy, inferência, custo, recurso ou merge. G3 PR #68 integrado permanece baseline; código novo é referência de contrato **não integrada ao gateway em cloud**.

## Artefatos

- `scripts/gt_t04b_auth_local.py`: contrato de decisão Ed25519 (mensagem de domínio separada), validação offline de RS256 JWT com chave pública previamente confiada, políticas de claims por rota, SQLite local com autorização, revogação, replay, kill switch e reserva única **sem inferência**.
- `tests/test_gt_t04b_auth_local.py`: somente chaves efêmeras geradas na RAM para testes sintéticos; nenhum segredo real. Não testar login GitHub, JWKS online nem Cloudflare.
- Este guia: sequência de bootstrap, pré-requisitos, rota de execução futura e reversão.

### Assinatura e custódia

Escolha candidata: Ed25519 via biblioteca `cryptography` (versão testada em ambiente local documentado no retorno), mensagem `GT-T04B-AUTH-v1\0` seguida de JSON **ASCII com chaves ordenadas, sem espaços** e campos fechados. **Isto NÃO implementa RFC 8785 completo**; proibir Unicode/números fracionários/objetos arbitrários até especificação interoperável, validação de versões de runtime e fixture de interoperabilidade. `sign_with_existing_key()` recebe bytes PEM privados previamente existentes e **não cria, grava, envia ou distribui chave**. Ferramenta CLI interativa ainda não autorizada/produzida; somente helper Python local sujeito a revisão antes de uso humano. Chave de teste **não serve como identidade da Direção**.

Quando autorização futura específica existir: Direção escolhe gerador de chave auditável e ambiente offline confiável; mantém chave privada fora GitHub/ChatGPT/Cloudflare, protegida por armazenamento cifrado offline e backup físico sob controle exclusivo, testa recuperação com amostra sintética; publica apenas chave pública e ID. Não transmitir PEM privado, seed ou frases de recuperação em chats, issues, workflows, artefatos e logs. Perda/comprometimento => bloquear `/authorize` e novas invocações, revogar chave e reconstruir trust store após decisão da Direção. Não há prova de custódia real nesta etapa.

### Bootstrap planejado, sem circularidade

1. **Pré-criação** (decisão separada e ainda pendente para cada ato): confirmar conta Workers Free e elegibilidade DO/Workers AI, limites/Stop usage reais de cada superfície, owner e papéis, nome candidato de um Worker + um DO, escopo IAM, chaves públicas/versionamento, zonas/rotas não necessárias, dados sintéticos e matriz campo→destino→região→TTL→exclusão→ACL, termos e rollback. Se custos/privacidade/IAM inconclusivos, NO-GO. Nenhuma chave é gerada aqui.
2. **Criação manual futura pela Direção**: após autorização específica e condições comprovadas, usar sessão humana do Cloudflare Dashboard para criar apenas Worker e DO SQLite privados; configurar bindings mínimos e material público de confiança. Não dar token Cloudflare ao GitHub. Criar/configurar NÃO autoriza deploy ou primeira inferência.
3. **Após configuração autorizada**: verificar recursos/ACL, runtime JWT/JWKS, região/retention, falha segura, storage, orçamentos, revogação, logs sanitizados; executar só ensaios sem IA se seu próprio gate autorizar. Nunca exigir log de recurso inexistente como condição anterior à criação.
4. **Deploy inicial manual**, somente decisão específica G5 com SHA e rollback; workflow de executor **inexistente/inativo** até autorização posterior. Quando for autorizado: job de invocação `contents:read` + `id-token:write`, sem token Cloudflare; workflow de autorização manual com identidade/OIDC separada e assinatura externa, não gerada pelo job.
5. **Primeira inferência sintética** só decisão distinta G6, após negativos de JWKS, assinatura, revogação, replay, quota/custo e privacidade em ambiente autorizado.

### Limitações e pendências críticas

O módulo atual NÃO fornece servidor HTTP, rotas Cloudflare reais, JWKS fetch/rotation, isolamento de workflows, assinatura humana verificada, DO remoto, identidade GitHub real, quotas de Workers AI ou transição `intent→AI→done`. `verify_rs256_jwt` usa chave pública **injetada e aprovada localmente**, não baixa JWKS; o gateway simulado recebe JWT assinado e verifica-o internamente com chave pública injetada; não aceita claims já decodificadas do chamador. Na integração futura, o middleware deve construir claims verificadas somente após validação do token e validar issuer/audience/algoritmo, JWKS com rotação e key ID, workflow SHA e trust boundaries. Os testes locais não validam serviço cloud.

A verificação do `actor_id` em GitHub confirma conta que iniciou workflow, não independência humana. A assinatura externa preserva aprovação do escopo contra executor sem chave; administrador do código do gateway continua capaz de alterar o verificador. Repo privado Free não fornece por presunção proteção de ambiente de revisão humana. Uma única pessoa não cumpre gate de independência de duas pessoas se exigido.

**Permissões futuras:** Direção é bootstrap/deployer manual, exclusivamente via sessão humana autorizada; Actions executor jamais recebe Cloudflare token/Admin/Editor, GitHub write/merge/publicação; um endpoint `/authorize` e `/revoke` diferenciado `/invoke`; chaves privadas somente na máquina offline Direção. Nenhum workflow YAML será criado neste pacote.

**Reversão:** nenhum recurso real a desfazer. Para futura reversão de recurso autorizado: bloquear novas invocações, revogar decisão/chave sob owner, preservar status incerto, excluir/rollback configurações apenas com autorização e sem apagar trilha.

**Bloqueio de publicação:** `.github/workflows/email-quality-gate.yml` e `.github/workflows/markdown-check.yml` na main têm `on: pull_request`; abrir Draft pode executar Actions automaticamente. ENG-16 veda executar workflows; portanto preparar apenas local, não criar branch remota/PR sem decisão expressa sobre esse efeito. Não modificar workflows para contornar.

## Correção focal ENG-19 / QA-09

A01 exige chaves, tipos exatos e valores dos seis campos do evento. A02 permite exclusivamente `synthetic-only`, rejeitando operações proibidas e tipos inválidos antes de consultar a allowlist. A03 exige subject do repositório/ref aprovado e claims sintéticos assinados de decisão, issue, recurso, missão, etapa, geração e corpus. Esses claims de aplicação são fixtures locais: não se afirma que GitHub OIDC real os emite; adaptação futura exige desenho autorizado separado. A04 exige identificadores decimais canônicos e usa array JSON na chave de replay. Negativos não consomem a reserva legítima. Regressões estão na suíte T04b; nenhuma integração cloud ou roteamento novo foi incluído.
