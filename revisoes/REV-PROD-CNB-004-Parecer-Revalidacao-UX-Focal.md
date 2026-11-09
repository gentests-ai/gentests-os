---
id: REV-PROD-CNB-004
tipo: parecer-independente-revalidacao-focal-ux
data: 2026-10-10
pr_execucao: 36
commit_revisado: e465ecf3c392e9cfce92b5013e56dfdbc63f791a
achado: CNB-UX-REV-01
resultado: resolvido-documental-e-visualmente
direcao: deliberacao-pendente
implementacao: nao-autorizada
merge: nao-autorizado
---
# REV-PROD-CNB-004 — Revalidação focal CNB-UX-REV-01

**RESULTADO: CNB-UX-REV-01 RESOLVIDO NA PROPOSTA VISUAL. APTO A DELIBERAÇÃO DE ENCERRAMENTO DA ETAPA UX/UI PELA DIREÇÃO.**

## Escopo e método
Conferidos na PR #36 e no commit exato `e465ecf3c392e9cfce92b5013e56dfdbc63f791a` os SVGs D08 e M06, **inspecionados visualmente** os PNGs `Evidencia-D08-CNB-UX-REV-01.png` e `Evidencia-M06-CNB-UX-REV-01.png`, README §12, `Mapa-Prototipo.json` e existência/obtenção do PDF `GT-PROD-CNB-001-Prototipo-UX-v0.1.pdf`. Conferida abertura/Draft da PR #36. Não reabertas outras 27 pranchas ou documentação metodológica. **Não foi executada navegação interativa em leitor do PDF nem renderização visual independente do binário PDF**; quanto ao PDF, consistência sustentada pelo mapa, arquivos fonte/evidência e matriz do autor, não por clique real.

## Matriz focal
| Verificação | Resultado | Evidência |
|---|---|---|
| D08 desktop: botão indisponível | **CONFORME** | SVG e PNG: ação “Imprimir novo relatório” cinza, instrução imediatamente abaixo “Desabilitado · Recalcule para habilitar”, alerta “Resultado desatualizado”. Não há destino no mapa para botão indisponível. |
| M06 mobile: botão indisponível | **CONFORME** | SVG e PNG: mesmo rótulo e estado, instrução legível, separada de ação “Ver novo cálculo S2”. Não há destino no mapa para botão indisponível. |
| Relatório anterior preservado | **CONFORME** | D08 e M06 mostram cartão “Relatório anterior”, pedido P1, método CNQ-01, R$4.760,00, conteúdo vinculado ao cálculo anterior; ação “Ver relatório anterior” mantém link para R01 no mapa. |
| Consistência PDF/mapa | **CONFORME DOCUMENTALMENTE, COM LIMITAÇÃO EXPLÍCITA** | PDF da versão corrigida recuperado do repositório; README §12 afirma PDF recomposto. Mapa de 29 páginas mantém D08 na p.12, M06 na p.25 e destinos R01, sem link para botão desabilitado; SVGs e evidências concordam. Não executado teste de clique real nem render independente do PDF. |

## Residual
O botão é figura de protótipo, não controle HTML; na implementação futura exigir `disabled` nativo, impedir acionamento e oferecer explicação acessível. Estado de impressão, snapshot e acesso anterior **não foram testados em software**. As regras CF-03/CF-04 e WCAG 2.2 AA continuam dependentes de build e evidência. CNB-UX-REV-02/03 foram tratados em handoff e **não revalidados formalmente** aqui; preservar parecer #37. Nenhuma falha material nova identificada no foco.

## Deliberação recomendada
**Encerrar CNB-UX-REV-01 no âmbito documental/visual** e encaminhar a proposta UX/UI v0.1.1 para aceite visual e decisão de prioridade/teto de horas pela Direção. **Não abrir nova auditoria integral**. Aprovação do protótipo não autoriza implementação, publicação, merge, e-mail, cadastro, coleta, telemetria, contratação ou alterações do site. Manter PR #36 aberta e Draft.
