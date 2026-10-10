---
id: REV-AI-LEARN-001
tipo: parecer-independente
versao: 0.1.0
status: parecer-para-deliberacao
data: 2026-10-10
objeto: GT-AI-LEARN-001
objeto_commit: 37d6fc810e5925702690180f31975f0bae9b338d
objeto_pr: 8
aprovacao_direcao: pendente
implementacao_autorizada: nao
publicacao_autorizada: nao
---
# REV-AI-LEARN-001 — Parecer independente sobre aprendizado operacional e Evals

> **Resultado: APROVADO COM RESSALVAS PARA EVOLUÇÃO DOCUMENTAL. NÃO APROVADO PARA PILOTO/IMPLEMENTAÇÃO, MERGE OU PUBLICAÇÃO.** Elegibilidade futura **condicional**, após correções, parecer de revalidação e decisão expressa da Direção. Este parecer não homologa qualquer política ou controle técnico.

## 1. Identificação, método e limitações

Objeto: `revisoes/GT-AI-LEARN-001-Diagnostico-Aprendizado-Operacional.md`, PR #8, commit `37d6fc810e5925702690180f31975f0bae9b338d`. Revisão documental do texto da proposta, conferência direta na `main` de `POL-001` (`00-Constituicao/Regras-de-Ouro.md`), `POL-002` (`Hierarquia-e-Conflitos.md`), `POL-003` (`Matriz-de-Permissoes.md`), `POL-004` (`Seguranca-e-Dados.md`), `SEC-AI-001`, `QG-001`, `GOV-5S-001`, `Gestao-de-Nao-Conformidades.md` e `Indicadores-de-Governanca.md`; comparação com GT-GOV-001 na branch da PR #6 e com descrição da PR #7.

**Limites:** não se executaram scripts/Evals, não se inspecionaram configurações administrativas, proteção de branches, permissões de tokens, logs de CI, faturamento, todos os contratos de agentes, todas as versões históricas nem o conteúdo integral do parecer da PR #7 (arquivo não encontrado na `main`). Portanto não há certificação de segurança operacional, concordância integral com REV-GOV-001 ou confirmação de cobertura de todos os artefatos. Achados de ausência de evidência são classificados como *não verificável*, não como prova de ausência de controle.

## 2. Síntese técnica

A proposta acerta ao distinguir aprendizado operacional de fine-tuning, separar casos candidatos de goldens aprovados, proibir autopromoção de regras, favorecer Python stdlib e revisão por PR, explicitar incerteza do custo e reconhecer a independência imperfeita entre agentes do mesmo modelo. O desenho é **plausível** para teste local offline de regras determinísticas com dados sintéticos e revisão humana; ainda é uma **arquitetura conceitual**, não uma execução demonstrada.

**Conformidade documental:** compatível em intenção com POL-001–004, SEC-AI-001, QG-001 e GOV-5S-001. Todos estes documentos examinados têm `status: proposta`; não é correto declarar conformidade normativa homologada. Matriz POL-003 reserva mudança de governança à Direção; revisão não é autorização. QG-001 prevê prevalência do nível de risco mais alto e evidência de aprovação; níveis QG-L/M/H do documento avaliado só poderão ser aplicados institucionalmente após decisão. SEC-AI-001 exige validação técnica dos controles, não apenas Markdown.

## 3. Achados itemizados

