# EGC5310 — Estruturas de Dados

## Semana 04 — Benchmark: busca sequencial × busca binária

**Arquivo:** `EGC5310-EstruturasDados-S04-05-Benchmark.md`  
**Versão:** 1.0  
**Data:** 02/09/2026

## 1. Objetivo

Produzir evidência experimental para comparar busca sequencial e busca binária sem confundir tempo medido com ordem de crescimento.

O experimento registra duas medidas:

- **comparações**, diretamente ligadas ao mecanismo;
- **tempo**, dependente da implementação e do ambiente.

## 2. Hipótese

Para o pior caso ou alvo inexistente:

- busca sequencial: até `n` comparações — `O(n)`;
- busca binária: aproximadamente `log₂(n)` comparações — `O(log n)`.

## 3. Procedimento

Execute:

```bash
python EGC5310-EstruturasDados-S04-05-Benchmark.py
```

O script usa coleções ordenadas de `100` a `1.000.000` elementos, os casos “último” e “inexistente”, 11 repetições e mediana do tempo.

## 4. Variáveis do CSV

| Campo | Significado |
|---|---|
| `n` | tamanho da coleção |
| `caso` | alvo no último índice ou inexistente |
| `algoritmo` | sequencial ou binária |
| `comparacoes` | comparações da execução |
| `repeticoes` | medições de tempo |
| `tempo_ns_mediano` | mediana em nanossegundos |
| `tempo_ns_min` | menor tempo observado |
| `tempo_ns_max` | maior tempo observado |

## 5. Interpretação didática

Perguntar antes da execução:

1. Quantas comparações são esperadas para cada `n`?
2. Em qual escala a diferença se tornará marcante?
3. Qual curva deve crescer quase linearmente?
4. O tempo será tão regular quanto a contagem?

Depois da execução:

1. A contagem confirma o mecanismo?
2. O ruído temporal contradiz a análise?
3. Em entradas pequenas, constantes podem dominar?
4. Por que o experimento não “prova” o Big-O?

## 6. Cuidados

- A busca binária exige dados ordenados pela chave pesquisada.
- Um resultado temporal isolado não caracteriza complexidade.
- A mediana reduz, mas não elimina, interferências do ambiente.
- O custo de ordenar não está incluído neste benchmark: essa exclusão é deliberada e deve ser discutida.

## 7. Resultado validado

O CSV fornecido foi produzido pela execução do script. Tempos podem variar entre máquinas; as contagens devem permanecer determinísticas.
