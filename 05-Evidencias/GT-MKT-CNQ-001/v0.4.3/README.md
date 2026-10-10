# GT-MKT-CNQ-001 v0.4.3 — correção focal de marca
Execução autorizada: [atividade #38, aprovação da Direção](https://github.com/gentestsai-sudo/gentests-os/issues/38#issuecomment-6102383808). Base: commit aa8b127332eefc143afbc23a9996bbed7b1e7e27 da PR #4. Data: 10/10/2026. Sem distribuição autorizada.

## Identificação
- Anterior preservado: `comercial/GT-MKT-CNQ-001-Guia-Executivo-v0.4.2.pdf`, 67.317 bytes; SHA-256 `44a2cae3dcb8706fb0674b8140a6e8a29edd9688bc6782c9f945dfdcf277b60e`.
- Novo: `comercial/GT-MKT-CNQ-001-Guia-Executivo-v0.4.3.pdf`, 796.103 bytes; SHA-256 `0d667a4f7e77aae5fa26dd1aef3c007ebf1ce3ce1d7026acd6e70edbafac4b8a`. Versão no nome e metadado Subject; cinco páginas. Hash confirmado com hashlib e sha256sum.
- Logo original: [Drive empresarial](https://drive.google.com/file/d/1rWILKE57xnGxQ0ao_DuVkB6GJ_UQU6La/view), `GenTests_logo_horizontal_transparente.png`, 468.695 bytes, 1613 × 466 px, modificação 09/10/2026 13:22:31.735 UTC. Sem versão nominal declarada. SHA-256 `6ee37fe355308b7ca82c3b80841e0b61c011355d82bc6f6d0dee7cbd1a46208c`. Cópia byte a byte em [logo-oficial-original.png](logo-oficial-original.png).
- Fontes de identidade: arquivos canônicos `01-Empresa/Identidade-Visual.md` e `01-Empresa/Registro-de-Ativos-de-Marca.md`, commit a4c3f7606747f29acb6e11928889f962355c3ab7; logo também conferida visualmente com o original do Drive.

## Matriz de alterações e evidências
| Item | Diagnóstico/delta | Evidência e resultado |
|---|---|---|
| Marca, página 1 | Confirmada ausência de logo: zero imagens em todas as páginas; cabeçalho tinha apenas texto GenTests.ai. Inserido PNG original na área livre inferior da primeira página, em fundo claro. | [Antes](antes-poppler-1.png), [depois Poppler](depois-poppler-1.png) e [depois MuPDF](depois-mupdf-1.png). Inspeção visual: sem colisão/corte; aplicação legível. Dimensões 210 × 60,66956 pt, x=44/y=170 no sistema PDF; escala uniforme, sem recorte, recoloração ou redesenho. |
| Textos e assinaturas | Nenhum texto substituído; cabeçalho institucional, metodologia, valores, CTA e numeração 1–7 preservados. Nenhuma assinatura V3 ou segunda assinatura aplicada/substituída. | [Checks](checks-v0.4.3.json): igualdade textual normalizada nas cinco páginas em pypdf; conteúdo já aprovado não reaberto. |
| Páginas 2–5 | Nenhuma alteração visual intencional. | Renderizações MuPDF idênticas pixel a pixel ao v0.4.2, geradas a partir do novo PDF; não é reaproveitamento de evidência histórica. |
| Links | Nenhum destino/retângulo/ação/StructParent modificado. | Comparação das anotações pypdf e links MuPDF; igualdade nas cinco páginas. Não comprova clique em leitor. |
| Acessibilidade | Logo repetindo identificação textual, marcada como Artifact; idioma pt-BR, estrutura original e navegação mantidos pela clonagem do documento. | Inspeção estrutural e cinco itens de navegação preservados; leitura assistiva NÃO EXECUTADA. Não declarar PDF/UA. |
| Identificação do binário | Novo arquivo e Subject v0.4.3; histórico v0.4.2 preservado. | SHA-256 independente acima; aumento de tamanho decorrente da incorporação da imagem original e transparência. |

## Impacto e testes práticos
| Verificação | Encaminhamento na v0.4.3 |
|---|---|
| Integridade | Recomputada em duas implementações; nova revisão focal deve conferir arquivo/hash. Fechamento histórico v0.4.2 não transfere automaticamente. |
| Inspeção visual | Repetida na página 1 em dois motores; páginas 2–5 comparadas com nova renderização. Revisão independente focal pendente. |
| TP-01 — leitor PDF clicável | **NÃO EXECUTADO**. Executar no novo arquivo, mesmo com anotação preservada, para comprovar o binário candidato. |
| TP-02 — leitura assistiva | **NÃO EXECUTADO**. Executar no novo arquivo; verificar também tratamento da imagem como decoração e preservação da leitura. |
| TP-03 — telefone físico | **NÃO EXECUTADO**. Executar no novo arquivo; observar logo, legibilidade/zoom e comportamento de abertura do arquivo maior. |

Seguir procedimento e dados mínimos da decisão #35/matriz GT-MKT-CNQ-009 existente. Esta seção registra somente o impacto do delta, sem substituir a matriz dos testes. Não reutilizar resultados entre versões. Cada execução deve registrar PDF, localização, versão/hash, ambiente/versões, data, passos, resultado, evidência e limitações, sem dados pessoais desnecessários.

## Reprodução
Script: `scripts/correcao_marca_cnq_v043.py`. Executar com quatro argumentos: PDF v0.4.2, PNG original, caminho de saída v0.4.3 e diretório de evidências. Dependências: pypdf, reportlab, Pillow, PyMuPDF e Poppler. O script guarda o hash da entrada e verifica texto, links, idioma, navegação e renderizações. Não sobrescrever artefatos históricos.

## Gate focal
Solicitar ao Revisor Independente somente fidelidade do ativo/aplicação na página 1, legibilidade, preservação dos textos/links/estrutura e identificação/versionamento/evidências. Solicitação documental PRC-MKT-001 na PR #39. Não solicitar auditoria integral de ciência, cálculos, conteúdo ou histórico aprovado sem defeito novo comprovado.

Estados: **autocheck técnico concluído no escopo declarado; parecer independente pendente; conformidade de marca independente pendente; aprovação final da Direção pendente; autorização comercial ausente**. PR #4 aberta e Draft; sem merge, publicação, distribuição, campanha, captação ou alteração de site/CRM/preços/contratos/políticas.
