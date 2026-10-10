---
tipo: plano-comercial
id: PLN-COM-002
versao: 0.1.0
status: proposta
marca: nome-pendente
responsavel: Comercial
aprovador: direcao
---
# PLN-COM-002 — Piloto de venda de sites (marca ainda sem nome)

**Hipótese:** empresas de serviços com presença digital fraca ou dificuldades verificáveis em seus sites podem querer contratar modernização ou um novo site simples. **Não afirmar que o site é ruim sem prova.** Marca, preço e execução não estão aprovados.

## Oferta candidata
Landing page ou site institucional enxuto, responsivo, com conteúdo fornecido ou aprovado pelo cliente, limites de páginas e revisões e prazo fechado. Não incluir e-commerce, integrações complexas, produção de conteúdo ilimitada ou manutenção sem contrato. **Não há preço definido:** calcular após piloto real de esforço/custo.

## Identificação de oportunidades
Selecionar manualmente até 10 sites institucionais públicos de um único segmento; verificar canais comerciais institucionais públicos sem coleta massiva de dados pessoais. Priorizar negócios com possibilidade plausível de melhorar jornada de contato/agendamento.

## Triagem técnica sem LLM
Usar [[03-Processos/PIL-SITES-001-Triagem-Sites]] apenas depois de testar o script em ambiente autorizado. Critérios de *revisão*, não reprovação: score Lighthouse performance abaixo de **50**; **3 ou mais tipos** de violação axe-core; **2 ou mais links** internos com HTTP 404/410, na pequena amostra. Playwright captura somente página pública. Evitar carga, autenticação, exploração, formulários e scraping amplo. Medir duração e falsos positivos; resultados inconclusivos não viram acusações.

## Ciclo inicial de 14 dias
1. Confirmar um nicho e reunir 10 candidatos; triagem controlada de 1–3 sites primeiro, expandir somente se resultado válido.
2. Validar manualmente até 3 oportunidades com achados concretos (limitações explícitas).
3. Criar até 3 mensagens individuais, curtas e respeitosas, descrevendo oportunidade comprovável, sem linguagem depreciativa. Submeter ao Validador e autorização humana antes de qualquer envio.
4. **Somente após resposta interessada**, elaborar até três prévias visuais leves, marcadas como conceituais e não oficiais, respeitando marca/conteúdo de terceiros e sem publicar cópias.
5. Confirmar requisitos, escopo, custo de criação e manutenção, preço e condições; proposta aprovada e contrato válido antes da execução.
6. Ao final de 14 dias, comparar interesse e custo desta frente com GenTests.ai. Não ampliar sem evidências.

## Custos e restrições
Nenhum token de LLM na triagem inicial. IA generativa apenas para interessados; custo e tempo rastreados por oportunidade. Não criar novo site institucional, CNPJ, assinatura, CRM ou automação de disparos neste piloto. Mesma infraestrutura interna de rastreabilidade, mas **marca, público e métricas separados**.

## Critérios de sucesso de aprendizado
Relatório reprodutível sem achados falsos apresentados como fatos; até 3 contatos personalizados aprovados; pelo menos um retorno interessado como meta de teste, não previsão. Medir sites verificados, falsos positivos, respostas, tempo e despesas.

## Decisões pendentes
Nome e identidade comercial; oferta fechada e limites de revisão/manutenção; precificação; contrato; autorização do canal de contato e tratamento de dados; confirmação da capacidade de entrega e suporte.

**Relacionados:** [[03-Processos/PIL-SITES-001-Triagem-Sites]] · [[00-Constituicao/Excelencia-Enxuta-5S]] · [[00-Constituicao/Quality-Gates/QG-STR-001-Disciplina-Estrategica]]
