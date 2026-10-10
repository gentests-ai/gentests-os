---
tipo: politica
id: QG-001
versao: 0.1.0
status: proposta
aprovador: direcao
---
# QG-001 — Quality Gate Adaptativo

## Objetivo
Todo artefato corporativo deve passar por validação proporcional ao contexto e ao risco **antes de ser declarado concluído ou enviado**. Abrange código, documentos, e-mails, artes, relatórios, políticas e entregas de agentes.

## Núcleo obrigatório — todos os níveis
1. Alinhamento à missão, à visão, aos valores e às políticas **aprovadas**.
2. Veracidade e rastreabilidade: fatos, métricas e afirmações devem ser sustentados por fontes verificáveis.
3. Segurança, privacidade, permissões e confidencialidade.
4. Objetivo e critério de aceite definidos; responsável e versão identificados.

## Classificação de risco
- **QG-L / Leve:** rascunho ou nota interna sem dados sensíveis, baixo impacto, totalmente reversível.
- **QG-M / Padrão:** comunicação externa, apresentação, código não crítico, relatório técnico ou impacto moderado.
- **QG-H / Crítico:** contrato, política institucional, dados sensíveis para público externo, alto impacto, ação de difícil reversão, produção, cobrança ou decisão financeira relevante.

**Regra de prevalência:** aplicar sempre o nível mais alto acionado por qualquer critério. O agente não pode rebaixar unilateralmente o risco.

## Controles adicionais
- **QG-L:** verificar núcleo obrigatório e consistência básica.
- **QG-M:** adicionar checklist do tipo de artefato, revisão contextual e evidências referenciadas.
- **QG-H:** adicionar revisão independente, registro formal da decisão e autorização humana conforme matriz de permissões.

## Resultado
- **Conforme:** todos os itens aplicáveis verificados com evidências.
- **Correção necessária:** falha corrigível; retorno ao executor e nova validação.
- **Bloqueado:** violação de segurança, política, ausência de aprovação obrigatória ou falha crítica.
- **Não verificável:** evidência insuficiente; não interpretar como conforme.

## Segurança operacional
O Validador não altera o artefato original, não o publica, não libera pagamentos e não aprova o próprio trabalho. Marcação de caixas não substitui comprovação ou aprovação humana. Nenhum agente consegue impor estas regras tecnicamente apenas com Markdown: implantação requer permissões e fluxos reais.

## Próximos documentos
- [[00-Constituicao/Quality-Gates/QG-CORE-Obrigatorio]]
- [[02-Agentes/Validador/Contrato-Agente-Validador]]
- [[07-Templates/Relatorio-Validacao-TEMPLATE]]

## Aprovação
Este texto é uma proposta. Registrar aprovação da direção com data, versão e decisão.
