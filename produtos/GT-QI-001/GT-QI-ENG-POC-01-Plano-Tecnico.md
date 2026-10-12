# GT-HANDOFF-001 — Plano Técnico da POC Quality Intelligence

**Destino:** 👑 Direção GenTests.ai. **Origem:** 💻 Engenharia — AGT-ENG.
**Iniciativa:** GenTests Quality Intelligence. **Handoff:** GT-QI-ENG-POC-01.
**Evento/versão:** GT-QI-ENG-POC-01-RETURN-001 / 0.1.0. **Data:** 12/10/2026, America/Sao_Paulo; horário exato não aferido.
**Entrada:** ACEITO nesta conversa. **Estado:** plano documental concluído; implementação e execução não autorizadas. **Prioridade:** estratégica, preservando atividades operacionais prioritárias.
**Responsável atual:** Engenharia até entrega; próximo responsável pela decisão: Direção. Rota direta determinada pela Direção, sem confirmação do Orquestrador. Alternativo não designado.

## 1. Recomendação e fontes

Preparar futuramente uma aplicação Python de linha de comando, em ambiente local isolado, com cinco cards sintéticos, dois modos de análise e avaliação humana cega. O candidato principal permanece Qwen3-30B-A3B-FP8 via REST do Cloudflare Workers AI. Não exige criar um Worker, banco, Durable Object, fila, Site ou workflow. Modelo é candidato, não escolha operacional aprovada.

Hipótese: a abordagem especializada produz achados mais pertinentes, fundamentados e acionáveis do que um prompt genérico, sem aumentar omissões críticas ou regras inventadas. Não há evidência atual de superioridade.

Fontes efetivamente consultadas:
- Discovery v0.2: `Texto colado(5).txt`, libfile_e8f96c8f38588191a1f68bfb490cfe12; parecer QA: `Texto colado(4).txt`, libfile_97f8add3493c819187b7fcaae7d904d9. Conteúdos integrais lidos. O arquivo v0.2 ainda diz aprovação pendente; a autorização conceitual posterior é a mensagem atual da Direção, sem editar a fonte.
- GT-QI-ENG-VIAB-01: recuperado como síntese de conversa anterior, não como documento integral ou registro GitHub verificado. Preservados resultado VIÁVEL COM CONDIÇÕES, Python + validações + LLM intercambiável + JSON/Markdown, alternativas Cloudflare/Gemini/Ollama e ausência de custo/privacidade operacional comprovados. Estimativa anterior 8–13 dias úteis referia-se ao recorte anterior; abaixo há estimativa específica menor para esta POC. Limitação de proveniência declarada, sem novo estudo amplo.
- Repositório oficial: AGT-ENG v0.1.2, POL-003 v1.2.1, SEC-AI-001 v0.1.0, QG-001 v0.1.0, PRC-ENG-001 v0.1.2, POL-002 e template GT-HANDOFF-001 v0.2.0, consultados na main; são propostas, não novas permissões.
- Documentação pública dos provedores, consultada em 12/10/2026, listada na seção 12.

Nenhuma issue canônica desta iniciativa foi confirmada. Não registrar em #47: é missão independente. Não houve escrita GitHub, branch, commit ou PR nesta etapa.

## 2. Arquitetura mínima e contratos

Fluxo futuro: **card sintético → validação de entrada → montagem do prompt → adaptador LLM → validação de saída → JSON/Markdown → revisão e comparação humana**. Um processo local, chamadas sequenciais, sem ferramentas externas disponíveis ao modelo. O gabarito pertence somente ao avaliador e nunca entra no prompt.

Entrada: versão do contrato, ID SYN-QI-01…05, título, descrição literal, critérios/contexto/dependências fornecidos e lista de controles obrigatórios explicitamente conhecidos. Trechos recebem IDs estáveis e offsets calculados sobre o texto original. Campos desconhecidos não são preenchidos por inferência. Os cinco cards oficiais permanecem literais; não adicionar requisitos para facilitar aprovação.

Saída: versão, card_id, estado, resumo, testabilidade e justificativa; achados com ID, classe, referência textual ou ausência explícita, justificativa, consequência, impacto, probabilidade qualitativa ou não estimável, confiança e limitação; até três prioridades principais; obrigatórios em lista separada; cenários fundamentados e condicionais, perguntas, riscos residuais, decisões humanas ainda pendentes e testes `não executados`.

