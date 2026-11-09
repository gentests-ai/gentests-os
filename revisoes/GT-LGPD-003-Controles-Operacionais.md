---
id: GT-LGPD-003
tipo: procedimento-operacional-privacidade
versao: 0.2.1
status: proposta-nao-implementada
data: 2026-10-10
---
# GT-LGPD-003 — Controles operacionais: registro, retenção, direitos e incidentes

> Fluxo candidato sem ativação. Reusar GitHub para decisões **sem copiar dados pessoais**, CRM Sheets para oportunidades se aprovado e caixa de e-mail controlada; não criar banco ou software novo.

## 1. Registro mínimo de atividades (ROPA simplificado)
Por operação: `id`, controlador, finalidade, titular, dados, origem, hipótese art. 7/11 quando aplicável, fornecedores/suboperadores, países, destinatários, segurança, prazo e gatilho de exclusão, fonte de autorização, canal de direitos, responsável, data e revisão. Registro técnico deve usar IDs e metadados não sensíveis; **não versionar lista de contatos, mensagens e consentimentos individuais no GitHub**. Aplicação de simplificações para pequeno porte somente após verificação dos requisitos da Res. 2/2022.

## 2. Ciclo de dados e retenção
1. **Receber:** validar finalidade, base, minimização, aviso e acesso; não solicitar credenciais, dados sensíveis ou anexos técnicos privados em landing page.
2. **Registrar:** criar ID único por oportunidade/solicitação e vincular origem e preferência, minimizando cópias no Gmail/Sheets/Drive. Não inferir que CRM está sincronizado.
3. **Acessar:** permissões individuais estritamente necessárias, MFA quando disponível, inventário de compartilhamento e revogação na saída de operadores.
4. **Revisar retenção:** prazo começa do evento definido por finalidade (ex. conclusão do atendimento, último contato válido ou revogação). **Prazos numéricos NÃO aprovados:** exigir decisão específica para formulário, leads, CRM, e-mails, registros de consentimento, backup, logs e evidência de incidente. Retenção após revogação somente nas hipóteses legais necessárias e fundamentadas; registro mínimo de oposição pode precisar persistir para evitar novo contato.
5. **Excluir/anonimizar:** localizar todas as cópias autorizadas em FormSubmit (se persistir), Gmail, Sheets, Drive, exportações e backups; executar procedimento conforme capacidades reais e prazos aplicáveis; registrar ID, data, responsável, sistemas verificados e justificativa de eventual retenção legal **sem expor o conteúdo apagado**.
6. **Revisar fornecedores:** termos/DPA, acesso, logs, apagamento, transferência e responsabilidade por incidente. Não assumir que e-mail excluído some dos backups externos.

## 3. Direitos dos titulares
Canal único a designar pela Direção. Receber pedido com protocolo e data; confirmar identidade por medida proporcional (evitar pedir CPF/cópia de documento por padrão); classificar direito e operação; localizar registros pelo identificador autorizado; avaliar restrições legais; atender gratuitamente nos casos previstos e comunicar resposta segura em linguagem clara. Para confirmação e acesso, observar resposta simplificada imediata quando aplicável e declaração completa em até 15 dias, salvo regime legal específico; verificar exceções/regime de pequeno porte antes de fixar SLA geral. Outros pedidos devem ser acompanhados até resposta nos prazos legalmente aplicáveis; não prometer prazo universal fictício. Registrar protocolo, categoria, sistemas consultados, responsável, decisão, data e resposta, com dados minimizados. Pedido de exclusão/retirada de consentimento deve atualizar lista de supressão e impedir novo contato comercial pelo mesmo fundamento. Escalar dúvidas à Direção e jurídico.

## 4. Resposta a incidente envolvendo dados pessoais
**Detectar e conter imediatamente:** bloquear credencial/sessão comprometida, preservar evidência minimizada, isolar fluxo afetado sem destruir rastreabilidade. **Classificar:** dados, número de titulares, sensibilidade, possibilidade de identificação, exposição, fonte, destinatários, impacto e medidas de contenção. **Escalar** prontamente ao controlador/Direção e responsável técnico; solicitar aconselhamento jurídico quando necessário. **Decidir notificação:** avaliar risco ou dano relevante nos termos do art. 48 LGPD e Resolução CD/ANPD 15/2024. Regra geral para incidentes notificáveis: comunicação à ANPD e titulares pelo controlador no prazo regulamentar de **3 dias úteis contados do conhecimento**, ressalvadas hipóteses legais/regulatórias específicas, inclusive tratamento diferenciado quando cabível; confirmar marco inicial, conteúdos exigidos, complementações e regime aplicável com jurídico. Não postergar triagem aguardando reunião. **Recuperar:** testar restauração, revogar/rotacionar segredos se aplicável, documentar causa e ação preventiva, validar encerramento por autoridade competente. Preservar registro de incidentes conforme prazo legal/regulatório confirmado, com acesso restrito.

