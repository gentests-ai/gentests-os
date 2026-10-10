---
id: GT-LGPD-003
tipo: procedimento-operacional-privacidade
versao: 0.1.0
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
