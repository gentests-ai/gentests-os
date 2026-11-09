# 09 — Matriz de vulnerabilidades e inconsistências PIX

**Projeto:** SLOT-REVERSE-001 | **Missão:** 002 — Frente G  
**Status:** Inicial — sem vulnerabilidades confirmadas  
**Issues:** G1 #152 · G2 #153

## 1. Escala de classificação

### Severidade
- **Crítica:** possibilidade comprovada de perda/transferência indevida relevante, crédito não lastreado ou comprometimento sistêmico.
- **Alta:** impacto financeiro ou de integridade relevante, com caminho reproduzível e evidência.
- **Média:** inconsistência limitada, risco operacional ou financeiro circunscrito.
- **Baixa:** problema de clareza, rastreabilidade ou experiência sem impacto financeiro demonstrado.
- **Informativa:** observação sem falha demonstrada.

### Confiança
- **Alta:** evidência direta, íntegra, reproduzível e corroborada.
- **Média:** evidência direta parcial ou fonte independente consistente, com lacunas.
- **Baixa:** indício isolado ou informação declarada sem validação.
- **Não avaliável:** não há evidência suficiente.

Severidade e confiança são campos independentes. Não elevar severidade apenas por impacto hipotético.

## 2. Registro de achados
| ID | Cenário | Descrição | Evidência | Impacto | Confiança | Severidade | Status |
|---|---|---|---|---|---|---|---|
| G-PIX-001 | PIX-001 a PIX-010 | Nenhuma ocorrência confirmada no momento da abertura | Nenhuma evidência primária anexada | Não avaliável | Não avaliável | Não classificada | Linha de base |

## 3. Modelo obrigatório por ocorrência
- **Identificador:**
- **Descrição:**
- **Etapa do fluxo / PIX-00X:**
- **Frente autora:** G1 ou G2
- **Evidência disponível e origem:**
- **Resultado esperado (fonte da regra):**
- **Resultado observado:**
- **Impacto potencial e impacto demonstrado:**
- **Grau de confiança:**
- **Severidade:**
- **Limitações da investigação:**
- **Recomendação de correção/mitigação:**
- **Estado:** hipótese / em validação / confirmado / não reproduzido / falso positivo / não verificável

## 4. Regras anti-falso-positivo
1. Estado visual de “pago” não comprova liquidação no banco.
2. Mensagem de erro não comprova falha de conciliação.
3. Ausência de crédito em captura isolada não comprova perda financeira.
4. Divergência de horário pode decorrer de fuso, atraso ou atualização assíncrona; registrar antes de interpretar.
5. Não inferir vulnerabilidade a partir de endpoint imaginado, parâmetro hipotético ou comportamento não observado.
6. Não executar testes destrutivos ou financeiros para reproduzir suspeitas.

## 5. Limitações
A investigação é observacional e restrita. Logs internos, banco de dados, PSP, webhooks, reconciliação e trilhas de auditoria podem não ser acessíveis. A ausência de evidência não prova ausência de falha; registrar como lacuna, não como achado.

## 6. Revisão
G1 e G2 mantêm registros independentes. Revisão cruzada deve questionar evidência, regra esperada, interpretação, severidade e confiança. O aceite final é do Head Tech Lead.