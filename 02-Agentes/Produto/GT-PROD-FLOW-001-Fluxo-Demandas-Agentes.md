---
tipo: especificacao-produto
id: GT-PROD-FLOW-001
versao: 0.1.0
status: proposta
responsavel: AGT-PROD
consultados_documentalmente: [AGT-GOV, AGT-PROC]
aprovador: Direcao
data: 2026-10-12
---
# GT-PROD-FLOW-001 — Fluxo de demandas e encaminhamentos entre agentes

## 1. Objetivo
Definir **quem encaminha para quem, quando, com qual evidência e responsabilidade**, para os 14 agentes canônicos, sem transformar o Orquestrador em gargalo nem contornar autoridade humana. Artefato de **Produto**, com análise de interfaces de Governança e Processos baseada nos contratos publicados; não constitui parecer emitido por esses agentes nem homologação.

**Princípio:** coordenação central de missão, execução e handoff horizontais quando autorizados, decisão humana nos atos reservados.

## 2. Premissas e fronteiras
- A lista de 14 agentes está em `02-Agentes/Indice-de-Agentes.md` (pasta **02**); a pasta `03-Processos` contém os procedimentos de interação.
- A Direção é autoridade humana, não 15º agente. Revisor Independente Modelo A é função temporária, não agente adicional. Agile Coach não está ativado.
- `GT-HANDOFF-001`, `POL-003` e os contratos consultados são propostas ou possuem cláusulas ainda pendentes de homologação. Este documento **não amplia privilégios**; conferir autorização efetiva, política prevalente, acesso real e conflitos antes de executar.
- A Issue canônica fica no repositório responsável pela entrega; o runtime futuro registra eventos operacionais por `demand_id` e `run_id`; painel consulta o runtime sem segundo estado canônico. No piloto atual, não presumir automação entre chats.
- Toda rodada registra SHA das definições de agentes utilizadas; alterações posteriores não reescrevem histórico.

## 3. Papéis e rotas principais
| Perfil | Recebe principalmente de | Entrega/encaminha principalmente para | Limite |
|---|---|---|---|
| Direção (humana) | ORQ e especialistas em ato reservado | ORQ e responsável executor autorizado | Aprova atos reservados; não substitui pareceres |
| AGT-ORQ Orquestrador | Direção, entrada nova, exceções dos agentes | Especialista competente; Direção para decisão reservada | Coordena e acompanha; não autoexecuta especialidades |
| AGT-PROD Produto | ORQ, Comercial, Marketing, Direção, QA | UX/UI, QA e Engenharia; ORQ em conflito | Define problema, prioridade proposta, requisitos e aceite; não aprova deploy |
| AGT-UXUI UX/UI | Produto, ORQ | Produto se regra ambígua; Engenharia e QA para handoff | Define experiência, não altera regra de negócio unilateralmente |
| AGT-ENG Engenharia | Produto, UX/UI, ORQ, QA (correção) | QA, Infra, Validador conforme gate | Implementa em escopo autorizado; não autoriza merge |
| AGT-INFRA Infraestrutura | Engenharia, ORQ, QA em incidentes | Engenharia, QA, Validador, ORQ | CI/CD, ambientes e operação sob controles e autorização |
| AGT-QA QA | Produto, Engenharia, UX/UI, Infra, ORQ | Autor da entrega para correção; Validador ou revisor designado | Testa, registra risco e parecer; não autoriza merge |
| AGT-VAL Validador | QA, ORQ, responsável pela entrega | Executor para correção; ORQ/Direção com gate | Confere critérios e evidências de terceiros, sem autoaprovação |
| AGT-AUD Auditor | ORQ, Governança, evidências de controles | Governança, Processos, ORQ/Direção | Audita controles de terceiros; não substitui QA |
| AGT-X9 Sentinela documental | ORQ, Governança, Processos ou varredura autorizada | Autor do documento, Governança, ORQ | Sinaliza inconsistência; não homologa nem prova conformidade |
| AGT-GOV Governança | Direção, ORQ, Processos, AUD/VAL/X9 | Processos para tradução operacional; ORQ/Direção para decisão | Propõe regras e autoridade; não homologa |
| AGT-PROC Processos | ORQ, Governança, especialistas | Especialista da interface; Governança para tema normativo | Desenha procedimento; não cria permissão |
| AGT-COM Comercial | ORQ, Marketing, Direção, Produto | Produto para necessidade; Financeiro para análise; Marketing para material | CRM e relacionamento apenas autorizados |
| AGT-MKT Marketing | ORQ, Produto, Comercial | Comercial para lead qualificado; revisão competente antes de publicação | Origem/contexto e conteúdo; não publica sem autorização aplicável |
| AGT-FIN Financeiro | ORQ, Comercial, Direção, área técnica | Comercial/Produto para premissas; Direção para decisão | Simula e concilia sob autorização; **nunca inicia, agenda ou executa pagamentos** |

