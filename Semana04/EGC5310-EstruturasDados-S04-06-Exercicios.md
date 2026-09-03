# EGC5310 — Estruturas de Dados

## Semana 04 — Exercícios

**Arquivo:** `EGC5310-EstruturasDados-S04-06-Exercicios.md`  
**Versão:** 1.0  
**Data:** 02/09/2026

## Exercício 1 — Execute sem código

Considere `[3, 8, 12, 17, 21, 29, 34, 41, 56, 63, 77, 88, 95]`.

Para buscar `63` por busca binária, registre em cada passo `inicio`, `fim`, `meio`, valor examinado e região descartada. Repita para `62`.

## Exercício 2 — Pré-condição

Uma lista de estudantes está ordenada por nome. É possível aplicar busca binária para localizar uma matrícula? Explique e indique o que precisaria mudar.

## Exercício 3 — Corrija o algoritmo

```python
def busca(dados, alvo):
    inicio = 0
    fim = len(dados) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if dados[meio] == alvo:
            return meio
        if dados[meio] < alvo:
            inicio = meio
        else:
            fim = meio
    return -1
```

a. Em que situação ele pode não terminar?  
b. Corrija-o.  
c. Explique por que sua correção garante progresso.

## Exercício 4 — Crescimento

Estime o máximo aproximado de comparações binárias para `n = 32`, `1.024`, `1.048.576` e `1.073.741.824`. Compare com a busca sequencial.

## Exercício 5 — Big-O e cronômetro

Para `n=100`, uma execução sequencial levou menos tempo que uma busca binária. Isso demonstra que a busca sequencial tem melhor complexidade? Dê duas razões para não concluir apenas pelo valor medido.

## Exercício 6 — Ordenar uma vez?

Um arquivo com dois milhões de matrículas é carregado uma vez e recebe 500 mil consultas, sem inserções. Compare:

- realizar todas as consultas sequencialmente;
- ordenar uma vez e depois usar busca binária.

Não calcule segundos. Compare qualitativamente os custos e justifique a escolha.

## Exercício 7 — Atualizações contínuas

Outro sistema recebe uma inserção para cada consulta. Explique por que a decisão do exercício anterior não pode ser simplesmente copiada.

## Exercício 8 — Generalização

Adapte a busca binária para uma lista de dicionários ordenada por `matricula`. Teste alvo no primeiro elemento, no último e inexistente.

## Exercício 9 — Casos-limite

Crie testes para lista vazia, um elemento existente, um elemento inexistente, primeiro, último e dois elementos. Explique qual erro cada teste pode revelar.

## Exercício 10 — Decisão argumentada

Escreva um parágrafo respondendo: “A busca binária é sempre melhor?”. Use obrigatoriamente os termos **pré-condição**, **frequência de consultas**, **atualizações** e **custo de organização**.
