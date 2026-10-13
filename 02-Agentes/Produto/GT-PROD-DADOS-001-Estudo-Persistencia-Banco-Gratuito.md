---
tipo: estudo-tecnico
id: GT-PROD-DADOS-001
versao: 0.1.0
status: estudo-nao-aprovado
responsavel: Produto
consultados: [Engenharia, Infraestrutura, Seguranca, QA, UX]
aprovador: Direcao
data: 2026-10-13
---
# GT-PROD-DADOS-001 — Estudo de persistência e banco de dados gratuito

## 1. Contexto
A Gen.Tools utiliza atualmente GitHub (issues, labels, Actions, repositórios e histórico) e documentação editada via Obsidian/versionada no repositório. A interface responsiva/PWA prevista deve inicialmente administrar agentes e demandas existentes, mas ser configurável para equipes de tamanhos variados e permitir, numa fase posterior, a criação/edição de agentes pela própria interface. A API do motor pode futuramente ser oferecida separadamente.

**Objeto deste documento:** registrar alternativas e critérios para evolução da persistência, sem escolher fornecedor, mudar fluxos, criar banco ou autorizar implantação.

## 2. Hipótese principal
**Não implantar banco externo apenas para disponibilizar a V1 de leitura da interface.** Primeiro levantar necessidades concretas, limitações das APIs do GitHub, custo de consultas, consistência, tempo de resposta e segurança. A V1 pode usar uma API Python que consulta/projeta as fontes existentes, desde que observadas as limitações técnicas. Preservar desde já uma abstração de persistência no motor para permitir introdução de banco sem refazer a UI.

GitHub Issues é fonte canônica de demandas, conforme arquitetura proposta GT-PROD-REPOS-001; **GitHub Actions não deve ser presumido banco transacional de estado operacional**. A definição da futura fonte de verdade de estados de execução exige decisão de Engenharia.

## 3. Distribuição preliminar de dados
| Categoria | Fonte inicial / proposta | Observação |
| --- | --- | --- |
| Constituição, contratos, regras, prompts versionados | Git/repositório + edição documental pelo Obsidian | Referenciar SHA/versão por execução; não replicar autoridade no banco |
| Issues, PRs, labels, evidências associadas | GitHub | Preservar IDs e URL canônica |
| Cadastro e metadados de agentes | Inicialmente manifestos/documentação; banco futuro se necessário | Separar identidade de versão das instruções e permissões |
| Configuração por organização e relacionamentos | Persistência futura | Planejar identificadores de organização/usuário/agente |
| Estado, transições, tentativas, filas e eventos | Definição pendente de Engenharia | Idempotência, concorrência, rastreabilidade e reconciliação |
| Consultas, projeções e indicadores | API com dados derivados; armazenamento futuro conforme volume | Indicar cobertura, origem e instante da última sincronização |
| Segredos/API keys | Gerenciador de segredos | Nunca registrar credenciais em claro em Git, logs ou tabelas comuns |

## 4. Alternativas para estudo
- **Sem banco novo (GitHub + documentação):** menor complexidade e custo imediato; limitações de latência, rate limits e consulta/consistência.
- **PostgreSQL gerenciado gratuito (ex.: Neon ou Supabase):** relacional, compatível com Python e portável entre provedores; verificar cotas, suspensão, backups, limites de conexão, retenção, SLA e condições vigentes antes de decidir.
- **SQLite/local ou serviço compatível (ex.: Turso):** alternativa leve, especialmente em instalações isoladas; validar concorrência, persistência durável entre execuções e operação distribuída.
- **Cloudflare D1:** opção SQL gerenciada, com modelo e integração próprios; avaliar cotas e adequação ao runtime Python.
Não assumir gratuidade permanente ou ausência de cobrança por excedentes; confirmar preços e termos oficiais na data de contratação.

