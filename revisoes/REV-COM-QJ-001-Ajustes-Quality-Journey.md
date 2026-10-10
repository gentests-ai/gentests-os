---
id: REV-COM-QJ-001
tipo: parecer-de-revisao-comercial
versao: 0.1.0
status: proposta
data: 2026-10-10
marca: GenTests.ai
revisao_independente_financeira: pendente
---
# GenTests Quality Journey — ajustes para consolidação

**Destinatário:** agente responsável pela proposta comercial e precificação.  
**Objetivo:** corrigir e consolidar a jornada, o catálogo, a campanha e a documentação antes de atualizar o site ou publicar a oferta.

## Orientação da direção

Cíntia considera a jornada mais fácil de vender porque suas etapas fazem sentido para o cliente. Preservar a estrutura de cinco etapas e a possibilidade de contratação independente ou progressiva. O primeiro pagamento permanece um marco de aquisição.

A proposta v3 registra Start R$ 290, Focus R$ 650 e Evolution R$ 1.200 como valores indicativos; Implementation e Excellence ficam sob proposta. Esses preços não devem ser confundidos com a campanha anterior de R$ 490 / R$ 1.490 / R$ 2.490.

**Não interpretar este parecer como aprovação de novos preços, margem, escopo, contrato ou publicação.**

## Fonte revisada

- Repositório: gentestsai-sudo/gentests-os.
- Branch: review/precificacao-2026-10-10.
- Documento: comercial/apresentacao-comercial-v3-quality-journey-proposta.md.
- Blob consultado: bed2a53bd69eaa2c5d517d43da0461add5497967.
- Link: https://github.com/gentestsai-sudo/gentests-os/blob/review/precificacao-2026-10-10/comercial/apresentacao-comercial-v3-quality-journey-proposta.md
- Consolidação anterior: https://github.com/gentestsai-sudo/gentests-os/pull/2

Este parecer avalia o texto da v3. Não constitui revisão visual do novo PPTX nem validação contábil independente. A nota de precificação consultada ainda descreve os serviços e preços anteriores.

## 1. Diferenciar os cinco serviços

As descrições de Start, Focus e Evolution ainda se sobrepõem em “avaliação”, “diagnóstico” e “riscos”. Definir a diferença pela pergunta respondida, pelo trabalho realizado e pela entrega concreta.

A matriz abaixo é uma **direção sugerida para refinamento**, não um escopo já aprovado:

| Etapa | Pergunta central | Entrega a especificar | Fronteira a esclarecer |
|---|---|---|---|
| Start — Descobrir | Onde devemos olhar primeiro? | Diagnóstico pontual com prioridades iniciais | Qual insumo é analisado? Há entrevista? Há execução de testes? |
| Focus — Investigar | O que acontece nesta jornada ou risco? | Investigação delimitada e evidências aplicáveis | Quantos fluxos/variantes? Qual profundidade? Há reteste? |
| Evolution — Planejar | O que melhorar e em qual ordem? | Diagnóstico estruturado e plano priorizado | Qual profundidade supera Start? Inclui Focus ou aproveita evidências existentes? |
| Implementation — Implementar | Como colocar as melhorias em prática? | Melhorias pactuadas, evidências e transferência | Implementa processo, automação, ferramentas ou código? Quais itens ficam fora? |
| Excellence — Sustentar | Como acompanhar a adoção e evolução? | Acompanhamento e indicadores pactuados | É recorrente? Qual duração, frequência, disponibilidade e limite? |

Para cada serviço, registrar: cliente indicado, problema tratado, entradas, unidade de escopo, tarefas, entregáveis, exclusões, prazo/dependências, limite interno de esforço, revisões/reteste, aceite e preço/condições.

O cliente deve conseguir escolher uma etapa sem sentir obrigação de contratar as cinco. Não exigir etapa anterior quando insumos suficientes já existirem.

## 2. Resolver preço regular versus promoção

Registrar explicitamente se R$ 290 / R$ 650 / R$ 1.200 são:

- a nova tabela regular; ou
- condições promocionais dos três primeiros clientes.

Não escolher essa classificação por inferência. Se houver tabela regular e promocional, mostrar ambas no registro interno, com vigência e decisão da direção.

Se a campanha dos três primeiros clientes continuar, confirmar:
- três clientes no total, compartilhados entre os serviços;
- quais etapas participam, especialmente Implementation e Excellence;
- regra de reserva/contagem, prazo da condição e tratamento de cancelamentos;
- preço aplicável depois da campanha e a contratos adicionais.

As regras da PR #2 eram propostas operacionais e não devem ser transportadas automaticamente para a jornada nova.

## 3. Compatibilizar margem, esforço e escopo

Atualizar a análise financeira para os novos serviços, usando a revisão contábil atual como referência rastreável. Não reutilizar a margem calculada para QA Express/Auditorias como se fosse margem de Start/Focus/Evolution.

Para cada etapa, incluir todo o esforço: alinhamento, análise, preparação, execução quando aplicável, evidências, relatório, revisão, devolutiva e comunicação. Separar preço-hora de custo-hora e evitar rateio duplicado.

Apresentar cenário esperado e cenário de maior esforço, premissas tributárias identificadas, custos atribuídos e resultado. Redução deliberada de margem para aquisição deve ser distinguida de prejuízo; eventual perda requer valor e decisão explícitos.

Horas podem ficar fora da apresentação pública, como propõe a v3, mas precisam permanecer no planejamento interno e sustentar o escopo vendido. Não inventar teto de horas para encaixar o preço.

## 4. Apresentação e site

Manter o nome GenTests Quality Journey e acompanhar os termos em inglês de descrições em português: Descobrir, Investigar, Planejar, Implementar e Sustentar.

Na apresentação:
- tornar as diferenças e entregas legíveis;
- manter o exemplo de cadastro explicitamente ilustrativo;
- delimitar Implementation e Excellence, mesmo sob proposta;
- evitar promessa de eliminar falhas, garantir resultados ou oferecer trabalho ilimitado;
- revisar visualmente o PPTX efetivo, além de verificar overflow.

Preparar a proposta de alteração do site após consolidar a oferta: mensagem principal, serviços, explicação da jornada e convite para conversa. Preços públicos dependem da decisão sobre tabela regular/promocional. Não afirmar que o site foi alterado ou revisado neste parecer; não publicar antes da revisão e autorização aplicáveis.

## 5. Consolidar o GitHub e o fluxo Obsidian

Preservar a história e reutilizar PLN-COM-001 como plano canônico. Atualizar a PR #2 ou preparar revisão que a substitua claramente; impedir integração da tabela antiga como oferta corrente.

Vincular:
1. plano e campanha;
2. catálogo/escopo da jornada;
3. análise financeira atualizada;
4. decisão da direção;
5. roteiro e PPTX correspondentes;
6. evidências e índices.

Explicar o destino dos serviços antigos: substituídos, renomeados ou mantidos como ofertas distintas. Não presumir equivalência QA Express = Start, Auditoria Funcional = Focus ou Processos QA = Evolution.

Manter IDs/caminhos estáveis quando possível; corrigir backlinks se houver renomeação. O GitHub é a referência documental; atualizar o Obsidian pelo fluxo existente após integração, sem declarar sincronização local não verificada. Não criar outro CRM.

## Entrega esperada do agente

Devolver uma versão revisada contendo a matriz de escopo dos cinco serviços, a classificação dos preços, a regra da campanha, o cálculo financeiro correspondente, o roteiro/PPTX alinhados e o impacto proposto no site.

Separar no retorno: **decisões registradas**, **sugestões do agente**, **premissas financeiras** e **pendências reais**. Apontar decisões que dependem da direção sem tratar preparação documental como homologação.

**Critério de conclusão:** cliente consegue distinguir as etapas; preço corresponde ao esforço delimitado; promoção e tabela regular estão claras; documentos não se contradizem; histórico preservado; revisão e autorização registradas antes de publicação.

