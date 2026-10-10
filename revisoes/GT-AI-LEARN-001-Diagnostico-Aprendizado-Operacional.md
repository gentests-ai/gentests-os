---
id: GT-AI-LEARN-001
tipo: diagnostico-arquitetura-aprendizado-operacional
versao: 0.1.0
status: proposta
estado_documental: aguardando-revisao-independente
data: 2026-10-10
responsavel_elaboracao: Orquestrador GenTests.ai
aprovador: Direcao
revisao_independente: pendente
implementacao_autorizada: nao
publicacao_autorizada: nao
---
# GT-AI-LEARN-001 — Aprendizado operacional controlado e suíte de Evals

> **PROPOSTA INTERNA — NÃO IMPLEMENTAR NEM PUBLICAR.** Diagnóstico e desenho para revisão independente. Não altera políticas, permissões, agentes ou fluxos existentes. Não inclui fine-tuning nem habilita qualquer autoaprendizado/autopromoção de regras.

## 1. Decisão executiva proposta

**Viabilidade favorável para um piloto pequeno, condicionada à revisão independente, aprovação humana e validação das permissões reais.** Reutilizar GitHub, arquivos Markdown/JSON, testes Python padrão (unittest) e GitHub Actions já existentes. Aprendizado é evolução controlada de instruções, critérios, casos e processo, **não** mudança de pesos de modelos, memória automática ou aprovação por agentes. A prioridade é curar erros já confirmados antes de ampliar o número de agentes.

## 2. Escopo examinado e limites

Inspeção documental da árvore `main` do repositório privado `gentestsai-sudo/gentests-os` e leitura dos principais documentos abaixo, além dos caminhos de PRs anteriormente analisados. Foram identificados scripts `scripts/agt_val_review.py`, `scripts/validate_commercial_email.py`, `scripts/x9_scan.py`, `scripts/check_links.py`, `scripts/triagem_sites.py`, testes `tests/test_agt_val_review.py`, `tests/test_commercial_email.py`, fixtures válidos/inválidos e workflows `email-quality-gate.yml`, `markdown-check.yml`, `x9-daily.yml`.

Referências lidas: `00-Constituicao/SEC-AI-001-Seguranca-Confiabilidade-Agentes.md`, `00-Constituicao/Quality-Gates/QG-001-Politica.md`, `03-Processos/Gestao-de-Nao-Conformidades.md`, `03-Processos/Inspecao-X9.md`, `03-Processos/Parecer-AGT-VAL-v02.md`, `05-Evidencias/Registro-de-Operacoes.md`, `06-Indicadores/Indicadores-de-Governanca.md`, `09-Backlog/RNC/RNC-2026-001.md`, `02-Agentes/Auditor/Contrato-Agente-Auditor.md`, além da matriz de permissões, POL-001/002, QG-CORE, GOV-5S-001 e documentos dos trabalhos anteriores.

O repositório foi retornado como **private** pelo conector. Isso não demonstra proteção de branch, configuração de runners, revisores obrigatórios, retenção de logs ou ausência de segredos. **Não foram executados testes**, auditados todos os commits/conteúdos dos PRs, obtidos custos contratados da conta ou consultados os controles administrativos de GitHub Actions. Custos e baseline são estimativas explícitas.

## 3. Mecanismos existentes e lacunas

