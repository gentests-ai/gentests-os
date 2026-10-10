# GT-MKT-CNQ-008 — Matriz de fechamento residual v0.4.2

Data: 2026-10-10. Complemento técnico focal ao relatório do commit `94d8d099544e49d15819f8156cdf40189076ee94`, conforme [REV-MKT-CNQ-008 / PR #32](https://github.com/gentestsai-sudo/gentests-os/pull/32). PDF v0.4.2 originalmente entregue no commit `17c9f8bf645fe75aaba083bad0be8c96440575f8`; nesta rodada, PDF, manifesto e PNGs recuperados do commit residual acima via conector GitHub, base64 decodificado sem regenerar o PDF. **Não constitui autorização para distribuição.**

| Verificação | Resultado nesta rodada | Evidência efetiva | Limite / risco |
|---|---|---|---|
| SHA-256 independente | **VERIFICADO — coincide com manifesto** | Python hashlib e GNU sha256sum produziram `44a2cae3dcb8706fb0674b8140a6e8a29edd9688bc6782c9f945dfdcf277b60e`; 67.317 bytes; identidade Git blob `b254e8e615299d1435a31f6dc1fe8285cf32dc7f` confirmada por SHA-1 do cabeçalho Git + bytes | Divergência anterior em JavaScript não reproduzida pelas duas implementações verificadas. Não há evidência de corrupção do binário. Código da implementação JavaScript anterior não disponível nesta execução: causa específica daquele resultado não determinada |
| Visual página 1 | **VERIFICADO — sem defeito observado** | Inspeção direta de [page-1.png](page-1.png), 1240 × 1755: título, subtítulo, blocos, lista, cabeçalho e rodapé legíveis e separados; margens preservadas | Inspeção visual pelo executor, não parecer independente nem experiência móvel |
| Visual página 2 | **VERIFICADO — sem defeito observado** | Inspeção direta de [page-2.png](page-2.png): três blocos completos, títulos consistentes, texto sem cortes ou sobreposições, rodapé separado | Mesmo limite |
| Visual página 3 | **VERIFICADO — sem defeito observado** | Inspeção direta de [page-3.png](page-3.png): rótulos, horas e valores em colunas distintas e legíveis; total e ressalvas completos; sem colisões | Apenas apresentação visual; cálculos e conteúdo financeiro não reavaliados |
| Visual página 5 | **VERIFICADO — sem defeito observado** | Inspeção direta de [page-5.png](page-5.png): CTA, URL, fontes e limitações legíveis e completos; sem cortes, sobreposições ou invasão do rodapé | Aparência da URL não prova clique nem acessibilidade |
| Página 4 | **APROVADO anteriormente, sem nova inspeção** | REV-MKT-CNQ-008 validou numeração 1–7 | Não recuperada como imagem, não renderizada e não reaberta nesta rodada |
| Clique real no link página 5 | **NÃO EXECUTADO** | Sem ambiente utilizável nesta sessão para abrir o binário exato em interface de leitor PDF e clicar na URL | Ferramentas de conector/API e renderização não são interface de leitor. Restrição anterior de file:// já documentada. Nenhuma nova tentativa de clique; não substituir por anotação/API, HTTP ou simulação |
| Acessibilidade assistiva | **NÃO EXECUTADO** | Nenhum leitor de tela operacional disponível nesta sessão | Ordem real, títulos, listas, tabelas e navegação continuam pendentes. Estrutura declarada não equivale a PDF/UA; atenção às tabelas com TD sem TH já documentadas |
| Dispositivo móvel físico | **NÃO EXECUTADO** | Nenhum telefone físico acessível ao executor | Simulações anteriores não usadas como comprovação; experiência real de zoom/pan e leitura permanece pendente |

## Integridade: procedimento e resultados verificáveis

Ambiente: Python 3.12.14; GNU coreutils sha256sum 9.4; Poppler pdftoppm 26.05.0. Arquivo local analisado: cópia binária exata obtida de `comercial/GT-MKT-CNQ-001-Guia-Executivo-v0.4.2.pdf` no commit residual. Não se usou PDF regenerado para o hash.

Antes do cálculo do PDF, as duas implementações passaram, separadamente, nos três vetores fixos:

| Entrada ASCII, sem quebra de linha | SHA-256 esperado e obtido em ambas | Resultado |
|---|---|---|
| String vazia (0 bytes) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | PASS |
| `abc` | `ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad` | PASS |
| `abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq` | `248d6a61d20638b8e5c026930c3e6039a33ce45964ff2167f6ecedd419db06c1` | PASS |

Saída efetiva sobre o PDF:

```text
Python hashlib: bytes=67317
Python hashlib SHA-256: 44a2cae3dcb8706fb0674b8140a6e8a29edd9688bc6782c9f945dfdcf277b60e
GNU sha256sum:          44a2cae3dcb8706fb0674b8140a6e8a29edd9688bc6782c9f945dfdcf277b60e
Git blob SHA-1:         b254e8e615299d1435a31f6dc1fe8285cf32dc7f
```

Reprodução em checkout que contenha o mesmo PDF, sem execução do gerador:

```bash
python3 - <<'PY'
from pathlib import Path
import hashlib, subprocess
vectors = [
    (b'', 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'),
    (b'abc', 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'),
    (b'abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq',
     '248d6a61d20638b8e5c026930c3e6039a33ce45964ff2167f6ecedd419db06c1'),
]
for data, expected in vectors:
    actual = hashlib.sha256(data).hexdigest()
    second = subprocess.run(['sha256sum'], input=data, capture_output=True,
                            check=True).stdout.decode().split()[0]
    assert actual == second == expected
    print('PASS', repr(data), actual)
p = Path('comercial/GT-MKT-CNQ-001-Guia-Executivo-v0.4.2.pdf')
b = p.read_bytes()
print('bytes', len(b))
print('hashlib', hashlib.sha256(b).hexdigest())
print('Git blob', hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest())
print(subprocess.check_output(['sha256sum', str(p)]).decode())
assert len(b) == 67317
assert hashlib.sha256(b).hexdigest() == '44a2cae3dcb8706fb0674b8140a6e8a29edd9688bc6782c9f945dfdcf277b60e'
assert hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest() == 'b254e8e615299d1435a31f6dc1fe8285cf32dc7f'
PY
```

## Vinculação das imagens ao binário

Cada PNG recuperado foi conferido contra o manifesto. Em seguida, renderização nova do PDF exato, somente páginas 1, 2, 3 e 5, com `pdftoppm -f N -l N -r 150 -png arquivo.pdf prefixo`, produziu PNGs **byte a byte idênticos** aos recuperados. Portanto, as imagens efetivamente inspecionadas correspondem ao binário cujo hash foi confirmado.

| PNG | Bytes | SHA-256 recuperado e reproduzido |
|---|---:|---|
| page-1.png | 155478 | `ee339c9abf0b0686f4d2a0cb6424c9f18f8bf10254ae057ac3ebcee860514e76` |
| page-2.png | 161823 | `c1663b9c28c9bc67ae7caa18e59c55a81c8f8191dfa5e66b5be74ddf54a46a72` |
| page-3.png | 164216 | `4e147c54176c4dca0cf8513ee80e4c1b89e81b7cb4ea7bfafc5bf2efe1456112` |
| page-5.png | 206758 | `3f5bea1de37b58eb77437376cbccb3f3ea6c50c75003d8a6dab3f60f5309277b` |

Consistência observada nas quatro imagens: mesma paleta azul-marinho/teal, hierarquia de títulos, alinhamento à esquerda, separadores e padrão de cabeçalho/rodapé. Nenhum defeito material demonstrado nesta rodada; nenhum conteúdo ou binário alterado e nenhuma nova versão de produto criada.

## Recomendação à Direção

**Manter PR #4 aberta e Draft, sem autorização para distribuição.** Submeter à revalidação independente exclusivamente os novos resultados de integridade e inspeção visual das páginas 1, 2, 3 e 5, incluindo a vinculação dos PNGs ao PDF. Clique real, leitura assistiva e dispositivo físico permanecem NÃO EXECUTADOS e não podem ser encerrados por inferência. A Direção deve decidir os próximos ambientes de teste e o tratamento das limitações antes de qualquer autorização comercial. HTML semântico permanece apenas alternativa já proposta, sem implementação.

Não reabrir página 4, ciência, cálculos, conteúdo aprovado ou auditoria integral. Sem merge, publicação, campanha, captação ou alteração em site, CRM, preços, contratos e políticas.
