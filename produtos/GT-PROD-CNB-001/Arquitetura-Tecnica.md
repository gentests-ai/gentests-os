---
id: GT-PROD-CNB-001-TEC
produto: GT-PROD-CNB-001
tipo: especificacao-tecnica
versao: 0.1.1
status: proposta
estado_documental: em-validacao
data: 2026-10-10
responsavel: Produto
aprovador: Direcao
validacao_independente: pendente
implementacao: nao-autorizada
publicacao: bloqueada
---

# Arquitetura técnica, custos e mensuração

## 1. Arquitetura proposta e verificação de viabilidade

MVP núcleo em HTML semântico, CSS e JavaScript modular nativo, consistente com site consultado; não exige SPA, framework, IA, banco, API financeira ou licença nova. Módulo de cálculo puro sem rede/DOM recebe dados canônicos e retorna resultado e memória. Módulos de UI validam, apresentam e imprimem. Hospedagem candidata: mesmo projeto Cloudflare Pages, a confirmar no painel futuro. Nenhum arquivo de site ou configuração foi criado nesta tarefa.

Valores permanecem em memória de aba. Sem localStorage/sessionStorage/cookies de cálculo por padrão; recarregar perde a simulação, aviso visível. Não incluir valores em URL/fragmento, eventos, logs, crash reporting ou payload de contato. Ausência de coleta de inputs não significa ausência de logs técnicos da hospedagem; inventariar separadamente.

Designações candidatas para implementação futura: página calculadora, assets/cnb/calculo.js, ui.js e estilo com escopo cnb para evitar regressão global. Não implementar agora. Versões schema_version, methodology_version e product_version explícitas; alteração financeira é versão revisada com parecer independente.

## 2. Contrato de dados proposto

Objeto local: `schema_version`, `methodology_version`, `mode`, `incident_local_id`, até quatro `labor_blocks` (role, hours_hundredths, rate_cents, origin, status, unique_confirmed), três `effects` (nature, amount_cents, local_event_ref, origin, status) e `reconciliations` contextuais (nature_left, nature_right, relation, included_amounts_cents, compared_values_origins, confirmed), frequency_monthly inteira opcional, downtime_hundredths contextual opcional. Sem texto livre/pessoa/comprovante. IDs gerados localmente são rótulos de conciliação; não comprovam evidência. O antigo booleano genérico reconciliation_confirmed é substituído pelas comparações de RN-09a: igualdade/diferença de refs não confirma distinção. Confirmed só é elegível com comparandos identificados, origem conhecida/hipotética explícita, relação resolvida e valores atuais compatíveis; edição invalida a comparação afetada.

Resposta do motor: linhas com operands, amount_cents, origin; R/E/A/O e T ou subtotal; M/Y ou null; completeness (complete/partial/no_data), excluded com razão; has_hypotheses; warnings; inputs_snapshot. Valores decimais canônicos transportados como strings de inteiros para evitar serialização/overflow de BigInt. Null sempre explícito para desconhecido; não omitir como zero. Lista de propriedades permitidas, enums e limites da funcional; rejeitar extras no endpoint futuro.

## 3. Componente opcional de entrega

Somente após gates: Pages Function/Worker como backend same-origin, segredo em binding/cofre (nunca JS/GitHub) e fornecedor aprovado de e-mail transacional. Cliente envia e-mail, snapshot numérico minimizado e imutável, snapshot_hash, methodology_version, marketing_opt_in separado, notice_version e request_id aleatório via HTTPS POST. Dados pessoais e identificadores reais continuam proibidos no snapshot. Não transmite refs de documentos/pessoas nem URLs de destino arbitrárias.

Backend valida schema/limites/tipos/proveniência, recalcula por versão canônica e constrói HTML escapado + texto. Não confiar em totais/HTML/assunto remetidos pelo navegador. Limite candidato de corpo 32KiB; payload excessivo 413, inválido 422 com códigos de campo, limitado 429, provedor indisponível 503 e referência opaca; sem echo de e-mail/inputs nos erros. Retorno 202 significa “aceito para processamento”.

**Contrato de integridade (CNB-REV-02):** no cálculo válido, criar cópia profunda imutável do snapshot com versões de schema/produto/método/guia, entradas canônicas, origens/estados, comparações contextuais, linhas/resultados, exclusões e limites. Canonicalizar por schema: chaves de objeto ordenadas, arrays de blocos/naturezas/comparações em ordem estável definida, valores inteiros como strings decimais sem zeros à esquerda (zero = "0"), null explícito, enums fechados, JSON UTF-8 compacto. Gerar snapshot_hash SHA-256 desses bytes; excluir do conteúdo hash/request_id, e-mail, preferência de marketing e timestamps de transporte para não produzir dependência circular ou alterar o cálculo. O schema deve fixar a mesma ordem/representação no cliente e servidor.

