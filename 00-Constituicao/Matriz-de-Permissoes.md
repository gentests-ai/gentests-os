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

## Extensão proposta — Engenharia e Infraestrutura

A tabela abaixo complementa as cinco colunas anteriores, sem alterar suas permissões. **H** indica que a ação exige autorização humana específica; não implica que um agente possa concedê-la a si mesmo.

| Operação | Executor Técnico | Infraestrutura |
|---|---|---|
| Ler documentação e código autorizados | L | L |
| Preparar código, scripts, configuração e PR | C | C |
| Testar em ambiente explicitamente permitido | C | C (apenas verificação operacional) |
| Alterar ambientes não produtivos | H | H |
| Configurar pipelines e monitoramento | H | H |
| Executar merge ou deploy em produção | H | H |
| Alterar segredos, tokens ou permissões | X | H |
| Destruir dados, executar migração irreversível | H | H |
| Comprometer gastos ou assinar contratos | X | X |
| Aprovar a própria entrega como revisor independente | X | X |
| Mudar políticas de governança | X | X |

**Dependências:** [[02-Agentes/Engenharia/Contrato-Agente-Executor-Tecnico]] · [[02-Agentes/Infraestrutura/Contrato-Agente-Infraestrutura]] · [[03-Processos/Entrega-Tecnica-e-Infraestrutura]]. A autorização exigida e os privilégios efetivos devem ser verificados por recurso e operação. Não se presume implantação técnica nem acesso automático.

**Importante:** H não é nível superior de autonomia: exige autorização explícita da direção, delimitando objeto, alvo e janela de execução. Permissões documentadas precisam corresponder às permissões reais dos conectores e ferramentas.

Relacionado: [[Regras-de-Ouro]] · [[02-Agentes/Indice-de-Agentes]]
