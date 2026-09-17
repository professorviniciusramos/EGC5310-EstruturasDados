# EGC5310 --- Semana 06

**Artefato:** 07 --- Soluções e comentários dos exercícios
complementares\
**Tema:** Representação, operações e custo\
**Status:** Revisado após consolidação dos notebooks

> As soluções completas das Atividades 1--9 estão no Notebook Professor.
> Este documento registra as soluções dos exercícios complementares e,
> principalmente, o raciocínio esperado, erros comuns e pontos de
> discussão.

## 1. Por que não converter `StockCode` simplesmente para número?

### Resposta

Porque o domínio contém códigos que não são puramente numéricos. A
representação como texto preserva códigos alfanuméricos e evita perder
informação estrutural.

Além disso, o dataset é transacional: o mesmo `StockCode` aparece em
várias linhas. Para as atividades de busca, construímos deliberadamente
uma visão com uma entrada por código.

### Raciocínio esperado

O estudante deve distinguir:

-   tipo conveniente para cálculo;
-   tipo que preserva a semântica do identificador.

Identificador não é necessariamente quantidade.

### Erro comum

Assumir que "parece número" significa que deve ser armazenado como
inteiro.

------------------------------------------------------------------------

## 2. Por que manter uma coleção ordenada se `dict` oferece consulta exata O(1) médio?

### Resposta

Porque a operação pode não ser busca exata.

Para consulta por faixa, uma coleção ordenada permite localizar o início
em O(log n) e percorrer os `k` resultados:

**O(log n + k)**, depois de preparada.

Um `dict` baseado em hashing não mantém as chaves organizadas segundo
proximidade lexicográfica para essa finalidade. Para descobrir todas as
chaves de uma faixa, uma solução simples precisa examinar as chaves:
O(n).

### Raciocínio esperado

A adequação depende da operação.

### Discussão

Se o sistema realiza muitas buscas exatas **e** muitas buscas por
intervalo, pode ser justificável manter mais de uma representação,
pagando memória, preparação e sincronização.

### Erro comum

Concluir que a Atividade 4 demonstra que lista ordenada é "melhor que
`dict`".

------------------------------------------------------------------------

## 3. Por que não devemos remover automaticamente `InvoiceNo` repetidos?

### Resposta

Porque uma mesma fatura pode possuir várias linhas, cada uma representando um item da venda. Nesse caso, a repetição da chave é parte da estrutura do fenômeno observado.

### Representações possíveis

Uma lista de registros preserva todas as ocorrências.

Um `set` pode responder "quais produtos distintos aparecem?", mas não preserva a multiplicidade.

Um `dict` simples como:

```python
vendas[invoice] = produto
```

substitui o valor anterior quando a mesma chave recebe nova atribuição.

Para representar uma venda com vários itens:

```python
vendas[invoice] = [(produto1, qtd1), (produto2, qtd2)]
```

### Conceito

Estruturas podem ser compostas. Uma chave de `dict` está associada a um valor, e esse valor pode ser outra estrutura.

### Erro comum

> "`dict` não permite vários valores."

A formulação mais precisa é: cada chave possui um valor associado; esse valor pode representar uma coleção de vários elementos.

## 4. O que significa `(A - B) | (B - A)`?

### Resposta

São os elementos que pertencem a exatamente um dos conjuntos.

É a **diferença simétrica**:

``` python
A ^ B
```

### Explicação

`A | B` é a união: elementos que estão em A, em B ou em ambos.

`A ^ B` é a diferença simétrica: elementos que estão em exatamente um dos conjuntos.


-   `A - B`: está em A e não em B;
-   `B - A`: está em B e não em A;
-   união desses dois resultados: está em apenas um deles.

### Ponto de discussão

Uma expressão de uma linha pode representar vários percursos, lookups e
inserções internas.

------------------------------------------------------------------------

## 5. `x in set` e `x in dict` têm relação?

### Resposta

Sim. Em condições usuais, ambos usam hashing para localizar uma
chave/elemento e possuem pertencimento O(1) médio.

Conceitualmente:

``` text
x
↓
hash(x)
↓
posição candidata
↓
comparação
↓
eventual tratamento de colisão/probing
```

### Então por que usar `set`?

Porque, no problema da aula, queremos representar uma coleção única e
realizar operações de conjuntos.

Se precisamos de:

``` text
chave → dados associados
```

um `dict` é semanticamente mais apropriado e também permite:

``` python
chave in dicionario
```

### Erro comum

Afirmar que `set` deve ser usado sempre que houver teste de
pertencimento.

------------------------------------------------------------------------

## 6. Por que `A & B` não é O(1) se `x in B` é O(1) médio?

### Resposta

Porque a interseção precisa considerar vários elementos.

Uma implementação didática equivalente é:

``` python
resultado = set()

for x in A:
    if x in B:
        resultado.add(x)
```

