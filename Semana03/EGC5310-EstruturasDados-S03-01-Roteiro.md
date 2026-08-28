# EGC5310 --- Estruturas de Dados

## Semana 03 --- Operações sobre dados: inserir, remover, ordenar e medir

**Arquivo:** `EGC5310-EstruturasDados-S03-01-Roteiro.md`\
**Carga útil planejada:** aproximadamente 160 minutos\
**Formato em teste:** Notebook Mestre + Quarto/Reveal.js + Notebook
Estudante\
**Cenário longitudinal:** Sistema Acadêmico

------------------------------------------------------------------------

## 1. Propósito da semana

A Semana 03 avança da discussão sobre **representação dos dados**,
realizada na Semana 02, para a investigação das **operações realizadas
sobre essas representações**.

A semana não deve retomar a busca sequencial como problema principal.
Esse mecanismo já foi utilizado nas semanas anteriores para introduzir
trabalho computacional, crescimento da entrada e escolha de
representação. O novo foco é mostrar que operações aparentemente simples
--- acessar, inserir, remover, atualizar, ordenar, transformar e
serializar --- podem esconder quantidades de trabalho muito diferentes.

A ideia central da semana é:

> **Não existe "o custo de uma estrutura". Existe o custo de uma
> operação, realizada sobre uma representação, dentro de uma determinada
> sequência de operações.**

A narrativa deve também desfazer uma equivalência frequente entre
`list`, `DataFrame` e JSON. Eles podem aparecer no mesmo pipeline de
dados, mas cumprem papéis diferentes.

------------------------------------------------------------------------

## 2. Relação com as semanas anteriores

### Semana 01

Pergunta predominante:

> Uma solução correta continua adequada quando a quantidade de dados
> cresce?

A busca sequencial foi utilizada para tornar o trabalho computacional
observável e introduzir qualitativamente `n`, `T(n)` e `O(n)`.

### Semana 02

Pergunta predominante:

> Como devemos representar os dados para aquilo que queremos fazer?

Foram discutidas diferentes representações e consolidada a pergunta:

> **Melhor para fazer o quê?**

A turma demonstrou familiaridade com listas e dicionários. A principal
dificuldade de programação observada foi com classes e objetos.

### Semana 03

A pergunta evolui para:

> **O que realmente acontece quando inserimos, removemos, ordenamos e
> transformamos dados --- e como o trabalho muda conforme a
> representação e a sequência de operações?**

A Semana 03 deve ampliar o repertório de complexidade sem formalizar
antecipadamente os conteúdos das semanas posteriores.

------------------------------------------------------------------------

## 3. Problema orientador

O Sistema Acadêmico não apenas consulta registros. Ao longo de um dia,
ele pode precisar:

-   receber novas matrículas;
-   cancelar matrículas;
-   atualizar informações;
-   incorporar lotes de novos registros;
-   produzir rankings;
-   filtrar estudantes;
-   agregar informações por curso;
-   receber e enviar dados para outros sistemas.

A pergunta orientadora será:

> **Essas operações têm o mesmo custo?**

A provocação inicial será uma operação aparentemente trivial:

``` python
alunos.append(novo_aluno)
```

Perguntas para a turma:

1.  O que essa linha faz?
2.  Quanto trabalho existe nela?
3.  Esse trabalho depende do tamanho de `alunos`?
4.  Uma linha de código significa uma operação de custo constante?

A aula deve evitar responder imediatamente. A intenção é construir a
resposta progressivamente.

------------------------------------------------------------------------

## 4. Resultados de aprendizagem

Ao final da semana, o estudante deverá ser capaz de:

1.  distinguir representação de dados de operação realizada sobre os
    dados;
2.  identificar operações predominantes em um problema de manipulação de
    dados;
3.  explicar por que número de linhas de código não representa
    quantidade de trabalho computacional;
4.  explicar qualitativamente por que a posição afeta inserções e
    remoções em uma lista;
5.  compreender, em nível introdutório, a diferença entre tamanho e
    capacidade de uma lista dinâmica;
6.  reconhecer `append()` como uma operação de custo amortizado
    constante, sem necessidade de demonstrar formalmente análise
    amortizada;