As rotas são **interfaces candidatas**, não disparos automáticos nem autorizações implícitas. A sequência real depende da natureza e risco da demanda.

## 4. Fluxo comum — estados e dono
1. **Entrada e registro:** originador ou Direção registra demanda na Issue do repositório responsável. ORQ assume triagem inicial; gerar/associar `demand_id` imutável e contexto, sem duplicar fonte.
2. **Classificação:** ORQ identifica tipo (produto, técnica, incidente, governança, processos, comercial, marketing, financeiro), risco, prioridade da Direção, dono e dependências. Consultar contratos e permissões.
3. **DoR:** problema/objetivo, escopo e exclusões, fonte, responsável, critérios verificáveis, risco, autorização e próxima ação. Lacunas voltam ao responsável pelo dado, com motivo. Não despachar prematuramente.
4. **Handoff:** remetente prepara pacote mínimo, registra `handoff_id`, destinatário, versão, evidências e estado; entrega por canal efetivo. **Registrado ≠ entregue ≠ recebido ≠ ACEITO**.
5. **Aceite e execução:** destinatário confirma ACEITO, torna-se dono da etapa e executa somente ações permitidas. Remetente mantém responsabilidade pelo transporte até aceite ou fila excepcional assumida pelo ORQ.
6. **Verificação proporcional:** autocheck do autor; QA para comportamento; VAL para critérios; AUD para controles; X9 para alerta documental; revisor independente Modelo A quando gate exigir. Não acionar todos automaticamente.
7. **Correção focal:** falha retorna ao autor/executor competente com achado, evidência e condição de rechecagem; não repetir provas válidas sem mudança material.
8. **Decisão protegida:** Direção recebe pacote com ato exato, objeto, riscos, evidências e responsável. Parecer positivo não substitui autorização.
9. **Integração/entrega:** executor habilitado realiza ato autorizado, registra commit/PR/deploy/resultado efetivo e reconcilia evidências.
10. **Encerramento:** ORQ verifica DoD e gates comprovados, registra estado final e próxima ação residual. Fechamento de Issue não presume publicação ou implantação.

**Exceções:** silêncio não é aceite; falha de transporte exige recuperação; conflito de prioridade/rota/escopo vai ao ORQ; dúvida normativa vai a GOV; risco urgente de segurança vai à Direção/ORQ e bloqueia apenas o trecho afetado. Trabalho independente autorizado pode seguir em paralelo.

## 5. Fluxos por natureza

### A. Funcionalidade ou produto novo
`Direção/originador → ORQ (triagem) → PROD (discovery/requisitos) ↔ QA (testabilidade) → UXUI (jornada) ↔ PROD (regras) → ENG (viabilidade/implementação autorizada) ↔ INFRA (ambiente) → QA (testes) → VAL (aceite quando aplicável) → revisão independente (se exigida) → Direção (ato reservado) → ENG/INFRA (integração/deploy autorizado) → ORQ (encerramento)`.

Produto, UX/UI, QA e Engenharia podem refinar em paralelo quando as interfaces estiverem claras; implementação sensível depende de autorização. QA prepara testes antecipadamente sem fingir execução.

### B. Bug, regressão ou incidente
`Origem/monitoramento → ORQ (prioridade/risco) → ENG ou INFRA (diagnóstico) ↔ QA (reprodução e risco) → ENG/INFRA (correção autorizada) → QA (regressão) → VAL/revisor conforme risco → Direção (ato protegido) → ENG/INFRA (entrega) → ORQ`.
Incidente crítico de segurança: escalar imediatamente à Direção e interromper operação afetada. PROD participa se comportamento esperado ou impacto de negócio for controverso.

### C. Política, contrato ou permissão
`Direção/achado → ORQ → GOV (análise normativa) ↔ PROC (impacto operacional) → AUD/VAL/revisor independente conforme gate → Direção (homologação) → PROC (procedimento derivado autorizado) → ORQ`.
Alteração normativa não é correção editorial; GOV/PROC não aprovam suas próprias propostas.

### D. Procedimento e melhoria de fluxo
`Especialista/ORQ → PROC (mapa, DoR/DoD, exceções) ↔ especialista da área → GOV se houver impacto em autoridade → revisão proporcional → Direção se mudar regra/controle reservado → PROC (documentação autorizada) → ORQ`.
Correções editoriais simples podem seguir autonomia documental estrita, branch isolada e PR, sem merge automático.

