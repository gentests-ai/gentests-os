---
id: REV-PROD-CNB-003
tipo: parecer-independente-ux-ui-focal
data: 2026-10-10
objeto: GT-PROD-CNB-001-UX-Proposta-001
pr_origem: 36
commit_revisado: 1656257d8ba84ac643aa96926cb35208ce0bf1fd
resultado: aprovado-com-ressalvas-para-deliberacao-visual
aprovacao_direcao: pendente
implementacao_autorizada: nao
publicacao_autorizada: nao
---
# REV-PROD-CNB-003 — Parecer independente UX/UI focal

**Resultado: APROVADO COM RESSALVAS PARA DELIBERAÇÃO DE PLANEJAMENTO. NÃO É HOMOLOGAÇÃO DE PRODUTO, WCAG, NEM AUTORIZAÇÃO DE IMPLEMENTAÇÃO.**

## Escopo e evidência
Revisados a PR #36 aberta/Draft, commit `1656257d8ba84ac643aa96926cb35208ce0bf1fd`, README, mapa de 29 pranchas, Contrastes.json, prévias PNG desktop/mobile e conteúdo SVG das pranchas D03, M03, D07, D08 e R01. Comparação focal com especificação v0.1.1 do commit `8df9e2f16019be3095ca7ab2bfe69c2ca94d6d8c` e parecer #31. **Não foi inspecionado visualmente cada um dos 29 quadros ou reproduzida a navegação real dos 92 links do PDF**; essas verificações são relatadas pelo autor. Não houve testes em navegador, telefone, teclado, leitor de tela, impressão ou execução de cálculos. Nenhuma auditoria financeira/documental reaberta.

## Conformidades observadas
- Direção visual coerente: azul profundo, turquesa, superfícies claras, tipografia legível, hierarquia entre valor principal, composição, projeções e CTA; prévias desktop/mobile sem cortes ou colisões visíveis.
- Projeção ilustrativa de R$4.760, R$14.280/mês e R$171.360/12 meses corretamente rotulada como hipótese; D07 apresenta subtotal incompleto de R$2.860 e projeções somente das parcelas mensuradas.
- D03 compara A↔O com valores e origens e lista as seis relações; não usa IDs diferentes como prova de distinção; M03 reconhece outras comparações pendentes de representação.
- D08 explicita desatualização após edição e preserva o pedido P1/S1 anterior; R01 identifica hipótese, origem e versão do método.
- Recomendações de WCAG 2.2 AA, contraste e testes futuros são proporcionais e explicitamente não equivalem à conformidade operacional. Fase 1 exclui e-mail, cadastro e telemetria.
- Planejamento distingue 29–48h de desenvolvimento e 49–81h total com handoff, QA, revisão e correções, sem orçamento aprovado; coerente como estimativa hipotética.

## Achados focais
| ID / severidade | Localização | Evidência | Recomendação proporcional |
|---|---|---|---|
| **CNB-UX-REV-01 — MÉDIA** | `pranchas/D08.svg`; README §5, edição após resultado; CF-03/04 | D08 apresenta ação visível **“Imprimir novo relatório”** ao lado de “Resultado desatualizado”, enquanto a regra do mesmo documento diz que novo relatório fica bloqueado até recálculo. Sem indicação inequívoca de controle desabilitado na representação textual, há risco de ambiguidade no handoff. | Marcar explicitamente o botão como desabilitado, com explicação “Recalcule para habilitar”, ou retirar a ação da prancha de estado desatualizado. Preservar acesso à prévia do pedido anterior. Conferir mesma semântica em mobile. |
| **CNB-UX-REV-02 — BAIXA** | `pranchas/M03.svg`, README §§4–5, CF-01–03 | Mobile ilustra apenas o par A↔O, relegando cinco pares a instrução textual “Também comparar...”. Isso é adequado como amostra estática, mas não demonstra a localização de todas as comparações nem o indicador de pendência numa jornada mobile longa. | Acrescentar no handoff indicação simples de lista/progresso de pares (ex. 1/6 e pendentes) e estratégia de expansão, sem criar seis novas pranchas. |
| **CNB-UX-REV-03 — BAIXA** | `Contrastes.json`, README §6 | A borda #64788D sobre #F3F6FA é 4,20:1 e sobre branco 4,55:1; não é falha AA por si (contraste de componentes geralmente 3:1), mas o arquivo não documenta variações de estado hover/foco/disabled. | Na futura implementação, medir todos os estados e contrastes reais; não declarar AA com base somente nos 12 tokens. Sem correção documental impeditiva. |

## Residual e limites
- Os 29 desenhos, PDF e SVG são protótipos com fixtures fixas. Os 34 critérios CA e oito CF **não foram executados**. Não afirmar aprovação de funcionalidade, navegação PDF, PDF/UA, reflow a 320px, impressão real, segurança ou WCAG 2.2 AA.
- Fontes e símbolo têm documentação de origem; o autor declara que a equivalência binária do ícone com o commit do site não foi verificada. Confirmar asset oficial antes de produção, sem bloquear planejamento.
- O total 49–81h é hipótese e depende de capacidade, prioridades comerciais e futuros testes; não inferir custo zero de mão de obra.

## Decisão recomendada
**APTO À DELIBERAÇÃO DA DIREÇÃO COM UMA RESSALVA MÉDIA DE HANDOFF E DUAS BAIXAS.** Solicitar ao autor apenas uma correção focal do estado de impressão desatualizada (CNB-UX-REV-01), se a Direção desejar encerrar o design antes de futura implementação. CNB-UX-REV-02/03 podem ser incorporados ao handoff/critério técnico sem nova rodada formal. Não reabrir auditoria financeira, UX integral ou PDF do guia. Direção decide aceite visual, teto de horas/capacidade, prioridade comercial e eventual autorização **separada** de implementação. PR #36 permanece Draft, sem merge/publicação/site/cadastro/e-mail/leads/telemetria.
