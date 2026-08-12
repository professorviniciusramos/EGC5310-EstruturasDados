# EGC5310 --- Semana 01 --- Soluções comentadas

**Disciplina:** EGC5310 --- Tópicos Especiais em Ciência de Dados VI\
**Semana:** 01\
**Tema:** Do problema ao custo computacional\
**Documento relacionado:** `Semana-01-Exercicios.md`\
**Uso:** material do professor

------------------------------------------------------------------------

# 1. Finalidade

Este documento apresenta soluções e comentários para os exercícios da
Semana 01.

As respostas não devem ser utilizadas apenas como gabarito. O objetivo é
registrar:

-   o raciocínio esperado;
-   respostas aceitáveis;
-   relações com os objetivos de aprendizagem;
-   erros ou confusões prováveis;
-   pontos que podem ser retomados oralmente em sala.

Nesta semana, é mais importante que o estudante compreenda a relação
entre **tamanho da entrada, operações e crescimento** do que reproduza
mecanicamente a notação Big-O.

------------------------------------------------------------------------

# Exercício 1 --- A busca passo a passo

A coleção possui seis estudantes.

## Respostas

**a. Busca por `1201`:** 1 comparação.

O elemento está na primeira posição. Este é o melhor caso.

**b. Busca por `1220`:** 4 comparações.

São examinadas, nessa ordem, as matrículas:

`1201 → 1207 → 1215 → 1220`

**c. Busca por `1248`:** 6 comparações.

A matrícula está no último registro.

**d. Busca por `9999`:** 6 comparações.

Como a matrícula não existe, todos os registros precisam ser examinados
antes que o algoritmo possa concluir que não encontrou o estudante.

**e. Melhor caso:** busca por `1201`.

O algoritmo encerra após uma comparação.

**f. Pior caso:** busca pelo último elemento ou por elemento
inexistente.

Nos dois casos, todos os seis elementos são examinados.

**g. Para `n` estudantes:** até `n` comparações no pior caso.

## Raciocínio esperado

O estudante deve perceber que a quantidade de trabalho não depende
apenas da existência do registro, mas também de sua posição.

A generalização importante é:

\[ comparações\_{`\text{pior caso}`{=tex}}=n \]

## Erro comum

Responder que uma matrícula inexistente realiza `n + 1` comparações.

Na implementação utilizada, existe uma comparação de matrícula para cada
elemento da coleção. Depois do último elemento, o laço termina; não
ocorre uma nova comparação de matrícula.

------------------------------------------------------------------------

# Exercício 2 --- Instrumentando um algoritmo

## Implementação esperada

``` python
def buscar_contando(estudantes, matricula):
    comparacoes = 0

    for estudante in estudantes:
        comparacoes += 1

        if estudante["matricula"] == matricula:
            return estudante, comparacoes

    return None, comparacoes
```

## Resultados esperados para a coleção do exercício

-   primeiro elemento (`1201`): 1 comparação;
-   elemento aproximadamente intermediário: depende do registro
    escolhido;
-   último elemento (`1248`): 6 comparações;
-   inexistente (`9999`): 6 comparações.

## Raciocínio esperado

A instrumentação não deve alterar o algoritmo que está sendo estudado.
Ela apenas adiciona uma observação sobre sua execução.

A variável `comparacoes` funciona como uma medida do trabalho relevante
para a análise proposta.

## Erros comuns

### Incrementar apenas quando encontra

Isto conta elementos encontrados, não comparações.

### Incrementar depois do `if`

Dependendo da organização do código, o estudante pode retornar antes de
registrar a comparação realizada.

### Usar tempo em vez de contador

O objetivo deste exercício é justamente construir uma medida
independente da velocidade da máquina.

------------------------------------------------------------------------

# Exercício 3 --- Antes de executar

Como a matrícula é inexistente, todos os elementos são examinados.

          n   Comparações previstas
  --------- -----------------------
         20                      20
        200                     200
      2.000                   2.000
     20.000                  20.000
    200.000                 200.000

## a. Multiplicação de n por 10

