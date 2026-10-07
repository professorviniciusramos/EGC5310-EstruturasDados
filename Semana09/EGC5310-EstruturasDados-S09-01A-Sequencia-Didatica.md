# EGC5310 — Semana 09 — Sequência Didática

**Disciplina:** EGC5310 — Estruturas de Dados para Ciência de Dados  
**Semana:** 09  
**Tema:** Merge/Join — combinando estruturas de dados  
**Artefato:** Sequência Didática  
**Versão:** 1.0  
**Data de revisão:** 07/10/2026

---

## 1. Propósito desta sequência

Este documento descreve **como conduzir a Semana 09 em sala**, articulando Notebook Mestre, Notebook Estudante e Notebook Professor.

Não se propõe uma divisão rígida entre “aula teórica” e “aula prática”. Em ambos os encontros, a dinâmica deve alternar:

```text
pergunta
  ↓
previsão
  ↓
código / representação
  ↓
execução
  ↓
observação
  ↓
explicação
  ↓
formalização
```

A unidade didática da semana é:

> **Como combinar informações distribuídas em estruturas diferentes quando elas compartilham uma chave?**

---

# ENCONTRO 1 — DA BUSCA REPETIDA ÀS ESTRATÉGIAS DE JOIN

## 2. Momento 1 — Retomada e apresentação do problema

**Duração de referência:** 10–15 min  
**Artefato principal:** Notebook Mestre  
**Notebook Estudante:** ainda fechado

### Objetivo

Recuperar conhecimentos anteriores e criar a necessidade do novo conteúdo.

### Professor

Apresentar as perguntas:

> Como encontramos um elemento?

> Como encontramos rapidamente por uma chave?

> O que a ordenação nos permite fazer?

Em seguida apresentar as duas coleções pequenas:

```text
estudantes
notas
```

e perguntar:

> Como produzir `matrícula + nome + nota`?

Não usar ainda:

- `merge`;
- `join`;
- `inner`;
- `left`;
- terminologia de banco de dados.

### Estudantes

Propor oralmente maneiras de relacionar as duas coleções.

### Evidência a observar

Espera-se que apareça alguma formulação equivalente a:

> “Para cada estudante, procurar a matrícula nas notas.”

### Se a resposta surgir muito rapidamente

Perguntar:

> E como o computador encontra a matrícula?

Isso força a passagem da descrição lógica para a operação concreta de busca.

---

## 3. Momento 2 — Previsão da solução ingênua

**Duração de referência:** 10 min  
**Artefato:** Notebook Estudante — Atividade 1

### Professor

Solicitar abertura do Notebook Estudante.

Os estudantes devem registrar:

- estratégia;
- máximo de comparações no exemplo;
- crescimento esperado.

Não mostrar ainda o código resolvido.

### Estudantes

Escrever a previsão individualmente ou em dupla.

### Professor — intervenção

Circular pela turma e observar especialmente:

- quem conta somente comparações efetivamente necessárias no exemplo;
- quem calcula `4 × 3`;
- quem já menciona dois `for`;
- quem pensa em dicionário antes da solução básica.

Não corrigir imediatamente.

### Evidência

O estudante deve perceber que combinar as coleções exige alguma forma de **localizar correspondências**.

---

## 4. Momento 3 — Nested-loop: tornar a busca visível

**Duração de referência:** 20–25 min  
**Artefatos:** Mestre + Estudante

### Professor

Construir a implementação por nested-loop.

Usar os comentários do código para explicar decisões e os `print`s para mostrar o percurso.

Parar nos primeiros pares:

```text
101 × 103
101 × 101
```

Perguntar:

> O algoritmo sabia que 101 estava na segunda posição?

Depois:

> Para Bruno, onde a procura começa?

### Estudantes

Completar a implementação da Atividade 1.

Comparar:

- previsão;
- número observado;
- máximo possível.

### Formalização

Somente depois da observação:

> **Nested-loop join**

Introduzir:

\[
O(nm)
\]

e, quando os tamanhos crescem juntos:

\[
O(n^2)
\]

### Ponto de atenção

Se o número de comparações observado for menor que 12:

> Isso contradiz `O(nm)`?

Resposta a construir:

Não. Uma instância concreta pode terminar buscas antecipadamente. A análise descreve o crescimento e o pior caso relevante da estratégia.

### Evidência

O estudante consegue explicar **por que** existem buscas repetidas.

---

## 5. Momento 4 — Escala: quando a solução simples deixa de ser confortável

**Duração de referência:** 10 min  
**Artefato:** Mestre

### Professor

Mostrar a progressão:

| n | comparações potenciais |
|---:|---:|
| 10 | 100 |
| 100 | 10.000 |
| 1.000 | 1.000.000 |
| 100.000 | 10.000.000.000 |

Perguntar:

> O problema é o `for`?

Esperar discussão.

### Síntese

O problema não é sintaticamente usar `for`. É **repetir uma busca linear completa para muitos registros**.

### Transição

> Já aprendemos alguma estrutura que permite procurar por uma chave sem percorrer a coleção inteira?

---

## 6. Momento 5 — Hash join: pagar antes para procurar melhor

**Duração de referência:** 25–30 min  
**Artefatos:** Mestre + Estudante — Atividade 2

### Professor

Recuperar hashing e construir o dicionário progressivamente.

Não mostrar apenas:

```python
indice_notas = {103: 8.5, ...}
```

Mostrar a transformação:

```text
lista
  ↓
matrícula → nota
```

### Pergunta

> O dado mudou?

Resposta esperada:

> Não; mudou a representação.

### Professor

Construir:

1. índice;
2. percurso dos estudantes;
3. consulta por matrícula.

### Estudantes

Completar a Atividade 2.

### Formalização do custo

Separar no quadro/slides:

```text
construção do índice → O(m)
consultas             → O(n)
--------------------------------
total médio           → O(n+m)
```

### Intervenção importante

Perguntar:

> Então hash join é O(1)?

A resposta deve ser **não**.

A consulta individual é aproximadamente `O(1)` no comportamento médio; a combinação das coleções exige construir e percorrer estruturas.

### Recuperação da S05

Reforçar:

> `O(1)` não significa uma única instrução.

### Evidência

O estudante deve distinguir:

- custo da consulta;
- custo da operação completa.

---

## 7. Momento 6 — Sort-merge: reutilizando a ordenação

**Duração de referência:** 25–30 min  
**Artefatos:** Mestre + Estudante — Atividade 3

### Professor

Apresentar as duas coleções ordenadas.

Perguntar:

> Se já passamos da matrícula 101, precisamos voltar a ela?

Introduzir:

```python
i = 0
j = 0
```

### Condução manual

Simular:

```text
101 == 101
102 < 103
103 == 103
104 == 104
```

A cada passo perguntar:

> Quem pode avançar?

> Por que é seguro avançar?

### Estudantes

Completar a implementação com dois ponteiros.

### Formalização

Se já ordenado:

\[
O(n+m)
\]

Se for necessário ordenar:

\[
O(n\log n)+O(m\log m)+O(n+m)
\]

### Pergunta essencial

> Sort-merge é sempre `O(n+m)`?

Não.

### Evidência

O estudante deve verbalizar:

> “Se os dados já estão ordenados...”

Essa condição é mais importante do que decorar a fórmula.

---

## 8. Momento 7 — Comparar sem eleger um vencedor universal

**Duração de referência:** 15–20 min  
**Artefato:** Notebook Estudante — Atividade 4

### Professor

Apresentar conjuntamente:

- nested-loop;
- hash join;
- sort-merge.

Perguntar:

> Qual é melhor?

Deixar respostas aparecerem antes de problematizar.

### Estudantes

Responder aos cenários da Atividade 4.

### Professor

Explorar:

- coleção pequena;
- dados já ordenados;
- índice já disponível;
- reutilização;
- memória.

### Fechamento do primeiro encontro

Construir oralmente:

> Não escolhemos estruturas e algoritmos isoladamente. A escolha depende de como os dados estão representados, do que já foi preparado e do que precisaremos fazer depois.

### Se houver tempo adicional

Antecipar a pergunta:

> Até agora só mantivemos quem encontrou correspondência. Isso é sempre o que queremos?

Não formalizar ainda todos os tipos de join.

---

# ENCONTRO 2 — SEMÂNTICA, CARDINALIDADE E DADOS REAIS

