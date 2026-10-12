---
tipo: politica
id: QG-001
versao: 0.2.0
status: proposta
aprovador: direcao
---
# QG-001 — Quality Gate Adaptativo

## Objetivo
Todo artefato corporativo deve passar por validação proporcional ao contexto e ao risco **antes de ser declarado concluído ou enviado**. Abrange código, documentos, e-mails, artes, relatórios, políticas e entregas de agentes.

## Núcleo obrigatório — todos os níveis
1. Alinhamento à missão, à visão, aos valores e às políticas **aprovadas**.
2. Veracidade e rastreabilidade: fatos, métricas e afirmações devem ser sustentados por fontes verificáveis.
3. Segurança, privacidade, permissões e confidencialidade.
4. Objetivo e critério de aceite definidos; responsável e versão identificados.

## Classificação de risco
- **QG-L / Leve:** rascunho ou nota interna sem dados sensíveis, baixo impacto, totalmente reversível.
- **QG-M / Padrão:** comunicação externa, apresentação, código não crítico, relatório técnico ou impacto moderado.
- **QG-H / Crítico:** contrato, política institucional, dados sensíveis para público externo, alto impacto, ação de difícil reversão, produção, cobrança ou decisão financeira relevante.

**Regra de prevalência:** aplicar sempre o nível mais alto acionado por qualquer critério. O agente não pode rebaixar unilateralmente o risco.

## Controles adicionais
- **QG-L:** verificar núcleo obrigatório e consistência básica.
- **QG-M:** adicionar checklist do tipo de artefato, revisão contextual e evidências referenciadas.
- **QG-H:** adicionar revisão independente, registro formal da decisão e autorização humana conforme matriz de permissões.

## Anexo candidato B2 — aplicação condicionada à homologação

> **PROPOSTA, SEM VIGÊNCIA.** Até decisão normativa expressa da Direção, prevalece a regra anterior: **QG-H exige revisão independente efetiva**. Este anexo não libera implementações, merges ou atos bloqueados. A classificação é do **artefato e da operação/efeito**, prevalecendo o risco mais alto; autor não rebaixa unilateralmente o nível.

### Categorias objetivas e segregação

| Categoria candidata | Critério objetivo | Verificações propostas | Limite |
|---|---|---|---|
| L0 — editorial reversível | Nota/rascunho interno, sem dados sensíveis, efeito externo, autoridade ou alteração de controle | Núcleo obrigatório, autocheck rastreável, versão/autor e diff | Ausência de fonte ou escopo autorizado = não verificável |
| M1 — operacional reversível | Documento não normativo ou código **não crítico**, sem produção, segredo, ACL ou cobrança, com rollback demonstrável | Núcleo, autocheck, testes determinísticos quando aplicáveis, revisão contextual competente e evidência ligada ao HEAD | Mudança material de comportamento ou ausência de revisão exigida bloqueia avanço |
| H1 — crítico reservado | Política, contrato, mudança de autoridade/gate, ACL, segredo, dados sensíveis, produção, envio/publicação sensível, pagamento, ação irreversível | Núcleo, testes/QA/VAL/AUD específicos, **revisão humana independente quando exigida**, decisão e autorização humana pertinentes | Ausência de revisor obrigatório: BLOQUEADO — REVISOR INDISPONÍVEL; proibição X nunca é compensada |
| H2 — preparação técnica sem efeito protegido | Estudo, simulação isolada, arquitetura e testes preparatórios de artefato futuramente crítico; **não é liberação do ato H1** | Núcleo, autocheck e controles técnicos apropriados à preparação; risco e bloqueio da operação final explicitados | Sem merge/deploy, alteração de ACL/segredo ou execução crítica por equivalência |

**H2 não é reclassificação de QG-H para QG-M:** a operação protegida continua QG-H/H1. Os critérios de possível revisão de exigibilidade são propostas para decisão futura, não exceções vigentes. Casos ambíguos, novos tipos, exposição pública, dados sensíveis ou irreversibilidade são H1 até classificação competente. Revisor Independente Modelo A exige elegibilidade por identidade humana real e ausência de autoria/execução/conflito; outra conversa ou função de IA sob a mesma identidade não satisfaz independência humana.

