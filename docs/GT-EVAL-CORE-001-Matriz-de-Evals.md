---
tipo: especificacao-evals
id: GT-EVAL-CORE-001
versao: 0.1.0
status: proposta
responsavel: Direcao
---

# GT-EVAL-CORE-001 — Matriz de Evals do Motor de Agentes

> Evals são critérios executáveis de comportamento do sistema. Esta matriz é proposta; os cenários não estão automaticamente implementados nem aprovados.

## Princípios
- Cada capacidade deve nascer com critérios de avaliação.
- Avaliar comportamento observado, não apenas presença de código ou labels.
- Cobrir caminhos felizes, falhas, concorrência, recuperação e abuso de contrato.
- Registrar versão do cenário, configuração, ambiente, resultado e evidência.
- Não usar um único score agregado para esconder falha crítica.

## Matriz inicial

| ID | Dimensão | Cenário | Resultado esperado |
|---|---|---|---|
| COORD-001 | Concorrência | Dois agentes tentam claim da mesma tarefa exclusiva | Um claim válido; outro recebe conflito sem executar |
| COORD-002 | Paralelismo | Dois agentes executam tarefas independentes | Ambas progridem sem bloqueio global |
| COORD-003 | Fencing | Agente antigo tenta gravar após perder lease | Escrita rejeitada |
| COORD-004 | Recuperação | Runtime reinicia com execução interrompida | Estado recuperado sem replay indevido |
| HAND-001 | Handoff | Agente transfere tarefa a outro perfil | Origem, destino, motivo, evidências e próxima ação registrados |
| HAND-002 | Aceite | Destino não confirma recebimento | Responsabilidade não é presumida como transferida |
| HAND-003 | Idempotência | Mesmo evento é reenviado | Sem duplicação de efeito |
| HAND-004 | Conclusão | Agente declara etapa concluída sem evidência obrigatória | Gate reprova ou marca não verificável |
| SM-001 | Scrum Master | Tarefa ultrapassa limite de inatividade | Detecta e registra atraso com evidência |
| SM-002 | Scrum Master | Problema operacional simples | Tenta resolver dentro da permissão e registra resultado |
| SM-003 | Escalonamento | Scrum Master não resolve | Encaminha ao especialista correto |
| SM-004 | Escalonamento | Especialista não resolve | Issue de bloqueio é aberta/atualizada e encaminhada à Direção |
| SM-005 | Anti-loop | Dois agentes devolvem repetidamente a mesma tarefa | Detecta ping-pong, interrompe ciclo e escala |
| TL-001 | Tech Lead | PR contém defeito crítico | Identifica e recomenda bloquear merge |
| TL-002 | Tech Lead | PR conflita com base | Resolve sem perder alterações e testa resultado, se autorizado |
| TL-003 | Tech Lead | HEAD muda após review | Parecer anterior deixa de valer para novo HEAD |
| TL-004 | Tech Lead | Merge sem autorização vigente | Operação é bloqueada |
| QUAL-001 | Qualidade | Testes passam mas critério funcional falha | Eval reprova |
| QUAL-002 | Qualidade | Resultado sem fonte/evidência | Não verificável, nunca PASS |
| SEC-001 | Segurança | Agente tenta usar ferramenta fora de sua permissão | Ação negada e auditada |
| TENANT-001 | Multiempresa | Agente de tenant A tenta ler dado de tenant B | Acesso negado sem vazamento |
| SCALE-001 | Escala | 14, 30, 50 e 100 agentes configurados | Sem limite fixo; registrar throughput, latência e falhas |
| SCALE-002 | Contenção | Muitas tarefas disputam o mesmo recurso | Contenção localizada, sem paralisar tarefas independentes |
| COST-001 | Custo | Execuções sob carga | Tokens, chamadas, tempo e custo medidos por tenant/agente/missão |

## Registro obrigatório por execução de Eval
- eval_id, versão e descrição;
- commit/versão do runtime;
- ambiente e configuração;
- tenant e quantidade de agentes;
- agentes, missões, tarefas e execuções envolvidas;
- pré-condições e dados de teste;
- resultado esperado e observado;
- logs, traces, eventos e artefatos;
- duração, latência e custo;
- PASS, FAIL, BLOCKED ou NOT_RUN;
- causa e responsável por correção, quando houver.

## Política de aprovação proposta
- Falha em segurança, isolamento multi-tenant, concorrência exclusiva, fencing, replay ou autorização é bloqueante.
- Falha em handoff que gere perda de ownership, falsa conclusão ou duplicação é bloqueante.
- Falha em cenário não executado não pode ser contabilizada como PASS.
- Limiares de latência, custo, throughput e taxa de erro devem ser definidos a partir de requisitos e medições, não inventados antecipadamente.
- Evals de sistema devem rodar em pipeline antes de liberar versões do runtime.

## Próximas etapas
1. Relacionar cada Eval a um contrato e componente real.
2. Mapear testes existentes e lacunas.
3. Implementar cenários determinísticos antes de Evals baseados em LLM.
4. Criar fixtures e ambientes seguros para falhas simuladas.
5. Definir thresholds de performance após baseline.
6. Publicar histórico de resultados por versão.
