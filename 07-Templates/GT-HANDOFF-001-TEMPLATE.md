---
tipo: template
id: GT-HANDOFF-001
versao: 0.4.0
status: proposta-para-revisao
---
# GT-HANDOFF-001 — Template de conclusão e transferência (PROPOSTA v0.4.0)

> Não homologado. Preencher com dados reais. Não declarar teste, entrega, recebimento, aceite ou autorização por presunção. Processo: [GT-HANDOFF-001](../03-Processos/Encaminhamento-de-Missoes-GT-HANDOFF-001.md). Auditoria de compatibilidade: [GT-HANDOFF-001-AUDIT-v0.4.0](../docs/GT-HANDOFF-001-AUDIT-v0.4.0.md).

## Como escolher a modalidade

- **CONCLUSÃO:** tarefa terminou (CONCLUÍDA, BLOQUEADA, INTERROMPIDA ou CANCELADA), sem mudança de ownership. Preencher a seção A. Não pedir ACEITO de transferência.
- **TRANSFERÊNCIA:** outro agente assumirá a continuidade. Preencher a seção B. O remetente mantém ownership até ACEITO explícito.
- Não emitir HANDOFF integral a cada checkpoint/commit/teste de uma tarefa ainda EM_ANDAMENTO.

---

## A. HANDOFF DE CONCLUSÃO — obrigatório ao encerrar tarefa

HANDOFF — CONCLUSÃO DE TAREFA

- Missão / tarefa / execução: [IDs ou N/A justificado]
- Origem / agente responsável: [identidade]
- Destinatário / owner da missão: [identidade ou N/A + motivo]
- Projeto / repositório / issue / PR: [referências ou N/A justificado]
- Commit / versão / artefato: [SHA/link/versão ou N/A]
- Data/hora/fuso: [ISO 8601]
- Objetivo e escopo delimitado: [descrição]
- Critérios de aceite da tarefa: [critérios definidos]
- Estado da tarefa: [CONCLUÍDA | BLOQUEADA | INTERROMPIDA | CANCELADA]
- Estado da missão: [estado real; não inferir encerramento]

### 1. Resultado
[O que foi efetivamente realizado, decisões e resultado observado.]

### 2. Não realizado
[Atividades não executadas, motivo e consequência. Se nada, declarar.]

### 3. Artefatos e alterações
[Arquivos, contratos, schemas, configurações, documentos, código, PRs, commits e links afetados. Declarar expressamente se nada foi alterado.]

### 4. Verificações e evidências
[Testes/verificações realizados, comando, ambiente, versão/commit, resultado e evidência.]
[Testes não realizados, motivo, consequência e responsável pela pendência.]

### 5. Riscos, pendências e dependências
[Itens, impacto, responsável e condição de desbloqueio/mitigação. N/A justificado quando aplicável.]

### 6. Próxima ação
- Responsável: [identidade ou N/A + motivo]
- Ação concreta: [ação ou N/A + motivo]
- Condição para avançar: [critério/evidência]
- Condição para encerrar a missão: [gates/decisões pendentes]

### 7. Ownership e aceite
- Ownership após este registro: **permanece com [responsável atual]**.
- Transferência de ownership: **NÃO OCORREU**.
- Aceite de transferência: **N/A — não houve transferência de ownership**.
- Registro canônico: [link ou PENDENTE + justificativa].

---

## B. HANDOFF DE TRANSFERÊNCIA — somente quando houver passagem real

HANDOFF — TRANSFERÊNCIA DE RESPONSABILIDADE

### 1. Identificação e rastreabilidade
- mission_id: [ID]
- task_id: [ID]
- execution_id: [ID]
- handoff_id: [ID único]
- event_id / versão: [ID / versão]
- Instante ISO 8601 com fuso: [timestamp]
- Origem / ator / agente: [identidade]
- Destinatário / competência: [identidade e papel]
- Autoridade / owner da missão: [identidade e fonte]
- Prioridade: [valor]
- Issue canônica / PR / commit / artefato: [links/SHA ou N/A justificado]

### 2. Objetivo, DoR e escopo
[Objetivo observável, critérios de aceite, insumos, dependências, limites e exclusões.]

### 3. Autoridade e permissões
[Ação permitida → autoridade aplicável → evidência → escopo/limite/validade. Registrar permissão efetiva; não inferir autorização.]

### 4. Estado e ownership antes/depois
- Estado da tarefa antes: [EM_ANDAMENTO | BLOQUEADA]
- Estado proposto após aceite: [EM_ANDAMENTO | BLOQUEADA]
- Natureza: **TRANSFERÊNCIA**
- Responsável atual (remetente): [identidade]
- Próximo responsável (destinatário): [identidade]
- Ownership antes do ACEITO: **permanece com o remetente**
- Ownership após ACEITO: **passa ao destinatário, somente no escopo aceito**

### 5. Trabalho, artefatos e evidências
[Resumo do realizado/não realizado; arquivos, contratos, schemas, configurações, commits, PRs, testes, resultados e links.]

### 6. Riscos, pendências, dependências e WIP
[Item, impacto, dono, próxima ação, condição de desbloqueio e condição de liberação de WIP.]

### 7. Transporte, recebimento e aceite — eventos distintos
| Marco | Estado | Evidência / instante / responsável |
|---|---|---|
| Preparado | [SIM/NÃO] | [prova] |
| Registrado | [SIM/NÃO/PENDENTE] | [link canônico] |
| Acionado/entregue | [COMPROVADO/PENDENTE/ERRO] | [canal, prova, instante] |
| Recebido | [CONFIRMADO/PENDENTE] | [confirmação verificável] |
| Aceite | [ACEITO/DEVOLVIDO/AGUARDANDO] | [declaração explícita, identidade, instante] |

- Em caso de DEVOLVIDO: [motivo, requisito faltante, dono e próxima ação].
- Em caso de erro/silêncio: [tentativas, impacto, responsável pela recuperação/escalonamento].
- Nunca inferir ACEITO por silêncio, comentário, label ou registro.

### 8. Próxima ação e condição de continuidade
- Ação esperada: [ação concreta]
- Critério de aceite: [critério verificável]
- Próximo passo/destino alternativo: [responsável e condição]
- Condição para liberar WIP: [entrega comprovada + ACEITO explícito + ausência de retrabalho ativo, conforme regra vigente]

### 9. Pareceres e segregação
[Author/executor/QA/validator/auditor/reviewer/approver, independência, participação prévia, habilitação e dispensas autorizadas. N/A justificado.]

---

## C. Checklist final

- [ ] Modalidade correta: conclusão ou transferência.
- [ ] Estado da tarefa, natureza do HANDOFF e ciclo de vida registrados separadamente.
- [ ] Identificadores, responsáveis, instante/fuso e links reais completos.
- [ ] Trabalho realizado/não realizado e artefatos afetados declarados.
- [ ] Verificações realizadas e não realizadas com evidências e motivos.
- [ ] Riscos, pendências, dependências e próxima ação com dono.
- [ ] Conclusão: ownership permanece; aceite de transferência = N/A.
- [ ] Transferência: remetente mantém ownership até ACEITO explícito.
- [ ] Nenhuma aprovação, autorização, integração ou conclusão de missão inferida.
- [ ] Registro canônico efetuado ou marcado PENDENTE com justificativa.
