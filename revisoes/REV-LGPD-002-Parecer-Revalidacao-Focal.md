---
id: REV-LGPD-002
tipo: parecer-independente-revalidacao-focal
versao: 0.1.0
status: emitido
resultado: apto-encerramento-documental-para-deliberacao
data: 2026-10-10
pr_origem: 16
commit_revisado: b6c6196abfaf1c6e8d639a02ff95f670594c8b54
pr_parecer_historico: 18
publicacao_autorizada: nao
captacao_autorizada: nao
merge_autorizado: nao
---
# REV-LGPD-002 — Revalidação independente focal GT-LGPD-001 v0.2.0

> **APTO AO ENCERRAMENTO DOCUMENTAL, SUJEITO À DECISÃO DA DIREÇÃO. NÃO APTO PARA PUBLICAÇÃO, CAPTAÇÃO, DECLARAÇÃO DE CONFORMIDADE OPERACIONAL OU MERGE.**

## Objeto, método e limites
PR de execução #16 https://github.com/gentestsai-sudo/gentests-os/pull/16, **Draft e aberta** no commit exato `b6c6196abfaf1c6e8d639a02ff95f670594c8b54`. Foram recuperados os quatro arquivos GT-LGPD-001 a 004 v0.2.0 e o parecer REV-LGPD-001 na PR #18 (baseada na branch histórica de execução). A PR #16 altera quatro documentos Markdown, sem edição do site. Revalidação focada exclusivamente nos sete apontamentos e riscos regressivos, sem inspecionar controles administrativos de FormSubmit, Gmail, Cloudflare, CRM, dados reais, deploy, navegador ou consentimentos praticados. Referência normativa oficial da Res. 15/2024 conferida no portal ANPD; Res. 2/2022 atualizada confere prazo diferenciado.

## Matriz individual
| ID | Severidade original | Estado documental | Evidência direta v0.2.0 | Pendência residual para operação |
|---|---|---|---|---|
| LGPD-REV-01 | Alta para lançamento | **Resolvido documentalmente** | GT-LGPD-001 §§7–8: checklist de identidade jurídica do controlador, canal, contratos/fornecedores, países, subprocessadores, papéis e mecanismo internacional; estados PENDENTE sem inventar dados | Prova de controlador/canal, relação com cada prestador, geografia e instrumentos jurídicos. Bloqueia publicação/coleta, não diagnóstico. |
| LGPD-REV-02 | Alta para ativação | **Resolvido documentalmente** | GT-LGPD-001 §9; GT-LGPD-002 §9: matriz específica contato, download direto, entrega e-mail, marketing, prospecção B2B, logs, direitos/incidentes com dados mínimos, arts. 7º e justificativas condicionadas | Bases finais e transparência por fluxo exigem fatos e validação jurídica/direção. Art. 7º V não é automaticamente aplicável ao guia gratuito. |
| LGPD-REV-03 | Média jurídica | **Resolvido documentalmente** | GT-LGPD-003 §7: acesso simplificado, declaração completa, outros direitos e notificação de incidentes em tabela; prazos 15 dias, regra geral 3 dias úteis e hipóteses de dobro específicas | Elegibilidade pequeno porte, início/contagem, critérios de notificação e exceções validados antes do uso, com atualização normativa. |
| LGPD-REV-04 | Média | **Resolvido documentalmente** | GT-LGPD-004 §6: 6 requisitos para futuro ajuste do FormSubmit/checkbox, campo livre, antiabuso, transparência e ensaios sintéticos | Nenhum formulário alterado, entrega e acessibilidade não testadas; trabalho próprio no site. |
| LGPD-REV-05 | Média | **Resolvido documentalmente** | GT-LGPD-003 §8: matriz por FormSubmit, Gmail, CRM, prova de consentimento, supressão, Drive, logs, backups e protocolos; revogação, propagação e exceções | Fixar períodos/critério determinável e validar eliminação em sistemas reais; backups e opt-out de campanhas futuras dependem de testes. |
| LGPD-REV-06 | Média | **Resolvido documentalmente** | GT-LGPD-004 §7: confronto direto vs e-mail mínimo, vantagens, custos, risco, LP-01–12 e opt-in promocional independente | Modalidade permanece decisão da Direção; LP-01–12 apenas candidatos, não executados. |
| LGPD-REV-07 | Baixa | **Resolvido documentalmente** | GT-LGPD-001 §5; GT-LGPD-003 §7: link oficial do ato Res. 15/2024, art. 14 II da Res. 2/2022 atualizado, canal ANPD e cautela de vigência | Conferir texto consolidado vigente antes de operar; documentação corretamente identificada. |