7.  relacionar acesso, inserção, remoção e ordenação a diferentes
    padrões de crescimento;
8.  perceber que uma sequência de operações pode produzir custo muito
    diferente de outra sequência que alcança o mesmo resultado;
9.  formular hipóteses antes de executar um benchmark;
10. interpretar resultados experimentais sem confundir tempo medido com
    complexidade assintótica;
11. explicar por que duas implementações `O(n)` podem apresentar tempos
    muito diferentes;
12. explicar por que DataFrames são particularmente importantes para
    processamento tabular e operações em lote;
13. reconhecer situações em que uma lista simples é mais natural que um
    DataFrame;
14. distinguir JSON como formato de representação/intercâmbio das
    estruturas utilizadas para processamento em memória;
15. compreender que é possível discutir complexidade das operações
    envolvendo DataFrames e JSON, mas que não existe "o Big-O do
    DataFrame" ou "o Big-O do JSON";
16. escolher uma representação de maneira preliminar a partir das
    operações predominantes no problema.

------------------------------------------------------------------------

## 5. Conceitos que serão introduzidos sem aprofundamento formal

Alguns conceitos devem aparecer porque ajudam a explicar os fenômenos
observados, mas não serão esgotados nesta semana:

-   array dinâmico;
-   tamanho e capacidade;
-   realocação;
-   deslocamento de elementos;
-   custo amortizado;
-   `O(n log n)` como classe associada a algoritmos eficientes de
    ordenação;
-   `O(n²)` produzido por repetição de operações crescentes;
-   processamento em lote;
-   vetorização;
-   constantes ocultas pela notação assintótica;
-   serialização e desserialização.

A regra didática será:

> **mostrar o mecanismo → nomear o fenômeno → medir o efeito → adiar a
> formalização que pertence a conteúdos futuros.**

Não serão aprofundados nesta semana:

-   implementação interna completa de `list` no CPython;
-   prova de análise amortizada;
-   Timsort;
-   algoritmos específicos de ordenação;
-   busca binária;
-   hashing;
-   árvores;
-   índices;
-   internals do pandas;
-   detalhes de I/O e sistemas de armazenamento.

------------------------------------------------------------------------

# 6. Narrativa didática detalhada

## Movimento 1 --- Uma linha de código pode esconder muito trabalho

**Tempo de referência: 15 min**

### Objetivo

Romper a associação entre quantidade de código escrito e quantidade de
trabalho executado.

### Sequência

Apresentar:

``` python
alunos.append(novo_aluno)
```

Depois:

``` python
alunos.insert(0, novo_aluno)
```

As duas instruções possuem aparência semelhante e ocupam uma linha.

Perguntar:

-   Fazem a mesma quantidade de trabalho?
-   O tamanho da lista interfere?
-   O local da inserção interfere?

### Mensagem de transição

> Para responder, precisamos olhar um pouco abaixo da interface
> oferecida pelo Python.

------------------------------------------------------------------------

## Movimento 2 --- Abrindo a caixa-preta da `list`

**Tempo de referência: 25 min**

### 2.1 Acesso por posição

Representar visualmente uma lista com índices.

``` python
alunos[2]
```

Explicar qualitativamente que, conhecida a posição, o acesso não exige
percorrer os elementos anteriores.

Associar:

`O(1)`.

Não transformar esse momento em revisão extensa de Big-O.

### 2.2 Inserção ao final

``` python
alunos.append(novo_aluno)
```

Introduzir a distinção:

-   tamanho utilizado;
-   capacidade disponível.

Representação conceitual:

``` text
tamanho = 3
capacidade = 5

[A][B][C][ ][ ]
```

### 2.3 Quando a capacidade termina

Mostrar conceitualmente:

``` text
[A][B][C][D]
```

e a chegada de `E`.

Explicar, sem detalhes de implementação:

1.  a estrutura precisa obter mais espaço;
2.  referências existentes precisam ser transferidas;
3.  o novo elemento é incorporado.

Introduzir o termo **custo amortizado**.

Mensagem:

> A maioria dos `append()` é muito barata. Algumas inserções ocasionais
> precisam realizar mais trabalho. Quando analisamos uma sequência
> longa, tratamos `append()` como `O(1)` amortizado.

Não demonstrar matematicamente.

### 2.4 Inserção no início

``` python
alunos.insert(0, novo_aluno)
```

Mostrar o deslocamento conceitual:

``` text
[A][B][C][D]

 →  →  →  →
[ ][A][B][C][D]

[X][A][B][C][D]
```

Perguntar:

> Se há `n` elementos, quantos podem precisar mudar de posição?

Associar qualitativamente a `O(n)`.

### Síntese intermediária

> **Uma linha de código não corresponde a uma quantidade fixa de
> trabalho.**

------------------------------------------------------------------------

## Movimento 3 --- Remover também depende da posição

**Tempo de referência: 15 min**

Comparar:

``` python
alunos.pop()
```

e:

``` python
alunos.pop(0)
```

Mostrar visualmente por que remover do início pode exigir deslocamentos.

Construir com a turma a primeira tabela, contendo apenas operações já
investigadas:

  ------------------------------------------------------------------------
  Operação                    Comportamento esperado Mecanismo principal
  --------------------- ---------------------------- ---------------------
  `lista[i]`                                  `O(1)` acesso por posição

  `append(x)`                      `O(1)` amortizado inserção no final +
                                                     crescimento ocasional

  `insert(0, x)`                              `O(n)` deslocamento

  `pop()`                                     `O(1)` remoção no final

  `pop(0)`                                    `O(n)` deslocamento
  ------------------------------------------------------------------------

A tabela deve ser consequência da investigação, e não conteúdo
apresentado antecipadamente.

------------------------------------------------------------------------

## Movimento 4 --- Notebook Estudante: prever antes de medir

**Tempo de referência: 20 min**

### Chamada visual obrigatória

A apresentação e o Notebook Mestre devem indicar explicitamente:

> **Abra agora o Notebook Estudante --- Atividade 1.**

O botão/link para o Notebook Estudante deve existir também no Notebook
Mestre.

### Atividade

Sem executar inicialmente, os estudantes devem comparar:

``` python
lista.append(x)
lista.insert(0, x)
lista.pop()
lista.pop(0)
```

para coleções crescentes.

Perguntas:

1.  Qual operação deve variar menos com `n`?
2.  Qual deve crescer com `n`?
3.  Qual mecanismo explica a previsão?
4.  O que esperam encontrar experimentalmente?

A previsão deve ser registrada antes da execução.

### Ponto natural de interrupção

Este é um possível ponto de encerramento do primeiro encontro. Se isso
ocorrer, a retomada seguinte deve ser:

> **Ontem construímos hipóteses. Agora vamos produzir evidências.**

Não é necessário exigir dos estudantes uma navegação explícita de
retorno à apresentação. Após a atividade, o professor retoma a projeção
e a turma acompanha.

------------------------------------------------------------------------

## Movimento 5 --- Operações formam processos

**Tempo de referência: 20 min**

Introduzir um ranking de estudantes.

``` python
ranking = [
    {"nome": "Ana", "nota": 9.5},
    {"nome": "Bruno", "nota": 8.7},
    {"nome": "Carla", "nota": 8.2},
]
```

Chega um novo estudante.

Uma solução correta:

``` python
ranking.append(novo_aluno)
ranking.sort(...)
```

Perguntar:

> Funciona?

Sim.

Depois:

> O fato de funcionar significa que devemos executar essa estratégia
> depois de cada nova inserção?

### Ordenação tem custo

Explicar apenas:

``` text
dados desordenados
       ↓
algoritmo de ordenação
       ↓
dados ordenados
```

Não ensinar algoritmo de ordenação nesta semana.

Apresentar `O(n log n)` apenas como uma classe típica de algoritmos
eficientes de ordenação e como elemento que será aprofundado
posteriormente.

------------------------------------------------------------------------

## Movimento 6 --- Critério de ordenação e microintrodução a `lambda`

**Tempo de referência: 10 min**

Como a turma está no segundo semestre, `lambda` não deve aparecer sem
explicação.

