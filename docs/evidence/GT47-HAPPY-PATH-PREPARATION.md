# GTS-47: preparação do caminho feliz — 13/10/2026

A rodada 03 permanece completed para a troca de pareceres e
adjustments_required para a demanda. Ambos os pareceres, as reservas e as
inconformidades são preservados; não se declara essa demanda finalizada.

A tarefa anterior ainda solicitava aprovação humana, contrariando a diretriz
posterior. A próxima tarefa é um checklist documental com três critérios
objetivos: persistência JSON/CAS e leitura, identidade reservada antes da chamada,
e recuperação sem limpar claims ou reenviar efeitos incertos. Não pede
implementação, ferramentas, merge, deploy ou gasto adicional. QA mantém liberdade
para needs_changes; finalização real só será declarada com seu parecer favorável.

O workflow 12 passa a permitir nova rodada após troca concluída e validada,
além de tentativa bloqueada. Exige pausa, ID esperado e commit diferente;
arquiva o registro integral antes de substituir a fila por CAS. Recusa fila
ativa, parecer corrompido, identidade já reservada e arquivo divergente.
Não reembolsa ou apaga reservas e não executa inferência.

Após merge, preparar pilot-round-04 com expected_id
3f1c75201f7a2768d008fd665317020eb7ea19555258790dc9be5a6f138fad69,
correspondente à rodada 03 observada. Verificar arquivo e orçamento intactos
antes de habilitar o workflow 09. Apenas uma Engenharia e uma QA após pelo
menos 300 segundos; pausar ao concluir ou falhar. Não reenviar chamadas incertas.
Continuam Actions USD 0 / Stop usage Yes, Groq Free e proibição de OpenAI pago.

Prova offline: caminho sintético completa duas chamadas, impede avanço de QA
antes do intervalo e não repete submissão após conclusão. A tarefa cabe no
limite de contexto mesmo com parecer de Engenharia nos limites máximos.
Essa prova sintética não é validação real do Groq. Nenhuma inferência real ou
escrita no estado de produção foi feita durante a preparação.