Classes fechadas: fato extraído, inconsistência demonstrável, hipótese de risco, pergunta pendente. Testabilidade: testável, parcialmente testável ou dependente de esclarecimento. Risco alto não equivale automaticamente a card não testável. Contradição central impede resultado esperado definitivo para essa parte, preservando partes independentes.

Validação determinística futura: IDs/versões/tipos/enums/campos obrigatórios, limites de tamanho, referências existentes e citações literais, prioridades até três, preservação dos IDs obrigatórios conhecidos, ausência de aprovação/execução automática. Saída inválida é registrada como falha, sem conserto semântico silencioso ou nova inferência automática. Referência correta não comprova raciocínio correto: pertinência, contradições, omissões e invenções são julgadas pelo avaliador.

Estado válido de relatório: análise pronta para revisão; erro de schema, truncamento, timeout ou fornecedor indisponível gera análise não concluída. Nenhum desses estados aprova funcionalidade.

## 3. Arquivos previstos — não criados

| Arquivo previsto | Responsabilidade |
|---|---|
| `README.md` e `requirements.lock` | Procedimento futuro, versões fixadas e hashes das dependências |
| `config/poc.json` | Modelo/modos, limites, rede desabilitada por padrão, teto de chamadas; sem segredos |
| `contracts/input.schema.json`, `output.schema.json` | Contratos fechados de entrada e saída |
| `fixtures/cards.json` | Cinco textos oficiais e respectivos IDs, sem gabaritos |
| `evaluation/reference.md` | Gabaritos QA literais, leitura exclusiva do avaliador |
| `evaluation/rubric.csv` | Critérios atômicos derivados dos gabaritos, pontuação, severidade e referência; não substitui o texto QA |
| `prompts/generic.md`, `specialized.md` | Baseline congelada e abordagem especializada, sem exemplos dos cinco casos |
| `qi/cli.py`, `pipeline.py` | Seleção de caso/modo, sequência e controle de estado |
| `qi/model_adapter.py` | REST Cloudflare; contingência selecionada explicitamente, sem troca automática |
| `qi/validation.py`, `reporting.py` | Checagem de contratos/referências e exportação derivada da mesma saída |
| `tests/test_contracts.py` | Verificações offline com respostas simuladas, sem avaliar inteligência |
| `runs/` e `evaluation/review.csv` | Saídas brutas/validadas, manifesto, decisão humana e pontuação; gerados somente na execução autorizada |

Sem framework de agentes, RAG, fine-tuning ou base vetorial. A especialização inicial é instrução de QA + contrato + controles; não se apresenta como modelo proprietário treinado.

## 4. Ambiente e procedimento futuro

Python 3.12 em venv local com versões/hashes fixados na implementação futura; registrar SO, runtime, dependências, modelo/ID, parâmetros, prompts e seus hashes, entrada e hash, data/hora, limites e resposta bruta. Scripts reproduzem procedimento; fornecedor pode atualizar pesos, portanto igualdade bit a bit da inferência não é garantida.

Primeiro, após autorização de implementação offline: materializar os cinco cards/gabaritos, conferir igualdade com fontes, montar contratos e prompts, testar serialização, falhas e relatórios com mocks. Rede bloqueada; nenhum teste offline pode ser chamado de comprovação de raciocínio de IA.

Depois, somente com autorização específica de inferência e condições verificadas: conferir plano gratuito/quota/privacidade; fixar prompts antes de gerar saídas; executar cada card isolado e sem histórico; salvar saídas; validar; anonimizar identidade do modo para o avaliador; pontuar; revelar os modos somente ao finalizar. Sem ajuste de prompt após observar respostas dos cinco cards na rodada comparativa.

Execução inicial: cinco cards × dois modos = **10 chamadas**. Se orçamento e autorização comportarem, repetir o mesmo lote uma vez, sem alteração, para explorar variabilidade: teto **20 chamadas totais**, contando falhas. Repetição não cria novos casos nem aumenta tamanho efetivo da amostra. Não há retries automáticos. Nova rodada após modificar prompts é outro experimento e requer autorização correspondente.

## 5. Modelo e alternativas

