# EGC5310 --- Semana 01 --- Exercícios

**Disciplina:** EGC5310 --- Tópicos Especiais em Ciência de Dados VI\
**Semana:** 01\
**Tema:** Do problema ao custo computacional\
**Cenário:** Sistema acadêmico\
**Materiais relacionados:** `Semana-01-Estudante.ipynb`,
`Semana-01-Professor.ipynb`, `Semana-01-Benchmark.md`

------------------------------------------------------------------------

## 1. Objetivos

Os exercícios consolidam os conceitos efetivamente trabalhados na Semana
01. Ao concluí-los, o estudante deverá ser capaz de:

-   explicar o funcionamento da busca sequencial;
-   identificar o tamanho da entrada de um problema;
-   contar operações relevantes de um algoritmo;
-   distinguir melhor e pior caso;
-   relacionar `T(n)` ao crescimento do custo;
-   interpretar `O(1)`, `O(n)` e `O(n²)` em nível introdutório;
-   distinguir tempo observado de ordem de crescimento;
-   interpretar resultados experimentais;
-   justificar por que uma solução correta pode tornar-se inadequada
    quando os dados crescem.

------------------------------------------------------------------------

# Exercício 1 --- A busca passo a passo

Considere a coleção:

``` python
estudantes = [
    {"matricula": 1201, "nome": "Alice"},
    {"matricula": 1207, "nome": "Bruno"},
    {"matricula": 1215, "nome": "Carla"},
    {"matricula": 1220, "nome": "Daniel"},
    {"matricula": 1234, "nome": "Eduarda"},
    {"matricula": 1248, "nome": "Felipe"},
]
```

e o algoritmo:

``` python
def buscar(estudantes, matricula):
    for estudante in estudantes:
        if estudante["matricula"] == matricula:
            return estudante
    return None
```

Responda:

a.  Quantas comparações são realizadas ao procurar a matrícula `1201`?\
b.  Quantas comparações são realizadas ao procurar `1220`?\
c.  Quantas comparações são realizadas ao procurar `1248`?\
d.  Quantas comparações são realizadas ao procurar `9999`?\
e.  Qual dos casos representa o melhor caso?\
f.  Qual ou quais representam o pior caso?\
g.  Se a coleção possuir `n` estudantes, quantas comparações poderão ser
    necessárias no pior caso?

------------------------------------------------------------------------

# Exercício 2 --- Instrumentando um algoritmo

Complete a função abaixo para que ela retorne, além do estudante
encontrado, o número de comparações realizadas.

``` python
def buscar_contando(estudantes, matricula):
    comparacoes = 0

    for estudante in estudantes:
        # complete

    # complete
```

A função deve produzir resultados compatíveis com:

``` python
resultado, comparacoes = buscar_contando(estudantes, 1215)
```

Depois:

a.  teste uma matrícula no primeiro elemento;\
b.  teste uma matrícula aproximadamente no meio da coleção;\
c.  teste a última matrícula;\
d.  teste uma matrícula inexistente.

Registre os quatro números de comparações e explique o padrão observado.

------------------------------------------------------------------------

# Exercício 3 --- Antes de executar

Considere uma busca sequencial por uma matrícula **inexistente**.

Sem executar código, complete:

          n   Comparações previstas
  --------- -----------------------
         20 
        200 
      2.000 
     20.000 
    200.000 

Depois responda:

a.  Se `n` for multiplicado por 10, o que ocorre com o número de
    comparações?\
b.  Qual relação existe entre `n` e o número de comparações no pior
    caso?\
c.  Essa relação é compatível com `O(1)`, `O(n)` ou `O(n²)`? Justifique
    em uma frase.

Somente depois de registrar as previsões, você pode escrever ou adaptar
um programa para verificá-las.

------------------------------------------------------------------------

# Exercício 4 --- De T(n) para a ordem de crescimento

Considere três algoritmos hipotéticos cujos custos são descritos por:

\[ T_A(n)=4 \]

\[ T_B(n)=3n+7 \]

\[ T_C(n)=2n\^2+5n+10 \]

Para cada algoritmo:

a.  identifique o termo que determina o comportamento quando `n`
    cresce;\
b.  classifique a ordem de crescimento entre `O(1)`, `O(n)` e `O(n²)`;\
c.  descreva, qualitativamente, o que tende a acontecer com o custo
    quando `n` dobra.

Não é necessário calcular tempos de execução.

------------------------------------------------------------------------

# Exercício 5 --- O cronômetro contradiz o Big-O?

Dois estudantes executaram a mesma busca sequencial no pior caso.

### Computador A

            n     Tempo
  ----------- ---------
       10.000   0,001 s
      100.000   0,008 s
    1.000.000   0,091 s

### Computador B

            n     Tempo
  ----------- ---------
       10.000   0,002 s
      100.000   0,014 s
    1.000.000   0,137 s

