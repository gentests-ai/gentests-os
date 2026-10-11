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
│ [Total 12 (EXEMPLO)]    │
│ [Execução 4 (EXEMPLO)]  │
│ [Bloqueadas 2]          │
│ [Aguard. decisão 3]     │
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
A navegação "Mais" expõe Especialidades, Alertas/decisões e Rastreabilidade de forma etiquetada; não ocultar funções de forma inacessível.

## M03 — Missões
```text
[←] Missões [Filtros]
[Buscar ID/título]
[Aguardando aceite — 2] [expandir]
  [GT-DEMO-002] [dono][ação][origem]
[Em execução — 1] [expandir]
  [GT-DEMO-003] [...]
[Ver todas em lista]
```
Sem Kanban horizontal obrigatório; grupos como listas com títulos semânticos. Status de qualidade permanece etiqueta separada.

## M04 — Detalhe de missão
```text
[← Missões] GT-DEMO-002
[Título] [Status: aguardando aceite]
[Área] [Prioridade] [Dono]
[Próxima ação] [Condição de conclusão]
[Handoff: emitido] [Aceite: Não verificado]
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
