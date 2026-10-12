---
tipo: especificacao-produto
id: GT-PROD-REPOS-001
versao: 0.1.0
status: proposta
responsavel: AGT-PROD
aprovador: Direcao
data: 2026-10-12
---
# GT-PROD-REPOS-001 — Arquitetura de repositórios GenTests.ai

## 1. Objetivo e decisão proposta
Separar governança institucional, motor de execução e entregas dos produtos, preservando rastreabilidade e permitindo migração incremental do piloto atual. **Esta especificação não autoriza criação de repositórios, extração de código ou deploy.** A aprovação compete à Direção após consulta a Engenharia, Infraestrutura, QA e Segurança.

Princípio: **a empresa define as regras; o runtime executa o fluxo; os produtos recebem as entregas**.

## 2. Fronteiras de responsabilidade

| Repositório | Responsabilidade | Contém | Não deve conter |
| --- | --- | --- | --- |
| `gentests-os` | Fonte de verdade institucional | Constituição, contratos de agentes, papéis, processos, políticas, modelos de demanda, decisões homologadas | Motor operacional de longo prazo, deploy dos produtos |
| `gentests-agent-runtime` (futuro) | Fonte de verdade operacional da execução | Ingestão e roteamento, estado das rodadas, histórico de transições, orçamento, reservas, evidências e adaptadores | Regras institucionais canônicas ou código específico dos produtos |
| `gentests-<produto>` | Fonte de verdade do artefato entregue | Código, testes, pipelines, documentação técnica e releases do produto | Orquestração corporativa e políticas institucionais duplicadas |
| `gentests-panel` (opcional) | Interface de visualização/controle | UI, testes, cliente de API e deploy do painel | Banco de estados paralelo ao runtime |

O painel lê projeções e eventos disponibilizados pelo runtime; comandos autorizados são encaminhados à API do runtime. Não se pressupõe que o painel já exista como repositório independente.

## 3. Organização proposta
```text
gentests-os/
  00-Constituicao/
  01-Empresa/
  02-Agentes/
    Produto/
      Contrato-Agente-Produto.md
      GT-PROD-REPOS-001-Arquitetura-Repositorios.md
  03-Processos/
  09-Backlog/                 # legado/transição; demandas novas em Issues
  produtos/                   # descobertas históricas; não migrar sem inventário
  ...                         # preservar estrutura atual até decisão específica

gentests-agent-runtime/       # somente após validação do piloto
  src/
    intake/
    orchestration/
    execution/
    budget/
    persistence/
    integrations/
    api/
  tests/
  migrations/
  docs/
  .github/workflows/

gentests-<produto>/
  src/
  tests/
  docs/
  .github/workflows/
```
A árvore dos futuros repositórios é ilustrativa, sujeita à decisão técnica de Engenharia. Não renomear ou mover pastas atuais nesta demanda.

## 4. Demandas, IDs e rastreabilidade
- A **Issue canônica** da demanda fica no repositório responsável pela entrega: política/contrato no `gentests-os`, motor no runtime, funcionalidade no repositório do produto.
- Toda demanda recebe um `demand_id` global, imutável, independente do número local da Issue; usar identificador único gerado pelo serviço responsável, com verificação de colisão e idempotência.
- Registrar `demand_id`, `source_repo`, `source_issue_number`, `source_issue_url`, `owner_repo`, `run_id`, `agent_id`, `agent_definitions_commit_sha`, `status`, `timestamps`, `evidence_refs`, `cost` e `reservation_refs` conforme aplicabilidade.
- Uma demanda pode gerar múltiplas rodadas; cada rodada possui `run_id` próprio e referencia a mesma demanda. A Issue representa trabalho; o runtime registra encaminhamentos, tentativas, estados e resultados. Links para PRs e artefatos são associados ao mesmo ID.
- Mudança de repositório responsável exige evento auditável de transferência, referência cruzada e preservação do ID; não duplicar Issue ativa sem relação explícita.
- A versão das definições dos agentes é fixada no início de cada rodada por SHA do `gentests-os` (e, se necessário, hashes de contratos/manifestos). Não reinterpretar rodadas históricas com regras posteriores.
- Eventos devem ser persistidos com controle de concorrência, idempotência e rastreabilidade. Formato, armazenamento, retenção e política de acesso dependem de validação técnica e de segurança.

## 5. Escopo e exclusões
**Inclui:** arquitetura-alvo lógica, responsabilidades, modelo mínimo de rastreabilidade, plano gradual, critérios de aceite e decisões pendentes.

**Exclui:** criação dos novos repositórios, migração física, mudanças em workflows existentes, alteração de permissões, custos ou deploy, transferência automática de Issues, implementação do painel e homologação de políticas.

