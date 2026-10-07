# EGC5310 — Semana 09 — Roteiro de Aula

**Disciplina:** EGC5310 — Estruturas de Dados para Ciência de Dados  
**Semana:** 09  
**Tema:** Merge/Join — combinando estruturas de dados  
**Artefato:** Roteiro de aula  
**Versão:** 1.0  
**Data de revisão:** 07/10/2026

---

## 1. Ideia central da semana

A Semana 09 introduz operações de **merge/join** a partir de um problema computacional, e não a partir da API do Pandas.

A pergunta orientadora é:

> **Como combinar eficientemente informações que estão em estruturas diferentes quando elas compartilham uma chave?**

A aula deve recuperar explicitamente conhecimentos das semanas anteriores:

- busca sequencial;
- hashing, `dict` e consulta por chave;
- ordenação;
- análise de custo;
- relação entre representação dos dados e operações eficientes.

A progressão principal é:

```text
duas coleções
      ↓
nested-loop
      ↓
busca repetida e custo
      ↓
hashing ───── ordenação
      ↓           ↓
 hash join    sort-merge
       \         /
          JOIN
           ↓
       semântica
           ↓
     cardinalidade
           ↓
 diagnóstico + Pandas
           ↓
          Olist
```

O objetivo não é ensinar apenas `DataFrame.merge()`. Ao final da semana, o estudante deve compreender que uma chamada curta de biblioteca encapsula decisões sobre **chaves, estruturas, busca, correspondência, cardinalidade e custo**.

---

## 2. Objetivos de aprendizagem

Ao final da semana, espera-se que o estudante seja capaz de:

1. reconhecer um problema de combinação de coleções por uma chave;
2. implementar uma solução simples por nested-loop;
3. explicar por que o nested-loop pode apresentar custo `O(nm)`;
4. reorganizar uma coleção em uma estrutura hash para reduzir buscas repetidas;
5. compreender o custo de preparação de um hash join;
6. usar a ordenação para compreender a estratégia de sort-merge com dois ponteiros;
7. distinguir o custo do percurso do custo de ordenar previamente os dados;
8. comparar nested-loop, hash join e sort-merge sem reduzir a decisão apenas ao Big-O;
9. compreender a semântica de `inner`, `left`, `right` e `outer`;
10. identificar relações 1:1, 1:N, N:1 e N:N;
11. diagnosticar unicidade e duplicação de chaves antes de um merge;
12. formular uma expectativa sobre o número de linhas do resultado;
13. utilizar `validate` no Pandas para confrontar os dados com a cardinalidade esperada;
14. interpretar crescimento de linhas como consequência possível da cardinalidade, e não automaticamente como erro;
15. aplicar esse raciocínio às tabelas do Olist;
16. formular hipóteses para o benchmark das estratégias de join.

---

## 3. Pré-requisitos

Os estudantes já devem ter trabalhado com:

- listas e dicionários em Python;
- iteração com `for` e `while`;
- acesso a elementos de listas;
- funções;
- noção de chave;
- hashing e `dict`;
- Big-O;
- busca;
- ordenação;
- DataFrames básicos;
- leitura de CSV.

Não assumir que o estudante conhece previamente:

- algoritmos de join;
- terminologia de bancos de dados para joins;
- cardinalidade como instrumento de diagnóstico de dados;
- `validate` do `pandas.merge()`.

---

## 4. Materiais da semana

Arquivos principais:

- `EGC5310-EstruturasDados-S09-99-Aula-Mestre.ipynb`
- `EGC5310-EstruturasDados-S09-04-Estudante.ipynb`
- `EGC5310-EstruturasDados-S09-05-Professor.ipynb`
- `EGC5310-EstruturasDados-S09-01-Roteiro.md`
- `EGC5310-EstruturasDados-S09-01A-Sequencia-Didatica.md`
- `EGC5310-EstruturasDados-S09-01B-Resumo-Professor.md`

Arquivos de benchmark serão produzidos separadamente.

Dados:

- exemplos pequenos gerados no próprio notebook;
- conjunto Olist para a aplicação real.

---

## 5. Preparação antes da aula

### Verificações técnicas

Antes da aula:

- abrir o Notebook Mestre;
- verificar a renderização dos slides;
- executar as células em sequência;
- abrir o Notebook Estudante em uma segunda aba;
- manter o Notebook Professor disponível para consulta;
- verificar a disponibilidade dos arquivos do Olist;
- verificar os caminhos usados para os CSVs;
- executar previamente o benchmark da semana;
- confirmar que os tamanhos escolhidos não tornam o nested-loop excessivamente demorado.

