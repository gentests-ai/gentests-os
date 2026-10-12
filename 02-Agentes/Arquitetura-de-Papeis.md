---
tipo: proposta-organizacional
id: GT-ORG-REFORM-001
versao: 0.1.3
status: proposta
---
# Reformulação da estrutura de agentes

## Objetivo e autoridade
Reformular funções por responsabilidade futura, independentemente da distribuição histórica de atividades, conforme instrução direta da Direção em 11/10/2026. Preservar registros anteriores. Este pacote é proposta documental: não ativa agentes, não altera permissões e não autoriza merge.

## Estrutura
Direção decide estratégia e atos reservados. Um Scrum Master (AGT-ORQ, nome anterior: Orquestrador Central) facilita o fluxo das missões sem chefiar especialistas nem aprovar encaminhamentos horizontais. Especialistas respondem por entregas do domínio. Governança e Processos têm funções transversais distintas. QA, Validador, Auditor e X9 mantêm fronteiras de controle próprias. Revisão Independente é função atribuída a especialista por missão (Modelo A), não agente permanente.

## Fronteiras e roteamento
| Pergunta ou objeto | Responsável primário | Limite |
|---|---|---|
| Quem facilita dependências, bloqueios e transparência da prioridade autorizada? | Scrum Master (AGT-ORQ) | Não decide mérito especializado nem aprova rota horizontal |
| O que o produto deve fazer? | Produto | Não autoriza implantação |
| Como a pessoa usa e entende a interface? | UX/UI | Não redefine negócio unilateralmente |
| Como implementar/corrigir software? | Engenharia | Não homologa a própria entrega |
| Como preparar/operar o ambiente? | Infraestrutura | Não amplia acesso nem contrata |
| Quais regras, autoridades e controles se aplicam? | Governança | Propõe; Direção homologa |
| Como executar o trabalho sob essas regras? | Processos | Não cria autoridade por procedimento |
| O comportamento atende aos requisitos? | QA | Testa e evidencia; não autoriza merge |
| As evidências satisfazem os critérios/gates nomeados? | Validador | Não altera o original que valida |
| Os controles foram respeitados e são efetivos? | Auditor | Não audita a própria produção |
| Há sinais de inconsistência documental? | X9 | Alerta provisório; não prova defeito por heurística |
| A entrega suporta avaliação crítica sem participação do autor? | Especialista na função de Revisor Independente | Não é segunda identidade humana presumida |

QA não precisa ser repetido pelo Validador: este reaproveita evidências suficientes e aponta somente lacunas relevantes. Auditoria é proporcional ao risco e não é etapa automática de toda entrega. X9 não absorve Auditoria. Processos não absorve Governança. Coordenação não substitui especialização.

## Nomes canônicos e aliases
| Nome anterior ou variante | Tratamento proposto |
|---|---|
| Executor Técnico, Executor de Software, Executor do Site | Engenharia (AGT-ENG), com site/software como escopo da missão |
| Infra, DevOps, Infraestrutura e DevOps | Infraestrutura (AGT-INFRA) |
| Orquestrador, Orquestrador Central | Scrum Master (AGT-ORQ), mesmo ID; aliases históricos preservados |
| Auditoria, Auditor | Auditor (AGT-AUD) |
| Validação, Validador | Validador (AGT-VAL) |
| Governança, agente de governança | Governança (AGT-GOV) |
| Processos, agente de processos | Processos (AGT-PROC) |
| Revisor Independente, Revisão Técnica independente | Função Modelo A atribuída por missão; revisar compatibilidade real |
| Agile Coach | Candidato de análise de fluxo; não incluído como agente ativo por este pacote |

“Executor” isolado é a função de quem produz a entrega, não sinônimo universal de Engenharia: Marketing executa conteúdo, Processos executa desenho de procedimento etc. Aliases preservam busca e rastreabilidade; não renomear históricos em massa. Chats de atividade são contexto, não novos agentes.

## Concorrência e impacto
- Issue #53: dona da reconciliação da matriz de permissões; este pacote não modifica POL-003. Inventariar os 14 papéis e Modelo A na proposta de #53 antes de adoção operacional.
- PR #52: já propõe AGT-ENG e AGT-INFRA. Preservados IDs e caminhos de arquivos para evitar contratos concorrentes. A nova proposta reformula esses textos; integrar uma versão única, nunca ambas sem reconciliação.
- PR #54: preservar escopo e restrições Financeiro; índice tem concorrência.
- PR #50: preservar responsabilidades Comercial/Marketing; reconciliar interfaces semânticas (sem alteração do índice no diff atual de #50), sem reescrever seus contratos aqui.
- PR #51 incorporado: preservar Produto/UX/UI e seus IDs. Sem regressão de requisitos.
- Issue #55 / GT-HANDOFF-001: aproveitar interfaces e distinguir propostas de homologação; contratos não ativam WIP, Agile Coach ou automação #47.
- Sem alteração de políticas, processos de domínio existentes, código, infraestrutura, histórico, permissões ou automações.

## Adoção e critérios de aceite
1. Cada papel tem nome/ID/contrato único e fronteira explícita.
2. Cinco contratos possuem entrada, DoR, execução, entrega, DoD, encaminhamento, devolução, escalonamento e limites.
3. Índice inclui Validador/X9 e distingue função de revisão independente.
4. Reconciliar diff de #52/#54/#50 e POL-003 em #53 antes de integrar; Orquestrador confirma integrador e sequência, Direção autoriza merge.
5. Revisão focal por autor distinto e decisão da Direção; sem alegação de independência humana baseada em chats.
6. Atualizar contratos antigos afetados somente com proposta específica revisável: este pacote delimita fronteiras, mas não declara esses textos já reconciliados.
7. Não comprovar implementação/autonomia apenas por existir contrato.

