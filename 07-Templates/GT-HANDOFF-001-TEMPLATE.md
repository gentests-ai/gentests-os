---
tipo: template
id: GT-HANDOFF-001
versao: 0.1.0
status: proposta
missao: GT-GOV-CHANGE-001
---
# GT-HANDOFF-001 — Despacho / retorno (PROPOSTA)

> **Preenchimento obrigatório pelo remetente quando o protocolo for homologado.** Este modelo não concede autorização nem prova que o destinatário foi acionado.

**Missão:** [ID canônico]  
**Etapa/encaminhamento:** [ID único e versão]  
**Origem:** [agente remetente]  
**Destino proposto/confirmado:** [agente especializado]  
**Tipo:** [diagnóstico/execução/correção/QA/validação/revisão/deliberação]  
**Prioridade:** [prioridade registrada]  
**Estado da missão:** [estado verificado]  
**Estado da etapa:** [estado verificado]  
**Issue canônica:** [link]  
**PR/commit/artefato:** [links/versões ou não se aplica]  
**Data/hora do registro:** [data e fuso]

## 1. Objetivo e prontidão (DoR)
[Resultado esperado, requisitos de entrada, documentos canônicos e dependências. Se ainda não atendidos, marcar PENDENTE e encaminhar para refinamento.]

## 2. Escopo, autoridade e restrições
[Ações permitidas/proibidas, autorizações comprovadas e riscos. Não inferir permissões pela matriz de roteamento.]

## 3. Resultado real, evidências e DoD
[No despacho inicial: **PENDENTE DE EXECUÇÃO**. No retorno: entregas, links e versões; verificações executadas e resultado; verificações não executadas e motivo; achados, pendências e riscos.]

## 4. Estado e aceite
**Declaração do remetente:** [DESPACHADA / CONCLUÍDA COM EVIDÊNCIA / BLOQUEADA / DEVOLVIDA]  
**Acionamento do destinatário comprovado?:** [SIM com evidência / NÃO / PENDENTE]  
**Decisão do destinatário:** [ACEITO / DEVOLVIDO / AGUARDANDO]  
**Se devolvido:** [motivo, requisito faltante, dono da correção e próxima ação]  
**Atenção:** aceite de entrada não aprova o mérito.

## 5. Próximo encaminhamento
**Responsável pela próxima ação:** [papel/agente]  
**Próxima ação inequívoca:** [ação]  
**Destino alternativo, se autorizado:** [papel ou BLOQUEADO]  
**Ação requerida da Direção:** [NENHUMA ou decisão específica]  
**Condição para avançar:** [evidência/decisão verificável]  
**Retorno obrigatório:** [Orquestrador Central / outro conforme rota homologada]

## 6. Limites e conferência
- [ ] Não confundi registro em issue com acionamento efetivo de agente.
- [ ] Não confundi etapa concluída com missão encerrada.
- [ ] Não confundi revisão/QA/validação com autorização da Direção.
- [ ] Registrei origem, evidências e próximo destino sem pedir roteamento rotineiro à CEO.

**Referência:** [[03-Processos/Encaminhamento-de-Missoes-GT-HANDOFF-001]] · [Issue #55](https://github.com/gentestsai-sudo/gentests-os/issues/55)


## 7. FORMATO DE SAÍDA OBRIGATÓRIO — mensagem copiável (requisito de interface)

**Não basta preencher uma tabela-resumo, emitir um parecer ou apontar o próximo agente.** Ao concluir a etapa, o remetente deve entregar **a mensagem integral de encaminhamento, em um único bloco copiável**, direcionada à especialidade seguinte e pronta para colar em outra conversa de agente, sem recomposição manual pela CEO.

- Em **ChatGPT**, usar **bloco de escrita/mensagem** com ação de copiar disponível no cliente, contendo todo o despacho como Markdown. Se o cliente não oferecer bloco de escrita, usar **um único bloco de código Markdown copiável**, não uma tabela solta.
- Em **GitHub/Obsidian**, manter a mesma mensagem integral sob título `GT-HANDOFF-001 — Mensagem pronta para encaminhar` em um bloco Markdown ou texto integral fácil de selecionar/copiar; o GitHub não dispara automaticamente conversas.
- Cabeçalho deve explicitar **DESTINO: [nome do próximo agente]**, **AÇÃO: ENCAMINHAR ESTA MENSAGEM**, missão, etapa, origem, estado, issue, objetivo, escopo, restrições, entregáveis, critérios, evidências existentes, próxima ação e retorno exigido.
- **Handoff de prestação de contas** pode ser dirigido ao Orquestrador para aceite/triagem, mas **isso não é o despacho final**: o Orquestrador aceita/devolve e, quando houver próxima especialidade, emite **outra mensagem completa copiável** endereçada ao especialista. O Orquestrador **não deve despachar para si mesmo**.
- Na fase manual, a Direção **somente copia e cola** a mensagem; não escolhe destinatário, não completa contexto e não redige instruções.
- O despacho não deve afirmar que outro agente foi acionado; registrar separadamente preparado, registrado, transportado, aceito.
- Dados indisponíveis ficam marcados como **NÃO VERIFICADO/PENDENTE**, não inventados.
- **Critério de rejeição:** resposta somente em tabela de campos/resumo de status (como `Missão | Etapa | Remetente | Destinatário`) **sem a mensagem integral pronta para copiar** = **DEVOLVIDO PARA COMPLEMENTAÇÃO DE FORMATO**.

### Exemplo mínimo de apresentação exigida

**DESTINO: Agente de UX/UI — COPIAR A MENSAGEM COMPLETA ABAIXO**

```markdown
# GT-HANDOFF-001 — Despacho para UX/UI
**Missão:** GT-MISSION-CONTROL-001
**Etapa:** GT-MISSION-CONTROL-001-UX-01
**Origem:** Orquestrador Central — GenTests.ai
**Destino:** Agente de UX/UI
**Estado:** Aguardando aceite do destinatário
**Referências:** [issue e documento de especificação efetivamente publicados]
## 1. Objetivo
Preparar proposta de interface com base na especificação funcional verificada.
## 2. Contexto / DoR
[versão do documento, critérios e dependências reais]
## 3. Escopo autorizado
[atividades permitidas, limites, sem deploy/merge]
## 4. Entregáveis e aceite
[telas/jornadas, evidências e critérios observáveis]
## 5. Próximo encaminhamento
[próximo responsável e ação após esta etapa; retorno pelo GT-HANDOFF-001]
```

**O exemplo é ilustrativo** e precisa ser preenchido com evidências reais antes de uso.
