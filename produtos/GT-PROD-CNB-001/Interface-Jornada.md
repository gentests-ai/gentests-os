---
id: GT-PROD-CNB-001-UX
produto: GT-PROD-CNB-001
tipo: interface-jornada
versao: 0.1.0
status: proposta
estado_documental: em-validacao
data: 2026-10-10
responsavel: Produto
aprovador: Direcao
validacao_independente: pendente
implementacao: nao-autorizada
publicacao: bloqueada
---

# Interface, jornada, SEO e privacidade

## 1. Jornada e composição propostas

| Etapa/estado | Conteúdo e comportamento |
|---|---|
| Descoberta | Página HTML com H1 “Calculadora de custo da não qualidade de software”, propósito e limites; links contextuais do guia/site após aprovação |
| Inicial vazio | Texto “Estime o impacto econômico de um incidente. Seus valores não são perdas verificadas”; botão secundário “Usar exemplo fictício” |
| 1. Esforço | Horas únicas e custo-hora por dev/QA/suporte; operação opcional; estados desconhecido/N/A e conciliação junto dos campos |
| 2. Efeitos distintos | Externo, ajuste de receita e margem não recuperável; ajuda com exclusões; referência local de evento; sem anexos/pessoas |
| 3. Recorrência | Frequência opcional e hipótese constante; indisponibilidade só contextual |
| Revisar/calcular | Sumário de erro com foco no primeiro erro e mensagens por campo; não depender só de cor |
| Resultado | Naturezas segregadas, total/subtotal e origem; projeções condicionais; memória e exclusões ao alcance da leitura |
| Próxima ação | “Conhecer a metodologia no guia” e “Conversar sobre como medir esses custos”; contato voluntário, sem preço/oferta nova |
| Relatório | Imprimir localmente; opção “Receber este relatório por e-mail” se componente aprovado/operacional |
| Editar/limpar | Preserve valores ao navegar; resultado desatualizado após edição; confirmar substituição por exemplo ou limpeza |
| Falha de rede/envio | Cálculo continua utilizável; envio com status verdadeiro, preserva snapshot sem repetir automaticamente |

Microcopy de resultado completo: “Impacto econômico gerencial estimado por incidente: R$ X. Valores informados por você; sem auditoria ou comprovação de perdas.”
Incompleto: “Subtotal estimado: R$ X. Existem parcelas não mensuradas ou excluídas. As projeções abrangem apenas as parcelas incluídas.”
Exemplo: banner persistente “Simulação fictícia do guia — não representa uma empresa real”.
Projeção: “Se este custo por incidente e a frequência permanecerem constantes, a projeção será R$ X/mês e R$ Y em 12 meses.”

## 2. Direção visual e acessibilidade

Reusar ativos oficiais e linguagem visual observada: azul escuro, destaque turquesa e tipografia existente; não recriar logo. Cada combinação exige medição de contraste, não aprovação presumida pelas cores atuais. Formulário com superfície clara ou contraste validado e números legíveis; fonte de corpo proposta ≥16px; números sem animação/counter alarmista; sem visualização que esconda tabela/memória.

Desktop ≥1024px: formulário e painel de resumo em duas colunas com largura fluida, sem altura fixa; resultado completo abaixo. Tablet/mobile: uma coluna e resumo após campos. Não fixar painel que cubra foco/conteúdo. Cabeçalhos e textos longos quebram naturalmente. Não usar cards com overflow oculto para conteúdo relevante.

Meta: WCAG 2.2 AA, incluindo teclado, sem armadilha, foco visível e não oculto, labels reais/unidades/instruções, fieldsets/legends, erros associados por aria-describedby, mensagens de status por live region moderada, idioma pt-BR e skip link. Contraste mínimo 4,5:1 corpo, 3:1 texto grande/controles quando aplicável. Alvos de interação propostos 44×44 CSS px (além do mínimo AA com exceções). Testar reflow 320 CSS px, zoom 200% e 400%, espaçamento de texto, retrato/paisagem e redução de movimento. Sem dependência de áudio, cor ou CAPTCHA visual.

Resultados devem ser tabela/lista semântica, legíveis em VoiceOver e NVDA. Botão Calcular não anuncia cada digitação. Teste automático ajuda, não certifica AA. Impressão não pode cortar linhas, valores ou disclaimers; HTML do relatório é alternativa acessível canônica, sem prometer PDF/UA por “Salvar como PDF”.

## 3. Relatório opcional por e-mail

