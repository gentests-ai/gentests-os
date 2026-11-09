---
tipo: procedimento
id: PRC-ENG-001
versao: 0.1.3
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

## Sequência progressiva de evidências — esclarecimento operacional proposto

**Aplicação:** ao piloto sintético [GT-AI-DISPATCH-001 #47](https://github.com/gentestsai-sudo/gentests-os/issues/47) e, por analogia, a atividades reversíveis proporcionais ao risco. Este trecho **não altera POL-003, QG-001, SEC-AI-001, GT-HANDOFF-001, autoridades, exigências de aprovação nem permissões efetivas**. Os quatro momentos abaixo são pontos de verificação do trabalho, **não quatro autorizações humanas automáticas**. Atos protegidos continuam sujeitos às decisões específicas da Direção e aos controles aplicáveis.

| Momento progressivo | Evidência já exigível | Evidência que só pode surgir depois | Saída sem presunções |
|---|---|---|---|
| **1. Prontidão para criação** | Recursos exatos, finalidade, principal responsável, decisão humana de escopo, menor privilégio projetado, conta/plano conhecido, teto de custo incremental permitido, restrição de dados, termos/risco preliminares e plano de falha segura/rollback. Risco sem controle verificável: NO-GO. | IDs de recursos inexistentes, quotas usadas pelos recursos novos, observação de revogação ou logs de execução ainda não criada. | Proposta específica de criação para deliberação da Direção; sem autorização, permanece bloqueada. |
| **2. Construção controlada** | Somente após autorização específica para cada recurso/configuração: verificar previamente os requisitos de segurança, privacidade e custo aplicáveis a cada ato de criação ou configuração autorizado; comprovar estado, identidade, ACL, fail-closed e limites observáveis após a configuração e antes da exposição ou primeira invocação operacional, especialmente de IA, sem dispensar autorização específica para deploy ou uso. | Resultados de inferência real, teste de comportamento da chamada e custo medido da operação ainda não autorizada. | Evidências de configuração e condições para solicitar a autorização seguinte; se recurso não puder garantir R$0/segurança, parar e redesenhar. |
| **3. Execução e teste real** | **Somente após autorização própria** de deploy/uso, ambiente elegível, controles reais suficientes de custo, dados, revogação e negação segura; fixtures sintéticas quando exigidas. | Logs sanitizados, medição real, testes de replay/negação/timeout e resultados operacionais do ato agora autorizado. | QA executa testes autorizados e relata falhas/limites; execução não implica publicação. |
| **4. Validação e decisão** | Diferença material, testes e evidências existentes, risco residual, revisor distinto quando gate aplicável exigir, autorizações e DoD do objeto. | Prova de efeitos externos não ocorridos permanece N/A/bloqueada, nunca inventada. | Validação focal e decisão reservada à Direção quando aplicável; missão só encerra após critérios efetivos. |

**Anticírculo:** não exigir como pré-requisito para *autorizar a criação* uma medição que depende de *executar o recurso ainda inexistente*. Em contrapartida, não dispensar prova prévia sobre elegibilidade, não cobrança e segurança para a criação, nem liberar a chamada real sem controles efetivos e aprovação específica. Impossibilidade de provar trava obrigatória implica **NO-GO** ou alternativa offline; não autorização por omissão.

**Reuso e comunicação:** referenciar parecer/QA já válidos pelo ID, versão, escopo e evidência; abrir nova análise somente com mudança material, falha ou dúvida relevante. Handoff integral GT-HANDOFF-001 apenas quando houver transferência real de responsabilidade ou retorno exigido; trabalho simples no mesmo escopo/owner pode registrar o resultado na issue/PR sem simular entrega entre chats. Registro, transporte, recebimento, ACEITO, execução, validação e autorização são eventos diferentes. O responsável atual mantém ownership até o aceite explícito do destinatário; depois, o destinatário assume a execução. O Scrum Master atua por exceção em impedimentos e conflitos, sem preservar fila central ou designar o próximo dono. Etapa documental concluída não declara o sistema funcional.

### Aplicação focal, sem repetir testes

- **#47 / T03→T04→T05:** GOV-10 [#6117050550](https://github.com/gentestsai-sudo/gentests-os/issues/47#issuecomment-6117050550), ENG-12 [#6117174642](https://github.com/gentestsai-sudo/gentests-os/issues/47#issuecomment-6117174642), INFRA-05 [#6117439942](https://github.com/gentestsai-sudo/gentests-os/issues/47#issuecomment-6117439942) e T04 [#6117494069](https://github.com/gentestsai-sudo/gentests-os/issues/47#issuecomment-6117494069) já fornecem planejamento e lacunas. G3 [PR #68](https://github.com/gentestsai-sudo/gentests-os/pull/68) comprovou apenas execução **offline**. T03 é **parcial**, G4 criação/deploy/inferência **não autorizados** e T05 real bloqueado. Próxima atividade útil: montar decisão de criação com recursos/identidades/controles pré-criação verificáveis; contas/termos/custo não comprováveis mantêm NO-GO ou levam a redesenho, **sem repetir pareceres**. Após eventual autorização distinta de criação, colher evidência de configuração; somente depois deliberar execução/teste real.
- **Documento interno reversível (QG-L se efetivamente classificado assim):** Processos recebe texto/link incorreto em procedimento sem alteração de autoridade/controle, confere versão e PR concorrente, edita em branch isolada, verifica diff e links, abre PR documental e registra a evidência na issue canônica para o responsável e os verificadores pertinentes. **Não** exige handoff para Engenharia só para editar Markdown, nem QA funcional ou quatro gates de infraestrutura. Revisão proporcional e autorização da Direção para merge continuam aplicáveis; autocheck não é revisão independente.

**Verificação desta proposta:** estes dois percursos são **simulações documentais de aplicação do fluxo**, não ensaios cloud, QA funcional, comprovação de economia de tempo nem homologação normativa. Responsáveis atuais/seguintes seguem registro vigente na issue e autorizações específicas, não este texto.

## Responsabilidades e interfaces
| Objeto | Responsável | Interface |
|---|---|---|
| Requisitos funcionais e priorização | Produto | UX/UI, QA, Engenharia |
| Interface e estados | UX/UI | Produto, Engenharia, QA |
| Implementação e correções | Engenharia | Produto, Infra, QA |
| Risco, prevenção e testes | QA | Engenharia, Produto, Infra |
| Ambiente, CI/CD e implantação autorizada | Infraestrutura | Engenharia, QA, Direção |
| Parecer independente, quando exigido | Especialista designado sem conflito | Validador, executor |
| Autorização sensível | Direção ou responsável formalmente autorizado | Scrum Master apenas acompanha impedimentos por exceção; não autoriza nem despacha |

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
AGT-ENG/AGT-INFRA e o índice seguem a proposta canônica de #61, preservando IDs e caminhos. Executor é função genérica; Engenharia é o nome canônico do domínio. Não existe ownership global, fila central ou rota obrigatória por Orquestrador. O Scrum Master atua por exceção e não substitui especialistas. Os cinco contratos e os 14 papéis não concedem privilégios; Modelo A permanece função por missão. POL-003/#53 são dependência separada, não alterada nesta reconciliação. #50 preserva fronteiras Comercial/Marketing; FIN-54-01 permanece com o responsável por #54. Sem homologação ou merge.