## Responsáveis e estado
Autor documental: assistente no chat Auditor, por instrução direta da Direção; autocheck não é auditoria independente. Etapa: proposta preparada. Próximo responsável: Orquestrador para reconciliar concorrências e encaminhar revisão focal. Transporte e aceite ainda precisam de comprovação. Autoridade final: Direção.

## Reconciliação focal GOV-03
Correções por Governança, em continuidade ao parecer [ORG-VAL-01 a 04](https://github.com/gentestsai-sudo/gentests-os/pull/61#issuecomment-6113396719). Autoria original pelo assistente no chat Auditor preservada acima; esta correção é produção documental e autocheck, sem auditoria independente.

| Achado | Correção / destino |
|---|---|
| ORG-VAL-01 | AGT-ORQ: devolução ao originador/dono do dado; decisão reservada ou conflito sem solução à Direção; fila como estado interno |
| ORG-VAL-02 | AGT-ENG/AGT-INFRA: controles específicos de #52 preservados abaixo e PRC-ENG-001 referenciado como proposta |
| ORG-VAL-03 | Índice: PRC-ENG-001/PRC-FIN-001, fronteiras de #50 e pendência FIN-54-01; inventário em #53, sem alterar POL-003 |
| ORG-VAL-04 | Cinco contratos: removido contexto temporário de autoria; mantida segregação geral; fato preservado neste registro |

### Controle → fonte → destino equivalente
Fonte de #52: commit f5b423d7e827645d7fae30f92ecfdf87edb15575; AGT-ENG e AGT-INFRA nos mesmos caminhos desta proposta.

| Controle preservado | Fonte em #52 | Destino em #61 corrigido |
|---|---|---|
| Repositório/branch, ambiente permitido, riscos/dependências/aceite | AGT-ENG Entradas/Pode | AGT-ENG Recebe de e Executa |
| Dados reais e credenciais com autorização específica; sem exposição | AGT-ENG Limites | AGT-ENG Limites específicos |
| Registro de acúmulo Engenharia/Infra; revisão/autorização separadas | AGT-ENG Limites; AGT-INFRA Limites | Ambos: Limites específicos e Segregação |
| Recursos/contas autorizados; testes/revisão e plano de reversão | AGT-INFRA Entradas | AGT-INFRA Recebe de |
| Credenciais, DNS, produção, custos, exclusões, deploy/rollback sob autorização específica | AGT-INFRA Limites | AGT-INFRA Limites específicos |
| Segredos protegidos; logs autorizados; menor privilégio e segregação de ambientes | AGT-INFRA Pode/Limites | AGT-INFRA Limites específicos |
| Estado anterior/posterior, contas, janela, observabilidade e confirmação de destino | AGT-INFRA Saídas; AGT-ENG Saídas | AGT-INFRA Entrega/Interface técnica e falhas; AGT-ENG Entrega/Interface técnica |
| Configuração real dos controles; sem pressupor automações | AGT-INFRA Limites; PRC-ENG-001 Controles | AGT-INFRA Limites específicos; ambos: Interface técnica |
| Contenção somente autorizada e escalonamento | AGT-INFRA Tratamento de falhas | AGT-INFRA Interface técnica e falhas |
| Revisão proporcional, evidências, limite de retrabalho e revalidação focal | PRC-ENG-001 Verificar/Revisar/Falha e retrabalho | Referência expressa ao procedimento de #52 em ambos os contratos e índice; SEC-AI-001 preservada |

### Sequência proposta ao Orquestrador
1. Manter #61 como versão canônica reconciliada dos cinco contratos e índice; manter PRC-ENG-001 na entrega de #52, sem perda de seus controles.
2. Antes de qualquer integração, responsável por #52 deve reconciliar seu delta com a versão corrigida de #61: impedir que seus contratos/índice restaurem texto ou aliases superados. Não integrar #52 posteriormente sem essa reconciliação; alternativa é integrar sua parcela técnica reconciliada antes de #61, com inspeção do delta final. Esta proposta não altera/fecha #52.
3. Responsáveis por #50/#54 preservam seus controles próprios e conciliam interfaces/índice; FIN-54-01 permanece em #54. POL-003 tem dono em #53 e entrega separada para os 14 papéis e Modelo A; issue aberta não equivale a matriz pronta.
4. Orquestrador confirma sequência e bloqueios, encaminha revalidação focal do delta e integração. Direção decide homologação e merge de cada objeto após evidências. Nenhuma ordem aqui autoriza merge.

DoD documental da correção depende do commit confirmado, autocheck e retorno; missão permanece não encerrada. Não foram alterados Financeiro, POL-003 ou PRs concorrentes por esta rodada.


## Delta GOV-04 — compatibilização de branches
PRC-ENG-001 v0.1.1/proposta incorporado nesta branch com os controles anteriores preservados e nome Engenharia canônico; qualquer merge exige autorização explícita da Direção. Contratos AGT-ENG/AGT-INFRA v0.1.2 e índice v0.2.2 agora usam referência local ao procedimento proposto. O delta correspondente de #52 usa os mesmos contratos e 14 papéis; destinos ainda ausentes em sua base são referências explícitas à proposta #61, sem criar contratos duplicados ou alegar integração.
A sequência anterior é substituída por: conferir compatibilidade do delta GOV-04 nas duas branches; responsável por #53 reconciliar separadamente POL-003 preexistente de #52/#54; responsáveis por #50/#54 tratar interfaces e FIN-54-01; Orquestrador encaminhar validação focal e confirmar sequência de integração; Direção decidir eventual merge/homologação. Não integrar #52 enquanto sua parcela de permissões não estiver reconciliada. ORG-VAL-01/02/04 preservados; ORG-VAL-03 permanece dependente das entregas externas nomeadas.
