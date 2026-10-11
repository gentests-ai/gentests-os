---
tipo: politica
id: POL-003
status: proposta
versao: 1.1.0
---
# Matriz de permissões

Legenda: **L** ler; **P** preparar; **C** execução controlada sob autorização definida; **H** aprovação humana por ação; **X** proibido.

| Operação | Comercial | Marketing | QA | Financeiro | Auditor |
|---|---|---|---|---|---|
| Consultar informação pública | L | L | L | L | L |
| Produzir rascunhos | P | P | P | P | P |
| Atualizar CRM dentro do escopo | C | X | X | X | L |
| Enviar e-mails externos | H | H | X | X | X |
| Publicar campanhas | X | H | X | X | X |
| Alterar identidade visual | X | H | X | X | X |
| Executar testes em ambiente permitido | X | X | C | X | X |
| Acessar dados financeiros | X | X | X | C | L somente relatórios autorizados |
| Comprometer gastos/assinar contratos | X | X | X | H | X |
| Mudar regras de governança | X | X | X | X | X |
| Revisar evidências e alertar desvios | L | L | L | L | C |

## Detalhamento proposto — operações do Financeiro

A coluna Financeiro acima permanece como referência geral; os controles abaixo detalham operações, sem ampliar autonomias. **P** preparar documentos internos; **C** registro controlado em fonte autorizada; **H** exige autorização humana específica antes de executar; **X** proibido.

| Operação financeira | Financeiro | Observação |
|---|---|---|
| Simular preço, margem e cenário financeiro | P | Premissas, fórmulas e fontes explícitas |
| Recomendar preço ou desconto | P | Não equivale a aprovação |
| Aprovar preço final, desconto ou compromisso | X | Decisão da Direção |
| Registrar contas a receber/pagar e conciliar | C | Somente registros autorizados e comprovantes reais |
| Preparar minuta de cobrança ou nota | P | Sem envio ou emissão real |
| Emitir documento fiscal ou cobrança real | H | Autorização específica e requisitos fiscais aplicáveis |
| Enviar cobrança ou dado financeiro a terceiro | H | Verificação de destinatário, privacidade e autorização |
| Executar transferência ou pagamento | X | Não delegado ao agente; ato humano autorizado fora do agente |
| Assinar contrato ou assumir compromisso | X | Direção/responsável formalmente autorizado |
| Acessar contas, extratos e dados financeiros | C | Apenas fontes e permissões efetivamente autorizadas |

**Vínculos:** [[02-Agentes/Financeiro/Contrato-Agente-Financeiro]] · [[03-Processos/PRC-FIN-001-Gestao-Financeira]]. **Apenas alteração documental em proposta:** a tabela não concede privilégios técnicos nem homologa novos fluxos. Reconciliar com extensões concorrentes de POL-003 antes do merge.

**Importante:** H não é nível superior de autonomia: exige autorização explícita da direção, delimitando objeto, alvo e janela de execução. Permissões documentadas precisam corresponder às permissões reais dos conectores e ferramentas.

Relacionado: [[Regras-de-Ouro]] · [[02-Agentes/Indice-de-Agentes]]