| Candidato | Uso no plano | Condições e limitações |
|---|---|---|
| Qwen3 `@cf/qwen/qwen3-30b-a3b-fp8` / Workers AI | Principal; mesmo modelo em ambos os modos | Catálogo/tabela pública não comprovam disponibilidade na conta. Exige plano Free elegível, quota e autorização futura de credencial/inferência |
| Gemini API Free | Contingência principal se Cloudflare não elegível | Confirmar modelo Flash elegível no Free vigente e seus limites na conta. Não ativar billing. Conteúdo gratuito pode ser usado para melhoria do provedor; somente sintéticos e aceite dessa condição |
| Qwen3 local via Ollama | Alternativa de privacidade se hardware existente permitir | API local compatível com adaptador; modelo/digest/licença/hardware ainda não confirmados. Sem aluguel de GPU ou download agora. Energia e conexão não tornam custo global zero automaticamente |

Ollama é runtime, não modelo. Usar um Qwen3 menor local altera capacidade e exige comparar os dois modos novamente nesse mesmo modelo. Troca de provedor interrompe lote; não misturar pares de fornecedores e atribuir diferença à especialização.

Sem tools, navegação, grounding, código, integrações ou memória. Temperatura mínima suportada, limite de saída e configuração de thinking idênticos nos dois modos; registrar comportamento efetivo. Não exportar cadeia interna de raciocínio: exigir justificativas curtas baseadas no card. Limites para tokens de raciocínio precisam estar esclarecidos antes de estimar teto.

## 6. Custo incremental R$ 0 — condição ainda não comprovada

A documentação Cloudflare declara 10.000 Neurons/dia no Workers Free; excesso falha e requer upgrade para continuar. Reset às 00:00 UTC. Paid permite cobrança além da franquia. Qwen3 candidato aparece com 4.625 Neurons por milhão de tokens de entrada e 30.475 por milhão de saída. Não aparece na lista paga obrigatória consultada; isso não prova elegibilidade autenticada da conta. [C1]

Estimativa de planejamento, não consumo medido: máximo 3.000 tokens de entrada e 2.000 tokens totais de saída por chamada, incluindo raciocínio se cobrado assim. Por chamada: (3.000×4.625 + 2.000×30.475)/1.000.000 = 74,825 Neurons. Dez chamadas ≈748,25; vinte ≈1.496,50. Reservar 2.000 Neurons para o lote. Se tokens ocultos não forem limitáveis/contabilizáveis, essa estimativa não é teto confiável; revisar condição antes de chamar. [C1, cálculo próprio]

Procedimento de confirmação futura, sem recursos nesta etapa:
1. Direção apresenta evidência sanitizada do plano Workers Free, conta-alvo, modelo elegível, saldo/consumo do dia e inexistência de rota Paid, créditos pré-pagos ou outro produto faturável no caminho. Não publicar dados financeiros ou credenciais.
2. Utilizar REST direto; sem Worker, armazenamento cloud, AI Gateway, logs remotos ou provedor alternativo automático. Confirmar documentação vigente do bloqueio de excedente e política de tokens.
3. Só iniciar se houver pelo menos 2.000 Neurons livres reservados para o lote; impedir concorrência com outros consumidores da mesma franquia. Se não houver prova de saldo, não executar.
4. Congelar teto de 20 tentativas, entrada/saída, timeout 120s e concorrência 1. Parar em 429/403/quota, mudança de plano, consumo inesperado, saldo não verificável ou custo não zero. Nunca fazer upgrade para destravar.
5. Registrar uso/custo antes e depois, incluindo falhas e tokens de raciocínio. Orçamento no cliente reduz consumo; a barreira de não cobrança é o plano Free comprovado. Não alegar que um contador local impede cobrança no Paid.

R$ 0 aqui significa **nenhuma nova cobrança de serviço, assinatura, compra de hardware ou infraestrutura**, não ausência de esforço humano. Energia/internet em máquina existente exigem que a Direção confirme ausência de desembolso adicional; se o critério incluir todo custo marginal físico, zero absoluto permanece não demonstrado. Contingência também precisa de comprovação própria, sem herdar a condição Cloudflare.

## 7. Privacidade e segurança

Enviar apenas os cinco textos sintéticos e instruções/contrato. Gabaritos, histórico de trabalho, dados reais, GitHub privado e prompts com credenciais ficam fora das requisições. O modelo não recebe acesso a arquivos, rede ou ferramentas; o texto do card é dado, inclusive quando contém instrução maliciosa.

Credencial futura de inferência com escopo mínimo confirmado, fora de repositório e relatórios, injetada na sessão local; nunca em CLI visível, logs, arquivos exportados ou conversa. Não criar/usá-la agora. Headers e erros devem ser sanitizados. Se menor privilégio não for comprovável, interromper configuração.