Responda:

a.  Os dois computadores produziram os mesmos tempos?\
b.  Isso significa que executaram algoritmos com complexidades
    diferentes?\
c.  Quantas comparações são esperadas para `n = 1.000.000`, supondo
    matrícula inexistente?\
d.  Qual informação caracteriza melhor a ordem de crescimento do
    algoritmo: os segundos medidos ou a relação entre `n` e o número de
    operações?\
e.  Explique por que os resultados são compatíveis com uma busca `O(n)`
    mesmo que as razões entre os tempos não sejam exatamente iguais.

------------------------------------------------------------------------

# Exercício 6 --- Uma solução correta pode ser inadequada?

Uma universidade possui uma coleção com **5 milhões de estudantes e
ex-estudantes**. Um serviço recebe frequentemente uma matrícula e
precisa recuperar o respectivo registro.

A primeira implementação percorre a coleção desde o início até encontrar
a matrícula.

Responda:

a.  O algoritmo pode estar correto?\
b.  Quantas comparações podem ser necessárias no pior caso?\
c.  Qual é sua ordem de crescimento no pior caso?\
d.  Por que dizer apenas que "o algoritmo funciona" é insuficiente para
    avaliar a solução?\
e.  Que pergunta sobre a **organização dos dados** deveria ser feita
    antes de decidir que essa solução é adequada?

> Não é necessário propor ainda uma estrutura de dados específica. O
> objetivo é formular corretamente o problema que deverá orientar uma
> solução posterior.

------------------------------------------------------------------------

# Exercício 7 --- Análise de uma modificação

Um estudante propõe o seguinte algoritmo:

``` python
def buscar_duas_vezes(estudantes, matricula):
    encontrado = None

    for estudante in estudantes:
        if estudante["matricula"] == matricula:
            encontrado = estudante

    for estudante in estudantes:
        if estudante["matricula"] == matricula:
            encontrado = estudante

    return encontrado
```

Considere o pior caso.

a.  Aproximadamente quantas comparações são realizadas para uma entrada
    de tamanho `n`?\
b.  Podemos representar o custo como algo semelhante a `T(n) = 2n + b`?\
c.  Se uma busca realiza aproximadamente `n` comparações e a outra `2n`,
    ambas possuem a mesma ordem de crescimento?\
d.  Classifique `buscar_duas_vezes` usando Big-O.\
e.  Explique por que Big-O pode classificar dois algoritmos na mesma
    ordem mesmo que um execute mais operações que o outro.

------------------------------------------------------------------------

# Exercício 8 --- Mini-investigação

Utilize o `Semana-01-Estudante.ipynb` ou crie uma pequena célula
adicional.

Escolha pelo menos **cinco tamanhos de entrada**, incluindo valores
diferentes daqueles usados originalmente na aula.

Para cada tamanho:

1.  gere a coleção de estudantes;
2.  execute a busca sequencial no pior caso;
3.  registre o número de comparações;
4.  registre o tempo de execução;
5.  organize os resultados em uma tabela.

Depois responda:

a.  O número de comparações confirmou a previsão feita antes da
    execução?\
b.  O tempo cresceu exatamente na mesma proporção em todos os casos?\
c.  Os resultados alteram ou reforçam a classificação `O(n)`?\
d.  Qual é a principal evidência utilizada para justificar sua
    resposta?\
e.  Escreva uma conclusão de **quatro a seis frases** distinguindo
    comportamento experimental e ordem de crescimento.

------------------------------------------------------------------------

# Questão de fechamento da Semana 01

Considere novamente o problema original:

> **Como localizar, pela matrícula, um estudante em uma coleção de
> registros acadêmicos?**

Em um parágrafo curto, explique o caminho percorrido durante a semana
utilizando, obrigatoriamente, os seguintes termos:

**problema --- dados --- algoritmo --- tamanho da entrada --- operações
--- pior caso --- crescimento linear --- O(n) --- tempo observado ---
organização dos dados**

O parágrafo deve terminar formulando uma pergunta que justifique
investigar novas formas de organizar os dados nas semanas seguintes.

------------------------------------------------------------------------

# Orientação de uso

Estes exercícios não precisam ser realizados integralmente durante um
único encontro.

Uma seleção possível para consolidação imediata é:

-   Exercício 1 --- leitura e análise;
-   Exercício 3 --- predição;
-   Exercício 5 --- interpretação experimental;
-   Exercício 6 --- retorno ao problema.

Os Exercícios 2, 7 e 8 exigem maior manipulação de código e podem ser
utilizados conforme o ritmo da turma ou como continuidade do trabalho da
semana.

A **Questão de fechamento** é especialmente útil para verificar se o
estudante compreendeu a narrativa completa da Semana 01, e não apenas a
sintaxe da implementação.
