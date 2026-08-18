# EGC5310 — Semana 02 — Exercícios

## Representação de dados e caracterização de problemas computacionais

**Disciplina:** EGC5310 — Tópicos Especiais em Ciência de Dados VI  
**Semana:** S02 — 20 e 21 de agosto de 2026  
**Artefato:** 06 — Exercícios  
**Cenário principal:** Sistema Acadêmico  

---

# 1. Objetivo dos exercícios

Os exercícios desta semana consolidam a ideia de que:

> **uma representação de dados deve ser analisada em relação ao problema, às operações e às restrições existentes.**

Eles não têm como objetivo testar memorização de estruturas de Python nem exigir análise formal de complexidade.

Ao responder, procure sempre justificar suas escolhas.

A pergunta-guia da semana continua sendo:

> **Melhor para fazer o quê?**

---

# Exercício 1 — A mesma informação, representações diferentes

Considere um livro de uma biblioteca com os seguintes dados:

- código: `501`
- título: `"Estruturas de Dados"`
- autor: `"A. Silva"`
- ano: `2024`
- disponível: `True`

## a)

Represente esse livro utilizando uma **lista**.

```python
# escreva sua resposta aqui
```

## b)

Represente o mesmo livro utilizando um **dicionário**.

```python
# escreva sua resposta aqui
```

## c)

Em cada representação, escreva uma expressão que recupere o **autor**.

## d)

Compare as duas soluções.

Qual delas deixa o significado dos campos mais explícito? Explique.

## e)

Isso significa que essa representação é sempre superior? Justifique.

---

# Exercício 2 — O que estamos representando?

Considere os códigos abaixo.

### Código A

```python
jogador = [10, "Rafael", "Brasil", 8]
```

### Código B

```python
convocados = {2, 5, 8, 10, 14, 21}
```

### Código C

```python
gols_por_jogo = [2, 0, 1, 3, 1]
```

### Código D

```python
jogador = {
    "numero": 10,
    "nome": "Rafael",
    "selecao": "Brasil",
    "gols": 8
}
```

Para cada caso, responda:

1. O que parece estar sendo representado?
2. A estrutura representa um elemento individual ou uma coleção?
3. Que tipo de operação parece natural sobre essa representação?
4. Que informação está explícita e que informação depende da posição ou do contexto?

---

# Exercício 3 — Estrutura adequada para qual operação?

Considere os dados:

```python
estudantes_lista = [
    {"matricula": 1023, "nome": "Ana", "curso": "CD"},
    {"matricula": 1047, "nome": "Bruno", "curso": "CD"},
    {"matricula": 1082, "nome": "Carla", "curso": "Engenharia"},
    {"matricula": 1125, "nome": "Daniel", "curso": "CD"},
]
```

e:

```python
estudantes_dict = {
    1023: {"nome": "Ana", "curso": "CD"},
    1047: {"nome": "Bruno", "curso": "CD"},
    1082: {"nome": "Carla", "curso": "Engenharia"},
    1125: {"nome": "Daniel", "curso": "CD"},
}
```

Para cada operação abaixo, diga qual representação parece mais conveniente e justifique:

## a)

Localizar o estudante de matrícula `1082`.

## b)

Listar todos os estudantes do curso `"CD"`.

## c)

Alterar o nome do estudante de matrícula `1047`.

## d)

Percorrer todos os estudantes para imprimir seus nomes.

## e)

Inserir um novo estudante.

Não basta responder “lista” ou “dicionário”. Explique **qual trabalho parece necessário em cada caso**.

---

# Exercício 4 — Torne o trabalho visível

Complete a função:

```python
def buscar_matricula(estudantes, matricula):
    comparacoes = 0

    for estudante in estudantes:
        # complete aqui
        pass

    return None, comparacoes
```

A função deve:

1. procurar uma matrícula;
2. contar quantas comparações foram realizadas;
3. retornar o estudante encontrado e o número de comparações;
4. retornar `None` e o total de comparações se a matrícula não existir.

Depois teste:

```python
for alvo in [1023, 1082, 1125, 9999]:
    resultado, comparacoes = buscar_matricula(estudantes_lista, alvo)
    print(alvo, comparacoes, resultado)
```

## Questões

### a)

O número de comparações é sempre o mesmo?

### b)

O que acontece quando o elemento procurado está no início?

### c)

E quando está no final?

### d)

E quando não existe?

### e)

Sem utilizar Big-O, descreva com palavras como o trabalho dessa busca se relaciona com o número de estudantes.

---

# Exercício 5 — O trabalho que não aparece no código

Considere:

```python
estudantes_dict.get(1082)
```

e compare com:

```python
for estudante in estudantes_lista:
    if estudante["matricula"] == 1082:
        print(estudante)
        break
```

Responda:

## a)

Qual dos dois códigos apresenta explicitamente um percurso pelos dados?

## b)

No primeiro caso, isso significa que o computador não realiza trabalho algum?

## c)

O que podemos concluir sobre a relação entre **código visível**, **estrutura utilizada** e **trabalho realizado**?

## d)

Por que seria incorreto concluir apenas a partir desse exemplo que “dicionário é sempre melhor”?

---

# Exercício 6 — Uma estrutura desconhecida pode ser compreendida

Observe o código:

```python
def buscar(no, alvo):
    if no is None:
        return None

    if alvo == no.valor:
        return no

    if alvo < no.valor:
        return buscar(no.esquerda, alvo)

    return buscar(no.direita, alvo)
```

