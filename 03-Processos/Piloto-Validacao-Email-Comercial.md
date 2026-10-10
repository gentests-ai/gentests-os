---
tipo: processo
id: PILOTO-VAL-001
status: proposta
versao: 0.1.0
---
# Piloto: validação de email comercial

## Objetivo
Demonstrar QG-M em um e-mail **fictício**, sem destinatário real e sem envio.

## Fluxo
1. Comercial produz rascunho e registra origem de todas as afirmações.
2. AGT-VAL recebe o conteúdo, sua finalidade, destinatário (quando aplicável), versão e fontes.
3. AGT-VAL aplica [[07-Templates/Checklists/Comercial-Email]] e [[00-Constituicao/Quality-Gates/QG-CORE-Obrigatorio]].
4. Um verificador determinístico pode identificar lacunas de campos do registro e termos de alegações não comprovadas, mas **não pode afirmar alinhamento estratégico por conta própria**.
5. Se houver falhas, retornar ao Comercial para correção. Se conforme, solicitar aprovação humana quando necessário.
6. Só depois de autorização explícita o envio poderá ser realizado em outro fluxo com permissões específicas; registrar evidência real do envio.

## Critérios de aceite do piloto
- [ ] Cenário válido com fontes e sem envio.
- [ ] Cenário sem fonte obrigatória é bloqueado.
- [ ] Cenário com afirmação quantitativa sem evidência é sinalizado.
- [ ] Nunca confundir parecer automatizado com aprovação da direção.
- [ ] Resultado e limitações ficam auditáveis.

## Limitações
Este piloto é **uma verificação de campos e alegações**, não um agente autônomo nem um classificador de conteúdo por IA. A conformidade semântica será realizada em revisão independente futura.
