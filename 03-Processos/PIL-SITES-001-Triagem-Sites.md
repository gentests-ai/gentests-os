# PIL-SITES-001 — Triagem enxuta de sites públicos (proposta)

**Objetivo:** experimentar um filtro técnico barato e reproduzível, sem LLM, sem envio de mensagens e sem qualificar negócios como “ruins” automaticamente. Execute somente contra sites públicos previamente selecionados, respeitando políticas de acesso e limites do serviço.

## Escopo e limites
- 1 a 10 URLs fornecidas manualmente em \`sites.txt\`, uma por linha; execução sequencial, com pausas.
- **Lighthouse**: apenas categoria performance (o comando também computa SEO, mas o filtro utiliza só performance).
- **Playwright**: captura de tela e carregamento em viewport móvel.
- **axe-core**: violações detectadas para WCAG 2/2.1 A/AA; **contagem de tipos de regras violadas**, não contagem de elementos.
- **Links**: máximo de 5 links internos por site, somente respostas **404 ou 410** contam como quebradas; redirecionamentos e erros de rede são inconclusivos.
- Gatilhos independentes: score Lighthouse < 50; pelo menos 3 tipos de violação axe-core; pelo menos 2 links 404/410.
- **Alerta significa revisão humana, nunca reprovação automática.** Resultados podem variar com rede, dispositivo, consentimento de cookies, conteúdo dinâmico e bloqueios anti-bot. Limiares são hipóteses.

**Não execute:** testes de carga, varredura de segurança, exploração, autenticação, cadastros, formulários, extração de contatos nem crawling amplo.

## Executar no computador
Requisitos: Python >= 3.10, Node.js >= 20, npm e acesso permitido aos sites.
\`\`\`bash
python -m pip install playwright requests
npm install --no-save lighthouse axe-core
python -m playwright install chromium
\`\`\`
Crie um \`sites.txt\` na raiz do repositório (não versionar alvos comerciais sensíveis), por exemplo:
\`\`\`text
https://example.com/
\`\`\`
Execute:
\`\`\`bash
python scripts/triagem_sites.py --sites sites.txt
\`\`\`

Resultados locais em \`reports/triagem/\`: \`resumo.csv\`, \`resultado.json\`, capturas, relatórios Lighthouse, violações axe e links por site. **Não publicar relatórios ou capturas de terceiros sem revisão.** Ao compartilhar diagnóstico, apresentar apenas achados confirmados e limitações.

## Custo e decisão
Nenhum token LLM. Há custo de computação/tempo e possível limite de serviço gratuito. Não há workflow agendado nem integração com o Comercial nesta versão. Medir tempo por lote e falsos positivos antes de aumentar.

**Próximo Quality Gate:** rodar com 1–3 sites permitidos, conferir relatórios e fazer revisão humana de cada alerta. Não anunciar ganho de performance nem afirmar perda de vendas sem prova.

Relacionado: [[00-Constituicao/Excelencia-Enxuta-5S]] · [[00-Constituicao/Quality-Gates/QG-STR-001-Disciplina-Estrategica]]
