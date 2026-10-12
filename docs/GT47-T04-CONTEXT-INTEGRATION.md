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
3. Consultar comentários da issue #47 por páginas até o término confirmado; **não** usar `complete=True` sem prova de exaustão. Selecionar explicitamente os 50 comentários mais recentes somente **após** concluir a paginação; preservar a contagem/histórico canônico no GitHub, sem tratar o recorte como histórico completo.
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
- **Atenção operacional:** a issue #47 possui mais de 50 comentários; o adaptador pagina o histórico e fornece apenas os 50 mais recentes ao envelope. Comentários antigos continuam no GitHub, mas não entram no contexto resumido; decisões e autorizações exigem fontes canônicas independentes do recorte.

## Resposta ao parecer QA/GOV da PR #92

A leitura completa agora rejeita IDs repetidos ou fora de ordem entre páginas, e retorna proveniência (quantidade consultada, primeiro/último ID, páginas e completude). O `fetch_context` incorpora a proveniência e o commit de referência no hash final do envelope. Testes negativos cobrem duplicidade entre páginas. A coleta por offset **não é snapshot transacional**; inclusões concorrentes no GitHub podem escapar à leitura, mesmo com páginas ordenadas. Antes do uso em produção, é necessário mecanismo de consistência/snapshot verificável ou aceitar formalmente janela eventual sem usar comentários como fonte de autorização. O parecer `ADEQUADO COM AJUSTES` não é aprovação de merge.

## Estratégia de consistência do contexto offline

A seleção é **eventualmente consistente**, não um snapshot transacional: lê todas as páginas, exige término observado, IDs estritamente crescentes e únicos, rejeita comentários vazios e mantém apenas os 50 mais recentes. Inserções que deslocam páginas e geram sobreposição são detectadas; inserções concorrentes sem sobreposição podem passar despercebidas. Portanto, `complete=True` significa somente exaustão observada da leitura. Nenhuma decisão normativa, autorização de merge ou comando operacional pode depender desse recorte. Para execução externa, obter decisões canônicas diretamente de fonte autorizada com versão/identidade verificadas e política de revalidação, não dos comentários selecionados.
