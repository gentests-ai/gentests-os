---
id: GT-GOV-QG-ENC-001
titulo: Politica de Criterios de Aceite, Revisao e Encerramento
tipo: politica-governanca
versao: 0.1.0
status: proposta
estado_documental: aguardando-revisao
data: 2026-10-10
responsavel_elaboracao: agente-redator
aprovador: Direcao
aprovacao: pendente
vigencia: nao-iniciada
aplicacao: somente-apos-homologacao
---
# GT-GOV-QG-ENC-001 — Critérios de aceite, revisão e encerramento

> **PROPOSTA INTERNA — NÃO É POLÍTICA VIGENTE.** Sujeita a revisão independente e aprovação expressa da Direção da GenTests.ai. Este documento não altera permissões, processos existentes, catálogos, preços nem o status de PRs anteriores.

## 1. Finalidade e princípios

Estabelecer decisões **proporcionais ao risco, baseadas em critérios e evidências**, reduzindo ciclos indefinidos de execução → revisão → execução. O objetivo não é perfeição absoluta: é demonstrar qualidade suficiente para o **uso previsto**. Revisão técnica, aceite de entrega e autorização de publicação são decisões distintas. A segurança, obrigações legais e aprovação humana não podem ser dispensadas por métricas.

Aplicável como proposta a documentos, estudos, conteúdo comercial, apresentações, sites, software, automações e demais artefatos. Cada tipo deve ter um checklist específico e gates adicionais de segurança, privacidade, acessibilidade ou financeiro quando aplicável. Um artefato pode ser aceito como **documento técnico** sem estar aceito como **peça pública**; a separação precisa constar do registro.

## 2. Papéis e segregação

| Papel | Atribuição | Não pode |
|---|---|---|
| Solicitante/PO | Define finalidade, escopo, entregáveis e critérios verificáveis antes da execução | Mudar escopo retroativamente sem controle de mudanças |
| Executor | Produz artefato, autotestes, evidências e matriz de tratamento dos achados | Declarar própria entrega homologada |
| Revisor independente | Confronta evidências, escopo e riscos; emite parecer e decide aceite técnico | Corrigir o mesmo artefato sob revisão ou aprovar decisões reservadas à Direção |
| Direção | Aceita risco residual quando autorizado, homologa política e aprova uso externo | Substituir requisitos legais ou controles obrigatórios por mera declaração |
| Especialista (quando aplicável) | Valida temas contábeis, jurídicos, segurança e outros sob sua competência | Ser presumido consultado sem registro |

O mesmo agente não deve atuar simultaneamente como executor e revisor da mesma alteração. Independência deve ficar registrada.

## 3. Contrato de revisão — obrigatório antes da primeira revisão

A ficha de escopo fixa: **ID/versão/repositório/commit; finalidade e público; artefatos obrigatórios; exclusões; referências normativas e seus status de aprovação; critérios de aceite testáveis; evidências exigidas; riscos e severidades; revisor e aprovador; condição de publicação; prazo ou evento de fechamento**.

Cada critério recebe ID, método de verificação, evidência esperada e natureza **bloqueante** ou **não bloqueante**. Critério exigido para um entregável visual (p. ex. PDF) não pode ser cumprido apenas por declaração ou hash de arquivo local. Ausência de evidência obrigatória = critério não atendido. Se a exigência não estava prevista, classificar como mudança de escopo, salvo segurança/lei/risco alto demonstrado.

**Congelamento de escopo:** após a primeira revisão, o contrato e o conjunto de achados ficam baselined por commit. Novas ideias, preferências estéticas ou oportunidades de melhoria viram backlog. Podem entrar no ciclo como bloqueio novo somente: (i) regressão comprovada; (ii) falha em critério obrigatório previamente definido; (iii) risco crítico/alto novo documentado; (iv) obrigação legal, privacidade, segurança ou governança aplicável. Sempre registrar evidência e motivo de inclusão.

## 4. Severidade, aceite e gestão de risco residual

