# EGC5310 — Estruturas de Dados
## Semana 03 — Exercícios

**Arquivo:** `EGC5310-EstruturasDados-S03-06-Exercicios.md`

Os exercícios desta semana aprofundam os conceitos trabalhados em aula. O objetivo não é apenas obter uma resposta correta, mas justificar o comportamento das operações e relacionar código, mecanismo e complexidade.

---

## Exercício 1 — Mesma quantidade de linhas, trabalhos diferentes

Considere:

```python
lista.append(x)
```

e:

```python
lista.insert(0, x)
```

Responda:

1. Por que as duas instruções não devem ser consideradas equivalentes em termos de trabalho?
2. Qual delas tende a depender do tamanho atual da lista?
3. Qual mecanismo estrutural explica essa diferença?
4. Qual classificação assintótica é esperada para cada uma?

---

## Exercício 2 — Remoção e posição

Considere:

```python
lista.pop()
```

e:

```python
lista.pop(0)
```

Suponha uma lista com `n` elementos.

1. O que acontece estruturalmente em cada operação?
2. Qual delas tende a exigir deslocamento de elementos?
3. Classifique cada operação em Big-O.
4. Explique por que remover um elemento de uma lista não possui um único custo independente da posição.

---

## Exercício 3 — Preencha a tabela

Complete:

| Operação | Comportamento esperado | Justificativa |
|---|---|---|
| `lista[i]` | | |
| `lista.append(x)` | | |
| `lista.insert(0, x)` | | |
| `lista.pop()` | | |
| `lista.pop(0)` | | |
| `x in lista` | | |
| `lista.sort()` | | |

Para `lista.sort()`, utilize o comportamento típico de uma ordenação eficiente.

---

## Exercício 4 — O que significa custo amortizado?

Explique, com suas palavras, por que `append()` pode ser considerado `O(1)` amortizado mesmo que algumas inserções eventualmente precisem realizar mais trabalho.

Não é necessário apresentar uma demonstração matemática.

Sua explicação deve mencionar:

- capacidade;
- realocação;
- sequência de operações.

---

## Exercício 5 — Inserir e ordenar

Considere:

```python
ranking = []

for aluno in novos_alunos:
    ranking.append(aluno)
    ranking.sort(key=lambda x: x["nota"], reverse=True)
```

e:

```python
ranking = []

for aluno in novos_alunos:
    ranking.append(aluno)

ranking.sort(key=lambda x: x["nota"], reverse=True)
```

Responda:

1. As duas soluções podem produzir o mesmo resultado final?
2. Qual delas realiza mais ordenações?
3. Por que a diferença entre as estratégias tende a crescer com a quantidade de alunos?
4. Qual princípio geral sobre sequência de operações esse exemplo ilustra?

---

## Exercício 6 — Reescrevendo `lambda`

Considere:

```python
ranking.sort(
    key=lambda aluno: aluno["nota"],
    reverse=True
)
```

Reescreva o código utilizando uma função nomeada com `def`.

Depois explique:

1. qual valor a função recebe;
2. qual valor ela devolve;
3. para que o parâmetro `key` é utilizado;
4. o que `reverse=True` altera.

---

## Exercício 7 — Mesmo Big-O, tempos diferentes

Considere:

```python
for aluno in alunos:
    aluno["nota"] += 1
```

e:

```python
df["nota"] += 1
```

Em um modelo simplificado, ambas as operações processam `n` valores e podem ser classificadas como `O(n)`.

Explique por que o tempo de execução pode ser muito diferente.

Sua resposta deve discutir pelo menos três dos seguintes elementos:

- overhead do interpretador Python;
- código compilado;
- vetorização;
- representação de memória;
- constantes ocultas pela notação Big-O.

---

## Exercício 8 — DataFrame incremental

Considere:

```python
df = pd.DataFrame()

for registro in registros:
    novo = pd.DataFrame([registro])
    df = pd.concat([df, novo], ignore_index=True)
```

Responda:

1. Por que essa estratégia pode ser ineficiente?
2. Que trabalho pode estar sendo repetido?
3. Por que a sequência `1 + 2 + 3 + ... + n` é relevante para compreender esse padrão?
4. Que classe de crescimento essa soma sugere?
5. Apresente uma alternativa de construção em lote.

---

## Exercício 9 — List ou DataFrame?

Para cada situação abaixo, indique qual representação parece mais adequada inicialmente: `list` ou `DataFrame`. Justifique cada resposta.