### Primeiro: função nomeada

``` python
def obter_nota(aluno):
    return aluno["nota"]

ranking.sort(
    key=obter_nota,
    reverse=True
)
```

Explicar:

-   `key` recebe uma função;
-   essa função informa qual valor deve ser utilizado como critério;
-   `reverse=True` solicita ordem decrescente.

### Depois: função `lambda`

Mostrar a equivalência:

``` python
def obter_nota(aluno):
    return aluno["nota"]
```

e:

``` python
lambda aluno: aluno["nota"]
```

Explicação mínima:

> Uma `lambda` é uma pequena função sem nome. Neste exemplo, recebe
> `aluno` e devolve `aluno["nota"]`.

Representar:

``` text
lambda aluno: aluno["nota"]
       ↑             ↑
    entrada        saída
```

Então:

``` python
ranking.sort(
    key=lambda aluno: aluno["nota"],
    reverse=True
)
```

Não introduzir programação funcional, closures ou conceitos adicionais.

------------------------------------------------------------------------

## Movimento 7 --- A sequência de operações também importa

**Tempo de referência: 15 min**

### Estratégia A

``` python
for aluno in novos_alunos:
    ranking.append(aluno)
    ranking.sort(
        key=lambda x: x["nota"],
        reverse=True
    )
```

### Estratégia B

``` python
for aluno in novos_alunos:
    ranking.append(aluno)

ranking.sort(
    key=lambda x: x["nota"],
    reverse=True
)
```

Perguntas:

-   ambas produzem o resultado desejado?
-   o que a primeira estratégia repete?
-   o número de ordenações é igual?
-   o que deve acontecer quando a quantidade de novos registros cresce?

Mensagem:

> **O desempenho depende da estrutura, da operação e também da sequência
> de operações.**

------------------------------------------------------------------------

# 7. Benchmark da semana

**Tempo de referência: 30 min**

O benchmark é parte central da narrativa da S03.

Não deve ser tratado como material complementar.

## 7.1 Princípios experimentais

Antes de executar, discutir brevemente:

-   variar `n`;
-   repetir medições;
-   evitar concluir a partir de uma única execução;
-   manter condições comparáveis;
-   registrar os resultados;
-   observar tendência, e não apenas um valor;
-   distinguir tempo medido de complexidade.

Reforçar:

> Big-O descreve crescimento. O cronômetro mede uma execução concreta.

## 7.2 Experimento A --- posição da inserção

Comparar:

``` python
lista.append(x)
```

com:

``` python
lista.insert(0, x)
```

Pergunta:

> A diferença aumenta conforme `n` cresce?

## 7.3 Experimento B --- posição da remoção

Comparar:

``` python
lista.pop()
```

com:

``` python
lista.pop(0)
```

## 7.4 Experimento C --- DataFrame registro a registro × lote

Este experimento deve ser o mais marcante da semana.

Estratégia incremental:

``` python
for aluno in novos_alunos:
    novo_df = pd.DataFrame([aluno])
    df = pd.concat([df, novo_df], ignore_index=True)
```

Estratégia em lote:

``` python
df = pd.DataFrame(novos_alunos)
```

ou, quando houver dados anteriores:

``` python
novos_df = pd.DataFrame(novos_alunos)
df = pd.concat([df, novos_df], ignore_index=True)
```

Tamanhos iniciais candidatos:

``` text
100
1.000
5.000
10.000
```

Os valores definitivos devem ser validados no desenvolvimento do
benchmark para evitar tempos excessivos.

## 7.5 Resultados

O benchmark deve produzir CSV e permitir tabela/gráfico no Notebook
Mestre.

Perguntas de interpretação:

1.  Qual diferença apareceu?
2.  Ela aumentou com `n`?
3.  Houve ruído?
4.  O resultado é compatível com o mecanismo discutido?
5.  Um resultado mais rápido significa automaticamente uma classe Big-O
    melhor?

------------------------------------------------------------------------

# 8. DataFrame: por que ele é tão importante em Ciência de Dados?

**Tempo de referência: 15 min**

Introduzir a provocação:

