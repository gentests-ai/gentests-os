---
id: GT-PROD-CNB-001-QA
produto: GT-PROD-CNB-001
tipo: matriz-aceite-testes
versao: 0.1.1
status: proposta
estado_documental: em-validacao
data: 2026-10-10
responsavel: Produto
aprovador: Direcao
validacao_independente: pendente
implementacao: nao-autorizada
publicacao: bloqueada
---

# Matriz de critérios de aceite e testes

**Cenários especificados, não executados no produto.** Não há calculadora implementada. Resultados abaixo são oráculos aritméticos/funcionais para revisão; a conferência documental do exemplo não comprova funcionamento de UI, e-mail, acessibilidade ou privacidade.

## 1. Critérios rastreáveis

| ID/prioridade | Referência | Cenário / ação | Resultado obrigatório |
|---|---|---|---|
| CA-01 P0 | RF-01/02 | Abrir calculadora | Vazio/desconhecido, sem valores/salários/frequência embutidos; usar sem cadastro |
| CA-02 P0 | RN-02–05 | Carregar exemplo canônico | R=2.260, E=600, A=900, O=1.000, T=4.760, M=14.280, Y=171.360; origens hipotéticas |
| CA-03 P0 | RN-07/08 | Campo desconhecido vs zero digitado vs N/A | Três estados distintos; ausente excluído e subtotal incompleto; N/A listado |
| CA-04 P0 | RN-07 | Somente dev 12h ×120, outras parcelas desconhecidas | Subtotal R$1.440, não custo integral; mês/ano não calculáveis se N ausente |
| CA-05 P0 | RN-08 | Todos desconhecidos / todos explícitos zero | Primeiro sem resultado; segundo R$0 parcelas consideradas, sem alegar ausência de todo impacto |
| CA-06 P0 | RN-09/10 | A=900 e O=1.000 com mesma referência de evento | Ambas excluídas até resolução; mantendo recursos e E: subtotal 2.860; conflito visível |
| CA-07 P0 | IN-06/RN-10 | Horas sem confirmação de unicidade | Parcela fora da soma conciliada, motivo e incompletude; confirmação não gera prova auditada |
| CA-08 P0 | RN-10 | Externo já incluído em custo-hora | E excluído; não somar a despesa novamente; relatório mantém motivo |
| CA-09 P0 | RN-11 | Downtime de 2h, salário, retrabalho e receita bruta | Downtime não monetiza; salário/retrabalho não duplicam; receita bruta não aceita como margem |
| CA-10 P0 | RN-05 | N=0, N ausente e N=3 | Respectivamente M/Y=0 pela hipótese, não calculável e 14.280/171.360 no exemplo |
| CA-11 P0 | RN-01 | Negativo, NaN, expoente, texto, 1,234 e agrupamento errado | Rejeitar acessivelmente sem normalização silenciosa; nenhum resultado novo |
| CA-12 P0 | RN-01 | 1.234,56 e 1234,56 | Ambos 123456 centavos; ponto decimal 1234.56 não aceito |
| CA-13 P0 | precisão RN-02 | 0,50h ×R$0,01/h | R$0,01 half-up; duas linhas iguais somam R$0,02, memória explica arredondamento por linha |
| CA-14 P0 | limites | IN limite e limite+0,01; N=100.000 e 100.001 | Limite permitido se total válido; acima rejeitado, sem truncar |
| CA-15 P0 | limites/overflow | T=R$7.000.000.000 e N=100.000 (quatro blocos e três efeitos nos tetos) | Y excede R$1 trilhão, projeção bloqueada com erro; não infinito/wrap |
| CA-16 P0 | RF-04 | Calcular e editar uma taxa | Resultado desatualizado, exportação/envio bloqueados até recalcular; snapshot coerente |
| CA-17 P0 | RF-02 | Exemplo sobre dados próprios / limpar | Confirma substituição/limpeza; cancelar preserva; exemplo não convertido em “informado” |
| CA-18 P0 | RF-03 | Misturar informado, hipotético e desconhecido | Calculado mantém provenance, badge hipóteses e incompletude; nunca “perda comprovada” |
| CA-19 P0 | UX/access | Teclado, VoiceOver/NVDA, erro e live region | Ordem/foco, labels/unidades, sumário, status legíveis; sem trap/som obrigatório |
| CA-20 P0 | UX/visual | 320/375/768/1280 CSS px, zoom, texto longo | Sem corte/sobreposição de qualquer campo, subtotal, aviso, botão ou relatório |
| CA-21 P0 | RNF-07 | Imprimir relatório multipágina | Memória inteira, valores e limites legíveis; HTML acessível disponível |
| CA-22 P0 | EMAIL-01/04 | Não fornecer e-mail nem marketing | Calcular, ler e imprimir normalmente; relatório por e-mail só pede endereço se solicitado |
| CA-23 P0 e-mail | EMAIL-01/05, LP-01/02 | Pedir envio sem opt-in / com opt-in | Ambos recebem mesmo relatório; sem opt-in não entra em campanha; com opt-in prova segregada |
| CA-24 P0 e-mail | LP-03/08 | Retirar marketing/pedir exclusão | Cessa campanhas/filas, supressão propagada; regras de cópias/backups e canal comprovados |
| CA-25 P0 e-mail | LP-04/05/07 | Inválido, abuso, quota, timeout/provedor falha | Não envia a destinatário inválido; rate limit; sem sucesso falso ou retry duplicado |
| CA-26 P0 e-mail | TEC §3 | Mesmo request_id, timeout ambíguo e payload alterado | Idempotência/reconciliação; conflito rejeitado; não afirmar entrega sem prova |
| CA-27 P0 e-mail | TEC §3 | Totais adulterados, HTML/CRLF, extras e 32KiB+ | Recalcular validando schema; escapar; rejeitar extras/injeção/payload excessivo |
| CA-28 P0 privacidade | RNF-08, LP-06/09–11 | Network/storage/logs, rejeitar telemetria e acessos negados | Inputs só deixam aba no envio solicitado autorizado; não entram em analytics/URL; sem acesso indevido |
| CA-29 P0 | métricas | Recalcular/exemplo/print/request/sent | Dedupe e separação; print não prova salvar, sent não prova delivered; zero denominador N/A |
| CA-30 P1 | SEO | Ler HTML com JS desligado | Método/FAQ visíveis; homologação noindex; nenhum dado individual indexável |
| CA-31 P1 | RNF-01–03 | Motor, bundle e performance | Metas medidas com dispositivo/método; não transformar laboratório em evidência de campo |
| CA-32 P0 | gates | Sem fornecedor/base/retention/autorização | E-mail/telemetria desligados; revisão não inicia operação |
| CA-33 P0 | RN-10 | Reabertura do mesmo incidente, horas adicionais | Somente horas novas únicas; frequência não aumenta por ticket duplicado |
| CA-34 P1 | RNF-05/06 | Rede/e-mail indisponível; JS ausente; browsers | Cálculo local segue quando JS disponível; sem JS há metodologia/mensagem honesta; compatibilidade registrada |

