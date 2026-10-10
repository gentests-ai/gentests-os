---
tipo: processo
id: AGT-VAL-V02
status: proposta
versao: 0.2.0
---
# Parecer de validação — versão 0.2

## Objetivo
Um rascunho comercial recebe parecer estruturado, com achados, gravidade, limitações, autorização humana pendente e `pode_enviar: false`.

## Execução na nuvem
`python3 -m unittest discover -s tests -p 'test_*.py' -v`

`python3 scripts/agt_val_review.py tests/fixtures/email_valido.json`

## Controles
- A detecção automática de alegações e segredos é heurística: pode falhar.
- Um relatório sem erros técnicos **não equivale a parecer conforme**.
- A validação semântica de missão, visão e valores ainda depende de revisão independente.
- As duas assinaturas são ativos oficiais, mas a segunda ainda precisa de identificação canônica.
- Não enviar mensagens nem processar dados reais de clientes nesta fase.
- Toda aprovação externa e toda alteração de política são humanas.

Relacionado: [[01-Empresa/Registro-de-Ativos-de-Marca]] · [[00-Constituicao/Quality-Gates/QG-001-Politica]]
