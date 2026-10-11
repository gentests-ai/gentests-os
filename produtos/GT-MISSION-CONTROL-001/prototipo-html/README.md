# Mission Control — protótipo local

Dados inteiramente fictícios, somente leitura, sem autenticação, API, credenciais, deploy ou tempo real. GitHub é a referência oficial do produto; as evidências do painel são registros locais simulados e não representam o backlog real.

## Executar

Baixe a branch do PR ou seu ZIP. Abra `index.html` nesta pasta em um navegador moderno; mantenha `app.js` e `styles.css` ao lado. Não exige instalação nem servidor. Opcional: `python -m http.server 8000 --bind 127.0.0.1` nesta pasta e abra `http://127.0.0.1:8000`.

## Explorar e testar

- Dashboard: 12 identificadas = 10 estados comprovados na fixture + 2 não verificadas; cobertura 12/15 = 80%. Os 3 ausentes não são contados. KPIs abrem consultas filtradas; lead time permanece Não apurado.
- Missões: busca ID/título e filtros estado, prioridade, área, responsável; Aplicar e Limpar. Desktop oferece Kanban e lista; abaixo de 700 px os grupos ficam verticais.
- GT-DEMO-001 permanece Aguardando revisão em todas as telas. GT-DEMO-002 tem despacho e handoff emitidos, sem aceite/início. GT-DEMO-011 tem merge simulado sem encerramento verificado.
- Abra missão, marcos e fontes locais para consultar evento, ator, ocorrido/observado, confiança e versão. Voltar preserva filtros. A referência externa abre a issue #58, sem alegar que comprova a fixture.
- Navegue por Especialidades, Alertas e Rastreabilidade. Nenhum agente é apresentado como online. Alertas seguem campos/eventos da fixture; não há atraso presumido sem SLA.
- No seletor Cenário demonstrativo, experimente falha 429, desatualização e inventário vazio. Falhas mantêm snapshot anterior, último sucesso e tentativa simulados.
- QA: testar desktop, 320/390 px, zoom 200%, Tab/Shift+Tab/Enter, foco ao voltar, leitor de tela e anúncio de filtros. Verificar ausência de rolagem horizontal da página, todas as rotas e combinações de filtros.

## Validação executada pela Engenharia

`node --check app.js` passou. `node test.cjs` passou: 20 verificações, com Node e DOM simulado, cobrindo partição, IDs, filtros, rotas, eventos, ausência de aceite presumido, merge sem encerramento, falhas/vazio, escaping, CSP e ausência de APIs de rede/storage.

**Não realizado:** renderização em navegador, capturas, layout real, teclado real, leitor de tela ou dispositivos físicos. Playwright está disponível no ambiente de Engenharia, mas seu executável Chromium não está instalado; tentativa de inicialização falhou por executável ausente. Testes com DOM simulado não homologam interface nem CA de produção. QA funcional focal permanece pendente.

Autenticação, integração real, segurança backend, sincronização e reconciliação com missões reais ficam fora desta autorização. Nome da empresa é texto; logo oficial não foi reproduzido sem o ativo original. Nenhuma documentação UX existente foi alterada.

Referências: [issue #58](https://github.com/gentestsai-sudo/gentests-os/issues/58), [despacho ENG-01](https://github.com/gentestsai-sudo/gentests-os/issues/58#issuecomment-6112912488), UX integrada pelo PR #59 no commit `4ac22f6cd6fbdeaf35473e878277c4e58250031e`.