Saídas/manifestações locais acessíveis apenas à equipe autorizada; retenção proposta de 30 dias para respostas brutas e exportações, depois descarte sob owner Direção. Resultados agregados podem ser mantidos mediante decisão. Não usar serviços de storage/cache/log cloud.

Cloudflare declara não usar Customer Content para treino ou melhoria sem consentimento e menciona armazenamento quando combinado com serviços de storage. Isso não comprova residência brasileira nem prazo absoluto de retenção operacional; consultar termos/licença do modelo e confirmar aceitabilidade para estes dados sintéticos antes de inferência. [C2] Gemini Free tem uso para melhoria declarado, sem garantia equivalente de privacidade. [G1] Substituição de provedor preserva contratos, mas depende de decisão explícita e rechecagem dos termos.

## 8. Comparação dos cinco casos

Preservar todos os gabaritos QA do anexo. Derivar unidades avaliáveis, com referência ao gabarito, sem transformar novas classificações numéricas em requisito de Produto aprovado. Nenhum gabarito ou rótulo de categoria é mostrado ao modelo. IDs para execução podem ser opacos para evitar que o nome da categoria entregue a resposta.

| Caso | Foco de avaliação derivado do gabarito |
|---|---|
| SYN-QI-01 | Contradição entre regras de cancelamento, esclarecimento de precedência/estorno, estados e limite de 24h; não escolher regra unilateralmente |
| SYN-QI-02 | Idempotência, concorrência, ordem dos eventos, origem e transições; não presumir deduplicação/assinatura |
| SYN-QI-03 | Termos não mensuráveis e condições de medição/falha; valores sugeridos não viram requisitos |
| SYN-QI-04 | Consumidores, mudança de contrato e propagação parcial; autenticação/regressão e perguntas pertinentes, sem alegar leitura de diff |
| SYN-QI-05 | Desvincular versus excluir globalmente, automações/autorização/histórico; testes destrutivos pendentes de regra |

Baseline: instrução genérica congelada para analisar o card, indicar testabilidade, problemas, riscos, até três prioridades, perguntas e referências. Mesmo contrato JSON e orçamento. QI acrescenta metodologia explícita de estados, limites, dependências, incerteza e checagem de consistência, sem exemplos/gabaritos dos casos. Essa comparação mede abordagem especializada, não superioridade entre marcas de modelo.

Apresentar ao avaliador pares A/B em ordem alternada, sem identificar modo. Dois relatórios recebem mesmo layout, com erros/truncamentos visíveis. O avaliador usa gabarito e rubrica; quem redige prompts não deve pontuar o mérito sozinho. QA humano nomeado futuramente pela Direção; outro chat da mesma identidade não é independência humana. Se só um avaliador existir, declarar limitação e resultados exploratórios. Medir tempo ativo até aceitar/editar/rejeitar e decisão final, sem contar espera de inferência como revisão; latência vai em coluna separada.

Indicadores por card e modo: cobertura de unidades esperadas (0 ausente / 0,5 parcial / 1 suficiente); omissões críticas em contagem; falsos positivos materiais (regra/defeito inventado, separado de hipótese válida); proporção de achados com fonte correta e suporte semântico; prioridades decisivas pertinentes/obrigatórios preservados; classificação justificada; número de edições, recomendação aceitar/editar/rejeitar e minutos de revisão. Reportar denominadores, dados por caso e mediana; não inventar probabilidade ou economia percentual sem medição.

Os cinco casos não cobrem caminho plenamente testável, adversários, longa documentação ou controles mandatórios em excesso. Não adicionar novos casos nesta POC. Esse limite impede declarar generalização, robustez comercial ou validade plena de toda a taxonomia.

## 9. Sucesso, falha e interrupção

Critérios propostos para congelar antes da execução, não metas de Produto já aprovadas:
- **Segurança mínima:** nenhuma omissão do problema central dos cinco casos; nenhuma regra/defeito inventado material ou aprovação/execução fictícia; nenhuma prioridade obrigatória conhecida perdida; todo relatório aceito no contrato e com referências válidas.
- **Sinal favorável à hipótese:** QI vence o genérico em utilidade/priorização fundamentada em mais pares do que perde, sem aumentar omissões/falsos positivos, com esforço de revisão mediano não maior. Declarar contagens e motivos. Não impor percentual arbitrário de ganho sem baseline.
- **Inconclusivo:** empate, variação que muda a conclusão entre rodadas, erros de fornecedor, revisão não cega, comparador não equivalente ou menos de cinco pares completos. Não selecionar só respostas boas.
- **Falha de qualidade:** problema central omitido, certeza inventada, contraditório chamado plenamente testável sem justificativa ou perda de controle obrigatório. Não significa inviabilidade definitiva; registrar causas para eventual decisão sobre novo experimento.
- **Interrupção operacional:** qualquer dado real/segredo, cobrança ou dúvida de quota/plano, timeout/truncamento sistemático, quebra de isolamento, provedor indisponível, saída solicitando ação externa. Parar o lote afetado; conservar evidência sanitizada e devolver ao owner. Sem repetição automática ou correção do prompt durante o benchmark.

