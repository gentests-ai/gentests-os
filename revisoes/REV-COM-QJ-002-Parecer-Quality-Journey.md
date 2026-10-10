---
id: REV-COM-QJ-002
tipo: parecer-revisao-independente
versao: 0.1.0
status: emitido
resultado: correcao-necessaria
data: 2026-10-10
timezone: America/Sao_Paulo
revisor: Codex
pr: 3
commit_revisado: 6fcf8aac73d96ee55ce972037da0c0afb1a7c80f
aprovacao_precos: nao-concedida
---
**Cópia de entrega do parecer registrado na PR:** https://github.com/gentestsai-sudo/gentests-os/pull/3#issuecomment-6099664427

# REV-COM-QJ-002 — Parecer independente sobre Quality Journey v3.1

**Versão do parecer:** 0.1.0 · **Data:** 10/10/2026 · **Revisor:** Codex, separado do executor da v3.1.  
**Resultado:** correção necessária antes de oferta vinculante ou publicação. Sustentabilidade dos preços e apresentação efetiva: não verificáveis integralmente com a evidência disponível. Não é homologação contábil, parecer jurídico ou aprovação da direção.

## Escopo e evidências

Revisão da [PR #3](https://github.com/gentestsai-sudo/gentests-os/pull/3), head **6fcf8aac73d96ee55ce972037da0c0afb1a7c80f**, base da PR **f047aa12275b66f7cdbc1ad2a291fd40650737e5** (branch da PR #2). A PR #3 adiciona um único Markdown, não um PPTX.

Documento avaliado: [GenTests_Quality_Journey_v3_1_Consolidacao.md na revisão examinada](https://github.com/gentestsai-sudo/gentests-os/blob/6fcf8aac73d96ee55ce972037da0c0afb1a7c80f/comercial/GenTests_Quality_Journey_v3_1_Consolidacao.md), blob **05db53e0707c02b801f81a0712e32c9f84e074c6**. Referência anterior: REV-COM-QJ-001, blob **df3dfdfc28c2176d1fbe6177b1be74263b3c20e1**, disponível na base da PR.

Também consultados QG-001 0.1.0, PRC-COM-001 0.1.0 e GOV-5S-001 0.1.0, todos com status proposta. São referências do processo solicitado, sem declará-los políticas formalmente aprovadas. A revisão financeira e os artefatos herdados da PR #2 foram considerados na comparação. O roteiro v3.1 foi avaliado; o binário v3.1 não foi localizado na árvore da PR nem na busca realizada de arquivos.

**Limites:** não conferi a documentação contábil integral, tributação efetiva do CNPJ, propostas assinadas ou CRM. A consulta à home e /quem-somos do site não retornou conteúdo acessível; avalio a estrutura proposta para o site, sem certificar o conteúdo publicado. Não executei alterações comerciais, merge ou publicação.

## Evolução em relação ao REV-COM-QJ-001

A v3.1 melhorou a distinção conceitual das cinco etapas; preservou contratação independente; diferenciou nota diagnóstica, investigação e plano; não equiparou serviços antigos aos novos; identificou a indefinição regular/promocional; recalculou cenários para os novos preços; manteve o exemplo ilustrativo e os avisos de proposta.

Esses avanços atendem parcialmente ao parecer anterior. A matriz ainda é sugerida: listar campos obrigatórios não equivale a preencher as cinco fichas. O conflito comercial está identificado, mas não decidido. Os cálculos são conferíveis, mas não demonstram viabilidade operacional.

## Achados e recomendações

Criticidade **alta**: impede afirmar prontidão para contratação/divulgação da condição afetada. **Média**: lacuna de implementação ou rastreabilidade a corrigir antes da passagem correspondente. Não há achado crítico de ação irreversível já executada.

### QJ31-01 — Alta: escopo e aceite não operacionalizados

**Evidência:** seção 2, especialmente a matriz e a linha 31. Start não define se inclui entrevista, acesso ou testes; Focus deixa jornadas, variantes e reteste abertos; Evolution não delimita dimensões/entrevistas; Implementation não define o tipo de intervenção; Excellence não define duração, frequência e suporte. Há entregáveis nominais, mas não critérios verificáveis de aceite por serviço.

**Impacto:** o cliente pode comprar interpretações diferentes do mesmo nome; quantidade de trabalho e retrabalho não sustentam um preço fixo.

**Correção objetiva:** preencher uma ficha por etapa, com unidade/quantidade de escopo, entradas, entregas mínimas, exclusões, dependências, prazo, esforço estimado, revisões, aceite e mudança de escopo. Para etapas sob proposta, fornecer parâmetros obrigatórios do orçamento, sem inventar preço fixo.

**Critérios sugeridos, a pactuar:**
- Start: nota identifica recorte, insumos, hipóteses versus evidências, limitações e prioridades; explicitar se houve teste.
- Focus: cobertura executada/não executada, ambiente/período, evidências aplicáveis e achados reproduzíveis quando houver. Ausência de achados não significa ausência de falhas.
- Evolution: ações priorizadas vinculadas a riscos, sequência/dependências e indicadores com definição; implantação excluída salvo contratação.
- Implementation: itens pactuados demonstrados em ambiente autorizado, com evidências de aceite, documentação e transferência; acesso/rollback quando aplicáveis.
- Excellence: entrega por ciclo, indicadores com fonte/período e reunião ou devolutiva pactuada; suporte e nova implantação delimitados.

**Direção:** escolher abrangência e posicionamento. **Executor:** traduzir a decisão em fichas e critérios; não deixar toda a definição para depois da venda.

### QJ31-02 — Alta: preços aritmeticamente consistentes, sustentabilidade não demonstrada

**Evidência:** seção 4. Recalculei os seis cenários: resultados e percentuais arredondados conferem. R$ 69,92/h é custo de oportunidade imputado; custos R$ 20/40/80 e horas 2/4, 5/8 e 10/16 são hipóteses novas sem evidência de estimativa por tarefa.

| Serviço/cenário | Horas | Resultado a 6% | Resultado a 15,5% |
|---|---:|---:|---:|
| Start R$ 290 — menor esforço | 2 | R$ 112,76 | R$ 85,21 |
| Start — maior esforço | 4 | −R$ 27,08 | −R$ 54,63 |
| Focus R$ 650 — menor esforço | 5 | R$ 221,40 | R$ 159,65 |
| Focus — maior esforço | 8 | R$ 11,64 | −R$ 50,11 |
| Evolution R$ 1.200 — menor esforço | 10 | R$ 348,80 | R$ 234,80 |
| Evolution — maior esforço | 16 | −R$ 70,72 | −R$ 184,72 |

**Ponto de equilíbrio ilustrativo**, mantendo exatamente as hipóteses da v3.1:
horas = [preço × (1 − tributo hipotético) − custo atribuído] / 69,92.

| Serviço | Equilíbrio a 6% | Equilíbrio a 15,5% |
|---|---:|---:|
| Start | 3,61 h | 3,22 h |
| Focus | 8,17 h | 7,28 h |
| Evolution | 14,99 h | 13,36 h |

Esses números não são tetos recomendados: representam resultado zero antes de custos adicionais não incluídos. No Focus de 8h/6%, R$ 11,64 já é uma folga muito pequena. Cenários menores são positivos dentro da fórmula, não prova de sustentabilidade real.

**Correção objetiva:** trocar “esperado” por “menor esforço ilustrativo” enquanto não houver estimativa/piloto. Abrir tempos por atividade e composição de custos, incorporar parcela atribuível de aquisição/revisão/ociosidade, esclarecer base do custo-hora e conferir tributação efetiva por serviço. Separar resultado econômico após remuneração imputada, custos desembolsados e caixa disponível: resultado gerencial negativo não comprova, sozinho, prejuízo de caixa.

**Tributação:** 6% e 15,5% são sensibilidades, não confirmação nem faixa exaustiva da empresa. Referência oficial de contexto: [LC 123, art. 18 e anexos](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm). A aplicação efetiva depende dos dados e enquadramento aplicáveis; nenhuma alíquota do CNPJ foi determinada neste parecer. Não colocar documentos sensíveis no repositório.

**Direção:** margem mínima, subsídio máximo de aquisição, eventual perda aceita e preços finais. **Contabilidade/executor:** base tributária e estimativas rastreáveis. Implementation e Excellence permanecem não verificáveis financeiramente até haver orçamento específico.

### QJ31-03 — Alta: conflito identificado, oferta corrente ainda ambígua

**Evidência:** seção 3 marca preços indicativos e alternativas A/B; seção 7 adia atualização do plano. Porém a base herdada da PR #2 continua descrevendo a campanha antiga como condição consolidada, enquanto a v3.1 a chama de histórico não automaticamente corrente.

**Avaliação do requisito:** a v3.1 identifica claramente o conflito, o que é correto. Não o resolve, e não deve inferir uma decisão ausente.

**Correção objetiva:** enquanto a decisão estiver pendente, acrescentar nos pontos de entrada do plano/oferta/índice um aviso de que a substituição está em avaliação, com link para esta proposta, sem apagar condições históricas. Antes da liberação comercial, registrar decisão única sobre tabela regular/promocional, serviços antigos, vagas, elegibilidade, vigência, reservas e cancelamentos; atualizar as fontes afetadas em conjunto.

**Direção:** escolher coexistência ou substituição e classificar os três preços. Sem essa decisão, não anunciar promoção nem tratar qualquer tabela como pronta para nova cotação.

### QJ31-04 — Alta: apresentação efetiva ausente e validação não reproduzível

**Evidência:** linha 82 declara renderização e teste de overflow executados; a descrição da PR informa que o PPTX v3.1 não foi versionado. A árvore examinada contém somente o PPTX anterior herdado da PR #2, não v3.1.

**Avaliação:** o roteiro de dez slides está coerente com a intenção da jornada e limita excessos (“itens pactuados”, ciclos, exemplo ilustrativo). Alinhamento do arquivo efetivo, contraste, legibilidade e cortes são **não verificáveis**. Não interpreto ausência de prova como prova de que o teste não ocorreu.

**Correção objetiva:** anexar/versionar o PPTX exato v3.1, registrar SHA-256, ligar roteiro e arquivo, e referenciar evidência de renderização/checagem. Submeter o mesmo arquivo à inspeção visual. Separar versão interna com valores indicativos da peça externa autorizada; nota “sujeito a escopo” não resolve sozinha preço indefinido.

**Direção:** autorizar peça/versão externa depois da revisão. Não atribuir aprovação visual ao revisor enquanto o binário não estiver disponível.

### QJ31-05 — Média: site implementável conceitualmente, migração não especificada

**Evidência:** seção 6 propõe hero, cartões e CTA, mas não mapeia páginas/conteúdos antigos que serão removidos, mantidos ou substituídos. O conteúdo live não pôde ser conferido.

**Avaliação:** a estrutura é implementável após delimitação comercial. Ela não assegura ausência de contradições entre home, serviços, sobre, páginas de campanha, formulários e materiais de apoio.

**Correção objetiva:** criar uma matriz “local atual → texto/oferta nova → decisão/versão fonte”, sem executar publicação. Reutilizar nomes em inglês com descrições em português; mostrar contratação independente; ocultar preços/urgência enquanto pendentes; explicitar resultados proporcionais. Implementation e Excellence precisam de limites públicos suficientes para não sugerir suporte ou implantação ilimitados.

**Direção:** aprovar posicionamento e destino das ofertas antigas. Após revisão, verificar responsividade/acessibilidade e consistência de todos os pontos comerciais, não apenas da home.

### QJ31-06 — Média: rastreabilidade parcial e dependência entre PRs

**Evidência:** há ID, versão, status proposta, referência ao parecer e PR empilhada sobre #2. O link do roteiro v3 aponta para uma branch mutável; o documento não identifica responsável pela elaboração nem referência verificável do binário/validação. A PR acrescenta uma nota, sem atualizar os índices e registros canônicos.

**Correção objetiva:** registrar autoria/responsável, congelar referências de origem em commits/blobs, ligar o parecer novo e indicar a dependência das PRs. Não integrar #2 com preços antigos como oferta vigente por conveniência da ordem de merge. Atualizar registro de decisão, evidências e índice quando a decisão ocorrer; preservar IDs e história. Versão numérica e estado separado são ajustes de padronização recomendados, sem reprovar conteúdo por nomenclatura isoladamente.

As duas verificações automáticas da PR passaram (“Verificar Markdown” e “Piloto QG Email Comercial”). Elas não validam escopo, margem, tributação, apresentação ou decisão humana. O respeito aos limites de autonomia é positivo: PR draft, sem alegação de publicação ou sincronização local concluída.

## Decisões e saída esperada

**Da direção:** preços regulares/promocionais; campanha e vagas; destino dos serviços antigos; limites de oferta; margem/subsídio; condições de contratação; autorização externa da versão.

**Do executor, sem esperar nova escolha estratégica:** preencher alternativas/fichas propostas, tornar cálculos reproduzíveis, fornecer o binário exato e evidências, corrigir avisos de pendência e referências.

**De validação especializada:** enquadramento/tributação e condições fiscais/contratuais pertinentes, sem substituir esses pareceres por simulação gerencial.

Revalidar os seis achados na revisão seguinte. Parecer independente em relação ao executor da v3.1; não equivale a auditoria profissional certificada ou aprovação da oferta. Nenhum preço aprovado, arquivo comercial alterado, merge realizado ou site publicado por este revisor.

