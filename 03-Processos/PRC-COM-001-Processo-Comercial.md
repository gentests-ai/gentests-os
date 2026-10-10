---
tipo: processo
id: PRC-COM-001
versao: 0.1.0
status: proposta
responsavel: Comercial
aprovador: Direcao
objetivo: Primeiro cliente pagante da GenTests.ai
---
# PRC-COM-001 — Processo comercial enxuto

> **Status: proposta para aprovação humana.** Não autoriza envio externo, precificação ou contratação.
> **Prioridade:** primeiro cliente pagante, com qualidade, simplicidade, segurança e evidência.

## Oferta de entrada (hipótese a validar)
Diagnóstico **pago** e delimitado de **uma jornada crítica** de produto digital (web/API), para identificar riscos prioritários, lacunas de testes e recomendações de prevenção.

Entregáveis propostos, sujeitos à confirmação de escopo: mapa conciso de riscos; cobertura mínima orientada a risco; recomendações priorizadas; reunião de devolutiva. Não prometer cobertura total, eliminação de bugs, certificação ou resultados financeiros sem evidência.

**Antes de ofertar:** direção define prazo, preço, capacidade, condições de acesso e dados, critérios de aceite, limites de responsabilidade e modelo contratual. Não solicitar credenciais nem dados sensíveis na primeira conversa.


**Roteiro complementar de prospecção:** [[03-Processos/Prospeccao-Comercial]] (ID próprio COM-APOIO-PROSPECCAO-001; este arquivo é a única fonte canônica de PRC-COM-001).

## Fluxo operacional
| Etapa | Entrada e ação | Critério de saída | Responsável |
|---|---|---|---|
| 1. Prospectar | Identificar empresa B2B SaaS/web/API e hipótese de dor real, com fonte | Contato e motivo de aderência registrados | Comercial |
| 2. Abordar | Redigir abordagem curta e personalizada; checagem de fatos, marca e segurança | Envio **somente após autorização**; registrar data/canal real | Comercial + direção |
| 3. Qualificar | Entender produto, jornada crítica, impacto, urgência, interlocutor e próximo passo | Necessidade concreta + interlocutor capaz de avançar + próximo passo | Comercial + direção |
| 4. Propor | Delimitar uma jornada, entregáveis, exclusões, prazo e preço | Proposta revisada por Quality Gate, aprovada pela direção e enviada com autorização | Comercial + direção |
| 5. Negociar e fechar | Ajustar condições sem promessas infundadas | Aceite contratual documentado, não mera intenção verbal | Direção |
| 6. Transferir | Resumir escopo vendido, premissas, riscos, prazo e aprovações | Handoff explícito para entrega; acessos e dados somente conforme autorização | Direção + execução |

## Gates proporcionais
- **G0 — Entrada**: perfil de cliente, hipótese de dor e fonte identificados.
- **G1 — Contato externo**: conteúdo verificável, linguagem clara, privacidade, identidade visual e autorização. O piloto [[03-Processos/Piloto-Validacao-Email-Comercial]] cobre somente parte da validação de e-mail.
- **G2 — Proposta**: escopo, preço, prazo, capacidade, risco e responsabilidade aprovados pela direção.
- **G3 — Contrato**: aceite/documento confirmado, condições pactuadas, antes do início.
- **G4 — Entrega**: transferência rastreável sem reinterpretação unilateral do escopo.

## Registro único de oportunidade
Um registro por oportunidade: `id`, empresa/contato profissional, origem/fonte, problema hipotético ou confirmado, etapa, último contato, próximo passo/data, responsável, documentos relacionados, autorização para ação externa. Registrar o mínimo necessário, evitar dados pessoais desnecessários. Não criar planilha/CRM paralelo enquanto Obsidian for suficiente.

Sugestão de ID: `OP-2026-001` (sequencial, não reutilizar). Vínculos: `OP -> proposta -> contrato -> entrega` somente se existirem. Não fabricar artefatos ou evidências ausentes.

## Medição e cadência
Indicadores mínimos: contatos efetivamente realizados, respostas, conversas qualificadas, propostas autorizadas/enviadas e contratos assinados/fechados.
Revisão semanal de 15 minutos: avaliar onde o funil trava, escolher **um** ajuste e registrar resultado. Metas são hipóteses, nunca projeção garantida.

## Prioridade do primeiro ciclo
1. Confirmar oferta inicial (incluindo prazo/preço/capacidade).
2. Selecionar pequeno grupo de empresas com hipótese específica de dor.
3. Executar contatos individualizados com autorização e acompanhar retorno.
4. Construir apenas demonstração mínima se realmente ajudar a gerar conversas.

Não expandir campanha, automatizar disparos ou construir sistemas de demonstração complexos sem evidência de demanda. Aplicar [[00-Constituicao/Quality-Gates/QG-STR-001-Disciplina-Estrategica]] quando houver ampliação de escopo/investimento.

## Limites de autonomia
- Comercial pesquisa, prioriza e redige. Não envia, publica, assina, assume preço, dá desconto, contrata ou acessa informações confidenciais sem autorização.
- AGT-VAL avalia conformidade dentro de suas capacidades; parecer técnico não substitui aprovação da direção.
- AGT-X9 identifica alertas rastreáveis, não altera documentos nem cria RNC por conta própria.
- RNC exige confirmação, correção e revalidação conforme [[03-Processos/Gestao-de-Nao-Conformidades]].

## Relações e pendências
- [[01-Empresa/Missao-Visao-Valores]] — diretrizes estratégicas, ainda em proposta.
- [[09-Backlog/RNC/RNC-2026-001]] — plano de visibilidade v1.1 pendente de revalidação.
- [[03-Processos/Piloto-Validacao-Email-Comercial]] — validação de e-mail fictício, não fluxo comercial completo.
- **Pendente de decisão humana:** aprovar este processo, oferta exata e limites comerciais.

## Critério de sucesso
Primeiro contrato com escopo aceito e evidência real, sem violar segurança ou comprometer qualidade. O processo deve custar menos esforço do que economiza.