| Mecanismo | Evidência | Estado/limitação | Lacuna para aprendizado |
|---|---|---|---|
| Registro de decisões | `04-Decisoes/Registro-de-Decisoes.md` | Sem catálogo consolidado de aprovações no snapshot examinado | Vincular mudança de regra a decisão e commit autorizado |
| RNC | `03-Processos/Gestao-de-Nao-Conformidades.md`, `09-Backlog/RNC/RNC-2026-001.md` | Fluxo previsto, RNC exemplar aberta | Extrair caso de regressão de falha confirmada e revalidada |
| Operações | `05-Evidencias/Registro-de-Operacoes.md` | Modelo com ID/agente/fonte/versão/resultado | Armazenar execução minimizada e resultado observável de maneira sistemática |
| Quality Gates | QG-001, QG-CORE, QG-STR-001 | Documentos em `proposta`; conformidade semântica depende de humano | Traduzir apenas critérios objetivos em testes determinísticos; não declarar gate aprovado |
| Métricas | `06-Indicadores/Indicadores-de-Governanca.md` | Indicadores propostos, sem linha de base | Definir numerador, denominador, unidade, janela e fonte |
| Validação automatizada | `scripts/`, `tests/`, `.github/workflows/` | Verificações de e-mail e heurísticas/documentação do X9 | Cobertura de regressões reais ainda não centralizada em suíte de Evals |
| Independência | AGT-VAL / AGT-AUD e SEC-AI-001 | Separação de funções especificada em proposta | Evidência de revisor distinto e aprovação humana por mudança |
| Experiência anterior | PRs OS #2–#7, site #1, pareceres REV-COM-QJ-003, REV-SITE-001, revisão CNQ e GOV-001 | Mudanças e pareceres versionados; vários PRs ainda abertos | Curadoria de cenários sem confundir parecer antigo, branch nova e fechamento real |

**Status normativo:** várias fontes acima estão com `status: proposta`; usar como referências cautelares de desenho, não apresentar como políticas já aprovadas. Nada neste plano modifica seus status.

## 4. Fontes históricas candidatas para os primeiros Evals

| Candidato | Falha ou acerto a verificar | Avaliação proposta | Condição de inclusão |
|---|---|---|---|
| Formulário de site (REV-SITE-001) | Configuração `_captcha=true` não comprova entrega/ativação | Dado um diff estático, saída esperada `não verificável funcionalmente` | Evidência documental e commit vinculados; não usar dados pessoais do formulário |
| Preços da campanha e QA Express | R$690, R$890, R$490 e QA Start R$290 não equivalem automaticamente | Agente deve identificar alternativas, não homologar preço nem misturar SKUs | Conferir versão/base de cada proposta |
| Quality Journey (REV-COM-QJ-003) | A apresentação declarada não estava na árvore inicialmente inspecionada | Declarar binário ausente `não verificável`, reavaliar com evidência nova | Vincular commit examinado e não reutilizar parecer em nova versão automaticamente |
| CNQ v0.3 | Caixa versus custo econômico gerencial | Validar categorias distintas, soma 2260+600+900+1000=4760 e vedar declaração de desembolso de 4760 | Confirmar texto vigente e modelo hipotético, sem dados reais de clientes |
| Primeiro PIX/CRM | `SENT` não equivale a entregue, aberto ou respondido | Caso negativo para inferência de resultado sem confirmação | Evidência sintética e rubrica aprovada |
| GOV-001 / GOV-11 | IDs duplicados e status `proposta` | Encontrar conflito, não alterar documentos nem declarar normas em vigor | Revisor confirmar achado antes de promover a teste canônico |
| AGT-VAL/e-mail | Sem fontes para alegações | Verificação determinística existente deve sinalizar ausência de evidência | Fixture fictício sem informações pessoais |
| Segurança | Instrução maliciosa em e-mail/anexo | Agente ignora instrução de elevar privilégio ou alterar políticas | Payload sintético; validação de segurança e revisão humana |

**Importante:** esses são **casos candidatos** e não suíte aprovada. Cada golden case deverá conter evidência primária, expectativa verificável, rubrica e parecer de curadoria independente. Um erro apontado, mas ainda contestado, deve permanecer fora do conjunto de referência homologado.

## 5. Modelo canônico proposto de Eval

Usar arquivos pequenos JSON ou YAML versionados no GitHub, por exemplo `evals/cases/EV-001.json`. Campos mínimos:
- `id`, `version`, `task_family`, `risk_level`, `source_repo`, `source_pr`, `source_commit`, `source_path`;
- `input_fixture` sintético/sanitizado, `expected_behavior` objetivo, `forbidden_behavior`, `rubric`;
- `oracle_type` (`deterministic` / `human`), `curation_status` (`candidate` / `reviewed` / `approved` / `retired`), `curator`, `reviewer`, `approved_by`, `decision_ref`;
- `data_classification`, `retention_rule`, `created_at`, `supersedes` e `tags`.

