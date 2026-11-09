---
id: GT-PROD-CNB-001-PLN
produto: GT-PROD-CNB-001
tipo: backlog-riscos-decisoes
versao: 0.1.0
status: proposta
estado_documental: em-validacao
data: 2026-10-10
responsavel: Produto
aprovador: Direcao
validacao_independente: pendente
implementacao: nao-autorizada
publicacao: bloqueada
---

# Backlog, riscos, dependências e decisões da Direção

## 1. Backlog priorizado por entrega

Itens são propostas não iniciadas; prioridade não é autorização. Produto especifica, Executor futuro implementa em PR do site autorizada, QA verifica e Revisor emite parecer separado. Direção mantém decisões e capacidade.

| ID/prioridade | Entrega e motivo | Dependência / aceite |
|---|---|---|
| B-01 P0 pré-MVP | Revisão financeira/metodológica das regras e limites | Guia CNQ-01, RN-01–11; CA-02–18 |
| B-02 P0 pré-MVP | Direção aprovar escopo núcleo, capacidade e teto de esforço | D-01/02; preservar PLN-COM-001 |
| B-03 P0 MVP núcleo | Motor puro, precisão decimal e estados | B-01/02; CA-02–18/33 |
| B-04 P0 MVP núcleo | UI responsiva, memória e conciliação | B-03; CA-01/16–20/34 |
| B-05 P0 MVP núcleo | Relatório HTML e impressão local | B-03/04; CA-21/22 |
| B-06 P0 MVP núcleo | Regressão automatizada e QA visual/assistivo independente | B-03–05; CA-19–21/28/34 |
| B-07 P1 MVP núcleo | Conteúdo SEO e links comerciais aprovados | Autorização guia/indexação; CA-30 |
| B-08 P0 gate lançamento | Parecer independente, decisão, PR técnica e rollout/rollback | Evidência do commit final; não autorizado agora |
| B-09 P0 opcional | Decidir jurídico/fornecedor/retention/owner para relatório e-mail | D-03–05; GT-LGPD-001–004 |
| B-10 P1 opcional | Backend de e-mail, idempotência, quota, template e status | B-09, autorização técnica; CA-23–27/32 |
| B-11 P0 para ativar e-mail | Ensaios sintéticos de entrega, direitos, supressão, abuso e acessos | B-10; LP-01–12 e CA-23–28; gate específico |
| B-12 P1 opcional | Telemetria mínima de eventos e dashboard agregado | D-06; CA-28/29; sem valores individuais |
| B-13 P2 evolução | Vários incidentes/perfis, média e totais observados | IDs únicos/completude; não extrapolar perfil único |
| B-14 P2 evolução | Sensibilidade com parâmetros editados pelo usuário | Hipóteses explícitas; sem percentis/probabilidades inventadas |
| B-15 P2 evolução | Entrada em minutos e agregados recorrentes fracionários | Nova precisão/unidades e regressão |
| B-16 P3 evolução | Importação local sanitizada de incidentes/CSV | Sem integrações/dados reais por padrão; revisão de privacidade |
| B-17 P3 evolução | Exportação PDF com acessibilidade verificada | HTML canônico e visual/assistivo; não chamar print PDF/UA |
| B-18 P3 evolução | Medição antes/depois por exposição equivalente | Protocolo CNQ-03, coortes e limites; não ROI automático |

Não construir B-13–18 para destravar MVP. Sem criar agente, novo CRM, campanha, integração operacional ou banco de incidentes nesta etapa.

## 2. Riscos e tratamento