O número de comparações também é multiplicado por 10.

## b. Relação

No pior caso:

\[ comparações(n)=n \]

Portanto, o número de comparações cresce proporcionalmente ao tamanho da
entrada.

## c. Ordem

\[ O(n) \]

A justificativa esperada é que o trabalho cresce linearmente com `n`.

## Raciocínio esperado

Este exercício deve ser resolvido **antes da execução**. O objetivo é
mostrar que a análise permite prever uma propriedade do comportamento do
algoritmo.

## Ponto de mediação

Perguntar:

> "Por que conseguimos prever exatamente o número de comparações, mas
> não exatamente quantos segundos a execução levará?"

Essa pergunta prepara a distinção entre análise e benchmark.

------------------------------------------------------------------------

# Exercício 4 --- De T(n) para a ordem de crescimento

Temos:

\[ T_A(n)=4 \]

\[ T_B(n)=3n+7 \]

\[ T_C(n)=2n\^2+5n+10 \]

## Algoritmo A

O custo não depende de `n`.

Termo dominante: constante.

\[ O(1) \]

Se `n` dobra, esse modelo de custo permanece igual.

## Algoritmo B

O termo que cresce com `n` é:

\[ 3n \]

Para valores grandes de `n`, a constante `7` não altera a ordem de
crescimento.

\[ O(n) \]

Quando `n` dobra, a parcela dominante do custo aproximadamente dobra.

## Algoritmo C

O termo dominante é:

\[ 2n\^2 \]

Logo:

\[ O(n\^2) \]

Quando `n` dobra:

\[ (2n)^2=4n^2 \]

Assim, a parcela quadrática cresce aproximadamente quatro vezes.

## Raciocínio esperado

O estudante deve começar a distinguir **valor exato de T(n)** de **ordem
de crescimento**.

Nesta semana não é necessário exigir uma definição assintótica formal
com constantes e limiares.

## Erro comum

Classificar `3n + 7` como `O(3n)` ou `O(n + 7)` como se Big-O fosse
apenas uma reescrita literal da expressão.

A discussão deve enfatizar a ordem de crescimento.

------------------------------------------------------------------------

# Exercício 5 --- O cronômetro contradiz o Big-O?

## a. Tempos iguais?

Não.

Os computadores produziram tempos diferentes.

## b. Complexidades diferentes?

Não é possível concluir isso a partir dos tempos apresentados. No
enunciado, ambos executam a mesma busca sequencial no pior caso.

A ordem de crescimento permanece:

\[ O(n) \]

## c. Comparações para n = 1.000.000

Como a matrícula é inexistente:

\[ 1.000.000 \]

comparações.

## d. Informação mais apropriada

Para caracterizar a ordem de crescimento, interessa a relação entre
tamanho da entrada e quantidade de trabalho/operações relevantes.

Os segundos são evidência experimental dependente do ambiente.

## e. Compatibilidade com O(n)

Os tempos aumentam à medida que a entrada cresce, mas as razões não
precisam ser exatamente iguais.

Big-O não afirma:

> "Se n aumentar dez vezes, o programa levará exatamente dez vezes mais
> segundos."

A classificação descreve a ordem de crescimento do custo do algoritmo em
função de `n`.

## Raciocínio esperado

Este é um exercício central da semana.

O estudante deve separar:

**análise estrutural do algoritmo**

de

**medição de uma execução concreta**.

## Erro comum

Dizer que o computador A possui "complexidade menor" porque executou
mais rápido.

Uma máquina mais rápida pode reduzir o tempo absoluto sem alterar a
ordem de crescimento do algoritmo.

------------------------------------------------------------------------

# Exercício 6 --- Uma solução correta pode ser inadequada?

## a. O algoritmo pode estar correto?

Sim.

Ele pode encontrar corretamente o registro procurado e retornar o
resultado esperado.

## b. Pior caso

Para 5 milhões de registros:

\[ 5.000.000 \]

comparações.

## c. Ordem de crescimento

\[ O(n) \]

no pior caso.

