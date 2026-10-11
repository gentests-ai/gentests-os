---
tipo: proposta-organizacional
id: GT-ORG-REFORM-001
versao: 0.1.0
status: proposta
---
# Reformulação da estrutura de agentes

## Objetivo e autoridade
Reformular funções por responsabilidade futura, independentemente da distribuição histórica de atividades, conforme instrução direta da Direção em 11/10/2026. Preservar registros anteriores. Este pacote é proposta documental: não ativa agentes, não altera permissões e não autoriza merge.

## Estrutura
Direção decide estratégia e atos reservados. Um Orquestrador Central coordena as missões. Especialistas respondem por entregas do domínio. Governança e Processos têm funções transversais distintas. QA, Validador, Auditor e X9 mantêm fronteiras de controle próprias. Revisão Independente é função atribuída a especialista por missão (Modelo A), não agente permanente.

## Fronteiras e roteamento
| Pergunta ou objeto | Responsável primário | Limite |
|---|---|---|
| Quem recebe a próxima etapa e qual a prioridade autorizada? | Orquestrador | Não decide mérito especializado |
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
| Orquestrador, Orquestrador Central | Orquestrador Central (AGT-ORQ), único |
| Auditoria, Auditor | Auditor (AGT-AUD) |
| Validação, Validador | Validador (AGT-VAL) |
| Governança, agente de governança | Governança (AGT-GOV) |
| Processos, agente de processos | Processos (AGT-PROC) |
| Revisor Independente, Revisão Técnica independente | Função Modelo A atribuída por missão; revisar compatibilidade real |
| Agile Coach | Candidato de análise de fluxo; não incluído como agente ativo por este pacote |

“Executor” isolado é a função de quem produz a entrega, não sinônimo universal de Engenharia: Marketing executa conteúdo, Processos executa desenho de procedimento etc. Aliases preservam busca e rastreabilidade; não renomear históricos em massa. Chats de atividade são contexto, não novos agentes.

## Concorrência e impacto
- Issue #53: dona da reconciliação da matriz de permissões; este pacote não modifica POL-003. Associar os cinco novos papéis na proposta de #53 antes de adoção operacional.
- PR #52: já propõe AGT-ENG e AGT-INFRA. Preservados IDs e caminhos de arquivos para evitar contratos concorrentes. A nova proposta reformula esses textos; integrar uma versão única, nunca ambas sem reconciliação.
- PR #54: preservar escopo e restrições Financeiro; índice tem concorrência.
- PR #50: preservar responsabilidades Comercial/Marketing; reconciliar índice, sem reescrever seus contratos aqui.
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
