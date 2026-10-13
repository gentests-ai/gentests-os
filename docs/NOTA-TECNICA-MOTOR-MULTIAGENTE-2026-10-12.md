# Nota técnica — avaliação de sugestões para o motor multiagente (12/10/2026)

**Status: nota consultiva, não normativa.** Esta nota não aprova políticas, concede permissões, ativa workflows ou declara funcionalidades implementadas. As sugestões abaixo foram confrontadas com a documentação e trechos de código existentes em `main`; requerem validação e decisão próprias antes de virar trabalho de implementação.

## Diagnóstico do piloto

O catálogo documenta 14 papéis; o piloto Groq GT47 opera apenas o fluxo de pareceres Engenharia → QA. Não confundir número de contratos com agentes executados. O teste de mesa manual é uma fonte útil de hipóteses e casos de teste sobre ambiguidades, handoffs, rigidez de prompts, desvios e limites de autonomia, **não** prova de conformidade ou de comportamento automático.

## Classificação

| Ideia | Parecer / posicionamento | Referência atual |
| --- | --- | --- |
| Cache da Constituição e dos contratos do vault | **Candidata, condicionada.** A leitura deve fixar commit/versão, verificar hash de blobs e invalidar cache quando as fontes mudarem; priorizar contexto mínimo por agente. Dentro de um único runner pode-se memorizar parsing imutável, sem comprometer verificações de integridade. Cache entre runs requer persistência verificável e política de invalidação; não presumir que o runner efêmero mantém arquivos. O gargalo potencial tende a ser chamadas externas/contexto de LLM, não leitura de Markdown pequeno, até medições provarem o contrário. | `scripts/gt47_t04_context_loader.py`; `docs/GT47-T04-CONTEXT-INTEGRATION.md` |
| Limite de loops de agentes | **Controle importante; não copiar o exemplo de cinco iterações.** SEC-AI-001 já propõe **máximo de duas rodadas automáticas de correção**, com escalonamento em persistência de erro. Distinguir profundidade de handoffs, número de correções, tentativas do provedor, tempo, tokens e orçamento por missão. Recomendar teste de ciclos A→B→A e encerramento determinístico, sem novos retries automáticos no piloto atual. | `00-Constituicao/SEC-AI-001-Seguranca-Confiabilidade-Agentes.md`; `docs/GT47-GROQ-ADVISORY.md` |
| Métricas de desvios comportamentais | **Candidata útil**, usando o registro canônico de incidentes/RNC e indicadores; não criar um banco de auditoria paralelo no Obsidian por padrão. Registrar missão, agente/contrato e versões, categoria de desvio, criticidade, origem, evidência minimizada, decisão e desfecho. Proteger segredos/dados sensíveis; distinguir inferência de evidência observada. | `03-Processos/Gestao-de-Nao-Conformidades.md`; `06-Indicadores/Indicadores-de-Governanca.md` |
| Flexibilizar prompts para evitar literalismo | **Aplicar só a orientações operacionais não críticas.** Tornar precedência e critérios de exceção explícitos; jamais dizer genericamente para priorizar o objetivo sobre qualquer regra. Segurança, autorização, separação de papéis e validação prevalecem. | `00-Constituicao/Hierarquia-e-Conflitos.md`; `SEC-AI-001` |
| Autonomia documental de Processos | **Já prevista parcialmente.** AGT-PROC admite edição operacional simples em branch isolada dentro de escopo e permissão efetiva; não admite autoaprovação de contratos, políticas ou privilégios. Não ampliar a autonomia por analogia. | `02-Agentes/Processos/Contrato-Agente-Processos.md` |
| Processos como middleware que reescreve regras em caso de erro | **Não adotar literalmente.** Resposta inválida deve gerar validação estrutural, diagnóstico, bloqueio/encaminhamento ou correção focal permitida. Alterações em instruções normativas não são tratamento automático de exceção; dependem de revisão/autoridade pertinente. | `SEC-AI-001`; `GT-HANDOFF-001` |
| Máquina de estados | **Alinhada ao desenho atual; aprofundamento eventual.** Preservar eventos e transições distintos de preparo, transporte, aceite, execução, verificação, autorização e encerramento. O piloto já usa `engineering_pending → qa_pending → completed`, mas `completed` de pareceres não equivale a execução ou deploy. Modelar transições de exceção/ciclo com gates explícitos antes de expansão dos 14 papéis. | `03-Processos/Encaminhamento-de-Missoes-GT-HANDOFF-001.md`; `docs/GT47-AUTOMATIC-DEMAND-OUTCOME.md` |
| SQLite / DuckDB | **SQLite parcialmente existente em protótipo offline**, não banco persistente implantado para os 14 agentes. Em GitHub Actions o disco do runner é efêmero; persistência requer destino durável e concorrência controlada. DuckDB é hipótese para análise, não escolha necessária de estado transacional. | `scripts/gt47_t06_claim_store.py`; `docs/GT47-GROQ-ADVISORY.md` |
| Webhooks serverless | **Hipótese futura**, condicionada a requisitos de latência, autenticação, idempotência, limites e custo real do plano. O mock Cloudflare não prova operação produtiva. | `docs/GT-AI-DISPATCH-001-T05-CLOUDFLARE-MOCK.md` |
| Kafka/RabbitMQ | **Nota de longo prazo, sem compromisso.** Só avaliar quando métricas demonstrarem volume, durabilidade, fan-out e throughput incompatíveis com solução mais simples. Há custos operacionais e risco de complexidade prematura. | Roadmap exploratório |
| Painel de personalidades pelo cliente | **Hipótese de produto**, sujeita a isolamento por cliente, versionamento, políticas não editáveis, verificação de permissões e risco de prompt injection. Upload de documentação não concede autoridade. | `02-Agentes/Indice-de-Agentes.md`; `SEC-AI-001` |

## Critérios objetivos para evolução

1. Medir custo por missão, duração do runner, chamadas/tokens reservados, rejeições, duplicidades, profundidade de handoff, rodadas de correção, escalonamentos e taxa de conclusão.
2. Acrescentar testes offline de rotas circulares, contexto obsoleto, mudança de hash, falha da governança, erro de formato, replay e queda depois da reserva de orçamento.
3. Preservar orçamento, idempotência, `fail-closed`, separação entre parecer e autoridade, e limites de correção documentados. Não habilitar retries externos para testar loops.
4. Priorizar mudanças pequenas, reversíveis e comprovadamente necessárias; registrar proposta e decisão separadamente.
5. Confirmar limites de cotas e possíveis cobranças com cada provedor; “custo zero” é objetivo do piloto, não garantia universal.

## Referência metodológica: teste de mesa manual

Documentar, para cada cenário reproduzível: objetivo, papéis envolvidos, versões dos prompts, passagem esperada, passagem observada, interpretação literal problemática, quantidade de voltas, resolução humana e hipótese de melhoria. Converter achados em casos de teste automatizados quando possível. Não inferir dos testes manuais que a integração de todos os agentes já funciona.

**Conclusão:** o caminho de menor risco é ampliar progressivamente os controles e a máquina de estados existentes. Não introduzir uma segunda governança, um segundo repositório canônico ou uma tecnologia de filas antes de evidência operacional que a justifique.