## d. Por que "funciona" é insuficiente?

Correção e eficiência são propriedades diferentes.

Uma solução pode produzir a resposta correta e ainda exigir uma
quantidade de trabalho inadequada para determinado volume de dados ou
frequência de uso.

## e. Pergunta sobre organização dos dados

Respostas aceitáveis incluem formulações como:

> "Podemos organizar os estudantes de uma forma que permita localizar
> uma matrícula sem percorrer potencialmente toda a coleção?"

ou:

> "Existe uma organização dos dados mais adequada para operações
> frequentes de busca por matrícula?"

Não é necessário nomear uma estrutura específica.

## Raciocínio esperado

Este exercício reconecta análise de algoritmos ao problema da
disciplina.

O estudante não deve concluir simplesmente que `O(n)` é "ruim". A
adequação depende do problema, do volume, da frequência das operações e
das alternativas disponíveis.

## Erro comum

Responder imediatamente "usar dicionário", "usar árvore" ou outra
estrutura sem explicar qual limitação está sendo enfrentada.

Nesta etapa, a formulação correta da necessidade é mais importante que
antecipar a solução.

------------------------------------------------------------------------

# Exercício 7 --- Análise de uma modificação

O algoritmo percorre toda a coleção duas vezes.

## a. Número aproximado de comparações

\[ 2n \]

## b. Modelo

Sim. Podemos representar o custo, de maneira simplificada, como:

\[ T(n)=2n+b \]

onde `b` representa operações cujo número não cresce proporcionalmente
com a entrada.

## c. Mesma ordem?

Sim.

Uma busca com aproximadamente `n` comparações e outra com
aproximadamente `2n` comparações apresentam crescimento linear.

## d. Classificação

\[ O(n) \]

## e. Explicação

Big-O descreve a ordem de crescimento e abstrai fatores constantes na
classificação.

Assim:

\[ n `\rightarrow `{=tex}O(n) \]

e

\[ 2n `\rightarrow `{=tex}O(n) \]

Isso não significa que os dois algoritmos tenham exatamente o mesmo
custo em uma execução concreta.

## Raciocínio esperado

Este exercício é importante para impedir a interpretação de Big-O como
contador exato de operações.

Dois algoritmos podem pertencer à mesma classe de crescimento e ainda
possuir diferenças práticas relevantes.

## Erro comum

Concluir que o segundo algoritmo é `O(2n)` como classificação final.

Pode-se usar `2n` para descrever uma contagem aproximada, mas a ordem é
linear:

\[ O(n) \]

------------------------------------------------------------------------

# Exercício 8 --- Mini-investigação

Não existe uma única tabela numérica correta para o tempo, pois os
estudantes escolherão tamanhos diferentes e executarão em ambientes
diferentes.

## Resultado esperado para comparações

Para matrícula inexistente:

\[ comparações=n \]

Assim, qualquer tabela correta deverá apresentar essa correspondência.

Exemplo:

          n   Comparações      Tempo
  --------- ------------- ----------
        500           500   variável
      5.000         5.000   variável
     25.000        25.000   variável
    150.000       150.000   variável
    750.000       750.000   variável

## a. Confirmação da previsão

Sim, desde que o experimento mantenha o pior caso e a mesma
implementação.

## b. Tempo na mesma proporção?

Não necessariamente.

É provável que exista uma tendência crescente, mas os tempos podem
apresentar variações.

## c. Classificação

Os resultados reforçam a classificação:

\[ O(n) \]

## d. Evidência principal

A evidência mais direta utilizada nesta semana é que, no pior caso:

\[ comparações=n \]

e que essa relação se mantém quando `n` aumenta.

## e. Exemplo de conclusão aceitável

> O experimento mostrou que o número de comparações acompanha
> diretamente o tamanho da entrada no pior caso. Quando aumentamos a
> quantidade de estudantes, a quantidade de comparações aumentou na
> mesma proporção. Os tempos de execução também apresentaram tendência
> de crescimento, mas não mantiveram uma proporção exatamente constante
> entre todos os testes. Isso ocorre porque o tempo depende também do
> ambiente de execução. Portanto, os resultados são compatíveis com o
> crescimento linear da busca sequencial, representado por `O(n)`.