### Verificações didáticas

Relembrar:

- `O(1)` médio não significa literalmente uma única instrução;
- `O(n+m)` do hash join inclui construção do índice e consultas;
- sort-merge é `O(n+m)` somente quando a ordenação já está disponível;
- `inner`, `left`, `right` e `outer` expressam semânticas distintas;
- crescimento de linhas após um merge pode ser perfeitamente correto;
- `validate` testa uma expectativa de cardinalidade e deve ser apresentado como instrumento de diagnóstico.

---

## 6. Abertura da aula

### Retomada

Começar recuperando três perguntas das semanas anteriores:

> Como encontramos um elemento?

> Como encontramos rapidamente por uma chave?

> O que ganhamos quando os dados estão ordenados?

Em seguida apresentar:

> **E se a informação que queremos estiver dividida entre duas coleções?**

Evitar começar com o termo `merge` ou com Pandas.

### Exemplo inicial

Usar as coleções pequenas de estudantes e notas.

Perguntar:

> Como produzir matrícula, nome e nota?

Enviar os estudantes para a **Atividade 1 do Notebook Estudante** antes de mostrar a implementação.

### Evidência esperada de compreensão

O estudante deve perceber que uma solução natural é:

```text
para cada estudante
    procurar sua matrícula nas notas
```

Ainda não é necessário que use o termo nested-loop.

---

## 7. Nested-loop join

Implementar a solução explicitamente.

Os comentários do código devem ser usados para explicar **decisões**, enquanto os `print`s mostram o comportamento do algoritmo.

### Perguntas durante a execução

- Onde começa a busca da nota de cada estudante?
- Por que procuramos novamente desde o início?
- Quantas comparações podem ocorrer?
- Por que o número real pode ser menor que `n × m`?
- Quando o `break` é seguro?
- O que aconteceria se a chave pudesse repetir?

### Formalização

Somente depois da implementação apresentar:

> **Nested-loop join**

Discutir:

\[
O(nm)
\]

e, para tamanhos semelhantes:

\[
O(n^2)
\]

### Cuidado didático

Se um estudante calcular menos comparações porque considerou o `break`, separar:

- custo da instância concreta;
- pior caso da estratégia.

Não transformar uma previsão razoável em erro conceitual.

---

## 8. Hash join

A transição deve surgir da pergunta:

> **Já conhecemos alguma estrutura que permita localizar uma matrícula sem percorrer toda a lista?**

Recuperar hashing.

Construir o dicionário progressivamente:

```text
matrícula → nota
```

Evitar entregar o dicionário pronto sem mostrar sua construção.

### Conceito central

O dado não mudou. Mudou sua **representação**.

A representação permite trocar:

```text
busca sequencial repetida
```

por:

```text
consulta por chave
```

### Custo

Separar:

- construção do índice: `O(m)`;
- consultas: aproximadamente `O(n)` no comportamento médio;
- total: aproximadamente `O(n+m)`.

### Discussão

Retomar a dúvida da Semana 05:

> `O(1)` não significa que existe literalmente uma operação.

Pode haver cálculo de hash, acesso, comparação e tratamento de colisões. O ponto é a relação entre custo e tamanho da entrada.

Enviar para a **Atividade 2**.

---

## 9. Sort-merge

A transição deve recuperar diretamente a Semana 08:

> **E a ordenação que acabamos de estudar? Ela pode ajudar a combinar coleções?**

Mostrar as duas coleções ordenadas.

Introduzir `i` e `j`.

### Condução do código

Percorrer manualmente os primeiros estados:

```text
101 == 101 → combina
102 < 103  → avança estudante
103 == 103 → combina
104 == 104 → combina
```

Perguntar:

> Por que podemos abandonar uma chave menor sem voltar depois?

A resposta deve depender da **ordenação**.

### Custo

Se já ordenado:

\[
O(n+m)
\]

Se for necessário ordenar:

\[
O(n\log n)+O(m\log m)+O(n+m)
\]

### Conceito central

Separar:

- custo de preparação;
- custo da operação;
- possibilidade de reutilização da preparação.

Enviar para a **Atividade 3**.

---

## 10. Comparação das estratégias

Apresentar conjuntamente:

