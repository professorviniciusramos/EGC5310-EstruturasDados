# EGC5310 — Estruturas de Dados
## Semana 03 — Benchmark

**Arquivos associados**
- `EGC5310-EstruturasDados-S03-05-Benchmark.py`
- `EGC5310-EstruturasDados-S03-05-Benchmark.csv`

## 1. Objetivo

Produzir evidências empíricas para três ideias da Semana 03:

1. a posição da inserção em uma `list` afeta o trabalho;
2. a posição da remoção em uma `list` afeta o trabalho;
3. construir um `DataFrame` registro a registro pode ser muito menos eficiente do que construí-lo em lote.

O benchmark não substitui a análise de complexidade. Ele confronta hipóteses com medições.

## 2. Método

As medições usam `time.perf_counter()` e a **mediana** de várias repetições.

Tamanhos:

- listas: `1.000`, `10.000`, `100.000`, `500.000`;
- DataFrame: `100`, `500`, `1.000`, `2.000`.

Nas operações de lista, cada repetição parte de uma cópia da mesma lista-base. Isso mantém condições comparáveis, mas significa que os tempos absolutos incluem também o custo dessa cópia. Por isso, o foco é a **tendência relativa**, não o tempo puro de uma única operação.

## 3. Resultados desta execução

### Inserção em lista

|      n |     append |   insert_inicio |
|-------:|-----------:|----------------:|
|   1000 | 0.00000253 |      0.00000244 |
|  10000 | 0.00001570 |      0.00001693 |
| 100000 | 0.00015467 |      0.00016463 |
| 500000 | 0.00203856 |      0.00201290 |

### Remoção em lista

|      n |   pop_final |   pop_inicio |
|-------:|------------:|-------------:|
|   1000 |  0.00000162 |   0.00000170 |
|  10000 |  0.00001402 |   0.00001499 |
| 100000 |  0.00014210 |   0.00015192 |
| 500000 |  0.00108921 |   0.00118258 |

### Construção de DataFrame

|    n |   incremental |       lote |
|-----:|--------------:|-----------:|
|  100 |    0.01650258 | 0.00010641 |
|  500 |    0.08237211 | 0.00029567 |
| 1000 |    0.19567842 | 0.00044686 |
| 2000 |    0.36439699 | 0.00077849 |

Razão `incremental / lote`:

|    n |   razão |
|-----:|--------:|
|  100 |   155.1 |
|  500 |   278.6 |
| 1000 |   437.9 |
| 2000 |   468.1 |

## 4. Interpretação didática

### 4.1 `append()` × `insert(0, ...)`

`insert(0, ...)` tende a apresentar crescimento adicional porque pode exigir deslocamento de referências. `append()` permanece associado a custo `O(1)` amortizado.

Como a preparação do experimento copia a lista para cada repetição, o benchmark não deve ser usado para estimar o tempo absoluto de `append()`. Ele é apropriado para discutir como os comportamentos divergem quando `n` cresce.

### 4.2 `pop()` × `pop(0)`

`pop(0)` pode exigir deslocamento dos elementos restantes. `pop()` remove do final e não precisa realizar esse deslocamento.

### 4.3 DataFrame incremental × lote

Este é o contraste mais forte da semana.

Na estratégia incremental, o programa cria pequenos DataFrames e realiza concatenações sucessivas. A estrutura manipulada cresce a cada iteração.

Na estratégia em lote, os registros são entregues juntos para a construção tabular.

O experimento ilustra por que **processamento em lote** é importante em Ciência de Dados e por que uma API conveniente não elimina o custo das operações realizadas por baixo.

Isso não significa que “DataFrame é pior que list”. Significa apenas que **DataFrame não é uma boa escolha para esse padrão específico de reconstrução registro a registro**.

## 5. Relação com Big-O

Modelos discutidos na semana:

- `list.append()` → `O(1)` amortizado;
- `list.insert(0, x)` → `O(n)`;
- `list.pop()` → `O(1)`;
- `list.pop(0)` → `O(n)`;
- concatenações sucessivas de estruturas crescentes podem produzir trabalho acumulado próximo de `O(n²)`;
- processamento em lote evita repetir parte desse trabalho.

Big-O descreve **como o trabalho cresce**. O benchmark mede tempo concreto numa implementação e ambiente específicos.

## 6. Ambiente desta execução

- Python: `3.13.5`
- pandas: `2.2.3`
- sistema: `Linux`

Os valores do CSV não são constantes universais. Em outra máquina os números podem mudar, mas espera-se preservar as tendências principais.

## 7. Uso em sala

Sequência recomendada:

1. formular hipóteses;
2. executar o Notebook Estudante;
3. observar tabelas e gráficos;
4. comparar com o benchmark oficial;
5. explicar os mecanismos;
6. formalizar a classe de crescimento.

Pergunta de fechamento:

> **Como a diferença mudou quando `n` aumentou, e qual mecanismo explica essa tendência?**