## 9. Momento 8 — Retomada do primeiro encontro

**Duração de referência:** 10 min  
**Artefato:** Mestre

### Professor

Sem mostrar a tabela comparativa inicialmente, perguntar:

> Quais foram as três estratégias?

Para cada uma:

> Onde ela paga o custo?

Esperado:

- nested-loop → busca repetida;
- hash → preparação do índice;
- sort-merge → ordenação, quando necessária.

### Objetivo

Retomar ideias, não sintaxe.

---

## 10. Momento 9 — O que fazer com quem não encontrou par?

**Duração de referência:** 20 min  
**Artefatos:** Mestre + Estudante — Atividade 5

### Professor

Retomar Bruno.

Perguntar:

> Bruno deve desaparecer?

Deixar a turma discutir o significado da pergunta.

### Apresentar

- inner;
- left;
- right;
- outer.

Usar a mesma base pequena.

### Estudantes

Prever se Bruno aparece em cada tipo.

Somente depois executar o Pandas.

### Formalização

Mostrar:

```python
df_estudantes.merge(
    df_notas,
    on="matricula",
    how="left"
)
```

### Pergunta

> O que `how` está decidindo?

Resposta esperada:

> Quais correspondências e ausências permanecem no resultado.

### Evidência

O estudante compreende que os tipos de join são principalmente uma decisão **semântica**.

---

## 11. Momento 10 — A chave precisa ser única?

**Duração de referência:** 15 min  
**Artefato:** Mestre

### Professor

Mostrar:

```text
101 → Estruturas
101 → Cálculo
101 → Estatística
```

Perguntar:

> Há algum problema em 101 aparecer três vezes?

Não responder imediatamente.

### Introduzir cardinalidades

- 1:1;
- 1:N;
- N:1;
- N:N.

Usar exemplos simples.

### Ponto central

Duplicação de chave não é automaticamente erro.

Ela deve ser interpretada em relação ao **domínio**.

---

## 12. Momento 11 — A multiplicação das correspondências

**Duração de referência:** 15 min  
**Artefatos:** Mestre + Estudante — Atividade 7

### Professor

Mostrar:

```text
A          B
1          1
1          1
```

Perguntar antes de executar:

> Quantas linhas?

### Estudantes

Registrar a previsão.

### Execução

Mostrar as quatro combinações.

Formalizar:

\[
a\times b
\]

para uma mesma chave.

### Mensagem

> N:N pode aumentar muito o número de linhas sem que o software produza qualquer erro.

### Evidência

O estudante deixa de usar “duplicou” como sinônimo automático de problema.

---

## 13. Momento 12 — Diagnóstico antes do merge

**Duração de referência:** 30–35 min  
**Artefatos:** Mestre + Estudante — Atividade 6

Este é um dos momentos mais importantes da semana.

### Professor

Apresentar as quatro perguntas:

1. Qual é a chave?
2. Onde ela deveria ser única?
3. Ela realmente é única?
4. Quantas linhas esperamos depois?

### Importante

Não deixar as perguntas apenas no nível discursivo.

Executar diagnóstico.

### Parte A — tamanho e unicidade

Usar:

```python
len(df)
df[chave].nunique(dropna=False)
df[chave].is_unique
df.duplicated(subset=[chave], keep=False)
```

Perguntar o que cada medida responde.

### Parte B — quais chaves repetem?

Usar:

```python
df[chave].value_counts()
```

Filtrar frequências maiores que 1.

### Parte C — expectativa explícita

Apresentar:

```python
validate="one_to_one"
validate="one_to_many"
validate="many_to_one"
validate="many_to_many"
```

### Pergunta

> Por que usar `validate` se o merge já funciona sem ele?

Resposta a construir:

Porque queremos testar uma **hipótese sobre os dados**, não apenas executar uma operação.

### Parte D — antes e depois

Comparar números de linhas.

### Estudantes

Resolver a Atividade 6.

### Evidência

O estudante consegue separar:

```text
o que deveria acontecer
```

de:

```text
o que os dados realmente mostram
```

---

## 14. Momento 13 — Olist: saindo do exemplo artificial

**Duração de referência:** 30–40 min  
**Artefatos:** Mestre + Estudante — Atividade 8

### Professor

Apresentar:

```text
orders
   │
   ▼
order_items
```

Não executar imediatamente.

### Previsão

Perguntar:

> `order_id` deve ser único em `orders`?

> E em `order_items`?

> Qual cardinalidade esperamos?

> O resultado terá quantas linhas em relação a `orders`?

### Estudantes

Registrar hipóteses.

### Professor

Carregar os dados.

Executar diagnóstico:

```python
diagnosticar_chave(...)
```

Comparar regra esperada com dado observado.

### Merge

Executar com:

```python
validate="one_to_many"
```

### Discussão

Se o resultado tiver mais linhas:

> O Pandas duplicou pedidos?

Conduzir para:

> Um pedido aparece uma vez para cada item associado.

### Extensão conceitual

Mostrar:

```text
customers
    ↓
orders
    ↓
order_items
    ↓
products
```

Perguntar para cada ligação:

> Qual chave?

> Onde esperamos unicidade?

Não é necessário executar todos os merges se o tempo estiver apertado.

### Evidência

O estudante transfere a rotina de diagnóstico do exemplo pequeno para um conjunto real.

---

## 15. Momento 14 — Benchmark: previsão antes do gráfico

**Duração de referência:** 25–30 min  
**Artefatos:** Estudante — Atividade 9 + benchmark da semana

### Professor

Antes de apresentar resultados, pedir:

> Desenhem ou descrevam as curvas esperadas.

Comparar:

- nested-loop;
- hash join;
- sort-merge incluindo ordenação;
- sort-merge com dados previamente ordenados.

### Estudantes

Registrar previsões.

### Professor

Executar ou apresentar resultados do benchmark.

### Discussão

Perguntar:

> O que exatamente foi medido?

> A construção do hash entrou no tempo?

> A ordenação entrou?

> E se o hash for reutilizado?

> E se os dados chegarem ordenados?

### Mensagem central

> **Preparação também é computação.**

### Cuidado

Não transformar o benchmark em ranking absoluto.

O objetivo é relacionar:

```text
representação
+
preparação
+
algoritmo
+
cenário
```

---

## 16. Momento 15 — Síntese

**Duração de referência:** 10–15 min  
**Artefatos:** Mestre + fechamento do Estudante

### Professor

Voltar para:

```python
df1.merge(df2, on="id")
```

Perguntar:

> O que essa linha esconde?

Registrar respostas da turma.

Esperar referências a:

- chave;
- busca;
- hash;
- ordenação;
- correspondência;
- ausências;
- cardinalidade;
- duplicatas;
- tamanho do resultado;
- custo.

### Síntese verbal sugerida

> No início da semana, `merge` poderia parecer apenas uma função do Pandas. Agora sabemos que combinar dados exige encontrar correspondências, escolher ou explorar representações, entender quais registros devem permanecer e verificar se a relação observada entre as chaves é aquela que esperávamos.

---

## 17. Momento 16 — Ponte para a próxima semana

**Duração de referência:** 5 min

Mostrar:

```text
cliente | pedido | produto | categoria | preço
```

Perguntar:

> Depois de construir essa coleção, como descobrir quanto cada categoria vendeu?

Não resolver.

Apresentar:

> **Semana 10 — agrupamentos e agregações.**

---

# 18. Gestão do tempo

Os tempos anteriores são referências, não blocos rígidos.

## Se o primeiro encontro estiver mais rápido

Aprofundar:

- simulação manual do sort-merge;
- efeito da reutilização do índice;
- comparação entre custo assintótico e tempo observado;
- situação em que uma chave repete e invalida o `break`.

## Se o primeiro encontro estiver mais lento

Preservar obrigatoriamente:

1. nested-loop;
2. hash join;
3. sort-merge;
4. comparação entre estratégias.

Reduzir o número de cenários discutidos na Atividade 4.

## Se o segundo encontro estiver mais rápido

Expandir:

- diagnóstico de outras relações do Olist;
- `customers → orders`;
- `order_items → products`;
- análise de chaves sem correspondência;
- discussão de memória no benchmark.

## Se o segundo encontro estiver mais lento

Preservar obrigatoriamente:

1. semântica inner/left;
2. cardinalidade;
3. diagnóstico antes do merge;
4. Olist;
5. pelo menos a previsão e leitura principal do benchmark.

