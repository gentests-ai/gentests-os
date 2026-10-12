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
