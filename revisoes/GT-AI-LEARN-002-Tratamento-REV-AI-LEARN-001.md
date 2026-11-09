---
id: GT-AI-LEARN-002
tipo: tratamento-parecer-independente
versao: 0.1.0
status: proposta-em-revalidacao-focal
data: 2026-10-10
origem: REV-AI-LEARN-001
objeto: GT-AI-LEARN-001-v0.2.0
implementacao_autorizada: nao
merge_autorizado: nao
---
# GT-AI-LEARN-002 — Tratamento controlado do REV-AI-LEARN-001

> Respostas documentais aos 11 apontamentos do parecer emitido na PR #9. **Nenhum achado é declarado tecnicamente resolvido, homologado ou encerrado pelo executor.** Revisor independente deve confirmar o fechamento **documental**, sem auditoria integral novamente. A presente PR permanece Draft.

## Referências e estado
- Proposta corrigida: `revisoes/GT-AI-LEARN-001-Diagnostico-Aprendizado-Operacional.md` v0.2.0, PR #8.
- Parecer original **preservado sem alteração**: `revisoes/REV-AI-LEARN-001-Parecer-Aprendizado-Operacional.md`, PR #9, commit examinado `37d6fc810e5925702690180f31975f0bae9b338d`.
- Governança: `revisoes/REV-GOV-001-Parecer-Diagnostico-Consolidacao.md` na PR #7 e `revisoes/GT-GOV-001-Diagnostico-Consolidacao-Governanca.md` v0.2.0, `revisoes/GT-GOV-002-Tratamento-REV-GOV-001.md` na PR #6.
- Limite de escopo: diagnóstico e especificação; controles reais, configuração administrativa, execução de testes e autorizações permanecem pendentes.

## Matriz dos 11 achados

| ID | Gravidade | Resposta executada (seção GT-AI-LEARN-001) | Estado para revalidação focal | Bloqueio futuro |
|---|---|---|---|---|
| AIL-01 | Alta | §13: quatro dimensões independentes; matriz POL/QG/SEC/5S; decisões DEC-GOV | Tratado documentalmente, **pendente de confirmação independente** | homologação e autorização específicas |
| AIL-02 | Alta | §14: checklist de branch, roles, token, runner, Actions, logs e ensaios | Tratado documentalmente; **controles não verificados** | CI/implementação |
| AIL-03 | Alta | §15: elegibilidade cumulativa, oráculo independente, disputa, versionamento e hash; sem autopromoção | Tratado documentalmente, **sem golden aprovado** | curadoria/uso |
| AIL-04 | Alta | §16: classes, finalidade, acesso, descarte, incidentes e injection | Tratado documentalmente; **retenção e permissões não aprovadas** | dados reais/piloto |
| AIL-05 | Média | §17: chave, oportunidade, deduplicação, janelas, exclusões e exemplos | Tratado documentalmente; validar semântica | indicador operacional |
| AIL-06 | Média | §17: outcomes separados, cobertura, regressão pareada e falha crítica | Tratado documentalmente; limite 95% candidato | gate real |
| AIL-07 | Média | §15: manifesto com SHA, estado de regra, grupos development/regression/holdout e histórico de exposição | Tratado documentalmente; nenhum manifesto criado | baseline |
| AIL-08 | Média | §18: fases, horas por atividade, tetos e stop criteria; custo não zero | Tratado documentalmente; **custos reais desconhecidos** | gasto/piloto |
| AIL-09 | Média | §13: correlação GOV-01–13 e REV-GOV-01–03; GT-GOV-002 v0.2 | Tratado documentalmente; decisões GOV pendentes | norma/fonte canônica |
| AIL-10 | Baixa | §18: responsabilidades por função, suspensão, revert, quarentena e escalonamento | Tratado documentalmente, SLA candidato | operação |
| AIL-11 | Baixa | §5/15: apenas JSON e Python stdlib na arquitetura inicial | Tratado documentalmente | parser futuro |

**Critério de estado:** "tratado documentalmente" quer dizer que há especificação e encaminhamento no texto, **não** que o risco foi mitigado em execução. Nenhum status original do parecer foi modificado, nenhuma RNC foi encerrada.

## Dependências bloqueantes e decisões

- **Para parecer documental focal:** verificar alinhamento entre §§13–19 e os achados, correção de contradições, status normativos, exatidão dos cálculos/exemplos e ausência de promoção tácita. A falta de acesso administrativo não bloqueia esta revalidação **documental**, desde que declarada.
- **Para piloto local futuro:** exigir aprovação explícita da Direção, vigência de critérios aplicáveis, evidência de segregação real dos papéis, classes de dados aprovadas, conjunto sintético curado e baseline, teto de esforço/orçamento e revisão independente de PR técnico próprio. Não executar enquanto AIL-01/03/04 estiverem sem decisão e verificação pertinente.
- **Para CI futuro:** além do piloto local, comprovar controles de AIL-02 por evidência administrativa e testes negativos/positivos; autorização técnica expressa posterior.
- **Para merge/publicação:** parecer focal favorável não substitui autorização expressa da Direção; não ocorre nesta rodada.

## Evidências a exigir, sem inventar testes

| Evidência | Situação no encerramento da execução |
|---|---|
| Commit e diff do Markdown v0.2.0 | presentes na PR #8 após commits desta rodada |
| Versões/SHAs originais dos pareceres | referenciados, preservados |
| Prova de branch protection, tokens, runners, secrets e Actions | **não verificada** |
| Execução de `unittest`, CI ou Evals | **não executada** |
| Manifesto de golden, caso aprovado ou holdout | **não criado**, desenho somente |
| Autorização institucional de políticas, piloto, CI, merge e publicação | **não concedida nesta rodada** |
| Preço do plano GitHub, cota de Actions e custo humano observado | **não verificados** |
| Dados reais de clientes | **não utilizados** |

## Solicitação objetiva ao revisor independente

Revalidar **apenas** AIL-01–11 no delta v0.1→v0.2 e eventuais regressões materiais altas/críticas. Avaliar, em especial: distinção política proposta/aprovação/enforcement/teste; aderência a GOV-01–13 e REV-GOV-01–03; proteção contra golden contaminado; completude do checklist administrativo; fórmulas com denominadores e exemplos; riscos S0–S3; orçamento/tetos e decisões expressas. Classificar cada achado como `fechado documentalmente`, `parcial` ou `aberto` com fonte, sem confundir revisão documental com autorização de piloto. **Não solicitar auditoria completa**, salvo novo risco alto/crítico fundamentado.

## Controle da rodada

Somente dois arquivos da PR #8 devem ser alterados/criados nesta rodada: o diagnóstico v0.2 e este tratamento. Nenhum arquivo em `.github/workflows/`, políticas, permissões, contratos, documentos do revisor, identidades ou artefatos de cliente deve ser modificado. Preservar histórico Git, PR Draft, e não realizar merge.
