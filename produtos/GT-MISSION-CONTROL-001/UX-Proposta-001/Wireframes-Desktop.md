# Wireframes desktop — UX v0.1.0
**TODOS OS DADOS ABAIXO SÃO FICTÍCIOS — não refletem o GitHub.** Desenhos textuais estáticos; sem software implementado.

## D01 — Login/autorização
```text
┌──────────────────────────────────────────────────────────────┐
│ [LOGO OFICIAL] GenTests.ai                                  │
│                         Mission Control privado              │
│                 [ Entrar por autenticação autorizada ]       │
│          Acesso restrito. Nenhuma missão antes do login.     │
└──────────────────────────────────────────────────────────────┘
```
Falha 401/403: "Acesso não autorizado" (sem qualquer conteúdo interno). Nenhuma credencial em browser.

## D02 — Dashboard executivo
```text
┌─────────────┬────────────────────────────────────────────────┐
│ GenTests.ai │ Mission Control  [Perfil autorizado]           │
│ Dashboard * │ GitHub | Último sucesso: 11/10 14:00 (EXEMPLO) │
│ Missões     │ [Última tentativa] [Cobertura: parcial]        │
│ Especialid. ├────────────────────────────────────────────────┤
│ Alertas/    │ [Filtros: estado | área | dono | prioridade]    │
│ decisões    │ [Identificadas 12] [Estado verificado 10]      │
│ Evidências  │ [Não verificado 2] [Execução 2] [Bloqueio 2]  │
│             ├───────────────────────┬────────────────────────┤
│             │ Missões prioritárias  │ Alertas/decisões       │
│             │ ID | Estado | Próxima │ tipo, dono, ação      │
│             │ ação | fonte          │ fonte, timestamp      │
│             └───────────────────────┴────────────────────────┘
└──────────────────────────────────────────────────────────────┘
```
* Fixture F-12 FICTÍCIA: estados comprovados refinamento 0 + pronta 1 + aceite 1 + execução 2 + revisão 1 + decisão 2 + concluída 1 + bloqueada 2 = 10. Estado não verificado 2 (fila de qualidade, NÃO novo estado operacional). Total identificado 10+2=12. Cobertura PARCIAL 12 de 15 IDs esperados (80%); 3 não recuperados, estados desconhecidos e fora das contagens. Lead time: NÃO APURADO (falta histórico); refinamento: ZERO verificado só entre as 12 recuperadas. Clique em KPI => Missões filtradas, não edição.

## D03 — Missões (Kanban)
```text
[Busca ID] [Estado] [Prioridade] [Área] [Responsável] [Limpar]
[Aguard. refinamento] [Pronta] [Aguard. aceite] [Em execução] [Revisão] [Decisão] [Concluída] [Bloqueada]
    └ ID título dono próxima ação fonte último evento ┘
[FILA DE QUALIDADE CONSULTÁVEL: Estado não verificado — 2] (fora do Kanban operacional)
  GT-DEMO-011 | estado operacional não comprovado | fonte disponível | regularização
  GT-DEMO-012 | estado operacional não comprovado | fonte disponível | regularização
Etiqueta secundária de qualidade pode aparecer em cartão com estado comprovado, mas não soma novamente a missão. "Não verificado" não é estado operacional.
```
Alternativa em lista acessível. Abrir cartão => D04.

## D04 — Detalhe de missão
```text
← Missões / GT-DEMO-001  [FICTÍCIO]  [Estado: aguardando aceite]
Título | prioridade | área | dono | próxima ação | condição de encerramento
[Bloqueios + dependências, com dono e ação]
Trilha informativa (etapas INDEPENDENTES, não barra de conclusão):
 [Despacho preparado/registrado: COMPROVADO*]   [Notificação tentada: NÃO VERIFICADO]
 [Agente acionado confirmado: NÃO VERIFICADO] [Handoff emitido: COMPROVADO*]
 [Aceite explícito: NÃO VERIFICADO]           [Execução iniciada confirmada: NÃO VERIFICADO]
 * SOMENTE NO EXEMPLO FICTÍCIO, com eventos individuais de prova simulados; produção requer URL, timestamp, ator.
Origem: [Issue GitHub] [PRs] [Commits] [Evidências]
Timeline: tipo | ocorreu | observado | ator | confiança | parser | fonte
[Abre issue no GitHub]     NÃO EXISTE botão "aprovar"/"executar"
```
Se PR merged e DoD não verificado, renderizar "Encerramento não verificado".

## D05 — Especialidades
```text
[Área] [Papel] [Missões atribuídas]
Especialidade | atividade COMPROVADA | último evento | evidência | próxima ação
Sem evento = "Sem atividade comprovada" (não "offline"/"online").
```

## D06 — Alertas e decisões
```text
[Alertas] [Decisões pendentes]
[Handoff sem aceite]   responsável | motivo | próxima ação | prova
[Missão sem dono]      "Não informado" | link origem
[Bloqueio]             razão/dono/ação ou lacuna sinalizada
[Decisão Direção]      autoridade | issue | evento | data
```
Nenhum botão de "aprovar", "enviar" ou "despachar".

## D07 — Rastreabilidade e sincronização
```text
GitHub (canônico) | Último sucesso | Última tentativa | Cobertura | Falhas
[event_id] [tipo] [ocorreu/observado] [ator] [confidence] [fonte]
Falha 429: "Informações possivelmente desatualizadas" (timestamps mantidos)
```

## D08 — Tela de erro/sem dados
- Vazio comprovado: "Nenhuma missão elegível para estes filtros" + limpar.
- Resultado parcial: "Cobertura parcial"; preservar valores antigos rotulados com data.
- Status em dúvida: "Não verificado"; detalhe da evidência.
- Sem prazo explícito: não produzir alerta de atraso.
- 403 sem autenticação: nenhuma área privada exibida.

Fluxo navegação: D01 → D02 → D03 → D04 → link GitHub; D02 → D06 → D04; D02 → D05 → D04; qualquer tela autenticada → D07. Retorno preserva filtros.
