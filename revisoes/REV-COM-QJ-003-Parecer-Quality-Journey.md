---
id: REV-COM-QJ-003
tipo: parecer-revisao-independente
versao: 0.1.0
status: emitido
resultado: correcao-necessaria
data: 2026-10-10
timezone: America/Sao_Paulo
revisor: Codex
pr: 3
branch: review/quality-journey-v3-1
commit_revisado: 01e614670381da56f035e67f72b2fedc13061833
parecer_anterior: REV-COM-QJ-002
aprovacao_precos: nao-concedida
aprovacao_visual: nao-concedida
---
# REV-COM-QJ-003 — Revalidação da Quality Journey v3.2

## Conclusão e alcance

**A jornada é estrategicamente coerente como portfólio e melhorou como especificação comercial. Ainda não é oferta liberada para contratação ou divulgação.** Uma das seis correções pode ser encerrada em seu alcance documental; quatro estão parcialmente resolvidas e a apresentação permanece pendente.

Revisão independente do executor da v3.2, com olhar de marketing, comercial, qualidade e alinhamento estratégico. Não constitui homologação contábil, parecer jurídico, validação de mercado ou aprovação da direção. Apenas este parecer é registrado; documentos comerciais, CRM, site e pareceres anteriores permanecem preservados. PR #3 deve continuar aberta, sem merge, até autorização expressa.

## Evidências e referência examinada

