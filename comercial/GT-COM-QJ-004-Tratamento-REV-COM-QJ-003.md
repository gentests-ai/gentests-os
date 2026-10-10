---
id: GT-COM-QJ-004
tipo: tratamento-parecer-e-proposta-operacional
versao: 3.2.1
status: proposta
estado_documental: aguardando-revisao-independente
data: 2026-10-10
timezone: America/Sao_Paulo
responsavel_elaboracao: Codex-executor
aprovador: Direcao
aprovacao: pendente
parecer_origem: revisoes/REV-COM-QJ-003-Parecer-Quality-Journey.md
tratamento_anterior: comercial/GT-COM-QJ-003-Tratamento-REV-COM-QJ-002.md
pr: 3
branch: review/quality-journey-v3-1
head_anterior: 021f9608d2abdd62e00e0b61a68145ff98b48e4d
homologacao_precos: nao
aprovacao_visual: nao
autorizacao_piloto: pendente
---
# Quality Journey v3.2 — Tratamento do REV-COM-QJ-003

**PROPOSTA INTERNA — NÃO COTAR, NÃO COMERCIALIZAR, NÃO PUBLICAR.** Esta rodada prepara correções e decisões; não libera os cinco serviços nem executa o piloto. Os limites abaixo são candidatos para aprovação, não alterações em contratos vigentes. Codex atua como executor e não emite revisão independente das próprias correções.

## 1. Origem, precedência e resposta aos achados