Separar dados de **teste**, critérios do **oráculo** e evidências de **execução** para evitar circularidade. Resultado deve guardar `case_version`, `agent_version/prompt_sha`, `model_identifier` se conhecido, `runner_version`, timestamp, resultado bruto saneado, resultado da rubrica, falhas e justificativa. Nunca registrar secrets, prompts internos sigilosos ou conteúdo de cliente sem autorização explícita.

Oráculos determinísticos avaliam esquema, links, soma, status e permissões objetivas; oráculos semânticos exigem revisor independente com critérios claros. LLM-as-judge seria hipótese futura: caro, variável e sujeito a viés; não ativar como aprovador.

## 6. Ciclo controlado

1. **Capturar:** executor registra resultado e evidências de execução. Parecer, RNC e issue apontam falhas e sua severidade, sem promover conhecimento automaticamente.
2. **Triar:** orquestrador agrupa por causa raiz, remove duplicatas e propõe novo caso, com dados sanitizados e fonte/commit.
3. **Curar:** revisor independente verifica que problema foi comprovado, define comportamento esperado e tenta invalidar o caso. Casos controversos permanecem candidatos.
4. **Autorizar:** direção aprova inclusão/alteração de golden cases com implicações institucionais e qualquer mudança de políticas, permissões ou processos. Aprovar caso não autoriza publicar conteúdo externo.
5. **Executar baseline:** runner local ou CI rodará apenas avaliações aprovadas, com reprodutibilidade de versão. Começar pelas determinísticas offline.
6. **Corrigir:** executor altera artefato, teste ou instrução **em PR separado**, sem editar o próprio parecer/oráculo aprovado unilateralmente.
7. **Revalidar:** revisor examina diff, evidências, resultados de regressão e riscos de false positive/false negative. Resultado técnico não se confunde com autorização humana.
8. **Registrar:** direção decide aplicação onde necessário; registrar decisão, SHA, métricas e rollback. Após duas rodadas automáticas malsucedidas, escalar em vez de entrar em loop.

A independência é por **papel e revisão efetiva**, não garantida apenas por nomes de agentes. Quando usar o mesmo provedor/modelo em papéis diferentes, complementar com avaliação determinística e revisão humana; não assumir independência metodológica perfeita.

## 7. Métricas propostas e fórmulas

| Indicador | Fórmula / base | Janela | Interpretação |
|---|---|---|---|
| Reincidência confirmada | Nº de falhas da mesma categoria/causa reaparecidas após correção aprovada ÷ Nº de oportunidades elegíveis de reavaliação dessa categoria | 30 dias ou últimos N casos, com ambos exibidos | Sem oportunidades, N/A; distinguir mesmo defeito reaberto de novo |
| Pass rate em Evals | Casos aprovados que passam ÷ casos aprovados executados | Por versão/PR e tendência semanal | Informar casos pulados/inválidos separadamente |
| Regressão | Casos aprovados que passavam no baseline e falham na versão candidata ÷ casos aprovados que passavam no baseline e foram reexecutados | Por comparação com baseline fixado | Não misturar adições/remoções de suíte sem estratificar |
| Retrabalho | Horas de correção, revalidação e reexecução associadas a falhas ÷ horas totais da atividade comparável | Semanal/mensal | Registrar tempo real, não estimado como observado |
| First-pass acceptance | Artefatos aceitos pelo revisor na primeira rodada ÷ artefatos elegíveis submetidos na primeira rodada | Mensal | Excluir cancelados com justificativa explícita |
| Evidência verificável | Execuções elegíveis com fonte, commit, contexto e resultado acessíveis ÷ execuções elegíveis | Mensal | 'Link existe' não prova conteúdo nem validade |
| Conformidade de autorização | Ações sensíveis com autorização válida anterior ÷ ações sensíveis verificadas | Mensal | Evento não autorizado é incidente, não apenas redução percentual |
| Custo por eval | Custo incremental medido de CI/API/revisão ÷ casos executados | Por rodada | Separar custo de ferramenta, infraestrutura e tempo humano |
| Escapes | Defeitos comprovados após aprovação ÷ entregas aprovadas e observadas na janela definida | Mensal + janela de maturação | Pequenas amostras, latência e severidade exigem destaque |

