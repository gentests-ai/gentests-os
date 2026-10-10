---
id: GT-LGPD-001
tipo: diagnostico-privacidade
versao: 0.2.0
status: proposta-para-revisao-independente
data: 2026-10-10
aprovador: Direcao
publicacao_autorizada: nao
---
# GT-LGPD-001 — Diagnóstico inicial de privacidade

> Análise documental limitada; **não é certificação de conformidade LGPD, parecer jurídico, inventário exaustivo nem autorização para coleta ou publicação**.

## 1. Método, fonte e limites
Inspeção de `gentestsai-sudo/gentests-site/main` (`index.html`, `contato.html`, `quem-somos.html`, `solucoes.html`) e de `gentests-os/main` (POL-004 v1.0.0 proposta, SEC-AI-001 v0.1.0 proposta, processo de prospecção e processo comercial). Referências adicionais: GT-MKT-CNQ-001 na [PR #4](https://github.com/gentestsai-sudo/gentests-os/pull/4), parecer do site [PR #5](https://github.com/gentestsai-sudo/gentests-os/pull/5) e governança [PRs #6/#7/#10/#12]. **O site publicado não pôde ser inspecionado funcionalmente pela ferramenta de navegação**; código da main não comprova deploy nem comportamento real. Não foram consultados painel Cloudflare, FormSubmit, Gmail, CRM, scripts de analytics, cookies em navegador, contratos/DPA, faturas, log de acesso ou destinatários reais. Cada inferência está marcada. A PR #4 foi identificada, mas o documento não estava em `main`; seu conteúdo vigente e eventual formulário de distribuição deverão ser revistos no respectivo PR.

## 2. Inventário inicial de operações e ferramentas
| Fluxo | Dados / origem | Ferramenta / destino identificado | Finalidade e hipótese jurídica pendente | Estado |
|---|---|---|---|---|
| Contato já codificado em `contato.html` | `nome`, `email`, `desafio` (categoria), `mensagem` livre e checkbox `consentimento`; potencial dado sensível inserido espontaneamente | ação HTML POST `https://formsubmit.co/gentests.ai@gmail.com`; destinatário e-mail Google; `_captcha=false` e campo `_honey`; redirecionamento `obrigado.html` | responder pedido do visitante; base legal a validar (procedimentos preliminares de contrato, legítimo interesse conforme avaliação, ou consentimento válido conforme desenho) | **Código verificado; entrega, ativação, segurança, retenção e coleta real NÃO verificadas** |
| Futuro download GT-MKT-CNQ-001 | proposta: e-mail mínimo; nome opcional; não exigir telefone, CPF, cargo, empresa ou campo livre | landing page, armazenamento e entrega **não implementados/confirmados** | envio do material solicitado separado de marketing; base conforme arquitetura aprovada | **projeto apenas** |
| Prospecção/CRM | contato profissional, empresa, canal, histórico, etapa, fonte, possivelmente telefone | Google Sheets referenciado em `03-Processos/Prospeccao-Comercial.md`, link ID `151zLp3akkkbdeA6D44EOAsefT9gjygvv0ZMsGRZ3WV0` | contatos B2B e acompanhamento; legítimo interesse é candidato sujeito a teste de balanceamento e transparência, não licença para disparos | **referência documental; conteúdo, compartilhamento e integridade não verificados** |
| Site e hospedagem | IP, user-agent, logs, cookies e telemetria **possíveis**, não confirmados | domínio `pages.dev` sugere Cloudflare Pages; contrato, região, logs e serviços efetivos a conferir | segurança, disponibilidade, análise de tráfego conforme configuração e base legal | **provedor sugerido pela URL, detalhes técnicos não verificados** |
| Analytics/cookies | identificadores, eventos e cookies eventuais | nenhum serviço específico comprovado nos HTML inspecionados | funcionalidade versus mensuração/marketing exige classificação e base legal por finalidade | **não verificado; não afirmar ausência** |
| Armazenamento e tratamento interno | mensagens, e-mails, leads e evidências | Gmail, CRM Sheets, possivelmente Drive; acessos e período desconhecidos | resposta comercial e retenção limitada por propósito | **fluxo e acessos não auditados** |

A página de contato apresenta checkbox obrigatória “Concordo com o uso dos dados informados para responder a esta solicitação”. **Isso não equivale a opt-in de campanhas**, e necessidade da checkbox para mera resposta deve ser reavaliada juridicamente. A página menciona FormSubmit e não inserir senhas/dados sensíveis, mas não comprova aviso completo de controlador, direitos, retenção, compartilhamentos e transferências internacionais. O código traz `_captcha=false`: avaliar abuso/spam e segurança em PR de site própria, sem alterar aqui. Dados inseridos em campo livre precisam de advertência e controle de minimização.

## 3. Principais achados e riscos
| ID/prioridade | Achado e risco | Evidência e tratamento necessário |
|---|---|---|
| LGPD-01 **P0** | Identidade jurídica do controlador, contato para titulares e condição de pequeno porte não confirmadas | Direção informar razão social ou pessoa natural responsável, CNPJ se existir, endereço/canal adequado; não inventar encarregado |
| LGPD-02 **P0** | Aviso completo e finalidades/bases não publicados ou verificados | site `contato.html` contém disclosure curto e checkbox; submeter GT-LGPD-002/004 à revisão jurídica e implementação controlada |
| LGPD-03 **P0** | Fluxo FormSubmit→Gmail com contrato, geografia, segurança, acesso e retenção desconhecidos | revisar termos, DPA, subprocessadores, exportações, configurações e apagamento; recepção funcional não testada |
| LGPD-04 **P0** | Projeto de lead magnet pode condicionar material ao marketing | exigir acesso gratuito independente de checkbox de marketing e comprovação de cada finalidade |
| LGPD-05 **P0** | Direitos dos titulares, retenção, descarte e incidentes sem procedimento operacional comprovado | proposta GT-LGPD-003; nomear dono e canal, ensaios sintéticos |
| LGPD-06 **P1** | CRM e e-mail podem duplicar contatos, manter consentimentos/desinscrições inconsistentes | definir ID canônico, fonte de preferências, acesso individual, registro mínimo e descarte em todos os destinos |
| LGPD-07 **P1** | Possível transferência internacional em Cloudflare/FormSubmit/Google | identificar exportadores/importadores, países, finalidades e mecanismos dos arts. 33–36; Res. ANPD 19/2024; não presumir conformidade por marcas |
| LGPD-08 **P1** | Cookies, analytics, logs e conectores desconhecidos | vistoria browser/network, painel de fornecedores, inventário de cookies; requisitos da ANPD por categoria |
| LGPD-09 **P1** | POL-004/SEC-AI-001 permanecem `proposta` | alinhar GT-GOV-003 sem declarar política em vigor nem criar governança paralela |
| LGPD-10 **P2** | Material em desenvolvimento/PR #4, sem processo de entrega validado | não publicar landing page nem coletar lead antes dos gates |

## 4. Responsabilidades e pequeno porte
A LGPD atribui papéis conforme quem decide finalidades e meios (`controlador`) e quem trata por sua conta e ordem (`operador`); qualificação por operação, não apenas pelo nome do fornecedor. A Direção deve confirmar quem atua juridicamente como controlador e quem é operador em cada fluxo. **Não assumir CNPJ ou DPO existentes.** A Resolução CD/ANPD 2/2022 prevê tratamento diferenciado para agentes de pequeno porte, inclusive dispensa de indicar encarregado quando seus requisitos são preenchidos, **mas mantém canal para titulares**; a elegibilidade e eventual exclusão por tratamento de alto risco exigem análise documentada. A dispensa não elimina obrigações de segurança, direitos, base legal ou incidentes. <https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-2-de-27-de-janeiro-de-2022>

## 5. Referências legais rastreáveis
- LGPD, Lei 13.709/2018: arts. 6 (princípios), 7/8/10 (bases, consentimento e legítimo interesse), 9 (transparência), 18 (direitos), 37 (registro de operações), 41 (encarregado), 46–49 (segurança), 48 (incidentes), 33–36 (transferência internacional). Texto oficial: <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>.
- ANPD Res. 2/2022, pequenos agentes: <https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-2-de-27-de-janeiro-de-2022>.
- ANPD Res. 15/2024, comunicação de incidentes: <https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/documentos/rcis___anonimizado_final_ocultado_2_parte3.pdf>.
- ANPD Res. 19/2024, transferência internacional: <https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-19-de-23-de-agosto-de-2024>.
- ANPD Guia Cookies: <https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia_orientativo_cookies_e_protecao_de_dados_pessoais>.
- ANPD guias para pequenos agentes e legítimo interesse: <https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes>.

## 6. Decisões exclusivas da Direção
| Decisão | Alternativas/encaminhamento recomendado | Situação |
|---|---|---|
| DEC-LGPD-01 | identificar controlador legal e canal para titulares; decidir responsável interno | **pendente** |
| DEC-LGPD-02 | confirmar elegibilidade pequeno porte e necessidade de encarregado / consultoria jurídica | **pendente** |
| DEC-LGPD-03 | aprovar por finalidade bases legais, transparência, uso do FormSubmit e geografia dos dados após verificação | **pendente** |
| DEC-LGPD-04 | escolher distribuição direta ou formulário mínimo; marketing sempre separado | **pendente** |
| DEC-LGPD-05 | aprovar retenção, descarte, direitos, incidentes, acessos e orçamento zero adicional desejado | **pendente** |
| DEC-LGPD-06 | autorizar PR de implementação no site **somente** após parecer independente e deliberação | **pendente** |

**Saída:** diagnóstico preliminar apto a revisão documental independente, não apto a declaração de conformidade operacional ou lançamento de landing page.


## 7. Tratamento focal REV-LGPD-001 — matriz única LGPD-REV-01 a 07 (v0.2.0)

Origem: [parecer independente PR #18](https://github.com/gentestsai-sudo/gentests-os/pull/18), emitido sobre commit `48993e09b04e554f0724640f5b0265d8dcd71883`. **Tratamento documental não é fechamento autoatribuído do achado.** Revisor deverá classificar o delta; Diretor(a) decidirá fatos institucionais e uso operacional.

| ID | Gravidade | Tratamento documental e evidência no pacote | Situação/resíduo |
|---|---|---|---|
| LGPD-REV-01 | Alta para lançamento | Checklist §8 de controlador, canal, fornecedor, subprocessadores, país e mecanismo de transferência | **Tratado na especificação; comprovação real pendente Direção/provedores** |
| LGPD-REV-02 | Alta para ativação | Matriz por finalidade e base jurídica candidata §9 e política GT-LGPD-002 §9 | **Tratado documentalmente; base definitiva condicionada à validação jurídica e Direção** |
| LGPD-REV-03 | Média jurídica | GT-LGPD-003 §7, tabela com regras gerais, prazo diferenciado e marco inicial | **Tratado documentalmente; enquadramento pequeno porte pendente** |
| LGPD-REV-04 | Média | GT-LGPD-004 §6, alterações do formulário atual em PR de site futura | **Requisito especificado; site intocado** |
| LGPD-REV-05 | Média | GT-LGPD-003 §8, matriz por cópias/sistemas com supressão e retenção | **Tratado documentalmente; prazos/tecnologia reais pendentes** |
| LGPD-REV-06 | Média | GT-LGPD-004 §7 comparação comercial x privacidade e aplicabilidade LP-01–12 | **Alternativas preservadas; escolha da Direção** |
| LGPD-REV-07 | Baixa | Substituída referência indireta à Res. 15/2024 por ato oficial identificado e página operacional ANPD | **Referência corrigida; conferir vigência antes de operação** |

### 8. Checklist de identificação e fornecedores — LGPD-REV-01
Preencher somente com documento/evidência; `PENDENTE` não equivale a ausência de controle.

| Item a confirmar | Responsável proposto | Prova requerida | Estado |
|---|---|---|---|
| Nome e natureza jurídica do controlador por operação; CNPJ **se existir** | Direção | documentação verificada, identificação para aviso público, responsável pelas decisões | PENDENTE |
| Canal de privacidade e responsável por respostas/incidentes; necessidade/dispensa de encarregado | Direção + jurídico | caixa realmente monitorada e orientação válida para pequeno porte | PENDENTE |
| FormSubmit, conta Gmail, Cloudflare Pages, Sheets/Drive e qualquer analytics | responsável técnico + Direção | nome legal do prestador, termos atuais, DPA/condições aplicáveis, acesso, retention e subprocessadores | PENDENTE |
| Papel jurídico de cada fornecedor por operação (controlador independente, operador etc.) | jurídico + Direção | finalidades e decisões de meios, contrato, compartilhamentos | PENDENTE |
| Países/origens/destinatários e existência efetiva de transferências internacionais | técnico + jurídico | locais de tratamento, acessos internacionais, subprocessadores e rotas por fluxo | PENDENTE |
| Transferência, se efetiva | jurídico + Direção | hipótese válida de tratamento da LGPD art. 7/11 **mais** mecanismo próprio do art. 33, Res. 19/2024; cláusulas e evidência, quando pertinentes | PENDENTE |
| Retenção/exclusão técnica e backup em cada provedor | Infra + operação | telas/configurações sanitizadas e ensaio sintético | PENDENTE |

**Bloqueio:** nenhuma afirmação de adequação internacional por nome de fornecedor; sem controlador, base e canal definidos, política externa e nova captura continuam não autorizadas.

### 9. Matriz de finalidade, operações e bases legais candidatas — LGPD-REV-02

| Operação/finalidade | Dados necessários e minimização | Hipótese jurídica candidata (**não aprovada**) | Necessidade, expectativas/oposição, terceiros/aviso e prova |
|---|---|---|---|
| Resposta ao contato espontâneo | e-mail e descrição mínima; nome apenas se necessário | art. 7 V **se** etapa preliminar solicitada relacionada a possível contrato; alternativamente art. 7 IX sujeito a teste; consentimento só se livre e adequado | preservar escopo do pedido; informação de FormSubmit/Gmail, canal e descarte; avaliar se checkbox atual é indevida |
| Download direto do guia | sem dado inserido pelo visitante; logs de acesso tratados à parte | sem base para cadastro inexistente; logs conforme linha abaixo | entregar mesmo sem marketing; aviso sobre tecnologia efetivamente usada |
| Entrega do guia por e-mail solicitado | e-mail; não exigir nome/telefone/empresa | art. 7 IX somente após teste de balanceamento da operação, ou outra hipótese juridicamente justificada; **não presumir art. 7 V por gratuidade** | finalidade limitada à entrega; alternativa direta; registro mínimo de entrega e descarte |
| Conteúdo comercial opcional | e-mail e preferência | consentimento art. 7 I/8 como desenho preferido; outros fundamentos só com análise específica | opt-in separado, desmarcado, sem prejuízo do guia; versão/texto/data/origem, revogação e descadastro |
| Prospecção B2B individual | contato profissional mínimo, empresa, fonte e etapa | art. 7 IX sujeito a teste de legítimo interesse por contexto | expectativa razoável, necessidade, transparência, oposição, opt-out, fonte/CRM e limites de abordagem |
| Logs de segurança / abuso | IP ou identificador estritamente necessário se comprovada coleta | art. 7 IX avaliado ou outra hipótese pertinente; não inventar obrigação legal genérica | prazo curto proporcional, acesso mínimo, fornecedores, cookies e descarte; bloquear uso secundário de anúncios |
| Direitos de titulares/incidentes | identificador mínimo e protocolo | obrigação legal/regulatória quando efetivamente aplicável (art. 7 II), ou fundamento válido específico | verificar identidade proporcional e período legal de evidências; restringir conteúdo |

A decisão final exige: controlador por operação, teste de necessidade, avaliação de legítimo interesse quando invocado, propósito, destinatários/transferências, cláusula do aviso, prazo e evidências. Validar com jurídico antes de ativar; dados sensíveis inesperados requerem análise do art. 11 quando cabível, não aproveitamento para marketing.

### 10. Bloqueios reais para publicação
Direção deve confirmar identidade/canal, bases por fluxo, modalidade do guia, fornecedores/transferências, retenção e atribuição operacional. Site requer PR própria, aviso publicável e testes sintéticos aplicáveis. Revisor independente deve apenas revalidar LGPD-REV-01–07 e novas regressões materiais, sem auditoria geral.
