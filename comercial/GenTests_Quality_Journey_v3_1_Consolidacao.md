---
id: GT-COM-QJ-CONS-20261010
tipo: consolidacao-comercial
versao: 3.1-proposta
status: proposta
estado_documental: em-validacao
data: 2026-10-10
aprovador: Direcao
aprovacao: pendente
fonte_revisao: revisoes/REV-COM-QJ-001-Ajustes-Quality-Journey.md
plano_canonico: 04-Decisoes/PLN-COM-001-Primeiras-Vendas-GenTests.md
---

> **REVISÃO SUPERVENIENTE (10/10/2026):** o [parecer REV-COM-QJ-002](../revisoes/REV-COM-QJ-002-Parecer-Quality-Journey.md) solicitou seis correções. A proposta técnica de tratamento está em [GT-COM-QJ-003 — v3.2](GT-COM-QJ-003-Tratamento-REV-COM-QJ-002.md). A v3.1 abaixo permanece histórica e **não está homologada**. Os preços R$ 290/650/1.200 e a campanha anterior não são ofertas correntes automaticamente. **Não publicar nem cotar.**

# GenTests Quality Journey — proposta consolidada v3.1

**Status: EM REVISÃO, não homologado.** Consolidação do parecer [REV-COM-QJ-001](../revisoes/REV-COM-QJ-001-Ajustes-Quality-Journey.md) da [PR #2](https://github.com/gentestsai-sudo/gentests-os/pull/2) com o [roteiro v3](https://github.com/gentestsai-sudo/gentests-os/blob/review/precificacao-2026-10-10/comercial/apresentacao-comercial-v3-quality-journey-proposta.md). Esta revisão não aprova preços, margem, escopo, contrato, publicação nem merge na main.

## 1. Direção registrada
Manter **Start/Descobrir → Focus/Investigar → Evolution/Planejar → Implementation/Implementar → Excellence/Sustentar**. As etapas são independentes ou progressivas; cliente não precisa comprar a anterior quando já possui os insumos necessários. Não exibir horas na apresentação, mas estimar esforço completo e pactuar limites em proposta individual. Primeiro contrato + entrada comprovada é marco de aquisição; não equivale a serviço entregue.

## 2. Matriz de escopo sugerida (NÃO homologada)

| Etapa | Pergunta do cliente | Entrada e trabalho propostos | Entrega concreta | Limites a fechar |
|---|---|---|---|---|
| **Start** | Onde olhar primeiro? | Objetivo, contexto, relato/evidência; triagem especializada de um ponto delimitado | **Nota diagnóstica**, hipóteses, prioridades iniciais e próximos passos | Se inclui entrevista, acesso ou execução de testes; não promete investigação completa |
| **Focus** | O que acontece nesta jornada/risco? | Jornada autorizada, critérios e ambiente; exploração de cenários/variantes pactuados | **Relatório de investigação**, evidências ou ausência de falhas observadas, limites e prioridades | Quantidade de jornadas/variantes, integrações, reteste; não garante encontrar bugs |
| **Evolution** | O que mudar e em qual ordem? | Práticas/requisitos/evidências; análise estruturada no recorte contratado | **Plano de melhoria priorizado**, mapa de riscos e indicadores candidatos | Dimensões, entrevistas e profundidade; não inclui Focus completo ou implantação automaticamente |
| **Implementation** | Como colocar em prática? | Backlog priorizado e acessos; implantar **itens escolhidos** | **Itens implantados**, evidências de aceite, documentação e handoff | Definir se processo, automação, ferramentas ou código; marcos e exclusões |
| **Excellence** | Como sustentar a evolução? | Melhorias existentes, responsáveis e métricas; acompanhamento por ciclos pactuados | **Indicadores e relatórios por ciclo**, recomendações e ajustes | Prazo, frequência, disponibilidade, canais, SLA, suporte e implementações adicionais |

Ficha obrigatória por serviço: público/problema, entradas, unidade de escopo, tarefas, entregáveis, exclusões, prazo/dependências, horas internas totais por atividade, revisões/reteste, aceite, preço, pagamento e cláusulas de mudança de escopo. **As quantidades concretas ainda não foram homologadas.**

## 3. Preços e campanha: NÃO inferir decisão

| Serviço | Preço da v3 | Classificação | Preço após campanha |
|---|---:|---|---|
| Start | R$ 290 indicativo | **Pendente: regular ou promocional** | Pendente |
| Focus | R$ 650 indicativo | **Pendente** | Pendente |
| Evolution | R$ 1.200 indicativo | **Pendente** | Pendente |
| Implementation | Sob proposta | Elegibilidade à campanha pendente | Sob proposta |
| Excellence | Sob proposta | Elegibilidade à campanha pendente | Sob proposta |

**Histórico da PR #2, não oferta corrente automaticamente:** QA Express R$ 490; Auditoria Funcional R$ 1.490; Processos QA R$ 2.490, com três clientes no total. **Não presumir equivalência** Express=Start, Funcional=Focus ou Processos=Evolution. Decidir se ofertas antigas serão mantidas, substituídas ou coexistirão.

**Alternativas para decisão da direção:**
- **A:** manter a campanha antiga restrita aos serviços antigos; definir tabela regular Quality Journey.
- **B:** migrar a campanha para Quality Journey, decidindo etapas elegíveis, preço regular/promocional, três vagas compartilhadas ou outro limite, vigência, reservas, cancelamentos e contratos adicionais.

A contagem de vagas da PR #2 (contrato aceito + entrada comprovada, um primeiro projeto por cliente distinto) é **proposta operacional histórica**, não regra automaticamente transferida. Não anunciar promoção ou urgência até decisão. Pagamento 50/50 permanece diretriz a revisar juridicamente e fiscalmente, não aprovação para novos serviços.

## 4. Viabilidade financeira: NOVA simulação gerencial

**Fonte histórica:** [revisão financeira](../revisoes/2026-10-10-precificacao-proposta.md) usa custo de oportunidade **R$ 69,92/h**, DAS hipotético **6%** e sensibilidade **15,5%**. Não são alíquota confirmada nem custo contábil; não transportar margens dos serviços antigos.

**Hipóteses de sensibilidade criadas nesta revisão, não estimativas aprovadas nem tetos de horas:** Start 2h/4h e custo atribuído R$20; Focus 5h/8h e custo R$40; Evolution 10h/16h e custo R$80. Horas devem cobrir alinhamento, preparação, análise, execução aplicável, evidências, relatório, revisão, devolutiva e comunicação. Substituir por tempos e despesas reais, sem rateio duplicado.

Fórmula: resultado = preço − preço×DAS hipotético − horas×R$69,92 − custos atribuídos.

| Serviço | Horas ilustrativas | Resultado a 6% | Margem a 6% | Resultado a 15,5% | Margem a 15,5% |
|---|---:|---:|---:|---:|---:|
| Start R$290 — esperado | 2 | R$112,76 | 38,9% | R$85,21 | 29,4% |
| Start — maior esforço | 4 | **−R$27,08** | −9,3% | **−R$54,63** | −18,8% |
| Focus R$650 — esperado | 5 | R$221,40 | 34,1% | R$159,65 | 24,6% |
| Focus — maior esforço | 8 | R$11,64 | 1,8% | **−R$50,11** | −7,7% |
| Evolution R$1.200 — esperado | 10 | R$348,80 | 29,1% | R$234,80 | 19,6% |
| Evolution — maior esforço | 16 | **−R$70,72** | −5,9% | **−R$184,72** | −15,4% |

**Interpretação:** risco de perda no cenário de maior esforço, especialmente Start e Evolution; não reduzir horas ficticiamente para encaixar preço. Isso não é lucro contábil e não inclui todos os custos de aquisição/ociosidade. Implementation e Excellence: **sem base de escopo/preço para simular margem**. Requerem orçamento específico e decisão explícita sobre qualquer subsídio comercial.

## 5. Roteiro comercial v3.1 (10 slides)
1. Capa: Quality Journey — da descoberta à qualidade sustentável.
2. Dor: riscos invisíveis, retrabalho e decisões sem evidências.
3. Jornada: cinco perguntas distintas; contratação independente/progressiva.
4. Start = triagem/nota; Focus = investigação/evidências; Evolution = plano/indicadores. Valores v3 **apenas indicativos para revisão interna**.
5. Implementation = implantação de itens pactuados; Excellence = acompanhamento por prazo/frequência definidos. Ambos sob proposta.
6. Exemplo de cadastro **explicitamente ilustrativo**, sem case inventado.
7. Entregáveis distintos e proporcionais ao serviço.
8. Alinhamento → escopo/aceite → execução → devolutiva.
9. Experiência técnica e estratégica real, sem números de resultados não comprovados.
10. CTA: conversa breve para escolher ponto de partida.

**PPTX v3.1:** revisão de textos e limites realizada; renderização visual e teste de overflow executados. **Pendente**: revisão independente e autorização da direção. O PPTX v3 original continua preservado na branch anterior.

## 6. Impacto proposto no site — NÃO publicado
**Hero:** “Qualidade de software, da descoberta à evolução contínua.”  
**Subtítulo:** “Investigamos riscos, estruturamos melhorias e apoiamos sua implementação — conforme a necessidade do seu negócio.”  
**Jornada:** cinco cartões com nome inglês, verbo em português, pergunta e entrega. Indicar independência das etapas.  
**Serviços:** três entradas delimitadas + duas ofertas sob proposta. **Sem publicar preços até definir regular/promocional.**  
**CTA:** “Converse com a GenTests.ai sobre seu desafio de qualidade.”  
**Gates:** revisão visual/responsiva, acessibilidade, SEO, precificação e autorização. Nenhuma alteração no site foi executada.

## 7. Governança e pendências
**PLN-COM-001 continua canônico.** Esta v3.1 complementa, mas não altera silenciosamente, a campanha da PR #2. Atualizar plano, decisão, catálogo, evidências, índices e backlinks **depois** da decisão sobre coexistência/substituição; manter IDs e histórico. CRM atual continua canônico para oportunidades; não criar CRM paralelo. Obsidian local só será atualizado após integração GitHub e sincronização verificável — **não sincronizado nesta execução**.

**Decisões necessárias da direção:**
1. Preços v3 regulares ou promocionais?
2. Destino da campanha anterior e elegibilidade dos cinco níveis?
3. Destino dos três serviços antigos?
4. Escopos, revisões, prazos e horas reais por etapa?
5. Alíquota efetiva/NFS-e, custos, margem mínima e eventual perda aprovada?
6. Contrato, 50/50, aceite, cancelamento, suporte e reteste?
7. Revisão independente e autorização explícita antes de atualizar site, main ou divulgar.

**Fontes:** REV-COM-QJ-001 (PR #2); apresentação v3 (branch review/precificacao-2026-10-10); revisão financeira 2026-10-10; PLN-COM-001 0.3.0. **Fatos documentais, sugestões, hipóteses e pendências foram distinguidos acima.**