Referências: [REV-COM-QJ-003](../revisoes/REV-COM-QJ-003-Parecer-Quality-Journey.md), blob `7a11cba3d08e12b87ed8f86314049bcd41369256`; [GT-COM-QJ-003](GT-COM-QJ-003-Tratamento-REV-COM-QJ-002.md), blob `3c11e4b811f4134a2210c5336829f822503e50fe`; [PR #3](https://github.com/gentestsai-sudo/gentests-os/pull/3), empilhada sobre a [PR #2](https://github.com/gentestsai-sudo/gentests-os/pull/2), base `f047aa12275b66f7cdbc1ad2a291fd40650737e5`. Pareceres e tratamentos anteriores permanecem intactos. Esta nota complementa e corrige especificações candidatas anteriores; não substitui decisões aprovadas. Em caso de conflito comercial ainda não decidido, interromper a cotação e solicitar decisão, sem eleger um preço pelo documento mais recente.

| Achado | Correção apresentada pelo executor | Evidência nesta rodada | Residual / responsável |
|---|---|---|---|
| QJ31-01 / QJ32-01 | Insumos, revisões, devolutivas, bloqueios e aceite definidos | §2, §4 | Direção escolhe limites; revisor revalida executabilidade |
| QJ31-02 | Composição candidata, método sem duplicação, registro de esforço e margens | §3, §4 | Dados reais, contador e decisão de margem/subsídio continuam pendentes |
| QJ31-03 | Alternativas preservadas; avisos de conflito adicionados aos pontos canônicos | §5; índice, plano e oferta antiga | Direção decide catálogo, campanha e tabela; nenhuma alternativa selecionada |
| QJ31-04 | Binário exato e dez PNGs disponibilizados; hash conferido | §6; manifesto e arquivos vinculados | Revisão visual independente; ocorrência no slide 2 não corrigida no binário exato |
| QJ31-05 / QJ32-04 | Quatro páginas públicas inventariadas e conteúdo real mapeado | §7; inventário JSON | Páginas fora da navegação, fluxos dinâmicos e QA de futura mudança não examinados |
| QJ32-02 | Start exclui testes sem exceção implícita | §2.2, §4 | Mudança dessa fronteira exigiria nova proposta e decisão |
| QJ32-03 | Comparação e texto conciliador candidato | §8 | Direção escolhe a referência; fontes institucionais preservadas |
| QJ32-05 | Título/descrição da PR atualizados para v3.2 e entregas efetivas | Metadados da PR #3 | Aprovação de integração continua separada |
| QJ31-06 | Rastreabilidade preservada | IDs, fontes e dependência #2 → #3 | Encerrado pelo REV-COM-QJ-003 apenas no alcance documental; não reaberto nem ampliado |

“Correção apresentada” não significa achado encerrado por revisão independente. O novo revisor decide o encerramento e sua extensão com base no commit desta rodada.

## 2. Especificações operacionais candidatas

### 2.1 Regras comuns

Cada proposta específica registra produto, problema do usuário/decisão de negócio, recorte, versão, responsável técnico e responsável pelo aceite do cliente. Confirmar capacidade, competência e ausência de conflito de interesse antes de contratar. Etapas são independentes; não exigir compra das anteriores quando as entradas forem suficientes.

- **Entrada:** insumos legíveis, autorização, interlocutor, ambiente e recorte aceitos por escrito. Não receber credenciais em documentos. Dados minimizados e evidências sanitizadas conforme procedimentos existentes; IA somente quando autorizada, com revisão humana e ferramenta adequada aos dados.
- **Início/prazo:** contar após confirmação de entrada completa e capacidade reservada. Janelas abaixo são candidatas; não prazo vinculante antes da proposta aprovada. Hora de espera não é hora de execução; registrar comunicação e remobilização separadamente.
- **Bloqueio:** comunicar no canal pactuado em até um dia útil após identificação, apontar causa, impacto e próxima ação. Suspender etapa afetada; após três dias úteis sem resposta, propor replanejamento. Suspensão, cobrança, cancelamento e retomada dependem de contrato validado; não aplicar automaticamente.
- **Aceite:** cliente revisa em três dias úteis da entrega (cinco para Implementation), devolvendo lista consolidada de desconformidades com referência ao critério. Silêncio não equivale a aceite. Sem retorno, registrar pendência e combinar data; não assumir aprovação ou recebimento.
- **Revisão:** uma rodada consolidada no recorte, com limite de esforço incluído indicado por serviço. Correção de desconformidade imputável ao executor não se transforma automaticamente em nova cobrança nem é dispensada quando esgotar o orçamento interno. Registrar retrabalho e impacto; direção trata exceção/capacidade, preservadas obrigações contratuais.
- **Mudança:** novos insumos, jornadas, variantes, ambientes, entrevistas, testes, prioridades ou itens após congelamento são avaliados por impacto. Preparar alteração com preço, esforço, prazo e critérios; executar somente após autorização específica. Sem acordo, manter o recorte original e registrar a limitação, se a entrega ainda for possível.
- **Conclusão:** entrega identificada, evidências/limitações, devolutiva e aceite explícito ou registro da divergência. Recomendar serviço seguinte não o inclui. Não garantir defeitos encontrados, ausência de falhas, certificação, conversão, receita ou melhora causal de indicadores.

### 2.2 QA Start — Descobrir

**Finalidade:** ajudar a escolher onde investigar primeiro, mediante triagem de insumos já existentes. **Não inclui execução de testes** manuais ou automatizados, navegação exploratória, reprodução de falha, consulta a ambiente, auditoria ou validação de hipótese. Links servem para identificar a fonte; avaliar a página/sistema por interação é outro escopo. O aceite anterior “se houve teste” fica corrigido por esta fronteira explícita.

**Unidade/entrada:** um produto, um problema e um interlocutor; relato estruturado de até uma página, mais até cinco páginas de documentos existentes e três capturas existentes, legíveis e sanitizadas. Sem vídeos, bases de dados, análise de logs extensos, entrevistas adicionais ou credenciais. Envio consolidado; documento maior precisa de extrato escolhido pelo cliente. Não somar uma segunda jornada ou problema.

**Execução/entrega:** alinhamento remoto de até 20 minutos; nota diagnóstica de até duas páginas com fontes, fatos relatados/observados apenas nos insumos, hipóteses, até três prioridades fundamentadas, lacunas, limitações e próximos passos. Não inventar três prioridades se os dados não as sustentarem. Devolutiva remota de até dez minutos; uma rodada consolidada de esclarecimento/correção, orçamento de 15 minutos. Novo diagnóstico não é revisão incluída.

**Prazo candidato:** até três dias úteis após entrada completa e capacidade confirmada. **Aceite:** todas as seções preenchidas ou lacuna explicitada, fontes identificadas, fatos separados de hipóteses e ausência de alegação de teste executado. Discordância de prioridade não é, isoladamente, defeito; fundamento incorreto ou seção faltante é desconformidade. Preço R$ 290 é somente hipótese da análise financeira. Piloto detalhado em §4.

### 2.3 QA Focus — Investigar

**Unidade candidata:** uma jornada com início/fim explícitos, até seis passos de negócio, um perfil, um ambiente, um navegador/versão desktop, até cinco cenários totais (incluindo variantes), um conjunto de massa sintética e até uma integração em sandbox já disponível. Um cenário tem pré-condição, ação e esperado. Mais passos/variantes não entram por serem chamados de “uma jornada”. Não inclui mobile/matriz de dispositivos, carga, pentest, acessibilidade completa, automação, correção ou reteste após mudança do produto.

**Entrada congelada antes da cotação:** jornada, cenários/esperados, acesso autorizado de teste, restrições, massa, dependências e estabilidade confirmada. Até cinco páginas de critérios e um alinhamento de 30 minutos. Definir explicitamente operação destrutiva/pagamento proibidos; autorização genérica não autoriza transações reais. Incompatibilidade com a estimativa exige redimensionamento antes da venda.

**Entrega/aceite:** relatório único, até cinco páginas mais anexos sanitizados, com status de cada cenário, ambiente/período, esperado/obtido, evidência ou motivo do bloqueio, achados reproduzíveis quando houver, prioridade e limites. Devolutiva até 30 minutos, uma rodada de esclarecimento até 30 minutos. Reexecutar para confirmar a observação durante a execução original é incluído; retestar produto corrigido não é. Zero achados pode ser entrega válida. Cenário bloqueado não vira “passou” nem entrega completa automaticamente: responsável decide desbloqueio/replanejamento ou redução escrita do recorte. Prazo candidato até cinco dias úteis após entrada. R$ 650 indicativo; esforço de 5–8h continua hipótese, não teto automaticamente viável para qualquer jornada.

### 2.4 QA Evolution — Planejar

**Unidade candidata:** um fluxo de entrega de uma equipe, até três participantes, duas entrevistas de até 30 minutos cada, até cinco artefatos/amostras somando 20 páginas, até três indicadores existentes e uma janela de dados definida na proposta. Não extrair/limpar bases ou criar baseline neste pacote. Uma reunião inicial de até 30 minutos; dúvidas documentais consolidadas em um retorno do interlocutor.

**Entrega:** diagnóstico de até oito páginas, mapa de riscos, até dez ações priorizadas com fundamento, sequência, dependências e responsáveis sugeridos. Até três indicadores com fórmula, unidade, fonte, período e qualidade da fonte; separar “disponível” de “recomendado, ainda sem dados”. Não inventar números nem atribuir resultado causal. Uma devolutiva até 45 minutos e uma rodada de esclarecimento até 30 minutos.

**Aceite:** cada ação ligada a risco/lacuna, critérios de priorização explícitos, plano executável dentro das dependências relatadas e indicadores definidos ou lacunas identificadas. Sem testes de Focus, implementação, automação ou acompanhamento. Prazo candidato até dez dias úteis após acesso e agenda. R$ 1.200 indicativo; 10–16h hipotéticas, preço/limites sujeitos a medição e decisão.

### 2.5 QA Implementation — Implementar

Não criar pacote universal nem número fictício de itens. **Cotação só é possível com ficha por item:** ID/tipo (processo, ferramenta, automação, instrumentação ou código); entrada/saída; competência; ambientes; dependência e seu responsável; esforço e custo; critério verificável; evidência; responsável técnico pela validação e responsável do cliente pelo aceite; marco e janela; documentação/handoff e rollback quando aplicável. Nenhum campo essencial pode ficar “a definir” em proposta vinculante.

**Entrega/limites:** lista fechada assinada, evidenciação por item e demonstração/handoff com quantidade/duração expressas no orçamento. Uma rodada consolidada de validação em cinco dias úteis por marco; orçamento de correção e janela de resposta especificados por item, sem eliminar dever de corrigir desconformidade. Janela técnica inicial candidata de até três dias úteis para diagnosticar divergência, depois plano de correção acordado. Novas funcionalidades, evolução e operação permanente excluídas. Bloqueio de integração não se compensa silenciosamente com outro item. Sem lista e competência confirmadas, estacionar a oferta, não prometer implantação genérica.

### 2.6 QA Excellence — Sustentar

**Referência candidata para orçamento:** um ciclo de 30 dias corridos, um produto/equipe, até três indicadores com fonte e baseline disponíveis, duas reuniões remotas de até 30 minutos e um relatório de até quatro páginas. Atendimento documental assíncrono em dias úteis, resposta inicial em até dois dias úteis, sem plantão, incidente ou SLA de recuperação. Início/fim, horas máximas, disponibilidade e renovação precisam constar no orçamento; ciclo não renova automaticamente.

**“Ajuste leve”:** apenas atualização de definição de indicador ou orientação documental no mesmo recorte, até um item e 30 minutos por ciclo, se contratado. Não alterar código, pipeline, automação, infraestrutura ou extrair nova base sob esse rótulo. Uma rodada de esclarecimento do relatório até 30 minutos. Sem baseline válida, relatório pode identificar lacuna; comparação de evolução só com dados comparáveis. Preparar baseline requer escopo próprio.

**Aceite:** janela/fontes, cálculos reproduzíveis, limites de comparabilidade, recomendações e devolutivas pactuadas. Não exigir melhora numérica para aceite. Sob orçamento por ciclo, considerando esforço total; teto de horas é decidido na cotação, sem promessa de disponibilidade ilimitada.

## 3. Custos, esforço e modelo de medição — QJ31-02

### 3.1 Dados conhecidos versus hipóteses

R$ 69,92/h é **remuneração/oportunidade imputada**, não custo contábil validado. R$ 290/650/1.200 são indicativos. Tributos 6% e 15,5% são sensibilidades; nenhum enquadramento do CNPJ foi confirmado nesta execução. A rodada não teve acesso à base contábil integral. Não inferir sustentabilidade pelo cenário mais barato.

Os envelopes R$ 20/40/80 não tinham composição real comprovada. Para tornar o cálculo auditável, propõe-se a seguinte **abertura exclusivamente ilustrativa**, mantendo os totais anteriores; não é levantamento de despesas nem orçamento homologado:

| Componente | Start | Focus | Evolution | Como substituir por dado real |
|---|---:|---:|---:|---|
| Uso incremental de tecnologia/IA/armazenamento | R$ 5 | R$ 10 | R$ 20 | Consumo atribuível e comprovante; revisão humana nas horas |
| Parcela de despesas fixas não humanas | R$ 15 | R$ 30 | R$ 60 | Pool mensal e critério de rateio aprovado; excluir consumo já alocado |
| **Envelope base hipotético** | **R$ 20** | **R$ 40** | **R$ 80** | Não denominar custo real |
| Taxas de recebimento, terceiros, deslocamento e extras | Não medidos | Não medidos | Não medidos | Acrescentar valores reais aplicáveis; zero somente se comprovadamente inaplicável |

Nos cenários publicados, extras não medidos foram omitidos, não provados inexistentes. A abertura não demonstra por que os custos seriam esses: é uma composição candidata para teste e deve ser substituída antes de decidir margem real.

Para reproduzir a sensibilidade de R$ 50 adicionais, usar **R$ 20 de aquisição + R$ 30 de ociosidade imputada**, ambos hipotéticos. Não afirmar CAC observado. Aquisição real inclui tempo comercial (prospecção, conversa gratuita, proposta e negociação) e despesas comerciais atribuíveis, alocados à coorte e depois aos projetos pelo método escolhido. Não jogar todas as oportunidades perdidas em um cliente sem critério. Nenhuma venda = CAC por cliente não calculável; registrar gasto da coorte.

**Separação temporal:** a conversa inicial gratuita do slide 10 é pré-venda e entra em aquisição; o alinhamento de Start só ocorre depois da autorização/contratação e entra em execução. Um minuto tem uma categoria, não duas. Reunião híbrida deve ter segmentos registrados sem sobreposição.

**Ociosidade:** adotar somente um método. Neste cenário, R$ 69,92/h não contém correção por utilização, e R$ 30 é sensibilidade separada. Se for escolhido custo-hora ajustado por horas faturáveis/utilização, retirar a linha de ociosidade. Da mesma forma, remuneração já embutida em rateio não pode ser imputada novamente. Rateio de fixos e idle são pools distintos; não alocar a mesma despesa em ambos.

### 3.2 Fórmulas e conferência

`Resultado gerencial = receita prevista − tributos − taxas − custos diretos não humanos − fixos não humanos alocados − horas de execução × custo-hora imputado − aquisição atribuída − ociosidade imputada`.

`Margem gerencial = resultado / receita`, se receita > 0. `Horas de equilíbrio = [preço × (1 − alíquota) − demais custos] / custo-hora`. Essas fórmulas não equivalem a lucro fiscal ou saldo bancário. Para caixa, separar recebimentos/desembolsos efetivos por data; excluir imputações sem desembolso e registrar pagamentos de remuneração efetivamente realizados uma única vez. Não chamar preço não aprovado de receita realizada.

| Serviço / horas | 6%, base | 15,5%, base | 6%, base + R$ 50 | 15,5%, base + R$ 50 |
|---|---:|---:|---:|---:|
| Start / 2 | R$ 112,76 | R$ 85,21 | R$ 62,76 | R$ 35,21 |
| Start / 4 | −R$ 27,08 | −R$ 54,63 | −R$ 77,08 | −R$ 104,63 |
| Focus / 5 | R$ 221,40 | R$ 159,65 | R$ 171,40 | R$ 109,65 |
| Focus / 8 | R$ 11,64 | −R$ 50,11 | −R$ 38,36 | −R$ 100,11 |
| Evolution / 10 | R$ 348,80 | R$ 234,80 | R$ 298,80 | R$ 184,80 |
| Evolution / 16 | −R$ 70,72 | −R$ 184,72 | −R$ 120,72 | −R$ 234,72 |

Com adicionais, horas de equilíbrio 6%/15,5%: Start 2,90/2,50; Focus 7,45/6,57; Evolution 14,27/12,64. São sensibilidades, não limites para comprimir trabalho necessário. Implementation/Excellence não têm preço determinado: estimar com as mesmas categorias por item/ciclo.

### 3.3 Modelo para esforço e margem real

Reutilizar registro de projeto e controles financeiros existentes. Esta nota fornece campos, sem criar outro CRM ou planilha paralela. Não gravar informações financeiras pessoais ou dados de clientes em repositório público.

| Registro | Campos mínimos / regra |
|---|---|
| Identificação | ID de projeto/oportunidade, versão autorizada, período, responsável e escopo; referência ao registro existente |
| Tempo, uma linha por segmento | Data, atividade, início/fim ou minutos, categoria aquisição/execução, planejado/real, motivo; execução: alinhamento, preparação, análise/teste conforme serviço, relatório, revisão, devolutiva |
| Retrabalho | Subcategoria: erro do executor, esclarecimento previsto ou solicitação nova; já dentro das horas, não somar novamente |
| Bloqueio | Motivo, início/fim de espera, comunicação/remobilização efetiva; espera fora de horas produtivas |
| Despesa | ID único/comprovante, valor, data, natureza direta/fixa/comercial, projeto ou pool, método de rateio, percentual; soma de alocações por comprovante ≤ 100% |
| Tributação/taxas | Base, alíquota efetiva confirmada ou hipótese marcada, competência, taxa de recebimento e documento de validação |
| Resultado | Preço aprovado quando existir, receita prevista/recebida separadas, horas totais, custo-hora/metodologia, aquisição, idle, resultado e margem por fórmula; estimativas distintas de realizados |
| Valor | Satisfação 1–5 opcional, clareza 1–5 opcional, decisão ajudada e próximo passo relatado; sem inferir ROI ou demanda por satisfação |

Reconciliar cada registro: minutos sem sobreposição, uma despesa em uma origem, rateios identificados, tributo não repetido em taxa, retrabalho não contado duas vezes. Comparar previsto/real por etapa e desvios absolutos/percentuais; previsto zero = percentual não aplicável. Revisar após cada piloto dentro do processo existente. Sem documentação fiscal ou despesas reais, manter “margem real não verificável”.

## 4. Proposta de piloto controlado do QA Start

**Estado:** proposta à direção; nenhum cliente recrutado, contratado ou atendido. Menor experimento: uma entrega Start para um problema delimitado, somente após decisão explícita. Um caso não valida mercado ou os cinco serviços.

**Hipótese:** o cliente consegue escolher uma ação de investigação a partir de insumos existentes e uma nota curta, com execução total de até 2h30. Risco contrário: pode esperar testes/bugs e não atribuir valor à triagem, ou o retrabalho tornar o preço indicativo insustentável.

**Entrada objetiva:** condições do §2.2; responsável capaz de fornecer insumos/aceitar; ausência de urgência operacional/incidente; problema não depende de testar o sistema para responder à pergunta inicial; recorte e limites entendidos. Se faltarem dados, solicitar uma complementação dentro do volume antes de iniciar; se ainda insuficientes, devolver como não elegível, sem inventar diagnóstico. Direção confirma capacidade, datas, modalidade do piloto, preço ou eventual subsídio e contrato/consentimentos antes de convite externo.

| Atividade incluída | Orçamento candidato |
|---|---:|
| Alinhamento pós-autorização | 20 min |
| Preparação/conferência dos insumos | 10 min |
| Triagem e análise documental | 45 min |
| Redação da nota | 35 min |
| Revisão técnica própria | 15 min |
| Devolutiva | 10 min |
| Comunicação/uma rodada do cliente | 15 min |
| **Total** | **150 min = 2,5h** |

Registrar gasto mesmo sem uso de toda a reserva de revisão; reserva não é tempo realizado. Aos 120 minutos, conferir esforço restante; se previsão ultrapassar 150, sinalizar e buscar decisão interna, sem abandonar desconformidade ou ampliar escopo silenciosamente. Cenário de estresse: 210 minutos = 3,5h, para dimensionar risco, não autorização de exceder orçamento.

Com preço **hipotético** R$ 290, envelope R$ 20 e adicionais R$ 50: 2,5h resulta em R$ 27,80 (9,59%) a 6% e **R$ 0,25 (0,09%) a 15,5%**; 3,5h resulta em −R$ 42,12/−R$ 69,67. Sem adicionais, somar R$ 50 aos resultados. Taxas/extras ainda não medidos podem reduzir esses valores. A meta 2h30 não comprova sustentabilidade. Direção deve definir margem mínima e teto monetário de subsídio; nenhum prejuízo fica autorizado por este documento.

**Entregável padronizado, único, até duas páginas:**

1. Identificação: projeto/versão/data, responsável, problema, decisão que se pretende apoiar, recorte e exclusões.
2. Fontes: insumo/data, fato relatado versus evidência documental, lacuna e confiabilidade.
3. Até três prioridades: risco/fricção, fundamento, hipótese ou fato, ação sugerida e dependência. “Dados insuficientes” é admissível quando justificado; não é defeito encontrado.
4. Próximo passo recomendado, limitações e declaração **“Não houve execução de testes neste serviço”**.
5. Devolutiva e histórico de uma rodada consolidada; não incluir informação sigilosa desnecessária.

**Aceite:** todas as seções verificáveis, recorte respeitado, fontes rastreáveis, nenhum teste alegado, revisão/devolutiva previstas realizadas ou reagendadas com acordo; janela de três dias úteis sem aceite presumido. Revisão limitada a esclarecimento/correção, não novos insumos ou investigação. Documento com fundamento incorreto precisa de correção conforme §2.1.

**Indicadores:** minutos totais/etapa; minutos e causa de retrabalho; prazo previsto/real descontando espera documentada; adequação do escopo e pedidos fora dele; satisfação e clareza opcionais 1–5; resposta aberta “qual decisão/ação esta nota ajudou você a tomar?”; custo e resultado gerencial por base validada. Separar ausência de resposta de insatisfação. Case/depoimento exigem consentimento próprio; não condição de pagamento.

**Continuidade proposta:** após a entrega, direção recebe registro e decide pausar, ajustar ou autorizar outro piloto. Evidência favorável candidata: aceite do recorte, tempo ≤150min, nenhuma extrapolação não autorizada, retrabalho ≤15min e clareza/satisfação ≥4 quando respondidas, além de ação útil relatada. Financeiro exige margem mínima ou subsídio explícito definido antes do piloto, não limiar inventado depois. Não resposta, tempo excedido ou percepção de “faltou teste” exigem investigação/ajuste. Ampliar para Focus ou mais clientes exige nova decisão; nenhuma continuidade é automática. Janela candidata de aprendizado: entregar até três dias úteis da entrada e consolidar resultado até cinco dias úteis após devolutiva, segundo agenda autorizada.

## 5. Campanha e tabela: alternativas preservadas

Três referências distintas coexistem: campanha anterior QA Express/Auditorias R$ 490/1.490/2.490 na PR #2; catálogo anterior R$ 690/1.800/2.900; Journey R$ 290/650/1.200 indicativos. O site observado exibe **QA Express a partir de R$ 690**. Isso é conteúdo publicado observado, não prova de homologação nesta rodada.

**A:** manter campanha antiga para seus próprios serviços e decidir tabela regular Journey. **B:** migrar campanha para a Journey, decidindo regular/promocional, elegibilidade, vagas compartilhadas, validade, reserva/cancelamento e capacidade. **C:** estacionar nova tabela, preparar somente o piloto autorizado com condição específica. Nenhuma escolhida; não mapear QA Express para Start automaticamente: Express prevê avaliação/execução e Start não testa.

Avisos documentais desta rodada em [INICIO](../INICIO.md), [PLN-COM-001](../04-Decisoes/PLN-COM-001-Primeiras-Vendas-GenTests.md) e [oferta antiga](../07-Templates/QA-Express-Oferta-Piloto.md) identificam conflito e referenciam este tratamento. Somente avisos/versão documental; tabelas e decisões históricas preservadas. Não modificar CRM, contratos, preços publicados ou condições de clientes existentes. Após decisão formal, atualizar em conjunto plano, catálogo, oferta, apresentação e site na versão autorizada.

## 6. PPTX exato e evidências — QJ31-04

[GenTests_Apresentacao_Comercial_Quality_Journey_v3_2_Revisao_Interna.pptx](apresentacoes/GenTests_Apresentacao_Comercial_Quality_Journey_v3_2_Revisao_Interna.pptx), **50.690 bytes**, dez slides. SHA-256 conferido antes/depois da renderização: `b228419977c3267a6b3696a25c40886fc9ffce6ff9ab0d5791750d6661760a48`. O original foi importado para exportação de PNGs, sem edição nem reexportação do PPTX. Origem: arquivo disponibilizado nesta conversa, versão armazenada 1, ID `libfile_719f2de112c0819192259c68c4ce1d38`.

[Manifesto de renderização](../05-Evidencias/Quality-Journey-v3.2/render-manifest.json), [guia de inspeção](../05-Evidencias/Quality-Journey-v3.2/README.md) e dez PNGs completos permitem revisão independente. PNGs são projeções do renderer, não garantia de equivalência tipográfica com PowerPoint. A peça continua interna, não autorizada para cliente.

**Pendência visual concreta:** no terceiro cartão do slide 2, título em duas linhas e corpo ficam próximos/sobrepostos na renderização realizada. Registrar a ocorrência, confrontar com o PowerPoint e solicitar ao autor revisão se confirmada. Não corrigir o binário exigido como exato nesta rodada. A declaração anterior de “overflow passou” não encerra a inspeção visual deste arquivo. Preços numéricos ausentes dos slides; “Preço em definição” e “sob proposta” não equivalem a aprovação. O slide 10 oferece conversa gratuita de pré-venda, distinta do alinhamento do Start. O slide 6 identifica exemplo ilustrativo. Essas verificações de conteúdo não constituem aprovação visual/comercial independente.

## 7. Inventário real e mapeamento do site

Observação read-only em **10/10/2026 16:59:35 UTC / 13:59:35 America/Sao_Paulo**, via HTTP/HTML. [Inventário JSON](../05-Evidencias/Quality-Journey-v3.2/site-inventory.json) preserva URLs pedidas/resolvidas, status, hashes SHA-256 do HTML, textos e links. Quatro páginas distintas pela navegação; aliases `.html` resolvem páginas sem extensão. `/robots.txt` e `/sitemap.xml` retornam HTML da home: não são mapas válidos nem prova de cobertura completa. Páginas não vinculadas, comportamento JS, envio de formulário, responsividade e acessibilidade não testados. Não houve publicação ou envio.

| URL/ponto real e conteúdo observado | Ação/texto candidato | Fonte da proposta e condição |
|---|---|---|
| [Home](https://gentests-site.pages.dev/): “Seus clientes encontram os bugs antes da sua equipe?”; apoio sobre riscos/jornadas, CTAs “Solicitar diagnóstico” / “Ver soluções” | Substituir hero apenas se posicionamento aprovado: “Entenda seus riscos de qualidade e escolha o próximo passo.” Apoio: “Da triagem de informações à investigação e melhoria, com escopo definido para cada serviço.” | §2 e direção; não sugerir que Start identifica bugs por execução |
| Home: cards QA Express, Qualidade da jornada, Quality Intelligence | A ou B define manter/migrar; candidato Journey descreve pergunta, entrega e independência de cada etapa. Não lançar cinco ofertas apenas por estarem documentadas | §5; catálogo e capacidade aprovados |
| Home: simulação de bugs/suporte/churn; GenIA | Manter identificação ilustrativa e supervisão humana; revisar qualquer causalidade/resultado garantido. Não apresentar IA como produto validado | §8; referência institucional/capacidades decididas |
| [Soluções](https://gentests-site.pages.dev/solucoes): “Soluções em Engenharia de Qualidade”; QA Express “Avaliação pontual de uma jornada pública...” / “A partir de R$ 690” | Manter até decisão; eventual retirada/substituição conjunta após escolher alternativa. Start candidato: “Triagem dos insumos que você já possui para escolher onde investigar. Não inclui testes.” Não substituir 690 por 290 silenciosamente | §2.2/§5; preços e destino Express exclusivos da direção |
| Soluções: Qualidade da jornada, Quality Intelligence “Sob proposta” | Mapear capacidades individualmente: Focus investigação; Evolution planejamento; Implementation itens; Excellence ciclos. Não declarar equivalência de pacotes ou cobertura completa | §2; escopos aprovados e evidência de capacidade |
| Soluções: demonstração fictícia de cadastro/CEP e erro | Manter aviso de demonstração, separar da oferta Start, não usar como prova de cliente/case; nenhuma interação executada nesta rodada | PPT slide 6, §2.2; revisão futura de UX |
| [Quem somos](https://gentests-site.pages.dev/quem-somos): fundadora Cíntia Guimarães Camargo, experiência, humanos com IA; avatares não são empregados/responsáveis legais | Manter responsabilidade humana e fatos verificáveis; texto institucional só após reconciliação aprovada. Não publicar missão candidata nem transformar avatares em equipe humana | §8; direção confirma referência/capacidades |
| [Contato](https://gentests-site.pages.dev/contato): “O que está acontecendo com seu software?”, nome/e-mail/desafio/descrição/consentimento; FormSubmit e alerta sobre dados sensíveis | Manter coleta mínima/avisos; CTA candidato “Converse sobre seu desafio de qualidade”. Distinguir conversa gratuita de serviço contratado; eventual seleção de etapa não cria checkout ou preço aceito | §2.2/§4; direção e validação de consentimento/fluxo |
| Todas: navegação/rodapé e nomes de páginas | Após decisão, atualizar nomes/links/metadados de forma conjunta, manter canais reais e avisos; testar aliases/redirects e acessibilidade antes de publicar | Inventário e versão comercial aprovada; autorização posterior |

Hash de cada página/alias no JSON. Qualquer futura execução deve reconsultar o site para detectar alterações após este snapshot, fixar commit da fonte web e mapear cada alteração para a decisão aprovada. Não foi acessado repositório-fonte do site: HTML observado não comprova commit de origem. Inventário é evidência pública pontual, não auditoria técnica completa.

## 8. Reconciliação institucional proposta — QJ32-03

Fontes não substituídas: [Missao-Visao-Valores 0.1.0](../01-Empresa/Missao-Visao-Valores.md), blob `c40c21a46411d556b86cfe9d72544c3d8d8837ed`; `GenTests_Identidade_Institucional_Visao_Missao_Valores.docx`, versão 1.0 de 09/10/2026, versão armazenada 1, ID `libfile_d646830de6088191b87217c5db8ab812`. Ambas em proposta; a segunda não está versionada nesta branch. Não escolher uma como política aprovada por ser mais recente.

| Tema | GitHub | Documento v1.0 | Reconciliação candidata |
|---|---|---|---|
| Missão | Engenharia de qualidade, IA, melhoria, riscos/desperdício/confiança | Fricções/experiência, evidências, diagnósticos, confiabilidade/acessibilidade/eficiência | Problema do usuário e decisão do negócio como finalidade; engenharia/evidência como método; IA responsável quando adequada |
| Visão | Referência em QE, IA/governança e resultados mensuráveis | Quality Intelligence une usuário, engenharia e negócio | QE como competência e Quality Intelligence como direção estratégica; medir quando houver dados comparáveis |
| Integridade/transparência | Integridade, responsabilidade/segurança | Ética, privacidade, IA responsável | Compromissos explícitos, revisão humana e uso autorizado |
| Qualidade/rigor/evidência | Qualidade desde origem, decisões por evidência | Rigor técnico, evidência antes de opinião | Prevenção e hipótese identificada; não vender documento como resultado validado |
| Pessoas/valor | Valorização de pessoas, eficiência sustentável | Empatia, impacto no negócio | Experiência humana e utilidade da decisão, sem prometer receita |
| Inovação/aprendizado | Inovação com propósito, aprendizado contínuo | Melhoria contínua, IA responsável | Experimentar em escopo pequeno, medir e decidir antes de ampliar |

**Missão candidata:** “Ajudar organizações a compreender fricções e riscos dos seus produtos digitais e a priorizar melhorias, unindo engenharia de qualidade, dados e evidências para apoiar experiências mais confiáveis, acessíveis e eficientes, com melhoria contínua e uso responsável de IA quando adequado.”

**Visão candidata:** “Ser referência em Quality Engineering e Quality Intelligence, conectando a experiência do usuário, a engenharia e os indicadores do negócio por meio de consultoria rigorosa, governança e IA sob supervisão humana, com resultados mensuráveis quando houver dados comparáveis.”

**Valores candidatos:** integridade e transparência; evidência e rigor técnico; qualidade desde a origem; empatia e valorização das pessoas; segurança e privacidade; impacto útil e eficiência sustentável; inovação com propósito e IA responsável; aprendizado e melhoria contínua. Não implica auditoria de acessibilidade em todo pacote nem IA obrigatória em toda entrega.

Direção pode escolher, ajustar ou rejeitar essa formulação. Registrar fonte/versionamento e quem aprovou; só depois atualizar os documentos de referência e comunicação. Evolução futura para produto/IA é ambição, não capacidade atualmente validada.

**Excelência enxuta:** [GOV-5S-001](../00-Constituicao/Excelencia-Enxuta-5S.md) e [QG-STR-001](../00-Constituicao/Quality-Gates/QG-STR-001-Disciplina-Estrategica.md) também são propostas. Esta rodada usa uma nota de tratamento e evidências vinculadas, sem novo CRM, cerimônia ou cinco lançamentos. Piloto pode ser estacionado se a direção não confirmar capacidade, valor da triagem ou perda tolerável. Documentação não é evidência de demanda.

## 9. Responsabilidades e devolução à revisão

**1 — Correções executadas documentalmente:** especificações candidatas e Start inequívoco; composição/modelo financeiro e piloto; inventário/mapeamento real; comparação institucional; avisos de conflito; binário exato/hashes/PNGs; metadados da PR atualizados. Encerramento por novo revisor, não autoaprovação.

**2 — Pendências técnicas/documentais:** inspeção visual independente e ocorrência do slide 2; dados reais de consumo, tempo, aquisição e idle; fonte/commit do site e páginas não navegadas; eventual revisão do PPTX pelo autor em novo arquivo/hash. Modelo de aceite e limites precisam ser confrontados com capacidade real. Não declarar sincronização do Obsidian, lançamento ou evidência de cliente atendido.

**3 — Decisões exclusivas da direção:** referência institucional; catálogo/campanha A/B/C; regular/promocional, preço/pagamento, vagas/validade; prioridade/limites dos serviços; capacidade/datas do piloto, modalidade e autorização externa; margem mínima/teto de subsídio; condições contratuais e posterior autorização de integração/publicação. Ausência de decisão é bloqueio, não escolha implícita.

**4 — Validações externas:** contador confirma classificação dos serviços, base/alíquota efetiva, emissão e tratamento tributário; assessoria jurídica valida aceite, revisão, mudança, cancelamento, confidencialidade/dados, uso de IA e condições de contratação. Não editar contratos vigentes. Direção não substitui essas comprovações técnicas.

Solicitar nova revisão independente sobre o commit desta rodada, incluindo reavaliação dos achados e inspeção do PPTX/PNGs. **PR #3 permanece draft, aberta e sem merge**, dependente da PR #2; não iniciar piloto/comercialização, alterar CRM, publicar site ou homologar preços. A documentação torna a proposta reviewável, mas não elimina os gates de decisão.
