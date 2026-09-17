# S06 --- Resumo do Professor

**Leitura de cinco minutos antes da aula**

## Pergunta central

> **Como a representação dos mesmos dados favorece algumas operações e
> encarece outras?**

A aula inteira deve evitar a ideia de "estrutura vencedora". O fluxo é:

**escolha inicial → implementações obrigatórias → medida → explicação do
mecanismo → mudança da operação → nova escolha**

## Dataset

Online Retail (UCI).

Lembrete importante:

-   \~541 mil linhas = **itens de transações**;
-   não são 541 mil produtos distintos;
-   para busca por produto usamos uma visão deduplicada
    `StockCode → Description`;
-   para clientes e NumPy voltamos ao dataset transacional.

## As nove atividades e uma exploração intermediária

1.  **Escolha inicial:** estudante escolhe estrutura para cinco
    operações. Não corrigir.
2.  **Busca exata:** lista/sequencial × ordenada/binária × `dict`.
3.  **Preparação × consulta:** medir construção e muitas consultas
    separadamente.
4.  **Intervalo:** lista ordenada passa a ter propriedade útil; `dict`
    não organiza chaves por faixa.
**Entre 4 e 5 — multiplicidade:** voltar ao dataset transacional. `InvoiceNo` repetido representa vários itens da mesma venda. Lista preserva ocorrências; `set` elimina multiplicidade; `dict[invoice] = produto` sobrescreve; `dict[invoice] = list(...)` representa 1:N e introduz composição de estruturas.

5.  **`set`:** problema realmente conjuntista com clientes A e B.
6.  **`list.append`:** tamanho × capacidade, over-allocation, remoção,
    O(1) amortizado.
7.  **Inserção:** `append` × `insort` × `dict` × `set`; preservar
    propriedade custa.
8.  **NumPy:** Python e NumPy são O(n), mas
    implementação mudam o tempo concreto.
9.  **Escolha revista:** voltar literalmente às respostas da Atividade
    1.

## Frases-chave para usar

> "Melhor para qual operação?"

> "O `dict` não piorou. A pergunta mudou."

> "Uma linha de Python não significa uma operação computacional."

> "O(1) não significa exatamente a mesma quantidade de trabalho em toda
> chamada."

> "`append` é O(1) amortizado; uma chamada específica pode provocar
> redimensionamento."

> "Python não precisa dobrar a `list` quando ela enche."

> "Remover metade dos elementos não implica liberar imediatamente metade
> da memória."

> "Encontrar a posição em O(log n) não torna a inserção em array O(log
> n)."

> "Big-O não é cronômetro."

## `set`: precisão

Não justificar `set` apenas por `x in A`.

`dict` também usa hashing para pertencimento. Nesta aula `set` faz
sentido porque queremos:

-   unicidade;
-   interseção;
-   união;
-   diferença;
-   diferença simétrica.

`x in A`: hash → posição candidata → comparação → eventual probing.

`A & B`: vários testes de pertencimento. Uma linha não é O(1).

## `list`: precisão

Modelo didático:

``` text
[ref][ref][ref][ref][   ][   ]
  ↓    ↓    ↓    ↓
 obj  obj  obj  obj
```

O array de referências é contíguo; os objetos não precisam ser.

`len()` = elementos usados. Capacidade interna = slots reservados.

Quando não cabe novo `append`, ocorre redimensionamento com
**over-allocation**. Não ensinar uma fórmula fixa.

`sys.getsizeof()` ajuda a observar degraus, mas não mede recursivamente
os objetos apontados.

## NumPy: precisão

-   Python com laço: O(n).
-   NumPy sobre n valores: O(n).
-   Tempos concretos diferentes não significam Big-O diferente.
-   `np.array(...)` produz um `numpy.ndarray`, mas não aprofundar `dtype`, layout de memória, strides, views ou implementação interna.
-   Explicação suficiente: NumPy oferece operações otimizadas sobre arrays.
-   Conversão/preparação dos dados também tem custo.
-   Não dizer que "NumPy ganhou porque tem Big-O melhor".

## Frases adicionais para usar

-   "Antes de remover duplicatas, pergunte o que a repetição significa."
-   "Uma chave de `dict` está associada a um valor; esse valor pode ser uma lista."
-   "`A | B` é união; `A ^ B` é diferença simétrica: exatamente um dos grupos."
-   "`bisect.insort` mantém a lista ordenada, mas encontrar a posição rápido não elimina o deslocamento."

## Gestão do tempo

-   0--30: hipótese + busca exata;
-   30--73: benchmark + intervalo;
-   73--115: `set` + interior da `list`;
-   115--151: inserções + NumPy;
-   151--160: decisão revista.

Se faltar tempo, reduza repetições/volumes do benchmark antes de
eliminar a interpretação.

**Preserve a Atividade 9.**

## Materiais abertos

-   Slides gerados pelo Notebook Mestre;
-   Notebook Estudante no Colab;
-   Notebook Professor resolvido.

O Professor deve acompanhar o Estudante na mesma ordem.

## Antes de entrar em sala

Conferir:

-   dataset/UCI e cópia local;
-   `openpyxl`;
-   links do Colab;
-   renderização do Mestre;
-   logo da primeira página;
-   chamadas visuais para o Estudante;
-   execução das soluções no Notebook Professor.

## Fechamento

A frase que os estudantes precisam conseguir defender é:

> **A estrutura deve ser escolhida a partir das operações e propriedades
> necessárias, considerando preparação, consulta, manutenção e
> representação --- não apenas pelo rótulo da complexidade.**