> **"Professor, eu usaria um DataFrame."**

Em seguida:

> **Por que DataFrame aparece tão frequentemente em Ciência de Dados?**

Mostrar uma estrutura tabular:

``` text
             variáveis
          ↓       ↓       ↓
       nome     curso    nota
      ┌────────┬───────┬──────┐
linha │ Ana    │ CD    │ 8.5  │
linha │ Bruno  │ CC    │ 7.2  │
linha │ Carla  │ CD    │ 9.1  │
      └────────┴───────┴──────┘
```

Operações naturais:

``` python
df["nota"].mean()
df[df["nota"] >= 7]
df.groupby("curso")["nota"].mean()
df.sort_values("nota")
```

Mensagem:

> DataFrame é uma abstração voltada ao processamento de dados tabulares.
> Muitas operações frequentes de análise já fazem parte diretamente de
> sua interface.

------------------------------------------------------------------------

## 9. List × DataFrame: Big-O e tempo não são a mesma coisa

Comparar:

``` python
for aluno in alunos:
    aluno["nota"] += 1
```

com uma operação sobre coluna:

``` python
df["nota"] += 1
```

Ambas precisam processar `n` notas.

Em uma análise simplificada:

``` text
list       → O(n)
DataFrame  → O(n)
```

Perguntar:

> Se ambos são `O(n)`, por que os tempos podem ser muito diferentes?

Introduzir:

``` text
Lista Python      T(n) ≈ a · n
DataFrame         T(n) ≈ b · n
```

As constantes `a` e `b` podem ser muito diferentes.

Explicar qualitativamente:

-   loops escritos em Python possuem overhead;
-   DataFrames se apoiam em estruturas tabulares especializadas;
-   várias operações são executadas em código compilado;
-   operações vetorizadas evitam parte do trabalho realizado elemento a
    elemento no interpretador.

Mensagem:

> **Big-O descreve como o custo cresce; não determina sozinho o tempo de
> execução.**

Evitar afirmar que DataFrame é sempre mais rápido.

------------------------------------------------------------------------

# 10. Por que operações em lote são importantes?

Contrastar:

``` text
criar 1 linha
concatenar
criar 1 linha
concatenar
...
```

com:

``` text
100.000 registros
       ↓
construir estrutura tabular
       ↓
processar em conjunto
```

Mostrar uma simplificação didática para concatenações repetidas, quando
cada nova concatenação precisa lidar com uma quantidade crescente de
dados:

``` text
1 + 2 + 3 + ... + n
```

Isso permite apresentar um primeiro caso significativo de comportamento
quadrático:

`O(n²)`.

Em contraste, acumular os dados em uma lista:

``` python
dados = []

for aluno in novos_alunos:
    dados.append(aluno)

df = pd.DataFrame(dados)
```

pode ser compreendido, em um modelo simplificado, como:

``` text
n inserções amortizadas → O(n)
construção tabular      → O(n)
```

Mensagem:

> **O(n) + O(n) continua O(n).**

Ressaltar que essa é uma modelagem didática do comportamento e não uma
especificação completa dos internals do pandas.

------------------------------------------------------------------------

# 11. Então List ou DataFrame?

Evitar a pergunta:

> "Qual é mais rápido?"

Substituir por:

> **Qual representação é mais adequada para as operações
> predominantes?**

Construir a comparação:

  -----------------------------------------------------------------------
  Necessidade             `list`                  `DataFrame`
  ----------------------- ----------------------- -----------------------
  adicionar registros     natural                 geralmente não é o uso
  individualmente                                 ideal

  acesso posicional       natural                 disponível

  manipular objetos       natural                 possível
  individualmente                                 

  operação sobre coluna   manual                  natural
  inteira                                         

  filtrar dados tabulares implementação explícita operação nativa

  agregações              implementação explícita operação nativa

  agrupamento             implementação explícita operação nativa

  ordenação               disponível              disponível

  estruturas heterogêneas muito flexível          orientado ao modelo
                                                  tabular

  análise tabular         possível                finalidade central
  -----------------------------------------------------------------------

A tabela deve ser interpretada como guia conceitual, não como regra
absoluta.

