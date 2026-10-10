---
tipo: metodologia
id: GQF-001
versao: 0.1.0
status: proposta
responsavel: Direcao
---
# GenTests Quality Framework — GQF-001

## Propósito
Organizar a qualidade de artefatos, processos e agentes de IA com foco em risco, evidência, alinhamento estratégico e melhoria contínua.

**Status atual:** metodologia interna proposta, em implantação piloto; não anunciar a clientes como produto consolidado ou certificação.

## Ciclo
1. **Definir:** objetivo, requisitos, contexto, responsável e destino do artefato.
2. **Classificar:** QG-L, QG-M ou QG-H por critérios da [[00-Constituicao/Quality-Gates/QG-001-Politica]].
3. **Executar:** agente responsável produz versão com referências e evidências.
4. **Pré-validar:** checagens técnicas determinísticas quando aplicáveis.
5. **Validar:** revisão independente semântica e contextual conforme risco.
6. **Autorizar:** direção decide nas ações sensíveis; parecer técnico não é permissão de envio.
7. **Registrar:** resultado, evidências e rastreabilidade.
8. **Aprender:** auditoria amostral, indicadores e prevenção de recorrência.

## Definição de concluído
Um artefato só pode receber estado **concluído** quando requisitos, checklist aplicável, evidências e aprovações exigidas estiverem satisfeitos. **Não verificável** não significa aprovado.

## Medidas futuras (não inventar números)
- Taxa de bloqueios procedentes e falsos positivos.
- Tempo de validação por classe de risco.
- Escape de defeitos após a liberação.
- Reincidência por tipo de falha.
- Aderência a identidade visual e políticas aprovadas.

## Piloto inicial
[[03-Processos/Piloto-Validacao-Email-Comercial]]; critérios específicos em [[07-Templates/Checklists/Comercial-Email]]. Registros em [[07-Templates/Relatorio-Validacao-TEMPLATE]].

## Restrições
- Nada de aprovação automática por checkbox ou resposta de IA.
- Não usar marca de terceiros nem materiais confidenciais como exemplos públicos sem autorização.
- A metodologia não transforma, por si só, Markdown ou prompts em controles técnicos.
