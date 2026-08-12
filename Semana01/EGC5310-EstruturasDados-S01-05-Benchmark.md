# EGC5310 --- Semana 01 --- Benchmark

**Disciplina:** EGC5310 --- Tópicos Especiais em Ciência de Dados VI\
**Semana:** 01\
**Problema:** busca de um estudante pela matrícula em uma coleção de
registros acadêmicos\
**Benchmark executável:** `Semana-01-Benchmark.py`\
**Resultados de referência:** `Semana-01-Benchmark-Resultados.csv`\
**Notebook do professor:** `Semana-01-Professor.ipynb`\
**Notebook do estudante:** `Semana-01-Estudante.ipynb`

------------------------------------------------------------------------

# Antes da aula --- leitura de 2 minutos

## O que estou tentando mostrar?

O objetivo deste benchmark **não é descobrir quantos segundos a busca
sequencial demora**. O objetivo é produzir evidência experimental que
ajude os estudantes a relacionar:

**tamanho da entrada → número de operações → tempo observado → ordem de
crescimento.**

O resultado estrutural mais importante é:

> No pior caso da busca sequencial, para uma coleção com `n` estudantes,
> são realizadas `n` comparações.

Portanto:

\[ T(n) `\propto `{=tex}n \]

e descrevemos a ordem de crescimento como:

\[ O(n) \]

## O que devo fazer em sala?

1.  **Não começar pelo benchmark.** Primeiro construir e compreender a
    busca sequencial.
2.  Contar comparações com uma coleção pequena.
3.  Perguntar aos estudantes o que esperam para entradas maiores.
4.  Formalizar `n`, `T(n)` e crescimento linear.
5.  No **slide 16**, abrir `Semana-01-Professor.ipynb`, seção
    **"Experimento --- crescimento da busca sequencial"**.
6.  Antes de executar, pedir uma previsão para o número de comparações.
7.  Executar o experimento.
8.  Comparar **comparações** e **tempo observado**.
9.  Pedir aos estudantes que reproduzam o experimento no
    `Semana-01-Estudante.ipynb`.
10. Comparar coletivamente os tempos obtidos em computadores diferentes.

## O que devo esperar?

Para matrícula inexistente:

            n   Comparações esperadas
  ----------- -----------------------
        1.000                   1.000
       10.000                  10.000
      100.000                 100.000
    1.000.000               1.000.000

Quando `n` aumenta 10 vezes, o número de comparações deve aumentar
**exatamente 10 vezes**.

O tempo de execução deve apresentar tendência crescente, mas **não deve
ser esperado que aumente exatamente 10 vezes**.

## Mensagem que deve ficar para os estudantes

> **Tempo observado não é complexidade computacional.**

Computadores diferentes podem produzir tempos diferentes para o mesmo
experimento. O padrão estrutural do algoritmo permanece: no pior caso, a
busca sequencial examina `n` elementos e apresenta crescimento linear,
`O(n)`.

------------------------------------------------------------------------

# 1. Objetivo do benchmark

Este benchmark complementa o problema desenvolvido durante a Semana 01:
localizar um estudante pela matrícula em uma coleção de registros
acadêmicos.

A implementação inicial utiliza uma busca sequencial. O benchmark tem
como finalidade verificar experimentalmente como essa busca se comporta
quando o tamanho da entrada aumenta.

Especificamente, pretende-se observar:

-   a relação entre tamanho da entrada (`n`) e número de comparações;
-   o comportamento do tempo de execução à medida que `n` cresce;
-   a diferença entre uma medida experimental de tempo e uma análise da
    ordem de crescimento;
-   a relação entre o comportamento observado e a classificação `O(n)`
    da busca sequencial no pior caso.

O benchmark não deve ser tratado como uma atividade isolada. Ele faz
parte da sequência:

**problema → algoritmo → instrumentação → predição → formalização →
experimento → interpretação.**

------------------------------------------------------------------------

# 2. Hipótese

A hipótese principal é:

> **Se o tamanho da entrada `n` aumentar, o número de comparações
> realizadas pela busca sequencial crescerá linearmente no pior caso.**

Como o experimento utiliza uma matrícula inexistente, todos os registros
precisam ser examinados.

Assim, espera-se:

\[ comparações(n)=n \]

Consequentemente, se:

\[ n_2=10n_1 \]

então:

\[ comparações(n_2)=10`\cdot `{=tex}comparações(n_1) \]

Essa relação é determinística para a implementação utilizada.

O mesmo **não** deve ser exigido do tempo de execução.

------------------------------------------------------------------------

# 3. Relação com os materiais da Semana 01

## Slides

O benchmark aparece conceitualmente nos seguintes pontos:

-   **Slide 15 --- Big-O não é cronômetro:** prepara a distinção entre
    tempo observado e ordem de crescimento.
-   **Slide 16 --- Vamos experimentar:** inicia explicitamente o
    experimento.

No slide 16, a referência operacional é:

**Notebook:** `Semana-01-Professor.ipynb`\
**Seção:** `Experimento — crescimento da busca sequencial`

## Notebook do professor

As seções diretamente relacionadas são:

-   `Contando comparações`;
-   `Melhor e pior caso`;
-   `Tempo × número de operações`;
-   `Experimento — crescimento da busca sequencial`.

O notebook do professor é o instrumento principal para a demonstração em
sala.

## Notebook do estudante

Os estudantes reproduzem uma versão orientada do experimento,
completando partes da implementação e registrando interpretações.

O objetivo não é apenas obter números, mas explicar o comportamento
observado.

## Script de benchmark

O arquivo `Semana-01-Benchmark.py` é o **benchmark de referência do
professor**.

Ele não precisa ser distribuído aos estudantes nesta semana.

Sua função é:

-   validar previamente os tamanhos das entradas;
-   reproduzir o experimento de forma independente;
-   verificar o comportamento em máquinas ou versões futuras do Python;
-   gerar resultados de referência;
-   preservar uma implementação experimental estável para futuras
    ofertas.

------------------------------------------------------------------------

# 4. Preparação antes da aula

Executar:

``` bash
python Semana-01-Benchmark.py
```

Verificar se:

-   o script termina sem erros;
-   `comparacoes == n` para todos os tamanhos;
-   os tempos aumentam de forma globalmente coerente;
-   a execução para `n = 1.000.000` não compromete a fluidez da aula;
-   o consumo de memória é aceitável;
-   o arquivo `Semana-01-Benchmark-Resultados.csv` é produzido
    corretamente.

Os tamanhos atualmente previstos são:

``` text
1.000
10.000
100.000
1.000.000
```

Esses valores não são pedagogicamente obrigatórios. Podem ser reduzidos
em uma oferta futura caso o ambiente computacional torne a execução
lenta.

O que deve ser preservado é a possibilidade de observar claramente
diferentes ordens de tamanho.

------------------------------------------------------------------------

# 5. Variáveis observadas

## 5.1 Tamanho da entrada

`n` representa a quantidade de estudantes armazenados na coleção.

## 5.2 Número de comparações

É a principal medida estrutural utilizada nesta semana.

No pior caso:

\[ comparações=n \]

## 5.3 Tempo de execução

O script registra:

-   tempo mediano;
-   tempo mínimo;
-   tempo máximo.

O tempo é uma medida experimental e depende do ambiente.

Entre os fatores que podem afetá-lo estão:

-   processador;
-   memória;
-   sistema operacional;
-   versão e implementação do Python;
-   processos concorrentes;
-   gerenciamento de memória;
-   condições momentâneas da máquina.

Por isso, o tempo não deve ser interpretado como propriedade exclusiva
do algoritmo.

------------------------------------------------------------------------

# 6. Por que usar uma matrícula inexistente?

O benchmark procura a matrícula `-1`.

Os registros gerados possuem matrículas a partir de `100000`. Assim,
`-1` não pertence ao conjunto de dados.

Isso garante que o algoritmo precise examinar toda a coleção.

Logo, para uma entrada de tamanho `n`:

\[ comparações=n \]

O experimento representa, portanto, o **pior caso da busca sequencial**.

Se a geração dos dados for modificada em uma oferta futura, é necessário
verificar novamente se a matrícula usada no benchmark continua
inexistente.

------------------------------------------------------------------------

# 7. Procedimento didático em sala

## Etapa A --- Construção

Construir ou revisar a busca sequencial com uma coleção pequena.

Não introduzir o benchmark antes que os estudantes compreendam o
algoritmo.