- [PR #3](https://github.com/gentestsai-sudo/gentests-os/pull/3), head **01e614670381da56f035e67f72b2fedc13061833**, base **f047aa12275b66f7cdbc1ad2a291fd40650737e5**, empilhada sobre a branch da PR #2.
- [Tratamento GT-COM-QJ-003 v3.2.0](https://github.com/gentestsai-sudo/gentests-os/blob/01e614670381da56f035e67f72b2fedc13061833/comercial/GT-COM-QJ-003-Tratamento-REV-COM-QJ-002.md), blob **3c11e4b811f4134a2210c5336829f822503e50fe**: seis seções lidas integralmente.
- REV-COM-QJ-002 0.1.0 e consolidação v3.1: histórico e critérios anteriores; a v3.1 recebeu aviso de revisão superveniente.
- PLN-COM-001 0.3.0, blob **488cc238de80c6ea357dad1e95359ae0a1670805**: plano canônico ainda descreve a proposta da campanha antiga.
- Missao-Visao-Valores 0.1.0, blob **c40c21a46411d556b86cfe9d72544c3d8d8837ed**; GOV-5S-001 0.1.0, blob **8759d58860dd38402767685861947d6c3c6c5c4f**; GQF-001 0.1.0, blob **090d80a515cbd8cd3225c198efecbe0820ad3072**; QG-STR-001 0.1.0, blob **6cd8dda92cff3f97e3d07067a4a91413d4e24a14**. Todos em proposta.
- Documento institucional **GenTests_Identidade_Institucional_Visao_Missao_Valores.docx**, versão 1.0 de 09/10/2026, versão armazenada 1, ID **libfile_d646830de6088191b87217c5db8ab812**, quatro páginas lidas. Também é minuta para aprovação.
- Árvore da branch inspecionada: não contém o PPTX exato v3.2. O hash informado pelo executor é declaração rastreável, não hash conferido pelo revisor.
- As verificações automáticas “Verificar Markdown” e “Piloto QG Email Comercial” passaram no commit examinado. Não demonstram viabilidade comercial ou revisão visual.

Não foram reconsultados contabilidade integral, CRM ou site publicado. Avaliação de site limitada à matriz proposta, não auditoria das páginas live. Evidências sobre renderização do novo PPTX não foram disponibilizadas para reprodução.

## Reavaliação individual

| Achado anterior | Classificação | Evidência e justificativa | Encerramento |
|---|---|---|---|
| **QJ31-01 — Escopo e aceite** | **Parcialmente resolvido** | Seção 1 preenche cinco fichas, distingue entregas, limita testes no Start e define aceite. Ainda deixa volume de insumos, variantes, entrevistas, revisão e prazos em aberto. | Encerrar somente após especificação candidata executável e decisão sobre a oferta a liberar; não exigir escopos padronizados artificiais para serviços sob orçamento. |
| **QJ31-02 — Viabilidade financeira** | **Parcialmente resolvido** | Seção 2 decompõe atividades, corrige “esperado”, distingue resultado gerencial de caixa e adiciona sensibilidade de aquisição/ociosidade. Totais e valores conferem. Custos e tempos continuam hipotéticos; sustentabilidade não demonstrada. | A correção aritmética está atendida. O achado amplo permanece até estimativa fundamentada, base tributária/custos e decisão de margem/subsídio. |
| **QJ31-03 — Campanha/tabela corrente** | **Parcialmente resolvido** | Seção 3 preserva alternativas e impede equivalência automática; v3.1 agora tem aviso de superação. O aviso para plano/oferta/índice foi redigido, mas não aplicado; o plano herdado ainda apresenta a tabela anterior. | Direção decide coexistência/substituição e regular/promocional; depois, atualizar fontes conjuntamente. Não inferir decisão. |
| **QJ31-04 — Apresentação efetiva** | **Pendente** | Seção 4 informa nome, tamanho e SHA-256 e relata remoção de preços. O binário não está na árvore examinada. | Versionar arquivo exato e evidências; conferir hash e slides antes de qualquer aprovação visual. |
| **QJ31-05 — Migração do site** | **Parcialmente resolvido** | Seção 5 fornece matriz por ponto, textos candidatos e bloqueios. Falta inventário real, conteúdo anterior e decisão/versão fonte por substituição. | Fechar inventário e mapeamento sem publicar; execução/autorização são etapas posteriores. |
| **QJ31-06 — Rastreabilidade** | **Resolvido, no alcance documental da correção** | YAML identifica responsável, versão numérica e estado; seção 6 fixa commits/blobs e dependência #2 → #3; histórico preservado e v3.1 sinalizada como anterior. | Pode encerrar a falha de autoria/proveniência/dependência. Não encerra QJ31-04 nem substitui a atualização de índices e decisão após homologação. |

Não confundir “resolvido documentalmente” com oferta aprovada ou PR autorizada para merge.

## Executabilidade e ajustes do executor

**Start:** já tem início (insumos/alinhamento), meio (triagem e redação) e fim (nota com aceite). É o candidato mais simples a pilotar. Delimitar tamanho/quantidade de insumos, formato da nota, canal/duração da devolutiva e revisão. O alinhamento de “até 20 minutos” é compatível com uma hipótese de 15 minutos no cenário menor; não é erro aritmético. Entretanto, seis minutos para devolutiva/comunicação no cenário menor precisam ser testados.

**Focus:** o relatório e o aceite são úteis e verificáveis; “uma jornada” não mede complexidade por si só. Preparar modelo que obrigue a preencher início/fim, variantes, perfis, integrações, massa, bloqueios e quantidade de retestes antes da cotação. Não transformar “retorno com falhas corrigidas” em reteste incluído.

**Evolution:** o plano distingue diagnóstico de execução de testes e implantação. Delimitar amostras, participantes, entrevistas e profundidade; separar fonte de indicador disponível de fonte apenas recomendada. A rodada de esclarecimento precisa de duração/limite.

**Implementation:** adequadamente sob orçamento por lista de itens. Acrescentar responsável por cada aceite, janela de validação, dependências e tratamento de bloqueios; “corrigir desconformidade” deve ter regra operacional de escopo e prazo. Processo, automação e código não são intervenções equivalentes em risco ou capacidade.

**Excellence:** corretamente por ciclo, com exclusão de 24x7 e suporte implícito. Definir duração, frequência, quantidade de indicadores, disponibilidade e o que conta como “ajuste leve”. Sem baseline/fontes válidas, propor levantamento específico ou restringir análise; não fabricar resultados.

Esses pontos são correções de proposta que o executor pode preparar. Escolher limites comerciais e aceitá-los cabe à direção; prazo concreto por cliente depende de escopo/capacidade. Não é necessário fechar toda a implantação futura para liberar um único piloto de Start, mas esse piloto precisa dos seus próprios limites, preço e autorização.

## Conferência financeira

Somatórios das seis atividades: **Start 2/4h; Focus 5/8h; Evolution 10/16h**, corretamente. Recalculados os **24 resultados** (seis linhas × quatro condições), sem divergência de centavos; pontos de equilíbrio sem adicionais também conferem.

| Serviço e esforço | 6%, sem adicionais | 15,5%, sem adicionais | 6%, + R$ 50 | 15,5%, + R$ 50 |
|---|---:|---:|---:|---:|
| Start, 2h | R$ 112,76 | R$ 85,21 | R$ 62,76 | R$ 35,21 |
| Start, 4h | −R$ 27,08 | −R$ 54,63 | −R$ 77,08 | −R$ 104,63 |
| Focus, 5h | R$ 221,40 | R$ 159,65 | R$ 171,40 | R$ 109,65 |
| Focus, 8h | R$ 11,64 | −R$ 50,11 | −R$ 38,36 | −R$ 100,11 |
| Evolution, 10h | R$ 348,80 | R$ 234,80 | R$ 298,80 | R$ 184,80 |
| Evolution, 16h | −R$ 70,72 | −R$ 184,72 | −R$ 120,72 | −R$ 234,72 |

Com os R$ 50 adicionais, o equilíbrio ilustrativo cai para **2,90/2,50h no Start; 7,45/6,57h no Focus; 14,27/12,64h no Evolution** (6%/15,5%). Não são limites aprovados nem recomendação de reduzir artificialmente o trabalho.

**Correções adicionais:** abrir a composição dos R$ 20/40/80 e definir se os R$ 50 representam aquisição e ociosidade somadas; evitar sobreposição com horas/rateio. Registrar a metodologia da ociosidade para não contá-la de novo no custo-hora. Separar tempo de prospecção pré-venda do alinhamento pós-contratação. Medir piloto antes de chamar qualquer cenário de previsão.

**Conclusão:** preços indicativos produzem resultado gerencial positivo apenas sob determinadas hipóteses de menor esforço; os cenários maiores permanecem frágeis/negativos. A direção pode deliberar margem reduzida, mas precisa de um orçamento de aquisição/subsídio limitado, não de perda indefinida. Tributos de 6%/15,5% são sensibilidades; nenhuma alíquota do CNPJ foi validada. Referência fiscal de contexto permanece a LC 123, art. 18 e anexos, já indicada no parecer anterior, sem determinação de enquadramento. Resultado após remuneração imputada não é lucro fiscal nem caixa.

## Alinhamento institucional, marketing e excelência enxuta

Há duas formulações institucionais propostas, convergentes, mas distintas:

- **GitHub:** missão centrada em engenharia de qualidade, IA, melhoria contínua, riscos e desperdícios; visão de referência em Quality Engineering e governança orientada por IA.
- **Documento institucional v1.0:** missão centrada em fricções e experiência digital, diagnósticos e produtos confiáveis, acessíveis e eficientes; visão de referência em Quality Intelligence, conectando usuário, engenharia e negócio.

Não elejo uma como vigente nem declaro uma incompatível com a outra. A direção deve reconciliar e registrar a referência institucional antes de falar em alinhamento a uma política aprovada.

| Diretriz/valor | Evidência na v3.2 | Avaliação e ajuste |
|---|---|---|
| Missão: diagnosticar riscos e melhorar produtos | Start/Focus investigam; Evolution prioriza; Implementation executa; Excellence acompanha | Alinhamento conceitual forte. Incluir problema do usuário e decisão de negócio no recorte, sem ampliar automaticamente o serviço. |
| Visão: referência em QE/Quality Intelligence, IA responsável e resultados mensuráveis | Jornada une investigação, processo e indicadores; análise apoiada por IA tem revisão humana | Direção coerente, maturidade ainda não comprovada. Não vender GQF ou agente IA como produto consolidado/certificação. |
| Evidência, rigor e transparência | Hipóteses separadas de fatos; cobertura/limites; cenários financeiros assumidos | Atendido na intenção; falta prova de execução e do PPTX. |
| Empatia pelo usuário/valorização das pessoas | Público descrito sobretudo como empresa/organização | Parcial: incluir sinais de fricção, acessibilidade quando pertinente, impacto humano e linguagem compreensível. Isso não obriga auditoria de acessibilidade em todos os pacotes. |
| Qualidade desde a origem | Evolution usa requisitos e processo; Implementation corrige melhorias pactuadas | Coerente; confirmar que prioridades considerem prevenção, não apenas achar defeitos. |
| Segurança, privacidade e integridade | Acesso autorizado, IA revisada, exclusões e ausência de garantias | Coerente como regra; aplicar procedimentos existentes de dados/evidências sem criar nova política paralela. |
| Eficiência sustentável e impacto no negócio | Escopos candidatos, horas e análise de margem | Ainda condicional: esforço real/capacidade e aquisição precisam de medição. Preço baixo por si só não comprova eficiência. |
| Aprendizado/melhoria contínua | Excellence, piloto e tempos mensuráveis | Definir métrica de valor percebido, clareza, retrabalho, prazo e resultado por projeto; não prometer efeito financeiro causal sem base. |
| 5S/GQF/Disciplina estratégica | Contratação independente, histórico e gates; piloto sugerido | Evitar amadurecer as cinco ofertas e o site simultaneamente. Reutilizar o plano/CRM existentes, priorizar um experimento e consolidar avisos de versão. |

**Parecer de marketing/comercial:** a jornada comunica progressão e cria portas de entrada independentes. O benefício precisa ser expresso como decisão ajudada, evidência recebida e risco delimitado, não como número de documentos. Start é triagem paga, não investigação técnica completa; deixar essa distinção clara para evitar venda inadequada.

**Contraditório estratégico:** ainda não há evidência de demanda ou valor percebido que justifique lançar os cinco níveis de uma vez. Ampliar Implementation/Excellence pode comprometer capacidade e dispersar a aquisição inicial. Recomenda-se preparar um piloto limitado, com hipótese, métrica, prazo e esforço, submetido à direção — não lançamento automático nem trabalho gratuito presumido.

## Riscos novos ou persistentes e responsáveis

| ID | Criticidade | Problema | Correção do executor | Decisão da direção |
|---|---|---|---|---|
| **QJ32-01** | Alta para venda | Insumos/revisões sem limite podem exceder esforço, especialmente Start | Propor limites, início/saída, devolutiva, janelas de revisão/aceite e regra de bloqueio; manter preços indicativos | Escolher limites, capacidade, preço e eventual subsídio |
| **QJ32-02** | Média | Start exclui testes, mas aceite diz “se houve teste (por padrão, não)”; pode sugerir exceção incluída | Tornar texto inequívoco: sem execução de testes no Start candidato; investigação requer escopo separado aprovado | Deliberar mudança de serviço apenas se desejada |
| **QJ32-03** | Média estratégica | Duas formulações institucionais sem referência vigente definida | Apresentar comparação e proposta de reconciliação; não sobrescrever identidade | Escolher/aprovar missão, visão e valores de referência |
| **QJ32-04** | Média | Matriz do site é roteiro de inventário, não inventário realizado; não identifica textos anteriores/versões fontes | Levantar URLs, conteúdos, ação manter/substituir/retirar e fonte da decisão, sem publicar | Destino do catálogo e posicionamento |
| **QJ32-05** | Média documental | Título/descrição da PR ainda enfatizam v3.1/PPTX v3.1, embora haja tratamento v3.2 | Atualizar metadados da PR e lista de artefatos na próxima rodada; aviso de pendência não decide campanha | Autorização de integração permanece separada |

QJ32-02 é uma ambiguidade textual, não evidência de teste não autorizado já executado. QJ32-03 identifica divergência de referência, não quebra comprovada de valores. Falta de binário não prova falsidade do relato de renderização, mas impede validá-lo.

## Separação de responsabilidades e condições de saída

**Executor:** completar propostas operacionais; compor custos; propor limites/aceite e método do piloto; fornecer binário e evidências; inventariar site; atualizar referências/metadados. Não precisa aguardar decisão para preparar alternativas, mas não pode escolhê-las como aprovadas.

**Direção:** referência institucional; oferta inicial/prioridade; preços regulares/promocionais; destino dos serviços antigos; campanha/vagas; limites de capacidade; margem/subsídio; contrato/pagamento e autorizações de uso externo/merge.

**Validação especializada:** confirmar tributação aplicável e condições fiscais/contratuais; decisão da direção não transforma hipótese em fato tributário.

**Pode encerrar:** QJ31-06 no alcance de rastreabilidade da rodada; subcorreções aritméticas e a existência das cinco fichas estão comprovadas, sem encerrar os achados amplos QJ31-01/02.
**Revalidar:** QJ31-01/02/03/05 e QJ32-01 a QJ32-05 quando tratados.
**Permanece não verificável:** aprovação visual/alinhamento efetivo do PPTX e sustentabilidade financeira real.
**Não realizado:** merge, publicação, alteração de CRM, homologação de preços ou edição de documentos comerciais pelo revisor.

A PR #3 permanece aberta e sem merge até autorização expressa. Este parecer mantém o histórico de REV-COM-QJ-001/002 e avalia apenas a revisão fixada acima.
