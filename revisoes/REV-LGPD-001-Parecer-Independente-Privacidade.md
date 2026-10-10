---
id: REV-LGPD-001
tipo: parecer-revisao-independente
versao: 0.1.0
status: emitido
resultado: aprovado-com-ressalvas
data: 2026-10-10
revisor: Agente Revisor Independente
pr_execucao: 16
commit_revisado: 48993e09b04e554f0724640f5b0265d8dcd71883
publicacao_autorizada: nao
captacao_leads_autorizada: nao
homologacao_politica: nao
---
# REV-LGPD-001 — Parecer independente focal de privacidade e captação de leads

## 1. Resumo executivo

**APROVADO COM RESSALVAS — APTO PARA DELIBERAÇÃO DOCUMENTAL DA DIREÇÃO, NÃO APTO PARA PUBLICAÇÃO, CAPTAÇÃO OU DECLARAÇÃO DE CONFORMIDADE OPERACIONAL.**

Os quatro documentos formam uma base inicial coerente, proporcional e conservadora: delimitam os dados e provedores conhecidos, separam fatos de hipóteses, evitam inventar CNPJ/controlador/encarregado, distinguem material gratuito e marketing, exigem controles verificáveis e explicitam lacunas de fornecedores e transferência internacional. Os 12 testes LP-01 a LP-12 são candidatos úteis, **não executados**.

**Principal correção jurídica obrigatória antes da ativação:** completar a matriz finalidade→operação→base legal, a definição do controlador e as condições contratuais/transferências e retenção dos provedores efetivos. O fluxo de incidentes deve diferenciar a regra geral de comunicação de **3 dias úteis** do regime especial de pequeno porte e dos requisitos de comunicação, sem pressupor elegibilidade. Ainda não existe prova suficiente de conformidade de FormSubmit/Gmail/Cloudflare/Sheets.

**Ressalva de alcance:** o diagnóstico parte do código do site `main` descrito pelo Executor; **não houve verificação de deploy funcional ou configuração real** nesta revisão. Não tratar coleta já codificada como prova de que ocorre em produção, nem afirmar que não ocorre. A landing page do material da PR #4 não foi examinada como produto publicado.

Esta avaliação é documental e normativa, **não substitui parecer jurídico especializado**, auditoria técnica nem aprovação da Direção.

## 2. Evidências e escopo

