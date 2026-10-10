---
id: GT-GOV-002
tipo: tratamento-parecer-e-matriz-rastreabilidade
versao: 0.2.0
status: proposta
estado_documental: aguardando-revalidacao-independente
data: 2026-10-10
origem: REV-GOV-001
diagnostico: GT-GOV-001
pr: 6
aprovador: Direcao
aprovacao: pendente
autorizacao_merge: pendente
---
# GT-GOV-002 — Tratamento REV-GOV-001 e matrizes de governança

> Documento interno. **Tratado pelo executor não significa encerrado pelo revisor.** Não altera políticas, catálogo, controles reais nem estados operacionais.

## 1. Matriz de evidências e tratamento GOV-01 a GOV-13

Links `main` referem-se ao snapshot consultado em 10/10/2026; branch ou SHA indicados identificam proposta histórica, não documento aprovado. Para arquivos diretamente verificados, a referência é a versão então recuperada; para fonte externa não lida integralmente, classificar verificação parcial/não verificada. Severidade: Alta ou Média conforme REV-GOV-001; as seis altas são 01,02,04,05,07,08. Cada linha indica **resposta documental proposta**, não conformidade final.

| ID | Risco | Evidência / versão ou commit | Verificação | Tratamento e encaminhamento |
|---|---|---|---|---|
| GOV-01 | Alta | [Registro de decisões](../04-Decisoes/Registro-de-Decisoes.md) (blob `86ed3dec588d9d734a10cd60f04f886543340f8b`); [Primeiro PIX](../04-Decisoes/Primeiro-PIX-Homologacao-Comercial.md) v0.2 (blob `314644c3727d86d1ff1ba48086756158491b4e4c`); [PR #1](https://github.com/gentestsai-sudo/gentests-os/pull/1) | Confirmado que índice não lista aprovação; autorização documental do PR #1 relatada, merge do PR #1 observável | Separar decisão documental comprovável de decisão empresarial pendente; não preencher 'aprovadas' sem prova |
| GOV-02 | Alta | [POL-001](../00-Constituicao/Regras-de-Ouro.md), [POL-002](../00-Constituicao/Hierarquia-e-Conflitos.md), [POL-003](../00-Constituicao/Matriz-de-Permissoes.md), [POL-004](../00-Constituicao/Seguranca-e-Dados.md), [QG-001](../00-Constituicao/Quality-Gates/QG-001-Politica.md), [QG-CORE](../00-Constituicao/Quality-Gates/QG-CORE-Obrigatorio.md), [QG-STR-001](../00-Constituicao/Quality-Gates/QG-STR-001-Disciplina-Estrategica.md), [SEC-AI-001](../00-Constituicao/SEC-AI-001-Seguranca-Confiabilidade-Agentes.md), [GOV-5S-001](../00-Constituicao/Excelencia-Enxuta-5S.md) | Campos YAML `proposta` observados; nenhuma homologação rastreada | Manter todas em proposta; pacote de decisão A com versão/alcance explícitos |
| GOV-03 | Média | [Kanban](../09-Backlog/Kanban.md) v1.1 (blob `4d39ccdc72ae25fc8feced1b93eaf14da9f09937`), [GOS-002](../09-Backlog/Cards/GOS-002.md) v1.1 (blob `f9c7fb194161817cd81feccdbe38ba84b3eec362`); repositório GitHub privado consultado | Privacidade do repositório e card aberto confirmados; configuração .gitignore/revisão/aceite não validada integralmente | Manter GOS-002 aberto; Infra verifica .gitignore, revisão efetiva, aceites, e então concilia Kanban |
| GOV-04 | Alta | [QA Express piloto](../07-Templates/QA-Express-Oferta-Piloto.md) v0.1 (blob `b045d72c3908ace91f14b97bcf4536514e84c3bc`), [Primeiro PIX](../04-Decisoes/Primeiro-PIX-Homologacao-Comercial.md) v0.2, [revisão de precificação PR #2](https://github.com/gentestsai-sudo/gentests-os/pull/2) | R$890 v0.1 e R$690 histórico confirmados na nota; R$490 na proposta de campanha, sem cotejo jurídico/financeiro | Matriz SKU §2; bloquear cotação até homologação |
| GOV-05 | Alta | [PR #3](https://github.com/gentestsai-sudo/gentests-os/pull/3), `comercial/GT-COM-QJ-004-Tratamento-REV-COM-QJ-003.md` v3.2.1, [PR site #1](https://github.com/gentestsai-sudo/gentests-site/pull/1) | Estrutura cinco níveis na proposta e três ofertas históricas confirmadas documentalmente; substituição não aprovada | Coexistência/substituição indeterminada; decisão E |
| GOV-06 | Média | [Processo comercial](../03-Processos/PRC-COM-001-Processo-Comercial.md) v0.1 (blob `4e8b84cec1cc6be84636fe8ec8cfbb9417e15944`), [Prospecção](../03-Processos/Prospeccao-Comercial.md) (blob `0c4066baa14edeb977b7c7adc1b72e7503b4434f`), [CRM Sheets](https://docs.google.com/spreadsheets/d/151zLp3akkkbdeA6D44EOAsefT9gjygvv0ZMsGRZ3WV0/edit) | Conflito textual confirmado; integridade/atualidade do CRM não verificada | Proposta de ownership §3, sem sincronização presumida |
| GOV-07 | Alta | [SEC-AI-001](../00-Constituicao/SEC-AI-001-Seguranca-Confiabilidade-Agentes.md), [POL-003](../00-Constituicao/Matriz-de-Permissoes.md), workflows `.github/workflows/` presentes em main | Especificação e existência de arquivos verificadas; enforcement GitHub/contas não verificado | Inventário técnico isolado com prova positiva/negativa, sem declarar ausência de proteção |
| GOV-08 | Alta | [REV-SITE-001 na PR #5](https://github.com/gentestsai-sudo/gentests-os/pull/5), [site PR #1](https://github.com/gentestsai-sudo/gentests-site/pull/1) | Parecer documental relata FormSubmit e LGPD pendentes; navegador, recebimento e avaliação legal não executados nesta revisão | Bloqueio de homologação/site mantido; gate funcional em PR do site |
| GOV-09 | Média | [PR #2](https://github.com/gentestsai-sudo/gentests-os/pull/2), [PR #3](https://github.com/gentestsai-sudo/gentests-os/pull/3), [PR #4](https://github.com/gentestsai-sudo/gentests-os/pull/4), [PR #5](https://github.com/gentestsai-sudo/gentests-os/pull/5), [PR #6](https://github.com/gentestsai-sudo/gentests-os/pull/6), [PR #7](https://github.com/gentestsai-sudo/gentests-os/pull/7) | PR #3 documenta dependência #2→#3; demais bases/diffs e conflito de merge não simulados | Grafo §4; reconsultar base/head e diff imediatamente antes de qualquer merge |
| GOV-10 | Média | [INICIO](../INICIO.md) v1.1 `aprovado-para-uso-inicial`, políticas `proposta`, identidade `referenciado`, parecer REV-GOV-001 `emitido` | Confirmado documentalmente | Duas dimensões §5: maturidade e autorização; índice não homologa conteúdo |
| GOV-11 | Média | [Processo comercial](../03-Processos/PRC-COM-001-Processo-Comercial.md) (blob `4e8b84cec1cc6be84636fe8ec8cfbb9417e15944`), [Prospecção](../03-Processos/Prospeccao-Comercial.md) (blob `0c4066baa14edeb977b7c7adc1b72e7503b4434f`) | Duplicidade YAML `id: PRC-COM-001` confirmada | Reservar PRC-COM-001 ao processo geral; propor alias `PRC-COM-001-PROSP`, sem mudar legado nesta etapa; decidir nome definitivo |
| GOV-12 | Média | [QG-001](../00-Constituicao/Quality-Gates/QG-001-Politica.md), [GQF-001](../03-Processos/GenTests-Quality-Framework.md), [relatório do site](https://github.com/gentestsai-sudo/gentests-site/blob/fix/site-001-auditoria-controlada-20261010/docs/GT-SITE-001-Relatorio-Testes-e-Publicacao.md) | Distinção de gate escrita; execução funcional pendente | Relatar quatro eixos independentes: documental, técnico, funcional e autorização |
| GOV-13 | Média (lacuna de cobertura) | Seção 1 de [GT-GOV-001 v0.1](https://github.com/gentestsai-sudo/gentests-os/blob/cd15cfcc51efba3cfbb4c815fd24b3bb131db287/revisoes/GT-GOV-001-Diagnostico-Consolidacao-Governanca.md), limitações do REV-GOV-001 | Cobertura incompleta admitida; não é defeito confirmado em fonte não inspecionada | Amostra por risco §7; pendências remanescentes separadas do encerramento do diagnóstico |

### REV-GOV-01–03 — correção executada documentalmente

| ID | Resposta | Evidência | Pendente |
|---|---|---|---|
| REV-GOV-01 | Matriz por ID com arquivos, versões/blobs conhecidos, links, classe de verificação e encaminhamento | §1 | Revalidação da suficiência pelo revisor |
| REV-GOV-02 | Separação de decisão anterior com prova, aprovação pendente e autorização limitada | §6 | Direção homologa onde aplicável |
| REV-GOV-03 | Ownership, chave, fluxo de atualização, conflito e backup definidos como **propostas** | §3 | Confirmar permissões, acessibilidade do Drive/Sheets e integração real |

## 2. Conflitos comerciais: matriz de SKU, escopo e preço

| Linha | Fonte / estado | Escopo distinto | Valor indicado | Uso permitido |
|---|---|---|---|---|
| QA Express catálogo v1 de 09/10 | Fonte histórica citada no Primeiro PIX; original Drive não verificado aqui | Até 5 páginas públicas **ou** jornada simples, 2 dias úteis | R$690 | Referência histórica; não presumir homologação |
| Diagnóstico inicial PLN-COM-001 v0.1 | Histórico Git/Primeiro PIX v0.2 | Diagnóstico sem execução de testes, até 5 dias úteis | R$1.890 | Alternativa antiga, não equiparar a QA Express com testes |
| QA Express piloto OFERTA-QA-EXPRESS v0.1 | Main, `status: proposta` | Um fluxo crítico, até 6h, avaliação funcional com testes e evidências | R$890 | Não cotar |
| Promoção primeiros três clientes | Precificação na PR #2, `status: proposta` | Escopo de catálogo a reconciliar com esforço real | R$490 Express; R$1.490 Funcional; R$2.490 Processos | Condição comercial sob validação; não cotar automaticamente |
| Auditoria Funcional catálogo | Revisão precificação PR #2, proposta | Até 3 jornadas, 4 dias úteis | R$1.800 | Referência proposta a reconciliar |
| Auditoria Processos QA catálogo | Revisão precificação PR #2, proposta | Entrevistas + 1 fluxo, 5 dias úteis | R$2.900 | Referência proposta a reconciliar |
| Quality Journey QA Start | PR #3, GT-COM-QJ-004 v3.2.1 proposta | Triagem documental, sem execução de testes; insumos e devolutiva limitados | R$290 hipótese | Não é sinônimo de QA Express |
| Quality Journey QA Focus/Evolution/Implementation/Excellence | PR #3, proposta | Investigação funcional; diagnóstico de QA; implantação por orçamento; acompanhamento por ciclo | Valores variáveis/hipóteses; não reproduzidos como tabela oficial | Decisão de coexistência/migração pendente |
| Site `solucoes.html` | site PR #1 draft | Página com três ofertas, preço retirado na proposta de correção | Sem preço público homologado | Publicação bloqueada |

**Decisão comercial pendente:** Direção definir catálogo oficial por SKU, escopo, preço regular, eventual preço promocional, vigência, critério de capacidade e documento fonte. Não substituir catálogo, contrato ou site nesta PR. Nenhuma oferta é declarada obsoleta por mera proximidade de nome.

## 3. Responsabilidade dos sistemas — proposta, não integração implementada

| Sistema | Entidades canônicas candidatas | Responsável por atualização | Identificador e procedimento | Conflito / backup |
|---|---|---|---|---|
| GitHub `gentests-os` | Políticas Markdown, decisões, pareceres, RNCs, histórico e trilha documental | Direção aprova política; executor versiona após autorização; revisor independente valida | ID estável + versão + commit SHA + PR; mudanças por PR e decisão vinculada | Divergência resolvida por versão aprovada/decisão, não pela mais recente; histórico Git preservado |
| Obsidian | Interface local de navegação e edição do vault Markdown | Operador designado pela Direção (a definir) | Mesmo caminho/ID Git; sincronização via Git somente se comprovada e configurada | Não criar notas paralelas como nova fonte; backup/restauração a testar |
| Google Drive | Ativos originais de marca, documentos societários/financeiros autorizados, documentos nativos que não são Markdown | Dono do artefato/direção, específico por pasta | File ID + revisão + link em índice Git (sem copiar documentos sensíveis) | Conflito por autorização expressa e registro de versão; política de permissões/backup pendente |
| CRM Google Sheets | Oportunidades, etapas, contato comercial mínimo, histórico de abordagem | Comercial dentro de escopo autorizado; Direção aprova ações externas | ID único de oportunidade; atualizar linha existente e ligar ao OS por ID/URL | Não recriar CRM no Obsidian; validação de permissões, deduplicação e backup pendente |

Nenhuma sincronização, automação ou backup acima foi testada. Um link externo não prova permissão de acesso, atualidade ou integridade. **Regra de atualização candidata:** cada alteração acontece primeiramente na fonte da entidade, depois referências/links são reconciliados manualmente; nunca manter dois registros editáveis concorrentes da mesma decisão/oportunidade.

## 4. Mapa de conflitos, duplicidades e dependências

| Objeto | Relação detectada | Estado | Encaminhamento |
|---|---|---|---|
| `PRC-COM-001` | Dois arquivos com mesmo identificador | Confirmado | Canonizar processo geral, alias de prospecção sujeito a decisão, sem apagar histórico |
| Catálogo / Primeiro PIX / Quality Journey | Preço e escopo divergentes; coexistência e migração ainda sem homologação | Confirmado parcialmente | Matriz §2 e decisão comercial E |
| Registro de decisões / notas específicas | Índice sem aprovações; autorização delimitada do PR #1 registrada em nota operacional | Confirmado | Separar índice de pendências e decisões com evidência; sem fabricar aprovação |
| PR OS #2 → PR OS #3 | Dependência de branch relatada no documento da PR #3 | Declarada e parcialmente verificada | Checar base/head/diffs antes de merge, não inferir merge seguro |
| PR OS #4 conteúdo CNQ | Parecer/tratamento e PDF sujeito a teste visual | Em revisão independente | Não liberar comercial; revisar em sua PR |
| PR OS #5 / site #1 | Parecer separado de execução, impedimentos funcionais e LGPD | Parecer emitido; homologação bloqueada | Revalidação funcional no site e autorização posterior |
| PR OS #6 / #7 | Diagnóstico executor e parecer revisor independente; parecer revisou commit v0.1 | Confirmado | Revalidação focal da v0.2, sem reaproveitar parecer como aprovação automática |
| PR OS #8 (AI-LEARN) | Proposta de Evals depende de clareza normativa GOV-001 | Dependência lógica, não branch comprovadamente empilhada | Implantação futura somente após gates próprios |
| Kanban GOS-002 / repositório privado | Repo existe, mas card ainda requer .gitignore, revisão e aceite | Parcial | Manter card aberto até verificar cada critério |
| Documentos anteriores/pareceres | Histórico por commit não invalida parecer antigo, nem aprova nova versão | Confirmado por estrutura | Preservar todos; sinalizar atualização sem exclusão |

## 5. Estados separados para impedir falsa homologação

**Maturidade documental candidata:** `rascunho` → `proposta` → `em-revisao` → `aprovado`; `historico` / `substituido` exigem referência de sucessor/decisão. `emitido` é estado de parecer, não aprovação normativa. `referenciado` e `aprovado-para-uso-inicial` podem qualificar índices/ativos específicos, não políticas vinculadas.

**Autorização de uso independente:** `interno-condicionado`, `externo-pendente`, `externo-autorizado`, `bloqueado`. Não assumir que `status: aprovado` de documento confere autorização de ação sensível.

**Eixo de verificação por entrega:** `documental`, `tecnico`, `funcional`, `autorizacao-humana`; cada um `conforme`, `correcao-necessaria`, `bloqueado` ou `nao-verificado`, citando versão/commit e método. Sem teste funcional, afirmar apenas conforme em inspeção estática.

**Escopo da mudança desta rodada:** taxonomia sugerida neste documento, sem migrar YAML dos arquivos legados; decisão B e plano posterior.

## 6. Decisões: comprovadas, limitadas e pendentes

| Prioridade | ID candidato | Natureza | Fonte/estado | Próximo responsável |
|---|---|---|---|---|
| Histórico | AUT-PR1-20261010 | Autorização delimitada para integrar documentos internos como propostas, não para aprovar políticas/comercial | Primeiro PIX v0.2 registra decisor e data; PR OS #1 está merged; autorização original do chat não foi revalidada independentemente | Direção/secretaria documental podem indexar após validar fonte primária |
| P0 | DEC-GOV-A | Aprovar/ajustar/rejeitar POL-001–004, QG-001/CORE/STR, SEC-AI-001 e 5S, por versão | Todas proposta, decisão não localizada no registro central | Direção |
| P0 | DEC-GOV-B | Canonização Git/Obsidian/Drive, taxonomia de estados e política de backup | Arquitetura §3 proposta; implementação não testada | Direção + Infra |
| P0 | DEC-GOV-D | Aprovação de matriz de poderes e controles técnicos reais após evidência | Políticas proposta; branch protection/conectores não inspecionados | Direção + Infra |
| P1 | DEC-GOV-C | CRM Sheets canônico e ID de oportunidades / ausência de duplicação | Conflito textual confirmado, ownership §3 candidato | Direção + Comercial |
| P1 | DEC-GOV-E | Portfólio, escopos, preços, promoções e lançamento | Propostas divergentes, tributos/custos não validados | Direção + Comercial/Financeiro |
| P1 | DEC-GOV-ID | Identificador estável de prospecção sem romper referências históricas | Duplicidade PRC-COM-001 comprovada; alias proposto | Direção + gestor documental |
| P1 | DEC-SITE | LGPD, marca, domínio, publicação e teste real | PR site #1 / parecer #5 bloqueiam publicação | Direção + responsável site |

**Não há homologação nova na v0.2.0.** Separar autorização histórica limitada, pendência e decisão futura; registrar `aprovado` apenas quando houver prova de objeto, aprovador, data, versão e alcance.

## 7. Controles reais, amostragem por risco e backlog posterior

| Prioridade | Trabalho posterior | Critério de aceite próprio | Dono candidato |
|---|---|---|---|
| P0 | Verificar permissões de conectores, tokens, branch protection/rulesets e aprovação de PRs | Evidência de configuração real e testes negativos/positivos sem segredo exposto | Infra + Auditor |
| P0 | Testar FormSubmit em desktop/mobile e tratamento de privacidade | Recebimento real com dados sintéticos, erros documentados e aprovação LGPD | Executor Site + revisor |
| P0 | Homologar Constituição após validação jurídica/operacional pertinente | Registro por versão, data, alcance e aprovador; sem mera marcação de checkbox | Direção |
| P1 | Reconciliar GOS-002 e Kanban; conferir os demais cards de maior risco | Cada aceite conferido antes de mudar status; trilha de alteração | Infra + Governança |
| P1 | Resolver IDs e fluxo de atualização de CRM/OS | Alias/referências consistentes e nenhuma oportunidade duplicada | Governança + Comercial |
| P1 | Portfólio e fontes comerciais canônicas | SKU e preço aprovados, escopo compatível e condições fiscais/financeiras verificadas | Direção + Financeiro |
| P2 | Inspecionar anexos e contratos de agentes por amostragem | Lista de arquivos inspecionados, limitações e achados relevantes | Auditor |
| P2 | Testar rotina de backup/restore Obsidian/Drive | Evidência de restauração e dono formalizado | Infra |
| P2 | Avaliar suíte AI-LEARN-001 | Baseline de testes curado e autorização em PR separado | QA + Direção |

**Amostragem proporcional:** priorizar políticas e permissões, decisões econômicas, dados pessoais e publicação; depois contratos de agentes, cards e binários relacionados a decisões efetivas. Arquivos irrelevantes para o diagnóstico não devem bloquear fechamento. Classificar cada item como verificado, parcial ou não verificado; ausência de acesso não significa defeito comprovado.

## 8. Critério de encerramento da rodada documental

- [x] Treze achados com severidade, referência, situação de evidência e encaminhamento.
- [x] REV-GOV-01–03 respondidos documentalmente.
- [x] Conflitos de serviços, preço, IDs, fonte canônica e PRs identificados.
- [x] Decisões pendentes separadas de autorização histórica limitada.
- [x] Sem alteração de política, permissão, contrato, preço, identidade ou código.
- [ ] Revisor independente confirma suficiência das evidências e ausência de regressão material.
- [ ] Direção autoriza eventual merge documental; **não** equivale à homologação normativa.

**Não solicitar auditoria integral novamente:** pedir revalidação focal dos itens corrigidos e novas regressões altas/críticas se houver. Não encerrar unilateralmente RNC ou achado.
