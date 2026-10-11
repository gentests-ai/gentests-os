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
│ decisões    │ [Total 12] [Execução 4] [Bloqueadas 2]         │
│ Evidências  │ [Revisão 1] [Decisão 3] [Concluídas 2]         │
│             ├───────────────────────┬────────────────────────┤
│             │ Missões prioritárias  │ Alertas/decisões       │
│             │ ID | Estado | Próxima │ tipo, dono, ação      │
│             │ ação | fonte          │ fonte, timestamp      │
│             └───────────────────────┴────────────────────────┘
└──────────────────────────────────────────────────────────────┘
```
* Os números são EXEMPLOS, não necessariamente somam o total. Implementação deve reconciliar contagens e denominadores, sem dupla contagem. Clique em KPI => Missões filtradas, não edição.

## D03 — Missões (Kanban)
```text
[Busca ID] [Estado] [Prioridade] [Área] [Responsável] [Limpar]
[Aguard. refinamento] [Pronta] [Aguard. aceite] [Em execução] [Revisão] [Decisão] [Concluída] [Bloqueada]
    └ ID título dono próxima ação fonte último evento ┘
Condição de qualidade: "Não verificado" transversal, não coluna operacional.
```
Alternativa em lista acessível. Abrir cartão => D04.

## D04 — Detalhe de missão
```text
← Missões / GT-DEMO-001  [FICTÍCIO]  [Estado: aguardando aceite]
Título | prioridade | área | dono | próxima ação | condição de encerramento
[Bloqueios + dependências, com dono e ação]
Trilha: [Despacho preparado] → [Handoff emitido] → [Aceite: NÃO VERIFICADO]
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
