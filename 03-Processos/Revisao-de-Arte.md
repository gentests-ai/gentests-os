---
tipo: procedimento
id: PRC-MKT-001
versao: 0.3.0
status: proposta
responsavel: Marketing
aprovador: Direcao
revisao: 2026-10-11
---
# Produção e revisão de materiais comerciais

**Proposta consolidada em execução autorizada pela atividade #38; homologação pendente.** Aplica-se a PDF, apresentações, posts e e-mails. Usar o registro da atividade e a PR do material para checklist, evidências e decisões; não criar procedimento, planilha ou controle paralelo.

## 1. Fontes e versão de marca

| Fonte canônica | Uso e identificação |
|---|---|
| [[01-Empresa/Identidade-Visual]] | Guia de Identidade Visual **v1**, logo horizontal, símbolo e paleta de trabalho; consultar os arquivos originais vinculados no Drive empresarial. |
| [[01-Empresa/Registro-de-Ativos-de-Marca]] | Registro **v0.1.0, proposta**: origem e estado dos ativos e assinaturas. |
| [[02-Agentes/Marketing/Contrato-Agente-Marketing]] | Contrato **v1.1.0, proposta**: competências, limites e necessidade de aprovação. |
| [[03-Processos/PRC-COM-001-Processo-Comercial]] | Processo **v0.2.0, proposta**: gates comerciais e autorização externa. |

Fixar na PR o commit das referências consultadas. Registrar para cada ativo utilizado: URL/ID canônico, nome original, versão declarada ou revisão/data do Drive e SHA-256 dos bytes obtidos. **Não inventar uma versão ausente**: logo e símbolo originais não possuem versão nominal documentada; usar identificação do arquivo, revisão/data e hash. A paleta acompanha a versão do guia/commit da referência, sem virar nova especificação de impressão.

Preservar proporções, cores e integridade dos originais. Não redesenhar por IA, recolorir, recortar a marca, inventar monograma nem usar cópia de origem desconhecida. Conferir contraste no fundo escolhido. Redimensionamento proporcional para aplicação é permitido no escopo autorizado.

**Assinaturas:** V3 está referenciada, com aplicação a confirmar; a segunda assinatura ainda não tem original identificado. Não são intercambiáveis. Usar somente a assinatura cuja fonte, versão e finalidade tenham decisão explícita; não substituir silenciosamente textos institucionais.

## Planejamento e mensuração

Antes da produção, registrar público, problema, objetivo, canal, conteúdo, responsável e métrica observável no registro existente da atividade/PR. Após divulgação **expressamente autorizada**, observar somente resultados reais disponíveis (alcance, cliques, downloads, leads atribuíveis), distinguir eventos de oportunidades qualificadas e registrar melhoria proposta sem inventar conversões. Compartilhar somente resultados agregados com o Comercial.

**Interface Marketing → Comercial:** Marketing documenta origem/campanha, material, data e contexto verificável do interesse, observando minimização de dados e privacidade. Comercial verifica duplicidade, base/autorizações aplicáveis, qualifica e registra próximo passo no processo [[03-Processos/PRC-COM-001-Processo-Comercial]]. O CRM em Google Sheets é apenas **proposta**, pendente de validação de acesso e ratificação da Direção; não manter pipeline paralelo. Interesse ou download não equivale a consentimento geral para contato. A interface não confere permissão adicional a agentes.

## 2. Responsabilidades e fluxo

| Papel | Responsabilidade |
|---|---|
| Marketing/executor autorizado | Preparar peça e checklist; verificar fontes e ativos; corrigir no escopo; registrar versão, mudanças e evidências. Não declarar a própria revisão como independente. |
| Revisor Independente/Quality Gate | Emitir resultado técnico focal e resultado de conformidade de marca separados, com evidência, ressalvas e testes efetivos. Declarar limitações e impedimentos. |
| Direção | Autorizar nova aplicação/alteração de identidade e exceções; homologar procedimento/versão final; decidir separadamente envio, publicação ou distribuição. |
| Comercial | Informar público, finalidade e canal; usar somente material e ação externa expressamente autorizados, conforme PRC-COM-001. |

Fluxo: escopo autorizado -> rascunho versionado -> autocheck/evidências -> revisão independente focal -> decisão da Direção -> ação comercial somente quando autorizada. Em correções, preservar histórico e revalidar o delta e seus impactos; ampliar revisão apenas diante de defeito novo comprovado.

## 3. Checklist comum

Preencher na PR **APROVADO / REPROVADO / NÃO EXECUTADO / NÃO APLICÁVEL**, com evidência e justificativa para N/A. Ausência de teste não equivale a aprovação.

