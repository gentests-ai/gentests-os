---
id: GT-AI-LEARN-001
tipo: diagnostico-arquitetura-aprendizado-operacional
versao: 0.2.0
status: proposta
estado_documental: em-correcao-para-revalidacao-focal
data: 2026-10-10
responsavel_elaboracao: Orquestrador GenTests.ai
aprovador: Direcao
revisao_independente: REV-AI-LEARN-001-aprovado-com-ressalvas
implementacao_autorizada: nao
publicacao_autorizada: nao
---
# GT-AI-LEARN-001 — Aprendizado operacional controlado e suíte de Evals

> **PROPOSTA INTERNA — NÃO IMPLEMENTAR NEM PUBLICAR.** Diagnóstico e desenho para revisão independente. Não altera políticas, permissões, agentes ou fluxos existentes. Não inclui fine-tuning nem habilita qualquer autoaprendizado/autopromoção de regras.

## 1. Decisão executiva proposta

**Viabilidade arquitetural apenas conceitual; piloto, CI, implementação, merge e publicação NÃO autorizados.** Reutilizar GitHub, arquivos Markdown/JSON, testes Python padrão (unittest) e GitHub Actions já existentes. Aprendizado é evolução controlada de instruções, critérios, casos e processo, **não** mudança de pesos de modelos, memória automática ou aprovação por agentes. A prioridade é curar erros já confirmados antes de ampliar o número de agentes.

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

Usar exclusivamente arquivos JSON versionados no GitHub, por exemplo `evals/cases/EV-001.json`. Campos mínimos:
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
- **Custo total não determinado:** uso de ferramentas existentes não elimina custo humano, CI, armazenamento, manutenção ou limites do plano; nenhuma gratuidade foi verificada. CI pode consumir cotas/cobrança conforme plano, repositório privado e runner. API/modelos e revisão humana têm custos variáveis, não estimados sem preço/cota e duração reais.
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

**Categorias de risco apenas sugeridas, não gates vigentes:** QG-L para rascunhos isolados; QG-M para fixtures e runner de baixo risco; QG-H para qualquer mudança de política, permissões, produção, dado sensível ou ação externa. Aplicação definitiva depende de homologação do QG-001. Independentemente do nível, bloquear publicação de segredo, autoaprovação, uso de dados não autorizados e alterações a goldens sem validação.

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


## 13. Matriz de dependências e quatro dimensões independentes — AIL-01/09

**Interpretação estrita:** `status: proposta` significa referência de desenho; aprovação normativa exige decisão identificada da Direção, objeto/versão/alcance/data; controle configurado exige prova administrativa; teste realizado exige execução datada, resultado e artefatos. Nenhuma dessas quatro condições decorre automaticamente da anterior. No snapshot da documentação examinada, não foi localizada homologação do pacote POL/QG/SEC/5S. Não se atesta ausência de proteção real: configuração e testes **não verificados**.