### a)
Receber estudantes um a um durante uma simulação e armazená-los temporariamente.

### b)
Calcular média de nota por curso para 500 mil estudantes.

### c)
Filtrar todos os estudantes com nota maior que 8.

### d)
Executar várias agregações por curso, semestre e turma.

### e)
Manter uma coleção heterogênea de objetos Python que não possui estrutura tabular regular.

Observação: se houver mais de uma alternativa plausível, explique o contexto.

---

## Exercício 10 — JSON não é DataFrame

Considere:

```json
[
  {"matricula": 101, "nome": "Ana"},
  {"matricula": 102, "nome": "Bruno"}
]
```

Responda:

1. Qual é o papel principal do JSON?
2. O que `json.loads()` normalmente produz em Python nesse exemplo?
3. Em que momento as operações passam a ocorrer sobre `list` e `dict`?
4. Por que a pergunta “qual é o Big-O do JSON?” é incompleta?
5. Que tipo de operação envolvendo JSON pode ser analisada em termos de complexidade?

---

## Exercício 11 — Parsing de JSON

Suponha um documento JSON textual com tamanho `m`.

Explique por que, em um modelo introdutório, interpretar completamente o documento pode ser considerado aproximadamente `O(m)`.

Sua resposta deve deixar claro qual é o significado de `m`.

---

## Exercício 12 — Pipeline de dados

Considere:

```text
API
 ↓
JSON
 ↓
list / dict
 ↓
DataFrame
 ↓
JSON
 ↓
outro sistema
```

Para cada transição, indique o que está acontecendo:

1. JSON → `list` / `dict`
2. `list` / `dict` → `DataFrame`
3. `DataFrame` → JSON

Use os termos:

- serialização;
- desserialização;
- representação em memória;
- processamento tabular.

---

## Exercício 13 — Interpretando benchmark

Um benchmark produziu:

| n | Estratégia A | Estratégia B |
|---:|---:|---:|
| 100 | 0,002 s | 0,001 s |
| 1.000 | 0,020 s | 0,003 s |
| 10.000 | 0,220 s | 0,010 s |

Responda:

1. É suficiente dizer que “B é mais rápida”?
2. O que deve ser observado na evolução da diferença entre A e B?
3. Esses valores, sozinhos, permitem provar a classe Big-O?
4. Que tipo de conclusão é apropriada a partir do benchmark?
5. Que fatores do ambiente podem alterar os valores medidos?

---

## Exercício 14 — Escolha baseada em operação predominante

Um sistema recebe dados de estudantes e realiza aproximadamente:

- 10 milhões de consultas por matrícula;
- 2 mil inserções por dia;
- 500 remoções por dia;
- uma ordenação completa por semana.

Responda:

1. Qual operação parece dominar a carga de trabalho?
2. Por que essa informação é mais importante do que simplesmente perguntar “qual estrutura é melhor”?
3. Que preocupação esse cenário prepara para a Semana 04?

Não é necessário propor ainda a estrutura definitiva.

---

## Exercício 15 — Investigação prática

Implemente um pequeno experimento que compare:

```python
lista.append(x)
```

com:

```python
lista.insert(0, x)
```

para pelo menos quatro valores diferentes de `n`.

Requisitos:

1. repetir cada medição pelo menos cinco vezes;
2. utilizar mediana ou média;
3. registrar os resultados em uma tabela;
4. produzir um gráfico;
5. escrever uma interpretação de até 10 linhas.

Sua interpretação deve responder:

- a diferença cresce com `n`?
- os resultados confirmam a hipótese?
- por que tempo medido e Big-O não são a mesma coisa?

---

## Exercício 16 — Desafio: reorganizando o trabalho

Considere um conjunto de `n` novos estudantes que precisam ser adicionados a um ranking.

Proponha duas estratégias:

1. uma estratégia que ordene repetidamente;
2. uma estratégia que reduza o número de ordenações.

Depois:

1. implemente as duas;
2. execute para pelo menos três valores de `n`;
3. compare os tempos;
4. explique qual trabalho foi evitado na segunda estratégia.

Não é necessário derivar formalmente a complexidade completa da solução.

---

# Questão de síntese

Responda em um parágrafo:

> **Por que “qual estrutura é mais rápida?” geralmente é uma pergunta mal formulada?**

Sua resposta deve utilizar os conceitos:

- operação;
- representação;
- tamanho da entrada;
- sequência de operações;
- complexidade;
- tempo medido.
