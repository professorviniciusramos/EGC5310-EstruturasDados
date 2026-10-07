# EGC5310 — Semana 09 — Resumo do Professor

**Tema:** Merge/Join — combinando estruturas de dados  
**Uso:** leitura rápida antes da aula  
**Versão:** 1.0 — 07/10/2026

---

## A ideia da semana em uma frase

> **Não ensinar `merge()` como uma função do Pandas; mostrar que combinar dados é um problema de encontrar correspondências entre estruturas e que hashing, ordenação, semântica e cardinalidade determinam como essa combinação funciona e como deve ser interpretada.**

---

## O fio narrativo

Começo com duas listas pequenas:

```text
estudantes
notas
```

e a pergunta:

> **Como produzir matrícula + nome + nota?**

Não falar em join ainda.

A solução natural é:

```text
para cada estudante
    procurar sua matrícula nas notas
```

Isso leva ao **nested-loop**.

Depois pergunto:

> **Por que estamos procurando novamente desde o início para cada estudante?**

Daí recupero **hashing** da S05.

Depois:

> **E se as duas coleções já estiverem ordenadas?**

Daí recupero a **ordenação** da S08 e construo o sort-merge com dois ponteiros.

Somente depois formalizo:

> Tudo isso são estratégias para resolver um problema de **join**.

A segunda parte da semana muda a pergunta:

> **Encontrar correspondências é suficiente? O que fazemos com quem não encontra par? E se uma chave aparecer várias vezes?**

Daí entram:

- `inner`, `left`, `right`, `outer`;
- cardinalidade;
- diagnóstico;
- `validate`;
- Olist;
- benchmark.

---

# ENCONTRO 1

## 1. Nested-loop

Antes do código → **Notebook Estudante, Atividade 1**.

Eles devem prever a estratégia e o número máximo de comparações.

Implementação:

```text
para cada estudante
    percorre notas
        compara matrícula
```

Custo:

\[
O(nm)
\]

Se `n ≈ m`:

\[
O(n^2)
\]

### Não esquecer

O número concreto de comparações pode ser menor por causa do `break`.

Se alguém disser um valor menor que `n × m`, não corrigir automaticamente. Perguntar se está falando:

- da execução concreta;
- ou do pior caso da estratégia.

### Pergunta de transição

> Já conhecemos uma estrutura que permite procurar diretamente por uma chave?

---

## 2. Hash join

Construir:

```text
matrícula → nota
```

com `dict`.

Mensagem principal:

> **O dado não mudou; mudou a representação.**

Custo:

```text
construir índice → O(m)
consultar n vezes → O(n)
total médio → O(n+m)
```

Antes/depois → **Notebook Estudante, Atividade 2**.

### Cuidado

**Hash join NÃO é O(1).**

A consulta individual pode ser `O(1)` em média.

Recuperar S05:

> `O(1)` não significa literalmente uma operação física.

---

## 3. Sort-merge

Pergunta:

> **A ordenação da semana passada pode ajudar?**

Usar dois ponteiros:

```text
i → estudantes
j → notas
```

Regras:

```text
iguais → combina; avança ambos
esquerda menor → avança esquerda
direita menor → avança direita
```

Pergunta essencial:

> **Por que podemos avançar sem voltar?**

Resposta:

> Porque os dados estão ordenados.

Se já ordenados:

\[
O(n+m)
\]

Se precisamos ordenar:

\[
O(n\log n)+O(m\log m)+O(n+m)
\]

→ **Notebook Estudante, Atividade 3**.

### Cuidado

Não dizer simplesmente:

> “sort-merge é O(n+m)”.

Sempre perguntar:

> **Os dados já estavam ordenados?**

---

## 4. Comparação

→ **Notebook Estudante, Atividade 4**.

Não procurar “o vencedor”.

Quero ouvir respostas condicionais:

> “Se já estiver ordenado...”

> “Se o hash já existir...”

> “Se o índice for reutilizado...”

> “Se os dados forem pequenos...”

> “Se memória for importante...”

Mensagem:

> **Big-O informa a decisão; não decide sozinho.**

---

# ENCONTRO 2

## 5. Semântica

Retomar Bruno, que não tem nota.

Perguntar:

> **Bruno desaparece ou permanece?**

Daí:

- `inner` → somente correspondências;
- `left` → preserva esquerda;
- `right` → preserva direita;
- `outer` → preserva ambos.

Só agora mostrar:

```python
df_estudantes.merge(
    df_notas,
    on="matricula",
    how="left"
)
```

→ **Notebook Estudante, Atividade 5**.

Mensagem:

> **`how` é principalmente uma decisão semântica.**

---

## 6. Cardinalidade

Pergunta:

> **A chave precisa ser única?**

Não necessariamente.

Relembrar:

```text
1:1
1:N
N:1
N:N
```

Exemplo importante:

```text
A      B
1      1
1      1
```

Resultado:

\[
2\times2=4
\]

Generalização para uma mesma chave:

\[
a\times b
\]

→ **Notebook Estudante, Atividade 7**.

Mensagem que precisa ficar:

> **Mais linhas depois do merge não significa automaticamente erro.**

---

## 7. Diagnóstico antes do merge

Esta é uma das partes mais importantes.

Quatro perguntas:

1. **Qual é a chave?**
2. **Onde ela deveria ser única?**
3. **Ela realmente é única?**
4. **Quantas linhas esperamos depois?**

Não ficar só nas perguntas.

Mostrar:

```python
len(df)
df[chave].nunique(dropna=False)
df[chave].is_unique
df.duplicated(subset=[chave], keep=False)
df[chave].value_counts()
```

Depois:

```python
validate="one_to_one"
validate="one_to_many"
validate="many_to_one"
validate="many_to_many"
```

→ **Notebook Estudante, Atividade 6**.

### Pergunta importante

> Por que usar `validate` se o merge funciona sem ele?

Resposta:

> Porque queremos testar nossa hipótese sobre a estrutura dos dados.

### Distinção essencial

```text
regra do domínio ≠ propriedade já confirmada nos dados
```

---

## 8. Olist

Usar primeiro:

```text
orders
   │
   ▼
order_items
```

Antes de executar:

> `order_id` é único em `orders`?

> É único em `order_items`?

> Qual cardinalidade esperamos?

Esperado:

```text
orders 1 ───── N order_items
```

Então diagnosticar.

Depois executar com:

```python
validate="one_to_many"
```

→ **Notebook Estudante, Atividade 8**.

Se aumentar o número de linhas:

> **O Pandas duplicou pedidos?**

Não.

Um pedido com três itens produz três relações pedido–item.

---

# 9. Benchmark

→ **Notebook Estudante, Atividade 9** antes de mostrar resultados.

Eles devem prever as curvas.

Comparar:

```text
nested-loop
hash join
sort-merge + ordenação
sort-merge já ordenado
```

### Perguntas

> O hash inclui a construção do índice?

> O sort-merge inclui a ordenação?

> E se o índice for reutilizado?

> E se os dados já chegarem ordenados?

Mensagem:

> **Preparação também é computação.**

Não transformar benchmark em:

> “qual algoritmo venceu?”

---

# 10. Fechamento

Voltar para:

```python
df1.merge(df2, on="id")
```

Perguntar:

> **O que essa linha esconde?**

Quero ouvir:

- chave;
- busca;
- hashing;
- ordenação;
- correspondências;
- ausências;
- cardinalidade;
- duplicatas;
- tamanho do resultado;
- custo.

Síntese:

> **Um merge é também uma hipótese sobre como duas estruturas de dados se relacionam.**

---

# 11. Ponte para S10

Mostrar:

```text
cliente | pedido | produto | categoria | preço
```

Perguntar:

> **Como descobrir quanto cada categoria vendeu?**

Não responder.

Próxima semana:

> **Agrupamentos e agregações.**

---

# 12. Cinco alertas para não esquecer

### 1. `O(1)` não significa uma instrução

Consulta hash média constante ≠ operação física única.

### 2. Hash join não é `O(1)`

A operação completa precisa construir/percorrrer estruturas:

\[
O(n+m)
\]

em média, nas condições discutidas.

### 3. Sort-merge não é sempre `O(n+m)`

Isso vale para o percurso quando a ordenação já existe.

### 4. Chave repetida não é automaticamente erro

Depende da cardinalidade esperada.

### 5. Mais linhas depois do merge não é automaticamente erro

Perguntar primeiro:

> **Qual era a cardinalidade esperada?**

---

# 13. Se eu tiver apenas 30 segundos antes de entrar em sala

Lembrar desta sequência:

```text
PROBLEMA
  ↓
nested-loop → O(nm)
  ↓
hash → preparar para buscar → O(n+m) médio
  ↓
ordenação → dois ponteiros → O(n+m) se já ordenado
  ↓
JOIN
  ↓
inner / left / right / outer
  ↓
CARDINALIDADE
  ↓
chave → unicidade → duplicatas → validate → nº de linhas
  ↓
OLIST
  ↓
BENCHMARK
  ↓
"o que df.merge() esconde?"
```

E repetir durante a aula:

> **Qual é a chave?**

> **Como estamos encontrando as correspondências?**

> **Onde a chave deveria ser única?**

> **Ela realmente é única?**

> **Quantas linhas esperamos depois?**
