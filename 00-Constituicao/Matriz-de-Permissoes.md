---
tipo: politica
id: POL-003
status: proposta
versao: 1.0.0
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

**Importante:** H não é nível superior de autonomia: exige autorização explícita da direção, delimitando objeto, alvo e janela de execução. Permissões documentadas precisam corresponder às permissões reais dos conectores e ferramentas.

Relacionado: [[Regras-de-Ouro]] · [[02-Agentes/Indice-de-Agentes]]