| Severidade | Regra de classificação | Condição no fechamento |
|---|---|---|
| Crítico | Exposição grave imediata, violação legal/segurança grave, perda material irreversível ou comprometimento essencial do objetivo | **0 abertos** |
| Alto | Impede finalidade prevista, dado/alegação material errôneo, evidência essencial ausente ou impacto comercial/reputacional significativo | **0 abertos** |
| Médio | Lacuna com impacto limitado, mitigável e sem impedir finalidade; evidência parcial não essencial | Permitido **apenas** com justificativa, mitigação, responsável, prazo e aceite de risco por autoridade competente |
| Baixo | Aprimoramento opcional, estética sem impacto relevante, detalhe editorial | Backlog; não impede aceite |

Se um 'médio' prejudicar uma exigência obrigatória do escopo, ele passa a **bloqueante** independentemente do rótulo. Achados não se encerram por decurso de prazo, quantidade de revisões ou porcentagem de testes. Incerteza deve ser explicitada, nunca convertida em 'aprovado'.

## 5. Gate de aceite objetivo

Aceite técnico só pode ser **APROVADO** se: (a) 100% dos critérios bloqueantes atendidos e comprovados; (b) 100% das evidências obrigatórias disponíveis e inspecionáveis; (c) zero achados críticos e altos em aberto; (d) verificações de regressão apropriadas concluídas; (e) não houver violação conhecida de lei, segurança ou governança.

**APROVADO COM RESSALVAS:** mesmos cinco mínimos atendidos, porém persistem achados médios/baixos não impeditivos com risco residual formalmente aceito, responsável, prazo e evidências de mitigação. Ressalvas não permitem dispensar critério obrigatório.

**REPROVADO / BLOQUEADO:** qualquer mínimo não atendido. **NÃO VERIFICÁVEL** é estado de um critério sem evidência e impede aprovação se bloqueante. **CANCELADO/SUBSTITUÍDO** encerra o trabalho sem atestar qualidade, por decisão explícita do solicitante/Direção.

**Aceite técnico ≠ homologação ≠ publicação.** Documentos com `status: proposta` continuam não vigentes. Uso externo, alteração de política, merge protegido ou campanha dependem das autorizações próprias, mesmo após aceite técnico.

## 6. Fluxo e limite de rodadas

1. **Preparação:** contratualizar escopo, critérios e evidências; executor faz autocheck e entrega versão identificada.
2. **Revisão ordinária 1 — abrangente:** revisor avalia todos os critérios, registra achados com ID/severidade/evidência/impacto/ação/critérios de resolução.
3. **Tratamento pelo executor:** corrigir apenas achados e requisitos aprovados, mapear cada mudança para ID, registrar testes e evidências.
4. **Revisão ordinária 2 — fechamento:** revalidar achados anteriores e regressões nas áreas modificadas; não reiniciar auditoria geral sem gatilho previsto no §3.
5. **Decisão:** emitir parecer de aceite/ressalvas/bloqueio e submeter autorização de uso à autoridade aplicável.
6. **Exceção:** se bloqueador persistir, fazer **verificação extraordinária focada no bloqueador** até resolver ou cancelar formalmente, com justificativa e escopo delimitado. Duas rodadas são uma **meta operacional**, nunca licença para liberar falha crítica.

Não reabrir achado encerrado sem evidência nova ou regressão. Qualquer mudança relevante de requisitos após baseline exige aditivo/novo item versionado e revisão proporcional, não revisão infinita do item original.

## 7. Métricas propostas e fórmulas

