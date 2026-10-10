---
id: GT-LGPD-001
tipo: diagnostico-privacidade
versao: 0.1.0
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
- ANPD Res. 15/2024, comunicação de incidentes: <https://www.gov.br/anpd/pt-br/assuntos/regulacao/analise-de-impacto-regulatorio/>.
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
