---
id: REV-PROD-CNB-001
tipo: parecer-independente-produto
versao: 0.1.0
status: emitido
resultado: aprovado-com-ressalvas-para-deliberacao-documental
data: 2026-10-10
objeto: GT-PROD-CNB-001
objeto_versao: 0.1.0
pr_origem: 28
commit_revisado: dd00bb5231cb9d026c7e36a28138c54d5bf851e3
aprovacao_direcao: pendente
implementacao_autorizada: nao
publicacao_autorizada: nao
---
# REV-PROD-CNB-001 — Parecer independente da Calculadora de Custo da Não Qualidade

**Resultado: APROVADO COM RESSALVAS PARA EVOLUÇÃO/DELIBERAÇÃO DOCUMENTAL. NÃO HOMOLOGADO PARA IMPLEMENTAÇÃO, PUBLICAÇÃO, ENVIO DE E-MAIL OU CAPTAÇÃO.**

## 1. Escopo, fonte e limites
Inspecionados integralmente os seis arquivos de `produtos/GT-PROD-CNB-001/` no commit `dd00bb5231cb9d026c7e36a28138c54d5bf851e3`, PR #28 Draft e aberta: `README.md`, `Especificacao-Funcional.md`, `Aceite-Testes.md`, `Arquitetura-Tecnica.md`, `Interface-Jornada.md`, `Backlog-Riscos-Decisoes.md`. Conferido alinhamento documental do exemplo com CNQ-01 do guia, tratamento LGPD referido e prioridade comercial do PLN-COM-001. Nenhum produto, teste, navegador, envio, provedor, quota, dispositivo ou orçamento foi executado/verificado. Normas propostas não foram homologadas. Os cálculos abaixo são verificação manual documental, não teste automatizado.

## 2. Avaliação por dimensão
| Dimensão | Estado | Evidência |
|---|---|---|
| Financeiro | **Conforme documentalmente** | FUN §§2–5: quatro naturezas R/E/A/O separadas; zero/desconhecido/N/A; exclusão de duplicidades; horas únicas × custo-hora; arredondamento half-up por bloco; subtotal incompleto; projeções condicionais, não caixa ou ROI. |
| Regras e 34 CAs | **Cobertura especificada: 34/34, não executada** | QA CA-01 a CA-34: fluxo inicial, exemplo, ausências, conflitos, horas, parsing, limites, precisão, UX, relatório, e-mail opcional, privacidade, SEO e no-go. CAs são critérios descritos, não testes passados. |
| Arquitetura | **Viável conceitualmente, condicionada** | TEC §§1–6: JS puro sem rede para cálculo, contrato com inteiros/strings, hospedagem Pages candidata, e-mail separado em endpoint futuro, sem autoescalada paga. Estimativa 28–48h núcleo, 44–80h com envio, não compromisso. |
| UX/acessibilidade | **Adequado como especificação** | UX §§1–2: HTML semântico, teclado, WCAG 2.2 AA como objetivo, reflow 320px e relatório imprimível; teste assistivo/visual ainda necessário. |
| LGPD | **Separação satisfatória no desenho** | UX EMAIL-01–05, TEC §§1,3,5; conta sem persistência padrão, e-mail só por opção, marketing separado, retenção e bases como pendentes. Sem certificação operacional. |
| Estratégia | **Coerente com ressalva de capacidade** | README objetivos e PLN; CTA voluntário, guia como próximo passo, sem oferta inventada. Direção precisa limitar horas para não prejudicar primeira venda. |

## 3. Conferência financeira e precisão
- `12×120=1440`, `6×90=540`, `4×70=280`; R=2260; E=600, A=900, O=1000; T=4760, M=3×4760=14280; Y=12×14280=171360. Hipóteses não representam caixa, receita bruta perdida ou retorno obtido.
- `0,50h×R$0,01/h=R$0,005` arredonda half-up para R$0,01; duas linhas somam R$0,02, não somar produtos não arredondados antes do total. Com horas e taxas armazenadas em centésimos, a fórmula de centavos `(hours_hundredths * rate_cents + 50) // 100` é coerente para não negativos.
- `N=0` gera M/Y=0 sem apagar custo por incidente; N desconhecido gera não calculável. Projeções parciais conservam advertência. Inteiros/BigInt e limites explícitos evitam overflow; saída com valores como strings canônicas é coerente.
- Defeito, incidente e ticket duplicado são distinguidos. Indisponibilidade não vira automaticamente perda monetária.
- Sem dados reais, não há comprovação de eficácia da conciliação, do parsing implementado ou do comportamento de report.

