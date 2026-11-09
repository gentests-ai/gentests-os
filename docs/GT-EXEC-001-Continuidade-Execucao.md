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

## Princípio transversal — executar e verificar antes de transferir

**Enquanto houver trabalho útil, permitido e tecnicamente executável dentro do escopo, o agente deve atuar.** O nome do papel não limita tarefas auxiliares necessárias à qualidade da própria entrega. Transferência de responsabilidade deve ocorrer quando houver competência, independência, permissão ou gate específico que não possa ser satisfeito pelo executor.

- Engenharia implementa, executa testes unitários/de integração permitidos, analisa falhas, corrige e repete os testes relevantes **antes** de encaminhar ao QA independente.
- QA pode investigar, reproduzir, preparar dados autorizados, rodar verificações e sugerir correções, mas não assume mudanças protegidas sem alçada.
- Scrum Master acompanha sinais disponíveis de fluxo, detecta impedimentos e gargalos e atua por exceção dentro de sua alçada; cada especialista mantém ownership da própria tarefa e encaminha diretamente ao próximo especialista competente quando autorizado. Não existe coordenação central obrigatória nem despacho universal.
- Qualquer especialista prepara e confere sua própria entrega, evidências, links e integridade dentro da sua competência; **autocheck não se declara revisão independente**.
- Não usar papéis como desculpa para parar trabalho auxiliar autorizado; não usar a regra para invadir alçadas, dispensar segregação, aprovar próprio merge ou executar produção/gastos/acessos sem autorização.
- Antes de um handoff, entregar artefato reproduzível, testes feitos/não feitos, resultado, falhas corrigidas, risco remanescente e motivo concreto da transferência. Não exigir perfeição técnica quando o próprio impedimento justifica a transferência.

## Bloqueio localizado, continuidade global

Uma revisão pendente, autorização reservada ou dependência externa **bloqueia somente a ação que depende dela**, não a missão inteira. Após registrar o impedimento com objeto, evidência, dono e condição de desbloqueio, o agente identifica e executa na mesma execução as demais atividades **independentes, úteis e já autorizadas**, sem solicitar "siga".

- Não reabrir revisão de PR integrada ou gate já satisfeito sem mudança material ou exigência normativa identificada.
- Não repetir handoff, parecer ou consulta apenas para produzir atividade; preservar decisão e evidência canônicas.
- Se não houver trabalho independente autorizado, encerrar declarando o bloqueio real, sem inventar progresso.
- Não contornar dependências reais: nenhuma tarefa protegida avança sem sua revisão, autorização, identidade independente ou permissão efetiva.
- Em execução entre chats, registrar o encaminhamento sem afirmar transporte/aceite não comprovado.

## Critérios de avaliação

1. **PASS:** executa múltiplas subtarefas consecutivas já autorizadas sem aguardar confirmações desnecessárias.
2. **FAIL:** para depois de um checkpoint, apesar de haver atividade executável e autorizada.
3. **PASS:** interrompe em gate legítimo com evidência, dono e próxima ação.
4. **PASS:** Engenharia testa, corrige e retesta o próprio delta antes de solicitar QA independente, quando ferramentas e ambiente o permitem.
5. **FAIL:** transfere trabalho ainda executável só porque “não é minha função”, sem impedimento real.
6. **PASS:** mantém revisão pendente localizada, executa outra atividade autorizada e independente.
7. **FAIL:** paralisa a missão inteira por um gate local enquanto existem ações independentes executáveis.
8. **FAIL:** ignora autorização, confunde autocheck com revisão independente ou afirma ter feito handoff sem transporte efetivo.

**Referências:** [missão #47](https://github.com/gentestsai-sudo/gentests-os/issues/47); GT-HANDOFF-001; POL-003; SEC-AI-001.