Autocheck do autor, verificação determinística, QA funcional, Validação de critérios, Auditoria de controles, revisão independente humana e autorização da Direção são eventos **distintos**, com ator, escopo, resultado, evidência e data. Não registrar uma categoria como substituta da outra.

### Controles compensatórios candidatos e eficácia

| Risco / modalidade | Compensação proposta para avaliação | Evidência mínima de eficácia | Risco residual preliminar e decisão |
|---|---|---|---|
| Erro técnico em M1/H2 | Testes automatizados determinísticos, QA por escopo e diffs ligados ao HEAD | Relatório de execução, saída/exit code, cobertura relevante, SHA e cenário negativo | Médio sem medição; falha = bloqueio do delta afetado |
| Autoaprovação ou parecer fictício | Atores e funções separados, declaração de conflito e checagem de identidade | Identidade real, autoria, executor, revisor e decisões verificáveis | Alto se independência humana obrigatória faltar; **não compensável automaticamente** |
| Alteração não autorizada / desvio de escopo | Escopo mínimo, diff/ACL, proteção de branch, autorização por objeto | Registro de permissão efetiva e aprovação humana específica, logs de alteração | Alto em H1; ausência de prova bloqueia operação |
| Evidência fabricada / alteração pós-check | Proveniência da fonte, logs verificáveis, resultados com SHA, revalidação só de delta material | Link à execução real e comparação HEAD testado/revisado | Médio até prova; não verificável ≠ conforme |
| Vazamento / prompt injection | Redação de segredos, isolamento, validação de entrada e teste negativo | Evidência de ambiente, controles de acesso e resultado do teste | Alto quando acesso/dado sensível incerto; bloquear ação externa |
| Falha de handoff / perda de contexto | Issue canônica com evento, transporte, aceite, owner e síntese incremental ORQ | IDs, links, estados separados e prova de entrega real | Médio sem integração real; comentário não notifica chat |

**Eficácia NÃO DEMONSTRADA** por este documento: cada compensação requer desenho de teste, ambiente, owner distinto quando requerido, entradas positivas e negativas, critérios de aprovação, execução observada, evidência e rechecagem após delta material. Redução de exigibilidade só pode ser avaliada mediante análise documentada, revisão competente e decisão/homologação da Direção com versão/vigência prospectiva. Não há dispensa automática, retroativa, por falta de revisor ou por decisão unilateral de um agente.

### Falha segura e gates não compensáveis automaticamente

Proibido compensar por autocheck: aprovação humana reservada, proibições X/ND, segregação de identidade realmente exigida, proteção de segredos, permissão técnica efetiva, evidência de execução real e revisão independente **enquanto exigida** pela norma aplicável. Sem revisor elegível, identificar objeto/HEAD, ação bloqueada, gate, owner, risco residual, próximo decisor e trabalho preparatório permitido. Somente a ação dependente permanece bloqueada; o restante autorizado pode prosseguir.

## Resultado
- **Conforme:** todos os itens aplicáveis verificados com evidências.
- **Correção necessária:** falha corrigível; retorno ao executor e nova validação.
- **Bloqueado:** violação de segurança, política, ausência de aprovação obrigatória ou falha crítica.
- **Não verificável:** evidência insuficiente; não interpretar como conforme.

## Segurança operacional
O Validador não altera o artefato original, não o publica, não libera pagamentos e não aprova o próprio trabalho. Marcação de caixas não substitui comprovação ou aprovação humana. Nenhum agente consegue impor estas regras tecnicamente apenas com Markdown: implantação requer permissões e fluxos reais.

## Próximos documentos
- [[00-Constituicao/Quality-Gates/QG-CORE-Obrigatorio]]
- [[02-Agentes/Validador/Contrato-Agente-Validador]]
- [[07-Templates/Relatorio-Validacao-TEMPLATE]]

## Aprovação
Este texto é uma proposta. Registrar aprovação da direção com data, versão e decisão.