## Etapa B --- Instrumentação

Adicionar a contagem de comparações.

Testar:

-   primeiro elemento;
-   elemento intermediário;
-   último elemento;
-   elemento inexistente.

## Etapa C --- Predição

Antes de executar entradas grandes, perguntar:

> Se tivermos 1.000 estudantes e a matrícula não existir, quantas
> comparações serão realizadas?

Depois:

> E com 10.000?

> E com 1.000.000?

Registrar ou discutir as previsões antes da execução.

## Etapa D --- Formalização

Relacionar a observação com:

\[ T(n)=a`\cdot `{=tex}n+b \]

e:

\[ T(n)`\propto `{=tex}n \]

Consolidar a ideia de ordem de crescimento:

\[ O(n) \]

## Etapa E --- Demonstração do professor

No slide 16, abrir:

`Semana-01-Professor.ipynb`

Seção:

`Experimento — crescimento da busca sequencial`

Executar o experimento.

Observar primeiro o número de comparações.

Somente depois discutir o tempo.

## Etapa F --- Reprodução pelos estudantes

Os estudantes executam:

`Semana-01-Estudante.ipynb`

Eles completam o experimento e registram os resultados.

O script `Semana-01-Benchmark.py` não é necessário para essa atividade.

## Etapa G --- Comparação coletiva

Perguntar aos estudantes quais tempos foram obtidos para as maiores
entradas.

É esperado que apareçam valores diferentes.

Em seguida, perguntar:

> Quantas comparações foram realizadas?

Para o mesmo `n` e o mesmo pior caso, a resposta deve coincidir.

Essa diferença é o ponto central da discussão.

------------------------------------------------------------------------

# 8. Resultados esperados

## Resultado estrutural

Espera-se:

            n   Comparações
  ----------- -------------
        1.000         1.000
       10.000        10.000
      100.000       100.000
    1.000.000     1.000.000

A razão esperada é:

  Transição               Razão de n   Razão das comparações
  --------------------- ------------ -----------------------
  1.000 → 10.000                  10                      10
  10.000 → 100.000                10                      10
  100.000 → 1.000.000             10                      10

## Resultado temporal

Espera-se que o tempo mediano aumente conforme `n` cresce.

Entretanto:

> **não existe expectativa de que a razão temporal seja exatamente 10.**

Ela pode ser, por exemplo, 7,8; 9,4; 11,2 ou outro valor.

Uma execução isolada também pode apresentar comportamento aparentemente
irregular.

Isso não contradiz `O(n)`.

------------------------------------------------------------------------

# 9. Perguntas de mediação

As seguintes perguntas podem ser utilizadas durante o experimento:

1.  Quantas comparações vocês esperam para `n = 100.000`?
2.  Por que conseguimos prever o número de comparações antes de
    executar?
3.  Conseguimos prever com a mesma precisão quantos segundos a execução
    levará?
4.  Por que computadores diferentes apresentam tempos diferentes?
5.  Se uma máquina executar a busca duas vezes mais rápido, o algoritmo
    deixa de ser `O(n)`?
6.  Se multiplicarmos `n` por 10, o que acontece com o número de
    comparações?
7.  O que exatamente a notação `O(n)` está descrevendo?
8.  Uma solução `O(n)` é necessariamente lenta?
9.  Para uma coleção pequena, a diferença de desempenho é importante?
10. O que muda quando imaginamos milhões de registros e muitas
    consultas?

------------------------------------------------------------------------

# 10. Interpretação correta

A conclusão esperada não é:

> "A busca sequencial demora X segundos."

Também não é:

> "Um milhão de registros é muito."

A conclusão conceitual é:

> **No pior caso da busca sequencial, o número de operações cresce
> proporcionalmente ao tamanho da entrada. Por isso, descrevemos sua
> ordem de crescimento como linear, `O(n)`. O tempo observado tende a
> refletir esse crescimento, mas é influenciado pelo ambiente de
> execução e não define a complexidade do algoritmo.**

------------------------------------------------------------------------

# 11. Resultados estranhos e como interpretá-los

## O tempo diminuiu em uma execução maior

Pode acontecer em medições isoladas.

Possíveis causas incluem:

-   ruído do sistema;
-   processos concorrentes;
-   resolução do cronômetro;
-   efeitos de cache;
-   gerenciamento de memória;
-   variação normal entre execuções.

