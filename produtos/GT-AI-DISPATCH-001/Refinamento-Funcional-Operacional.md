---
id: GT-AI-DISPATCH-001
tipo: refinamento-funcional-operacional
versao: 0.1.0
status: proposta-para-revisao-independente-focal
data: 2026-10-10
autor_papel: Gerente-de-Produto
issue_canonica: 47
implementacao_autorizada: nao
piloto_executado: nao
merge_autorizado: nao
---
# GT-AI-DISPATCH-001 — Despacho e Notificação de Missões dos Agentes

## 1. Visão, problema e limite da entrega

Uma solicitação registrada deve ter destino, autorização, responsável pelo encaminhamento, confirmação observável e resultado verificável. Hoje o GitHub registra a demanda, mas isso não comprova o acionamento de um agente conversacional. O produto é um fluxo de missões rastreáveis na issue existente, começando por coordenação humana e recursos nativos. Benefício esperado: menos missões esquecidas e menos consultas manuais da Direção; benefício ainda não medido.

Este refinamento aproveita o [diagnóstico da Governança](https://github.com/gentestsai-sudo/gentests-os/issues/47#issuecomment-6103014403), sem repetir o discovery ou auditar controles administrativos. A [Issue #47](https://github.com/gentestsai-sudo/gentests-os/issues/47) continua sendo o registro canônico da demanda. Este arquivo especifica o produto; a PR conterá somente seu delta documental, sem uma segunda fila de missões. A solicitação da Direção nesta sessão autoriza refinamento e registro, não implantação.

**Prioridade:** planejamento estrutural, subordinado ao P0 comercial da #45. Nenhuma dependência deste desenho bloqueia correções comerciais já autorizadas. Nenhum workflow, integração, credencial, label, atribuição operacional, permissão, política ou automação é criado/alterado nesta entrega. Não executar piloto, contratar, fazer merge ou acionar outros agentes.

### Fontes examinadas e limites

Baseline da main: `a4c3f7606747f29acb6e11928889f962355c3ab7`, consultada em 10/10/2026. Não há AGENTS.md no inventário dessa árvore.

| Fonte | Estado e consequência |
|---|---|
| POL-003 — `00-Constituicao/Matriz-de-Permissoes.md` | v1.0.0, proposta; blob `7bf11bc753244ddf4164750c3e764b28d8704de1`. Não explicita os papéis de coordenação/execução/revisão |
| QG-001 — `00-Constituicao/Quality-Gates/QG-001-Politica.md` | v0.1.0, proposta; blob `f58d0d10e3718379b6dd0311056b5e0cc3754430`; gate documental não comprova enforcement |
| SEC-AI-001 — `00-Constituicao/SEC-AI-001-Seguranca-Confiabilidade-Agentes.md` | v0.1.0, proposta; blob `5a3a7067a03041011ecbef3da8cc0f82df5a366d` |
| GOV-5S-001 — `00-Constituicao/Excelencia-Enxuta-5S.md` | v0.1.0, proposta; blob `8759d58860dd38402767685861947d6c3c6c5c4f`; reutilizar fontes/fluxos |
| Índice e sete contratos de `02-Agentes/` | Especificações de design, todos os contratos em proposta; ausência de prova de conta/sessão permanente |
| [PR #17 — DEC-GOV3-20261010-001](https://github.com/gentestsai-sudo/gentests-os/pull/17) | Registro delimitado: preparação encerrada e redação revisada de POL-003 autorizada; nove normas não homologadas; GT-GOV-004 somente backlog; sem merge/execução técnica |
| [DISC-QA-001 #46](https://github.com/gentestsai-sudo/gentests-os/issues/46#issuecomment-6102935301) e parecer posterior na mesma issue | Proposta não vigente; revisão aponta A01–A04 e não recomenda institucionalizar ainda o fluxo completo. Não antecipar resolução nem alterar seu diagnóstico |
| [GT-AI-LEARN-001 PR #8](https://github.com/gentestsai-sudo/gentests-os/pull/8) | v0.2.0, head `74453f80ec03bc00bcd0e1b73838138ba29933e3`; revisão focal documental favorável, piloto/CI/curadoria não autorizados |
| Metadados do repositório | Privado, main como padrão; acesso de leitura/escrita do conector nesta sessão não prova identidades ou permissões dos futuros agentes |
| Três workflows existentes em `.github/workflows/` | Markdown, QG e X9 determinístico; arquivos lidos, execução/cotas não inspecionadas. Não demonstram despacho ou IA conectada |
| Labels/canais/plano | Inventário completo de labels não obtido: endpoint recusado pelo conector. Configurações pessoais, plano contratado, saldo/cotas e entrega de notificações não verificados |

Normas em proposta são referências de desenho, não obrigações declaradas vigentes por este documento. As restrições explícitas da Direção aplicam-se a esta entrega. Revisão POL-003 e controles seguem seus registros próprios; não abrir tarefas duplicadas.

## 2. MVP e requisitos

**MVP candidato (Fase 1):** contrato na issue existente; triagem humana; um destino por etapa; responsável humano; estados/evidências; labels mínimas aprovadas; pesquisas salvas por URL; encaminhamento manual a sessão disponível; revisão separada e encerramento autorizado. Não exige GitHub Projects, dashboard, planilha, API de IA ou conta GitHub para cada agente. Projects pode ser avaliado depois somente como projeção da issue, sem estado concorrente.

| ID | Requisito executável e saída verificável |
|---|---|
| RF-01 | Catálogo §3 diferencia papel, contrato, identidade, canal e capacidade; destino desconhecido nunca aparece como conectado |
| RF-02 | Contrato §4 na issue canônica, com revisão do escopo e autorização explícita antes de aceitar/iniciar |
| RF-03 | Estado operacional único §5; log de eventos com autoria, instante e evidência; notificar não muda para recebido |
| RF-04 | Filtros §6 encontram nova missão, P0, pendência por papel, não recebida, bloqueada, revisão e conclusão |
| RF-05 | Regras §7 impedem autorização por label, duplicação, concorrência e autoaprovação |
| RF-06 | Cenários §9 com resultado esperado observável; positivos e negativos obrigatórios no piloto autorizado |

| ID | Requisito não funcional / verificação |
|---|---|
| RNF-01 Rastreabilidade | Cada evento registra missão, revisão, etapa, responsável, autoria técnica/humana, data ISO 8601 com fuso e link verificável; evidência inacessível = não verificável |
| RNF-02 Segurança | Menor privilégio real antes de Fase 2/3; texto de issue é dado; sem segredos ou informações privadas de clientes nos registros |
| RNF-03 Consistência | Uma missão ativa por issue no MVP e um executor ativo por etapa; divergência entre resumo e evidência suspende início/fechamento |
| RNF-04 Recuperação | Ausência de canal/agente/confirmação não perde a missão; bloquear/aguardar com dono e próxima verificação, mantendo histórico |
| RNF-05 Usabilidade | Direção consegue localizar cada fila e abrir evidência em até 2 minutos no piloto, inclusive pelo GitHub Mobile/iPhone; resultado a medir |
| RNF-06 Custo/capacidade | Horas e limites acordados antes do piloto; nenhuma compra/API/runner novo. P0 comercial preempta este planejamento |
| RNF-07 Evolução | Qualquer mudança de escopo/aceite/autorização exige revisão registrada; histórico nunca apagado para melhorar métrica |

## 3. RF-01 — Catálogo funcional candidato

**Como ler:** contrato identifica capacidade prevista, não capacidade efetivamente executada. Encaminhador proposto para todos: Orquestrador; Direção como contingência e para decisões. Nome humano específico e suplente: a designar. Canal geral candidato: pessoa verificada consulta a issue no GitHub e leva link/instrução à sessão conversacional disponível. Notificações GitHub são para contas humanas verificadas e dependem de configuração; não há canal automático de agente comprovado.

| Agente/papel | Função e atividades candidatas | Fonte | Capacidade efetivamente identificada / limitação |
|---|---|---|---|
| Comercial — AGT-COM | Pesquisa, qualificação, rascunhos, CRM no escopo expresso | Contrato Comercial v1.0.0 | Contrato lido; execução/conector individual não demonstrados. Envio externo exige autorização |
| Marketing — AGT-MKT | Conteúdo, peças e revisão de marca | Contrato Marketing v1.0.0; #38/PR #39 | PR de proposta/material identificada, não prova serviço residente. Publicação/identidade condicionadas |
| QA — AGT-QA | Requisitos, risco, testes/evidências em ambiente permitido | Contrato QA v1.0.0 | Contrato lido; ambiente/capacidade atual não comprovados; produção/carga/destruição não presumidas |
| Financeiro — AGT-FIN | Análises e registros com fontes | Contrato Financeiro v1.0.0 | Dados/ferramentas autorizados não verificados; sem pagamentos autônomos |
| Auditor — AGT-AUD | Conformidade e efetividade por amostra | Contrato Auditor v1.0.0 | Contrato lido; acesso/auditoria efetiva não comprovados; não confundir com executor |
| Validador — AGT-VAL | Parecer contextual, QG, evidências | Contrato Validador v0.1.0 | Contrato diz não implementado como autônomo; não edita/valida própria entrega |
| X9 — AGT-X9 | Inspeção documental e alertas | Contrato X9 v0.1.0; workflow x9-daily | Especificação determinística de workflow presente; não se verificou run nem IA autônoma |
| Orquestrador | Triagem, deduplicação, coordenação e acompanhamento | #47, Governança; GT-GOV-003 §3 | Papel operacional referido; contrato próprio/conta/serviço não encontrados no inventário consultado |
| Governança | Avaliar autorização, riscos, fontes normativas e desvios | Comentário 6103014403 | Diagnóstico entregue na issue; prova de trabalho documental, sem identidade GitHub individual/continuidade |
| Executor Técnico | Viabilidade e futuras implementações delimitadas | #47/#45; GT-GOV-003 §3 | Missões referidas, capacidade de integração permanente desconhecida; código/workflow fora desta autorização |
| Revisor Independente | Revisar delta e emitir parecer separado | #47; parecer #46; PR #11 | Pareceres identificados; seleção de sessão/autor distinto ainda depende de coordenação verificável |
| Gerente de Produto | Refinamento, requisitos, piloto e priorização | Solicitação atual | Refinamento documental elaborado nesta sessão; não possui serviço permanente demonstrado |
| UX/UI | Propostas e estados de interface | PR #36 | Proposta identificada; conta/contrato/integração não comprovados |
| Executor do Site | Alterações delimitadas no site | PR #5 referencia execução no gentests-site | Referência documental somente; acesso/capacidade atual não inspecionados |

Todos os destinos acima: conta GitHub própria **não verificada**, sessão contínua **não comprovada**, serviço acionável **não comprovado**, disponibilidade **a confirmar por missão**. A conta `gentestsai-sudo` observada como autora dos registros não representa contas separadas de agentes. Não inferir independência só por login ou nome do papel.

Na preparação autorizada do piloto, registrar **na #47**, sem cadastro externo, confirmação de cada destino usado: papel; operador humano e suplente; conta GitHub elegível verificada; canal real; referência da sessão/serviço sem dado sensível; ferramentas/ações demonstradas; disponibilidade e data de confirmação. Pode registrar “encaminhamento humano obrigatório” e “sem conta de agente”. Nenhuma prova de disponibilidade equivale a permissão.

## 4. RF-02 — Contrato de missão na issue

O ID é o já existente; se ausente, usar referência estável `gentests-os#N`, sem inventar novo código corporativo. Uma issue contém uma missão ativa no MVP; execução e revisão são etapas da mesma missão. A #47 guarda esta proposta, sem duplicar missões de #45/#46.

**Bloco candidato no corpo da issue (implantação posterior autorizada):**

| Campo | Conteúdo mínimo / regra |
|---|---|
| Identificação/descrição | ID, problema, resultado esperado e issue canônica |
| Revisão autorizada | Inteiro do escopo/aceite; começa 1; incremento só com decisão válida que altere a missão |
| Etapa e destino | Execução ou revisão; papel destinatário; executor atual; revisor distinto |
| Responsável humano | Operador/encaminhador, conta verificada ou sem conta, suplente, canal disponível |
| Prioridade/risco | Prioridade explícita, inclusive P0; risco separado; sem prazo/SLA presumidos |
| Autorização | Referência da decisão, decisor, objeto, ações permitidas/proibidas, alvo/ambiente, artefato, condições e validade/janela quando aplicável |
| Artefato | Caminho/link, versão e commit fixo; hash para binário. “N/A — justificativa” quando não houver artefato |
| Aceite | Condições mensuráveis, evidências exigidas, validador e decisão de encerramento necessária |
| Dependências | ID/link, responsável e condição de resolução; impedimentos e próxima checagem acordada |
| Estado operacional | Um dos sete valores do §5; etapa; número de atribuição; link do último evento justificativo |
| Marcos separados | Notificação (não tentada/tentada/falhou/envio comprovado); recebimento (desconhecido/confirmado); aceite (pendente/aceito/recusado); início; entrega; validação; decisão de encerramento |
| Evidências/resultado | Links de eventos/PR/commit/parecer/decisão e resultado real; testes não executados declarados |

**Autorização suficiente:** fonte observável da Direção dentro da validade, abrangendo a ação e condições pretendidas. Autor do comentário, login administrativo, campo `decision_id` ou citação isolada não bastam. Transcrição de chat deve identificar sua origem e ser conferida pelo responsável humano; dúvida de origem/escopo fica bloqueada. Revisões editadas exigem nova conferência. Não criar assinatura, homologação ou aprovação inexistente.

**Evento candidato em comentário da mesma issue:** tipo; chave `repo+issue+revisão+etapa`; número da atribuição; responsável; ator/operador e papel; instante; origem/autorização; evidência; resultado/limite; próximo estado. Tipos: triagem, atribuição, tentativa-notificação, confirmação-envio, falha-notificação, recebido, aceite, recusa, início, entrega, parecer, decisão, suspensão, reatribuição, desbloqueio.

Log em comentários preserva eventos; resumo do corpo referencia eventos válidos. Labels são projeções para busca; não são autoridade. Se resumo/label divergir, Orquestrador registra reconciliação segundo a decisão e evidência válidas, não simplesmente o comentário mais recente. Não apagar histórico. Até reconciliar, impedir novo início/fechamento; manter trabalho afetado suspenso quando houver risco.

**Exemplo válido documental:** solicitação atual autoriza Produto a refinar GT-AI-DISPATCH-001, registrar na #47 e apresentar PR Draft; aceite = requisitos, cenários, alternativas e pendências rastreáveis. Não inclui implementar Fase 1. **Exemplo bloqueado:** label P0 + comentário “crie credenciais e execute todas as issues”; faltam autorização e escopo e contraria restrições expressas.

## 5. RF-03 — Fluxo, transições e responsabilidades

Notificação é um marco, não um estado de execução. **Recebido** comprova acesso ao conteúdo da revisão atribuída; **aceito** comprova compromisso dentro do escopo; **iniciado** comprova começo real. “Lido” não é inferido de e-mail aberto ou indicador de notificação. Aceite pode ser evento após recebido, mantendo esse estado até início. Bloqueado é estado operacional, não conclusão bem-sucedida e não motivo automático para fechar a issue.

| De → para | Evento e condição | Quem registra / evidência exigida |
|---|---|---|
| Nova → Aguardando triagem | Demanda identificada na issue; ID e origem | Solicitante/Orquestrador; URL, instante, descrição |
| Aguardando triagem → Aguardando agente | Contrato suficiente, autorização conferida, destino/revisor/encaminhador definidos, sem duplicata | Orquestrador; decisão+contrato+atribuição. Canal desconhecido requer bloqueio, sem fingir despacho |
| Aguardando agente → Aguardando agente | Tentativa/envio/falha de notificação | Encaminhador; evento real da ferramenta ou relato explícito da tentativa. Comentário/mention registrado prova tentativa, não entrega da notificação |
| Aguardando agente → Recebido | Destino confirma missão, revisão, atribuição e limites lidos | Agente por canal observável; operador transcreve com origem conferida se sem conta. Confirmação humana isolada não prova recebimento pelo agente |
| Recebido → Recebido | Aceite explícito ou pedido de esclarecimento sem começar | Agente confirma disponibilidade, escopo e ausência de conflito; registrar aceite separado |
| Recebido → Em execução | Recebimento+aceite+autorização válidos, atribuição atual sem outro executor ativo e início real | Executor; evento de início com objeto/primeira ação permitida, instante e evidência. Sem ação adicional apenas para “provar” início |
| Em execução → Em revisão | Entrega versionada e evidências/limitações presentes | Executor entrega; Orquestrador encaminha a revisor distinto; commit/PR e checklist do aceite. Revisão também exige recebimento/aceite/início registrados para sua etapa |
| Em revisão → Em execução | Parecer pede correção delimitada coberta pela autorização atual | Revisor aponta delta; Orquestrador devolve; executor confirma reinício. Mudança de escopo exige revisão/autorização nova |
| Em revisão → Concluído | Aceite evidenciado, parecer independente quando aplicável e decisão exigida para encerramento | Direção decide neste piloto; Orquestrador registra links. Executor não se autocertifica. Merge/publicação continuam atos distintos |
| Qualquer ativo → Bloqueado | Falta de autorização, canal/agente indisponível, conflito, incidente ou dependência impeditiva | Detector relata; Orquestrador registra causa, etapa anterior, dono e condição de desbloqueio. Segurança escala imediatamente |
| Bloqueado → estado ativo pertinente | Condição impeditiva resolvida por evidência e autorização atual reconferida | Orquestrador; decisão, prova, etapa e atribuição atual. Não saltar recebido/aceite/início |
| Concluído → Aguardando triagem | Novo fato material justificado, reabertura ou nova revisão autorizada | Direção/Orquestrador registra motivo/decisão; preserva conclusão anterior, sem nova contagem indevida |

Direção autoriza escopo/custos, arbitra conflitos e decide encerramento; Produto especifica; Orquestrador coordena sem homologar; Governança verifica conformidade/identidade de autorização sem conceder acesso; executor trabalha dentro do escopo; revisor em sessão/autor distinguível não modifica a entrega original; Infra fornece comprovações técnicas futuras. São responsabilidades propostas, não extensão silenciosa da POL-003.

Cancelamento/duplicata: registrar resultado e vínculo, com decisão competente; pode fechar issue como não planejada quando autorizado, mas não usar label Concluído nem contabilizar entrega validada. Issue fechada por interface não prova conclusão válida.

## 6. RF-04 — Filas nativas e acompanhamento

Nomenclatura abaixo é **candidata**, não criada nem validada contra inventário completo. Orquestrador deve inspecionar labels existentes antes do piloto, mapear equivalentes e propor só as ausentes. Uma label `mission`, uma prioridade, um papel da etapa atual e **um** estado: `status:triagem`, `status:aguardando-agente`, `status:recebido`, `status:execucao`, `status:revisao`, `status:concluido`, `status:bloqueado`. Usar `agent:<papel>` para destino lógico e assignee somente para conta verificada do responsável humano ou agente real elegível; não atribuir conta fictícia. Se uma pessoa encaminha vários papéis, filtro por assignee não substitui agente.

Consultas candidatas a salvar como URLs/favoritos no GitHub, depois da conciliação dos nomes:

| Visão | Consulta (prefixar `repo:gentestsai-sudo/gentests-os is:issue`) |
|---|---|
| Todas as missões ativas | `is:open label:mission sort:created-asc` |
| Novas | `is:open label:mission label:"status:triagem" sort:created-asc` |
| P0 | `is:open label:mission label:"priority:p0" sort:created-asc` |
| Pendências de um agente | `is:open label:mission label:"agent:product" sort:created-asc` (substituir papel mapeado) |
| Sem confirmação | `is:open label:mission label:"status:aguardando-agente" sort:created-asc`; conferir também bloqueados por recebimento |
| Bloqueadas | `is:open label:mission label:"status:bloqueado" sort:updated-asc` |
| Aguardando revisão | `is:open label:mission label:"status:revisao" sort:created-asc` |
| Concluídas validadas | `label:mission label:"status:concluido" sort:updated-desc`; conferir links de aceite, não contar fechamento simples |

Bloqueio por falta de confirmação mantém marco “desconhecido” e causa no resumo. A fila bloqueada é parte obrigatória da consulta de não recebidas; não esconder pendência por trocar label. Missão sem qualquer label pode escapar dos filtros: na triagem periódica humana conferir também issues abertas sem classificação contra o contrato, sem tratar toda issue como missão.

P0 não implica prazo ou permissão. Orquestrador verifica filas no início de sua sessão de trabalho e antes de encerrar; próxima checagem é registrada quando não houver disponibilidade contínua. Cadência e suplente precisam ser aprovados; não se promete monitoramento permanente.

Notificações nativas dependem de conta elegível e preferências pessoais (watch/participação/mentions/atribuição). GitHub permite inbox, e-mail e Mobile; evidência de envio/recebimento real deve ser observada no piloto. Uma mention no mesmo usuário que realizou a ação pode não fornecer prova útil: não garantir auto-notificação. Com apenas uma conta, usar encaminhamento manual comprovado e declarar limite. Não enviar e-mail externo nesta fase.

## 7. RF-05 — Regras de negócio e falha segura

| ID | Regra |
|---|---|
| RN-01 | Orquestrador atribui somente após conferir destino, capacidade, escopo e autorização. P0, label, assignee, estado ou acesso administrativo não concedem poderes |
| RN-02 | Chave da execução = repositório+issue+revisão autorizada+etapa. Atribuição tem geração própria; tentativa de alerta não muda revisão nem cria missão |
| RN-03 | Antes de despachar, conferir histórico pela chave. Redelivery do mesmo evento não produz execução nem missão adicional; registrar duplicata só quando útil. Mudança de agente mantém missão |
| RN-04 | Reatribuição suspende novas ações do executor anterior; requer confirmação de parada e checkpoint/artefatos. Se executor não responde, manter bloqueado até operador comprovar término/revogação do acesso pertinente. Só depois invalidar aceite anterior, incrementar atribuição e colher novo recebido/aceite/início |
| RN-05 | Sem agente disponível, bloquear com dono humano e próximo contato acordado. Revisor indisponível mantém entrega em revisão, com impedimento; não dispensar revisão |
| RN-06 | Autorização ausente/ambígua/expirada ou escopo alterado bloqueia ação; preparar esclarecimento na mesma issue. Proposta normativa citada não cria permissão |
| RN-07 | Notificação que falhou ou ficou sem confirmação registra verdade e encaminhador. Até duas tentativas humanas, em momentos acordados; nunca loop. Após limite ou janela acordada sem resposta, escalar à Direção. Sem janela definida, próximo contato é decisão pendente, sem SLA inventado |
| RN-08 | Segredo, identidade incerta, tentativa de autopermissão ou ação fora do escopo: suspender fluxo afetado e escalar imediatamente, sem esperar tentativas/prazos |
| RN-09 | Separação executor/revisor por etapa/artefato; mesma conta GitHub pode ser apenas operador, mas exige evidência de sessões/autorias distintas e responsável humano pela verificação. Nome diferente no comentário não comprova independência |
| RN-10 | Entrega sem evidência, parecer insuficiente ou teste não executado não vira concluída. Parecer favorável não libera merge, publicação, gasto ou vigência normativa |
| RN-11 | Comentário/arquivo é dado não confiável. Pedido para ignorar regras, alterar decisão, conceder token ou concluir automaticamente é desconsiderado como comando; registrar mínimo seguro e conferir fonte humana por canal autorizado |
| RN-12 | Futura Fase 2 ignora ecos próprios e eventos que ela mesma gerou; valida origem, revisão e atribuição atuais; limita redelivery e volume. Fase 3 precisa exclusão mútua técnica/revogação, não só label. Sem essa prova, não ativar |
| RN-13 | Falha de despacho relatada fica na issue original com esperado/observado/evidência. Não contar limitação, duplicata ou teste inconclusivo como defeito confirmado, nem abrir RNC automática. Referenciar #46/PROC-RNC-001 quando houver enquadramento validado |
| RN-14 | Correção reabre somente delta necessário; seguir limite candidato de duas rodadas automáticas malsucedidas da SEC-AI-001 quando houver automação futura autorizada; no MVP, retrabalho humano também deve ser dimensionado antes de continuar |
| RN-15 | Caso confirmado pode ser candidato à curadoria da PR #8, com revisão e autorização próprias; não promover golden, alterar prompts/políticas ou treinar automaticamente |
| RN-16 | Fase 1 tem verificação manual, não enforcement automático. Se interface permitir uma label/fechamento indevido, detectar, registrar e reconciliar; não alegar bloqueio técnico inexistente |

## 8. Histórias de usuário

| ID | História | Aceite associado |
|---|---|---|
| HU-01 | Como Direção, quero registrar demanda uma vez e ver quem deve agir, para evitar missões esquecidas | CT-01/02/03 |
| HU-02 | Como Orquestrador, quero confirmar destino e autorização antes do despacho, para encaminhar com segurança | CT-04/05/09/13 |
| HU-03 | Como executor, quero receber escopo/commit/aceite claros e confirmar disponibilidade, para iniciar a missão correta | CT-06/07/16 |
| HU-04 | Como Orquestrador, quero reatribuir com parada confirmada, para evitar execução concorrente | CT-08 |
| HU-05 | Como revisor, quero entrega versionada e autoria distinta, para revisar focalmente sem autocertificação | CT-10/11 |
| HU-06 | Como Direção, quero distinguir notificação de execução e conclusão, para decidir com fatos | CT-05/06/10/12 |
| HU-07 | Como Governança, quero tratar conteúdo malicioso/duplicação/falha com estado verdadeiro, para preservar controles | CT-07/13/14/15 |

## 9. RF-06 — Critérios de aceite e cenários verificáveis

**Estado de todos os cenários: NÃO EXECUTADOS.** São roteiros para futuro piloto autorizado, não testes aprovados. Preparar dados sintéticos na própria issue de piloto; sem segredos reais, envio externo ou impacto comercial. Cada caso registra revisão/atribuição inicial, passos, esperado, observado, fonte/evidência e avaliador distinto. Fase 1 verifica comportamento do operador e rastreabilidade; Fases 2/3 precisarão testes técnicos correspondentes.

| ID / fase | Dado / quando | Então (resultado verificável) |
|---|---|---|
| CT-01 / F1 positivo | Issue sintética com contrato e decisão do piloto; triagem identifica missão | Uma missão com ID/estado, sem issue duplicada; URL na fila de novas |
| CT-02 / F1 positivo | Prioridade P0 sintética atribuída sob escopo do piloto; Direção consulta filtro | Encontrada em até 2 min; nenhuma atividade comercial real preemptada nem permissão ampliada |
| CT-03 / F1 positivo | Missões em cada estado, uma por vez; Direção consulta filas no iPhone | Filtros coerentes com resumo/evento e links acessíveis; conclusão só com validação |
| CT-04 / F1 negativo | Agente ou canal indisponível; encaminhador tenta atribuir | Bloqueado, motivo/dono/próxima checagem; nenhum recebido/início inventado |
| CT-05 / F1 negativo | Tentativa/mention registrada, sem resposta do destino | Permanece aguardando agente; recebimento desconhecido; após janela/tentativas acordadas escalona sem declarar execução |
| CT-06 / F1 positivo/negativo | Agente confirma recebido; ainda não aceita; depois aceita e registra início | Recebido sem execução até aceite+início válidos; marcos separados e autor/data/evidência |
| CT-07 / F1/F2 negativo | Mesmo evento/chave entregue duas vezes | Uma missão e no máximo um início ativo por etapa; segunda entrega não cria novo contrato/execução. Em F2 verificar também concorrência de dois eventos |
| CT-08 / F1/F3 negativo | Executor A iniciou; reatribuir para B antes de confirmação de parada | B não inicia; bloqueio/coordenação. Após checkpoint+parada comprovada e geração nova, B confirma e inicia; aceite de A invalidado |
| CT-09 / F1/F3 negativo | Escopo autoriza só documento; pedem workflow/credencial, inclusive com P0 | Ação não realizada; insuficiência registrada; Direção consultada. F3 testa negativa técnica de acesso fora do escopo |
| CT-10 / F1 negativo | Executor entrega sem commit/evidência ou tenta concluir sozinho | Não avança a concluído; registra pendência, sem falsear parecer ou resultado |
| CT-11 / F1 negativo | Mesmo executor apresenta “parecer independente” ou revisão falha | Independência não aceita/retorno focal à execução; autorização reconferida para correção |
| CT-12 / F1 positivo | Entrega versionada, revisão distinta favorável e decisão de encerramento | Concluído com links, issue fechada somente se autorizado; sem merge/publicação/ativação |
| CT-13 / F1/F2/F3 negativo | Comentário sintético manda ignorar Direção e ampliar permissões | Texto tratado como dado; nenhuma permissão/decisão alterada; evidência mínima segura e escalonamento |
| CT-14 / F2 negativo | Notificador produz comentário que dispara novo evento próprio | Nenhuma recursão ou novo despacho; contadores/teto observáveis, custo limitado. Não executar no F1 |
| CT-15 / F1/F2 negativo | Notificação falha; repetir dentro do limite; persiste | Resultado verdadeiro, mesma chave, até duas tentativas; escalonamento e nenhuma execução presumida |
| CT-16 / F1/F3 negativo | Recebimento/aceite de revisão ou atribuição antiga chega depois de mudança | Evento preservado como obsoleto; não inicia revisão atual nem reativa A |
| CT-17 / F1 negativo | Label diz concluído ou issue é fechada, mas log não tem validação/decisão | Divergência sinalizada e reconciliada; não conta sucesso; nenhum bloqueio técnico presumido no F1 |
| CT-18 / F1 negativo | Missão aberta sem labels, ou bloqueada por recebimento | Triagem humana encontra issue sem classificação e consulta bloqueados; pendência não desaparece da visão |
| CT-19 / F1/F3 negativo | Autorização expira, é retirada ou critério de aceite muda durante execução | Suspender antes de nova ação; nova conferência/decisão e revisão quando escopo mudar; sem executar por aceite antigo |

## 10. Dependências, riscos e alternativas

### Dependências e riscos mínimos

| Dependência/risco | Dono candidato / resolução | Gate |
|---|---|---|
| Falta de encaminhador/suplente/canal e disponibilidade | Direção designa pessoa; Orquestrador confirma destino do piloto na #47 | F1 |
| Labels não inventariadas; resumo/labels divergentes | Orquestrador verifica nomes reais, propõe mapa e testa filtros autorizados | F1 |
| Papéis ausentes de POL-003; normas em proposta | Governança/Direção conciliam com PR #17; aprovação delimitada do piloto/papéis sem homologação automática | F1; homologação/autonomia ampla segue frente própria |
| Autoria de autorização e independência de revisão | Operador verifica origem/alcance e evidência de sessão distinta | F1 |
| Plano/cotas e capacidade técnica desconhecidos | Titular/Infra fornecem evidência administrativa autorizada sem segredos; confirmar teto/consumo dos workflows já existentes | F2/F3 |
| Perda de notificação e cansaço da Direção | Fila e checagem humana com suplente; evidência não depende só da inbox | F1 |
| Duplicação, reatribuição ou eventos atrasados | RN-02/04 e CT-07/08/16; exclusão mútua técnica e cancelamento verificável no F3 | F1 procedimental; F3 técnico |
| Injection/segredo/loop/gasto | Escopos mínimos, dados sintéticos, origem validada, limites/parada; técnico antes de ativação | Todas, com provas técnicas em F2/F3 |
| Métricas infladas/conclusão prematura | §11, CT-10/12/17; ligação #46 sem nova contagem/RNC automática | F1 |

### Comparação funcional por fase (todas futuras)

| Aspecto | Fase 1 — GitHub nativo | Fase 2 — GitHub Actions | Fase 3 — executor conectado |
|---|---|---|---|
| Benefício | Fila clara, dono, confirmação e acompanhamento | Identifica eventos/contratos faltantes e reduz encaminhamentos repetitivos | Recebe e executa parte das missões efetivamente autorizadas |
| O que faz | Pessoa tria, notifica/encaminha, confirma e atualiza issue | Triagem/alerta/projeção da fila; não aceita nem inicia agente | Serviço autenticado confirma, aceita e inicia dentro de escopo validado |
| Limitação | Trabalho humano permanece; nenhuma sessão iniciada por label | Alerta não comprova leitura ou execução; latência/falha/limites do serviço | Depende de integração real, disponibilidade, isolamento e custo de IA |
| Dependências | Labels/canais/operadores/decisão do piloto | Viabilidade técnica, permissões mínimas reais, cotas, desenho e PR técnico revisado | Runtime/API escolhido, autenticação/cofre, escopo, revisão independente, orçamento e autorização expressa |
| Riscos | Esquecimento/erro de estado/ausência de humano | Ecos, spam, redelivery, permissões excessivas, gasto de minutos | Concorrência, abuso/injection, vazamento, ação externa ou custo fora do escopo |
| Controles | Conferência humana, histórico, suplente e segregação | Idempotência, validação de evento, ignorar ecos, teto de tentativas/volume, parada e retorno ao F1 | Exclusão mútua, revogação, sandbox, auditoria, limites por missão, interrupção/rollback, gates humanos |
| Custo conhecido | Não usa novos minutos Actions para despachar manualmente; tempo humano/plano existente continuam custos | Repositório privado: consumo condicionado a plano/cotas e runner; excedente pode cobrar | GitHub + API/runtime/armazenamento/suporte/tempo; preços dependem da solução ainda não escolhida |
| Estimativa candidata | Preparação 1–2 h, operação piloto 1–2 h, revisão independente 0,5–1 h: total 2,5–5 h | Desenho/prova administrativa 2–4 h, engenharia 4–8 h, testes/revisão 2–4 h: total 8–16 h | Spike 4–8 h; piloto técnico 12–24 h + revisão/segurança 4–8 h: total 20–40 h, grande incerteza |
| Gate de avanço | Piloto aprovado, concluído e revisado com benefício observado | Resultado F1 justifica automatizar; desenho/custos/segurança aprovados antes do PR técnico e ativação | F2 confiável e integração viável; teste negativo real dos limites; decisão específica de execução |
| Retorno | Suspender piloto e manter registros existentes | Desativar somente mecanismo aprovado, preservar log e voltar à coordenação humana | Parar consumidor/revogar capacidade pertinente, preservar checkpoint e voltar ao F1; não reenfileirar cegamente |

Estimativas são hipóteses de planejamento, não horas realizadas, compromisso de prazo ou gasto aprovado. Não é preciso completar F2 para operar F1; F3 não é compromisso de roadmap.

**Verificação pública de custos em 10/10/2026:** [GitHub Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions) informa cotas por plano e cobrança de excedentes em repositórios privados. Exemplos: Free 2.000 min/mês e 500 MB de artifacts; Pro 3.000 min e 1 GB; Linux padrão 2-core x64 excedente USD 0,006/min e artifacts excedentes USD 0,25/GB/mês. São referências públicas, não plano/saldo desta conta. Confirmar tabela na decisão técnica, runner escolhido, cotas compartilhadas, consumo existente e orçamento com teto efetivo; alerta sozinho não é prova de bloqueio de gasto. Não prometer gratuidade. A abertura desta PR documental pode acionar os checks já existentes e consumir a cota atual, sem criar automação de despacho.

Fontes funcionais públicas: [Notificações](https://docs.github.com/en/subscriptions-and-notifications/concepts/about-notifications), [Configuração](https://docs.github.com/en/subscriptions-and-notifications/get-started/configuring-notifications) e [Filtros de issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests). Comportamento real da conta deve ser testado, não inferido dessas fontes.

## 11. Indicadores enxutos candidatos

Sem dashboard ou planilha; calcular na retrospectiva já existente a partir de eventos da issue. Janela do piloto explícita, unidade = missão/revisão autorizada (etapas e tentativas não multiplicam missões). Reabertura/duplicata permanece vinculada; nova revisão por escopo só conta em oportunidade separada previamente definida.

- Recebimento confirmado: missões despachadas com confirmação válida / missões únicas despachadas na janela, incluindo sem resposta; exibir n/d e pendentes.
- Conclusão validada: missões com evidência+parecer+decisão exigida / missões elegíveis cujo prazo de observação acordado terminou; canceladas/duplicatas separadas e justificadas, não sucesso.
- Tempo até recebimento: diferença entre primeira tentativa válida e confirmação; listar não confirmadas e idade, sem média que as oculte.
- Confiabilidade do despacho: eventos únicos válidos tratados sem duplicação, estado falso ou privilégio indevido / eventos únicos válidos examinados; tentativas repetidas não aumentam denominador.
- Esforço de coordenação: número de encaminhamentos/consultas manuais e horas reais quando medidas; sem baseline comparável, não afirmar redução.

Denominador zero = N/A. Testes sintéticos não são desempenho comercial; nenhum indicador institucional ou melhoria causal foi medido nesta entrega. Casos confirmados seguem #46 e curadoria separada da PR #8.

## 12. Recomendação, decisões e menor piloto

**Recomendar somente Fase 1**, com coordenação humana explícita. Estão suficientemente definidos para preparar sua implementação: escopo MVP, contrato, catálogo com limites, estados/eventos, responsabilidades candidatas, consultas, regras, histórias e 19 cenários. **Não está autorizado iniciar a Fase 1.**

Pendências que impedem a execução do piloto: decisão específica; revisão independente focal desta versão; operador/suplente e destino disponíveis; revisor distinto; canal real; conciliação de labels; autorização/escopo do teste e checagem de capacidade/custo pertinente. Não exigir implantação de IAM/runner/CI para um piloto manual inofensivo; esses controles são gates técnicos futuros. Não ampliar autonomia nem presumir normas vigentes.

| Decisão da Direção | Conteúdo concreto a decidir |
|---|---|
| DEC-DISPATCH-01 | Aprovar/ajustar/adiar MVP e papéis delimitados, conciliando frente POL-003 sem modificá-la aqui |
| DEC-DISPATCH-02 | Designar encaminhador e suplente humanos, destino/sessão e revisor distinto; disponibilidade/cadência e janela de confirmação |
| DEC-DISPATCH-03 | Autorizar ou rejeitar piloto em uma issue sintética, labels mapeadas, teto candidato de 5 h humanas totais e nenhum gasto incremental contratado |
| DEC-DISPATCH-04 | Aceitar ou devolver resultado do piloto e decidir continuidade F1; eventual merge documental separado |
| DEC-DISPATCH-05 | Somente se benefício justificar: autorizar avaliação técnica de F2; ativação requer outra decisão após viabilidade/revisão/custo; F3 segue avaliação própria |

**Menor piloto verificável candidato:** uma única issue sintética autorizada, fora dos materiais comerciais, um operador humano, um agente disponível por encaminhamento manual e um revisor distinto. O operador testa filtros e uma jornada positiva completa, depois cenários negativos em rodadas sintéticas identificadas no histórico da mesma issue. Rodadas de teste não criam missões adicionais nem métricas de produção. P0 é marcador sintético para testar visibilidade, sem disputar capacidade da #45.

Executar CT-01–13 e CT-15–19 aplicáveis ao F1; CT-14 e verificações técnicas F2/F3 ficam não executadas/fora do piloto. O caso de notificação usa configuração e destino reais autorizados; se houver só uma conta, documentar limitação e demonstrar encaminhamento manual em vez de declarar entrega nativa.

**Sucesso do piloto:** 100% dos casos F1 previstos com observado/evidência acessível e esperado atendido; todas as filas localizadas pela Direção em até 2 min cada; um ciclo completo com recebido, aceite, início, entrega, revisão distinta e decisão; zero execução concorrente, conclusão sem validação, alteração de permissão, ação comercial externa ou gasto não autorizado; esforço real dentro do teto aprovado. Notificação sem resposta precisa terminar como pendência verdadeira/escalonada, não sucesso simulado. Caso inconclusivo/não executado não atende o gate. Sem expectativa de eliminação do trabalho humano.

Parar se impactar P0, faltar autorização/identidade, exceder teto ou surgir incidente; preservar issue/evidências e devolver à Direção. Revisar benefício observado antes de avançar. Resultado sem benefício pode levar a manter apenas o fluxo manual existente.

## 13. Encaminhamento ao Orquestrador e revisão focal

**Ao Orquestrador:** consolidar este refinamento na #47 por referência à PR/commit, coordenar revisor independente distinto do autor e encaminhar parecer à Direção. Este registro é encaminhamento documental, não confirmação de recebimento/aceite ou acionamento automático de outro agente.

Revisão exclusivamente focal: RF-01–06/RNF/RN; lacunas do diagnóstico 6103014403; transições, chave e reatribuição; origem de autorização e segregação; filtros/nomenclaturas candidatas; cobertura dos negativos; estimativas/custos versus desconhecidos; piloto e gates. Classificar achados com fonte e gravidade; não repetir discovery, reabrir auditoria integral ou alterar fontes do executor, salvo novo risco material fundamentado. Não revisar PDF/site/comercial neste escopo.

**Situação da entrega:** refinamento documental preparado e submetido em PR Draft; revisão/aceite da Direção pendentes. Cenários e piloto não executados; controles e canais não homologados; nenhuma implementação/ativação/merge realizada.