------------------------------------------------------------------------

# 12. JSON: uma categoria diferente

**Tempo de referência: 10 min**

Apresentar:

``` json
[
  {"matricula": 101, "nome": "Ana"},
  {"matricula": 102, "nome": "Bruno"}
]
```

Perguntar:

> **Qual é o Big-O do JSON?**

Resposta:

> A pergunta, isoladamente, está mal formulada.

Explicar que JSON é um formato de representação/intercâmbio.

Em Python:

``` python
dados = json.loads(texto_json)
```

O resultado pode ser composto por:

``` text
list
 └── dict
      ├── str
      ├── int
      └── ...
```

A partir daí, operações em memória ocorrem sobre essas estruturas.

------------------------------------------------------------------------

## 12.1 O trabalho envolvendo JSON

Apresentar o pipeline:

``` text
arquivo / mensagem JSON
          ↓
        leitura
          ↓
        parsing
          ↓
  estruturas em memória
          ↓
      manipulação
          ↓
     serialização
          ↓
        escrita
```

Em nível introdutório, para um documento textual de tamanho `m`, ler e
interpretar seu conteúdo exige trabalho aproximadamente proporcional ao
tamanho do documento:

`O(m)`.

A serialização também precisa percorrer os dados que serão produzidos.

Não aprofundar I/O.

------------------------------------------------------------------------

# 13. Um pipeline real pode usar os três

Amarrar as representações em um único cenário.

Uma API fornece:

``` json
[
  {"matricula": 101, "curso": "CD", "nota": 8.7},
  {"matricula": 102, "curso": "CC", "nota": 7.9}
]
```

Recebimento:

``` text
JSON
 ↓
desserialização
 ↓
list de dict
```

Manipulação incremental:

``` python
dados.append(novo_aluno)
```

Análise tabular:

``` python
df = pd.DataFrame(dados)

df.groupby("curso")["nota"].mean()
```

Intercâmbio posterior:

``` text
DataFrame
 ↓
serialização
 ↓
JSON
 ↓
outro sistema
```

Mensagem:

> **Não existe um vencedor entre List, DataFrame e JSON. Eles podem
> cumprir funções diferentes no mesmo pipeline.**

------------------------------------------------------------------------

# 14. Formalização da semana

**Tempo de referência: 10 min**

Construir com a turma:

  ------------------------------------------------------------------------
  Operação / situação          Modelo de crescimento Observação
  --------------------- ---------------------------- ---------------------
  acesso `lista[i]`                           `O(1)` posição conhecida

  `list.append()`                  `O(1)` amortizado crescimento ocasional

  `list.insert(0,x)`                          `O(n)` deslocamentos

  `list.pop()`                                `O(1)` final

  `list.pop(0)`                               `O(n)` deslocamentos

  percurso de `n`                             `O(n)` todos são visitados
  registros                                          

  operação vetorizada       `O(n)` em modelo simples constantes podem ser
  sobre `n` valores                                  menores

  ordenação eficiente            `O(n log n)` típico aprofundamento
                                                     posterior

  concatenações               pode aproximar `O(n²)` sequência de
  crescentes repetidas                               operações

  parsing de documento        aproximadamente `O(m)` `m` = tamanho do
  JSON                                               documento
  ------------------------------------------------------------------------

Ressaltar:

> A tabela descreve operações e modelos simplificados. Não existe "o
> Big-O da List", "o Big-O do DataFrame" ou "o Big-O do JSON".

------------------------------------------------------------------------

# 15. Fechamento

Retomar o Sistema Acadêmico:

> Quais operações dominam o sistema?

Possibilidades:

-   receber matrículas;
-   cancelar matrículas;
-   atualizar notas;
-   consultar matrícula;
-   ordenar rankings;
-   agrupar por turma;
-   exportar informações.

Pergunta final:

> **Se conhecemos as operações predominantes, podemos organizar os dados
> para favorecer justamente essas operações?**

Em seguida:

> Se consultar matrícula ocorrer milhões de vezes, ainda queremos
> percorrer os estudantes?

Não resolver nesta semana.

