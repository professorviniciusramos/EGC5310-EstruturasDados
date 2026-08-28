# EGC5310 — Estruturas de Dados
## Semana 03 — Soluções comentadas

**Arquivo:** `EGC5310-EstruturasDados-S03-07-Solucoes.md`

Estas soluções são referências para discussão e correção. Em vários exercícios, mais de uma formulação pode ser considerada adequada se a justificativa relacionar corretamente **operação, representação, mecanismo e crescimento do trabalho**.

---

## Exercício 1 — Mesma quantidade de linhas, trabalhos diferentes

```python
lista.append(x)
lista.insert(0, x)
```

1. As duas instruções possuem tamanho semelhante no código, mas acionam mecanismos diferentes.
2. `insert(0, x)` tende a depender diretamente do número de elementos já armazenados.
3. Na inserção no início, as referências existentes podem precisar ser deslocadas para abrir a posição zero. No `append()`, normalmente existe espaço reservado ao final.
4. Em uma `list` Python:

   - `append(x)` → `O(1)` amortizado;
   - `insert(0, x)` → `O(n)`.

A palavra **amortizado** é importante: algumas chamadas de `append()` podem provocar crescimento da capacidade e custar mais, mas esse custo é distribuído ao longo de uma sequência de inserções.

---

## Exercício 2 — Remoção e posição

```python
lista.pop()
lista.pop(0)
```

1. `pop()` remove o último elemento. `pop(0)` remove o primeiro.
2. `pop(0)` pode exigir que os elementos seguintes sejam deslocados para preencher a posição liberada.
3. Em uma lista Python:

   - `pop()` → `O(1)`;
   - `pop(0)` → `O(n)`.

4. Portanto, “remover de uma lista” não define uma complexidade única. É necessário especificar **qual operação de remoção e em qual posição**.

---

## Exercício 3 — Tabela

| Operação | Comportamento esperado | Justificativa |
|---|---:|---|
| `lista[i]` | `O(1)` | acesso direto à posição |
| `lista.append(x)` | `O(1)` amortizado | inserção ao final com crescimento ocasional |
| `lista.insert(0, x)` | `O(n)` | pode deslocar os elementos existentes |
| `lista.pop()` | `O(1)` | remove o último elemento |
| `lista.pop(0)` | `O(n)` | pode deslocar os elementos restantes |
| `x in lista` | `O(n)` | no pior caso, precisa testar os elementos sequencialmente |
| `lista.sort()` | `O(n log n)` típico | ordenação eficiente; detalhes serão estudados posteriormente |

A tabela reforça que não existe “a complexidade da lista”: existem complexidades associadas às operações.

---

## Exercício 4 — Custo amortizado

Uma `list` Python mantém uma capacidade que pode ser maior que seu tamanho atual. Enquanto houver capacidade livre, adicionar um elemento ao final é uma operação muito barata.

Quando a capacidade disponível termina, a estrutura precisa crescer, o que pode envolver alocação de espaço adicional e transferência de referências. Essa chamada específica realiza mais trabalho.

Entretanto, o crescimento não ocorre em todo `append()`. Ao analisar uma longa **sequência de inserções**, o custo ocasional de crescimento é distribuído entre muitas operações baratas. Por isso, dizemos que:

`append()` → `O(1)` **amortizado**.

---

## Exercício 5 — Inserir e ordenar

As duas estratégias podem produzir o mesmo ranking final, desde que a única exigência seja que o resultado esteja ordenado depois que todos os novos alunos forem incorporados.

Na primeira:

```python
for aluno in novos_alunos:
    ranking.append(aluno)
    ranking.sort(key=lambda x: x["nota"], reverse=True)
```

a ordenação é executada depois de **cada inserção**.

Na segunda:

```python
for aluno in novos_alunos:
    ranking.append(aluno)

ranking.sort(key=lambda x: x["nota"], reverse=True)
```

as inserções são realizadas primeiro e a ordenação ocorre apenas uma vez.

À medida que o número de estudantes aumenta, repetir uma operação relativamente cara sobre coleções crescentes acumula trabalho desnecessário.