| Estratégia | Ideia | Custo aproximado |
|---|---|---|
| Nested-loop | comparar pares | `O(nm)` |
| Hash join | construir índice | `O(n+m)` médio |
| Sort-merge | ordenar + percorrer | `O(n log n + m log m)` |
| Sort-merge já ordenado | dois ponteiros | `O(n+m)` |

### Pergunta principal

> Qual é melhor?

A resposta esperada não é o nome de um algoritmo.

Explorar:

- dados pequenos;
- dados já ordenados;
- índice já existente;
- reutilização do índice;
- memória;
- custo de preparação.

Enviar para a **Atividade 4**.

### Evidência esperada de compreensão

O estudante deve abandonar frases como:

> “hash é sempre melhor”

e passar a formular respostas condicionais:

> “se o índice já existe...”

> “se os dados já estão ordenados...”

> “se vamos reutilizar...”

---

## 11. Semântica dos joins

Somente neste momento formalizar que as estratégias anteriores resolvem um problema de **join**.

Usar Bruno, que não possui nota, para introduzir a questão:

> O que fazemos com um registro que não encontrou correspondência?

Apresentar:

- `inner`;
- `left`;
- `right`;
- `outer`.

### Conceito central

Os tipos de join expressam principalmente a **semântica do resultado**, e não uma classificação de desempenho.

Depois apresentar `pandas.merge()`.

Enviar para a **Atividade 5**.

---

## 12. Cardinalidade

Esta é uma parte central da semana e não deve ser tratada apenas como detalhe do Pandas.

Introduzir:

- 1:1;
- 1:N;
- N:1;
- N:N.

Usar exemplos de estudantes e disciplinas.

### Demonstração N:N

Mostrar duas ocorrências da mesma chave em cada lado.

Antes de executar, perguntar:

> Duas linhas de um lado e duas do outro produzem quantas correspondências?

Mostrar:

\[
2\times2=4
\]

Generalizar:

\[
a\times b
\]

### Mensagem principal

> **Mais linhas depois de um merge não significam automaticamente erro.**

O problema é não saber se o crescimento era esperado.

---

## 13. Rotina de diagnóstico antes do merge

Não apresentar apenas um checklist abstrato.

Construir uma rotina operacional.

### Passo 1 — Qual é a chave?

Perguntar o que ela representa no domínio.

### Passo 2 — Onde ela deveria ser única?

Definir a cardinalidade esperada antes de observar o resultado.

### Passo 3 — Ela realmente é única?

Usar:

```python
df[chave].is_unique
df[chave].nunique()
df.duplicated(subset=[chave], keep=False)
df[chave].value_counts()
```

### Passo 4 — Declare a expectativa

Usar `validate`:

```python
validate="one_to_one"
validate="one_to_many"
validate="many_to_one"
validate="many_to_many"
```

### Passo 5 — Compare antes e depois

Registrar:

- linhas à esquerda;
- linhas à direita;
- linhas no resultado;
- ausências;
- duplicações relevantes.

### Pergunta ao estudante

> O resultado observado é compatível com a estrutura que você acreditava que os dados possuíam?

Enviar para as **Atividades 6 e 7**.

---

## 14. Aplicação com Olist

Passar dos exemplos artificiais para dados reais.

Relação inicial:

```text
orders
   │
   ▼
order_items
```

Antes de executar qualquer merge, perguntar:

- `order_id` deveria ser único em `orders`?
- deveria ser único em `order_items`?
- qual cardinalidade esperamos?
- o número de linhas deve aumentar?

### Hipótese esperada

```text
orders 1 ───── N order_items
```

Executar os diagnósticos.

Somente depois:

```python
orders.merge(
    order_items,
    on="order_id",
    how="inner",
    validate="one_to_many"
)
```

### Discussão

Se o número de linhas crescer, perguntar:

> O merge duplicou pedidos por engano?

Mostrar que cada linha representa uma relação pedido–item.

### Extensão

Apontar as próximas relações:

```text
customers
    ↓
orders
    ↓
order_items
    ↓
products
```

Para cada novo merge, repetir:

1. chave;
2. unicidade;
3. cardinalidade;
4. tamanho esperado.

Enviar para a **Atividade 8**.

---

## 15. Benchmark

O benchmark deve comparar as estratégias, mas não ser apresentado como corrida de velocidade.

Comparar:

- nested-loop;
- hash join;
- sort-merge com preparação;
- sort-merge com dados previamente ordenados.

Tamanhos iniciais sugeridos:

```text
500
1.000
2.500
5.000
10.000
```

Calibrar conforme a máquina.

### Antes de mostrar resultados

