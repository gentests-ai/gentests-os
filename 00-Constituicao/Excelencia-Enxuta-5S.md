---
tipo: principio-operacional
id: GOV-5S-001
versao: 0.1.0
status: proposta
aprovador: direcao
---
# Excelência Enxuta — 5S Digital

> **A complexidade deve ser justificada. A simplicidade, preservada. A qualidade, comprovada.**

## Propósito
Adotar 5S como princípio operacional transversal da GenTests.ai: qualidade técnica elevada, processos leves e controles proporcionais ao risco, sem abrir mão de segurança, rastreabilidade e evidências.

## Os cinco sensos
1. **Seiri — Utilização:** manter apenas processos, ferramentas e artefatos que tragam valor ou cumpram obrigação real. Eliminar duplicidades com cuidado para não perder evidências ou registros obrigatórios.
2. **Seiton — Organização:** cada decisão, atividade, ativo de marca e evidência deve ter localização e responsável identificáveis.
3. **Seiso — Limpeza:** revisar inconsistências, links quebrados, versões obsoletas e informações sem fonte; preservar histórico no GitHub.
4. **Seiketsu — Padronização:** reutilizar nomenclaturas, templates, fontes oficiais e as duas assinaturas institucionais conforme suas regras de uso aprovadas; não recriar logos.
5. **Shitsuke — Disciplina:** aplicar rotinas proporcionais ao risco, registrar exceções, acompanhar indicadores úteis e melhorar continuamente.

## Critérios de decisão
- Reutilizar o que já existe antes de adotar ferramenta ou processo novo.
- Toda etapa deve possuir finalidade e benefício explícitos.
- Simplificar quando o custo do controle superar o risco mitigado, **sem flexibilizar requisitos legais, segurança ou aprovações obrigatórias**.
- Evitar documentos, checklists e cerimônias duplicados.
- Simplificar experiência do cliente, preservando robustez dos controles internos.

## Aplicação aos agentes e artefatos
Executor: utilizar modelos e fontes oficiais; registrar entregas de forma organizada.
Validador: observar redundâncias e complexidade injustificada no parecer contextual do [[00-Constituicao/Quality-Gates/QG-001-Politica|QG-001]], sem criar cinco gates extras ou reprovar automaticamente conteúdo extenso.
Auditor: avaliar amostras de desperdícios, inconsistências e exceções, sem atuar como autocertificador.

## Engenharia e documentação

O 5S também orienta a construção do produto e do próprio sistema:

- **Clareza:** nomes, contratos, interfaces e decisões devem ser compreensíveis sem explicações paralelas.
- **Objetividade:** cada componente, regra, documento e etapa deve ter finalidade identificável.
- **Simplicidade:** escolher a menor solução que satisfaça os requisitos, sem camadas, abstrações, agentes ou dependências desnecessárias.
- **Robustez:** simplicidade não significa fragilidade; preservar segurança, tratamento de falhas, testes, observabilidade e recuperação.
- **Eficácia:** medir o resultado e remover trabalho que não melhora qualidade, confiabilidade ou valor entregue.
- **Documentação:** uma fonte canônica por assunto; texto curto, direto e suficiente para construir, operar e manter. Evitar duplicação, burocracia e documentação que apenas repete código ou outra fonte.

A qualidade esperada é de alto nível de engenharia com o mínimo de complexidade necessária — não o mínimo de controles. Controles devem ser proporcionais ao risco e nunca removidos quando forem essenciais à segurança, integridade ou conformidade.

## Implementação enxuta
Revisar durante os processos e retrospectivas já existentes; **não criar cerimônia exclusiva do 5S**. Priorizar uma única fonte canônica por regra e versionamento pelo GitHub.

Relacionado: [[01-Empresa/Missao-Visao-Valores]] · [[03-Processos/GenTests-Quality-Framework]] · [[01-Empresa/Registro-de-Ativos-de-Marca]]


## Convenção mínima de nomes e rastreabilidade (proposta)

**Para novos artefatos formais:** `ID-Titulo-curto_vX.Y.ext` quando forem arquivos exportados; para notas do Obsidian, manter o nome legível e o `id` estável no YAML. Exemplo ilustrativo: `COM-001-Visibilidade-Comercial_v1.1.pdf`.

- Identificadores são únicos, estáveis e vinculados à origem; **não renumerar arquivos existentes**.
- Preferir hífen entre palavras, sem acentos, espaços ou nomes de pessoas em arquivos técnicos/exportados; manter a extensão correta.
- **Não inserir RNC, data nem estado no nome por padrão**: relacionar RNCs, status, data, autoria e versão completa via YAML ou registro de evidências. Incluir data apenas quando distinguir instantâneos entregues fizer sentido.
- A fonte editável é canônica; PDF é exportação. Versões históricas permanecem recuperáveis por Git ou arquivo histórico, sem cópias concorrentes de “final”, “final2”, “agora-vai”.
- Para entregas externas, manter número da versão no arquivo exportado e identificação do documento no conteúdo. Publicar somente a versão aprovada.
- O X9 pode sinalizar nomes fora do padrão em **novos arquivos**, mas não renomear nem reprovar legado automaticamente. Aplicação prospectiva, proporcional ao risco.

**Princípio:** só criar novo código quando houver artefato de negócio que precise de rastreabilidade; não numerar cada rascunho nem cada mensagem.

## Aprovação
**Proposta:** somente a direção poderá aprovar e registrar versão, data e decisão. A publicação no repositório não equivale a aprovação.