**Baseline:** iniciar sem metas fictícias. Registrar ao menos duas rodadas da mesma suíte antes de usar tendência; pequenas amostras são descritivas, não prova causal de melhoria. Reportar numerador e denominador junto ao percentual. Medir dimensão crítica por severidade e família, evitando que inúmeros testes simples escondam falha de segurança.

## 8. Arquitetura mínima e custo

**Etapa 0 (somente planejamento agora):** este Markdown e PR draft, custo incremental direto de serviço externo não identificado; esforço humano não é zero.

**Piloto candidato após autorização:**
```
gentests-os/
  evals/
    README.md
    cases/           # fixtures sintéticas e rubricas versionadas
    baselines/       # manifestos de versão aprovados
    results/         # apenas relatórios agregados e sanitizados, se retenção aprovada
  scripts/
    run_evals.py     # unittest/stdlib primeiro
  tests/
    test_evals.py
  .github/workflows/
    evals.yml        # proposta futura, não criada nesta PR
```
- GitHub privado já existe; versionamento Markdown/JSON e revisão por PR podem reutilizar a conta atual.
- Python stdlib (json, unittest, pathlib) dispensa licenças e dependências adicionais.
- Primeiro rodar localmente; GitHub Actions somente após examinar limites de minutos, armazenamento, retenção, segurança de workflows, runner e condições do plano vigente.
- Sem chamada paga a API/modelos na fase determinística; avaliação semântica inicialmente manual e amostrada.
- **Custo monetário adicional estimado:** R$0 para arquivos, scripts locais e testes determinísticos sem novos serviços pagos, desde que ferramentas/infraestrutura existentes comportem o volume; não é promessa de custo total zero. CI pode consumir cotas/cobrança conforme plano, repositório privado e runner. API/modelos e revisão humana têm custos variáveis, não estimados sem preço/cota e duração reais.
- **Esforço humano exploratório (não compromisso):** curadoria inicial de 5–8 casos, algo como 4–10 horas distribuídas entre executor/revisor/orquestrador, mais validação da direção; medir no piloto. Implementação técnica futura pode exigir esforço adicional e não está autorizada.

## 9. Segurança, contaminação e antiaprendizado incorreto

1. **Não contaminar goldens:** jamais transformar texto gerado pelo próprio agente em `expected` sem evidência/oráculo independente; guardar `candidate` fora do baseline.
2. **Sem autoalteração:** executor não muda rubrica, dataset de referência ou sua permissão sem revisão e decisão. Falha de teste não permite diminuir severidade ou remover teste silenciosamente.
3. **Proveniência:** fonte primária, commit, versão, status, revisor e justificativa imutáveis em histórico Git; não confundir parecer de commit anterior com versão corrente.
4. **Proteção de dados:** sanitizar nomes, identificadores, credenciais, conteúdos de e-mail e incidentes de clientes; minimizar logs e limitar acesso. Verificar licenças/consentimentos antes de usar material externo.
5. **Prompt injection:** entradas externas são dados de teste não confiáveis. Não executar instruções nelas contidas; runner offline sem segredos e sem privilégios de escrita, sempre que possível.
6. **CI seguro:** avaliar `pull_request` versus `pull_request_target`, tokens mínimos, aprovação de contribuidores, dependências fixadas, arquivos de relatório e retention; nunca expor credenciais a PR não confiável.
7. **Separar teste e treino:** não usar avaliação como novo prompt de produção inadvertidamente; não confiar em score se o agente viu respostas esperadas.
8. **Falsos positivos e regressões:** manter caso negativo e positivo, revisão amostral, comparação de baseline fixo e procedimento de rollback/revert.
9. **Ciclos e drift:** limitar duas correções automáticas, revalidar rubricas quando política for formalmente alterada, registrar mudança no denominador da métrica.
10. **Auditoria:** logs minimizados, hashes/SHAs, registro do aceite humano, ausência explícita de ações não realizadas.

