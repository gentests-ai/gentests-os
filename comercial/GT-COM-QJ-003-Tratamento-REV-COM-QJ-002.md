---
id: GT-COM-QJ-003
tipo: tratamento-parecer-e-especificacao-comercial
versao: 3.2.0
status: proposta
estado_documental: em-validacao
data: 2026-10-10
responsavel_elaboracao: agente-executor-Quality-Journey
aprovador: Direcao
aprovacao: pendente
parecer_origem: revisoes/REV-COM-QJ-002-Parecer-Quality-Journey.md
---
# Quality Journey v3.2 — Tratamento do REV-COM-QJ-002

**PROPOSTA INTERNA — NÃO PUBLICAR, NÃO COTAR.** Correções técnicas do [parecer REV-COM-QJ-002](../revisoes/REV-COM-QJ-002-Parecer-Quality-Journey.md) da [PR #3](https://github.com/gentestsai-sudo/gentests-os/pull/3). Não são decisões de preço, margem, campanha, contrato ou catálogo. A PR #3 tem como base a branch da PR #2; não mesclar a PR #2 como oferta vigente por conveniência. [Consolidação v3.1](GenTests_Quality_Journey_v3_1_Consolidacao.md).

## 1. Fichas operacionais candidatas — QJ31-01

Os parâmetros de quantidade são **hipóteses para validação**, não escopos aprovados. Cada contratação deve delimitar insumos, ambiente, unidade de escopo, prazo, revisão, aceite e mudança de escopo. Contratação independente ou progressiva, sem etapa anterior obrigatória quando houver insumos suficientes.

### QA Start / Descobrir
- **Pergunta/público:** onde olhar primeiro? Empresa com problema ou ponto de atenção específico.
- **Unidade candidata:** um ponto delimitado de um produto, insumos existentes e alinhamento remoto inicial de até 20 minutos.
- **Entradas:** relato, objetivo, documentos/evidências existentes; sem credenciais por padrão.
- **Trabalho:** triagem documental, classificação preliminar de risco, redação, revisão e devolutiva.
- **Entrega:** nota com recorte, fontes, hipóteses separadas de fatos, até três prioridades candidatas, limitações e próximos passos.
- **Fora:** execução de testes, auditoria completa, investigação profunda, reteste, implementação e monitoramento.
- **Prazo/dependências:** definir na proposta a partir da disponibilização de insumos.
- **Revisão:** correção de erro material; ampliação de recorte é nova proposta.
- **Aceite:** nota identifica recorte, insumos, fundamentos, prioridades, limitações e se houve teste (por padrão, não).
- **Preço:** R$ 290 indicativo; regular/promocional pendente.

### QA Focus / Investigar
- **Pergunta/público:** o que acontece nesta jornada ou risco? Cliente com suspeita delimitada.
- **Unidade candidata:** uma jornada e variantes fechadas na proposta, em ambiente autorizado; quantidades a dimensionar antes da cotação.
- **Entradas:** critérios, ambiente, dados/credenciais autorizados e restrições de segurança.
- **Trabalho:** cobertura por risco, preparação, execução pactuada, evidências, análise, relatório e devolutiva.
- **Entrega:** cenários executados/não executados, ambiente e período, resultados, evidências pertinentes, achados reproduzíveis se houver, prioridades e bloqueios.
- **Fora:** cobertura integral, carga/segurança ofensiva, correção de código, reteste ilimitado, garantia de encontrar defeitos.
- **Prazo/dependências:** definir conforme estabilidade do ambiente, massa e variantes.
- **Revisão:** erro material no relatório; reteste somente se quantidade prevista no contrato.
- **Aceite:** status/cobertura por cenário, evidências ou justificativas, ambiente/período, limitações e classificação fundamentada; ausência de achados não garante ausência de falhas.
- **Preço:** R$ 650 indicativo; pendente.

### QA Evolution / Planejar
- **Pergunta/público:** o que melhorar e em qual ordem? Organização com problemas de processo/qualidade.
- **Unidade candidata:** um fluxo de entrega ou dimensão de qualidade, com áreas, entrevistas e artefatos previamente delimitados.
- **Entradas:** processo, papéis, amostras de requisitos/testes/bugs, indicadores e entrevistas autorizadas.
- **Trabalho:** diagnóstico, análise documental, entrevistas pactuadas, riscos/gaps, priorização, plano e devolutiva.
- **Entrega:** diagnóstico do recorte, mapa de riscos, backlog priorizado, dependências, responsáveis sugeridos e indicadores candidatos com definição/fonte.
- **Fora:** Focus completo, implantação, automação, operação e resultados quantitativos sem baseline.
- **Prazo/dependências:** pactuar entrevistas, profundidade, acesso e prazo.
- **Revisão:** uma rodada de esclarecimento do plano, sem incluir novos fluxos.
- **Aceite:** ações ligadas a riscos, critério de priorização, sequência, dependências, definição/fonte de indicadores e exclusões.
- **Preço:** R$ 1.200 indicativo; pendente.

### QA Implementation / Implementar
- **Pergunta/público:** como implantar melhorias priorizadas? Equipe com backlog selecionado.
- **Unidade:** projeto com lista fechada de itens e ambiente; identificar processo, automação, ferramenta, instrumentação ou código em cada item.
- **Entradas:** backlog, critérios de aceite, acessos autorizados, responsáveis e rollback quando aplicável.
- **Trabalho:** estimar por item, implantar, testar, demonstrar, documentar e transferir conhecimento.
- **Entrega:** itens pactuados demonstrados com evidências, documentação e handoff.
- **Fora:** funcionalidades extras, operação permanente, suporte ilimitado, garantia de zero falhas.
- **Prazo/dependências:** cronograma/marcos, ambientes e aprovações; mudança por aditivo.
- **Revisão:** corrigir desconformidade com critério contratado no prazo de aceite; evolução nova é escopo novo.
- **Aceite:** evidência por item e critério, demonstração, documentação, responsável e rollback se aplicável.
- **Preço:** orçamento individual; não oferecer horas ilimitadas.

### QA Excellence / Sustentar
- **Pergunta/público:** como medir adoção e manter evolução? Cliente com indicadores e melhorias implantadas.
- **Unidade:** ciclos com duração, frequência, indicadores, disponibilidade, canais e encerramento pactuados.
- **Entradas:** baseline, fontes de dados autorizadas, responsáveis e registros.
- **Trabalho:** análise por período, recomendações, devolutiva e ajustes leves apenas quando expressamente contratados.
- **Entrega:** relatório por ciclo com janela, fontes, indicadores, limitações, recomendações e devolutiva acordada.
- **Fora:** 24x7, SLA implícito, incidentes, novas implantações, suporte ilimitado e garantia de melhoria numérica.
- **Prazo/dependências:** definir ciclos, horário/canais, limites e renovação.
- **Revisão:** esclarecimento do relatório; análises extras exigem reorçamento.
- **Aceite:** relatório do ciclo, fonte/definição dos indicadores, período, limitações e devolutiva.
- **Preço:** orçamento por ciclo/escopo; recorrência somente mediante contrato.

**Regra transversal:** evidências e dados somente em ambiente autorizado, com segurança e revisão humana de qualquer análise apoiada por IA. Qualidade desde os requisitos, decisões baseadas em evidências e eficiência sustentável são objetivos, não resultados garantidos.

## 2. Viabilidade financeira reproduzível — QJ31-02

**Não chamar de esforço esperado.** Os tempos são hipóteses de *menor* e *maior esforço ilustrativo*, não estimativa comprovada ou teto de execução.

| Atividade (horas) | Start menor/maior | Focus menor/maior | Evolution menor/maior |
|---|---:|---:|---:|
| Alinhamento | 0,25 / 0,50 | 0,50 / 0,75 | 1,00 / 1,50 |
| Preparação e insumos | 0,50 / 0,75 | 0,75 / 1,25 | 2,00 / 3,00 |
| Investigação/análise | 0,50 / 1,25 | 2,00 / 3,25 | 3,00 / 5,00 |
| Evidências/relatório/plano | 0,40 / 0,75 | 0,75 / 1,25 | 2,00 / 3,00 |
| Revisão/retrabalho previsto | 0,25 / 0,50 | 0,50 / 0,75 | 1,00 / 2,00 |
| Devolutiva/comunicação | 0,10 / 0,25 | 0,50 / 0,75 | 1,00 / 1,50 |
| **Total** | **2 / 4** | **5 / 8** | **10 / 16** |

Premissas da v3.1: **R$ 69,92/h de custo de oportunidade imputado** (não custo contábil); despesas atribuídas hipotéticas **R$ 20/40/80**; DAS hipotético **6% ou 15,5%**, não alíquota confirmada. Não confundir preço-hora comercial com custo-hora nem duplicar rateios. Fórmula gerencial: `preço × (1 − DAS) − horas × 69,92 − custos atribuídos − aquisição atribuível − ociosidade atribuível`. Resultado gerencial com remuneração imputada **não é igual ao caixa incremental**, que depende de pagamentos, impostos efetivos e despesas desembolsadas. CAC e ociosidade não mensurados: usar sensibilidade de R$ 50 **adicionais hipotéticos**, não custo real.

| Preço e horas | 6% sem adicionais | 15,5% sem adicionais | 6% com R$ 50 adicionais | 15,5% com R$ 50 adicionais |
|---|---:|---:|---:|---:|
| Start R$ 290 / 2h | R$ 112,76 | R$ 85,21 | R$ 62,76 | R$ 35,21 |
| Start / 4h | −R$ 27,08 | −R$ 54,63 | −R$ 77,08 | −R$ 104,63 |
| Focus R$ 650 / 5h | R$ 221,40 | R$ 159,65 | R$ 171,40 | R$ 109,65 |
| Focus / 8h | R$ 11,64 | −R$ 50,11 | −R$ 38,36 | −R$ 100,11 |
| Evolution R$ 1.200 / 10h | R$ 348,80 | R$ 234,80 | R$ 298,80 | R$ 184,80 |
| Evolution / 16h | −R$ 70,72 | −R$ 184,72 | −R$ 120,72 | −R$ 234,72 |

Ponto de equilíbrio ilustrativo sem adicionais: Start **3,61h/3,22h** (6%/15,5%); Focus **8,17h/7,28h**; Evolution **14,99h/13,36h**. Não são tetos recomendados. Implementation e Excellence: não há preço ou escopo fechado para margem. Falta comprovar custos, aquisição, ociosidade, tributação efetiva por serviço e estimativa/piloto; direção precisa definir margem mínima e eventual subsídio.

## 3. Campanha e preços — QJ31-03

**Aviso de bloqueio para inserir nos pontos canônicos quando autorizado:** “A migração da Campanha dos Três Primeiros Clientes para a Quality Journey está em avaliação. R$ 490/1.490/2.490 pertencem a QA Express/Auditorias da PR #2; não valem automaticamente para Start/Focus/Evolution. R$ 290/650/1.200 são indicativos, ainda não classificados como regulares ou promocionais. Não cotar nem divulgar nova tabela até decisão formal.”

**Alternativa A:** manter campanha antiga restrita aos serviços antigos e criar tabela regular Quality Journey. **Alternativa B:** migrar campanha para a Journey e decidir preços regulares/promocionais, etapas elegíveis, três vagas compartilhadas ou outro limite, validade, reserva, cancelamento e contratos adicionais. Não inferir equivalência entre os serviços nem aprovação do pagamento 50/50. **Sem decisão da direção, não alterar o plano canônico PLN-COM-001, catálogo, índice, CRM ou site.**

## 4. Apresentação — QJ31-04

Preparada versão interna de 10 slides: `GenTests_Apresentacao_Comercial_Quality_Journey_v3_2_Revisao_Interna.pptx`, 50.690 bytes, SHA-256 `b228419977c3267a6b3696a25c40886fc9ffce6ff9ab0d5791750d6661760a48`. **Preços foram retirados do slide de entradas** até classificação regular/promocional; Implementation e Excellence continuam sob proposta, cadastro continua exemplo ilustrativo. Renderização local e teste de overflow passaram; isso **não equivale a revisão independente**. **PENDÊNCIA:** versionar o binário exato na PR #3 para que o revisor possa conferir hash, slides e legibilidade. Não alegar que o arquivo está no GitHub antes do upload. Peça não autorizada para envio.

## 5. Matriz de migração do site — QJ31-05

URLs conhecidas: https://gentests-site.pages.dev/ e https://gentests-site.pages.dev/quem-somos . **Conteúdo atual não inspecionado nesta execução**; páginas adicionais e textos atuais a levantar antes de executar.

| Ponto a inventariar | Proposta (NÃO publicada) | Bloqueio |
|---|---|---|
| Home / hero | “Qualidade de software, da descoberta à evolução contínua.” | Posicionamento aprovado |
| Home / serviços | Cinco etapas, pergunta, entrega e contratação independente | Escopos aprovados |
| Quem somos | Engenharia de qualidade, riscos, evidências, melhoria contínua; IA apenas se validada | Missão/visão/capacidades |
| Páginas de serviços, se existentes | Remapear ou preservar pacotes antigos | Destino do catálogo |
| Campanhas/preços, se existentes | Não exibir valores ou escassez pendentes | Tabela e vigência |
| Formulários/CTA, se existentes | “Converse com a GenTests.ai sobre seu desafio de qualidade.” | Processo/consentimento |
| Rodapé/metadados | Nomenclatura, links, SEO e acessibilidade consistentes | Inventário/testes |

Subtítulo sugerido: “Investigamos riscos, estruturamos melhorias e apoiamos sua implementação, conforme a necessidade do seu negócio.” Revisar conteúdo live, responsividade, acessibilidade e SEO antes de publicar.

## 6. Governança, rastreabilidade e resposta ao parecer — QJ31-06

- Parecer REV-COM-QJ-002, PR #3, revisou commit `6fcf8aac73d96ee55ce972037da0c0afb1a7c80f`.
- Consolidação v3.1: blob `05db53e0707c02b801f81a0712e32c9f84e074c6`; REV-COM-QJ-001: blob `df3dfdfc28c2176d1fbe6177b1be74263b3c20e1`.
- Plano canônico PLN-COM-001 0.3.0 herdado da PR #2. Não duplicar CRM nem declarar Obsidian sincronizado.
- Missão/visão/valores, GQF e 5S Digital estão em status **proposta**, não políticas formalmente aprovadas.
- QJ31-01: fichas candidatas preenchidas; **pendente** aprovação de quantidades/prazos.
- QJ31-02: tempos e custos hipotéticos reproduzíveis; **pendente** contabilidade, piloto, margem e custos reais.
- QJ31-03: conflito documentado; **pendente** decisão e atualização conjunta das fontes.
- QJ31-04: arquivo interno gerado/testado; **pendente** upload do binário e revisão independente.
- QJ31-05: matriz proposta; **pendente** inventário do site real e aprovação.
- QJ31-06: autoria, IDs, commits e dependência registrados; **pendente** índices/decisão/integração.
- Quality Gate estratégico: **não lançar ainda**; o menor experimento reversível é um piloto com esforço medido e escopo aprovado, sem promessa comercial pública.
