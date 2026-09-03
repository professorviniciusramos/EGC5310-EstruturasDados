# EGC5310 — Estruturas de Dados

## Semana 04 — Soluções comentadas

**Arquivo:** `EGC5310-EstruturasDados-S04-07-Solucoes.md`  
**Versão:** 1.0  
**Data:** 02/09/2026

## Exercício 1

Para `63`: meio 6 (`34`), depois meio 9 (`63`): dois passos. Para `62`: examina 34, 63, 41 e 56; o intervalo então se torna vazio. A sequência exata decorre da divisão inteira dos limites.

## Exercício 2

Não é seguro buscar matrícula binariamente quando a lista está ordenada por nome. As comparações de matrícula não permitem eliminar a metade esquerda ou direita. Seria necessário ordenar pela matrícula ou manter outra organização apropriada a essa chave.

## Exercício 3

Com intervalo de dois elementos, `meio` pode coincidir com um limite; atribuir novamente `inicio = meio` ou `fim = meio` preserva o intervalo e pode gerar laço infinito.

```python
def busca(dados, alvo):
    inicio, fim = 0, len(dados) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if dados[meio] == alvo:
            return meio
        if dados[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1
```

Excluir o próprio meio garante que o intervalo diminua.

## Exercício 4

Os valores são potências de dois: aproximadamente 5, 10, 20 e 30 divisões/comparações, admitindo variações de uma unidade conforme a convenção e o caso. A busca sequencial pode exigir respectivamente 32, 1.024, 1.048.576 e 1.073.741.824 comparações.

## Exercício 5

Não. Big-O descreve crescimento para entradas crescentes, não o vencedor de uma execução. Para entradas pequenas, constantes e overhead podem dominar; além disso, o tempo sofre interferência do ambiente. Deve-se observar tendência e mecanismo.

## Exercício 6

As consultas sequenciais custam qualitativamente `500.000 × O(n)`. Ordenar uma vez custa tipicamente `O(n log n)` e as consultas seguintes `500.000 × O(log n)`. Com muitas consultas e nenhuma atualização, o investimento inicial tende a compensar.

## Exercício 7

Manter uma lista simples ordenada durante inserções pode exigir localizar a posição e deslocar elementos. Como atualizações e consultas são igualmente frequentes, o custo total muda; é necessário considerar estruturas que mantenham organização com atualizações eficientes, tema posterior.

## Exercício 8

```python
def buscar_estudante(estudantes, matricula):
    inicio, fim = 0, len(estudantes) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        atual = estudantes[meio]["matricula"]
        if atual == matricula:
            return estudantes[meio]
        if atual < matricula:
            inicio = meio + 1
        else:
            fim = meio - 1
    return None
```

A lista deve estar ordenada por `matricula`.

## Exercício 9

Os testes cobrem ausência de intervalo, intervalo mínimo, atualização dos dois limites e extremos. São úteis para revelar condição de parada incorreta, erro de `+1/-1`, índice inválido e tratamento inadequado do inexistente.

```python
assert busca([], 1) == -1
assert busca([1], 1) == 0
assert busca([1], 2) == -1
assert busca([1, 2, 3], 1) == 0
assert busca([1, 2, 3], 3) == 2
assert busca([1, 2], 2) == 1
```

## Exercício 10

Resposta esperada: a busca binária não é sempre melhor. Ela depende da pré-condição de ordenação pela chave pesquisada. Muitas consultas favorecem pagar o custo de organização; atualizações frequentes podem tornar cara a manutenção da ordem. A decisão deve considerar o processo completo.