Ponte explícita:

**Semana 04 --- Busca sequencial × busca binária.**

------------------------------------------------------------------------

# 16. Estrutura prevista do Notebook Mestre / apresentação

A estrutura de referência é de aproximadamente 45--47 slides,
majoritariamente leves, cada um dedicado a uma ideia, pergunta,
diagrama, código ou atividade.

## Bloco A --- Abertura

1.  Semana 03 --- título
2.  De onde estamos vindo?
3.  Sistema Acadêmico em funcionamento
4.  `append()` parece simples

## Bloco B --- Caixa-preta da lista

5.  Lista e posições
6.  Acesso por posição
7.  Inserção no final
8.  Tamanho × capacidade
9.  Quando a capacidade termina
10. Custo amortizado
11. Inserção no início
12. Deslocamentos
13. Uma linha ≠ uma quantidade de trabalho

## Bloco C --- Remoção

14. `pop()`
15. `pop(0)`
16. Primeira tabela construída

## Bloco D --- Atividade

17. Notebook Estudante --- prever antes de medir

## Bloco E --- Sequências de operações

18. Chegam novos estudantes
19. Inserir e ordenar
20. Ordenar também é trabalho
21. Função de critério com `def`
22. O que a função de critério faz?
23. `lambda` como forma compacta
24. Ordenar após cada inserção
25. Ordenar uma vez ao final
26. Estrutura + operação + sequência

## Bloco F --- Benchmark

27. Hipóteses do benchmark
28. Como medir
29. Experimento: inserção
30. Experimento: remoção
31. Resultados e interpretação inicial

## Bloco G --- DataFrame

32. "Professor, eu usaria DataFrame"
33. Por que DataFrame é central em Ciência de Dados?
34. Operações tabulares
35. List × DataFrame: ambos podem ser `O(n)`
36. Se ambos são `O(n)`, por que os tempos diferem?
37. DataFrame é sempre melhor?
38. Registro a registro × lote
39. De onde pode surgir `O(n²)`?
40. Benchmark DataFrame incremental × lote

## Bloco H --- JSON

41. "E JSON?"
42. JSON não ocupa o mesmo papel
43. O trabalho escondido no JSON
44. Pipeline JSON → list/dict → DataFrame → JSON

## Bloco I --- Síntese

45. Então qual representação usar?
46. Não existe "o Big-O da estrutura"
47. Ponte para a Semana 04

A numeração poderá sofrer pequenos ajustes durante a implementação do
Notebook Mestre, sem alterar a narrativa.

------------------------------------------------------------------------

# 17. Distribuição dos aproximadamente 160 minutos

  Movimento                            Tempo de referência
  ---------------------------------- ---------------------
  Problema + `append` × `insert`                    15 min
  Caixa-preta da `list`                             25 min
  Remoção                                           15 min
  Notebook Estudante: previsão                      20 min
  Operações + ordenação + `lambda`                  25 min
  Benchmark                                         30 min
  DataFrame + operações em lote                     15 min
  JSON + pipeline                                   10 min
  Síntese e ponte                                    5 min
  **Total**                                    **160 min**

Os tempos são referências. A discussão produzida pelos experimentos tem
prioridade sobre o cumprimento mecânico do número de slides.

------------------------------------------------------------------------

# 18. Regras de implementação para o Notebook Mestre

1.  O Notebook Mestre continua sendo a fonte de conteúdo e apresentação.
2.  Não inserir configuração `format` no notebook.
3.  Preservar a configuração Quarto/Reveal.js já validada externamente
    no projeto.
4.  Não duplicar células de código apenas para apresentar a saída.
5.  Sempre que possível, uma única célula deve apresentar código e
    resultado.
6.  Código projetado deve ser curto e legível.
7.  Explicações mais longas devem ser divididas em slides.
8.  Cada slide deve ter uma função predominante: pergunta, mecanismo,
    código, resultado ou síntese.
9.  Toda atividade no Notebook Estudante deve possuir chamada visual
    explícita.
10. O botão/link para o Notebook Estudante também deve aparecer no
    Notebook Mestre.