Ao pedir impressão ou e-mail, gerar request_id e vincular de forma imutável o snapshot_hash, snapshot e methodology_version; não consultar novamente o estado editável para compor o relatório. No e-mail, backend valida a versão suportada, confirma equivalência entre versão do envelope/snapshot, recalcula pela mesma metodologia e confere conteúdo/hash canônicos antes de aceitar. Divergência ou versão não suportada rejeita o pedido, sem atualizar silenciosamente para método novo. Hash não é assinatura nem dispensa validação; os bytes do snapshot e o envelope de entrega também são comparados ao registro do pedido.

Idempotência por request_id e janela/retention a definir: mesmo ID + mesmo snapshot/hash/versão + mesmo envelope de entrega devolve o estado existente, sem outro envio; mesmo ID com qualquer alteração de conteúdo, destinatário, aviso ou escolha de entrega é conflito (409), não atualização. Não registrar endereço, valores, snapshot_hash ou conteúdo do envelope em analytics/logs gerais; o vínculo mínimo operacional tem acesso/retenção aprovados.

Edição, limpeza e novo cálculo não alteram pedido já em curso; novo cálculo válido e nova solicitação explícita geram outro request_id vinculado ao novo snapshot. Timeout do cliente depois do POST ou do backend depois de acionar o provedor mantém o pedido original como não confirmado: consultar/reconciliar com o registro/provedor pelo vínculo original antes de retry. Só retomar o mesmo pedido quando houver evidência de que o provedor não aceitou o envio e controle de idempotência; se aceitou, atualizar estado sem reenviar; se inconclusivo, bloquear retry de envio e mostrar “resultado de envio não confirmado”. Não criar automaticamente novo request_id para contornar timeout, nem prometer exactly-once.

Persistência mínima de idempotência/fila somente em infraestrutura autorizada; nenhum banco novo escolhido nesta proposta. Preferir recurso já existente se comprovar controles; sem capacidade confiável de preservar vínculo e reconciliar timeout, componente e-mail permanece desativado. Retenção/janela/provedor continuam decisões futuras; este ajuste de contrato não antecipa implementação.

Antiabuso: limite por origem técnica minimizada, global por quota e por destinatário de modo proporcional, honeypot auxiliar, validação server-side e backoff limitado. IP pode ser dado pessoal; política/base/retenção precisam incluir controles de segurança. Valores iniciais de rate limit a calibrar em teste sintético autorizado, não baseados em tráfego inexistente. Se Turnstile for escolhido, validar token no backend, acessibilidade e privacidade; só um widget não garante segurança. Proteção contra spam a terceiros, enumeração, CRLF/header injection, XSS e exfiltração. TLS, CSP ajustada ao stack, sem open relay; origem permitida explicitamente (CORS sozinho não autentica nem evita abuso), segredos rotacionáveis e privilégio mínimo. Kill switch de e-mail e limites globais sem migrar automaticamente para plano pago.

## 4. Opções e custos: hipóteses, não contratação

| Opção | Adequação e custo externo | Decisão |
|---|---|---|
| Núcleo estático Pages | Sem consumo de Functions para calcular; assets estáticos grátis sem limite de requests conforme fonte atual. Domínio existente a confirmar | Recomendado para MVP núcleo |
| Function/Worker + provedor transacional | Quotas Workers compartilhadas; custo de envio/domínio/retention pode existir | Viável condicionalmente; e-mail não homologado |
| FormSubmit existente | Código encaminha contato para caixa da empresa; não comprova gerar/entregar relatório ao usuário | Não reutilizar como motor de relatório sem capacidade demonstrada |
| Cloudflare Email Service | Docs atuais descrevem envio beta; gratuidade a destinos verificados da conta não prova entrega grátis a visitantes arbitrários | Avaliar elegibilidade, quotas, domínio/DNS e preço antes de escolher |
| E-mail manual | Custo financeiro possivelmente baixo, mas operação, autorização, exposição e tempo recorrentes | Não pressupor como automação gratuita; somente alternativa deliberada |
| PDF server-side / banco / IA | Complexidade e custo desnecessários para cálculo determinístico | Fora do MVP núcleo |

