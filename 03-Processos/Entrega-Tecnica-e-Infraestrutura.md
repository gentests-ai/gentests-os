---
tipo: procedimento
id: PRC-ENG-001
versao: 0.1.1
status: proposta
responsavel: Engenharia e Infraestrutura
aprovador: Direcao
---
# PRC-ENG-001 — Entrega técnica e infraestrutura

## Finalidade e escopo
Estabelecer fluxo enxuto entre Produto, UX/UI, Engenharia, QA e Infraestrutura para alterações de código, scripts, automações e ambientes. Não comprova implantação de CI/CD nem autoriza operações em produção.

## Fluxo
1. **Receber e delimitar** — confirmar requisitos, aceite, origem, prioridade, ambiente, dependências, classificação QG e aprovações exigidas.
2. **Implementar em branch** — Engenharia faz mudança mínima e versionada, descrevendo impactos e riscos.
3. **Verificar** — aplicar testes apropriados e observabilidade; QA contribui na análise de riscos, testes e evidências; documentar testes não realizados.
4. **Revisar** — controles automáticos comprovadamente disponíveis e revisão por especialista independente quando exigida pelo nível de risco; o próprio autor não emite parecer independente.
5. **Deliberar** — autorização explícita da Direção para qualquer merge, implantação, acesso a produção, credenciais, despesas e demais operações sujeitas à matriz.
6. **Implantar e acompanhar** — Infraestrutura executa apenas operação autorizada, verifica estado posterior e mantém instruções de rollback; comunicar incidentes, resultados e limitações.

## Responsabilidades e interfaces
| Objeto | Responsável | Interface |
|---|---|---|
| Requisitos funcionais e priorização | Produto | UX/UI, QA, Engenharia |
| Interface e estados | UX/UI | Produto, Engenharia, QA |
| Implementação e correções | Engenharia | Produto, Infra, QA |
| Risco, prevenção e testes | QA | Engenharia, Produto, Infra |
| Ambiente, CI/CD e implantação autorizada | Infraestrutura | Engenharia, QA, Direção |
| Parecer independente, quando exigido | Especialista designado sem conflito | Validador, executor |
| Autorização sensível | Direção ou responsável formalmente autorizado | Orquestrador |

## Evidências mínimas
Identificador e versão, PR/commit, ambiente e permissões, requisitos atendidos, testes realmente executados, resultados e logs seguros, risco residual, aprovação exigida, confirmação da implantação se houve e possível plano de reversão.

## Falha e retrabalho
Falha ou ausência de evidência não equivale a aprovação. Corrigir apenas o escopo identificado; aplicar revalidação focal. Após duas rodadas automáticas malsucedidas, divergência crítica ou risco de segurança, interromper e escalar conforme [[00-Constituicao/SEC-AI-001-Seguranca-Confiabilidade-Agentes]].

## Controles e limites
- Os controles do GitHub, GitHub Actions e provedores de hospedagem devem ser verificados na configuração real antes de serem declarados ativos.
- Permissões da documentação não substituem permissões de tokens, contas, ambientes e branch protection.
- No acúmulo de Engenharia e Infra pelo mesmo agente, separar execução de autorização e revisão independente; não pressupor que existam duas pessoas.
- PR concluído não significa merge, implantação ou publicação.
- Integração com [[03-Processos/Ciclo-de-QA]] e [[00-Constituicao/Quality-Gates/QG-001-Politica]].

## Homologação
Documento em proposta; implantação dos controles e adoção obrigatória dependem de revisão e decisão da Direção.

## Reconciliação GOV-04
AGT-ENG/AGT-INFRA e o índice seguem a proposta canônica de #61, preservando IDs e caminhos. Executor é função genérica; Engenharia é o nome canônico do domínio. Orquestrador mantém fila/rota, sem autohandoff. Os cinco contratos e os 14 papéis não concedem privilégios; Modelo A permanece função por missão. POL-003/#53 são dependência separada, não alterada nesta reconciliação. #50 preserva fronteiras Comercial/Marketing; FIN-54-01 permanece com o responsável por #54. Sem homologação ou merge.