DoD futuro: dez relatórios pareados avaliados contra gabaritos imutáveis, falhas incluídas, manifesto completo, custo comprovado antes/depois e parecer humano sobre a hipótese. A repetição de dez chamadas é opcional; ausência reduz evidência de estabilidade.

## 10. Esforço e dependências

| Trabalho futuro | Estimativa |
|---|---:|
| Fixtures, contratos e rubrica | 4–6h |
| Pipeline, adaptador, limites e relatórios | 8–12h |
| Prompts congelados e verificações offline | 4–6h |
| Lote autorizado, conferência de evidências e comparação | 4–6h Engenharia + 2–3h avaliador |
| Síntese e correção focal de defeitos técnicos | 2–4h |
| **Total** | **22–34h Engenharia + 2–3h avaliador** |

Estimativa de planejamento, sem medições; cerca de 3–5 dias úteis de esforço técnico, excluindo espera por decisão/acesso e download/localização de hardware. Não equivale ao MVP anterior estimado em 8–13 dias. Sem reserva de dedicação integral ou gastos.

Bloqueios para implementar: autorização posterior e definição do ambiente/artefatos permitidos. Bloqueios apenas para inferir: conta/modelo elegíveis, R$0 e privacidade demonstrados, acesso mínimo autorizado e disponível, limites de tokens e avaliador designado. Documento integral ENG-VIAB-01 não recuperado é limitação de proveniência, não motivo para refazer discovery. #47, Jira, bancos, interface e despacho automático não são dependências.

Riscos não bloqueantes para preparar código offline: amostra pequena e enviesada; modelo atualizado; sensibilidade ao prompt; limites das validações determinísticas. Devem aparecer no relatório final.

## 11. Objeto exato de autorização futura e retorno

Deliberação proposta A: autorizar somente implementação local da estrutura da seção 3, com os cinco fixtures/gabaritos preservados, mocks, exportação e verificação offline, sem chamadas reais, GitHub ou cloud. Nenhuma branch/commit/PR é inferida; caso desejados, incluir repositório, branch, arquivos e efeito CI na autorização específica.

Deliberação proposta B, depois das evidências: selecionar Qwen3/Workers AI ou contingência; autorizar credencial mínima local e até 20 tentativas sintéticas conforme limites da seção 6, exclusivamente na conta/plano comprovados, sem provisionar Worker/DB/Gateway, upgrade ou gasto; nomear avaliador e aceitar termos/retencão. Não autorizar genericamente um provedor pago com orçamento zero. Integração real, UI, treino e publicação continuam fora.

**Verificações desta etapa:** leitura e conferência documental de fontes, coerência dos contratos, cálculos estimados e limites; nenhum teste funcional, implementação, inferência ou acesso a credenciais. QA consultivo anterior reutilizado; novos QA/validação/auditoria/revisão independente não acionados; nenhuma dispensa inventada.

**ENCAMINHAMENTO:** este documento é a mensagem integral de retorno à Direção, na mesma conversa, conforme rota direta solicitada. Preparado e entregue aqui; registro GitHub não realizado; transporte/aceite de terceiros não presumidos. WIP de planejamento concluído, sem execução seguinte automática. Direção recebe o plano para ACEITAR/DEVOLVER e deliberar posteriormente sobre os objetos A/B. Não se solicita reconfirmação da análise já autorizada. **Iniciativa permanece aberta; implementação NÃO autorizada.**

## 12. Fontes públicas e institucionais