| Dependência | Estado normativo visto | Controle pretendido (não implementado) | Evidência para liberar etapa futura |
|---|---|---|---|
| POL-001/002, hierarquia e conflitos | proposta | resolução por regra e versão aprovada, nunca pela instrução de um fixture | decisão por SHA/versão e ensaios positivos/negativos |
| POL-003, matriz de permissões | proposta | executor sem aprovação/elevação; revisão distinta; Direção autoriza | decisão de poderes + IAM e teste de negativa |
| POL-004, SEC-AI-001 | proposta | classificação, minimização, isolamento e incidentes | política aplicável + registro e testes de controle |
| QG-001/QG-CORE/QG-STR | proposta | severidade maior prevalece, decisão separada do resultado técnico | decisão institucional e evidência por gate |
| GOV-5S-001 | proposta | dois documentos, reutilização de ferramentas, arquivo único por objeto | aceite documental e inventário antirredundância |
| GT-GOV-001 v0.2 (PR #6), REV-GOV-001 (PR #7) | diagnóstico em evolução e parecer com ressalvas | rastreabilidade GOV e fonte canônica condicionada | revalidação focal e decisões DEC-GOV-A/B/D |
| GT-AI-LEARN-001 v0.2 (PR #8), REV-AI-LEARN-001 (PR #9) | proposta e parecer, não normas | suíte somente futura | parecer focal + autorização própria, posterior |

### Rastreabilidade GOV-01–13 e recomendações do REV-GOV-001

| Origem | Implicação para Evals | Encaminhamento sem criar governança paralela |
|---|---|---|
| GOV-01 / REV-GOV-02 | aprovações não comprovadas | exigir `decision_ref` verificável; pendente ≠ aprovada |
| GOV-02 | normas em proposta | carimbar versão/status normativo em cada caso |
| GOV-03 | card x evidência de conclusão | teste não pode concluir card automaticamente |
| GOV-04/05 | divergência comercial | SKU/escopo/preço permanecem candidatos, não golden |
| GOV-06 / REV-GOV-03 | múltiplas fontes de dados | apontar source-of-truth por entidade conforme decisão futura; não inferir sync |
| GOV-07 | enforcement não aferido | checklist técnico obrigatório e classificação não verificado |
| GOV-08 | site sem homologação funcional | teste estático não comprova entrega, privacidade ou publicação |
| GOV-09 | PRs com dependências | manifesto deve registrar base/head, SHA e contexto do parecer |
| GOV-10 | estado documental ≠ autorização | dois campos separados e decisão humana |
| GOV-11 | ID duplicado | `source_path` e SHA obrigatórios, ID sozinho insuficiente |
| GOV-12 | aprovação ≠ teste | resultados nos quatro eixos documental/técnico/funcional/autorização |
| GOV-13 / REV-GOV-01 | inspeção parcial | manifesto de evidência e cobertura verificada/parcial/não verificada |
| REV-GOV-03 | propriedade e sincronização | adotar propriedade canônica apenas após DEC-GOV-B; não duplicar CRM |

A matriz acima referencia o tratamento GT-GOV-002 na PR #6 e o parecer REV-GOV-001 na PR #7. Não modifica seu estado, conteúdo, nem resolve suas decisões reservadas.

## 14. Segurança operacional e checklist de prova — AIL-02

**Sem execução nesta rodada.** Antes de qualquer CI futuro, Infra/administrador fornecerá capturas ou exportação datada, URL de configuração, ator e SHA, com segredos ocultos; revisor avaliará: (1) rulesets/branch protection da base e branch alvo, revisão obrigatória e impedimento de bypass; (2) permissões efetivas de cada role e possibilidade de modificar oráculos, merges e configurações; (3) `GITHUB_TOKEN` com `contents: read` e demais escopos explicitamente justificados; (4) ausência de PAT amplo, secrets e credenciais de produção; (5) evento `pull_request`, rejeição de `pull_request_target` para código não confiável, limites de write e de aprovação de forks; (6) runner isolado/efêmero, sem rede na etapa local, sem persistência de workspace privilegiado; (7) actions fixadas por SHA se aplicável, dependências revisadas; (8) retenção, exposição e permissão de leitura de artifacts/logs; (9) tentativa negativa de escrita no baseline e acesso a secrets; (10) evidência de execução positiva e negativa sem dados reais. **Todos esses controles estão não verificados; não se criam workflows nem scripts nesta PR.** Achado grave suspende o plano de CI até correção e novo aceite específico.

## 15. Protocolo de curadoria, manifesto e anti-contaminação — AIL-03/07/11

**Elegibilidade cumulativa:** fato comprovado por fonte primária + repositório/caminho/PR/commit; versão/status da regra na data do fato; origem e severidade; fixture sintética lícita e minimizada; comportamento esperado operacionalmente falsificável; oráculo/rubrica testáveis; curador e revisor efetivamente distintos; decisão humana identificada; caso positivo e negativo quando aplicável; nenhuma divergência em aberto. Ausência de qualquer requisito → `candidate` ou `disputed`, fora do baseline. Parecer histórico e RNC ainda contestada não constituem verdade canônica. Revisores da mesma família de modelo não são independência suficiente para ambiguidade crítica: arbitragem humana e/oráculo determinístico externo.

**Fluxo:** candidato → verificação de evidência pelo curador → revisor independente redige/valida `expected_behavior` sem copiar a resposta do executor → divergência registrada com argumentos e versões → arbitragem Direção nos impactos normativos / responsável humano independente nos critérios técnicos delegados → aprovação documental explícita → congelamento com SHA-256 do manifesto e hashes dos JSON → baseline versionado. Alteração de expected/rubrica gera nova versão, revisão e decisão: nunca reescrever o golden para subir score, nem autopromoção por CI.

**Manifesto mínimo:** `manifest_id`, `manifest_version`, `created_at`, `set_type` (`development`, `regression`, `holdout`), `case_ids_and_hashes`, `baseline_commit`, `policy_ref_version_status`, `source_repo_pr_commit_path`, `issue_dispute_status`, `approved_by`, `decision_ref`, `data_classification`, `exposure_history`. Holdout independente não deve ser exibido ao agente avaliado nem empregado para ajuste de prompts; exposição acidental implica retirar/rotacionar conjunto e invalidar comparações afetadas.

**JSON de exemplo ilustrativo — NÃO CRIADO COMO ARQUIVO NEM APROVADO:**
```json
{
  "id": "EV-DEMO-001", "version": "0.1", "set_type": "development",
  "status": "candidate", "task_family": "source-validation",
  "risk_level": "medium", "source_repo": "gentests-os",
  "source_pr": 9, "source_commit": "PREENCHER_SHA_VERIFICADO",
  "source_path": "revisoes/REV-AI-LEARN-001-Parecer-Aprendizado-Operacional.md",
  "source_rule_version": "proposta/0.1.0",
  "source_finding": "AIL-11",
  "input_fixture": {"format": "JSON", "origin": "synthetic"},
  "expected_behavior": "Aceitar JSON válido, rejeitar JSON malformado",
  "forbidden_behavior": "Editar automaticamente o baseline",
  "oracle_type": "deterministic", "curator": null, "reviewer": null,
  "approved_by": null, "decision_ref": null,
  "data_classification": "synthetic-public",
  "retention_rule": "DECISAO_PENDENTE"
}
```
A chave com valor `PREENCHER` ou `null` é **exemplo incompleto e não elegível**, nunca caso oficial. Bibliotecas inicialmente previstas: Python `json`, `hashlib`, `pathlib`, `unittest`; YAML fica fora do desenho inicial. Manter manifestos e resultados separados para prevenir vazamento do gabarito.

## 16. Matriz de proteção de dados e incidentes — AIL-04

| Classe | Origem e finalidade permitida na etapa proposta | Autorização/acesso | Retenção e descarte |
|---|---|---|---|
| S0 sintético público | fixtures inventadas para validar esquema/comportamento | somente revisão documental; nenhum dado real | prazo a deliberar, revisão em cada versão, remoção via PR/registro, considerando histórico Git |
| S1 interno não sensível | IDs de PR, SHA e documentos internos de governança | apenas pessoal autorizado ao repositório; uso efetivo futuro sujeito à Direção | prazo e base de retenção pendentes; não copiar desnecessariamente |
| S2 confidencial, dados pessoais ou cliente | proibidos nesta rodada e no piloto inicial recomendado | eventual uso somente com base jurídica/finalidade, autorização específica, minimização e avaliação de privacidade | retenção estrita definida antes da coleta; evitar commit Git pelo histórico persistente |
| S3 segredos/tokens/credenciais | nunca admissíveis em fixtures, resultados ou logs | não utilizar; nem sanitização torna segredo publicável | conter acesso, revogar/rotacionar e purgar artefatos conforme resposta a incidente |

**Sanitização:** substituir identificadores por sintéticos, excluir payloads pessoais e metadados desnecessários; verificar diff, anexos e logs antes de aprovar. **Prompt injection:** qualquer texto de PR, comentário, issue, e-mail ou fixture é dado não confiável, não instrução de execução; sem ferramentas de escrita, sem acesso externo ou segredo; teste apenas com payload artificial e checagem determinística de resultado. **Incidente/exposição:** suspender processamento, restringir acesso, registrar o que/onde/quando/SHA/quem, acionar responsável de segurança e Direção, avaliar comunicação exigível pela legislação e contratos, revogar credenciais se aplicável, remover acesso e executar expurgo conforme limites do Git; revisor avalia antes de retomar. Prazos de retenção, matriz nominativa de acesso e procedimento aprovado estão **pendentes**, não inventados.

## 17. Dicionário operacional de métricas — AIL-05/06

**Unidade:** execução comparável = par `(case_id, case_version, baseline_manifest_hash, candidate_sha, run_id)`; oportunidade de reincidência = `(causa_raiz_aprovada, processo, entrega_id, janela)`. Uma mesma falha com múltiplos relatos na mesma entrega/janela é deduplicada; reabertura do mesmo defeito sem correção homologada não é reincidência nova. Categorias/causas devem ser validadas pelo revisor; eventos inconclusivos e não comprovados fora do numerador, explicitamente contados em separado.

| Medida | Numerador / denominador | Janela, exclusões e decisão |
|---|---|---|
| Reincidência (%) | oportunidades comparáveis **com ≥1** falha repetida confirmada após correção aprovada / todas oportunidades comparáveis observadas | 30 dias após aprovação, estratificar severidade; excluir reaberturas sem nova correção, duplicatas e oportunidades sem exposição |
| Frequência de falhas | ocorrências confirmadas / oportunidades | pode superar 100% em razão de múltiplos eventos; não chamar de taxa de reincidência |
| Aprovação válida (%) | casos com resultado pass / casos **validamente executados** (pass + fail) | por manifest/SHA, estratificada por família/risco |
| Cobertura (%) | casos elegíveis do manifesto com resultado válido / todos casos elegíveis e aprovados do manifesto | cobertura de segurança crítica = 100% proposta para futura validação; cobertura geral mínima candidata 95%, sujeita a aceite da Direção |
| Regressão pareada (%) | casos válidos `pass` no baseline e `fail` na candidata / casos `pass` no baseline reexecutados validamente sob mesma versão de caso e oráculo | listar caso adicionado/removido, troca de fixture/oráculo e falha ambiental em separado; não misturar bases |
| Escapes (%) | entregas observadas que tiveram ≥1 defeito comprovado pós-aceite / entregas aprovadas com janela de observação completa | janela de maturação candidata 30 dias; não observadas ficam fora, declaradas |
| Evidência auditável (%) | execuções elegíveis com fonte+SHA+regra+oráculo+resultado / execuções elegíveis | `N/A` para população zero |

**Contabilidade de execução obrigatória:** `eligible`, `selected`, `attempted`, `valid_pass`, `valid_fail`, `skipped`, `invalid`, `blocked`, `inconclusive`, com classes mutuamente exclusivas no desfecho por caso; `executed_valid=valid_pass+valid_fail`. Para a cobertura, skipped/invalid/blocked/inconclusive continuam no denominador elegível e não são sucesso. Exemplo: elegíveis 8; 5 pass, 1 fail, 1 skipped, 1 blocked → 6 válidos, aprovação 5/6=83,33%; cobertura 6/8=75%; **no-go de cobertura**, apesar do pass rate. Reincidência exemplo: 2 de 10 oportunidades com falha repetida =20%; três relatos duplicados na primeira oportunidade não viram três falhas. Regressão: 1 fail de 4 casos que passavam e foram pareadamente reexecutados =25%; dois casos baseline pass não reexecutados devem constar como lacuna de cobertura, não entrar na fração de regressão. **Gatilho incondicional de no-go:** vazamento de segredo, falha crítica, violação de autorização, modificação indevida de golden; score agregado nunca neutraliza bloqueio. Denominador zero → N/A, jamais 0%. Comparações em amostras pequenas são descritivas, não inferência causal.

## 18. Plano incremental, custos e responsabilidades — AIL-08/10

| Fase futura (nenhuma autorizada) | Trabalho/estimativa candidata para dimensionamento, não custo constatado | Condição de parada/aceite |
|---|---|---|
| F0 conciliação documental | 2–4 h humanas para decisões/fontes + revisão separada | bloqueio se regra aplicável/owner ainda ambíguo |
| F1 curadoria 5–8 casos sintéticos | curadoria 4–10 h + revisão independente 2–5 h + retrabalho observado à parte | 100% com primária, SHA, oráculo, classes e parecer |
| F2 runner local determinístico | implementação 4–8 h + revisão 2–4 h + execução/análise 1–3 h | sem rede/segredos, igualdade reprodutível, positivos/negativos |
| F3 eventual CI | engenharia 3–8 h + auditoria 2–4 h + minutos/storage efetivos cobrados pelo plano | controles de §14 comprovados; aprovação separada |
| F4 manutenção | registrar horas de cada rodada (curadoria, revisão, execução, análise, correção, manutenção) | revisar custo-benefício após duas rodadas comparáveis |

**Tetos candidatos a decidir antes de F1:** até 8 casos, no máximo 20 horas humanas totais na primeira experiência local, nenhum gasto incremental em API sem orçamento específico, nenhuma execução em CI sem cotas e preços confirmados. Se atingir 80% do orçamento, revisar escopo; ao atingir teto ou ocorrer incidente, parar, registrar custo e solicitar nova decisão. Infraestrutura/armazenamento, GitHub Actions, API e tempo humano são rubricas separadas; custos de plano atual **não verificados**. Estimativas são hipóteses de planejamento, não compromisso nem gratuidade.

**RACI enxuto:** executor prepara fixture/documentação e relata execução, mas não aprova o próprio oráculo; revisor independente valida evidência, esperado e regressão; Orquestrador triagem, deduplicação, registro e encaminhamento sem homologar; Direção decide normas, orçamento, exceções, autorização de piloto/CI/publicação/merge e arbitragem institucional. Infra fornece evidência de controle sem revelar segredos. Triagem candidata até 2 dias úteis após registro, sujeita à capacidade; alto/crítico implica suspensão imediata sem esperar SLA. Falha crítica/privacidade/permissão suspende; mudança técnica futura exige revert no PR próprio e baseline anterior verificado; golden contestado é **quarentenado** (não apagado), com motivo e SHA, e eventual retirada depende de parecer e decisão. Arquivar caso apenas com histórico preservado, nunca para melhorar indicador.

## 19. Pendências explícitas da Direção e decisão de encerramento documental

1. DEC-AIL-01: decidir vigência/alcance de POL/QG/SEC/5S e integração com DEC-GOV-A/B/D, sem homologação presumida.
2. DEC-AIL-02: designar dono de segurança/infra e autorizar inspeção administrativa específica; **não autoriza CI**.
3. DEC-AIL-03: aprovar ou rejeitar protocolo, papéis, baseline, definição de cobertura e retenção por classe.
4. DEC-AIL-04: estabelecer orçamento/tetos, responsável por custos e eventual autorização **separada** do piloto offline, condicionada a nova revisão.
5. DEC-AIL-05: decidir eventual PR técnico, controles reais e eventual ativação de workflow **somente depois** de resultados verificáveis.
6. DEC-AIL-06: decidir merge documental somente após parecer focal, sem vincular a implantação.
7. DEC-AIL-07: confirmar proprietário e versão canônica de artefatos GitHub/Obsidian/Drive/Sheets em alinhamento com GT-GOV-002.

**Classificação ao fim desta rodada:** controles GitHub, gates operacionais, aprovação de normativos, retenção, orçamento real, baseline e testes **não verificados/não autorizados**. O tratamento dos 11 achados é **documental proposto**, aguardando revalidação independente focal; não se afirma encerramento de risco operacional. Proibidos merge, publicação, criação de workflow, acesso a cliente, fine-tuning e qualquer ativação.
