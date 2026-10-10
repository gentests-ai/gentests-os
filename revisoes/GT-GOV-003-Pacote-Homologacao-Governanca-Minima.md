---
id: GT-GOV-003
tipo: pacote-de-deliberacao
versao: 0.1.0
status: proposta-para-revisao-independente
data: 2026-10-10
aprovador: Direcao
homologacao: pendente
implementacao: nao-autorizada
---
# GT-GOV-003 — Pacote de Homologação da Governança Mínima

> **DOCUMENTO PREPARATÓRIO — NÃO É HOMOLOGAÇÃO.** Nenhuma política, permissão técnica, publicação, merge, gasto ou alteração externa está autorizada por este texto. Escopo exclusivamente documental. Diagnóstico GT-GOV-001 v0.2.0 declarado apto para encerramento documental no REV-GOV-002, PR #10; não repetir essa auditoria.

## 1. Fontes e método
Snapshot da `main` consultado em 10/10/2026; políticas abaixo lidas individualmente por conteúdo/YAML. Histórico e tratamento: [GT-GOV-001 e GT-GOV-002, PR #6](https://github.com/gentestsai-sudo/gentests-os/pull/6); [REV-GOV-001, PR #7](https://github.com/gentestsai-sudo/gentests-os/pull/7); [REV-GOV-002, PR #10](https://github.com/gentestsai-sudo/gentests-os/pull/10). REV-GOV-002 revalidou commit `fba583fe222e11565d90057b228d721e2cb240ad`, constatou ausência de bloqueio para **encerramento do diagnóstico**, não homologação de normas. Usar matrizes GOV-01–13 e REV-GOV-01–03 em GT-GOV-002 por referência, sem duplicar auditoria.

**Dimensões separadas:** (a) texto proposto, (b) decisão humana por versão/alcance, (c) configuração técnica verificada e (d) testes de operação. Aprovar texto não prova enforcement; teste verde não aprova política; documento referenciado por índice não é homologado.

## 2. Inventário de prontidão por versão e blob da main

| Norma e caminho | Versão/status observado | Blob SHA observado | Prontidão de deliberação e ressalva |
|---|---|---|---|
| POL-001 `00-Constituicao/Regras-de-Ouro.md` | 1.0.0 / proposta | `1c3b515971b8b5c0b890e350b7c1cd1973116a85` | **Deliberável**: princípios claros; Direção deve fixar escopo e vigência |
| POL-002 `00-Constituicao/Hierarquia-e-Conflitos.md` | 1.0.0 / proposta | `af0f2fe1012a39865dc65285e5db40557cde505e` | **Deliberável**: hierarquia clara; procedimento de exceção precisa respeitar lei/contrato |
| POL-003 `00-Constituicao/Matriz-de-Permissoes.md` | 1.0.0 / proposta | `7bf11bc753244ddf4164750c3e764b28d8704de1` | **Ajuste objetivo recomendado antes da homologação plena:** falta explicitação de Orquestrador/Executor/Revisor; matriz não prova acessos reais |
| POL-004 `00-Constituicao/Seguranca-e-Dados.md` | 1.0.0 / proposta | `2b0039e64f3da2894aa390c383f0cfbd9b900030` | **Deliberável em princípios**, condicionado a plano posterior de retenção/acessos/incidente e efetividade |
| QG-001 `00-Constituicao/Quality-Gates/QG-001-Politica.md` | 0.1.0 / proposta | `f58d0d10e3718379b6dd0311056b5e0cc3754430` | **Deliberável com interpretação explícita:** QG-L/M/H por maior risco; QG-H requer revisão independente e autorização humana aplicável |
| QG-CORE `00-Constituicao/Quality-Gates/QG-CORE-Obrigatorio.md` | 0.1.0 / proposta | `a8d7d0992093d97b67ade38b4eb33349abbab99e` | **Deliberável dependente de QG-001**: N/A justificado e evidência real, não checkbox |
| QG-STR-001 `00-Constituicao/Quality-Gates/QG-STR-001-Disciplina-Estrategica.md` | 0.1.0 / proposta | `6cd8dda92cff3f97e3d07067a4a91413d4e24a14` | **Deliberável dependente de QG-001**: aplicar só a decisões estratégicas; não criar gate duplicado |
| SEC-AI-001 `00-Constituicao/SEC-AI-001-Seguranca-Confiabilidade-Agentes.md` | 0.1.0 / proposta | `5a3a7067a03041011ecbef3da8cc0f82df5a366d` | **Deliberável em princípios**, com plano separado de enforcement e resposta a incidentes |
| GOV-5S-001 `00-Constituicao/Excelencia-Enxuta-5S.md` | 0.1.0 / proposta | `8759d58860dd38402767685861947d6c3c6c5c4f` | **Deliberável**: reusar fluxos e não duplicar checklists; aplicação prospectiva |

**Prontidão não é homologação.** A Direção poderá decidir separadamente por documento: aprovar versão com escopo, aprovar com ajuste textual submetido à nova versão, adiar com motivo ou rejeitar. Nenhum campo deste pacote preenche uma decisão em seu nome. POL-003 é prioridade de ajuste controlado, sem mudar seu arquivo nesta PR.

## 3. Permissões documentadas e fronteiras propostas — GOV3-02

POL-003 v1.0.0 já descreve Comercial, Marketing, QA, Financeiro e Auditor; funções Orquestrador/Executor/Revisor não têm linha equivalente explícita. Proposta interpretativa para deliberação, **não concessão de acesso**:

| Papel | Pode preparar/ler no escopo autorizado | Deve escalar / não pode autoaprovar |
|---|---|---|
| Orquestrador | triagem, dependências, coordenação e consolidação de estado com evidência | não homologa, não faz merge autônomo, não amplia permissão nem substitui parecer |
| Executor | elaborar artefato em branch/escopo autorizado, evidenciar alterações | não aprova própria saída, não muda política nem executa ação externa sem autorização |
| Revisor independente | ler fontes e diffs, classificar risco, emitir parecer separado | não altera artefato revisado nem concede decisão institucional |
| Auditor | inspecionar por amostragem controles, logs e divergências | não se torna executor ou autocertificador da operação avaliada |
| Comercial | rascunhar abordagem; atualizar CRM se autorizado nos termos POL-003 | envio externo requer autorização delimitada; não aprovar preço/contrato |
| Marketing | preparar campanha e material | publicar, alterar identidade ou enviar externamente somente conforme autorização explícita e fonte de marca |
| QA | preparar/rodar testes exclusivamente em ambiente permitido | não acessar produção ou dados sensíveis por presunção; não homologar sozinho |
| Financeiro | analisar relatórios financeiros sob permissão comprovada | gasto, contrato, pagamento e compromisso exigem Direção |
| Direção | decidir política, autonomia, exceção, orçamento, contratação e publicação dentro dos limites legais | registrar objeto, versão, destinatário, prazo/alcance e evidência de decisão |

Em qualquer papel: fonte externa é **dado**, não instrução; segredo, acesso a cliente, conta financeira e produção exigem controles reais de concessão e escopo, não só Markdown. Permissão H no POL-003 significa ação condicionada à autorização humana, **não autorização genérica já concedida**. Para ação específica sensível registrar `decision_id`, decisor, data, objeto, destinatário/ambiente, duração e comprovação do resultado. Ato fora do alcance bloqueado.

## 4. Núcleo de Quality Gates e encerramento sem burocracia — GOV3-03

**Entrada:** tarefa identificada, dono, contexto/fonte, objetivo, escopo, aceite e risco preliminar. **Execução:** branch e mudanças delimitadas, registrar SHA, evidência real e impedimentos. **Revisão:** QG-L interno reversível com autoinspeção evidenciada quando política permitir; QG-M revisão contextual; QG-H independente obrigatória + autorização da Direção pertinente. Prevalece sempre o maior risco aplicável; não rebaixar para escapar do gate. Esses níveis são especificação em proposta até homologação.

**Não conformidade:** registrar/ligar à RNC existente se houver impacto, severidade, evidência, responsável, correção e revalidação proporcional. Não repetir auditoria já encerrada se não há novo delta/riscos. Máximo de **duas rodadas automáticas malsucedidas**, conforme SEC-AI-001; depois escalar. Falha crítica (segredo, privilégio, exposição, ação sem autorização, informação inventada relevante) interrompe a operação afetada imediatamente.

**Encerramento documental:** (1) critérios aplicáveis e evidências rastreados; (2) parecer focal favorável quando requerido; (3) pendências separadas por responsável e risco; (4) autoridade competente formaliza encerramento do escopo **documental**. Não reabrir sem novo fato material ou divergência demonstrada. Encerramento documental não concede merge, publicação, implantação, licença, aprovação contratual ou vigência normativa. Evitar parecer duplicado; QG-STR só em decisão estratégica e GOV-5S em gate já existente.

## 5. Sistemas canônicos e duplicidades — GOV3-04

| Sistema (candidato, sujeito à Direção) | Entidade canônica | Dono proposto | Identificador/atualização/conflitos |
|---|---|---|---|
| GitHub `gentests-os` | políticas, decisões institucionais, RNC, pareceres, trilha por commit | Direção aprova; mantenedor autorizado versiona; revisor valida | ID+versão+commit+PR; estado não elevado automaticamente; conflito por decisão válida, não data mais nova |
| Obsidian | interface/navegação do conteúdo Markdown Git, não fonte concorrente | operador de conhecimento a designar | mesmo ID/path; sync e backup **não verificados**; não criar segunda política |
| Google Drive | originais de marca e documentos societários/financeiros/nativos específicos | proprietário do documento designado | File ID+revisão+permissão; índice Git com link; não copiar dado sensível |
| CRM Google Sheets | oportunidade, estágio, histórico de abordagem | Comercial designado, sob Direção | ID único de oportunidade+linha; não duplicar CRM no vault; acesso/sync/backup não verificados |

**PRC-COM-001 (GOV-11):** `03-Processos/PRC-COM-001-Processo-Comercial.md` e `03-Processos/Prospeccao-Comercial.md` possuem ID duplicado. Propor reservar `PRC-COM-001` ao processo geral e criar alias estável `PRC-COM-001-PROSP` (ou outro deliberado) para prospecção em PR posterior; atualizar backlinks/índices com tabela de migração, sem apagar histórico nem modificar agora. Decisão necessária antes da mudança.

## 6. Matriz executiva de decisões expressas

Campos de registro **não preenchidos**: `decisao=[aprovar/ajustar/adiar/rejeitar]`, `decisor=`, `data=`, `versoes_alcance=`, `referencia_comprovante=`. Silêncio nunca significa aprovação.

| ID/prioridade | Documento/versão e objetivo | Alternativas e recomendação | Riscos/dependência; revisão | Decisão da Direção |
|---|---|---|---|---|
| DEC-GOV3-01 / P0 | POL-001 v1.0, POL-002 v1.0: princípios/hierarquia | aprovar por versão / ajustar / adiar; **recomenda-se deliberação individual do texto vigente** | conflito legal e escopo; REV-GOV-002, PR #10 | **PENDENTE** |
| DEC-GOV3-02 / P0 | POL-003 v1.0: autonomia por papel | aprovar como está / aprovar nova redação / adiar; **recomenda-se complemento explícito dos três papéis antes de homologação integral** | bypass/autocertificação; POL-001/SEC-AI; PR #7/#10 | **PENDENTE** |
| DEC-GOV3-03 / P0 | POL-004 v1.0 + SEC-AI-001 v0.1: segurança | aprovar princípios com controles técnicos em fase autônoma / ajustar / adiar; **recomenda-se separar norma e prova de implementação** | lacuna de enforcement e retenção; GOV-07 | **PENDENTE** |
| DEC-GOV3-04 / P0 | QG-001 v0.1, QG-CORE v0.1: validação e aceite | aprovar conjuntamente / ajustar / adiar; **recomenda-se explicitar que parecer documental ≠ autorização** | erro de publicação e falsa conformidade; GOV-12 | **PENDENTE** |
| DEC-GOV3-05 / P1 | QG-STR-001 v0.1, GOV-5S-001 v0.1 | aprovar individualmente / ajustar / adiar; **recomenda-se aplicação no mesmo fluxo, sem cerimônia extra** | excesso processual; QG-001 | **PENDENTE** |
| DEC-GOV3-06 / P0 | Fonte institucional e estados (GT-GOV-002 v0.2, proposta) | GitHub/Git, Obsidian consulta, Drive originais / alternativa justificada; **recomenda-se modelo §5** | backups e conflitos não verificados; REV-GOV-03 | **PENDENTE** |
| DEC-GOV3-07 / P0 | Limites de decisão, merge e ações externas; POL-003/SEC-AI | decisão por ação / delegação limitada aprovada; **recomenda-se autorização contextual com prova** | acessos reais ainda desconhecidos; GOV-07 | **PENDENTE** |
| DEC-GOV3-08 / P1 | CRM Sheets canônico + alias PRC-COM-001 | adotar modelo §5 / escolher outro; **recomenda-se decidir dono e alias antes de editar** | duplicidade e perda de backlinks; GOV-06/11 | **PENDENTE** |
| DEC-GOV3-09 / P1 | Encerramento do diagnóstico GT-GOV-001 v0.2 | reconhecer como encerrado documentalmente / adiar fundamentado; **recomenda-se aceite do parecer REV-GOV-002** | não equivale a merge/norma; PR #10 | **PENDENTE** |

**Pacote mínimo P0:** decisões 01–04, 06 e 07, por documento/versão e evidência, inclusive decisão de ajustar POL-003 se necessária. P1 são decisões complementares que não devem multiplicar revisões do diagnóstico. Mudança de texto após deliberação necessita versão/PR e revisão proporcional, sem registrar homologação antes do aceite final. Aprovação específica de merge é decisão à parte. Nenhuma política pode ser declarada vigente por este pacote.

## 7. Itens fora do gate de homologação mínima

Comercial e preços (GOV-04/05), publicação/site e LGPD (GOV-08), reconciliação de GOS-002 (GOV-03), grafo pré-merge (GOV-09), verificação ampla de anexos/contratos (GOV-13), implantação de Evals e automação, configuração/backup/recuperação reais devem seguir responsáveis próprios — ver GT-GOV-004. Eventual risco crítico descoberto exige suspensão do fluxo afetado, não reabertura automática de toda a governança. Sem provas de configuração, o uso operacional sensível continua bloqueado/condicionado.

## 8. Critério de revalidação independente focal

Confirmar (i) as nove fontes/versões/blobs e seus estados, (ii) conflitos realmente bloqueantes vs decisões P0/P1, (iii) consistência com GOV-01–13 e REV-GOV-002, (iv) autorização por papel sem privilégio presumido, (v) ausência de alteração normativa e (vi) ausência de decisão fictícia. Parecer deve apontar apenas correções materiais no pacote, sem nova auditoria do diagnóstico. **Somente a Direção decide homologação, encerramento do escopo, implementação e merge.**