| Indicador | Cálculo | Meta candidata | Frequência |
|---|---|---|---|
| Cobertura dos critérios bloqueantes | critérios bloqueantes aprovados com evidência ÷ total de bloqueantes aplicáveis × 100 | **100% para fechar** | Por entrega |
| Completude de evidências obrigatórias | evidências verificadas ÷ evidências obrigatórias previstas × 100 | **100% para fechar** | Por entrega |
| Achados crítico/alto abertos | contagem por severidade no momento da decisão | **0** | Por entrega |
| Rodadas ordinárias | nº de revisões ordinárias da entrega | **≤ 2, meta** | Mensal |
| Reabertura não justificada | achados reabertos sem nova evidência/regressão ÷ total de achados encerrados × 100 | **0%** | Mensal |
| Novos bloqueadores fora de baseline | nº de bloqueadores descobertos após revisão 1, classificados por causa | Monitorar tendência; exigir justificativa de 100% | Mensal |
| Retrabalho de revisão | horas adicionais atribuídas à revisão/correção ÷ horas totais de entrega × 100 | **Medir baseline antes de definir meta** | Mensal |
| Tempo de ciclo até aceite | data/hora do aceite técnico − data/hora da primeira entrega pronta para revisão | **Medir baseline antes de definir meta** | Mensal |

Indicadores não são incentivos para ocultar achados, reduzir testes ou reclassificar severidade. Reportar volume de entregas e classificação de risco junto dos percentuais; com baixa amostra, apresentar contagem absoluta. Revisar metas após 60–90 dias de aplicação real autorizada.

## 8. Formato mínimo dos registros

**Ficha de entrega:** ID, finalidade, responsável, público, repositório/PR/commit, versões, entregáveis, critérios [ID, bloqueante?, procedimento, evidência], riscos, status normativo, exclusões e autorização para publicação.

**Achado:** ID estável, critério, descrição, evidência verificável (arquivo, seção/linha, URL ou artefato), severidade fundamentada, impacto, ação esperada, executor, status (`aberto`, `parcial`, `resolvido`, `não verificável`), commit da correção, teste de revalidação e risco residual.

**Parecer:** versão examinada e commit fixo, resultados por critério/achado, novos bloqueadores justificados, limitações, contagem por gravidade, decisão técnica, pendências, autorização de publicação **separada**, revisão e aprovadores identificados.

## 9. Aplicação ilustrativa: GT-MKT-CNQ-001

Escopo 1 — **conteúdo técnico em Markdown:** integridade das referências, cálculos, premissas, rastreabilidade, status documental, separação entre simulação e fato. Pode receber aceite técnico somente quando todos os critérios obrigatórios documentais passarem.

Escopo 2 — **material visual para distribuição:** inclui PDF/PPTX binário recuperável no GitHub, hash calculado do arquivo versionado, inspeção de páginas, legibilidade/acessibilidade e consistência com texto aprovado. Ausência de PDF bloqueia **o pacote visual**, não exige reabrir automaticamente toda a análise científica do texto. A publicação de qualquer peça exige aprovação expressa da Direção.

Esta política **não altera retroativamente** o parecer REV-MKT-CNQ-002 nem declara CNQ-04 resolvido. Caso se escolha separar entregáveis, formalizar novos gates e decisões sem apagar o histórico de achados.

## 10. Governança, implementação e revisão desta proposta

Fontes relacionadas: README de `gentests-os`; referências QG-001, PRC-COM-001 e GOV-5S-001 citadas em pareceres anteriores como **propostas**, não regras homologadas; parecer REV-MKT-CNQ-002; Quality Journey PR #3 em validação. Antes da homologação, Direção/revisor devem verificar conflitos com documentos canônicos e status vigentes, atualizar índice e matriz de permissões conforme processo aprovado e designar proprietário deste procedimento.

**Gate de aprovação da política:** (i) revisão independente, (ii) aprovação expressa e registrada da Direção, (iii) versão/data de vigência, (iv) comunicação a executores e revisores. Até isso ocorrer, trata-se exclusivamente de proposta.

**Controle de mudanças:** alterações futuras exigem nova versão, justificativa, avaliação de impacto, revisor distinto e decisão da Direção. A política não dispensa regras legais, privacidade, segurança, contratos ou aprovações especializadas.

---
**Decisão pendente da Direção:** aprovar/rejeitar/ajustar esta política. Nenhuma execução ou aplicação compulsória se presume pela presença no GitHub.