## 5. Diretrizes arquiteturais propostas
1. API Python como fronteira para interface e consumidores externos; não expor tokens GitHub nem credenciais do provedor ao navegador.
2. Camada de acesso à persistência desacoplada do fornecedor (interfaces/adaptadores); separar leituras/projeções de comandos.
3. Uma fonte canônica por informação e estratégia explícita de sincronização/reconciliação; evitar estados paralelos painel/runtime.
4. Preparar IDs estáveis de organização, usuário, agente, demanda e rodada; autorização e isolamento entre clientes (multi-tenant) deverão ser testados antes de uso comercial.
5. Na V1, usar visualização dinâmica de agentes; na V2, prever criação/edição por UI mediante autorização no backend, validação de contratos, versionamento e auditoria.
6. API comercial não é mero endpoint interno: requer autenticação, escopos, quotas, documentação, versionamento, observabilidade, proteção de dados e política de suporte.
7. Considerar exportação/migração para banco do próprio cliente sem dependência obrigatória de um serviço específico.
8. Não ativar ações de escrita na UI sem desenho e aprovação de permissões e governança.

## 6. Gatilhos para reavaliar banco
- Necessidade de consultas, filtros, histórico e indicadores sem percorrer muitas issues/logs.
- Alterações frequentes de cadastro/configurações pela interface.
- Concorrência, transações, eventos e reprocessamentos não atendidos adequadamente pelas fontes atuais.
- Multi-organização, controle de acesso, isolamento e requisitos comerciais/contratuais.
- Latência, custo ou limites de GitHub API incompatíveis com a experiência proposta.

## 7. Proposta de fases
**Fase 0 — diagnóstico:** inventário das fontes atuais e medições do caminho feliz, volumes, frequência, latência, limites, falhas e recuperação.

**Fase 1 — interface somente leitura:** API Python/adaptadores para GitHub e dados documentais; UI responsiva/PWA com origem, atualização, erros e cobertura visíveis. Alinhar à proposta GT-MISSION-CONTROL-001, sem presumir aprovação dela.

**Fase 2 — persistência operacional (se justificada):** prova de conceito PostgreSQL e alternativas, migração incremental, reconciliação, backup/restauração, observabilidade e rollback.

**Fase 3 — gestão dinâmica e comercialização:** criação e edição autorizada de agentes, multi-tenant, API externa documentada e opção de banco configurável, mediante análise de segurança e produto.

## 8. Critérios de comparação e validação
Comparar: custo total e limites grátis; duração/política do plano; operação Python/Actions; latência; concorrência/transações; backups e restauração; portabilidade; segurança/segredos; segregação entre clientes; migração; observabilidade; disponibilidade; conformidade de dados.

**Ensaios mínimos antes de adoção:** criação/consulta/atualização concorrente; reenvio idempotente; falha de conexão; recuperação e reconciliação; restauração de backup; acesso entre organizações negado; medição de quotas e latência. Nenhum ensaio foi executado nesta nota.

## 9. Riscos e decisões pendentes
- Risco: GitHub como banco transacional ou canal de consultas intensivas → limitar escopo V1 e medir uso.
- Risco: duplicação/divergência de estado → fonte canônica e reconciliação.
- Risco: custo inesperado de plano gratuito → alertas, limites e validação contratual.
- Risco: exposição de dados/segredos → controle de acesso no servidor e revisão de Segurança.
- Risco: acoplamento a fornecedor → adaptadores e plano de migração.
- **Pendente Produto/UX:** atributos e ações essenciais do painel, navegação para 5/15/50+ agentes.
- **Pendente Engenharia:** eventos/estado canônicos, contrato da API, modelo de dados, estratégia de consistência.
- **Pendente Infra/Segurança:** opções de hospedagem, backups, credenciais, isolamento e custos.
- **Pendente QA:** testes de falha, dados inconsistentes, concorrência, idempotência e migração.
- **Pendente Direção:** qualquer adoção/implantação e investimento.

## 10. Referências internas
- [GT-PROD-REPOS-001 — Arquitetura de repositórios](GT-PROD-REPOS-001-Arquitetura-Repositorios.md)
- [PRC-PROD-001 — Refinamento Produto, UX/UI, Engenharia e QA](../../03-Processos/Refinamento-Produto-UX-Handoff.md)
- [GT-MISSION-CONTROL-001 — Proposta UX/UI](../../produtos/GT-MISSION-CONTROL-001/UX-Proposta-001/UX-Especificacao-v0.1.0.md)

**Natureza:** estudo inicial não homologado. Não altera Constituição, permissões, workflows, infraestrutura ou fontes canônicas existentes.