## 5. RACI leve e evidências
Direção/controlador: finalidade, bases, aprovações, resposta final e decisão de notificar. Operador comercial: atende solicitações autorizadas, atualiza preferências/CRM e encaminha direitos. Infra: inventaria acesso/segurança, logs, backups, fornecedores e executa contenção autorizada. Revisor independente: confirma evidências e limites sem acessar dados reais nesta etapa. Agente de IA: somente apoio com exemplos fictícios, **sem base de leads ou dados de titulares**. Evidências futuras: capturas sanitizadas de configuração, ensaios com fixture sintética e trilha de decisão; nunca anexar segredos ou base de contatos a PR.

## 6. Critério futuro de ativação
Identidade/controlador e canal aprovados; inventário de fornecedores, países e base legal fechado; avisos revisados e publicados com autorização; preferências separadas e provadas; acesso/retention/descarte testados; resposta a direitos/incidentes atribuída; contrato e transferências resolvidos; teste funcional sintético do site e parecer independente. Até lá, **não ativar novo formulário nem publicar a landing page**.


## 7. Prazos e eventos regulatórios — LGPD-REV-03
Quadro normativo candidato, **não é autorização para o controlador utilizar automaticamente prazos ampliados**. O marco de incidente é o conhecimento pelo controlador de que foram afetados dados pessoais; conter e investigar imediatamente.

| Evento | Regra geral | Possível regime de pequeno porte, somente comprovada elegibilidade | Responsável e evidência |
|---|---|---|---|
| Confirmação de tratamento/acesso simplificado | art. 19 I LGPD: acesso em formato simplificado imediatamente quando cabível | Res. 2/2022 art. 15: declaração simplificada em até 15 dias contados do pedido | responsável canal; protocolo e identidade proporcional |
| Declaração clara e completa de acesso | art. 19 II LGPD: até 15 dias do requerimento | Res. 2/2022 art. 14 III: prazo em dobro para declaração completa (observadas regras e elegibilidade) | controlador; entrada, classificação, decisão e resposta |
| Outros direitos do art. 18 | prazos conforme LGPD e regulamentos próprios aplicáveis, sem SLA universal artificial | art. 14 I Res. 2/2022: dobro apenas nas hipóteses expressamente cobertas por regulamentação; não dobrar todos os direitos por presunção | canal e jurídico; protocolo, norma aplicável e resposta |
| Incidente que possa acarretar risco ou dano relevante | Res. 15/2024 arts. 6 e 9: comunicação pelo controlador à ANPD e titulares em **3 dias úteis** do conhecimento relevante, salvo prazo específico | art. 14 II Res. 2/2022 (redação atualizada): **dobro quando cabível**, condicionado a enquadramento e exceções legais; confirmar com jurídico, não adiar contenção | controlador/segurança; data de ciência, classificação e comunicações |
| Incidente sem risco ou dano relevante demonstrado | investigar, mitigar e registrar, sem declarar notificação automática de toda falha | sem dispensa de resposta e documentação | segurança + Direção; fundamentação de risco e decisão |

A Res. 15/2024 prevê conteúdo necessário, possibilidade de comunicação complementar quando faltarem informações, e disciplina de registro de incidentes. Nem toda indisponibilidade constitui incidente notificável. **Nunca aguardar o prazo final para começar triagem ou comunicar risco crítico.** O regime pequeno porte não dispensa segurança nem pressupõe elegibilidade por faturamento ou número reduzido de pessoas. A Res. 2/2022 art. 15 (simplificada até 15 dias) **não** substitui automaticamente o prazo dobrado da declaração completa previsto no art. 14 III.

