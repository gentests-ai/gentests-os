---
id: REV-PROD-CNB-002
tipo: parecer-independente-revalidacao-focal
versao: 0.1.0
status: emitido
data: 2026-10-10
objeto: GT-PROD-CNB-001-v0.1.1
pr_execucao: 28
commit_revisado: 8df9e2f16019be3095ca7ab2bfe69c2ca94d6d8c
parecer_anterior: REV-PROD-CNB-001
resultado: apto-encerramento-documental
aprovacao_direcao: pendente
implementacao_autorizada: nao
publicacao_autorizada: nao
merge_autorizado: nao
---
# REV-PROD-CNB-002 — Revalidação focal de fechamento da Calculadora CNQ v0.1.1

**DECISÃO: APTO PARA ENCERRAMENTO DOCUMENTAL, condicionado ao aceite da Direção.** Não autoriza implementação, testes operacionais, publicação, e-mail, captação, merge ou homologação técnica.

## Objeto e limites
Revalidação independente apenas de CNB-REV-01, CNB-REV-02 e CNB-REV-03 do REV-PROD-CNB-001 (PR #30), na PR #28, commit exato `8df9e2f16019be3095ca7ab2bfe69c2ca94d6d8c`. Conferidos `Especificacao-Funcional.md`, `Interface-Jornada.md`, `Arquitetura-Tecnica.md`, `Aceite-Testes.md` v0.1.1 e preservação conceitual dos 34 CA originais; README e backlog permanecem baseline v0.1.0. PR #28 foi confirmada aberta, Draft e não merged. Sem execução de calculadora, scripts, e-mail, navegador ou serviços; cenário especificado não é teste aprovado.

## Matriz de revalidação focal
| ID e gravidade original | Resultado | Evidências concretas | Residual futuro |
|---|---|---|---|
| **CNB-REV-01 — Média** | **RESOLVIDO DOCUMENTALMENTE** | FUN IN-10, RN-09a e RN-09/10: comparação por natureza E/A/O versus R, valor, origem e relação; ausência de checkbox global; refs locais diferentes não equivalem a conciliação; desconhecido/sobreposto excluído; edição invalida confirmação. UX §1 mostra rubricas simultaneamente; QA **CF-01–03** cobrem refs diferentes sem prova, sobreposição, incrementos e edição | Confirmação permanece declaratória, sem prova financeira externa; validar UX e exclusões em produto construído. |
| **CNB-REV-02 — Média** | **RESOLVIDO DOCUMENTALMENTE** | FUN RF-04, TEC §3 e UX EMAIL-03: snapshot imutável com versões/metodologia, canonicalização/hashing SHA-256 e request_id; impressão e e-mail ligados ao snapshot original; idempotência por envelope/ID, conflito 409, edição não altera pedido; timeout com estado inconclusivo e sem retry cego. QA **CF-04–07** testa edição durante impressão/envio, novo snapshot, timeout e payload alterado | Hash não é assinatura; persistência, fornecedor, retenção e prova de entrega ainda não aprovados. E-mail deve continuar desligado se idempotência/reconciliação não puder ser implementada. |
| **CNB-REV-03 — Baixa** | **RESOLVIDO DOCUMENTALMENTE** | FUN IN-13, UX §1: até 744h = 31 dias é limite operacional de contexto, não máximo real; acima rejeitar sem truncar, sem monetização automática e sem bloquear outras parcelas válidas. QA **CF-08** trata 744h e 744,01h | Validar visualização do aviso e tratamento de erro na futura UI. |

## Preservação e regressões
- Os **34 critérios CA-01–34** continuam especificados; CF-01–08 são **oito cenários complementares** e não alteram o total de critérios originais. Não há evidências de execução ou resultados de testes.
- Fórmulas gerenciais preservadas: `R=sum(horas únicas × custo-hora)`, `T=R+E+A+O`, `M=T×N`, `Y=M×12`, sem transmutação de subtotal em prejuízo/caixa ou ROI. Vetor canônico histórico R$ 2.260/R$ 4.760/R$ 14.280/R$ 171.360 mantido.
- A especificação v0.1.1 é um delta focal em quatro arquivos; não há alteração do escopo offline sem cadastro ou ativação de e-mail.
- **Nenhuma regressão material encontrada no delta documental.**

## Pendências não impeditivas para encerrar documento
A Direção ainda deve deliberar orçamento/capacidade e prioridade das primeiras vendas, limites e regras metodológicas, existência/fase de envio, controlador e bases LGPD, retenção, segurança do provedor e eventual autorização de PR técnica. O núcleo local/impresso é independente do backend opcional. Futuro teste deve verificar CF-01–08 e CA-01–34 na implementação real com evidências, incluindo acessibilidade e estados extremos. O uso de SHA-256 não garante origem/autenticidade e ids locais não comprovam ausência de duplicação; documentos afirmam expressamente esses limites.

## Conclusão
**Zero bloqueios materiais para encerrar a elaboração e revalidação documental** da proposta GT-PROD-CNB-001 v0.1.1. Recomendo ao Orquestrador registrar CNB-REV-01–03 fechados documentalmente e enviar à Direção decisão de aceite/encerramento. **Não abrir outra auditoria geral** salvo nova evidência alta/crítica. Encerramento documental não concede aprovação normativa, permissão de implementação, merge, lançamento, contato de leads nem execução de e-mail. 
