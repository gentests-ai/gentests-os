# Wireframes mobile — UX v0.1.0
**DADOS E DATAS DEMONSTRATIVOS, NÃO DADOS REAIS.** Largura de referência 320–430 CSS px, reflow e zoom conforme WCAG 2.2 AA (ver especificação).

## M01 — Login
```text
┌─────────────────────────┐
│ [LOGO OFICIAL]          │
│ Mission Control         │
│ Área privada            │
│ [Entrar]                │
│ Acesso restrito         │
└─────────────────────────┘
```
Sem conteúdo privado renderizado em falha de autenticação.

## M02 — Dashboard
```text
┌─────────────────────────┐
│ GenTests.ai   [Menu]    │
│ Visão executiva         │
│ [Dados desatualizados?] │
│ GitHub • Último sucesso │
│ [Filtros]               │
│ [Identificadas 12]      │
│ [Verificadas 10]        │
│ [Não verificadas 2]     │
│ [Execução 2] [Bloq. 2]  │
│ [Cobertura: 12/15=80%]  │
│ [Lead time: Não apurado]│
│ Missões prioritárias    │
│ ┌─────────────────────┐ │
│ │ GT-DEMO-001         │ │
│ │ Estado: revisão     │ │
│ │ Dono: Não informado │ │
│ │ Próxima ação: ...   │ │
│ │ [Ver evidência]     │ │
│ └─────────────────────┘ │
│ [Início][Missões][Mais] │
└─────────────────────────┘
```
Fixture F-12: 10 missões com estado operacional comprovado (refinamento 0, pronta 1, aceite 1, execução 2, revisão 1, decisão 2, concluída 1, bloqueada 2) + 2 em fila de qualidade "Estado não verificado" = 12 recuperadas. 15 esperadas, 3 ausentes por cobertura parcial (80%) e não contadas. Zero 0 indica nenhuma no estado refinamento dentre as recuperadas, não certeza sobre as três ausentes. Lead time Não apurado não é zero. Todos os números são FICTÍCIOS.

A navegação "Mais" expõe Especialidades, Alertas/decisões e Rastreabilidade de forma etiquetada; não ocultar funções de forma inacessível.

## M03 — Missões
```text
[←] Missões  [Filtros ativos: 0] [Abrir filtros]
[Buscar ID/título]
[Painel FILTROS: Estado | Prioridade | Área | Responsável]
[Aplicar] [Limpar filtros] [Fechar]
[Estado não verificado — 2] [abrir fila de qualidade]
  [GT-DEMO-011] [Sem estado comprovado] [Fonte] [Próxima ação]
  [GT-DEMO-012] [Sem estado comprovado] [Fonte] [Próxima ação]
[Aguardando aceite — 1] [expandir]
  [GT-DEMO-002] [dono][ação][origem]
[Em execução — 2] [expandir]
  [GT-DEMO-003] [dono][ação][origem]
[Ver todas em lista]
```
Sem Kanban horizontal obrigatório; grupos como listas com títulos semânticos. A fila consultável "Estado não verificado" é condição de qualidade e não transição operacional. Missão ali não aparece simultaneamente em grupo operacional. Painel mobile explicita todos os filtros: estado (inclusive "Não verificado" rotulado qualidade), prioridade, área e responsável; busca, aplicar, limpar, chips ativos e retorno preservado. Não inferir zero global com cobertura parcial.

## M04 — Detalhe de missão
```text
[← Missões] GT-DEMO-002
[Título] [Status: aguardando aceite]
[Área] [Prioridade] [Dono]
[Próxima ação] [Condição de conclusão]
[Trilha de eventos — passos INDEPENDENTES]
[Despacho preparado/registrado: Comprovado*]
[Notificação tentada: Não verificado]
[Agente acionado confirmado: Não verificado]
[Handoff emitido: Comprovado*]
[Aceite explícito: Não verificado]
[Execução iniciada confirmada: Não verificado]
[* Provas simuladas na fixture; produção só com fonte, data, ator]
[Eventos e evidências] [expandir]
[Evento + data + ator + fonte]
[Abrir issue GitHub ↗]
```
Informação crítica expandida por padrão; timeline em cards verticais, não tabela com scroll horizontal.

## M05 — Especialidades
```text
[Especialidades] [Filtro área]
[Papel] [Missão atribuída]
[Último evento confirmado ou "Sem atividade comprovada"]
[Ver evidência]
```

## M06 — Alertas/decisões
```text
[Alertas] [Decisões] (abas)
[Tipo: Handoff sem aceite]
[Dono: papel/Não informado]
[Próxima ação] [Ver fonte]
```
"Decisões" mostra demandas de deliberação; nenhuma decisão pode ser tomada pelo painel.

## M07 — Falha e estado vazio
```text
[Faixa fixa de status: sincronização falhou]
[Último sucesso DD/MM HH:mm]
[Última tentativa DD/MM HH:mm]
[Valores antigos: desatualizados]
[Ver origem]
```
Para zero resultados: "Sem resultados para filtros" + "Limpar filtros"; para dado ausente "Não informado"; para prova ausente "Não verificado"; para métrica sem base "Não apurado".

## M08 — Acessibilidade e navegação
Ordem teclado e leitor de tela: cabeçalho → aviso de sincronização → filtros → KPIs → listas → navegação. Foco visível, alvo de toque preferencial 44 px, controle "Pular ao conteúdo", rótulos explícitos, contador anunciante somente sob ação do usuário, sem foco perdido ao abrir/fechar filtros. Links externos informam destino. Cabeçalho da missão permanece contextual após retorno. Estados por texto+ícone, não apenas cor.