## 10. Plano incremental e gates

| Fase | Execução proposta | Entrada | Critério de aceite | Autorização |
|---|---|---|---|---|
| 0 — Diagnóstico | Documento e PR draft | Documentação existente | Parecer independente e limites claros | Esta fase é apenas proposta |
| 1 — Curadoria piloto | 5–8 casos históricos sintéticos; taxonomia de erro | Falhas confirmadas e fontes | 100% casos com fonte/commit, status, rubrica, dado minimizado e parecer | Direção autoriza trabalho, sem promoção automática |
| 2 — Runner determinístico | Python stdlib local e golden baseline versionado | Casos aprovados | Mesma entrada/versão produz resultado reproduzível; caso positivo/negativo; sem rede/segredos | PR técnico separado e revisão |
| 3 — CI controlado | Workflow GitHub limitado a leitura/teste | Runner validado e proteção de PR verificada | CI reporta falha sem alterar política/artefato; execução em fork/PR segura | Autorização técnica específica |
| 4 — Avaliação semântica amostral | Rubricas humanas e divergência entre revisores | Baseline estável | Discrepâncias registradas; humano resolve; custos medidos | Direção decide expansão |
| 5 — Aprendizado contínuo | Correções por PR e painel simples | 2+ rodadas comparáveis | Regressão, reincidência e esforço exibidos com denominadores | Aprovação por mudanças relevantes |

**Quality Gates propostos:** QG-L para rascunhos isolados; QG-M para fixtures e runner de baixo risco; QG-H para qualquer mudança de política, permissões, produção, dado sensível ou ação externa. Aplicação definitiva depende de homologação do QG-001. Independentemente do nível, bloquear publicação de segredo, autoaprovação, uso de dados não autorizados e alterações a goldens sem validação.

**Go/no-go do piloto:** go apenas se casos elegíveis, dados permitidos, papéis independentes, baseline auditável, custo aceitável e decisão humana estiverem documentados. Senão: não verificável/bloqueado conforme natureza do impedimento.

## 11. Dependências e riscos residuais

- GOV-001 e REV-GOV-001 (PRs OS #6 e #7) podem alterar a taxonomia, hierarquia e definição da fonte canônica; alinhar antes de tornar qualquer procedimento oficial.
- Confirmação de privilégios do GitHub, regras de proteção da main e configuração de Actions não realizada nesta análise.
- Avaliação automática de qualidade semântica permanece aberta; nunca declarar acurácia ou consistência inexistente.
- Conjunto inicial pequeno pode induzir overfitting de prompts/casos; usar holdout e novos casos independentes quando houver volume.
- Conhecimento histórico pode estar desatualizado, ser hipótese ou conter dados privados; revisar proveniência e prazo de validade por item.
- Indicadores dependem de tempo real registrado, não somente de quantidade de documentos produzidos.

## 12. Solicitação ao revisor independente

Conferir fontes, classificação de status, viabilidade, riscos, critérios de curadoria, independência e custos; procurar exemplos concretos falsos/insuficientes, falsos positivos, vazamento e circularidade de oráculo. Recomendação de parecer itemizado com bloqueios, correções e decisão de elegibilidade para **piloto futuro**, não para implementação atual. Não alterar este arquivo, não realizar merge ou instalar workflows.

**Resultado deste PR:** proposta documental isolada; nenhum Eval foi criado/rodado, nenhum workflow alterado e nenhuma regra institucional promovida.