## 4. Apontamentos rastreáveis e correções proporcionais
| ID/severidade | Documento/critério | Constatação | Correção objetiva e prioridade |
|---|---|---|---|
| **CNB-REV-01 — MÉDIA** | FUN IN-10, RN-09/10; TEC §2; QA CA-06/08/18 | IDs locais e confirmações de distinção são conscientemente autodeclarados, mas não está especificado de maneira inequívoca **como o UI impede marcar confirmada a distinção sem identificar quais parcelas foram comparadas**, sobretudo com referências locais geradas automaticamente para eventos independentes. Um clique genérico pode dar aparência de conciliação que não ocorreu. | Antes da PR técnica, fixar por natureza uma confirmação contextual obrigatória após exibir simultaneamente A/O/E e suas relações; quando houver mesma referência, exigir escolha de exclusão ou discriminação incremental explícita, invalidada a cada edição. Manter o aviso de que confirmação humana não é auditoria. Acrescentar um CA negativo para refs diferentes mas origem desconhecida/confirmada sem avaliação. |
| **CNB-REV-02 — MÉDIA** | FUN RF-04, RN-07/09; UX §1; QA CA-16/21 | Está prevista impressão de relatório com snapshot e desatualização, porém **o momento de congelamento do que é impresso não está explicitamente conectado a todo estado assíncrono** do componente de e-mail, caso a UI preserve formulário editável após solicitação. Pode produzir divergência entre o que foi visto e o que chega. | Especificar vínculo do `request_id` a hash/snapshot `methodology_version` imutável; edição posterior jamais altera envio em curso e deve exibir qual versão foi solicitada. Cobrir edição após pedido e timeout no CA-26. Pode ser resolvido no próprio contrato, sem backend novo nesta rodada. |
| **CNB-REV-03 — BAIXA** | FUN IN-13, RN-11; QA CA-09; UX §1 | O campo indisponibilidade é explicitamente contextual e não monetizado, mas o limite 744h poderia ser lido como limite universal de incidente em vez de horizonte de 31 dias de referência mensal. | Indicar no label/ajuda “até 744h nesta ferramenta, não duração máxima real de incidentes”; opcionalmente mover ao bloco de contexto. Não impede encerramento documental. |

Os dois achados médios são **ajustes de especificação necessários antes de implementar conciliação e envio**, não prova de defeito em software ainda inexistente. Não exigem nova auditoria integral nem contratação financeira.

## 5. Critérios de aceite e risco
Os 34 critérios CA-01–34 estão presentes com rastreabilidade a regras/requisitos. CA-15 contém cenário de teto extremo destinado a rejeitar projeção > R$1 trilhão; caso válido como teste negativo, condicionado aos limites dos operandos. CA-19–21 cobrem teclado/VoiceOver/NVDA, mobile e impressão, mas só podem ser marcados aprovados após produto e evidências reais. CA-23–28/32 são **gates do e-mail** e podem ser N/A justificado enquanto componente permanecer desligado; não bloqueiam o núcleo offline, mas bloqueiam ativar envio. Convém acrescentar vetor de separação contextual de efeitos e edição após pedido sem aumentar artificialmente o escopo do MVP.

## 6. Segurança, LGPD e viabilidade
Dados monetários podem constituir informação empresarial confidencial mesmo sem nome/CPF. Modo local é escolha de baixo risco; em e-mail opcional transportar apenas snapshot minimizado, informar fornecedores antes do pedido e nunca copiar totais a logs, URLs ou analytics. Decidir identidade de controlador, bases, retenção, proteção antiabuso, quota, mecanismos internacionais e acesso antes de ligar endpoint. `202 Accepted` não significa `delivered`; idempotência e status inconclusivo estão bem definidos, implementação não provada. Custos Pages/Workers e envio a terceiros não foram validados nesta revisão; manter teto adicional zero até autorização.

Estimativa de 28–48h de núcleo é plausível **como hipótese**, não comprometimento verificado. O esforço real pode variar em testes acessíveis e ajustes de apresentação, notadamente devido a complexidade de estados de exclusão e arredondamento. Não implementar e-mail para desbloquear calculadora local, e não prometer data ou custo zero em mão de obra.

## 7. Decisões da Direção
D-01 aprovar escopo offline sem cadastro; D-02 priorizar contra prospecção e fixar teto horas; D-03 validar limites/regras financeiras; D-04 decidir envio de e-mail por fase, provedor e teto; D-05 identidade jurídica, bases e prazos; D-06 telemetria; D-07 vinculação ao guia/SEO/CTA e status publicável; D-08 futura PR técnica; D-09 revisão independente; D-10 quatro blocos/limites/relatório local. Nenhuma dessas decisões é inferida pela presente revisão.

## 8. Conclusão
**APTO PARA EVOLUÇÃO FOCAL E DELIBERAÇÃO DOCUMENTAL, COM DUAS RESSALVAS MÉDIAS.** Recomendo ajuste textual limitado CNB-REV-01/02 antes da implementação, mantendo CNB-REV-03 como melhoria de clareza não impeditiva. A revisão não encontrou inconsistência material nos vetores financeiros nem omissão grosseira entre os 34 critérios especificados. O pacote ainda não é contrato homologado do produto e não libera PR técnica, CI, envio, coleta, merge ou publicação. Executor deve atualizar somente os trechos afetados e apresentar rastreabilidade; revisor faz revalidação focal, sem nova auditoria integral. Direção decide encerramento documental e autorização de implementação separadamente.
