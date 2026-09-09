# EGC5310 — Estruturas de Dados

## Semana 05 — Soluções comentadas

**Tema:** hashing, conjuntos, dicionários e estruturas associativas  
**Versão:** 1.0  
**Status:** material do professor

## Exercício 1

`121 → 1`, `134 → 4`, `147 → 7`, `154 → 4`, `181 → 1`, `194 → 4`. Colidem `(121, 181)` e o grupo `(134, 154, 194)`. O resultado depende do padrão das chaves e do tamanho 10; chaves com finais concentrados produzirão muitos buckets longos. Um conjunto pequeno não demonstra distribuição geral.

## Exercício 2

A matrícula é uma chave do domínio e identifica o estudante. `20260123 % 10 == 3` é uma posição candidata produzida pela função didática. A posição em uma lista é consequência da ordem atual da coleção. Se Ana está na posição 0 e um novo estudante é inserido no início, Ana passa à posição 1, mas sua matrícula permanece `20260123`.

## Exercício 3

O programa não lança erro. Ao final, `tabela[2] == (172, "Bruno")`; Ana foi sobrescrita. Foi violado o requisito de preservar e recuperar os dois registros. Uma solução é usar uma lista por posição:

```python
tabela = [[] for _ in range(10)]
tabela[2].append((102, "Ana"))
tabela[2].append((172, "Bruno"))
```

O erro comum é considerar “executou” como sinônimo de “está correto”.

## Exercício 4

```python
def buscar(tabela, matricula):
    posicao = matricula % len(tabela)

    for chave_existente, estudante in tabela[posicao]:
        if chave_existente == matricula:
            return estudante

    return None
```

A função hash leva a um bucket, não necessariamente a um único item. Chaves distintas podem colidir; por isso, a busca confirma a chave dentro do bucket.

## Exercício 5

```python
def inserir(tabela, matricula, estudante):
    posicao = matricula % len(tabela)
    bucket = tabela[posicao]

    for indice, (chave_existente, _) in enumerate(bucket):
        if chave_existente == matricula:
            bucket[indice] = (matricula, estudante)
            return

    bucket.append((matricula, estudante))
```

Também é aceitável retornar `True` para inserção e `False` para atualização, desde que o contrato seja explicado. Esquecer o `return` após substituir é um erro comum: a função também adicionaria uma cópia ao final.

## Exercício 6

```python
por_matricula = {}
for estudante in estudantes:
    por_matricula[estudante["matricula"]] = estudante

encontrado = por_matricula.get(118)
ausente = por_matricula.get(999)
```

Uma compreensão equivalente é aceitável:

```python
por_matricula = {
    estudante["matricula"]: estudante
    for estudante in estudantes
}
```

A primeira forma é preferível neste momento por ser mais explícita. Construir o índice percorre `n` registros, portanto custa `O(n)` no total. O custo pode ser amortizado por muitas consultas posteriores com custo médio esperado próximo de `O(1)`. `por_matricula[999]` geraria `KeyError`; `.get(999)` retorna `None` por padrão.

## Exercício 7

```python
vistas = set()
duplicadas = []

for matricula in matriculas:
    if matricula in vistas and matricula not in duplicadas:
        duplicadas.append(matricula)
    else:
        vistas.add(matricula)

print(duplicadas)
```

Uma segunda estrutura `set` para duplicadas evita a busca linear em `duplicadas` quando o volume cresce. Converter diretamente para `set` remove repetições, mas não informa quais valores repetiram nem preserva, como requisito geral, a ordem das segundas ocorrências.

## Exercício 8

1. `list`: preserva sequência e repetições.
2. `dict`: código → dados da disciplina.
3. `set`: pertencimento é a operação predominante.
4. `dict`: categoria → contagem.
5. `list`: sequência curta e ordenada no tempo.

Alternativas podem ser válidas sob requisitos adicionais. Por exemplo, para guardar também dados associados a cada CPF bloqueado, um `dict` seria mais expressivo que um `set`.

## Exercício 9

1. Chaves distintas podem produzir a mesma posição; a implementação deve tratar colisões.
2. A consulta em `dict` tem custo médio/esperado `O(1)` sob condições adequadas; casos adversos e detalhes de implementação existem.
3. `O(1)` indica que o crescimento dominante não depende de `n`; não especifica uma instrução nem tempo zero.
4. Um `set` representa elementos únicos e pertencimento, sem associação explícita de cada elemento a um valor.
5. `dict` é apropriado para acesso por chave; listas permanecem adequadas para sequência, ordem, repetições e percursos.

## Exercício 10

Uma solução combina:

```python
eventos_em_ordem = []       # todos os eventos, na ordem de chegada
ids_processados = set()     # pertencimento/unicidade de id_evento
perfil_por_usuario = {}     # id_usuario -> perfil
```

Cada estrutura atende uma operação distinta. Usar apenas `dict` por `id_evento` poderia rejeitar duplicatas, mas não expressaria sozinho a sequência completa se eventos legítimos precisassem ser preservados em ordem; detalhes do requisito determinam a combinação.

## Exercício 11

Exemplo de projeto:

- variável independente: tamanho `n` (`10²`, `10³`, `10⁴`, `10⁵`, ...);
- métricas: comparações e tempo por consulta; memória, se o ambiente permitir;
- cenários: alvo no início/meio/fim e ausente; amostra de consultas existentes e ausentes;
- preparação: ordenar a lista e construir o `dict`, medidos separadamente;
- controle: mesmos dados e mesmas consultas, aquecimento, várias repetições e mediana;
- ameaças: ruído do ambiente, otimizações de Python, distribuição das chaves, tamanhos insuficientes e comparação injusta que omita preparação.

Não há uma única resposta correta, mas a comparação deve separar construção de consulta e explicitar a carga de trabalho.