- [ ] Finalidade, público, canal, versão e autorização de execução identificados.
- [ ] Logo/símbolo provenientes dos originais; proporções, cores, fundo e assinatura coerentes com fontes e finalidade autorizada.
- [ ] Textos legíveis no tamanho de uso; sem cortes, colisões ou distorções; contraste verificado, incluindo azul sobre azul. Como referência digital, texto normal >= 4,5:1 e grande >= 3:1; registrar medida e contexto, sem afirmar conformidade integral.
- [ ] Conteúdo e afirmações materiais sustentados por fontes; sem métricas, clientes, cases ou depoimentos inventados. Preservar conteúdo já aprovado.
- [ ] Links visíveis e destinos coerentes; área acionável correta; registrar teste real no canal e eventuais redirecionamentos, sem enviar formulários sem autorização.
- [ ] Acessibilidade pertinente ao formato verificada: idioma, ordem de leitura, títulos, alternativas textuais e navegação. Inspeção estrutural não substitui tecnologia assistiva.
- [ ] Arquivo final e versão identificados; evidências correspondem à versão efetivamente testada; pendências e três decisões abaixo explicitadas.

## 4. Critérios por formato e evidência mínima

| Formato | Critérios e evidências |
|---|---|
| PDF | SHA-256 e tamanho do binário; renderização das páginas alteradas e inspeção de cortes/legibilidade; fontes, idioma, ordem/estrutura e anotações quando aplicáveis. Testar link em leitor PDF, leitura assistiva e telefone físico quando requeridos, identificando ambiente real. Simulação não comprova telefone físico; não declarar PDF/UA sem validação específica. |
| Apresentação | Identificar arquivo/versão e hash do PPTX/exportação utilizada; inspecionar slides alterados em renderização e modo apresentação, fontes, margens e contraste. Conferir links, ordem de leitura e alternativas textuais. Validar exportação separadamente se for o material entregue. |
| Post | Identificar imagem/texto e dimensões para o canal; prévia em desktop e móvel, incluindo recortes. Conferir texto em tamanho real, contraste, legenda/alternativa textual e URL do CTA. Prévia local não equivale a publicação ou teste em aparelho real. |
| E-mail | Identificar corpo/HTML e assinatura canônica; conferir versão em texto simples, links, leitura móvel, imagens bloqueadas, alternativa textual e ordem de leitura. Registrar cliente/versão nas prévias ou testes autorizados. Envio e recebimento reais exigem autorização; não presumir sucesso por inspeção de HTML. |

Evidência comum mínima: arquivo/versão (hash para binários), fonte/revisão/hash do ativo aplicado, página/slide/área alterada, captura ou renderização, procedimento e resultado observado, data e ambiente/ferramenta/versão. Para links registrar destino e resultado real; para acessibilidade registrar verificações realizadas e limitações. Remover dados pessoais desnecessários das evidências. Vincular tudo à PR/atividade existente.

## 5. Alterações, impedimentos e exceções

Se faltar original, houver versões conflitantes, assinatura não identificada ou aplicação ambígua: registrar item, fonte consultada, impedimento e impacto na atividade; interromper a aplicação afetada e pedir orientação à Direção. Continuar tarefas independentes. Não improvisar ativo nem considerar o silêncio como aprovação.

Exceção exige decisão explícita da Direção vinculada à PR: motivo, alcance, versão/canal, risco, prazo quando aplicável e condição de encerramento. Não concede autorização comercial por consequência.

Ao alterar binário: preservar anterior; criar versão identificável; registrar novo SHA-256 e delta; produzir novas evidências das áreas modificadas; conferir impactos em texto, layout, links e acessibilidade. Evidências históricas continuam válidas somente para o arquivo histórico. Cada teste prático deve indicar versão/localização/hash exatos; resultado não se transfere automaticamente para outro binário.

## 6. Decisões separadas

| Decisão | Critério de registro |
|---|---|
| Aprovação técnica | Parecer com escopo, arquivo/versão/hash, resultados e pendências; testes não realizados permanecem explícitos. |
| Conformidade de marca | Originais e finalidade conferidos; fidelidade visual demonstrada; ressalvas e decisão sobre exceções registradas. |
| Autorização comercial | Deliberação expressa da Direção para versão, finalidade e canal. Parecer técnico, conformidade de marca ou aprovação de execução não autorizam envio/publicação/distribuição. |

Manter Draft, bloqueio de distribuição e demais restrições enquanto determinados pela decisão da atividade. Não realizar merge por este procedimento. A Direção homologa o PRC-MKT-001 e decide a liberação comercial do material em registros distintos.