Uma implementação eficiente pode explorar o menor conjunto, mas ainda há
uma quantidade de trabalho relacionada à cardinalidade dos conjuntos.

### Raciocínio esperado

**Uma linha de código não equivale a uma operação computacional.**

------------------------------------------------------------------------

## 7. O que `len(lista)` e `sys.getsizeof(lista)` medem?

### Resposta

`len(lista)` informa quantas referências estão logicamente em uso.

`sys.getsizeof(lista)` informa o tamanho, em bytes, da própria estrutura
da lista naquele momento, incluindo seu overhead e armazenamento de
referências. Não soma recursivamente a memória dos objetos apontados.

### Consequência

Duas listas com o mesmo `len()` podem, em determinados momentos,
apresentar capacidade interna diferente em razão das políticas de
alocação.

### Erro comum

Interpretar `sys.getsizeof(lista)` como memória total de todos os dados
alcançáveis pela lista.

------------------------------------------------------------------------

## 8. O que acontece quando `append()` encontra uma `list` sem capacidade?

### Resposta

De forma simplificada:

1.  a estrutura precisa aumentar seu armazenamento de referências;
2.  o CPython solicita uma capacidade maior que o tamanho estritamente
    necessário;
3.  essa estratégia é chamada de **over-allocation**;
4.  o bloco pode eventualmente ser expandido ou pode ser necessário
    utilizar outra região;
5.  se necessário, as referências são movimentadas para o novo
    armazenamento;
6.  a nova referência é inserida;
7.  os próximos `append`s podem aproveitar os slots já reservados.

### Importante

Não é correto ensinar que Python "sempre dobra" a capacidade.

### Complexidade

Uma chamada específica pode ser cara quando há redimensionamento.

Entretanto, numa sequência longa:

**`append` = O(1) amortizado.**

------------------------------------------------------------------------

## 9. Se removermos metade da lista, a memória cai pela metade?

### Resposta

Não necessariamente.

A política de redimensionamento evita alocar e desalocar memória a cada
pequena oscilação do tamanho lógico. A redução pode ocorrer em degraus e
não precisa coincidir exatamente com a remoção de metade dos elementos.

### Raciocínio esperado

Distinguir:

-   tamanho lógico;
-   capacidade/armazenamento reservado.

------------------------------------------------------------------------

## 10. Por que `bisect.insort()` não implica inserção O(log n)?

### Resposta

`bisect` pode localizar a posição em O(log n).

Mas uma `list` é um array dinâmico de referências. Para criar espaço no
meio, referências posteriores podem precisar ser deslocadas.

Assim:

-   localizar: O(log n);
-   abrir espaço/inserir: O(n);
-   operação total: O(n).

### Erro comum

Usar a complexidade da busca da posição como complexidade de toda a
operação.

------------------------------------------------------------------------

## 11. Se Python e NumPy são O(n), por que NumPy pode ser muito mais rápido?

### Resposta
As duas soluções continuam processando uma quantidade de dados proporcional a `n`, portanto a comparação didática permanece O(n) × O(n).

NumPy pode apresentar tempo concreto menor porque oferece implementações otimizadas para operações sobre arrays e evita que escrevamos e executemos explicitamente o laço elemento a elemento em Python.

Nesta semana não é necessário explicar a organização interna do `ndarray`.

Big-O descreve a taxa de crescimento; não determina sozinho o tempo em segundos.

### Erro comum

Dizer:

> "NumPy é mais rápido porque é O(1)."

Não é o caso do experimento.

------------------------------------------------------------------------

## 12. Quando a conversão para NumPy pode não compensar?

### Resposta

Converter uma lista em `ndarray` também custa tempo e memória,
tipicamente proporcionais ao volume convertido.

Se os dados já estão em arrays e serão processados muitas vezes, o custo
de preparação pode ser amortizado.

Se há poucos dados ou uma única operação simples, a conversão pode
representar parcela relevante do custo total.

### Relação com a Atividade 3

É novamente:

> **preparar × usar**

------------------------------------------------------------------------

## 13. Como atender simultaneamente busca exata e consulta por faixa?

### Solução possível

Manter duas representações:

-   `dict` para busca exata;
-   estrutura ordenada para faixa.

### Novo problema

Cada inserção, remoção ou alteração precisa atualizar as duas
representações corretamente.

Surge uma questão de:

-   sincronização;
-   consistência;
-   memória;
-   custo de manutenção.

Outra possibilidade é reconstruir periodicamente a estrutura ordenada,
aceitando que ela possa ficar temporariamente desatualizada.

### Conclusão

Não existe resposta universal. A decisão depende da frequência relativa
de consultas e atualizações e das garantias exigidas.

------------------------------------------------------------------------

# Síntese

As soluções desta semana devem sempre retornar à mesma pergunta:

> **Qual propriedade da representação está ajudando esta operação e qual
> custo estamos pagando para mantê-la?**