## Análise focal
**Finalidades e bases legais.** O desenho distingue resposta espontânea, entrega de guia gratuito, opt-in promocional, prospecção B2B, logs e atendimento legal. Bases candidatas não se confundem com autorização já concedida. O legítimo interesse é condicionando à necessidade/balanceamento; não se condiciona guia à autorização de marketing.

**Prazos.** Conferidos os dispositivos de pequeno porte Res. 2/2022 arts. 14–15 e Res. 15/2024 sobre comunicação de incidente. A tabela corretamente evita um único SLA para todos os direitos; prazos concretos somente após qualificação da operação e enquadramento. A resposta imediata a incidentes não é adiada pelo prazo de comunicação.

**Formulário e retenção.** Requisitos são especificação futura, não reparo do site. Revogação comercial deve propagar-se a listas e envios agendados, preservando somente supressão mínima justificada. Prazos reais, localizações de dados e configurações dos fornecedores continuam não verificados, sem falso aceite.

**Estratégia orgânica.** As duas arquiteturas permanecem elegíveis para deliberação: download direto minimiza dados, mas não identifica automaticamente lead; entrega por e-mail pode ter propósito restrito à entrega, com marketing opcional separado, transparente, revogável e não pré-selecionado. Nem consentimento para resposta, nem solicitação do guia autorizam campanhas automaticamente.

**Governança.** As políticas POL-004/SEC-AI-001 ainda são tratadas como propostas. Não foram inventados CNPJ, controlador, DPO, contratos, mecanismos de transferência ou conformidade. Ausência de provas reais não equivale a ausência de controles.

## Regressões, ressalvas e bloqueios
**Nenhuma regressão material alta/crítica identificada no delta documental.** Dois ajustes de precisão não bloqueantes: (a) a remissão GT-LGPD-001 §7 ao texto oficial é rastreável mas, na aplicação futura, a equipe deverá confirmar consolidação normativa e exceções; (b) retenção ainda traz eventos e responsabilidades candidatos, devendo ser tornada determinável antes de qualquer dado novo. A avaliação NÃO verificou nenhum sistema real.

**Impedimentos ao encerramento da fase documental:** nenhum, desde que a Direção reconheça o escopo de diagnóstico e proposta, não de validação operacional.

**Impedimentos efetivos à publicação/captação:** identificação e canal do controlador; bases legais finalizadas; transparência/aviso aprovado; fornecedores e transferências; retenção e supressão verificáveis; arquitetura escolhida; testes sintéticos do site, LP aplicáveis, autorização institucional e revisão do go-live.

## Decisão e encaminhamento
Recomendo **aceite/encerramento documental** de GT-LGPD-001 a 004 v0.2.0 e REV-LGPD-001 achados LGPD-REV-01 a 07 como **resolvidos no desenho**, condicionado à decisão da Direção. Não repetir auditoria integral desses documentos. O Orquestrador deve criar atividades futuras limitadas aos controles e decisões do lançamento do guia GT-MKT-CNQ-001, evitando burocracia duplicada. Não se autoriza merge, publicação, formulário, coleta de dados, piloto com dados reais, homologação de políticas ou afirmação de adequação integral à LGPD.

Fontes oficiais externas consultadas: https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/documentos/rcis___anonimizado_final_ocultado_2_parte3.pdf ; https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-2-de-27-de-janeiro-de-2022 .
