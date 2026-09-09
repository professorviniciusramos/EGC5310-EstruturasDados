# EGC5310 — Estruturas de Dados

## Semana 05 — Revisão e registro pós-aula

**Tema:** hashing, conjuntos, dicionários e estruturas associativas  
**Versão:** 1.0  
**Status:** síntese pré-aula e instrumento para preenchimento posterior

## 1. Síntese da proposta

Narrativa:

> lista ordenada → custo de manutenção → chave como localização → tabela inicial → colisão → encadeamento → `dict` → `set` → escolha → complexidade → pergunta experimental

Pergunta central:

> **Como localizar uma matrícula rapidamente sem depender da posição do registro na coleção?**

## 2. Objetivos essenciais

- distinguir chave e posição;
- explicar função hash e colisão;
- completar inserção e busca com encadeamento;
- usar `dict` para associação e `set` para pertencimento;
- escolher estruturas pela operação predominante;
- interpretar `O(1)` como comportamento médio/esperado sob condições adequadas;
- preparar a comparação experimental da S06.

## 3. Conceitos-chave

| Conceito | Formulação curta |
|---|---|
| chave | informação do domínio usada para identificar/acessar |
| função hash | transforma chave em localização possível |
| colisão | chaves distintas indicam a mesma posição |
| bucket | coleção de itens associados a uma posição |
| `dict` | associação chave → valor |
| `set` | elementos únicos e pertencimento |
| `O(1)` médio | crescimento esperado aproximadamente constante, não um passo literal |

## 4. Atividades planejadas

1. prever posições;
2. provocar e explicar colisão;
3. implementar inserção e busca por encadeamento;
4. construir e consultar `dict`;
5. detectar duplicatas com `set`;
6. escolher estruturas e justificar;
7. corrigir uma interpretação equivocada de `O(1)`.

## 5. Decisões pedagógicas

- Introduzir o problema antes dos nomes das estruturas.
- Manter código curto e visível no Mestre.
- Descobrir colisão pela falha da implementação ingênua.
- Introduzir `dict` somente depois da tabela didática.
- Introduzir `set` por necessidade de unicidade.
- Exigir previsão antes da execução.
- Não realizar benchmark formal; formular seu desenho para a S06.
- Usar VisuAlgo apenas como reforço opcional posterior à implementação.

## 6. Pontos de atenção antes da aula

- Testar o link do Colab no segundo slide.
- Confirmar que os estudantes não executam antes da previsão nas Atividades 1 e 2.
- Explicar `%` e a criação de buckets se houver hesitação.
- Não permitir que “o programa rodou” encerre a análise da sobrescrita.
- Diferenciar ordem de inserção do `dict` e ordenação por chave.
- Repetir “médio/esperado” sempre que `O(1)` for mencionado.
- Preservar pelo menos cinco minutos para a ponte experimental.

## 7. Relação com a Semana 06

A S05 encerra com uma hipótese, não com um resultado experimental. A S06 deverá comparar busca sequencial, busca binária e `dict`, separando custos de preparação e consulta, controlando tamanho, cenário de busca, repetições e ruído.

---

# Evidências pós-aula

Preencher somente com fatos observados. Usar “não observado” quando aplicável.

## 8. O que funcionou

> Preencher após a aula.

## 9. O que não funcionou

> Preencher após a aula.

## 10. Dificuldades dos estudantes

- Chave × posição:
- Operador `%`:
- Colisões:
- Buckets e laços:
- `dict` × `set`:
- Complexidade média/esperada:

> Preencher após a aula.

## 11. Participação e atividades

| Atividade | Concluída? | Evidência de aprendizagem | Ajuste necessário |
|---|---|---|---|
| 1. Prever posições |  |  |  |
| 2. Provocar colisão |  |  |  |
| 3. Inserir e buscar |  |  |  |
| 4. Construir `dict` |  |  |  |
| 5. Usar `set` |  |  |  |
| 6. Escolher estrutura |  |  |  |
| 7. Interpretar `O(1)` |  |  |  |

## 12. Tempo real

- Ponto de término do primeiro encontro:
- Ponto de retomada do segundo encontro:
- Movimento que excedeu o previsto:
- Movimento reduzido/retirado:
- Tempo disponível para síntese:

## 13. Problemas técnicos

- Notebook Mestre/HTML:
- Notebook Estudante/Colab:
- Logo e CSS:
- Código/saídas:
- Links/VisuAlgo:

> Preencher após a aula.

## 14. Concepções equivocadas observadas

> Registrar frases ou produções concretas dos estudantes.

## 15. Alterações para futuras ofertas

### Manter

> Preencher.

### Modificar

> Preencher.

### Retirar

> Preencher.

### Retomar

> Preencher.

## 16. Evidências e decisões para a S06

- Hipóteses formuladas pela turma:
- Estratégias que precisam ser retomadas:
- Controles experimentais compreendidos:
- Riscos para o benchmark:
- Decisão principal para a S06:

> Preencher após a aula.

