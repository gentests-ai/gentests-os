# GT47 T05 — integração autenticada controlada

## Entrega executável

O módulo `scripts/gt47_t05_authenticated_readiness.py` disponibiliza `authenticated_readiness(token, commit_sha, agent_id, contract_path)`. A execução **não é automática**. Com token explicitamente fornecido pelo operador, consulta o GitHub somente por GET HTTPS e caminhos autorizados, valida Git blobs, políticas e contrato no mesmo commit, pagina comentários, valida SHA-256 do envelope e retorna **somente um resumo sem token nem corpos de comentários**. Nunca despacha agentes, cria comentários, modifica GitHub, aciona workflow ou chama LLM.

## Critérios de aceite e limites

- Testes offline negativos: token ausente, SHA não fixado, envelope adulterado e execução habilitada devem falhar sem ações externas.
- Teste E2E autenticado real: requer token de leitura do repositório privado, contrato real de agente e commit fixado. **Não realizado apenas por CI de mocks.**
- Validar vínculo agente/contrato real e proveniência antes de confiar no resultado. Comentários não autorizam ações.
- A paginação continua eventualmente consistente e não serve como fonte de decisão normativa.
- Custo zero, limites de Actions e privacidade do provedor de IA **não comprovados** para ativação. Não criar credenciais, configurar IAM, ativar workflow desabilitado ou gastar recursos por inferência.
- Antes de executar agente na nuvem: obter autorização expressa da Direção para ambiente, credenciais, escopo, custo, replay e operação; QA independente conforme política.

**Estado:** preparação segura T05; a conclusão funcional da T05 depende de E2E autenticado e gates externos verificáveis. Não confundir esta entrega com agente autônomo funcionando.

## Ensaio manual parametrizado (não executado)

O segredo informado pela Direção deve ter o nome exato `GT47_T05_READONLY_TOKEN` nas configurações do repositório. A existência e o valor do segredo **não são visíveis** ao conector de leitura. O workflow `.github/workflows/gt47-t05-readonly-e2e.yml` só pode ser despachado manualmente após estar disponível no branch padrão; a PR Draft por si só não o torna executável em Actions. Não confundir merge com autorização para ativar agentes: este workflow executa apenas GET autenticados e não chama IA.

Parâmetros de referência verificados no GitHub, para o primeiro ensaio de leitura:

- `commit_sha`: `a0e23f62752bb2d75df810585bfcfc4b026f6c70` (merge T04 fixado em main)
- `agent_id`: `AGT-QA`
- `contract_path`: `02-Agentes/QA/Contrato-Agente-QA.md` (contrato real, ID conferido)

O ensaio não exige token na interface de dispatch. Se o segredo estiver ausente, a execução deve falhar sem imprimir seu conteúdo. Resultado esperado: linha `GT47 T05 authenticated read-only E2E: PASS`, digest SHA-256 e `Comments complete: True`. Sem logs de PASS de uma execução real, **não declarar E2E concluído**.