### E. Marketing e Comercial
`MKT (origem/contexto) → COM (deduplicação, qualificação e CRM autorizado) → PROD (necessidade/oportunidade) ou FIN (análise econômica) → Direção (compromisso/preço/publicação quando reservado) → responsável autorizado → ORQ`.
Campanha: `MKT → revisão de marca/conteúdo competente → Direção para publicação protegida → MKT autorizado`. Não presumir envio externo ou CRM paralelo.

### F. Financeiro
`COM/PROD/Direção → FIN (premissas, estimativa, conciliação autorizada) → responsável pela premissa para ajuste → Direção (decisão comercial/financeira reservada) → responsável humano habilitado por ato externo → FIN (registro/conciliação autorizada) → ORQ`.
**FIN não inicia, agenda nem executa pagamentos/transferências; tampouco envia cobrança financeira externa.** Não converter simulação em gasto ou recebimento real.

### G. Controle, auditoria e alerta documental
`X9 → autor/GOV/ORQ (indício e evidência)`; `AUD → GOV/PROC/ORQ (achado de controle)`; `VAL → autor/ORQ (critério atendido ou lacuna)`. Nenhum desses pareceres é homologação ou autorização de merge.

## 6. Contrato mínimo do encaminhamento
Campos: `demand_id`, `run_id` (se execução), `handoff_id`, `source_issue`, `from_agent`, `to_agent`, `current_owner`, `next_owner`, `objective`, `scope`, `acceptance_criteria`, `risk`, `required_authorization`, `agent_definitions_commit_sha`, `artifact_refs`, `evidence_refs`, `state`, `timestamp`, `next_action`. Campos inaplicáveis devem ser marcados N/A com motivo.

Estados distintos: `PREPARADO`, `REGISTRADO`, `ENTREGA_PENDENTE`, `ENTREGUE`, `AGUARDANDO_ACEITE`, `ACEITO`, `DEVOLVIDO`, `EM_EXECUCAO`, `BLOQUEADO`, `CONCLUIDO_ETAPA`, `EM_VERIFICACAO`, `AGUARDANDO_DECISAO`, `AUTORIZADO`, `INTEGRADO`, `ENCERRADO`, `CANCELADO`. O modelo de eventos técnico será detalhado por Engenharia/Processos, com idempotência e compatibilidade ao GT-HANDOFF-001.

## 7. Regras de roteamento e prevenção de gargalos
- ORQ coordena a missão global e exceções; **não** recebe cada handoff horizontal para retransmitir.
- O especialista que conclui uma etapa encaminha diretamente à próxima competência **somente quando rota e autoridade efetivas permitem**, dando ciência na Issue canônica.
- Nenhuma etapa exige passar pelos 14 agentes. Gate é escolhido por tipo de entrega e risco; segregação e revisão independente permanecem quando obrigatórias.
- Direção não é balcão de confirmação de atos ordinários já autorizados. Reutilizar autorização expressa válida para o mesmo objeto e condições, sem inferir cobertura de novos atos.
- Paralelismo só quando reduzir espera e não causar conflito de recurso/branch ou duplicação de trabalho; priorização da Direção prevalece.
- Não presumir que GitHub Issues aciona chats; o piloto precisa comprovar transporte, recebimento e aceite antes de automatizar.
- Painel é projeção operacional; a Issue canônica e o registro do runtime possuem responsabilidades distintas, sem estado operacional duplicado.

## 8. Critérios de aceite
- CA-01: cada um dos 14 agentes possui ao menos entrada, saída, limite e rota de exceção definidos.
- CA-02: nova demanda possui Issue canônica, `demand_id`, dono, tipo e DoR; duplicidade é identificável.
- CA-03: handoff não avança a `ACEITO` sem confirmação efetiva do destinatário; silêncio, comentário ou mensagem preparada não bastam.
- CA-04: rota horizontal autorizada não exige passagem obrigatória pelo ORQ, mas deixa evidência para supervisão.
- CA-05: solicitação de merge, deploy, publicação, gasto ou mudança de política não é executada sem autorização específica e permissão efetiva.
- CA-06: autoria, QA, validação, auditoria e revisão independente respeitam segregação e elegibilidade verificável.
- CA-07: correção devolve ao dono competente e só reexecuta verificação impactada, preservando evidências anteriores.
- CA-08: piloto comprova fluxo feliz ponta a ponta com `demand_id`, `run_id`, SHA de definições, eventos e evidências antes de extração.
- CA-09: bloqueio tem motivo, responsável e próxima ação; atividades independentes autorizadas podem continuar.
- CA-10: painel e runtime não mantêm estados canônicos concorrentes; reconciliação e latência são testadas na implementação futura.
- CA-11: fluxo financeiro impede tecnicamente e procedimentalmente iniciação/agendamento/execução de pagamentos por FIN.
- CA-12: encerramento de missão depende de DoD, verificações e atos reais comprovados, não apenas PR aberta ou parecer.