## 2. Casos-limite complementares

- Horas-pessoa podem superar duração calendário do incidente; não usar 24h como limite de esforço de uma equipe.
- Horas >0 com taxa desconhecida → custo desse bloco não mensurado; horas=0 com estado explícito conhecido → valor zero sem exigir taxa. Taxa=0 e horas>0 exige confirmação.
- Margem informada=0 em evento sem contribuição → zero econômico nessa parcela; não inventar percentual. Recuperação integral de venda → não lançar oportunidade perdida; recuperação parcial exige informar apenas margem não recuperável conciliada.
- Remover referência/alterar valor de parcela reconciliada invalida confirmação; IDs locais diferentes sem confirmação de distinção não bastam para total completo.
- N fracionário (3,5) inválido no MVP; média observada fracionária é evolução, não arredondar para quatro.
- Uma parcela positiva e demais N/A confirmadas → total do escopo considerado com exclusões explícitas; sem apresentar “custo total da empresa”.
- Precisão centésimos de hora não representa minuto exato: 1 minuto≈0,0167h não é suportado sem arredondamento pelo usuário; informar limitação, evolução pode aceitar minutos.
- E-mail: aparar espaços externos, máximo candidato 254 caracteres; preservar local-part, normalizar domínio conforme biblioteca/contrato aprovado; não rejeitar “+tag”. Sintaxe válida não prova titularidade/entrega. Endereços internacionais exigem decisão de suporte, não regex improvisada.
- Sem fontes reais, nenhuma comparação antes/depois, tendência, redução causal, benchmark ou ROI.