Consultadas em 12/10/2026; reconferir antes da execução:
- [C1 — Workers AI pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/): franquia, reset, bloqueio Free e coeficientes Qwen3. Leitura concluída via URL da mesma página com parâmetro `ref=runtimewire`, após falha na URL simples.
- [C2 — Workers AI data usage](https://developers.cloudflare.com/workers-ai/platform/data-usage/).
- [C3 — modelos com exigência de Paid](https://developers.cloudflare.com/changelog/post/2026-07-28-models-require-workers-paid/): mostra que acesso gratuito depende do modelo, não garante conta.
- [G1 — Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing), [billing](https://ai.google.dev/gemini-api/docs/billing/) e [rate limits](https://ai.google.dev/gemini-api/docs/rate-limits): limites efetivos requerem leitura na conta; nenhum número de RPM/RPD presumido.
- [O1 — Ollama API](https://docs.ollama.com/api/introduction): API local. Card específico Qwen3-4B e página individual Cloudflare Qwen3 não abriram; não afirmar licença, memória, contexto ou parâmetros dessas páginas sem confirmação.
- [AGT-ENG](https://github.com/gentestsai-sudo/gentests-os/blob/main/02-Agentes/Engenharia/Contrato-Agente-Executor-Tecnico.md), [POL-003](https://github.com/gentestsai-sudo/gentests-os/blob/main/00-Constituicao/Matriz-de-Permissoes.md), [PRC-ENG-001](https://github.com/gentestsai-sudo/gentests-os/blob/main/03-Processos/Entrega-Tecnica-e-Infraestrutura.md), [SEC-AI-001](https://github.com/gentestsai-sudo/gentests-os/blob/main/00-Constituicao/SEC-AI-001-Seguranca-Confiabilidade-Agentes.md), [QG-001](https://github.com/gentestsai-sudo/gentests-os/blob/main/00-Constituicao/Quality-Gates/QG-001-Politica.md), [template](https://github.com/gentestsai-sudo/gentests-os/blob/main/07-Templates/GT-HANDOFF-001-TEMPLATE.md).

## Anexo — cards e gabaritos QA preservados

### SYN-QI-01 — Cancelamento de pedidos
Texto: “Permitir cancelar pedidos pagos até 24 horas após a compra. CA1: cancelamento permitido somente antes da separação. CA2: cancelamento permitido inclusive após a expedição.”

Gabarito esperado: detectar a contradição entre prazo e estado do pedido; sinalizar que não há regra inequívoca; perguntar qual condição prevalece e como funciona o estorno. Priorizar testes nas transições entre separado, expedido e cancelado, além do limite de 24 horas. Não inventar que o cancelamento pós-expedição é permitido ou proibido.

### SYN-QI-02 — Webhook de pagamento
Texto: “Ao receber o evento de pagamento aprovado, atualizar o pedido para pago e liberar o produto. O provedor poderá reenviar eventos ou entregá-los fora de ordem.”

Gabarito esperado: destacar idempotência, concorrência e eventos fora de ordem como riscos prioritários; recomendar duplicação do mesmo evento e chegada de um evento antigo após um novo. Questionar validação da origem e regras de transição. Não assumir que existe assinatura ou mecanismo de deduplicação sem essa informação.

### SYN-QI-03 — Dashboard operacional
Texto: “O dashboard deve abrir rapidamente e exibir informações atualizadas em tempo real, mantendo uma experiência fluida.”

Gabarito esperado: apontar “rapidamente”, “tempo real” e “fluida” como critérios não verificáveis; solicitar limites de tempo, frequência ou latência de atualização, condições de medição e comportamento em falhas. Propor exemplos de critérios mensuráveis, sem apresentar valores sugeridos como requisitos aprovados.

### SYN-QI-04 — Alteração de e-mail
Texto: “Permitir alterar o e-mail do usuário. Esse dado é utilizado para login, notificações e contato de faturamento. Outro card da mesma release altera o contrato de integração do campo `email` para `primary_email`.”

Gabarito esperado: identificar os três consumidores, o risco de incompatibilidade de contrato e a possibilidade de dados divergentes entre serviços. Priorizar teste de integração/regressão envolvendo alteração, autenticação e propagação. Perguntar sobre confirmação do novo endereço, compatibilidade durante a release e tratamento de atualização parcial. Não alegar que o diff real foi analisado.

### SYN-QI-05 — Remoção de etiquetas
Texto: “Permitir que o usuário remova uma etiqueta utilizada em contatos. CA1: após remover, ela deve desaparecer da tela. Algumas etiquetas também são usadas em automações.”

Gabarito esperado: perceber que “remover” pode significar desvincular do contato ou excluir globalmente; questionar o impacto nas automações, autorização e histórico. Destacar risco de efeito colateral, mas não afirmar que a remoção deve apagar históricos ou interromper automações. Suspender a definição dos testes destrutivos até esclarecimento.