Você não precisa saber implementar uma árvore para responder.

## a)

Depois de comparar `alvo` com `no.valor`, o código continua procurando em todos os lugares?

## b)

O que acontece quando `alvo < no.valor`?

## c)

Que característica da organização dos dados esse código parece aproveitar?

## d)

Compare qualitativamente esse comportamento com:

```python
for valor in valores:
    if valor == alvo:
        return valor
```

## e)

Qual das duas soluções precisa, necessariamente, examinar os elementos na mesma sequência em que estão armazenados?

---

# Exercício 7 — Dados ordenados mudam o problema?

Considere:

```python
matriculas = [1023, 1047, 1082, 1125, 1201, 1350]
```

Responda:

## a)

Que informação adicional existe nessa coleção além dos próprios valores?

## b)

Essa informação poderia ser utilizada por um algoritmo de busca?

## c)

Se os valores estivessem em ordem aleatória, a mesma estratégia poderia ser utilizada da mesma forma?

## d)

Organizar os dados antes de uma operação também tem custo. Que possível trade-off aparece aqui?

Não é necessário implementar busca binária.

---

# Exercício 8 — Caracterização de um problema

Uma plataforma de streaming precisa armazenar informações sobre filmes e séries.

Para cada título, existem:

- identificador;
- nome;
- gênero;
- ano;
- avaliação média.

A plataforma precisa realizar frequentemente:

- localizar um título pelo identificador;
- listar títulos por gênero;
- incluir novos títulos;
- atualizar a avaliação média.

Caracterize o problema utilizando:

> **PROBLEMA → DADOS → OPERAÇÕES → REPRESENTAÇÃO → TRABALHO ESPERADO → VOLUME → RESTRIÇÕES**

Preencha:

## Problema

## Dados

## Operações

## Representação possível

## Trabalho esperado

## Volume

Considere, por exemplo, 100 registros e depois 10 milhões.

## Restrições

---

# Exercício 9 — Uma representação, duas operações

Considere a seguinte representação:

```python
filmes = {
    101: {"titulo": "Filme A", "genero": "Drama"},
    102: {"titulo": "Filme B", "genero": "Comédia"},
    103: {"titulo": "Filme C", "genero": "Drama"},
    104: {"titulo": "Filme D", "genero": "Ação"},
}
```

## a)

Escreva código para localizar o filme de identificador `103`.

## b)

Escreva código para listar todos os filmes do gênero `"Drama"`.

## c)

Compare as duas operações.

Qual delas utiliza diretamente a maneira como o dicionário foi organizado?

## d)

Qual delas ainda exige percorrer vários registros?

## e)

O que esse exemplo mostra sobre a frase:

> **“Uma representação pode favorecer uma operação sem favorecer todas.”**

---

# Exercício 10 — Decisão justificada

Um sistema precisa armazenar aproximadamente 500 mil usuários.

As operações mais frequentes são:

1. localizar usuário pelo identificador;
2. atualizar seu e-mail;
3. ocasionalmente listar todos os usuários de determinada cidade.

Você pode considerar, entre outras possibilidades:

- lista de registros;
- dicionário indexado pelo identificador;
- alguma organização mais sofisticada.

Escolha uma representação inicial e escreva uma justificativa técnica curta.

Sua resposta deve mencionar obrigatoriamente:

- os dados;
- a operação predominante;
- alguma consequência da escolha;
- uma operação que sua escolha **não resolve automaticamente**.

---

# Exercício 11 — Identifique o trade-off

Para cada situação, explique qual possível trade-off existe.

## a)

Manter dados ordenados para facilitar buscas, sabendo que novas inserções podem exigir reorganização.

## b)

Usar uma representação muito compacta, mas com campos identificados apenas por posição.

## c)

Criar uma estrutura específica para acelerar consultas por matrícula, embora consultas por curso continuem exigindo percurso.

## d)

Usar uma estrutura simples e fácil de entender para poucos dados, mesmo sabendo que outra poderia ser mais eficiente para milhões de registros.

---

# Exercício 12 — Fechamento conceitual

Responda em poucas frases.

## a)

Por que “funciona” não é suficiente para dizer que uma representação é adequada?

## b)

Por que não faz sentido perguntar apenas “qual estrutura é mais rápida?”?

## c)

Qual é a relação entre:

> **dados → operações → representação → trabalho esperado**

## d)

Complete:

> **Uma representação é adequada quando...**

## e)

Durante esta semana utilizamos expressões como “parece exigir menos trabalho”.

Que pergunta ainda precisamos responder para comparar soluções de maneira mais rigorosa?

---

# Desafio opcional — Proponha outra representação

Escolha um dos problemas desta lista:

- sistema acadêmico;
- álbum de figurinhas;
- biblioteca;
- streaming.

Proponha uma representação diferente das utilizadas nos exemplos.

Pode ser uma estrutura que você já conheça ou que pesquise por conta própria.

Explique:

1. como os dados seriam organizados;
2. qual operação essa estrutura pretende favorecer;
3. qual possível limitação ela introduz;
4. que conhecimento adicional seria necessário para implementá-la.

O objetivo deste desafio não é encontrar uma estrutura “melhor”, mas ampliar o repertório de possibilidades.

---

# Pergunta final

Ao terminar os exercícios, volte à pergunta:

> **Melhor para fazer o quê?**

Se a resposta depender da operação, do volume e das restrições, você chegou ao ponto central da Semana 02.