## Critério de avaliação

Não exigir tempos semelhantes ao benchmark do professor.

Resultados temporais diferentes são esperados.

A avaliação deve se concentrar na coerência do experimento e da
interpretação.

------------------------------------------------------------------------

# Questão de fechamento da Semana 01

## Exemplo de resposta

> O problema inicial era localizar um estudante pela matrícula em uma
> coleção de dados acadêmicos. Construímos um algoritmo de busca
> sequencial e analisamos como seu comportamento muda de acordo com o
> tamanho da entrada. Ao contar as operações, observamos que, no pior
> caso, o algoritmo pode realizar `n` comparações. Isso caracteriza
> crescimento linear, representado por `O(n)`. O tempo observado nos
> experimentos aumentou com entradas maiores, mas variou entre execuções
> e computadores, mostrando que tempo medido e ordem de crescimento não
> são a mesma coisa. A análise mostra que uma solução correta pode
> apresentar limitações quando o volume de dados aumenta. Assim, surge a
> pergunta: **podemos modificar a organização dos dados para realizar a
> busca com menor custo?**

## Critério de avaliação

O estudante não precisa reproduzir esta redação.

Uma resposta adequada deve estabelecer uma cadeia coerente:

**problema → dados → algoritmo → tamanho da entrada → operações → pior
caso → crescimento linear → O(n) → tempo observado → necessidade de
reconsiderar a organização dos dados.**

## Sinais de compreensão

-   distingue correção de eficiência;
-   explica `n` no contexto do problema;
-   relaciona pior caso a todos os elementos examinados;
-   interpreta `O(n)` como crescimento linear;
-   não identifica Big-O com segundos;
-   formula uma necessidade de reorganização dos dados.

------------------------------------------------------------------------

# Síntese para o professor

Ao corrigir ou discutir os exercícios, priorizar quatro ideias.

## 1. O algoritmo deve ser observado, não apenas executado

O estudante precisa conseguir explicar o que ocorre em cada passo
relevante.

## 2. n precisa ter significado concreto

Nesta semana:

> `n` = quantidade de estudantes na coleção.

Evitar que `n` seja tratado apenas como símbolo abstrato.

## 3. Big-O descreve crescimento

Nesta introdução:

-   `O(1)` --- constante;
-   `O(n)` --- linear;
-   `O(n²)` --- quadrático.

Não exigir formalização assintótica além do necessário para compreender
o crescimento.

## 4. O problema continua

A Semana 01 não deve produzir a impressão de que "busca sequencial é
ruim".

Ela deve produzir uma pergunta mais precisa:

> **Em que condições essa solução deixa de ser adequada e como a
> organização dos dados pode alterar o custo das operações?**

Essa pergunta é a ponte conceitual para o desenvolvimento posterior da
disciplina.

------------------------------------------------------------------------

# Erros conceituais a observar durante a semana

  -----------------------------------------------------------------------
  Afirmação do estudante              Intervenção sugerida
  ----------------------------------- -----------------------------------
  "O(n) significa n segundos."        Retomar a diferença entre operação
                                      e tempo observado.

  "Se meu computador foi mais rápido, Perguntar se o código e o número de
  meu algoritmo é melhor."            comparações mudaram.

  "O(n) é ruim."                      Perguntar: para qual tamanho de
                                      entrada, frequência de operação e
                                      alternativa?

  "O pior caso sempre acontece."      Explicar que pior caso caracteriza
                                      um limite/situação, não frequência
                                      de ocorrência.

  "2n é O(2n), então é outra classe." Retomar ordem de crescimento e
                                      fatores constantes.

  "Se funciona, está resolvido."      Retomar correção versus
                                      adequação/eficiência.
  -----------------------------------------------------------------------

------------------------------------------------------------------------

**Versão:** 1.0\
**Semana 01 --- EGC5310**
