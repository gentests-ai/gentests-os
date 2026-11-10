# GT-EXEC-001 — Continuidade de execução sem checkpoints conversacionais

**Status:** proposta documental para a missão GT-AI-DISPATCH-001 (#47).  
**Escopo:** comportamento do agente durante uma execução já iniciada, dentro das competências e autorizações vigentes.  
**Efeito:** esta instrução não cria autonomia entre mensagens, não concede novas permissões e não dispensa controles de QA, Governança ou decisões reservadas à Direção.

## Instrução operacional

> Não responda confirmando esta instrução. Execute imediatamente a próxima atividade autorizada da #47. Não encerre para anunciar checkpoints. Só responda após esgotar as ações executáveis ou encontrar um impedimento real.

## Aplicação

- Após cada commit, teste, correção ou registro, verificar a próxima ação **já autorizada** e prosseguir na mesma execução sempre que possível.
- Registrar checkpoints e evidências no GitHub sem transformar cada registro em uma solicitação de "siga" no chat.
- No encerramento de cada tarefa delimitada, emitir o HANDOFF integral do GT-HANDOFF-001 v0.3.0: resultado real, artefatos/arquivos/contratos/commits/PRs afetados, testes feitos e não feitos, evidências, riscos, estado e próxima ação. Aplicar também a BLOCKED/interrompida/cancelada. Não emitir a cada checkpoint enquanto a tarefa continua; sem transferência, registrar aceite como N/A e manter o ownership atual.
- Se a próxima atividade exigir outra identidade revisora, permissão, aprovação humana ou canal entre agentes indisponível, registrar o gate verdadeiro e **não simular** execução, aceite nem independência.
- A continuidade só se aplica enquanto ferramentas, tempo de execução e limites operacionais permitirem. Ao encerrar uma resposta, o chat não continua autonomamente por esta regra.

## Princípio transversal — executar e verificar antes de transferir

**Encerramento obrigatório:** ao terminar uma tarefa delimitada, qualquer agente deve emitir o registro integral de conclusão/transferência do GT-HANDOFF-001. O registro é obrigatório mesmo sem troca de agente; não cria checkpoint intermediário nem exige aceite quando não há transferência.

**Enquanto houver trabalho útil, permitido e tecnicamente executável dentro do escopo, o agente deve atuar.** O nome do papel não limita tarefas auxiliares necessárias à qualidade da própria entrega. Transferência de responsabilidade deve ocorrer quando houver competência, independência, permissão ou gate específico que não possa ser satisfeito pelo executor.

- Engenharia implementa, executa testes unitários/de integração permitidos, analisa falhas, corrige e repete os testes relevantes **antes** de encaminhar ao QA independente.
- QA pode investigar, reproduzir, preparar dados autorizados, rodar verificações e sugerir correções, mas não assume mudanças protegidas sem alçada.
- O runtime (mecanismo de execução, não um agente coordenador) mantém estado, encaminhamento, permissões e rastreabilidade. Agentes especialistas fazem handoffs horizontais nas rotas autorizadas; o Scrum Master atua por exceção em impedimentos e saúde operacional, sem intermediar o fluxo normal.
- Qualquer especialista prepara e confere sua própria entrega, evidências, links e integridade dentro da sua competência; **autocheck não se declara revisão independente**.
- Não usar papéis como desculpa para parar trabalho auxiliar autorizado; não usar a regra para invadir alçadas, dispensar segregação, aprovar próprio merge ou executar produção/gastos/acessos sem autorização.
- Antes de um handoff, entregar artefato reproduzível, testes feitos/não feitos, resultado, falhas corrigidas, risco remanescente e motivo concreto da transferência. Não exigir perfeição técnica quando o próprio impedimento justifica a transferência.

## Execução eficiente da demanda — diretriz registrada em 12/10/2026

**Origem:** orientação explícita da usuária na continuidade do piloto GTS-47.
Registrar esta regra no processo consultado pelos agentes; o documento não
comprova que o motor já implementa todas as transições descritas abaixo.

> O agente mantém a demanda enquanto puder avançá-la com competência e dentro
> das permissões e do escopo autorizado. Executa, faz o autocheck e continua
> até esgotar o trabalho útil ao seu alcance. Transfere somente por necessidade
> concreta de outra competência, permissão ou revisão independente.

- **Continuidade de responsabilidade:** mudança de etapa ou atividade auxiliar
  não exige trocar de agente. Se o executor consegue realizar a próxima atividade
  autorizada, continua; não cria um handoff apenas para cumprir uma sequência de
  cargos. Papéis orientam responsabilidade e alçada, sem impor passagem pelos
  14 agentes em toda demanda. O objetivo dos 14 papéis é especialização de alto
  nível: tarefas auxiliares ao alcance do executor não substituem a competência
  especializada necessária, e ele transfere quando a entrega exigir essa
  profundidade técnica. Recebimento, aceite e transferência reais continuam
  exigindo registro e transporte efetivo.
- **Revisão mínima obrigatória:** toda demanda passa ao menos uma vez por outro
  agente com perfil de QA/Revisor, distinto do autor e sem participação conflitante
  na entrega examinada. A revisão cobre a versão final e seus critérios de aceite.
  Autocheck não atende esse requisito; ter outro nome de papel também não comprova
  independência. O revisor de entrega é QA/Revisor, não Auditoria Independente:
  Auditoria avalia conformidade dos processos e controles, aponta não conformidades
  e verifica correções posteriormente, sem executar a correção nem alterar o objeto
  auditado. Gates especializados adicionais continuam conforme risco e escopo.
- **Mudança após revisão:** registrar a versão/commit revisado. Alteração posterior
  exige reavaliar o delta e seus impactos antes de concluir, reutilizando evidências
  anteriores ainda válidas. Não repetir revisão completa sem motivo concreto.
- **Ajustes:** devolver ao executor apontamentos objetivos ligados aos critérios;
  ele corrige e continua dentro da sua alçada. Não finalizar demanda que ainda
  precisa de ajustes. O retorno automático permanece evolução posterior ao caminho
  feliz; não presumir que já foi implementado.
- **Finalização:** com entrega final, critérios atendidos e revisão independente
  favorável vinculada à mesma versão, o motor finaliza a demanda automaticamente,
  sem aprovação humana obrigatória no fluxo normal autorizado. Registrar resultado,
  responsável e evidências. Essa conclusão não concede permissões para merge,
  deploy, execução técnica, comunicação externa ou gastos.

### Economia de tokens sem interromper trabalho útil

- Código do motor controla estados, roteamento determinístico, intervalos,
  orçamento e finalização; chamar IA para interpretação, criação ou avaliação
  necessária, não para consultar ou retranscrever estados.
- Enviar contexto suficiente e mínimo: demanda, critérios, versão, delta e
  evidências relevantes. Consultar histórico adicional quando houver necessidade,
  sem reenviar todo o repositório ou toda a conversa a cada etapa.
- Reutilizar artefatos e pareceres com fonte, versão e limites. Sem mudança de
  entrada, falha ou evidência nova, não repetir a mesma análise.
- Usar saída estruturada e curta, suficiente para o próximo passo. Selecionar
  somente os agentes necessários, preservando a revisão independente mínima.
- Definir limites de tokens por etapa/demanda/dia e de ciclos de ajustes conforme
  o fluxo. Ao atingir limite, registrar espera/bloqueio e próxima ação; não gerar
  conversa indefinida ou declarar conclusão para economizar tokens.
- Reservar quota antes da chamada; manter claims e bloquear reenvio de resultado
  incerto. Exibir consumo real separado de reservas. Os 1.024 tokens da rodada 03
  são uma observação inicial, não uma média nem um orçamento universal.

### Verificação prática

- **PASS:** um executor resolve subtarefas autorizadas e faz autocheck antes de
  transferir, com motivo concreto para cada handoff.
- **PASS:** outro QA/Revisor examina a entrega final; o motor conclui com evidência
  favorável e critérios atendidos, sem checkpoint humano rotineiro.
- **FAIL:** troca de agente por rótulo, repetição de contexto/análise sem motivo,
  autoaprovação ou conclusão apoiada somente em revisão de versão ultrapassada.
- **FAIL:** demanda com ajustes marcada como finalizada, orçamento excedido ou
  chamada incerta reenviada para tentar obter um resultado.

## Bloqueio localizado, continuidade global

Uma revisão pendente, autorização reservada ou dependência externa **bloqueia somente a ação que depende dela**, não a missão inteira. Depois de registrar o impedimento com objeto, evidência, responsável e condição de desbloqueio, o agente identifica e executa na mesma execução as demais atividades **independentes, úteis e já autorizadas**, sem solicitar confirmação conversacional desnecessária.

- Não reabrir revisão de PR integrada ou gate já satisfeito sem mudança material ou exigência normativa identificada.
- Não repetir handoff, parecer ou consulta apenas para produzir atividade; preservar decisão e evidência canônicas.
- Se não houver trabalho independente autorizado, encerrar declarando o bloqueio real, sem inventar progresso.
- Não contornar dependências reais: nenhuma tarefa protegida avança sem sua revisão, autorização, identidade independente ou permissão efetiva.
- Em execução entre chats, registrar o encaminhamento sem afirmar transporte ou aceite não comprovado.
- A identidade compartilhada da conta GitHub não elimina a necessidade de distinguir agentes internamente; também não prova, por si só, independência entre autor e revisor.

## Critérios de avaliação da continuidade

1. **PASS:** executa múltiplas subtarefas consecutivas já autorizadas sem aguardar confirmações desnecessárias.
2. **FAIL:** para depois de um checkpoint, apesar de haver atividade executável e autorizada.
3. **PASS:** interrompe em gate legítimo com evidência, dono e próxima ação.
4. **PASS:** Engenharia testa, corrige e retesta o próprio delta antes de solicitar QA independente, quando ferramentas e ambiente o permitem.
5. **FAIL:** transfere trabalho ainda executável só porque “não é minha função”, sem impedimento real.
6. **PASS:** mantém revisão pendente localizada, executa outra atividade autorizada e independente.
7. **FAIL:** paralisa a missão inteira por um gate local enquanto existem ações independentes executáveis.
8. **FAIL:** ignora autorização, confunde autocheck com revisão independente ou afirma ter feito handoff sem transporte efetivo.

**Referências:** [missão #47](https://github.com/gentestsai-sudo/gentests-os/issues/47); GT-HANDOFF-001; POL-003; SEC-AI-001.
