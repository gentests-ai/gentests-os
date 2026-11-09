# 01 — Auditoria documental

**Projeto:** SLOT-REVERSE-001  
**Missão:** 002 — Poker Kingdom Win / PGW.bet  
**Frente:** A — AGT-AUD  
**Estado:** Parcial; pesquisa inicial, não é parecer final  
**Consulta:** 09/11/2026 (BRT)

## 1. Método e limites
Hierarquia de evidência: documentação oficial do fornecedor/regulador; relatório específico de laboratório; captura verificável do jogo; catálogo/análise de terceiro. Informação de terceiro não é tratada como confirmação oficial. Somente fontes públicas. Sem login, apostas, carteira, bypass, proteção ou dados privados.

## 2. Identidade e parâmetros preliminares

| Campo | Valor encontrado | Classificação / ressalva |
|---|---|---|
| Título | Poker Kingdom Win | Secundário convergente |
| Fornecedor | PG Soft / Pocket Games Soft | Secundário convergente; não prova build PGW |
| ID | 2009635 | Secundário; falta catálogo oficial diretamente validado |
| Código | poker-kingdom | Secundário |
| Grade | 5 rolos × 3 linhas | Secundário convergente |
| Formas | 243 ways | Secundário convergente |
| RTP referência | 96,74% | Secundário convergente |
| Volatilidade | Alta | Secundário convergente |
| Prêmio máximo | 5.000× | Secundário convergente |
| Documento | versão 1.0.r5, 29/01/2026 | Citado por terceiro; PDF oficial ainda não validado diretamente |

Fontes: [North Island Casinos](https://northislandcasinos.com/games/pg-soft/poker-kingdom-win/) e [iGaming Tools](https://i-gaming.tools/slot-games/poker-kingdom-win-b30/). Os dados são linha de base secundária, não especificação certificada do build PGW.

## 3. Divergência de RTP: 96,74% × 96,75%
- RTP de referência em fontes secundárias: **96,74%**.
- RTP informado na interface PGW na MISSÃO 001: **96,75%**; a captura original precisa ser anexada ao dossiê.
- Diferença nominal: **0,01 ponto percentual** (0,0001 em taxa decimal).
- Não atribuir a diferença automaticamente a arredondamento, configuração alternativa, erro de interface ou irregularidade.
- Não foi encontrada evidência pública suficiente de perfis alternativos nem de qual perfil estaria carregado na PGW.

Hipóteses em aberto, sem confirmação: perfil distinto; valor informativo arredondado/cadastrado separadamente; metadado desatualizado; transcrição de build/documento diferente.

Para resolver: PDF oficial da versão/configuração entregue, identificação de build/perfil RTP da sessão PGW e captura legível da tela informativa com data/hora. Até lá, divergência **não resolvida**.

## 4. Regras e mecânicas — somente evidência secundária
North Island Casinos descreve: grade 5×3, 243 ways, cascatas, símbolo Multiplier-Ways com valor inicial 3 que representa pilha/ways (não multiplicador monetário direto), persistência após vitória, incremento de +1, transformação conforme paridade, posições persistentes em Free Spins, RTP 96,74% dividido em 62,38% jogo principal + 34,36% Free Spins, hit rate total 21,37% (20,97% principal + 0,40% Free Spins), teto de 5.000× e Feature Buy na referência.

Não congelar essas regras para implementação até confronto com documentação oficial e paytable. iGaming Tools declara captura manual de 33 telas e OCR da paytable, mas aponta lacunas: RTP/volatilidade não impressos no build capturado, ausência de versão visível, transformação ímpar sem frame dedicado e incerteza sobre retrigger. É captura independente, não documentação oficial.

## 5. Certificação e laboratórios
A [página corporativa oficial PG Soft](https://www.pgsoft.com/corporate) identifica BMM Testlabs e Gaming Associates e descreve suas credenciais. Isso **não comprova certificação específica** do Poker Kingdom Win, ID 2009635, versão ou build PGW.

iGaming Tools relata que o splash screen capturado exibe “Certified by GA / BMM” e marca MGA. É observação secundária sem certificado específico anexado.

O [relatório público de Gaming Associates para Butterfly Blossom](https://www.pgsoft.com/uploads/GamesResource/e015159f-4320-4c40-863d-8d14b39d73c9.pdf) demonstra apenas que há relatórios de avaliação publicados para outros jogos PG Soft; não é certificado deste jogo.

## 6. Integração PGW
A URL https://pgw13.com/?a=uq6igjhx foi aberta publicamente e retornou título PGW.BET, mas sem linhas de conteúdo legíveis no método de inspeção. Não há evidência documental suficiente sobre entidade operadora, agregador, endpoint de lançamento, build, perfil RTP ou certificado da implantação PGW.

## 7. Fontes consultadas
1. [PG Soft — Corporate](https://www.pgsoft.com/corporate) — oficial, corporativa, não específica do jogo.
2. [North Island Casinos — Poker Kingdom Win](https://northislandcasinos.com/games/pg-soft/poker-kingdom-win/) — secundária, especificação e referência a versão.
3. [iGaming Tools — captura Poker Kingdom Win](https://i-gaming.tools/slot-games/poker-kingdom-win-b30/) — captura manual secundária e lacunas declaradas.
4. [Gaming Associates — relatório Butterfly Blossom](https://www.pgsoft.com/uploads/GamesResource/e015159f-4320-4c40-863d-8d14b39d73c9.pdf) — oficial hospedado no domínio PG Soft, mas de outro jogo.
5. [PGW.BET](https://pgw13.com/?a=uq6igjhx) — alvo; conteúdo não legível pelo método utilizado.

## 8. Lacunas e próximos passos
- Localizar e validar diretamente o PDF oficial Poker Kingdom Win Game Information, versão 1.0.r5.
- Extrair regras, paytable, símbolos, Scatter, Free Spins e limites.
- Verificar se o documento descreve uma ou várias configurações RTP.
- Localizar certificado/relatório de laboratório para ID 2009635 e versão exata.
- Anexar captura verificável do RTP 96,75% exibido pela PGW.
- Não emitir conclusão de conformidade, fraude ou aleatoriedade antes das evidências primárias.

## 9. Parecer da etapa
**EM ANDAMENTO.** A especificação secundária orienta a coleta, mas não basta para congelar regras matemáticas ou identificar o RTP implantado na PGW. Frente A segue independente da Frente B. Auditoria final deve ser feita por agente distinto do autor da implementação.