| ID | Gravidade | Achado e evidência | Correção / critério verificável |
|---|---|---|---|
| AIL-01 | **Alta — bloqueante para piloto** | Políticas POL-001–004, QG-001, SEC-AI-001 e GOV-5S-001 estão em `proposta` na main; GT-GOV-001, PR #6, GOV-02/GOV-07, reconhece ausência de homologação e prova de enforcement. GT-AI-LEARN-001 §§3,10 admite dependência, mas ainda usa gates como desenho. | Anexar matriz de dependências: regra de desenho vs norma aprovada vs controle configurado vs teste executado; obter decisões expressas sobre normativos aplicáveis e acesso; não bloquear avaliação **documental** por falta de homologação, mas bloquear execução de piloto até autorização específica. |
| AIL-02 | **Alta — bloqueante para CI** | §§2,8,9 reconhecem não terem verificado branch protection, Actions, tokens e isolamento. Repositório privado não prova menor privilégio. | Checklist com evidência de permissões efetivas, revisores obrigatórios, direitos de escrita, token read-only, proteção de branch, configuração de runners, artefatos/logs e teste de PR não confiável; autorização técnica antes de qualquer workflow. |
| AIL-03 | **Alta — bloqueante para goldens** | §§4–6 exigem curadoria, mas não fixam protocolo de disputa do oráculo, critérios de elegibilidade, congelamento de baseline e segregação de identidade quando o mesmo modelo atua em dois papéis. | Formalizar gate de curadoria: evidência primária e commit, regra vigente naquele momento, fixture sanitizada, oráculo independente, dois exemplos contrastivos quando aplicável, divergência escalada, decisão humana, hash de dataset e proibição de alterar goldens para melhorar score. |
| AIL-04 | **Alta — bloqueante para uso de dados** | §§5,9 propõem minimização e defesa contra prompt injection, mas não há demonstração de política de retenção por classe, autorização de uso, controle de acesso nem plano de resposta ao incidente na suíte. | Definir tabela por classificação: origem, finalidade, base/autorização, sanitização, retenção/exclusão, acesso, segredo, logs e incidente. Testar payload malicioso sintético como **dado**, sem executar ferramentas externas; verificar antes de qualquer material real de cliente. |
| AIL-05 | **Média** | §7: reincidência usa “oportunidades elegíveis” e escapes usam entregas “observadas”, sem especificação operacional de unidade, atribuição causal, deduplicação e maturação. | Dicionário de métricas com evento, chave de unicidade, população, janelas, exclusões, N/A, severidade, intervalos pequenos e exemplos calculados. Para reincidência, fixar se o numerador conta categorias por oportunidade ou ocorrências; impedir numerador maior que denominador para taxas. |
| AIL-06 | **Média** | §7: pass rate é definido sobre executados e regressão sobre reexecutados, mas uma suíte que pula falhas pode melhorar artificialmente o score. | Reportar elegíveis, selecionados, executados, skipped, inválidos, bloqueados e inconclusivos; impor cobertura mínima por risco; calcular regressão pareada com manifestos de baseline imutáveis e enumerar casos removidos/adicionados. Incidentes críticos devem bloquear independentemente do agregado. |
| AIL-07 | **Média** | §§4,6: exemplos vêm de PRs e pareceres ainda abertos, podendo refletir versões antigas ou achados contestados; há risco de leakage entre treino operacional e avaliação. | Manifesto da proveniência com PR, SHA e data da política; não converter parecer em verdade automaticamente; separar conjuntos de desenvolvimento, regressão congelada e holdout independente; registrar quando o agente teve acesso às respostas. |
| AIL-08 | **Média** | §8 prevê 5–8 casos, 4–10 h de curadoria exploratória e custo monetário incremental R$0 sob condições; esforço técnico de implementação, revisão, APIs e CI não estão orçados. | Estimar por atividade (curadoria, execução, análise, retrabalho, manutenção, revisão e custos de infraestrutura) após amostra real; estabelecer teto de horas, orçamento e condição de parada; evitar prometer custo zero. |
| AIL-09 | **Média** | §§10–11 vinculam a arquitetura a GOV-001/REV-GOV-001; conteúdo completo de REV-GOV-001 não foi confirmado nesta revisão (PR #7 informa 13 achados e três recomendações). | Ler documento exato da PR #7 e montar rastreabilidade GOV-01–13 / recomendações → decisões → controles da suíte; suspender taxonomia e fonte canônica definitiva até conciliação. |
| AIL-10 | **Baixa** | §10 propõe fases e limites, mas não explicita proprietário operacional, SLA de triagem, arquivamento e gatilho de rollback por severidade. | Acrescentar RACI leve e critérios de suspensão, rollback e retirada de caso, sem cerimônia duplicada; manter aderência ao 5S. |
| AIL-11 | **Baixa** | §5 permite JSON **ou YAML**, enquanto o piloto visa Python stdlib; YAML demanda dependência externa ou parser adicional. | Escolher JSON no piloto; YAML apenas mediante justificativa e gestão de dependência. |

## 4. Revisão de arquitetura e independência

GitHub + JSON + Python `json/unittest/pathlib` atende validações estáticas offline sem aquisição de ferramentas. A reprodutibilidade depende de versões fixadas, input imutável, fixtures positivas/negativas, isolamento e testes de falha. O runner de avaliação não deve poder alterar os próprios oráculos. **Dois chats/agentes usando a mesma família de modelo não equivalem, por si sós, a revisores independentes**. Registrar papel, autor efetivo, executor, revisor e aprovador; usar oráculo determinístico ou arbitragem humana independente para decisões críticas.

Prompts e documentos externos devem ser classificados como **dados não confiáveis**. Acesso do runner deve ser mínimo, idealmente sem rede e sem segredos durante o piloto local; `pull_request_target` com código não confiável não pode receber token privilegiado. Esses são critérios de projeto, **não controles verificados em operação**.

## 5. Métricas e critérios de regressão recomendados

- **Pass rate** = aprovações / execuções válidas; sempre publicar também elegíveis, tentados, skipped, inválidos e N/A, por severidade/família.
- **Cobertura da suíte** = casos elegíveis executados / casos elegíveis aprovados no manifesto congelado; explicar cada omissão.
- **Regressão pareada** = casos que passaram no baseline e falharam na candidata / casos que passaram no baseline e foram validamente reexecutados; reportar também diferenças de composição do conjunto.
- **Reincidência** = oportunidades com pelo menos uma falha reincidente confirmada / oportunidades comparáveis observadas após correção; se preferir contagem de eventos, nomear como frequência e não porcentagem. Deduplicar por causa e janela.
- **Autorização** = ações sensíveis autorizadas previamente / ações sensíveis observadas; registrar qualquer ação não autorizada como incidente bloqueante independentemente do percentual.
- Falha crítica de segurança, segredo exposto, alteração não autorizada de golden ou autopermissão: **no-go imediato**, mesmo com pass rate alto. Rodadas pequenas não demonstram significância nem melhoria causal.

## 6. Elegibilidade do piloto e riscos residuais

**Status atual:** elegível **em tese para planejamento e correções documentais**, **não elegível para execução**. Um piloto local futuro deve ser restrito a 5–8 casos sintéticos, oráculos determinísticos, sem rede/segredos, sem integração de produção, com custo/tempo limitados e decisão expressa de Direção. Exigir antes do go: (a) resolução de AIL-01 a AIL-04, (b) dicionário de métricas e manifesto de baseline, (c) conciliação com PRs #6/#7, (d) revisão independente da implementação em PR próprio, (e) autorização humana específica.

**Riscos residuais, mesmo após correções:** sobreajuste aos exemplos, falsa sensação de qualidade por taxa agregada, revisão enviesada pelo mesmo modelo, drift de políticas e evolução dos custos humanos. Mitigações: holdout, revisão amostral, versionamento de regra/oráculo, reporte estratificado e revisão periódica de custo-benefício.

## 7. Decisão e restrições

**Parecer:** aprovado com ressalvas **somente para evolução documental**. Correções recomendadas e revalidação independente antes de recomendar piloto. **Não aprovado para implementação, criação de workflows, publicação, mudança de políticas/permissões, merge ou adoção como norma.** Permanecem pendentes os controles administrativos não verificados e a aprovação expressa da Direção. Nenhum teste foi executado neste parecer.

Referências:
- [GT-AI-LEARN-001 — PR #8](https://github.com/gentestsai-sudo/gentests-os/pull/8), commit `37d6fc810e5925702690180f31975f0bae9b338d`;
- [GT-GOV-001 — PR #6](https://github.com/gentestsai-sudo/gentests-os/pull/6);
- [REV-GOV-001 — PR #7](https://github.com/gentestsai-sudo/gentests-os/pull/7);
- Documentos normativos e processos citados na seção 1, consultados na `main` em 2026-10-10.