Enviar para a **Atividade 9** e pedir que os estudantes desenhem ou descrevam as curvas esperadas.

### Perguntas

- Onde aparece o comportamento quadrático?
- O custo de construir o hash foi contabilizado?
- A ordenação foi contabilizada?
- O que muda se o índice for reutilizado?
- O que muda se os dados já estiverem ordenados?
- Tempo é o único custo relevante?
- Memória altera a decisão?

### Resultado conceitual esperado

O benchmark deve reforçar:

> **Preparação também é computação.**

e:

> **Uma comparação só é justa quando sabemos exatamente o que está sendo medido.**

---

## 16. Fechamento

Retornar à chamada:

```python
df1.merge(df2, on="id")
```

Perguntar:

> O que essa linha esconde?

Esperar respostas envolvendo:

- chave;
- busca;
- estruturas auxiliares;
- organização dos dados;
- correspondência;
- semântica;
- unicidade;
- cardinalidade;
- duplicação;
- tamanho do resultado;
- custo.

### Síntese

A mensagem final da semana é:

> **Combinar dados não é apenas chamar `merge()`. É formular e testar uma hipótese sobre como duas estruturas se relacionam.**

---

## 17. Ponte para a Semana 10

Apresentar uma visão analítica:

```text
cliente | pedido | produto | categoria | preço
```

Perguntar:

> Agora que combinamos as informações, como responder quanto cada categoria vendeu?

Isso introduz naturalmente:

**Semana 10 — agrupamentos e agregações.**

---

## 18. Evidências de aprendizagem a observar

Durante a aula, observar se os estudantes conseguem:

- explicar por que o nested-loop repete buscas;
- identificar onde o hash join paga o custo de preparação;
- explicar por que os ponteiros do sort-merge não retornam;
- distinguir dados já ordenados de dados que ainda precisam ser ordenados;
- evitar escolher algoritmo apenas pelo menor Big-O;
- explicar por que Bruno desaparece em um inner join;
- reconhecer uma relação 1:N;
- prever crescimento de linhas;
- investigar duplicatas antes do merge;
- usar `validate` de acordo com uma hipótese;
- interpretar o resultado do Olist sem confundir multiplicação legítima com erro.

---

## 19. Dificuldades prováveis e intervenções

### “Hash join é O(1)”

Intervir:

> A consulta individual pode ser `O(1)` em média. Quantos registros precisamos inserir no índice? Quantas consultas faremos?

Levar a `O(n+m)`.

### “Sort-merge é sempre O(n+m)”

Intervir:

> Os dados chegaram ordenados ou fomos nós que os ordenamos?

Separar preparação de percurso.

### “Se aumentou o número de linhas, o merge está errado”

Intervir:

> Quantas correspondências cada chave pode produzir?

Retomar cardinalidade.

### “A chave deveria ser única, então não preciso verificar”

Intervir:

> Isso é uma regra do domínio ou uma propriedade que você já confirmou nos dados?

Distinguir expectativa e observação.

### “O Pandas fez isso sozinho”

Intervir:

> Que problema computacional precisa ser resolvido independentemente da biblioteca?

Voltar às estratégias manuais.

---

## 20. Checklist de encerramento do professor

Antes de considerar a semana concluída, verificar se foram explicitamente discutidos:

- [ ] problema de combinação por chave;
- [ ] nested-loop;
- [ ] custo `O(nm)`;
- [ ] construção de índice hash;
- [ ] custo médio `O(n+m)` do hash join;
- [ ] sort-merge com dois ponteiros;
- [ ] custo da ordenação;
- [ ] comparação contextual entre estratégias;
- [ ] `inner`, `left`, `right`, `outer`;
- [ ] 1:1, 1:N, N:1 e N:N;
- [ ] multiplicação `a × b` em chaves repetidas;
- [ ] diagnóstico de unicidade;
- [ ] `value_counts`/duplicatas;
- [ ] `validate`;
- [ ] comparação do número de linhas antes/depois;
- [ ] caso Olist;
- [ ] previsão e discussão do benchmark;
- [ ] ponte para agrupamentos e agregações.

---

## 21. Artefatos ainda a concluir na Semana 09

Após este roteiro:

1. Sequência Didática detalhada;
2. Resumo do Professor — leitura em aproximadamente 5 minutos;
3. scripts/notebook do benchmark;
4. resultados do benchmark;
5. análise/interpretação do benchmark;
6. revisão cruzada entre Mestre, Estudante, Professor e demais documentos.