## 3. Estratégia e evidências futuras

Motor: testes unitários/tabela de vetores do guia, estados e limites; propriedades: determinismo, soma por natureza igual ao total das linhas elegíveis, ordem não altera valor, desconhecido nunca vira zero, parcelas excluídas não aumentam total, aumento de operandos não reduz parcela antes do teto. Propriedades não substituem revisão metodológica.

UI: testes de integração e e2e com fixtures fictícias, fluxo vazio→exemplo→editar→erro→recalcular→imprimir. E-mail: ambiente isolado aprovado e mailbox sintética; sem destinatários reais/prospectos por esta tarefa. Acessibilidade: automação mais teclado/leitores de tela. Visual: todas as telas e relatório final, estados longos/erros/mobile, screenshots vinculados a commit e método; qualquer conteúdo material cortado/sobreposto é bloqueante, mesmo que testes automatizados passem.

Para cada execução futura: CA, data, ambiente, commit do site, versão do método, fixture, esperado/obtido, status passou/falhou/não verificado/N/A justificado, captura sanitizada e executor. Nunca marcar passou porque cenário foi escrito. Revisor independente inspeciona evidências do artefato exato. Parecer e autorização de implementação/publicação/merge são atos separados.

## 4. Cenários complementares da rodada focal v0.1.1

Os **34 critérios CA-01–CA-34 acima permanecem integralmente preservados**. CF-01–CF-08 são cenários subordinados aos critérios existentes, não nova fase ou funcionalidade. Todos são especificados e **não executados no produto**.

| Cenário / achado | Critérios existentes | Ação/fixture sintética | Resultado obrigatório |
|---|---|---|---|
| CF-01 / CNB-REV-01 — negativo | CA-06/18 | R=2.260 e E=600 com conciliação contextual válida; A=900 e O=1.000 recebem refs diferentes automáticas, mas comparação A/O sem resposta específica ou somente booleano genérico. Repetir com origem A desconhecida e tentativa de confirmed=true | Refs diferentes não confirmam ausência de duplicidade; comparação sem identificação/avaliação ou origem desconhecida é inelegível. A/O ficam excluídos, subtotal 2.860 incompleto, com motivo. Não aceitar total 4.760 nem apresentar auditoria |
| CF-02 / CNB-REV-01 | CA-06/08 | A/O com mesma referência; tentar “distinto” genérico. Depois retirar O, ou informar nos campos existentes somente valores incrementais externos conciliados e selecionar parcela_incremental_distinta com naturezas/valores comparados | Primeiro, ambas excluídas. Segundo, incluir somente parcelas com resolução contextual explícita; não criar outra rubrica. Confirmar que E já incluído em R continua excluído |
| CF-03 / CNB-REV-01 | CA-16/18 | Após confirmação contextual de E/A/O/R, editar valor, origem, estado, referência ou relação; testar edição de R | Invalidar todas as comparações afetadas, bloquear inclusão dessas parcelas até nova avaliação contextual; edição de R invalida comparações com R. Origem hipotética continua rotulada, nunca comprovada |
| CF-04 / CNB-REV-02 | CA-16/21 | Calcular S1; solicitar impressão P1; editar formulário durante preparação/paginação | P1/request_id fica ligado ao snapshot/hash/metodologia S1 congelado antes de renderizar; nenhuma página usa valores editados. Novos relatórios bloqueados até recalcular; pedido anterior identificado separadamente |
| CF-05 / CNB-REV-02 | CA-16/26 | Calcular S1, pedir e-mail Q1 e editar/limpar/carregar exemplo enquanto envio está em curso. Recalcular S2 e solicitar explicitamente outro relatório | Q1 conserva S1/hash/versão, data e status “cálculo anterior”; formulário não cancela nem sobrescreve envio. Novo pedido Q2 usa novo snapshot S2, sem reaproveitar Q1. Sem ação explícita, nenhum novo envio |
| CF-06 / CNB-REV-02 — timeout | CA-25/26 | Timeout após POST aceito, timeout do provedor e tentativa de retry após edição; simular provedor aceitou / não aceitou com prova / estado inconclusivo | Manter Q1/S1/hash/versão e status não confirmado até reconciliação. Aceitou: atualizar estado sem reenviar. Não aceitou comprovadamente: retomar mesmo pedido sob idempotência. Inconclusivo: bloquear retry de envio. Não trocar por S2 ou criar ID novo automaticamente; não declarar entregue |
| CF-07 / CNB-REV-02 — integridade | CA-26/27 | Mesmo request_id com snapshot/hash/versão/envelope idênticos; depois alterar snapshot, destinatário ou versão. Também enviar hash inconsistente, envelope com metodologia diferente ou versão não suportada | Pedido idêntico retorna estado sem novo envio; alteração sob mesmo ID resulta conflito 409; hash/versões inválidos rejeitados antes de aceitar. Backend recalcula pela versão suportada correspondente, sem migração silenciosa. Hash não dispensa validação nem atesta entrega |
| CF-08 / CNB-REV-03 | CA-09/14 | Informar 744h e 744,01h de contexto; simular incidente real superior a 31 dias | 744h permitido somente como limite operacional do campo do MVP; 744,01h rejeitado sem truncar com aviso “não é duração máxima real de incidentes”. Campo de contexto permanece não informado, não vira zero e não bloqueia parcelas monetárias válidas nem as monetiza |

