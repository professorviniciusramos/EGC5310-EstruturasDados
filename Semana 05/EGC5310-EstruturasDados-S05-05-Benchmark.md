# EGC5310 — Estruturas de Dados

## Semana 05 — Benchmark: distribuição, colisões e custo de busca

**Arquivo:** `EGC5310-EstruturasDados-S05-05-Benchmark.md`  
**Versão:** 1.0  
**Data:** 08/09/2026  
**Status:** experimento executado e validado

## 1. Objetivo

Mostrar experimentalmente que o custo de uma tabela hash não depende apenas da notação “`O(1)` médio”, mas também da distribuição das chaves entre os buckets.

O benchmark não compara ainda busca sequencial, busca binária e `dict`. Essa comparação permanece como objetivo da Semana 06. Aqui, duas tabelas didáticas com o mesmo número de chaves e a mesma capacidade apresentam comportamentos diferentes por causa das colisões.

## 2. Pergunta experimental

> Se duas tabelas possuem a mesma quantidade de chaves e a mesma capacidade, a distribuição dessas chaves pode alterar o custo da busca?

## 3. Hipóteses

### Chaves distribuídas

Com chaves `0, 1, ..., n-1`, tabela de tamanho `n` e `h(chave) = chave % n`:

- cada bucket recebe uma chave;
- não há colisões;
- o maior bucket possui tamanho 1;
- uma busca examina no máximo uma chave.

### Chaves concentradas

Com chaves da forma `indice * n + 2`:

- todas as chaves produzem resto 2;
- há `n - 1` colisões;
- apenas um bucket fica ocupado;
- uma busca pelo último elemento ou por uma chave ausente no mesmo bucket examina `n` chaves.

## 4. Procedimento

Execute no diretório da Semana 05:

```bash
python EGC5310-EstruturasDados-S05-05-Benchmark.py
```

O script:

1. cria tabelas com encadeamento separado;
2. utiliza `n = 100`, `1.000`, `10.000` e `100.000`;
3. mantém taxa de carga igual a 1, isto é, `n` chaves e `n` buckets;
4. compara chaves distribuídas e deliberadamente concentradas;
5. realiza uma busca pelo último elemento inserido e uma busca ausente no mesmo bucket;
6. conta comparações;
7. mede o tempo de busca em 11 repetições e registra a mediana;
8. registra separadamente o tempo de construção.

## 5. Variáveis do CSV

| Campo | Significado |
|---|---|
| `n` | número de chaves inseridas |
| `cenario` | chaves distribuídas ou concentradas |
| `tamanho_tabela` | quantidade de buckets |
| `taxa_carga` | `n / tamanho_tabela` |
| `colisoes` | inserções além da primeira em cada bucket |
| `buckets_ocupados` | buckets com pelo menos uma chave |
| `comprimento_medio_buckets_ocupados` | média considerando apenas buckets ocupados |
| `maior_bucket` | maior quantidade de chaves em um bucket |
| `caso_busca` | alvo existente ao final ou ausente no mesmo bucket |
| `comparacoes` | chaves examinadas durante a busca |
| `repeticoes` | repetições da medição temporal |
| `tempo_construcao_ns` | tempo de construção da tabela |
| `tempo_busca_ns_mediano` | mediana da busca em nanossegundos |
| `tempo_busca_ns_min` | menor tempo observado |
| `tempo_busca_ns_max` | maior tempo observado |

## 6. Condução didática

Antes da execução, peça previsões:

1. Quantos buckets ficarão ocupados em cada cenário?
2. Qual será o tamanho do maior bucket?
3. Quantas comparações serão necessárias na busca pelo último elemento?
4. As duas tabelas têm o mesmo `n` e a mesma capacidade. Por que seus custos podem diferir?

Depois da execução:

1. A contagem de colisões correspondeu à previsão?
2. As comparações cresceram com `n` no cenário concentrado?
3. O tempo acompanhou exatamente a contagem ou apresentou ruído?
4. O experimento contradiz a afirmação de `O(1)` médio/esperado?
5. Por que este cenário concentrado não representa necessariamente o funcionamento usual do `dict` de Python?

## 7. Interpretação esperada

No cenário distribuído, cada busca examina uma única chave. No cenário concentrado, a tabela continua calculando a posição em tempo constante, mas depois precisa percorrer um bucket de tamanho `n`. Portanto, o cálculo do hash não basta para assegurar recuperação eficiente.

O experimento ilustra a diferença entre:

- **caso médio/esperado**, com distribuição e gerenciamento adequados;
- **caso adverso**, com muitas colisões no mesmo bucket.

Não se deve concluir que o `dict` real usa esta implementação ou esta função hash. A estrutura didática torna o mecanismo observável; Python utiliza uma implementação otimizada, outros procedimentos para colisões e redimensionamento automático.

## 8. Limites do experimento

- O cenário concentrado é construído deliberadamente.
- A função `% n` é didática e não representa o hash interno completo do Python.
- O tempo de construção varia com o ambiente e aparece repetido nas duas linhas de busca de cada tabela.
- A contagem de comparações é evidência mais estável que diferenças temporais pequenas.
- O benchmark não mede memória.
- O experimento não compara estruturas concorrentes; isso será feito na S06.

## 9. Resultado validado

O CSV entregue foi produzido pela execução do script. As métricas estruturais e as comparações são determinísticas. Os tempos devem variar quando o experimento for repetido em outro computador.