Usar a mediana de várias execuções reduz parte desse ruído.

Não modificar a conclusão estrutural apenas por uma medição isolada.

## Os tempos dos estudantes são muito diferentes

Isso é esperado e pedagogicamente útil.

Usar a diferença para reforçar:

> máquinas diferentes → tempos diferentes;

mas:

> mesmo algoritmo + mesmo pior caso + mesmo `n` → mesmo número de
> comparações.

## O benchmark ficou lento

Reduzir os tamanhos, por exemplo para:

``` text
1.000
10.000
50.000
200.000
```

A relação conceitual deve ser preservada.

## O número de comparações não é igual a n

Verificar:

1.  se a matrícula pesquisada realmente não existe;
2.  se `buscar_contando` continua incrementando exatamente uma
    comparação por elemento examinado;
3.  se a geração dos dados foi modificada;
4.  se o algoritmo utilizado ainda é a busca sequencial original.

Esse resultado deve ser investigado antes da aula.

------------------------------------------------------------------------

# 12. O que não aprofundar nesta semana

O benchmark introduz alguns elementos metodológicos que não precisam se
transformar em novos conteúdos na Semana 01.

Não é necessário aprofundar:

-   metodologia formal de microbenchmark;
-   warm-up/aquecimento;
-   distribuição estatística dos tempos;
-   intervalos de confiança;
-   garbage collection;
-   cache de CPU;
-   complexidade de memória;
-   otimizações do interpretador;
-   comparação entre implementações de Python.

Esses elementos podem ser retomados posteriormente caso se tornem
relevantes.

Nesta semana, mediana e aquecimento pertencem principalmente à
infraestrutura do benchmark do professor.

------------------------------------------------------------------------

# 13. Critério de sucesso pedagógico

O benchmark cumpriu sua função se, ao final, o estudante conseguir
explicar algo equivalente a:

> "Na busca sequencial, se o elemento não existir ou estiver no final,
> podemos precisar examinar todos os `n` elementos. Quando `n` cresce
> dez vezes, o número de comparações também cresce dez vezes. Isso
> caracteriza crescimento linear, `O(n)`. Os segundos medidos podem
> variar entre computadores e execuções, portanto o tempo observado não
> é a própria complexidade do algoritmo."

Não é necessário que o estudante reproduza formalmente essa redação.

O importante é que consiga estabelecer corretamente a relação entre:

**entrada → operações → crescimento → Big-O → medição experimental.**

------------------------------------------------------------------------

# 14. Ponte para o problema seguinte

O benchmark não encerra o problema.

Ele deve produzir uma nova pergunta:

> **Se realizarmos muitas buscas sobre milhões de estudantes, podemos
> organizar os dados de outra maneira para reduzir o custo da
> operação?**

Essa pergunta mantém a lógica da disciplina:

**problema → solução → análise → limitação → nova necessidade.**

A estrutura de dados seguinte deve aparecer como resposta a essa
necessidade, e não como um conteúdo desconectado.

------------------------------------------------------------------------

# 15. Arquivos associados

  --------------------------------------------------------------------------
  Arquivo                                Papel
  -------------------------------------- -----------------------------------
  `Semana-01-Professor.ipynb`            condução, demonstração e
                                         experimentação em sala

  `Semana-01-Estudante.ipynb`            reprodução orientada e registro das
                                         interpretações

  `Semana-01-Benchmark.md`               documentação pedagógica e
                                         operacional do experimento

  `Semana-01-Benchmark.py`               implementação reproduzível do
                                         benchmark de referência

  `Semana-01-Benchmark-Resultados.csv`   resultados de uma execução de
                                         referência
  --------------------------------------------------------------------------

------------------------------------------------------------------------

# 16. Registro para futuras ofertas

Após a aula, registrar nesta seção observações que possam melhorar
futuras ofertas.

## Ambiente utilizado

-   Data:
-   Versão do Python:
-   Ambiente:
-   Máquina:
-   Tamanhos utilizados:

## Funcionou bem

-   

## Problemas observados

-   

## Ajustes recomendados

-   

## Observações sobre a reação dos estudantes

-   

------------------------------------------------------------------------

**Versão:** 1.0\
**Semana 01 --- EGC5310**
