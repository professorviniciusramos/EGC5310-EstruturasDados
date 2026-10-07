# EGC5310 — Semana 09 — Análise do Benchmark

**Tema:** Merge/Join — comparação de estratégias  
**Arquivo de resultados:** `EGC5310-EstruturasDados-S09-06-Benchmark-Resultados.csv`  
**Data da execução de referência:** 07/10/2026

> Os tempos abaixo são uma execução de referência desta máquina. Em sala, os valores absolutos podem mudar. O interesse didático está principalmente no **formato do crescimento** e na distinção entre **preparação** e **consulta/percurso**.

---

## 1. Cenários medidos

O benchmark compara cinco situações:

| Cenário | O que está incluído |
|---|---|
| `nested_loop` | busca aninhada completa |
| `hash_completo` | construção do índice + consultas |
| `hash_indice_pronto` | somente consultas, com índice já construído |
| `sort_merge_completo` | ordenação das duas coleções + percurso |
| `sort_merge_ja_ordenado` | somente percurso, com dados já ordenados |

Cada cenário foi executado **5 vezes** para cada tamanho, e a análise usa a **mediana**.

---

## 2. Resultados de referência

| n | Nested-loop | Hash completo | Hash pronto | Sort-merge completo | Sort-merge já ordenado |
|---:|---:|---:|---:|---:|---:|
| 500 | 3.394 ms | 0.092 ms | 0.064 ms | 0.259 ms | 0.099 ms |
| 1.000 | 14.272 ms | 0.157 ms | 0.120 ms | 0.538 ms | 0.213 ms |
| 2.500 | 93.771 ms | 0.431 ms | 0.472 ms | 1.350 ms | 0.597 ms |
| 5.000 | 389.526 ms | 0.962 ms | 1.306 ms | 3.064 ms | 1.399 ms |
| 10.000 | 1558.955 ms | 2.316 ms | 1.969 ms | 6.880 ms | 2.895 ms |


---

## 3. O que deve chamar a atenção dos estudantes?

### Nested-loop

Quando `n` dobra, o tempo tende a crescer muito mais do que duas vezes.

Na execução de referência:

- `n = 5.000`: aproximadamente **0.390 s**;
- `n = 10.000`: aproximadamente **1.559 s**.

Dobrar `n` levou a um aumento próximo de quatro vezes, coerente com a expectativa de comportamento aproximadamente quadrático quando as duas coleções crescem juntas.

Isso é mais importante que o valor exato em segundos.

---

## 4. Hash join

Para `n = 10.000`, o hash join completo levou aproximadamente:

**2.316 ms**

Nesta execução, o nested-loop foi cerca de **673 vezes** mais demorado.

Não usar essa razão como regra geral. Ela depende:

- da implementação;
- da máquina;
- do tipo de dado;
- do tamanho;
- do comportamento do cache;
- do custo real da função hash.

A conclusão correta é:

> O crescimento observado do hash join é muito mais próximo do comportamento linear esperado do que o nested-loop.

---

## 5. Índice pronto versus hash completo

Teoricamente queremos separar:

```text
construção do índice
+
consultas
```

de:

```text
somente consultas
```

Nos tamanhos pequenos deste experimento, os tempos são tão baixos que ruído de execução pode fazer `hash_indice_pronto` ocasionalmente aparecer igual ou até um pouco mais lento que `hash_completo`.

Isso **não** demonstra que construir um índice é gratuito.

É uma excelente oportunidade para perguntar:

> Quando duas operações levam frações de milissegundo ou poucos milissegundos, até que ponto pequenas diferenças observadas são evidência confiável?

A função do cenário `hash_indice_pronto` é mostrar conceitualmente o que pode ser reutilizado.

---

## 6. Sort-merge

Para `n = 10.000`:

- sort-merge completo: aproximadamente **6.880 ms**;
- dados já ordenados: aproximadamente **2.895 ms**.

A diferença representa o custo de preparação por ordenação, embora os tempos absolutos também estejam sujeitos a ruído.

A pergunta principal não é:

> “Sort-merge é rápido?”

É:

> **“Os dados já estavam ordenados ou tivemos de pagar pela ordenação?”**

---

## 7. Hash versus sort-merge

Nesta implementação de referência, o hash join completo é mais rápido que o sort-merge completo.

Isso não autoriza concluir:

> “hash é sempre melhor”.

O benchmark foi construído com:

- dados em memória;
- chaves inteiras;
- correspondência 1:1;
- implementação Python específica;
- ausência de custo de I/O;
- memória suficiente;
- nenhum índice persistente;
- nenhuma vantagem externa da ordenação.

Em outro cenário, a decisão pode mudar.

---

## 8. Por que não aumentar muito além de 10 mil?

O nested-loop domina rapidamente o tempo total do experimento.

Com `n = 10.000`, uma repetição já leva aproximadamente **1.56 s** nesta máquina. Como são feitas cinco repetições, esse único ponto consome vários segundos.

A faixa atual é suficiente para mostrar a curva sem transformar a aula em espera pelo benchmark.

Se o computador usado em sala for significativamente mais lento, reduzir o maior tamanho para `7.500` ou diminuir temporariamente o número de repetições.

---

## 9. Perguntas para projetar antes dos resultados

Antes de exibir a tabela ou o gráfico:

1. Qual curva deve crescer mais rapidamente?
2. O que esperamos quando `n` dobra no nested-loop?
3. Qual cenário paga pela construção do hash?
4. Qual cenário reutiliza o hash?
5. Qual cenário paga pela ordenação?
6. Qual cenário parte de dados já ordenados?
7. Os tempos absolutos serão iguais em todos os computadores?
8. Se duas medições diferirem por poucos microssegundos ou décimos de milissegundo, podemos afirmar que uma estratégia é realmente melhor?

---

## 10. O que os estudantes devem concluir

A leitura principal deve ser:

```text
nested-loop
    → pouca preparação
    → muita busca repetida

hash join
    → constrói representação auxiliar
    → consultas eficientes

sort-merge
    → explora ordenação
    → percurso eficiente
    → mas ordenar também custa
```

A decisão depende do **estado inicial dos dados** e do que poderá ser **reutilizado**.

---

## 11. Relação com Big-O

O benchmark não “prova” matematicamente Big-O.

Ele fornece evidência empírica compatível com a análise teórica.

A ordem correta da discussão é:

```text
entender o algoritmo
      ↓
analisar operações
      ↓
formular expectativa de crescimento
      ↓
medir
      ↓
comparar teoria e observação
```

Não:

```text
medir
 ↓
adivinhar uma complexidade
```

---

## 12. Mensagem para fechar o benchmark

> **O melhor tempo observado em uma execução não define sozinho o melhor algoritmo. Precisamos saber o que foi preparado, o que foi medido, o que pode ser reutilizado e como o custo cresce quando os dados aumentam.**

Essa mensagem conecta diretamente o benchmark ao restante da Semana 09.