O princípio geral é:

> **A complexidade de um processo depende também da sequência e da frequência das operações.**

---

## Exercício 6 — Reescrevendo `lambda`

Uma solução equivalente é:

```python
def obter_nota(aluno):
    return aluno["nota"]

ranking.sort(
    key=obter_nota,
    reverse=True
)
```

1. `obter_nota` recebe um registro `aluno`.
2. Ela devolve o valor associado à chave `"nota"`.
3. `key` informa à ordenação qual valor deve ser extraído de cada elemento para realizar a comparação.
4. `reverse=True` solicita a ordenação em ordem decrescente.

Portanto:

```python
lambda aluno: aluno["nota"]
```

é uma forma compacta de expressar a mesma pequena função.

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

Em ambos os casos, `n` valores precisam ser processados. Em um modelo simplificado, portanto, ambos podem apresentar crescimento `O(n)`.

Isso não significa tempos iguais.

Uma representação possível é:

```text
Lista Python      T(n) ≈ a · n
DataFrame         T(n) ≈ b · n
```

Mesmo que ambos sejam lineares, `a` e `b` podem ser muito diferentes.

Entre os fatores estão:

- **overhead do interpretador:** um laço escrito diretamente em Python executa repetidamente operações no nível do interpretador;
- **código compilado:** várias operações de pandas/NumPy delegam trabalho para implementações compiladas;
- **vetorização:** uma operação é expressa sobre um conjunto de valores em vez de ser comandada elemento por elemento em Python;
- **representação de memória:** a organização dos dados influencia acesso e processamento;
- **constantes:** Big-O omite fatores constantes e detalhes que podem ser decisivos nos tamanhos encontrados na prática.

Conclusão:

> **Big-O descreve a taxa de crescimento; não é um cronômetro.**

---

## Exercício 8 — DataFrame incremental

O código:

```python
df = pd.DataFrame()

for registro in registros:
    novo = pd.DataFrame([registro])
    df = pd.concat([df, novo], ignore_index=True)
```

realiza repetidamente criação e concatenação de estruturas.

À medida que `df` cresce, cada nova concatenação pode precisar lidar com uma quantidade maior de dados. Em um modelo didático simplificado, o trabalho acumulado pode se comportar como:

```text
1 + 2 + 3 + ... + n
```

Como:

```text
1 + 2 + ... + n = n(n + 1) / 2
```

o termo dominante é proporcional a `n²`.

Assim, esse padrão pode produzir comportamento próximo de:

`O(n²)`.

Uma alternativa é construir em lote:

```python
df = pd.DataFrame(registros)
```

Ou, se já existe um DataFrame anterior:

```python
novos_df = pd.DataFrame(registros)

df = pd.concat(
    [df, novos_df],
    ignore_index=True
)
```

O objetivo não é concluir que DataFrames são lentos, mas perceber que **o padrão de uso da estrutura importa**.

---

## Exercício 9 — List ou DataFrame?

### a) Receber estudantes um a um

Uma `list` é uma escolha inicial bastante natural:

```python
alunos.append(novo_aluno)
```

Ela oferece crescimento incremental simples e `append()` com custo `O(1)` amortizado.

### b) Média por curso para 500 mil estudantes

Um `DataFrame` tende a ser mais conveniente:

```python
df.groupby("curso")["nota"].mean()
```

A estrutura e sua API são orientadas a operações tabulares e agregações.

### c) Filtrar estudantes com nota maior que 8

As duas representações permitem realizar a tarefa.

Lista:

```python
selecionados = [
    aluno for aluno in alunos
    if aluno["nota"] > 8
]
```

DataFrame:

```python
selecionados = df[df["nota"] > 8]
```

Se essa filtragem fizer parte de um fluxo analítico tabular, o DataFrame tende a ser mais natural. Para uma pequena coleção geral de objetos, uma lista pode ser suficiente.

### d) Várias agregações

`DataFrame` é uma escolha natural porque agregação, agrupamento, seleção e operações por coluna fazem parte diretamente da abstração.