- PR #16: https://github.com/gentestsai-sudo/gentests-os/pull/16; branch `docs/gt-lgpd-001-diagnostico-20261010`.
- Commit analisado `48993e09b04e554f0724640f5b0265d8dcd71883`, documentos lidos integralmente: `revisoes/GT-LGPD-001-Diagnostico-Privacidade.md`; `GT-LGPD-002-Politica-Privacidade-Proposta.md`; `GT-LGPD-003-Controles-Operacionais.md`; `GT-LGPD-004-Requisitos-Captacao-Leads.md`.
- Fontes normativas oficiais: [LGPD — Lei 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm); [ANPD Resolução 2/2022, texto atualizado](https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-2-de-27-de-janeiro-de-2022); [ANPD Resolução 15/2024 — incidente](https://www.gov.br/anpd/pt-br/assuntos/regulacao/analise-de-impacto-regulatorio/); [ANPD Resolução 19/2024 — transferência internacional](https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-19-de-23-de-agosto-de-2024); [ANPD orientações sobre cookies](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia_orientativo_cookies_e_protecao_de_dados_pessoais).
- Fora de escopo/não verificados independentemente: painel do Cloudflare, serviços e DPA FormSubmit, caixas Gmail, permissões CRM Sheets, rede/cookies do site em navegador, registros de operação, status de implantação, envio de e-mails, conteúdo completo do PR #4 e dados reais dos titulares. Essas lacunas impedem conclusão de conformidade **operacional**, não de consistência **documental**.

## 3. Matriz LGPD-R01 a LGPD-R06

| Dimensão | Situação | Severidade residual | Evidência | Ação |
|---|---|---|---|---|
| **LGPD-R01** Inventário e diagnóstico | **Apto com ressalvas** | Alta para ativação | GT-LGPD-001 §1–2 descreve formulário POST FormSubmit→Gmail, CRM Sheets, Cloudflare provável e analytics desconhecido; distingue código e produção | Fechar evidências de fornecedor, fluxo, armazenamento, papéis, países e configuração real antes de ativar |
| **LGPD-R02** Fundamentação jurídica | **Apto para proposição, incompleto para uso** | Alta para ativação | GT-LGPD-002 §3 e GT-LGPD-004 §2 tratam bases como candidatas; não confundem consentimento com pré-contrato | Aprovar matriz por operação/finalidade; corrigir prazos diferenciados e validar hipóteses específicas |
| **LGPD-R03** Política/transparência | **Rascunho consistente, não publicável** | Alta para publicação | GT-LGPD-002 §1, §4, §6, §8 têm campos a confirmar de controlador, contato, retenção, transferências/cookies | Identificação verdadeira, aviso final e canal; completar descrição fiel do fluxo real |
| **LGPD-R04** Controles | **Plano proporcional, não implementado** | Alta para operação | GT-LGPD-003 §1–6 especifica ROPA enxuto, supressão, direitos e incidente; sem evidência operacional | Distinguir prazos, validar retenção/eliminação e capacidade de fornecedores, ensaiar com dados sintéticos |
| **LGPD-R05** Leads | **Arquitetura recomendada adequada, não testada** | Média documental; alta se publicada antes de testes | GT-LGPD-004 §1–5 prioriza download direto, opt-in separado e LP-01 a LP-12 | Direção escolhe modalidade; revisar interesse/consentimento e medir viabilidade; executar critérios sintéticos antes de lançamento |
| **LGPD-R06** Governança/viabilidade | **Apto com ressalvas** | Média | POL-004 e SEC-AI-001 citadas como propostas, sem autorizações fictícias; uso enxuto de ferramentas existentes | Formalizar proprietários, autorização e decisão; não duplicar bancos, gates ou políticas |

## 4. Achados rastreáveis e correções do Executor

### LGPD-REV-01 — Alta para lançamento: controlador, fornecedores e ciclo não identificados

**Local:** GT-LGPD-001 §2–4; GT-LGPD-002 §1/4/8; GT-LGPD-003 §2/6.

A identidade jurídica do controlador, o canal efetivamente atendido, o papel de cada prestador por operação, retenção real, subprocessadores, países envolvidos e possíveis transferências não estão comprovados. A sinalização [A CONFIRMAR] é **correta para um rascunho**; não deve ser convertida em afirmação no site.

**Executor:** preparar checklist conciso de confirmação sem CNPJ inventado; vincular prova dos termos e da configuração de FormSubmit/Gmail/Cloudflare/Sheets, controlador↔operador quando aplicável, países e mecanismos art. 33. Nos termos da Res. 19/2024, se houver transferência internacional, não basta registrar “fornecedor global”: documentar também uma base legal art. 7/11 **e** mecanismo de transferência aplicável. Não é obrigatório que todo provedor seja operador em todos os fluxos; classificar pelo tratamento efetivo.

**Direção:** confirmar titular jurídico controlador e canal; decidir provedores, responsáveis e contratação pertinente após informação factual.

### LGPD-REV-02 — Alta para ativação: bases legais ainda não determinadas por fluxo

**Local:** GT-LGPD-001 §2, GT-LGPD-002 §3, GT-LGPD-004 §2.

Os documentos corretamente recusam consentimento genérico obrigatório. Porém “responder solicitação”, “entregar guia”, “prospecção B2B”, “segurança/logs” e “marketing” ainda têm base apenas candidata e exigem fundamentação contextual. **Procedimentos preliminares de contrato (art. 7º, V)** não servem automaticamente para todo pedido gratuito de guia ou contato informativo; **legítimo interesse (art. 7º, IX; art. 10)** exige finalidade legítima específica, expectativa razoável e teste de necessidade/balanceamento quando aplicável. Consentimento (arts. 7º I/8º) requer liberdade, granularidade e prova, com revogação descomplicada. Consentimento de resposta no site não autoriza envio promocional.

**Executor:** matriz com 1 linha por finalidade, dados necessários, controlador, base, avaliação de necessidade, expectativa/oposição, aviso, opt-out, destinatário e prova; deixar explícito quando a escolha exige jurídico. Evitar condicionar a resposta básica ou o guia a checkbox publicitária. Não escolher artificialmente consentimento para tudo.

### LGPD-REV-03 — Média jurídica: regime de pequeno porte e prazos

**Local:** GT-LGPD-001 §4; GT-LGPD-003 §3–4.

O texto reconhece a Res. 2/2022 e menciona prazo diferenciado, mas precisa de regra de operação mais explícita para não resultar em SLA equivocado. Art. 19 da LGPD: declaração clara e completa em **até 15 dias**, sujeita a hipóteses regulamentares; art. 15 da Res. 2/2022 permite ao agente de pequeno porte a declaração **simplificada em até 15 dias**. O art. 14 da Res. 2/2022 contempla **prazo em dobro** em hipóteses especificadas, inclusive declaração completa e notificação de incidente sob Res. 15/2024. A regra geral de comunicação de incidente notificável pela Res. 15/2024 é **3 dias úteis**, mas aplicação do dobro e exceções devem ser documentadas caso a elegibilidade seja comprovada, sem postergar contenção nem triagem. A regra de incidente aplica-se a situações com risco ou dano relevante, não a toda falha indiscriminadamente. Não inferir dispensa de encarregado nem de direitos pela simples alegação de ser pequena empresa.

**Executor:** tabela evento→marco inicial→regra geral→possível regime diferenciado→responsável→evidência, referenciada no texto oficial atualizado. Validar com jurídico enquadramento e exceções. Evitar SLA único para todos os direitos.

### LGPD-REV-04 — Média: transparência e segurança do formulário de contato preexistente

**Local:** GT-LGPD-001 §2–3; GT-LGPD-004 §4.

O formulário codificado usa POST para FormSubmit, texto livre, checkbox de resposta e `_captcha=false`. O diagnóstico **não prova** entrega, coleta real ou risco técnico explorável. Ainda assim há risco de conteúdo livre conter dados de terceiros, sensíveis ou segredos e de dupla finalidade por eventual reutilização de consentimento.

**Executor:** recomendar no PR técnico futuro eliminar a exigência injustificada de checkbox para simples resposta **caso** a base aprovada não seja consentimento; preservar aviso claro e separação de marketing; minimizar campo livre, prever triagem/descarte de dados inesperados, mitigação de spam proporcional, não expor dados em URL/erro, e testar sem dados pessoais reais. Não alterar site nesta atividade.

### LGPD-REV-05 — Média: retenção, preferência e exclusão dependem de capacidades reais

**Local:** GT-LGPD-002 §6; GT-LGPD-003 §1–3.

A ausência de prazos numéricos inventados é prudente. Contudo, para ativar, é preciso definir prazos ou critérios determináveis por finalidade e diferenciar e-mail enviado, base de leads, registros mínimos de opt-in, opt-out, logs e backup, com localização de todas as cópias. A supressão de contato **pode** justificar registro mínimo após revogação com finalidade própria, em vez de reter indefinidamente dados para marketing. Direitos não são irrestritos e retenção legal ou legítima deve ser documentada.

**Executor:** tabela simples por categoria e sistema: evento de início, prazo/critério, responsável, exclusão, eventual exceção e meio de comprovação; ensaiar acesso, revogação, exclusão e supressão com dados sintéticos.

### LGPD-REV-06 — Média: captação de leads e avaliação das duas alternativas

**Local:** GT-LGPD-004 §1–5.

**Download direto** é mais simples, barato e evita pedir identificação, mas não gera base de leads por si só; logs de hospedagem permanecem objeto separado. **Entrega por e-mail** permite contatos identificáveis, porém adiciona provedor, custo operacional, erro de entrega, retenção, prova de preferências e exposição. Se adotada, pedir só e-mail para entrega; consentimento promocional separado, voluntário e desmarcado. Não há base para afirmar conversão superior sem experimento. A alternativa direta pode incluir CTA voluntário de assinatura sem condicionar download.

**LP-01 a LP-12:** todos os doze cenários têm resultado verificável em princípio, cobrindo separação de finalidades, opt-in/out, erro, abuso, dado inesperado, fornecedor, titular, acesso, transferência, cookies e evidência. **Ressalvas pontuais para futuro aceite:** LP-03 verificar também tratamento de campanhas já programadas e lista de supressão; LP-05 explicitar como comprovar limite antiabuso sem CAPTCHA obrigatório; LP-09 usar credenciais/fixture de teste não privilegiadas; LP-10 não transformar mera existência de contrato em prova de mecanismo internacional válido; LP-12 exige evidência de execução, não checkbox preenchido. Dados pessoais reais são proibidos nesta fase.

### LGPD-REV-07 — Baixa documental: referência de Resolução 15/2024 pouco direta

**Local:** GT-LGPD-001 §5.

O link registrado como fonte para a Resolução 15/2024 aponta a uma página geral de análise de impacto regulatório, não ao texto regulamentar identificado. **Executor:** substituir ou complementar por ligação oficial direta ao ato atualizado; confirmar regramento de comunicação e atualização normativa antes do uso. Não é razão para reprovar a arquitetura inteira.

## 5. Direitos, contratos, transferências e responsabilidade

A arquitetura proposta satisfaz o princípio de minimizar dados e respeitar finalidades distintas, mas **não demonstra execução**. Verificação posterior necessária por fornecedor inclui termos de tratamento, subprocessadores, localização e condições de acesso/retention/remoção; avaliação de mecanismos art. 33 quando aplicável; resposta a titulares e notificações; além de registro de autorização. A Res. ANPD 19/2024 exige mecanismo próprio para transferência internacional além da hipótese legal de tratamento, quando houver transferência. A qualificação de controladores/operadores exige decisão sobre finalidades e meios por operação, não dedução pelo nome “Cloudflare” ou “Google”.

O regime ANPD de pequeno porte pode permitir simplificações, mas **não é presunção**, não elimina segurança e depende de critérios e exceções. Não presumir CNPJ, DPO, estrutura societária ou contrato existente.

## 6. Riscos residuais e decisões da Direção

**Pendências altas antes de publicação/coleta:** identidade e contato do controlador; finalidades/bases aprovadas; versão publicável do aviso; mapeamento e condições dos fornecedores reais; retenção/exclusão/preferências testáveis; canal e resposta a incidentes; evidência dos LP pertinentes à arquitetura escolhida. Uma landing page não deve ser lançada por simples aprovação deste parecer.

**DEC-LGPD-01:** controlador legal verdadeiro, contato, dono de incidentes e direitos; verificar condições para pequeno porte e eventual encarregado.

**DEC-LGPD-02:** arquitetura do material GT-MKT-CNQ-001 — download direto (preferência técnica por minimização) ou entrega por e-mail; finalidade e desenho do opt-in.

**DEC-LGPD-03:** fundamentos jurídicos e transparência por fluxo, revisão especializada onde houver ambiguidade; não sacrificar requisitos de liberdade por metas de conversão.

**DEC-LGPD-04:** uso e alternativas aos fornecedores, termos, transferências, limitações técnicas, retenção, descarte e acesso; orçamento proporcional.

**DEC-LGPD-05:** dono por operação e cronograma realista, autorizações futuras de PR do site, testes sintéticos e publicação; integração com POL-004 e SEC-AI-001 somente após aprovação normativa pertinente.

**Separação de agentes:** Executor prepara artefatos e propostas de correção; Revisor avalia independentemente sem alterar originais; Orquestrador consolida parecer e pendências; Direção delibera e autoriza. Não se deve enviar banco de leads/contatos a modelos de IA para prova de conceito.

## 7. Condições para fechamento da revisão e encaminhamento

**Apto agora a deliberação documental:** sim, **com ressalvas**, pois as lacunas de implementação e identidade são declaradas, e a arquitetura preferencial não exige coletar dados. Não é necessário elaborar documento redundante nem contratar sistema pago para preparar a decisão. Encaminhar ao Orquestrador juntamente com esta lista de pendências e impedir qualquer interpretação de “aprovado” como “landing page pronta”.

**Correções recomendadas antes da autorização de publicação:** preencher fatos institucionais, matriz finalidade/base, regra pequena empresa/prazos de incidente, prova de fornecedor/transferência, desenho final do aviso e retenção, e testar fluxos LP-01–LP-12 aplicáveis com dados sintéticos e evidência. Parecer jurídico quando houver dúvida sobre legitimidade do interesse, qualificação, internacionalização, incidente ou regime de pequeno porte.

**Gates:** próxima etapa do Executor é preparar tratamento focal de LGPD-REV-01–07 em branch separada, sem editar os originais nesta revisão; Direção decide os fatos institucionais e arquitetura; revisor confere apenas deltas materiais antes do go-live. Não reabrir esta revisão documental integralmente sem nova regressão.

**Conclusão: APROVADO COM RESSALVAS — encaminhar à Direção para decisões, sem publicação, captação ou homologação.** Não autoriza coleta, fornecedor, contrato, testes reais, merge ou publicação. 