11. Não exigir uma "transição de volta" por parte dos estudantes; após a
    atividade, o professor retoma a projeção.
12. Previsões devem anteceder execuções experimentais.
13. Resultados de benchmark não devem ser apresentados antes da
    formulação das hipóteses.
14. Evitar classes e objetos próprios nesta semana, pois essa foi a
    principal dificuldade de Python observada na S02.
15. Utilizar prioritariamente `list`, `dict`, funções simples, pandas e
    JSON.

------------------------------------------------------------------------

# 19. Evidências da Semana 02 incorporadas

A S03 incorpora explicitamente as seguintes observações da execução da
S02:

-   a retomada da semana anterior funcionou;
-   a pergunta sobre representação foi compreendida;
-   a progressão problema → dados → operações → representação ficou
    clara;
-   a introdução qualitativa ao custo foi suficiente;
-   não houve tempo para explorar adequadamente o fechamento;
-   as chamadas visuais para o Notebook Estudante foram percebidas;
-   a abertura do Notebook Estudante ocorreu no momento correto;
-   a previsão antes da execução funcionou;
-   listas e dicionários eram familiares;
-   classes e objetos produziram dificuldade;
-   os últimos cinco slides não foram explorados adequadamente;
-   o benchmark não foi realizado;
-   exercícios extras não foram realizados;
-   código duplicado no slide apenas para mostrar saída prejudicou a
    apresentação;
-   o Notebook Mestre + Quarto funcionou razoavelmente e merece mais um
    teste;
-   o acesso ao Notebook Estudante deve aparecer também no Notebook
    Mestre;
-   os estudantes não realizam uma transição explícita de volta à
    apresentação: acompanham a projeção do professor.

Essas evidências justificam:

-   mais código concreto e menos repetição conceitual;
-   benchmark incorporado ao núcleo da aula;
-   menor dependência de classes;
-   atividades de previsão mantidas;
-   eliminação de código duplicado;
-   continuidade do teste Notebook Mestre + Quarto;
-   maior atenção ao tempo efetivamente gasto na exploração.

------------------------------------------------------------------------

# 20. Artefatos previstos para a Semana 03

1.  `EGC5310-EstruturasDados-S03-01-Roteiro.md`
2.  apresentação derivada do Notebook Mestre via Quarto/Reveal.js; PPTX
    apenas se houver necessidade posterior
3.  `EGC5310-EstruturasDados-S03-03-Aula.ipynb`
4.  `EGC5310-EstruturasDados-S03-04-Estudante.ipynb`
5.  `EGC5310-EstruturasDados-S03-05-Benchmark.py`
6.  `EGC5310-EstruturasDados-S03-05-Benchmark.csv`
7.  `EGC5310-EstruturasDados-S03-05-Benchmark.md`
8.  `EGC5310-EstruturasDados-S03-06-Exercicios.md`
9.  `EGC5310-EstruturasDados-S03-07-Solucoes.md`
10. `EGC5310-EstruturasDados-S03-08-Revisao.md`

------------------------------------------------------------------------

# 21. Critérios para considerar a semana bem-sucedida

Ao final da S03, a turma não precisa dominar internals de Python ou
pandas.

A semana terá cumprido seu papel se os estudantes conseguirem
argumentar, com exemplos, que:

> `append()` e `insert(0, ...)` parecem semelhantes no código, mas não
> realizam o mesmo trabalho.

> A posição de inserção ou remoção pode alterar o custo de uma operação.

> Ordenar repetidamente pode ser muito diferente de ordenar uma única
> vez.

> Uma lista pode ser mais natural para crescimento incremental, enquanto
> um DataFrame é especialmente adequado a operações tabulares e em lote.

> Duas soluções podem ser `O(n)` e ainda apresentar tempos bastante
> diferentes.

> JSON não é um substituto direto para `list` ou `DataFrame`; ele cumpre
> principalmente papel de representação e intercâmbio.

> Para escolher uma representação, é necessário conhecer as operações
> predominantes.

Essa compreensão constitui a base para avançar, na Semana 04, para
algoritmos de busca e para a relação entre organização dos dados e
eficiência de recuperação.
