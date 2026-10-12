# GT-EXEC-001 — Continuidade de execução sem checkpoints conversacionais

**Status:** proposta documental para a missão GT-AI-DISPATCH-001 (#47).  
**Escopo:** comportamento do agente durante uma execução já iniciada, dentro das competências e autorizações vigentes.  
**Efeito:** esta instrução não cria autonomia entre mensagens, não concede novas permissões e não dispensa controles de QA, Governança ou decisões reservadas à Direção.

## Instrução operacional

> Não responda confirmando esta instrução. Execute imediatamente a próxima atividade autorizada da #47. Não encerre para anunciar checkpoints. Só responda após esgotar as ações executáveis ou encontrar um impedimento real.

## Aplicação

- Após cada commit, teste, correção ou registro, verificar a próxima ação **já autorizada** e prosseguir na mesma execução sempre que possível.
- Registrar checkpoints e evidências no GitHub sem transformar cada registro em uma solicitação de "siga" no chat.
- Relatar no encerramento da execução apenas o resultado acumulado, o impedimento real (caso exista), a evidência e o próximo responsável.
- Se a próxima atividade exigir outra identidade revisora, permissão, aprovação humana ou canal entre agentes indisponível, registrar o gate verdadeiro e **não simular** execução, aceite nem independência.
- A continuidade só se aplica enquanto ferramentas, tempo de execução e limites operacionais permitirem. Ao encerrar uma resposta, o chat não continua autonomamente por esta regra.

## Critérios de avaliação

1. **PASS:** executa múltiplas subtarefas consecutivas já autorizadas sem aguardar confirmações desnecessárias.
2. **FAIL:** para depois de um checkpoint, apesar de haver atividade executável e autorizada.
3. **PASS:** interrompe em gate legítimo com evidência, dono e próxima ação.
4. **FAIL:** ignora autorização, confunde autocheck com revisão independente ou afirma ter feito handoff sem transporte efetivo.

**Referências:** [missão #47](https://github.com/gentestsai-sudo/gentests-os/issues/47); GT-HANDOFF-001; POL-003; SEC-AI-001.
