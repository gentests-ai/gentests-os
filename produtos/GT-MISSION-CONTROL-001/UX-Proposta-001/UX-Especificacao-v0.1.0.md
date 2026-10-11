# GT-MISSION-CONTROL-001 — Proposta UX/UI v0.1.0
**Estado:** entrega documental para conferência; implementação NÃO autorizada
**Handoff:** GT-MISSION-CONTROL-001-UX-01-CONT | **Data:** 2026-10-11
**Fonte funcional:** [Issue #58](https://github.com/gentestsai-sudo/gentests-os/issues/58) (Produto v0.1.0)
**Governança:** [#55](https://github.com/gentestsai-sudo/gentests-os/issues/55), [#47](https://github.com/gentestsai-sudo/gentests-os/issues/47), [#53](https://github.com/gentestsai-sudo/gentests-os/issues/53)
**Identidade:** [01-Empresa/Identidade-Visual.md](../../../01-Empresa/Identidade-Visual.md)

## 1. Princípios e fronteiras
Painel WEB PRIVADO, autenticado, **somente leitura**. GitHub permanece fonte canônica: toda missão, decisão, alerta, data e status mostra o vínculo para evento verificável, proveniência e versão. Sem editar issue, aprovar, criar despacho, notificar, executar, publicar, merge ou conceder acesso. As capturas/wireframes são **fixtures fictícias**; números são demonstrativos, nunca amostra do backlog real. Nunca indicar "online" sem telemetria confirmada. Não usar merge de PR nem fechamento de issue como prova isolada de conclusão.

## 2. Arquitetura de informação e jornadas
Navegação primária (desktop sidebar, mobile barra inferior/menu acessível): **Visão executiva** / **Missões** / **Especialidades** / **Alertas e decisões** / **Rastreabilidade**. "Decisões" é uma aba filtrada no módulo Alertas, não um mecanismo de aprovar. Todas as telas compartilham: identidade GenTests.ai, origem GitHub, última tentativa, última sincronização bem-sucedida, indicação de cobertura e qualidade, filtro aplicado e acesso a Ajuda de estados. Breadcrumbs voltam ao ponto de origem, mantendo filtros e posição do scroll.

**Direção:** Login → dashboard → filtro "Aguardando decisão" → missão → evento/autoridade/evidência → abrir GitHub para deliberação em canal autorizado → retorno ao painel para verificar atualização (sem inferir sincronismo instantâneo).
**Orquestrador:** Login → missões/kanban → filtros área/dono/prioridade/órfãos → missão → handoff sem aceite, próxima ação e link → regularização externa no GitHub → conferência de sincronização.
**Jornada transversal de erro:** qualquer página → aviso de dados desatualizados/cobertura parcial → consultar último sucesso/tentativa → abrir fonte; nunca apresentar dados antigos como atuais.

## 3. Wireframes
Versões descritivas em [Wireframes-Desktop.md](Wireframes-Desktop.md) e [Wireframes-Mobile.md](Wireframes-Mobile.md). Cada elemento é uma proposta de interface, não tela implementada.

## 4. Componentes e especificação de estado
| Componente | Conteúdo mínimo | Ação permitida | Estado de falha |
|---|---|---|---|
| Cabeçalho de sincronização | fonte, último sucesso, última tentativa, cobertura, timezone | ver detalhes | aviso persistente e timestamp; nunca ocultar dados antigos |
| KPI estado | número de missões canônicas elegíveis + denominador e filtros | abrir lista filtrada | "Não apurado" / "Cobertura parcial"; jamais zero falso |
| Cartão de missão | ID, título, área, prioridade, estado, dono, próxima ação, último evento, fonte | abrir detalhe | campos faltantes "Não informado" |
| Coluna Kanban | estado exclusivo, quantidade elegível | filtrar/abrir missão | condição de qualidade separada do estado |
| Trilha de handoff | preparado, acionado, emitido, aceito, início confirmado, entregue | abrir prova | ausente = "Não verificado"; nunca inferir aceite |
| Cartão de especialidade | função, atribuições, última atividade confirmada, evidência | abrir missão/evento | "Sem atividade comprovada", não "Offline" nem "Online" |
| Alerta | tipo, gravidade, motivo, dono, ação, prova, atualização | abrir evidência | regra sem evidência = "Não verificado" |
| Decisão pendente | assunto, competência/autorização, fonte, próxima ação | abrir registro GitHub | não oferece botões de aprovação |
| Timeline auditável | event_id, ator, ocorrido/observado, fonte, confiança e parser | abrir link canônico | "Fonte indisponível", sem alegar confirmação |
| Controle de filtros | estado, prioridade, área, responsável, buscar ID | aplicar/limpar | preserva seleção e comunica 0 resultados |

**Vocabulário de exibição PROVISÓRIO, dependente da #55:** Aguardando refinamento; Pronta; Aguardando aceite; Em execução (somente com evidência explícita); Aguardando revisão; Aguardando decisão; Concluída (com DoD verificável); Bloqueada (motivo/dono/ação obrigatórios). **Desconhecido/inconsistente** é qualidade de dado, não estado operacional. Cada missão pertence a exatamente uma contagem de estado. Sem estado apurável, incluir em "Estado não verificado" fora das categorias mutuamente exclusivas e explicitar denominador/cobertura.

**Eventos não intercambiáveis:** atividade registrada ≠ despacho preparado ≠ notificação tentada ≠ agente acionado confirmado ≠ handoff emitido ≠ handoff aceito ≠ execução iniciada confirmada ≠ entrega submetida ≠ revisão concluída ≠ autorização concedida ≠ encerramento comprovado. Label, menção, silêncio, comentário genérico, issue fechada ou PR merged não substituem comprovação.

## 5. Estados de interface / microcopy
| Cenário | Apresentação e microcopy |
|---|---|
| Inventário vazio verificado | "Nenhuma missão elegível encontrada nos filtros atuais." Mostrar filtros, cobertura e última sincronização. |
| Nenhuma ocorrência sob filtro | "Sem resultados para estes filtros." Botão "Limpar filtros" local. Não alegar ausência global. |
| Carregando | skeleton rotulado "Carregando dados" sem valores zero temporários. |
| Campo ausente | "Não informado" + orientação "Consultar issue canônica". |
| Estado ambíguo | "Não verificado — evidências insuficientes" + eventos disponíveis; não declarar encerramento. |
| Handoff não aceito | "Handoff emitido; aceite não registrado" e link; não colocar em execução. |
| Bloqueada | "Bloqueada — motivo: [motivo comprovado]; responsável: [dono]; próxima ação: [ação]"; lacunas sinalizadas. |
| Sem agente comprovado | "Último evento confirmado: [data/fonte]" ou "Sem atividade comprovada"; sem presença online. |
| Token ausente/401/403 | página de acesso negado sem qualquer conteúdo privado; orientações de autenticação, sem tokens. |
| API 429/5xx/timeout | faixa "Sincronização indisponível; informações podem estar desatualizadas", último sucesso e última tentativa, motivo genérico, sem segredos. |
| Retorno parcial | "Cobertura parcial: [identificados]/[esperados se conhecidos]; totais não representam universo completo". |
| Evidência inacessível | "Fonte não disponível para este perfil"; sem confirmação substitutiva. |
| Métrica inelegível | "Não apurado" + motivo; nunca exibir 0 por falta de histórico. |
| Autorização reservada | "Decisão exigida da Direção — consultar evidência"; sem botão de aprovar. |
| Segurança | indisponibilidade de autenticação: não renderiza HTML/JSON privado antes de autorização backend. |

A atualização não é chamada de "em tempo real". Texto sugerido: "Última sincronização bem-sucedida: DD/MM/AAAA HH:mm (America/Sao_Paulo); tentativa: ...". Timestamp de origem e timezone explícitos; evitar cor como único significado. Em mobile a barra de erro deve continuar perceptível ao rolar. Links externos anunciam "Abre GitHub em nova aba" quando aplicável.

## 6. Diretrizes visuais e acessibilidade
Paleta documental oficial: #04132F, #075BDF, #00BDF2, #00CCB5, #7546ED, #FFFFFF. Uso ilustrativo de fundo marinho e superfícies com bordas; contraste de pares reais ainda deve ser medido, não presumido pela paleta. Logo: SOMENTE ativo original do guia oficial, sem monograma improvisado, proporção preservada. Tipo, ícones e detalhes visuais sujeitos à validação com guia canônico no Drive.
Padrão-alvo **WCAG 2.2 AA**: navegação por teclado com ordem coerente, skip-link para conteúdo, foco visível com contraste, títulos hierárquicos, landmarks, nomes acessíveis, estados não dependentes apenas de cor, status e erros com anúncio apropriado, labels de filtros, descrição de contagens e tabelas, teclado no Kanban com alternativa em lista, sem drag-and-drop obrigatório, alvos de toque de pelo menos 24×24 CSS px (preferência 44×44), zoom até 200% sem perda de funcionalidade, reflow a 320 CSS px equivalente, espaços e controle de tamanho de texto, suporte a redução de movimento. Modal apenas para detalhes não navegacionais, foco recuperado ao fechar. Não atualizar o leitor de tela repetitivamente em polling; anunciar apenas mudança material solicitada.
Breakpoints conceituais: >=1024px sidebar e grid 4/6 cards conforme largura; 600–1023px navegação compacta e grid 2 colunas; <600px cartões em coluna, tabelas convertidas em pares rótulo/valor, filtros em painel acessível. Kanban mobile alterna para lista agrupada, com títulos e quantidades. Sem rolagem horizontal obrigatória da página.

## 7. Acesso, filtros e auditabilidade
Login/erro de acesso são superfícies separadas do aplicativo e do cache privado. Um papel não autorizado jamais vê informações pela tela nem pelos endpoints. Qualquer link de estado abre detalhe contendo evento, occurred_at, observed_at, confiança explicit/derived/unknown, source_url e versão do parser; não inventar links para eventos ausentes. Filtros persistem na navegação interna, com "Limpar filtros". Contagens usam missões canônicas, não somam PRs como missões. Dados demonstrativos têm tarja "FÍCTÍCIOS"; não contam como reconciliação real. Segurança do conteúdo de issue: renderização sem execução de HTML/scripts.

## 8. Matriz de rastreabilidade
MC-01: tela de acesso e negação | MC-02: lista/cartão e detalhe | MC-03: KPIs e proveniência | MC-04: Kanban + lista mobile | MC-05: detalhe + timeline | MC-06: especialidades | MC-07: alertas/decisões | MC-08: banner de sincronização | MC-09: evidências e confiança.
CA-01: IDs, cobertura, exclusividade | CA-02: prova de estado/alerta | CA-03: eventos separados em timeline | CA-04: handoff sem aceite | CA-05: "Não verificado" para mero merge/issue fechada | CA-06: filtros e acessibilidade | CA-07: falhas e last-success | CA-08: acesso bloqueado | CA-09: sem online falso | CA-10: "Não apurado" e requisito QA amostra real | CA-11: apenas navegação/links.

## 9. Verificações e limites
**Verificado documentalmente no escopo UX:** correspondência conceitual MC-01..09, existência de propostas desktop/mobile, ausência de controles de mutação nos wireframes, estados de erro/sem dados, referências da marca. **Não realizados:** testes de leitor de tela/teclado, dispositivos físicos, medições de contraste, testes de integração, autenticação, segurança, amostra real, inspeção de implementação, validação por Produto ou revisão independente. São especificações para posterior QA, não resultados de testes executados.

## 10. Riscos, pendências e decisão
R1 governança #55: taxonomia e DoD não homologados; R2 #53 permissões de leitura sem aprovação; R3 #47 eventos de acionamento não reconciliados; R4 qualidade/histórico GitHub incompletos; R5 cor e logo precisam de checagem final do guia Drive; R6 métricas WIP/aging futuras exigem baseline; R7 custo/limites de sincronização para Engenharia/Infra. Não alterar POL-003 nem criar permissões neste PR.
**Próximo gate:** Orquestrador confere completude; Gerente de Produto avalia aderência funcional; depois revisão independente por encaminhamento específico. **Não solicitar implementação.**

## 11. Ajustes focais de Produto — PROD-59-01/02/03 (11/10/2026)
**PROD-59-01 — Agrupamento operacional de consulta (não estado operacional):** a navegação Missões e o dashboard oferecem uma **seção consultável "Estado não verificado"**, além das colunas/grupos de estados operacionais. É uma *fila de qualidade de dados* para missões cujo estado operacional não pode ser comprovado. Essa fila não é uma transição na máquina de estados. Missão sem estado verificável integra **uma única categoria de exibição**, na fila de qualidade, e nenhuma coluna de estado; missão com estado comprovado pode receber etiqueta secundária de qualidade (por exemplo, dono ausente) sem duplicar contagem. Filtro "Estado" oferece "Estado não verificado" como opção explicitamente marcada *condição de dados*. O cartão mostra ID, evidência disponível, razão da incerteza, responsável por regularizar e próxima ação (ou "Não informado").

**PROD-59-03 — Regra aritmética verificável (fixture F-12, inteiramente FICTÍCIA):**
- 12 missões canônicas elegíveis **identificadas na coleção lida**; 10 com estado comprovado e 2 em "Estado não verificado".
- Partição exclusiva das 10 comprovadas: aguardando refinamento **0**, pronta **1**, aguardando aceite **1**, em execução **2**, aguardando revisão **1**, aguardando decisão **2**, concluída **1**, bloqueada **2**. Soma = 10; mais 2 não verificadas = 12. O indicador "Total identificado" inclui todas as 12, inclusive as 2 sem estado verificável.
- **Zero verificado (0)** só quando a população elegível e a condição foram consultadas com sucesso e nenhuma missão satisfaz aquele estado (ex.: aguardando refinamento 0 **dentro da coleção lida**, não afirmação sobre universo incompleto).
- **Não apurado** é métrica sem base suficiente, ex.: lead time = Não apurado; não se deve substituir por 0.
- **Cobertura parcial** é qualidade da extração, independente das contagens: fixture leu 12 missões e a fonte informa 15 IDs elegíveis conhecidos; portanto **12/15 (80%) de cobertura** e **3 não recuperados**, fora de todas as contagens. Não atribuir estado aos três ausentes. Se o total esperado não for conhecido, mostrar "12 identificadas / universo desconhecido" e cobertura "Não apurada", jamais 100%.
- A soma dos indicadores particionados só é mostrada como reconciliação da coleção **lida**; é vedado apresentar 12 como total completo do universo se a cobertura for parcial. KPIs resumidos como "Em execução 2", "Bloqueadas 2", "Revisão 1", "Decisão 2", "Concluídas 1" são *subconjuntos*, não soma alternativa do total.
- Filtros de **estado, prioridade, área, responsável** e busca por ID/título disponíveis em desktop e painel mobile, com contagens recalculadas sobre a coleção filtrada, filtros ativos visíveis, "Aplicar" e "Limpar"; comunicar "0 resultados verificados" apenas para filtro em conjunto completo consultado. Em cobertura parcial, "0 encontrados nos dados disponíveis" e aviso persistente.

**PROD-59-02 — Timeline não inferencial:** apresentar como etapas/eventos distintos, nesta ordem de leitura: **despacho preparado/registrado → notificação tentada → agente acionado confirmado → handoff emitido → aceite explícito → execução iniciada confirmada**. Cada nó contém status **Comprovado** apenas com evento individual, timestamp, ator e URL da fonte. Sem evidência exibir **Não verificado**, não marca de conclusão. A ordem é explicativa, não garantia de ocorrência cronológica: handoff pode ser emitido sem notificação comprovada e sem acionamento. **Registro de despacho no GitHub não comprova notificação, acionamento, aceite ou execução**; notificação tentada não comprova entrega; acionamento não comprova aceite; aceite não comprova início. Em caso de lacuna, desenhar sequência com nós independentes, sem linha contínua de progresso ou check verde implícito. A lista de eventos exibe ocorrido/observado, ator, fonte e confiança; não inserir eventos fictícios como fatos reais.

**Verificação:** fixture F-12 somada manualmente (0+1+1+2+1+2+1+2=10; 10+2=12; 12/15=80%); critérios de revisão documental apenas. Não é teste funcional, de QA ou reconciliação do repositório real.