### e) Coleção heterogênea sem estrutura tabular regular

Uma `list` tende a ser mais flexível.

A conclusão importante é:

> **A escolha depende das operações predominantes e da natureza dos dados.**

---

## Exercício 10 — JSON não é DataFrame

1. JSON é principalmente um **formato textual de representação e intercâmbio de dados**.
2. Neste exemplo:

```python
dados = json.loads(texto_json)
```

produz uma `list` contendo objetos `dict`.
3. Depois da desserialização, as operações em memória passam a ocorrer sobre essas estruturas Python.
4. “Qual é o Big-O do JSON?” é uma pergunta incompleta porque JSON não possui uma única operação cujo custo esteja sendo especificado.
5. Podemos analisar, por exemplo:

   - parsing/desserialização;
   - serialização;
   - leitura;
   - escrita;
   - operações realizadas depois da conversão para estruturas em memória.

---

## Exercício 11 — Parsing de JSON

Se `m` representa o tamanho da representação textual do documento — por exemplo, sua quantidade de caracteres/bytes em um modelo simplificado — interpretar completamente o documento exige examinar seu conteúdo para reconhecer objetos, listas, chaves, valores e delimitadores.

Assim, uma modelagem introdutória razoável é:

`parsing(m) ≈ O(m)`.

Isso não significa que todos os parsers tenham exatamente o mesmo tempo. Significa que, para interpretar integralmente um documento maior, a quantidade de conteúdo examinada cresce aproximadamente com seu tamanho.

---

## Exercício 12 — Pipeline de dados

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

### 1. JSON → `list` / `dict`

**Desserialização.**

A representação textual é interpretada e transformada em estruturas em memória.

Exemplo:

```python
dados = json.loads(texto_json)
```

### 2. `list` / `dict` → `DataFrame`

Mudança de representação em memória para uma estrutura orientada ao **processamento tabular**.

```python
df = pd.DataFrame(dados)
```

### 3. `DataFrame` → JSON

Os dados são convertidos novamente para uma representação adequada ao intercâmbio.

É uma forma de **serialização**.

O pipeline mostra que não precisamos escolher um único formato para todas as etapas.

---

## Exercício 13 — Interpretando benchmark

Resultados:

| n | Estratégia A | Estratégia B |
|---:|---:|---:|
| 100 | 0,002 s | 0,001 s |
| 1.000 | 0,020 s | 0,003 s |
| 10.000 | 0,220 s | 0,010 s |

1. Não é suficiente apenas afirmar que B foi mais rápida.
2. É importante observar **como os tempos e a diferença entre eles evoluem conforme `n` aumenta**.
3. Os valores não provam sozinhos uma classe Big-O. Big-O exige análise do algoritmo/mecanismo; o experimento fornece evidências compatíveis ou incompatíveis com uma hipótese.
4. Uma conclusão apropriada seria: “neste ambiente e para os tamanhos testados, B apresentou crescimento de tempo menor que A; o resultado é compatível com a hipótese formulada”.
5. Os valores podem mudar por hardware, versão do Python, bibliotecas, sistema operacional, carga da máquina, gerenciamento de memória e ruído experimental.

A análise mais importante é:

> **benchmark + mecanismo + modelo de crescimento**, e não benchmark isoladamente.

---

## Exercício 14 — Operação predominante

O sistema realiza:

- 10 milhões de consultas por matrícula;
- 2 mil inserções;
- 500 remoções;
- uma ordenação semanal.

A carga é claramente dominada pelas **consultas por matrícula**.

Isso muda a pergunta de projeto. Em vez de:

> “Qual estrutura é melhor?”

devemos perguntar:

> “Qual representação favorece a operação que executaremos milhões de vezes?”

Esse cenário prepara a Semana 04 porque, se cada consulta percorre sequencialmente uma coleção grande, pode ser interessante investigar se **organizar os dados** permite reduzir o trabalho de busca.

Não precisamos ainda decidir a solução.

---

## Exercício 15 — Investigação prática

Uma implementação possível:

```python
import time
import statistics
import pandas as pd
import matplotlib.pyplot as plt

def medir(funcao, repeticoes=7):
    tempos = []

    for _ in range(repeticoes):
        inicio = time.perf_counter()
        funcao()
        tempos.append(time.perf_counter() - inicio)

    return statistics.median(tempos)

tamanhos = [1_000, 10_000, 100_000, 500_000]
resultados = []

for n in tamanhos:
    base = list(range(n))

    def testar_append():
        lista = base.copy()
        lista.append(-1)

    def testar_insert():
        lista = base.copy()
        lista.insert(0, -1)

    resultados.append({
        "n": n,
        "append": medir(testar_append),
        "insert_inicio": medir(testar_insert)
    })

df_resultados = pd.DataFrame(resultados)
print(df_resultados)

plt.plot(
    df_resultados["n"],
    df_resultados["append"],
    marker="o",
    label="append"
)

plt.plot(
    df_resultados["n"],
    df_resultados["insert_inicio"],
    marker="o",
    label="insert(0, ...)"
)

plt.xlabel("n")
plt.ylabel("tempo (s)")
plt.legend()
plt.show()
```

### Interpretação esperada

`insert(0, ...)` tende a sofrer efeito crescente do deslocamento de elementos, enquanto `append()` possui custo amortizado constante.

Há, entretanto, um cuidado metodológico: neste código cada teste começa copiando a lista. Assim, o tempo registrado também contém o custo de `base.copy()`, que é `O(n)`. O experimento é útil para comparação didática e tendência, mas não isola perfeitamente o tempo de cada operação.

Essa observação é importante porque benchmark também precisa ser criticado metodologicamente.

Tempo medido e Big-O não são equivalentes: o primeiro é uma observação concreta; o segundo é um modelo de crescimento.

---

## Exercício 16 — Desafio: reorganizando o trabalho

### Estratégia A — ordenar repetidamente

```python
def estrategia_a(novos_alunos):
    ranking = []

    for aluno in novos_alunos:
        ranking.append(aluno)
        ranking.sort(
            key=lambda x: x["nota"],
            reverse=True
        )

    return ranking
```

### Estratégia B — ordenar uma vez

```python
def estrategia_b(novos_alunos):
    ranking = []

    for aluno in novos_alunos:
        ranking.append(aluno)

    ranking.sort(
        key=lambda x: x["nota"],
        reverse=True
    )

    return ranking
```

Uma comparação pode utilizar:

```python
for n in [100, 1_000, 5_000]:
    alunos = gerar_alunos(n)

    # medir estrategia_a(alunos)
    # medir estrategia_b(alunos)
```

A segunda estratégia evita executar uma ordenação completa após cada inserção.

O ponto central não é apenas “B é mais rápida”, mas:

> **B reorganiza o processo para evitar trabalho repetido.**

---

# Questão de síntese

Uma resposta possível:

> Perguntar “qual estrutura é mais rápida?” é incompleto porque estruturas não possuem um único custo independente do uso. É necessário especificar qual **operação** será realizada, sobre qual **representação**, para qual **tamanho de entrada** e dentro de qual **sequência de operações**. A análise de **complexidade** ajuda a compreender como o trabalho cresce, enquanto o **tempo medido** mostra o comportamento concreto de uma implementação em determinado ambiente. Assim, a escolha de uma estrutura deve ser orientada pelas operações predominantes do problema, e não por uma classificação absoluta de estruturas como rápidas ou lentas.

---

# Síntese para correção

Ao corrigir os exercícios, priorizar respostas que demonstrem estas relações:

```text
operação
   +
representação
   +
posição / sequência
   +
tamanho da entrada
        ↓
quantidade de trabalho
        ↓
modelo de crescimento
```

e:

```text
complexidade assintótica ≠ tempo medido
```

O estudante não precisa conhecer detalhes internos de CPython ou pandas para atingir os objetivos da Semana 03. O esperado é que consiga explicar **por que** comportamentos diferentes surgem e utilizar Big-O como modelo para descrevê-los.
