# GT47 T04 — Contrato de integração e aceite

**Missão:** GT-AI-DISPATCH-001 (#47). **Escopo desta PR:** preparação offline e fail-closed, sem ativação de agentes.

## Entregue

- Envelope determinístico, com identidade da missão e agente, hash SHA-256 do envelope e `execution_allowed=false`.
- Integridade Git blob dos textos de contrato e políticas, caminhos canônicos das três políticas, identidade de eventos e limites de volume.
- Seleção de comentários somente quando o chamador confirmar paginação completa; comentários são dados, não comandos ou autorizações.
- Testes de integridade, falsificação de origem, adulteração, duplicidade e paginação incompleta.

## Contrato obrigatório do futuro adaptador autenticado

1. Consultar GitHub com identidade autenticada e permissão somente de leitura; fixar commit SHA do repositório antes de obter arquivos.
2. Obter contrato e políticas pelo mesmo commit, reter caminho, texto UTF-8 e SHA de blob da API; falhar se qualquer fonte estiver ausente ou inconsistente.
3. Consultar comentários da issue #47 por páginas até o término confirmado; **não** usar `complete=True` sem prova de exaustão. O limite atual de 50 registros deve provocar rejeição, nunca truncamento silencioso.
4. Normalizar apenas `id`, `body`, `html_url` e rejeitar URL divergente. Não inferir autorização de linguagem natural dos comentários.
5. Aplicar verificação de autoridade humana separada, com identidade e decisão assinadas/verificáveis, escopo e revogação, antes de qualquer efeito externo.
6. Manter desligado o workflow sintético anteriormente desabilitado; não publicar, chamar LLM, disparar workflow ou fazer merge nesta fase.

## Critérios de aceite

- CI no HEAD com suíte Python completa aprovada.
- QA independente quando exigido pela política vigente; autocheck não substitui independência.
- Direção autoriza merge e qualquer ativação conforme alçadas vigentes.

**Não comprovado nesta PR:** autenticidade da resposta da API, prova real de paginação, autorização humana, disponibilidade/custo de provedor de IA ou execução cloud com computador desligado.

## Adaptador de leitura implementado (ainda não executado contra GitHub real)

- `scripts/gt47_t04_github_adapter.py`: consulta conteúdo por SHA fixado e comentários paginados, rejeitando origem inconsistente e volumes acima de 50.
- `scripts/gt47_t04_transport.py`: transporte HTTPS GET com token fornecido pelo chamador, domínio/repositório/endpoints permitidos, sem redirecionamento, com timeout e limite de resposta.
- O adaptador não possui agendamento, workflow ou execução automática; autenticação, integridade da resposta TLS, autorização da Direção e testes E2E reais continuam gates separados.
- **Atenção operacional:** a issue #47 pode ultrapassar 50 comentários; nesse caso a integração rejeita o histórico completo, exigindo estratégia aprovada de seleção e paginação sem perda de evidências antes do uso real.