## 5. Matriz de tratamento REV-PROD-CNB-001

Fonte: [parecer PR #30](https://github.com/gentestsai-sudo/gentests-os/pull/30), commit do parecer `dd28e2371e9a7e958d2c3fa0ffbb826aac2481b4`, sobre execução `dd00bb5231cb9d026c7e36a28138c54d5bf851e3`. Uma única rodada focal, restrita a CNB-REV-01–03.

| Achado / severidade | Tratamento documental e localização | Cenários / estado |
|---|---|---|
| CNB-REV-01 / média | FUN IN-10/RN-09a identifica naturezas/valores/origens comparados; refs diferentes e checkbox global não conciliam. UX §1 mostra rubricas simultâneas. TEC §2 substitui booleano genérico por comparações contextualizadas e invalidação após edição | CF-01–03 ligados a CA-06/08/16/18; tratado documentalmente pelo autor, **fechamento independente pendente** |
| CNB-REV-02 / média | FUN RF-04, UX EMAIL-03 e TEC §3 fixam snapshot/hash/request_id/metodologia antes da impressão/POST; edição não muda pedido em curso; timeout conserva vínculo original, exige reconciliação e impede retry cego | CF-04–07 ligados a CA-16/21/25–27; tratado documentalmente pelo autor, **fechamento independente pendente** |
| CNB-REV-03 / baixa | FUN IN-13 e UX §1 explicitam 744h/31 dias como limite operacional de contexto; excedente não define duração máxima real, não trunca, monetiza ou impede parcelas válidas | CF-08 ligado a CA-09/14; tratado documentalmente pelo autor, **fechamento independente pendente** |

Limitações residuais: conciliação continua declaratória sem auditoria de documentos; hash não é assinatura/prova financeira; nenhuma integridade, idempotência, UI ou entrega foi demonstrada por software. Provedor, retenção/janela de idempotência e autorização de e-mail permanecem pendentes nos gates já existentes; não antecipar Fase 2. Prioridade comercial de primeiros clientes mantida.

Arquivos revisados para 0.1.1: Especificacao-Funcional.md, Interface-Jornada.md, Arquitetura-Tecnica.md e Aceite-Testes.md. README.md e Backlog-Riscos-Decisoes.md permanecem na baseline 0.1.0, sem nova visão, backlog, estimativa ou decisões. Histórico 0.1.0 preservado no Git; a identificação 0.1.1 corresponde somente ao delta focal.

**Solicitação de revalidação:** conferir exclusivamente CNB-REV-01–03, CF-01–08, coerência entre os quatro documentos e preservação dos 34 CAs e fórmulas. Sem nova auditoria integral. PR #28 deve permanecer aberta/Draft; encerramento documental cabe à Direção após parecer. Nenhuma implementação, alteração de site, contratação, envio, captação, publicação ou merge autorizado/executado nesta rodada.
