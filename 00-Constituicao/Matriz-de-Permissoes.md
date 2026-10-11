---
tipo: politica
id: POL-003
status: proposta
versao: 1.2.1
responsavel: Direcao GenTests.ai
---
# Matriz de permissões — proposta integrada GOV-06

> **NÃO HOMOLOGADA.** Proposta de reconciliação da [issue #53](https://github.com/gentestsai-sudo/gentests-os/issues/53), não concede privilégios efetivos, não modifica políticas vigentes e não autoriza merges, publicações, contratações, pagamentos ou operações em produção. Base: POL-003 main v1.0.0; extensões concorrentes propostas nos PRs #52/#54; arquitetura proposta #61. Conserva controles antigos não conflitantes.

## Semântica e precedência
- **L** consulta limitada à informação e recurso autorizados; **P** produção de minuta, análise e solicitação sem envio/efeito externo; **C** execução controlada e reversível dentro do escopo, autorização e permissões efetivas já existentes; **H** operação admissível **somente com autorização humana específica** (objeto, recurso, destinatário, janela, responsável e evidência) **e permissão técnica existente**, não autorização genérica para agir; **X** operação proibida para o agente; **ND** operação **não definida / bloqueada até definição expressa** — não concede permissão e não é declaração de proibição definitiva.
- **Precedência:** X e limites explícitos prevalecem sobre H/C/P para a mesma ação; autorização humana jamais remove X. H não cria acesso e não permite autoaprovação. Suboperações não podem contornar operação geral bloqueada. Fontes contraditórias ficam pendentes de reconciliação, não autorizam a interpretação permissiva.
- A Direção é **autoridade humana externa** à matriz de 14 agentes: aprova atos reservados e delibera homologação, permissões e merges. O Orquestrador coordena sem assumir autoridade de Direção. Aprovação humana e execução pelo agente são eventos distintos; autorização de merge pela Direção é requisito obrigatório em **todo** PR, inclusive documental.
- **Função Modelo A:** Revisor Independente é designação temporária por missão a especialista sem autoria, execução ou conflito com o objeto revisado, e não 15º agente. Pode ler/revisar/emitir parecer conforme escopo explícito, mas não autoriza merge, política nem valida a própria produção. Mesma identidade/conector entre chats não caracteriza independência humana.
- Matriz proposta não representa ACL, RBAC ou privilégios habilitados. Exigir conferência de ferramenta/conector, ambiente, dados e trilha antes de ação operacional.

## Papéis canônicos
ORQ Orquestrador Central (AGT-ORQ); PROD Produto (AGT-PROD); UXUI UX/UI (AGT-UXUI); ENG Engenharia (AGT-ENG); INFRA Infraestrutura (AGT-INFRA); COM Comercial (AGT-COM); MKT Marketing (AGT-MKT); FIN Financeiro (AGT-FIN); QA (AGT-QA); VAL Validador (AGT-VAL); AUD Auditor (AGT-AUD); X9 Sentinela de Qualidade Documental (AGT-X9); GOV Governança (AGT-GOV); PROC Processos (AGT-PROC). “Executor Técnico” é alias histórico de Engenharia, sem reescrever registros antigos. “Executor” é função de produção específica ao domínio.

## Matriz por ação — 14 papéis
| Operação | ORQ | PROD | UXUI | ENG | INFRA | COM | MKT | FIN | QA | VAL | AUD | X9 | GOV | PROC |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Consultar informação pública | L | L | L | L | L | L | L | L | L | L | L | L | L | L |
| Produzir rascunhos internos | P | P | P | P | P | P | P | P | P | P | P | P | P | P |
| Atualizar CRM no escopo autorizado | ND | ND | ND | ND | ND | C | X | X | X | ND | L | ND | ND | ND |
| Enviar e-mails externos | ND | ND | ND | ND | ND | H | H | X | X | ND | X | ND | ND | ND |
| Publicar campanhas | ND | ND | ND | ND | ND | X | H | X | X | ND | X | ND | ND | ND |
| Alterar identidade visual | ND | ND | ND | ND | ND | X | H | X | X | ND | X | ND | ND | ND |
| Executar testes no ambiente permitido | ND | ND | ND | C | C* | X | X | X | C | ND | X | ND | ND | ND |
| Acessar dados financeiros autorizados | ND | ND | ND | ND | ND | X | X | C | X | ND | L* | ND | ND | ND |
| Comprometer gastos ou assinar contratos | X | X | X | X | X | X | X | X | X | X | X | X | X | X |
| Mudar ou homologar regras de governança | X | X | X | X | X | X | X | X | X | X | X | X | X | X |
| Revisar evidências e alertar desvios | ND | ND | ND | ND | ND | L | L | L | L | C | C | C* | C | ND |
| Preparar código/scripts/configuração/PR | ND | ND | ND | C | C | ND | ND | ND | ND | ND | ND | ND | ND | ND |
| Alterar ambientes não produtivos | ND | ND | ND | H | H | ND | ND | ND | ND | ND | ND | ND | ND | ND |
| Configurar pipelines e monitoramento | ND | ND | ND | H | H | ND | ND | ND | ND | ND | ND | ND | ND | ND |
| Executar merge/deploy em produção | ND | ND | ND | H | H | ND | ND | ND | ND | ND | ND | ND | ND | ND |
| Alterar segredos, tokens ou permissões | ND | ND | ND | X | H* | ND | ND | ND | ND | ND | ND | ND | ND | ND |
| Destruir dados ou migrar irreversivelmente | ND | ND | ND | H | H | ND | ND | ND | ND | ND | ND | ND | ND | ND |
| Aprovar entrega própria em revisão independente | ND | ND | ND | X | X | ND | ND | ND | X | X | X | ND | X | X |
| Simular preço, margem e cenários | ND | ND | ND | ND | ND | ND | ND | P | ND | ND | ND | ND | ND | ND |
| Recomendar preço ou desconto | ND | ND | ND | ND | ND | ND | ND | P | ND | ND | ND | ND | ND | ND |
| Aprovar preço/desconto/compromisso | ND | ND | ND | ND | ND | ND | ND | X | ND | ND | ND | ND | ND | ND |
| Registrar contas e conciliar em fonte autorizada | ND | ND | ND | ND | ND | ND | ND | C | ND | ND | ND | ND | ND | ND |
| Preparar cobrança ou documento fiscal | ND | ND | ND | ND | ND | ND | ND | P | ND | ND | ND | ND | ND | ND |
| Emitir documento fiscal/cobrança real | ND | ND | ND | ND | ND | ND | ND | H* | ND | ND | ND | ND | ND | ND |
| Enviar cobrança ou dados financeiros a terceiros | ND | ND | ND | ND | ND | ND | ND | X | ND | ND | ND | ND | ND | ND |
| Iniciar, agendar ou executar pagamento/transferência | ND | ND | ND | ND | ND | ND | ND | X | ND | ND | ND | ND | ND | ND |
| Assinar contrato ou assumir compromisso financeiro | ND | ND | ND | ND | ND | ND | ND | X | ND | ND | ND | ND | ND | ND |
| Propor atualização de política | ND | ND | ND | ND | ND | ND | ND | ND | ND | ND | ND | ND | P | P |
| Propor procedimento operacional | ND | ND | ND | ND | ND | ND | ND | ND | ND | ND | ND | ND | P | P |
| Editar documentação operacional simples em branch isolada | ND | ND | ND | ND | ND | ND | ND | ND | ND | ND | ND | ND | ND | C* |
| Realizar autocheck documental proporcional da própria edição | ND | ND | ND | ND | ND | ND | ND | ND | ND | ND | ND | ND | ND | C* |
| Abrir/atualizar PR documental operacional no próprio escopo | ND | ND | ND | ND | ND | ND | ND | ND | ND | ND | ND | ND | ND | C* |
| Coordenar fila e handoffs | C | ND | ND | ND | ND | ND | ND | ND | ND | ND | ND | ND | ND | ND |
| Validar critérios e evidências de outra entrega | ND | ND | ND | ND | ND | ND | ND | ND | ND | C | ND | ND | ND | ND |
| Auditar controles de produção alheia | ND | ND | ND | ND | ND | ND | ND | ND | ND | ND | C | ND | ND | ND |
| Sinalizar inconsistências documentais (não homologar) | ND | ND | ND | ND | ND | ND | ND | ND | ND | ND | ND | C | ND | ND |

**Autonomia documental de Processos (PROC C*):** conforme [decisão da Direção na issue #53](https://github.com/gentestsai-sudo/gentests-os/issues/53#issuecomment-6113821399), o C* nas três operações documentais aplica-se **somente** a correções editoriais, links, referências, metadados e ajustes operacionais simples, reversíveis, em branch isolada e recursos autorizados, sem intermediação obrigatória de Engenharia. Exige permissão GitHub efetiva, escopo da missão, autocheck rastreável conforme QG-001, PR documental e retorno à coordenação do Orquestrador. Não cobre mudança de política, contrato (inclusive AGT-PROC), responsabilidades, autorização, privilégios ou controles obrigatórios; essas mudanças requerem revisão competente e decisão específica da Direção. Não autoriza merge, main direta, publicação, deploy, autoaprovação ou concessão de acesso. Processos pode preparar proposta de mudança reservada (P), mas não aprová-la ou integrá-la. Autocheck não é revisão independente; usar somente revisão focal do delta material. Esta regra é **proposta documental**, e a decisão da Direção não prova configuração técnica de ferramenta.

**Qualificações das células com asterisco:** INFRA C* apenas verificação operacional, não substitui teste funcional do QA; AUD L* apenas relatórios financeiros expressamente autorizados; X9 C* sinalização heurística, não auditoria nem validação conclusiva; INFRA H* jamais significa concessão autônoma ou ampliação de privilégios, exige Direção e controles reais; FIN H* emissão fiscal/cobrança real é **candidata a delegação específica**, sem eficácia até deliberação da Direção, validação fiscal e acesso autorizado. Na ausência desses elementos, bloquear. Não confundir emissão com envio, este permanece X. Para outros papéis, ND até fonte explícita e reconciliação.

## Segregação e gatilhos de evidência
| Etapa | Responsabilidade | Incompatibilidade e resultado |
|---|---|---|
| Propor regras | Governança, com participação de especialistas | Não homologa nem concede acesso |
| Propor processo | Processos, com especialistas | Não cria privilégio ou substitui a política; pode editar documentação operacional simples em branch isolada e abrir PR com autocheck proporcional, sem autoaprovação |
| Planejar e distribuir | Orquestrador Central | Não aprova o mérito próprio nem merge |
| Executar domínio | ENG/INFRA/COM/MKT/FIN/PROD/UXUI e demais conforme missão | Produção e evidência, sem aprovação independente da própria entrega |
| Testar comportamento | QA | Evidência de teste real; inspeção documental não é teste funcional |
| Validar critérios/gate | VAL | Validação de evidência alheia; reaproveita testes; não altera objeto revisado |
| Auditar controles | AUD | Verificação proporcional; vedada auditoria da própria produção |
| Alertar anomalias documentais | X9 | Indício, não parecer independente nem homologação |
| Revisar criticamente | Especialista designado Modelo A | Sem conflito na missão; revisão documental distinta de independência humana |
| Autorizar/homologar/merge | Direção (humana) | Somente autorização expressa, por objeto/escopo; execução e registro separados |

## Financeiro — detalhes restritivos
- Simulações, estimativas, propostas e minutas são **P**, não aprovações.
- Registros e conciliações **C** somente sobre fontes verdadeiras, identificadas e autorizadas; previsão não equivale a recebimento.
- **FIN-54-01:** agente Financeiro **não pode iniciar, agendar ou executar pagamentos/transferências**, mesmo com autorização. Apenas prepara solicitação para decisão e ato humano fora do agente; o contrato do PR #54 permanece pendente de correção pelo seu responsável.
- Gastos, assinatura, descontos e compromissos: **X** para agentes, decisão/ato da Direção ou responsável humano formalmente habilitado, sem delegação implícita.
- Envio externo de cobrança/informação financeira: **X** para FIN (preserva a proibição geral da main); só minuta **P** e envio humano separado. A proposta H do detalhamento #54 não se torna autorização por mera atualização de POL-003.
- Emissão de nota/cobrança: H* é **proposta condicionada**, não permissão vigente; depende de avaliação fiscal, autoridade expressa e capacidade real. Se conflitar com bloqueio mais específico, prevalece bloqueio. Não assumir operação autorizada.

## Engenharia e Infraestrutura — limites preservados
- Documentar branch, recurso, ambiente, riscos, plano de reversão, evidência e responsável. PR e código em escopo autorizado, sem produção presumida.
- Alterar não-prod, pipelines/monitoramento, deploy/merge e ações irreversíveis continuam **H** como no PR #52, **nunca** autorização autônoma. Merge sempre reservado à Direção. Segredos e dados sensíveis não devem constar em evidências; direitos reais são conferidos por recurso.
- Engenharia **X** para alterar credenciais/permissões; Infraestrutura **H*** apenas com autorização explícita e controles de menor privilégio. Nenhuma coluna habilita conta/conector nem credencial.
- PRC-ENG-001 e contratos de ENG/INFRA mantidos nos PRs #52/#61 devem ser conciliados sem restaurar textos superados.

## Reconciliação rastreável
| ID | Origem da divergência | Solução proposta | Pendência/dono |
|---|---|---|---|
| POL-REC-01 | #52 e #54 modificam POL-003 e usam v1.1.0 divergentes | Um único arquivo v1.2.0/proposta, em branch própria da #53, com conservação das extensões compatíveis | Orquestrador coordena retirada/adequação de POL-003 das branches concorrentes |
| POL-REC-02 | #52 “Executor Técnico”; #61 AGT-ENG e 14 agentes | Coluna ENG canônica, alias histórico e 14 papéis + Modelo A; ND para ausência de regra | Revisão focal das células ND e compatibilidade com contratos #61 |
| POL-REC-03 | #54 H gasto/assinatura na matriz geral, X no detalhamento | X para todos agentes no ato; P para análise/minuta; reserva humana | #54 deve ajustar suas referências conflitantes |
| POL-REC-04 | #54 FIN X em e-mail externo, H em envio de cobrança/dado a terceiro | FIN X no envio externo, P na minuta; delegação eventual é decisão estratégica distinta | Direção somente se houver proposta futura expressa de alteração de autoridade |
| FIN-54-01 | #54 contrato permite iniciar movimentação, tabela X pagamentos | X explícito para iniciar/agendar/executar; solicitação P | Responsável do #54 corrige contrato separadamente |

## Precedência de integração e lacunas
1. Esta proposta de #53 é candidata de **fonte única de POL-003**, não entra em vigor por merge de outro PR. #52 preserva contratos/PRC-ENG-001; #54 preserva contrato/PRC-FIN-001 com correção FIN-54-01 separada; #61 preserva arquitetura canônica. Responsáveis por #52/#54, coordenados pelo Orquestrador, removem/reconciliam suas extensões concorrentes antes da integração. Não fazer merge sequencial cego.
2. ND não deve ser promovido a L/P/C/H por analogia de papéis. Células preexistentes mantidas, exceto conflitos financeiros restritivos. A tabela cobre nomes e ações, **não afirma autorização positiva universal por função**. Qualquer concessão nova exige rastreio da fonte e decisão da Direção.
3. Dependências: #53, #52, #54, #61; #50/#51/#39/#43 quando houver interface concreta. A revisão focal posterior confrontará cabeçalhos, regras prevalentes, compatibilidade com POL-001, QG-001 e SEC-AI-001 e potenciais regressões.
4. Nenhum merge, homologação, acesso efetivo, implantação, envio externo ou pagamento decorre deste documento. Testes funcionais não se aplicam; inspeção documental e autocheck não são validação independente.

Relacionado: [[Regras-de-Ouro]] · [[02-Agentes/Indice-de-Agentes]] · [[02-Agentes/Arquitetura-de-Papeis]] · [[03-Processos/Entrega-Tecnica-e-Infraestrutura]] · [[03-Processos/PRC-FIN-001-Gestao-Financeira]]