## 6. Plano incremental
1. **Inventário e linha de base:** mapear código do piloto, workflows, testes, dependências, contratos, Issues, PRs, evidências, reservas e estados persistidos. Registrar SHA e referências de origem.
2. **Validar caminho feliz no repositório atual:** entrada da Issue → encaminhamento → execução controlada → evidência → resultado persistido → consulta, com ID único e versão de definições registrada.
3. **Definir contratos de extração:** eventos, API, persistência, identidade, permissões, orçamento, compatibilidade e estratégia de rollback. Engenharia/Infra/QA/Security avaliam.
4. **Extrair por fatias para `gentests-agent-runtime`:** migrar componentes somente após testes de equivalência e aprovação; manter referências cruzadas de histórico, reservas e evidências; não reescrever fatos históricos.
5. **Separar produtos quando houver necessidade real:** mover código/testes/deploy específicos, preservar vínculos de PRs, commits, Issues e releases; configurar observabilidade e ownership.
6. **Painel:** consumir API/projeções do runtime sem criar uma segunda fonte de estado; validar reconciliação e permissões.
7. **Desativar legado apenas com evidência:** verificar integridade, reversibilidade e autorização antes de remover caminhos antigos.

## 7. Critérios de aceite testáveis
- **CA-01:** documento distingue explicitamente fonte institucional, operacional e de entrega, sem responsabilidades conflitantes.
- **CA-02:** demanda criada em qualquer repositório responsável tem `demand_id` único e ligação verificável com a Issue canônica.
- **CA-03:** duas rodadas da mesma demanda têm `run_id` diferentes e preservam seus próprios SHA de definições.
- **CA-04:** consulta do painel e consulta do runtime retornam o mesmo estado canônico para uma rodada concluída ou em andamento, dentro de latência definida pela Engenharia.
- **CA-05:** repetição de webhook/comando não duplica execução, reserva nem cobrança indevidamente; resultado de idempotência é auditável.
- **CA-06:** piloto passa pelo caminho feliz antes de qualquer extração, com logs e evidências verificáveis.
- **CA-07:** extração demonstra reconciliação de histórico, reservas e evidências, com plano de rollback testado.
- **CA-08:** mudanças institucionais não alteram retroativamente a versão usada por execuções anteriores.
- **CA-09:** nenhuma migração ou publicação ocorre sem autorização da Direção e gates aplicáveis.

Os CA-02 a CA-09 são critérios para fases futuras, **não testes executados nesta entrega documental**.

## 8. Riscos e mitigação
| Risco | Mitigação proposta |
| --- | --- |
| Perda de histórico ou evidências | Inventário, IDs estáveis, referências cruzadas, backups, reconciliação e rollback |
| Divergência entre regras e execução | Pinning de SHA por rodada e manifesto de definições |
| Duplo estado painel/runtime | Runtime canônico; painel somente consulta/projeta |
| Duplicação de demandas ou cobranças | Chaves de idempotência e eventos auditáveis |
| Quebra do piloto durante migração | Extração em fatias com testes de equivalência e possibilidade de retorno |
| Acesso indevido a logs, reservas e custos | Revisão de permissões, minimização e retenção por Segurança/Infra |

## 9. Dependências, hipóteses e decisões pendentes
- **Hipótese:** GitHub Issues é adequado como entrada canônica de trabalho, não como armazenamento transacional de execução.
- **Pendente Engenharia:** estrutura física do runtime, contrato de eventos/API, esquema de IDs, armazenamento e consistência.
- **Pendente Infraestrutura/Segurança:** credenciais entre repositórios, proteção de branches, ambientes, segredos, retenção e permissões.
- **Pendente QA:** plano de testes do caminho feliz, falhas, duplicidades, recuperação e reconciliação.
- **Pendente Direção:** homologar fronteiras, autorizar criação de repositórios e aprovar cada fase de migração.

## 10. Handoff e referências
Produto mantém coerência funcional e rastreabilidade. Engenharia define viabilidade e arquitetura executável; QA avalia riscos e testabilidade; Infraestrutura e Segurança avaliam operação e acessos; Direção decide sobre implementação e escopo.

Referências: [AGT-PROD](Contrato-Agente-Produto.md), [PRC-PROD-001](../../03-Processos/Refinamento-Produto-UX-Handoff.md), [Matriz de Permissões](../../00-Constituicao/Matriz-de-Permissoes.md), [QG-001](../../00-Constituicao/Quality-Gates/QG-001-Politica.md).

**Estado da entrega:** proposta documental; nenhuma validação funcional, revisão independente ou aprovação institucional é alegada.