| ID/risco | Prioridade e tratamento | Responsável/dependência |
|---|---|---|
| R-01 Total chamado de perda comprovada/caixa | Alta: rótulo gerencial, origem, natureza e limites persistentes | Produto + financeiro/revisor; B-01 |
| R-02 Horas/receita/fornecedor duplicados | Alta: confirmação, refs anônimas, exclusão de conflitos, revisão do método; confirmação não audita | Produto/QA; CA-06–09 |
| R-03 Ausências tratadas como zero | Alta: estados separados, subtotal incompleto e projeção parcial | Executor/QA; CA-03–05 |
| R-04 Perfil único extrapolado a todos incidentes | Alta: projeção condicional e mesma classe; múltiplos perfis apenas evolução | Produto; RN-05 |
| R-05 E-mail gera marketing indevido/exposição | Alta: opt-in independente, minimização de valores transmitidos, juridico/retention e kill switch | Direção/privacidade/técnico; B-09–11 |
| R-06 Gratuidade presumida ou quota esgotada | Média: verificar plano/envio, teto zero adicional e limites; não upgrade automático | Direção/técnico; D-04 |
| R-07 Produto distrai da primeira venda | Média: núcleo pequeno, teto de esforço e prioridade explicitamente deliberados | Direção; PLN-COM-001 |
| R-08 Layout/relatório ilegível | Alta: todas as telas/estados testados e inspeção independente do artefato final | QA/revisor; B-06 |
| R-09 Guia/LGPD/site evoluem em PRs separadas | Média: fixar referências, verificar deltas antes de implementar; não tratar draft como main | Produto/revisor |
| R-10 Conciliação simplificada cria falsa confiança | Alta: ferramenta não verifica documentos; exemplos e labels não auditados; sem alegar comprovado | Produto/financeiro |
| R-11 Spam a terceiros / timeout duplica e-mail | Alta: backend seguro, quota, idempotência e estado inconclusivo verdadeiro | Técnico/QA; CA-25–27 |
| R-12 Logs/analytics revelam custos da empresa | Alta: allowlist, zero valores nos eventos, inspeção network/logs e retention | Técnico/privacidade; CA-28 |
| R-13 Norma proposta tomada como homologada | Alta: separar fonte consultada, revisão, decisão e configuração | Direção/revisor; README |

## 3. Decisões solicitadas — nenhuma preenchida em nome da Direção

| ID | Questão e recomendação preparada | Efeito de adiar |
|---|---|---|
| D-01 | Aprovar escopo: núcleo público sem cadastro e e-mail opcional separado? Recomenda-se esta composição, mantendo prioridade de e-mail para guia já documentada | Não iniciar implementação |
| D-02 | Quem executa e mantém, qual prioridade frente ao PLN-COM-001 e teto de horas? Estimativa hipotética núcleo 28–48h; recomendar orçamento/escopo explícitos | Sem prazo/compromisso |
| D-03 | Quem valida método financeiro, conciliação, precisão e limites? Designar revisão independente proporcional antes de código | Regras permanecem propostas |
| D-04 | Incluir e-mail no primeiro lançamento ou fase posterior? Qual provedor, plano/domínio/DNS, limites e custo máximo? Recomenda-se fase posterior se gates não resolvidos | E-mail desligado; não prometer entrega |
| D-05 | Controlador, canal, bases por finalidade, países/mecanismos, retenção e responsáveis reais? Reusar GT-LGPD, completar fatos e validar juridicamente | Nenhuma coleta/envio/marketing novo |
| D-06 | Aprovar mensuração mínima e fornecedor? Qual janela/coorte e retention? Recomenda-se sem valores e sem rastreio de leitura | Eventos só especificados, não ativados |
| D-07 | Autorizar uso/distribuição de qual versão do guia, rota/domínio, indexação, CTA e contato? Sem preço/diagnóstico gratuito | SEO/links comerciais ficam planejamento |
| D-08 | Após revisão, autorizar PR técnica de implementação em gentests-site? Testes, preview e publicação com alcance separado | Esta PR continua exclusivamente documental |
| D-09 | Quem emite parecer independente sobre o pacote e registra encerramento documental? | Não autoaprovar nem marcar ready/merge |
| D-10 | Confirmar 4 blocos, limites numéricos e relatório local sem persistência? São opções de MVP, ampliar só com revisão | Contrato proposto não homologado |

Registro futuro de decisão: ID, decisor humano, data, documentos/versões/commit, aprovar/ajustar/adiar/rejeitar, fundamento e alcance. Aprovar documento não concede merge, infraestrutura, implementação, teste com dados, captação, publicação ou campanha. Esta tarefa autoriza somente documentação em branch/PR Draft.

## 4. Prontidão e passagem para revisão

Conferência do autor: fontes e status fixados; seis documentos integrados; exemplo canônico e aritmética conferidos; regras de ausências/duplicidades, privacidade e restrições registradas. Revisor deve verificar suficiência funcional/técnica e coerência com CNQ-01, LGPD atual e PLN-COM-001; apontar achados específicos por regra/CA, sem afirmar testes do produto executados.

Gate documental: documentação completa → parecer independente → tratamento focal se necessário → Direção delibera versões/alcance. Gate técnico futuro separado: autorização de implementação → PR do site e testes sintéticos → inspeção visual/assistiva e privacidade do commit final → autorização de lançamento/merge conforme alcance. Nada desta sequência foi disparado por esta especificação.

Sem contratação, código de calculadora, alteração de site, serviço ativado, coleta, merge ou atividade comercial. Os únicos atos externos autorizados são o registro destes documentos em branch própria e abertura da PR Draft.