Fontes oficiais: [Resolução CD/ANPD 15/2024 — texto do ato no DOU disponibilizado pela ANPD](https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/documentos/rcis___anonimizado_final_ocultado_2_parte3.pdf); [ANPD — comunicação de incidente](https://www.gov.br/anpd/pt-br/canais_atendimento/agente-de-tratamento/comunicado-de-incidente-de-seguranca-cis); [Res. 2/2022 consolidada](https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-2-de-27-de-janeiro-de-2022). Conferir versão vigente antes de aplicar.

## 8. Matriz de retenção, cópias, revogação e supressão — LGPD-REV-05
**Nenhum prazo numérico inventado.** Direção/jurídico deverá aprovar prazo ou evento determinável, exceções e capacidade real por fornecedor antes de captura de novos leads.

| Sistema/cópia potencial | Marco inicial e regra de retenção proposta | Titular revoga/exclui — ação candidata | Responsável/prova pendente |
|---|---|---|---|
| FormSubmit / fila ou armazenamento intermediário, se existir | recebimento; apagar após entrega confirmada ou prazo técnico/contratual necessário **a definir** | requerer eliminação no prestador, localizar logs/backup aplicáveis | Infra; termos, configurações e confirmação de descarte |
| Gmail: mensagem recebida e cópias enviadas | conclusão da solicitação, com eventual guarda justificada por obrigação/defesa | remover mensagens/cópias pertinentes e conferir lixeira/retenção/backups conforme capacidade | operador atendimento; IDs sem conteúdo sensível |
| CRM Google Sheets: oportunidade e histórico | encerramento da oportunidade/último contato válido, critério aprovado | eliminar ou anonimizar campos dispensáveis, marcar oposição, impedir recriação indevida | Comercial; chave única e trilha de alteração |
| Registro mínimo de consentimento | aceite ou alteração da preferência; conservar apenas enquanto necessário para prova de base/defesa | retirar finalidade promocional de imediato; conservar prova mínima apenas com fundamento próprio e prazo definido | responsável privacidade; versão, horário, origem e situação |
| Lista de supressão / opt-out | oposição/revogação; mínimo necessário para não recontatar, com revisão da necessidade | impedir campanhas atuais e agendadas, inclusive integrações; não manter perfil completo | Comercial; teste de bloqueio e propagação |
| Drive/exportações/planilhas copiadas | momento da cópia; proibir cópia redundante e reconciliar com fonte principal | inventariar arquivos, eliminar versões não necessárias; backups conforme política | dono do sistema; registro sem dados pessoais |
| Cloudflare / hospedagem / analytics, se houver | criação do log/evento; prazo técnico final a definir pela configuração real | políticas de acesso, descarte, opt-out de cookies não essenciais | Infra; inventário cookies/logs e evidência de configuração |
| Backups de sistemas | criação do backup e ciclo aprovado, com impedimento de reimportação indevida | documentar limites reais de eliminação e garantir que restauração reaplique supressão | Infra; simulação de restore sintético |
| Protocolos de direitos/incidentes | abertura do pedido/conhecimento do incidente; exigências legais e prescrição a validar | minimizar/anônimizar quando possível sem destruir dever legal de registro | Direção + jurídico; prazo e justificativa |

**Fluxo mínimo:** localizar por identificador autorizado → registrar manifestação/oposição → cancelar campanhas agendadas e cessar marketing → solicitar exclusão nos sistemas identificados → documentar exceção legal minimizada → conferir cópias/backups/terceiros → responder titular com evidência segura. Ensaiar integralmente com identidade e mensagens fictícias antes da ativação.

## 9. Aplicação futura prioritária ao e-mail do material educativo (PR #21)

A decisão DEC-LGPD-20261010-001 altera **somente a prioridade do desenho**, mantendo a matriz de retenção do §8 e controles de incidentes do §7. Antes de ativar, definir para a operação **entrega de guia por e-mail**: responsável pela caixa e provedor, identificação mínima por solicitação, deduplicação sem importação indiscriminada ao CRM, prazo/evento de exclusão do endereço nas filas, mensagens enviadas, registros de entrega e backups, e prova de descarte onde tecnicamente possível.

Para **marketing**, registrar preferência em campo distinto, aviso/versão e momento de aceite (se consentimento for base aprovada), fornecer descadastro, cancelar campanhas agendadas e conservar somente supressão minimizada com fundamento e prazo próprios. Não manter toda a mensagem/contato para provar oposição. Tratar envios malsucedidos sem considerar tentativa como entrega confirmada. Nenhum dado real, lista, fornecedor ou teste pode ser operado a partir deste adendo.