**Estado dos testes:** critérios propostos; não foram executados testes funcionais nesta entrega documental.

## 9. Riscos, dependências e decisões pendentes
| Risco | Tratamento |
|---|---|
| Fluxo horizontal conflitar com contratos anteriores | GOV/PROC reconciliam GT-HANDOFF-001, POL-003 e contratos; Direção decide |
| Aceite fictício por comentário GitHub | Separar eventos de registro, transporte, recebimento e ACEITO |
| Excesso de gates | Matriz por risco e natureza; não acionar todos por padrão |
| Autoaprovação | Verificar identidade e conflito real, não apenas nome de agente/chat |
| Regras mudarem no meio da execução | SHA fixo por rodada, mudança material com decisão de atualização |
| Duplo estado Issue/runtime/painel | Issue é demanda, runtime é execução, painel é projeção |
| Falha de automação/duplicidade | Idempotência, trilha, recuperação e teste do piloto |

**Pendências:** GOV confirmar precedência normativa e permissões; PROC reconciliar procedimento de handoff; ENG/INFRA definir eventos e transporte real; QA definir testes de rota/recuperação; VAL verificar critérios; Direção aprovar modelo e autorizar implementação. Não alegar que essas áreas já emitiram parecer.

## 10. Referências e handoff
- [AGT-PROD](Contrato-Agente-Produto.md)
- [Diretório de agentes](../Indice-de-Agentes.md)
- [AGT-ORQ](../Orquestrador/Contrato-Agente-Orquestrador.md)
- [AGT-GOV](../Governanca/Contrato-Agente-Governanca.md)
- [AGT-PROC](../Processos/Contrato-Agente-Processos.md)
- [GT-HANDOFF-001](../../03-Processos/Encaminhamento-de-Missoes-GT-HANDOFF-001.md)
- [PRC-PROD-001](../../03-Processos/Refinamento-Produto-UX-Handoff.md)
- [POL-003](../../00-Constituicao/Matriz-de-Permissoes.md)
- [Arquitetura de repositórios proposta](GT-PROD-REPOS-001-Arquitetura-Repositorios.md)

**Handoff solicitado:** Governança (conformidade de autoridade), Processos (semântica de transições), Engenharia/Infra (viabilidade), QA/Validador (testabilidade e gates), Direção (deliberação). Documento de Produto em proposta, sem modificação dos contratos existentes, políticas, código ou runtime.


## 11. Decisão posterior da Direção — Scrum Master sem centralização (AGT-SM)

Esta seção substitui as referências anteriores a AGT-ORQ como coordenador central, triador obrigatório, intermediário de handoffs e responsável por encaminhar toda etapa.

- **Papel:** Scrum Master (AGT-SM), anteriormente denominado Orquestrador Central/AirCaster.
- **Responsabilidade:** monitorar saúde do fluxo; detectar tarefas paradas, impedimentos, gargalos, falhas de transporte/aceite e conflitos; classificar impacto e urgência; encaminhar ao especialista ou responsável competente; escalar o que exceder a alçada; acompanhar o desfecho registrado.
- **Não é executor nem solucionador:** não corrige, não implementa, não decide pelo especialista e não assume a tarefa bloqueada. Sua ação termina no encaminhamento/escalonamento e acompanhamento.
- **Handoffs horizontais:** agentes podem se comunicar e transferir etapas diretamente, quando a rota estiver definida e a autorização/permissão efetiva existir. O registro canônico dá visibilidade ao Scrum Master, mas não exige sua intermediação.
- **Entrada de demandas:** pode existir um mecanismo determinístico de registro/classificação inicial, mas isso não transforma o Scrum Master em ponto obrigatório de passagem. Tarefas podem ser direcionadas ao especialista competente por regras de roteamento.
- **Merge:** o Scrum Master pode acompanhar PRs, verificar presença dos pareceres e gates definidos e encaminhar pendências ao responsável. A ideia de ele aceitar/autorizar ou executar merges é registrada como **proposta pendente**: POL-003 vigente reserva autorização de merge à Direção e não pode ser alterada por este documento de fluxo. Qualquer delegação exige decisão explícita, revisão da matriz, segregação de funções e permissões técnicas compatíveis.
- **Automação econômica:** estados, filas, timeouts, limites, detecção de bloqueios e encaminhamentos padronizados devem ser implementados em código determinístico. Chamar API/LLM somente quando a classificação exigir interpretação contextual que regras não resolvam, com orçamento/cota explícitos.

O fluxo feliz não passa pelo Scrum Master. Ele atua por exceção, com visibilidade operacional e rastreabilidade, sem se tornar gargalo.