**EMAIL-01:** cálculo/resultado na tela sem cadastro. E-mail é obrigatório somente para quem pede envio; não solicitar nome, empresa, cargo, CPF, telefone, mensagem, anexo ou identificador real de cliente. Remeter somente dados numéricos do snapshot, categorias, origens, exclusões e versão do método; aviso antes do envio informa que valores de custo também serão tratados por fornecedores de entrega.

Aviso candidato: “Usaremos seu e-mail e os valores desta simulação para enviar o relatório solicitado. Consulte o Aviso de Privacidade para conhecer fornecedores, retenção e seus direitos.” Identidade/canal, fornecedor, base e prazo reais precisam substituir as lacunas antes do uso externo.
Opt-in independente, desmarcado: “Quero receber conteúdos e novidades da GenTests.ai sobre qualidade de software por e-mail. Posso cancelar quando quiser.”
Entrega nunca depende desse opt-in. Não adicionar checkbox genérica de “LGPD” como se resolvesse a base legal.

**EMAIL-02:** relatório HTML com alternativa texto: data, código aleatório de solicitação, versões do produto/método/guia, entradas, proveniência, cálculo linha a linha, arredondamento, naturezas, T/M/Y, hipótese constante, ausências/conflitos e limites. Não incluir rastreio de abertura/pixel ou links que contenham valores/e-mail. Assunto neutro; não usar cifras no assunto. Sem link público persistente para relatório individual; enviar conteúdo no e-mail. Guide link somente após autorização de distribuição do guia exato.

**EMAIL-03:** estados rascunho → validando → aceito para processamento → enviado ao provedor → entregue (somente com evidência de entrega) ou falhou. 202/resposta do provedor não prova caixa de entrada, leitura ou interesse. Reenvio explícito com idempotência; não disparar campanha ou follow-up automático.

**EMAIL-04:** entrega solicitada, marketing, telemetria e contato são finalidades separadas. GT-LGPD-001 §9 conserva bases candidatas; legítimo interesse exige teste específico quando escolhido; gratuidade não prova art. 7 V. Direção/jurídico valida base por finalidade, controlador/canal, subprocessadores/países/mecanismo internacional, termos e prazos/eventos de retenção antes da captura.

**EMAIL-05:** registro mínimo de pedido e preferência em ambiente autorizado, jamais GitHub. Marketing somente se escolhido e com prova de texto/versão, momento, origem e estado; descadastro sem login obrigatório, supressão minimizada e propagação inclusive filas/campanhas programadas. Retenção sem prazo numérico aprovado é bloqueio de ativação; precisa abranger filas, e-mails, CRM, logs, exportações e backups conforme GT-LGPD-003 §8. Pedido de relatório não vira oportunidade/contato no CRM automaticamente.

Prioridade documental de guia por e-mail (DEC-LGPD-20261010-001) respeitada; esta especificação não a altera. Resultado público sem cadastro e impressão local da simulação são propostas específicas do novo produto, sujeitas à Direção. Contingência de download direto **do guia** continua exigindo decisão própria.

## 4. SEO e jornada comercial

Após autorização de indexação: rota candidata `/calculadora-custo-nao-qualidade`, URL canônica no domínio efetivamente aprovado; title específico e description sobre estimativa, não “quanto você perde comprovadamente”. H1 único, introdução, método, exemplo fictício e FAQ em HTML estático indexável, sem depender de JS para explicar o produto. Perguntas: “É saída de caixa?”, “Como evitar duplicidade?”, “E se eu não souber o custo-hora?”, “Como funciona a projeção anual?”.

Links do guia, soluções e contato após aprovação; sitemap e robots atualizados na futura PR técnica. Manter noindex nas versões de homologação e proteger preview quando cabível: noindex não é controle de acesso. Não remover noindex global nesta entrega. Dados individuais não aparecem em URLs, metadados, compartilhamento social ou conteúdo indexável.

Dados estruturados opcionais WebApplication/Breadcrumb somente se refletirem conteúdo real; sem review/rating inventado ou promessa de rich result/posição. Conteúdo editorial informativo, sem extrapolar CISQ/NIST para empresas brasileiras. UTMs permitem somente códigos de campanha previamente autorizados (sem nomes/e-mails); não guardar querystring completa.

Convite para conversa não implica diagnóstico gratuito ou compra. Qualificação futura segue PLN-COM-001: dor confirmada, interlocutor, jornada, urgência e próximo passo; CRM existente registra oportunidade apenas sob autorização, com origem calculadora e preferências por finalidade.
