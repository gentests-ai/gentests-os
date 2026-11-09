# 02 — Arquitetura observável

**Projeto:** SLOT-REVERSE-001  
**Missão:** 002 — Poker Kingdom Win / PGW.bet  
**Frente:** B — AGT-ENG  
**Estado:** Parcial; inspeção pública inicial  
**Consulta:** 09/11/2026 (BRT)

## 1. Escopo e limites
Inspeção restrita à superfície pública e aos dados expostos por navegação normal. Sem autenticação, bypass, tentativa de contornar anti-bot, exploração de endpoints, dados de terceiros, extração de segredos ou operação financeira.

## 2. Observação direta do alvo
- URL fornecida: https://pgw13.com/?a=uq6igjhx
- A abertura pública retornou título de página **PGW.BET**.
- O método de leitura não retornou linhas de conteúdo HTML legíveis.
- Não foram obtidos headers HTTP, DOM, lista de scripts, requisições de rede, cookies, storage, versão de frontend ou payloads do jogo.
- Não há identificação técnica verificável de fornecedor, agregador ou endpoint do jogo na evidência coletada.

**Fato observado:** título público PGW.BET. A ausência de conteúdo legível não prova que o site esteja vazio ou sem integração.

## 3. Identificadores do jogo
A investigação anterior informa Poker Kingdom Win, fornecedor de referência PG Soft e ID de catálogo 2009635. iGaming Tools descreve, em captura independente, caminho de build /2009635/index.html e ausência de versão impressa no build capturado. Esse caminho **não foi observado no domínio PGW** e não deve ser atribuído à implantação PGW.

## 4. Matriz da arquitetura observável

| Camada | Evidência | Estado |
|---|---|---|
| Navegador / página pública | Título PGW.BET | Observado parcialmente |
| Frontend do operador | DOM/scripts não legíveis | Não identificado |
| Login/autenticação | Não inspecionado | Fora do escopo desta etapa |
| Catálogo/lobby | Jogo identificado na investigação anterior | Registro prévio; captura pendente |
| Agregador | Nenhuma evidência direta | Não identificado |
| Integração PG Soft | Fornecedor em fontes externas; sem endpoint PGW | Não confirmada tecnicamente |
| Cliente HTML5 | HTML5 citado genericamente em material do fornecedor; build externo secundário | Não atribuído à PGW |
| API de sessão/saldo/resultado | Nenhuma requisição observada | Não identificada |
| RNG / matemática no servidor | Não acessível pela superfície consultada | Não observável |
| Versão / perfil RTP | Não expostos no conteúdo lido | Não identificados |

## 5. Tecnologias e dependências
Nenhum framework, CDN, servidor, biblioteca, SDK, agregador, provedor de identidade ou protocolo foi confirmado diretamente. Não preencher a lacuna com fingerprinting especulativo. A documentação corporativa PG Soft descreve suporte geral a HTML5, iOS, Android, macOS e Windows; isso não demonstra qual cliente ou SDK a PGW utiliza.

## 6. Fluxos de comunicação
Não foi possível mapear fluxos do jogo porque a inspeção não produziu DOM ou log de rede. Não inferir endpoints, métodos HTTP, WebSocket, mensagens, autenticação, assinatura, tokens ou protocolo proprietário.

Próxima coleta autorizada, se disponível por navegação pública normal:
1. Capturar página pública e lobby em navegador comum, sem iniciar sessão.
2. Registrar URL final e redirecionamentos visíveis.
3. Registrar metadados públicos do documento e recursos carregados, sem baixar/extrair código proprietário protegido.
4. Se houver demonstração pública sem conta, registrar apenas metadados de requests/respostas necessários para identificar fornecedor/build; não chamar endpoints manualmente.
5. Remover cookies, IDs de sessão, tokens e dados pessoais antes de anexar evidências.
6. Se a observação exigir login, sessão autenticada, carteira ou ação financeira, parar e classificar como não observável nesta missão.

## 7. Limites de observabilidade
- Página sem texto extraível pode depender de JavaScript, recursos externos, redirecionamento, proteção ou conteúdo dinâmico; nenhuma causa foi confirmada.
- A camada cliente não revela por si só RNG, pesos de símbolos, estado do servidor ou integridade do resultado.
- Caminho de asset/ID não prova versão matemática nem configuração RTP.
- Splash screen ou selo de laboratório não substitui certificado específico e escopo de avaliação.
- Sem documentação do operador ou demonstração pública autorizada, não é possível atribuir arquitetura de backend à PGW.

## 8. Evidências e referências
1. [PGW.BET — URL alvo](https://pgw13.com/?a=uq6igjhx) — abertura pública retornou título, sem linhas de conteúdo legíveis.
2. [iGaming Tools — captura Poker Kingdom Win](https://i-gaming.tools/slot-games/poker-kingdom-win-b30/) — fonte secundária informa caminho de build /2009635/index.html e ausência de versão visível; não prova implantação PGW.
3. [PG Soft — Corporate](https://www.pgsoft.com/corporate) — informação geral sobre plataformas/laboratórios; não comprova tecnologia da integração PGW.

## 9. Parecer da etapa
**EM ANDAMENTO / EVIDÊNCIA INSUFICIENTE PARA DIAGRAMA DE INTEGRAÇÃO.** A única observação direta registrada é o título público da página. Nenhum componente, versão, fluxo de rede ou dependência específica foi confirmado. Frente B segue independente da Frente A; novas conclusões exigem evidência pública direta e reproduzível.