`right` e `outer` podem ser tratados de forma mais breve.

---

# 19. Perguntas-chave da semana

Estas perguntas devem reaparecer ao longo da aula.

### Sobre algoritmo

> Onde o algoritmo está procurando?

> Ele precisa começar novamente?

> O que já sabemos sobre a organização dos dados?

### Sobre custo

> Estamos medindo apenas a consulta ou também a preparação?

> Os dados já estavam ordenados?

> O índice já existia?

### Sobre semântica

> Quem deve permanecer quando não existe correspondência?

### Sobre cardinalidade

> Onde a chave deveria ser única?

> Ela realmente é única?

> Quantas correspondências uma chave pode produzir?

### Sobre validação

> O resultado é compatível com aquilo que acreditávamos sobre os dados?

---

# 20. Erros produtivos

Alguns erros devem ser explorados em vez de imediatamente corrigidos.

## “São exatamente `n × m` comparações”

Perguntar:

> O `break` pode alterar a execução concreta?

Depois distinguir pior caso e execução observada.

## “Hash join é O(1)”

Perguntar:

> Quem construiu o hash?

> Quantos registros precisam ser processados?

## “Sort-merge é O(n+m)”

Perguntar:

> Quem ordenou os dados?

## “Duplicata é erro”

Perguntar:

> Um pedido pode ter dois itens?

## “O merge aumentou as linhas, então deu errado”

Perguntar:

> Qual era a cardinalidade esperada?

## “Se deveria ser único, então é único”

Perguntar:

> Você descreveu uma regra do domínio ou verificou os dados?

---

# 21. Critérios de sucesso da semana

A semana cumpriu seu objetivo se, ao final, a maior parte da turma conseguir explicar, sem depender da sintaxe exata do Pandas:

1. por que nested-loop pode ficar caro;
2. como hashing evita buscas repetidas;
3. como ordenação permite percursos sincronizados;
4. por que preparação deve entrar na análise;
5. por que tipos de join mudam o significado do resultado;
6. por que cardinalidade determina o potencial crescimento do resultado;
7. por que devemos verificar unicidade e duplicatas;
8. por que `validate` transforma uma suposição em uma verificação;
9. por que um merge correto pode produzir mais linhas;
10. quais perguntas devem ser feitas antes de confiar em `df.merge()`.

---

# 22. Relação entre os artefatos

## Notebook Mestre

Usado para:

- narrativa;
- explicações;
- demonstrações;
- código completo;
- visualização do comportamento;
- formalização.

## Notebook Estudante

Usado para:

- previsão;
- implementação;
- registro;
- interpretação;
- comparação entre expectativa e resultado.

## Notebook Professor

Usado como:

- gabarito;
- apoio durante a aula;
- referência para respostas aceitáveis;
- registro de intervenções importantes.

## Roteiro

Usado para:

- visão global da semana;
- conceitos;
- preparação;
- dificuldades;
- objetivos.

## Sequência Didática

Este documento responde principalmente:

> **Em que ordem e de que maneira devo conduzir cada momento em sala?**

## Resumo do Professor

Será o documento curto para leitura imediatamente antes da aula.

---

# 23. Checklist imediatamente após a aula

Registrar brevemente:

- [ ] os estudantes perceberam a relação entre S05, S08 e S09?
- [ ] os prints ajudaram a compreender nested-loop?
- [ ] a construção progressiva do hash foi suficiente?
- [ ] o sort-merge com dois ponteiros foi compreendido?
- [ ] houve confusão entre `O(1)` da consulta e custo do join?
- [ ] houve confusão entre `O(n+m)` do percurso e custo de ordenação?
- [ ] os tipos de join ficaram semanticamente claros?
- [ ] cardinalidade 1:N foi compreendida?
- [ ] N:N causou surpresa produtiva?
- [ ] a rotina de diagnóstico foi aplicada antes do merge?
- [ ] `validate` fez sentido para os estudantes?
- [ ] o Olist funcionou tecnicamente?
- [ ] o benchmark confirmou ou contrariou as previsões?
- [ ] houve tempo suficiente para a síntese?
- [ ] que ajuste deve ser incorporado à S10 ou a uma futura edição da S09?