Fontes atuais consultadas: [Pages limites](https://developers.cloudflare.com/pages/platform/limits/), [Functions pricing](https://developers.cloudflare.com/pages/functions/pricing/), [Email Service](https://developers.cloudflare.com/email-service/), em 10/10/2026. Free Pages: 500 builds/mês, uma build simultânea, 20.000 arquivos e 25MiB por asset. Functions compartilham 100.000 requests/dia com Workers Free; não é quota exclusiva do produto. Preços/quota reais da conta, créditos GitHub privados e envio público **não verificados**. Revalidar antes de implementar. Limites de plataforma não são SLA de disponibilidade.

Estimativa de esforço **hipotética**, sem orçamento aprovado: núcleo/UI 16–24h; testes/QA/acessibilidade 8–16h; revisão e documentação 4–8h (núcleo 28–48h). E-mail/controles/ensaios adicionam 16–32h; total com e-mail 44–80h. Não são proposta comercial ou prazo prometido. Justificativa: motor pequeno, porém conciliação, estados incompletos, mobile, relatório e operação de e-mail exigem validação. Dependem de executor disponível e requisitos aprovados; registrar esforço real por etapa. Custo interno = horas efetivas × custo-hora interno validado; taxa não conhecida, portanto não calcular valor monetário. Infra estática pode ter custo adicional zero; tempo de desenvolvimento/manutenção não é gratuito.

## 5. Eventos e indicadores (somente desenho)

Telemetria desativada até inventário/base/avisos/fornecedor/retention e autorização. Cálculo não depende de consentimento de analytics. Rejeição de coleta não impede uso. Sem fingerprint, tracking de abertura, ID persistente entre serviços ou valores financeiros. Evento não pode transportar e-mail, inputs, frequência, downtime, refs locais ou URL completa.

Payload permitido: event_name, product_version, methodology_version, time_bucket, page_code, mode (own/example), result_state (complete/partial), categoria de erro predefinida e campanha de allowlist; identificador efêmero de sessão apenas se aprovado para deduplicação, sem ligação ao e-mail/CRM. Sessões medidas são somente coorte observável; não atribuir cobertura de todos os visitantes.

| Evento candidato | Gatilho / unicidade |
|---|---|
| calculator_view | primeira visualização mensurável na sessão |
| calculator_start | primeira edição humana, não exemplo programático |
| example_loaded | ação explícita, segregada de estimativas próprias |
| calculation_valid | primeiro cálculo válido por sessão/modo; recalcular não é nova conclusão de funil |
| validation_failed | tentativa inválida; categoria fixa, sem conteúdo digitado |
| report_print_requested | clique em impressão; não prova arquivo salvo |
| report_email_requested | pedido aceito pelo backend; request_id operacional deduplica, sem enviar e-mail para analytics |
| report_email_sent / delivered / failed | estados comprovados do provedor; sem delivered inventado |
| guide_cta_clicked / contact_cta_clicked | cliques, não download/leitura/contato efetivo |
| marketing_opt_in / withdrawn | operação de preferência comprovada; registro segregado, sem perfil financeiro |

Indicadores: ativação = sessões iniciadas / visualizações elegíveis; conclusão = sessões próprias com calculation_valid / próprias iniciadas; erro = sessões com erro / sessões que tentaram calcular; pedido de relatório = pedidos únicos / conclusões elegíveis na mesma coorte; entrega = pedidos entregues confirmados / pedidos aceitos; opt-in = preferências válidas / pedidos elegíveis, se marketing oferecido. Denominador zero = N/A; publicar janela, cobertura e exclusão de exemplo/bots/retries. Falta de webhook impede medir entrega, não substituí-la por envio.

Oportunidades qualificadas, reuniões realizadas, propostas autorizadas e contratos/entrada ficam no CRM canônico de PLN-COM-001. Atribuição só quando origem declarada/verificável; sem ligar sessão financeira a pessoa. Conversões comerciais usam a mesma coorte e janela com censura/lags declarados. Sem meta de receita ou taxa inventada. Métricas de busca futuras: impressões/cliques/CTR da página no Search Console se propriedade e acesso autorizados, sem garantia de ranking.

## 6. Requisitos não funcionais e operação futura

Metas propostas RNF-01: calcular até 4 blocos em ≤100ms p95 em aparelho de teste identificado; 20 rodadas aquecidas, sem rede no cálculo. RNF-02: JS específico ≤50KiB gzip, sem dependências remotas essenciais; payload inicial e regressões medidos. RNF-03: LCP≤2,5s, INP≤200ms, CLS≤0,1 como objetivos de experiência a confirmar por medição adequada; laboratório não comprova p75 de campo sem tráfego. RNF-04: acessibilidade/visual em Interface-Jornada. RNF-05: cálculo utilizável durante falha do e-mail; JS indisponível apresenta método e mensagem honesta, sem resultado falso.

RNF-06: duas últimas versões estáveis disponíveis na homologação de Safari iOS, Chrome Android/desktop, Firefox e Edge; registrar versões/dispositivos reais. RNF-07: teste de impressão com paginação e relatório HTML/texto; sem PDF/UA presumido. RNF-08: zero rede contendo inputs antes de pedido autorizado; inspeção de network/storage/logs e cópias. RNF-09: motor determinístico, contratos compartilhados e regressão do exemplo por versão. RNF-10: rollback futuro por versão previamente aprovada e feature flags de envio/analytics; mudança de método invalida snapshot antigo sem recalcular silenciosamente.

Dono técnico, monitoramento de quotas, entrega/abuso, acesso, suporte e resposta a direitos/incidentes precisam ser designados. Não há SLA externo definido; publicar indisponibilidade corretamente e desligar e-mail diante de risco sem impedir consulta ao método.

## Histórico focal

0.1.1: CNB-REV-01/02 — contrato de conciliação contextual e integridade/idempotência do relatório, sem infraestrutura, fornecedor ou funcionalidade adicional ativados. Revalidação focal pendente.
