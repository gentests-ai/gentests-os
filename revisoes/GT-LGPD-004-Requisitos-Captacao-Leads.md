---
id: GT-LGPD-004
tipo: requisitos-captacao-leads
versao: 0.1.0
status: proposta-nao-implementada
data: 2026-10-10
---
# GT-LGPD-004 — Requisitos de captação para GT-MKT-CNQ-001

> Especificação futura, sem landing page criada, sem coleta real e sem autorização de publicação. Material educacional em revisão na PR #4 do `gentests-os`. Público B2B não exclui aplicação da LGPD a e-mails pessoais ou profissionais identificáveis.

## 1. Modelo mínimo recomendado
**Alternativa preferencial de menor risco:** disponibilizar download gratuito por link direto **sem solicitar dados**, usando convite voluntário e separado para assinar notícias, se houver finalidade comercial real. Se a Direção demonstrar necessidade legítima do formulário, limitar a **e-mail obrigatório apenas para entregar link por e-mail**, nome opcional e não coletar telefone, cargo, CPF, empresa, senha, anexo, histórico de navegação para enriquecimento ou texto livre. Formulário não deve esconder conteúdo atrás de consentimento de marketing.

### Microcopy candidata (publicação condicionada)
**Título:** Baixe gratuitamente o guia “Custo da Não Qualidade de Software”.

**Finalidade de entrega:** “Usaremos o e-mail informado apenas para enviar o link do material solicitado. Consulte o Aviso de Privacidade para conhecer o tratamento dos dados.”

**Opt-in opcional, desmarcado, independente:** “Quero receber por e-mail conteúdos e novidades da GenTests.ai sobre qualidade de software. Posso cancelar a qualquer momento.”

**Links necessários:** Política/Aviso de Privacidade e canal de privacidade identificando controlador legal após confirmação. Não usar `consentimento` obrigatório genérico para marketing, nem condicionar download a aprovação promocional.

## 2. Matriz de finalidade, base e prova
| Operação | Dados mínimos | Base legal candidata e condição | Prova/controle |
|---|---|---|---|
| Download direto | nenhum campo identificado exigido | sem captação de lead; logs técnicos de hospedagem separados e sujeitos à avaliação | material acessível sem checkbox |
| Entrega por e-mail, se adotada | e-mail | definir base apropriada ao pedido do titular antes de executar; não presumir marketing consentido | formulário e evento de entrega com registro mínimo |
| Conteúdo promocional opcional | e-mail e escolha | consentimento específico (art. 7 I e art. 8) como opção preferida de desenho; nunca pré-marcado | versão do texto, data/hora, origem, estado, retirada, identificador mínimo |
| Contato solicitado | nome, e-mail e mensagem estritamente necessária | base avaliada conforme contexto do pedido, sem duplicar marketing | resposta limitada à solicitação |
| Analytics/cookies não essenciais | identificador/evento somente se necessário | avaliação específica da base, transparência e escolha conforme guia ANPD; desativados até validação se não imprescindíveis | inventário e ensaios de rejeição/aceite, sem dark patterns |

Se a empresa escolher base de legítimo interesse para comunicações específicas, exigir teste documentado de balanceamento, necessidade e expectativas do titular, sem presumir que todo contato B2B autoriza campanha. **Não utilizar autorização de entrega de guia para promover assinaturas automaticamente.**

## 3. Critérios de aceite verificáveis antes de ativar
| ID | Cenário sintético | Resultado obrigatório |
|---|---|---|
| LP-01 | visitante solicita download sem aderir a marketing | conteúdo acessível/entregue; nenhum registro de opt-in comercial |
| LP-02 | visitante opta pelo marketing | escolha opcional desmarcada por padrão, prova da versão e momento do aceite, sem campos excessivos |
| LP-03 | visitante desmarca/retira consentimento | marketing cessa e lista de supressão evita novo contato; eventual retenção de prova mínima fundamentada |
| LP-04 | endereço inválido/dado ausente | mensagem acessível e sem vazamento de erro/identificadores |
| LP-05 | formulário duplicado/robô | rate limit ou mitigação proporcional, sem depender só de campo oculto ou CAPTCHA ineficaz |
| LP-06 | usuário informa dado sensível indevido | não solicitar, minimizar e acionar tratamento seguro de exclusão |
| LP-07 | fornecedor indisponível | falha segura; não prometer entrega, nem expor dados em URL/erro |
| LP-08 | solicitação de acesso/exclusão | canal e procedimento GT-LGPD-003 operacionais, com resposta rastreável |
| LP-09 | acessos internos | só identidades autorizadas podem ver leads; teste negativo de privilégio |
| LP-10 | terceiros/geografia | fornecedores, operadores, contratos e transferência internacional eventualmente necessária documentados |
| LP-11 | cookies e telemetria | identificar categorias reais; nenhuma tecnologia não essencial sem base/controle pertinente |
| LP-12 | relatório | execução real com data, ambiente, commit, resultado e evidência sanitizada; não aprovar por checklist não testado |

## 4. Integração com site existente
O arquivo `contato.html` na `gentests-site/main` mostra `POST` para FormSubmit, `_captcha=false`, honeypot `_honey`, campos nome/e-mail/desafio/mensagem e checkbox obrigatória apenas para retorno. **Não reutilizar esse checkbox para marketing; não copiar automaticamente toda mensagem ao CRM.** Antes de nova landing page, reavaliar FormSubmit (contrato, acesso, retenção, geografia, entrega, spam) e Gmail; comparar com download direto sem fornecedor adicional. Atualização de site ocorrerá apenas em PR técnico próprio após parecer e aprovação da Direção.

## 5. Dependências e decisões
DEC-LP-01: download sem coleta ou captura de e-mail justificada? **Pendente.**
DEC-LP-02: controlador, aviso final, base legal por operação, canal e encarregado/dispensa? **Pendente.**
DEC-LP-03: fornecedores, retenção, transferências e eventual opt-in? **Pendente.**
DEC-LP-04: CRM, mecanismo de exclusão/descadastro e dono de preferências? **Pendente.**
DEC-LP-05: liberação documental, orçamento e PR futura de site? **Pendente.**

**Bloqueio final:** sem publicação, coleta, envio de campanha ou ativação por esta atividade. A PR #4 sobre conteúdo educativo e aprovação de marketing são processos distintos; conformidade com LGPD requer validação jurídica e operacional proporcional ao risco.
