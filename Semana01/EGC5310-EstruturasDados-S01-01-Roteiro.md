# EGC5310 --- Semana 01 --- Roteiro Didático

## Do problema ao custo computacional

**Disciplina:** EGC5310 --- Tópicos Especiais em Ciência de Dados VI\
**Semestre:** 2026/2\
**Carga semanal prevista:** 4 h-aula, distribuídas em dois encontros\
**Tempo didático de referência:** aproximadamente 80 minutos úteis por
encontro\
**Cenário longitudinal desta etapa:** Sistema acadêmico\
**Ambiente computacional:** Google Colab\
**Unidade didática:** a semana, e não cada encontro isoladamente

------------------------------------------------------------------------

# 1. Finalidade deste roteiro

Este documento orienta a condução da **Semana 01 como uma única
sequência didática contínua**.

Os dois encontros não são organizados como "aula teórica" e "aula
prática", nem possuem conteúdos que precisem obrigatoriamente começar ou
terminar em um dia específico.

A lógica é:

> **começar a narrativa no primeiro encontro, avançar conforme o ritmo
> real da turma e, no encontro seguinte, continuar exatamente do ponto
> em que ela foi interrompida.**

Os tempos apresentados neste roteiro são referências de planejamento,
não blocos rígidos.

Na primeira oferta, particularmente nesta semana, também serão
observados:

-   nível de programação dos estudantes;
-   familiaridade com Python;
-   facilidade de acesso ao Google Colab;
-   ritmo de discussão;
-   tempo necessário para atividades;
-   funcionamento de duplas/trios;
-   adequação dos slides e notebooks;
-   fluidez da alternância entre apresentação, discussão e código.

Portanto, **não é obrigatório concluir todo o conteúdo previsto na
Semana 01**.

Se uma atividade revelar uma dificuldade relevante ou produzir uma
discussão pedagogicamente útil, ela pode receber mais tempo.

------------------------------------------------------------------------

# 2. Relação com o Plano de Ensino

O Plano de Ensino caracteriza a Semana 01 como:

> **Apresentação da disciplina. Diagnóstico. Introdução aos problemas de
> manipulação de dados.**

A busca sequencial é utilizada nesta semana como **problema introdutório
e instrumento para observar custo computacional**.

Seu uso aqui não substitui o tratamento sistemático de busca previsto
posteriormente no cronograma da disciplina. A comparação formal entre
estratégias de busca, incluindo busca binária, permanece para a etapa
correspondente do semestre.

Nesta semana, a busca sequencial serve para construir a primeira cadeia
de raciocínio da disciplina:

> **problema → solução → operações → custo → crescimento → limitação**

------------------------------------------------------------------------

# 3. Objetivos de aprendizagem da Semana 01

Ao final da sequência --- ainda que parte dela precise continuar no
início da semana seguinte --- espera-se que o estudante seja capaz de:

1.  reconhecer que uma solução computacional deve ser avaliada não
    apenas pela correção, mas também pelo trabalho necessário para
    executá-la;
2.  identificar o tamanho da entrada de um problema;
3.  explicar o funcionamento de uma busca sequencial simples;
4.  contar comparações realizadas pelo algoritmo;
5.  distinguir intuitivamente melhor e pior caso;
6.  compreender `T(n)` como uma forma de descrever o custo em função do
    tamanho da entrada;
7.  reconhecer crescimento linear e relacioná-lo a `O(n)`;
8.  diferenciar tempo de execução observado de ordem de crescimento;
9.  formular uma hipótese sobre o comportamento do algoritmo e testá-la
    experimentalmente;
10. perceber que a maneira como os dados são organizados pode
    influenciar o custo das operações.

Não é objetivo da Semana 01:

-   memorizar tabelas de complexidade;
-   dominar formalmente análise assintótica;
-   estudar todas as estruturas de dados;
-   comparar sistematicamente busca sequencial e busca binária;
-   aprofundar metodologia de benchmarking;
-   dominar ferramentas de Git/GitHub.

------------------------------------------------------------------------

# 4. Problema orientador

O cenário é um **sistema acadêmico**.

Existe uma coleção de registros de estudantes contendo, entre outros
atributos:

-   matrícula;
-   nome;
-   curso.

O problema inicial é:

> **Como localizar, pela matrícula, um estudante em uma coleção de
> registros acadêmicos?**

A matrícula utilizada nos primeiros exemplos pode ser `1082`.

O problema deve aparecer antes de qualquer definição abstrata de
estrutura de dados ou complexidade.

------------------------------------------------------------------------

# 5. Pergunta central da semana

A pergunta mais ampla que orienta a narrativa é:

> **Quando uma solução que funciona deixa de ser uma boa solução?**

Ela deve permitir que o professor introduza experiências e exemplos
reais relacionados a:

-   crescimento do volume de dados;
-   aumento da frequência de consultas;
-   soluções simples que funcionam em pequena escala;
-   necessidade de reorganizar dados ou algoritmos quando o problema
    cresce.

------------------------------------------------------------------------

# 6. Materiais utilizados

## 6.1 Apresentação institucional

`EGC5310-Apresentacao-Disciplina.pptx`

Utilizada no início do primeiro encontro para:

-   apresentar a disciplina;
-   apresentar o professor;
-   explicar objetivos e metodologia;
-   mostrar avaliação;
-   explicar frequência;
-   apresentar AVA e Google Colab;
-   indicar os principais marcos do semestre.

Esta apresentação é independente do conteúdo da Semana 01.

## 6.2 Slides da Semana 01

`Semana-01-Slides.pptx`

São **17 slides que constituem uma sequência única para toda a semana**.

A apresentação pode ser interrompida em qualquer ponto.

Não existe:

-   "último slide da quinta";
-   "primeiro slide da sexta";
-   obrigação de concluir determinado conjunto em cada encontro.

## 6.3 Notebook do professor

`Semana-01-Notebook-Professor.ipynb`

É a versão completa utilizada pelo professor no Google Colab.

## 6.4 Notebook do estudante

`Semana-01-Notebook-Estudante.ipynb`

Possui:

-   `TODO`s;
-   tarefas orientadas;
-   espaços de interpretação;
-   experimentos;
-   conclusão.

## 6.5 Exercícios

`Semana-01-Exercicios.md`

Os exercícios não constituem obrigatoriamente uma lista aplicada ao
final.

Alguns devem ser usados como **paradas de aprendizagem** dentro da
narrativa.

## 6.6 Benchmark

`Semana-01-Benchmark.md`\
`Semana-01-Benchmark.py`

O benchmark completo é principalmente infraestrutura e documentação do
professor.

O estudante reproduz o experimento didático no notebook.

------------------------------------------------------------------------

# 7. Regra operacional da apresentação

A condução deve seguir:

> **slide → discussão/atividade/Colab quando necessário → próximo
> slide**

Não:

> slide 7 → notebook → slide 12 → slide 7 → exercício → slide 15

A apresentação deve avançar sempre.

Se o slide 6 abrir uma exploração de 25 minutos no Colab, a apresentação
permanece parada no slide 6.

Terminada a exploração:

> **avançar para o slide 7.**

Se o primeiro encontro terminar no slide 8:

> **o segundo encontro começa no slide 9.**

Uma retomada oral breve é suficiente.

------------------------------------------------------------------------

# 8. Sequência didática detalhada

## Movimento 0 --- Apresentação da disciplina

### Material

`EGC5310-Apresentacao-Disciplina.pptx`

### Objetivo

Apresentar o funcionamento da disciplina antes de iniciar o problema
computacional.

### Condução

Apresentar:

-   professor;
-   propósito da disciplina;
-   metodologia;
-   AVA;
-   Google Colab;
-   avaliação;
-   frequência;
-   principais datas.

Também utilizar esse momento para conhecer minimamente a turma.

### Diagnóstico informal

Perguntas possíveis:

-   Quem já programou em Python?
-   Quem já utilizou Google Colab?
-   Quem costuma utilizar Jupyter Notebook?
-   Quem já estudou algoritmos ou estruturas de dados?
-   Quem trouxe notebook?
-   Quem está confortável em trabalhar em dupla/trio quando necessário?

Não transformar o diagnóstico em prova.

### Tempo

Variável.

Na primeira semana, pode consumir uma parcela significativa do primeiro
encontro.

------------------------------------------------------------------------

# 9. Movimento 1 --- Apresentar a pergunta da disciplina

### Slides

1--3.

### Ideias

**Slide 1:** identificação da Semana 01.

**Slide 2:**

> **Quando uma solução que funciona deixa de ser uma boa solução?**

**Slide 3:**

> **Problema → Dados → Operação → Solução → Custo → Limitação → Nova
> solução**

### Condução

A fala deve ser predominantemente oral.

O professor pode contar um caso real em que:

-   uma consulta funcionava com poucos registros;
-   uma rotina se tornou lenta com o crescimento dos dados;
-   uma solução precisou ser reorganizada.

### Objetivo

Fazer o estudante compreender que a disciplina não será uma coleção de
estruturas para memorizar.

As estruturas aparecerão como respostas a problemas.

### Evidência de compreensão

O estudante reconhece que "funcionar" e "ser adequado" não são
necessariamente a mesma coisa.

------------------------------------------------------------------------

# 10. Movimento 2 --- Introduzir o sistema acadêmico

### Slides

4--5.

### Problema

Mostrar uma pequena coleção:

  Matrícula   Nome    Curso
  ----------- ------- ------------------
  1023        Ana     Ciência de Dados
  1047        Bruno   Ciência de Dados
  1082        Carla   Engenharia
  1091        Diego   Ciência de Dados

Perguntar:

> **Como encontrar o estudante de matrícula 1082?**

Depois:

> **Qual seria o seu algoritmo?**

### Condução

Não mostrar código imediatamente.

Permitir:

-   descrição oral;
-   pseudocódigo;
-   conversa em dupla;
-   descrição passo a passo.

### Diagnóstico

Observar:

-   quem entende iteração;
-   quem fala em índice;
-   quem pensa em percorrer registros;
-   quem antecipa estruturas mais sofisticadas;
-   quem possui dificuldade em formular um algoritmo.

### Intervenção

Se algum estudante antecipar "dicionário", "banco de dados", "índice",
"árvore" etc., reconhecer a ideia sem abandonar o problema:

> "Essa pode ser uma alternativa. Antes, vamos observar o que acontece
> com a solução mais direta."

------------------------------------------------------------------------

# 11. Movimento 3 --- Primeira solução executável

### Slide

6 --- Uma primeira solução.

### Código central

``` python
def buscar(estudantes, matricula):
    for estudante in estudantes:
        if estudante["matricula"] == matricula:
            return estudante
    return None
```

### Pergunta

> **Funciona. Então o problema está resolvido?**

### Colab

Professor:

`Busca sequencial`

Estudante:

`Atividade 1 — Complete a busca`

### Condução

Neste ponto, abrir o Google Colab.

O professor pode:

1.  mostrar a coleção;
2.  executar a função;
3.  buscar `1082`;
4.  testar outra matrícula;
5.  testar matrícula inexistente;
6.  pedir que os estudantes completem sua versão.

### Importante

Este primeiro acesso ao Colab pode consumir bastante tempo.

Isso não é considerado atraso.

Observar:

-   problemas de login;
-   estudantes sem computador;
-   dificuldade para localizar células;
-   dificuldade para executar;
-   erros de Python;
-   necessidade de formação de duplas/trios.

### Critério para avançar

A maioria deve compreender:

-   entrada da função;
-   laço;
-   comparação;
-   retorno.

Não exigir domínio sintático perfeito.

------------------------------------------------------------------------

# 12. Movimento 4 --- De correção para custo

### Slides

7--9.

### Slide 7

Representar:

`1023 → 1047 → 1082 → 1091`

Perguntar:

> **Quanto trabalho foi necessário?**

### Colab

`Contando comparações`

### Atividade

`Exercício 1 — A busca passo a passo`

### Slide 8

Comparar:

-   primeiro;
-   intermediário;
-   último;
-   inexistente.

Perguntar:

> **O algoritmo realiza a mesma quantidade de trabalho?**

### Slide 9

Formalizar:

> **n = tamanho da entrada**

No problema:

> **n = quantidade de estudantes na coleção**

### Objetivo

Fazer a quantidade de operações emergir do algoritmo antes da
matemática.

### Evidência

O estudante consegue dizer, por exemplo:

-   primeiro elemento → 1 comparação;
-   último → `n`;
-   inexistente → `n`.

------------------------------------------------------------------------

# 13. Movimento 5 --- Predizer antes de executar

### Slide

10 --- E quando os dados crescem?

### Tabela

            n   Comparações no pior caso
  ----------- --------------------------
           10                          ?
          100                          ?
        1.000                          ?
       10.000                          ?
    1.000.000                          ?

### Atividade

`Exercício 3 — Antes de executar`

### Regra

**Não executar imediatamente.**

Primeiro, pedir previsão.

### Perguntas

-   Para 10 estudantes?
-   Para 100?
-   Para 1 milhão?
-   O que ocorre quando `n` é multiplicado por 10?

### Objetivo

Mostrar que podemos prever estruturalmente o comportamento do algoritmo.

### Resultado esperado

No pior caso:

\[ comparações=n \]

------------------------------------------------------------------------

# 14. Movimento 6 --- Formalizar o crescimento

### Slides

11--13.

## Slide 11 --- T(n)

Definir:

\[
T(n)=`\text{quantidade de operações para uma entrada de tamanho }`{=tex}n
\]

Modelo:

\[ T(n)=a`\cdot `{=tex}n+b \]

e:

\[ T(n)`\propto `{=tex}n \]

Explicar:

> **T(n) ∝ n significa que o custo cresce proporcionalmente ao tamanho
> da entrada.**

## Slide 12 --- Big-O

Mostrar:

\[ a`\cdot `{=tex}n+b `\longrightarrow `{=tex}O(n) \]

Definição introdutória:

> **Big-O descreve uma ordem de crescimento do custo em função do
> tamanho da entrada.**

Não apresentar definição assintótica formal nesta semana.

## Slide 13 --- Comparação qualitativa

Introduzir apenas:

\[ O(1),`\quad `{=tex}O(n),`\quad `{=tex}O(n\^2) \]

Perguntar:

> **O que acontece quando n dobra?**

Esperado:

-   `O(1)` → essencialmente não depende de `n`;
-   `O(n)` → aproximadamente dobra;
-   `O(n²)` → aproximadamente quadruplica.

### Atividade possível

Parte do `Exercício 4`.

### Objetivo

Dar significado à notação, não criar uma tabela para memorização.

------------------------------------------------------------------------

# 15. Movimento 7 --- Retornar ao algoritmo

### Slide

14 --- E a nossa busca?

### Classificação

**Melhor caso:** `O(1)`

**Pior caso:** `O(n)`

### Pergunta

> **Por quê?**

### Colab

Professor:

`Melhor e pior caso`

Estudante:

`Atividade 3 — Compare melhor e pior caso`

### Objetivo

A formalização deve retornar imediatamente ao problema concreto.

### Cuidado

Não dizer apenas:

> "Busca sequencial é O(n)."

Perguntar sempre:

> "Em qual caso?"

------------------------------------------------------------------------

# 16. Movimento 8 --- Big-O não é cronômetro

### Slide

15. 

### Contraste

**Tempo observado**

versus

**ordem de crescimento**

### Frase

> **Tempo de execução observado ≠ ordem de crescimento**

### Colab

`Tempo × número de operações`

### Atividade

`Exercício 5 — O cronômetro contradiz o Big-O?`

### Condução

Executar várias vezes.

Se possível, perguntar os tempos obtidos em diferentes computadores.

Depois:

> "Os tempos foram iguais?"

Provavelmente não.

Perguntar:

> "E quantas comparações foram realizadas?"

Para o mesmo `n` e mesmo pior caso, o resultado estrutural deve
coincidir.

### Objetivo

Evitar desde a primeira semana a identificação de complexidade com
segundos.

------------------------------------------------------------------------

# 17. Movimento 9 --- Experimento

### Slide

16 --- Vamos testar nossa hipótese.

### Hipótese

> **Se n aumentar, o número de comparações da busca sequencial crescerá
> linearmente no pior caso.**

### Entradas

`1.000 → 10.000 → 100.000 → 1.000.000`

### Antes de executar

Perguntar:

> **Se n aumentar 10 vezes, o que esperamos para as comparações?**

Depois:

> **Esperamos exatamente a mesma razão para o tempo?**

### Colab

Professor:

`Experimento — crescimento da busca sequencial`

Estudante:

`Experimento — crescimento da busca sequencial`

### Procedimento

1.  formular previsão;
2.  professor executa;
3.  observar comparações;
4.  observar tempo;
5.  estudantes reproduzem;
6.  comparar resultados;
7.  interpretar coletivamente.

### Benchmark

O professor pode consultar previamente:

`Semana-01-Benchmark.md`

O script:

`Semana-01-Benchmark.py`

não precisa ser entregue ou explicado aos estudantes nesta etapa.

### Resultado estrutural esperado

            n   comparações
  ----------- -------------
        1.000         1.000
       10.000        10.000
      100.000       100.000
    1.000.000     1.000.000

### Conclusão

Quando `n` aumenta 10 vezes, as comparações aumentam exatamente 10 vezes
neste pior caso.

O tempo deve apresentar tendência crescente, mas não razão exatamente
constante.

------------------------------------------------------------------------

# 18. Movimento 10 --- O problema continua

### Slide

17. 

### Afirmação

> **A solução funciona.**

### Limitação

> **Mas, no pior caso, precisamos examinar n elementos.**

### Cenários

-   10 milhões de registros;
-   milhares de consultas;
-   operação repetida continuamente.

### Pergunta

> **Podemos organizar os dados de outra maneira?**

### Atividade

`Exercício 6 — Uma solução correta pode ser inadequada?`

### Objetivo

Gerar necessidade.

Não apresentar imediatamente uma estrutura específica como "resposta
correta".

A conclusão deve ser:

> **A forma como os dados estão organizados pode alterar o custo das
> operações.**

Essa pergunta alimenta o restante da disciplina.

------------------------------------------------------------------------

# 19. Exercícios e pontos naturais de inserção

  -----------------------------------------------------------------------
  Ponto da narrativa                  Exercício
  ----------------------------------- -----------------------------------
  após slides 7--8                    Exercício 1 --- A busca passo a
                                      passo

  junto ao Colab inicial              Exercício 2 --- Instrumentando um
                                      algoritmo

  slide 10                            Exercício 3 --- Antes de executar

  slides 11--13                       Exercício 4 --- De T(n) para a
                                      ordem de crescimento

  slide 15                            Exercício 5 --- O cronômetro
                                      contradiz o Big-O?

  slide 17                            Exercício 6 --- Uma solução correta
                                      pode ser inadequada?

  se houver tempo/continuidade        Exercício 7 --- Análise de uma
                                      modificação

  extensão                            Exercício 8 --- Mini-investigação

  fechamento                          Questão de fechamento
  -----------------------------------------------------------------------

Não existe obrigação de realizar todos.

------------------------------------------------------------------------

# 20. Gestão do tempo

A Semana 01 possui aproximadamente dois encontros de 80 minutos úteis,
mas **não deve ser convertida em uma sequência rígida de 16 blocos de 10
minutos**.

Uma distribuição de referência, apenas para planejamento, pode ser:

  Movimento                                    Faixa aproximada
  ------------------------------------------ ------------------
  apresentação da disciplina + diagnóstico           20--35 min
  problema e formulação inicial                      15--25 min
  primeiro uso do Colab                              20--35 min
  observação e contagem                              15--25 min
  crescimento e formalização                         20--30 min
  tempo e experimento                                20--35 min
  fechamento                                         10--15 min

A soma pode exceder o tempo disponível.

Isso é deliberado.

O roteiro contém **mais possibilidades do que precisam necessariamente
ser executadas**.

A prioridade é preservar a progressão conceitual.

------------------------------------------------------------------------

# 21. Onde interromper o primeiro encontro?

Em qualquer ponto conceitualmente estável.

Exemplos adequados:

### Após a primeira implementação

> "Temos uma solução que funciona. No próximo encontro vamos começar
> perguntando quanto trabalho ela realiza."

### Após a contagem

> "Já sabemos que a posição interfere no custo. Vamos continuar
> investigando o que acontece quando os dados crescem."

### Após T(n)

> "Já conseguimos descrever o custo. O próximo passo será abstrair como
> ele cresce."

Não criar um encerramento artificial apenas porque terminou o encontro.

------------------------------------------------------------------------

# 22. Como retomar no segundo encontro?

Retomada oral de poucos minutos.

Exemplo:

> "No encontro anterior começamos com uma busca por matrícula,
> implementamos uma solução e chegamos à seguinte questão..."

Mostrar o próximo slide da sequência.

Não retornar sistematicamente aos slides anteriores.

Se necessário, usar o próprio Colab para recuperar rapidamente um
resultado já produzido.

------------------------------------------------------------------------

# 23. Critérios para decidir avançar ou permanecer

## Permanecer mais tempo quando

-   muitos estudantes não conseguem executar o Colab;
-   há dificuldade generalizada com o `for`;
-   a turma não compreendeu o que está sendo contado;
-   `n` ainda é apenas um símbolo sem significado;
-   Big-O está sendo confundido com tempo;
-   a discussão está produzindo boas hipóteses;
-   um exercício revela dificuldade importante.

## Avançar quando

-   a maioria consegue explicar a ideia central;
-   erros restantes são individuais;
-   a atividade começa a repetir o mesmo raciocínio;
-   o próximo movimento ajuda a consolidar o atual.

------------------------------------------------------------------------

# 24. Diagnóstico da turma a registrar

Após a semana, o professor deve registrar brevemente:

## Python

-   nível geral;
-   principais dificuldades;
-   estudantes muito avançados;
-   necessidade de revisão.

## Google Colab

-   acesso funcionou?
-   houve problemas de conta?
-   tempo de abertura?
-   estudantes sem equipamento?

## Dinâmica

-   duplas/trios funcionaram?
-   participação oral?
-   exercícios longos ou curtos demais?

## Conteúdo

-   até onde a narrativa avançou?
-   quais conceitos exigiram mais tempo?
-   quais conceitos foram compreendidos rapidamente?

## Materiais

-   slides ajudaram?
-   alternância slide/Colab foi natural?
-   notebook do estudante funcionou?
-   quais células precisam de ajuste?

Essas observações devem orientar a Semana 02 e futuras ofertas.

------------------------------------------------------------------------

# 25. Formatos experimentais da Semana 01

Além da combinação:

**slides + Google Colab**

será produzida uma versão experimental:

`Semana-01-Aula.ipynb`

Ela deverá integrar:

-   narrativa;
-   perguntas;
-   imagens;
-   código;
-   experimentos;
-   atividades.

O objetivo é avaliar se um único notebook pode substituir parte da
alternância entre apresentação e ambiente computacional.

Também poderá ser testada posteriormente uma ferramenta de transformação
de notebook em apresentação.

Esses formatos são **experimentos de infraestrutura didática** e não
alteram os objetivos de aprendizagem da semana.

------------------------------------------------------------------------

# 26. Evidências de aprendizagem

Ao final da sequência, procurar evidências de que o estudante consegue
responder:

1.  Qual era o problema?
2.  Qual foi a primeira solução?
3.  Como a busca sequencial funciona?
4.  O que significa `n` nesse problema?
5.  Quantas comparações ocorrem no pior caso?
6.  O que significa dizer que o crescimento é linear?
7.  O que `O(n)` comunica?
8.  Por que `O(n)` não significa "n segundos"?
9.  Por que dois computadores podem obter tempos diferentes?
10. Por que uma solução correta pode deixar de ser adequada?
11. Que papel a organização dos dados pode ter nessa questão?

------------------------------------------------------------------------

# 27. Critério de sucesso da Semana 01

A Semana 01 terá cumprido sua função se o estudante conseguir
reconstruir uma narrativa equivalente a:

> Temos um problema de busca em uma coleção de dados. Criamos uma
> solução sequencial que produz a resposta correta. Ao observar o
> algoritmo, percebemos que a quantidade de trabalho depende do tamanho
> da entrada e da posição do elemento. No pior caso, examinamos `n`
> registros. Esse custo cresce linearmente e pode ser representado por
> `O(n)`. O tempo medido varia entre ambientes e não é a própria
> complexidade. Quando os dados e a frequência das operações crescem,
> precisamos perguntar se existe uma maneira mais adequada de organizar
> os dados.

Não é necessário que todos os estudantes utilizem exatamente essa
formulação.

------------------------------------------------------------------------

# 28. Arquivos da Semana 01

## Documentos-fonte

-   `Semana-01-Roteiro.md`
-   `Semana-01-Especificacao-Slides.md`
-   `Semana-01-Benchmark.md`
-   `Semana-01-Exercicios.md`
-   `Semana-01-Solucoes.md`

## Artefatos executáveis

-   `Semana-01-Notebook-Professor.ipynb`
-   `Semana-01-Notebook-Estudante.ipynb`
-   `Semana-01-Benchmark.py`

## Artefatos visuais

-   `Semana-01-Slides.pptx`
-   `EGC5310-Apresentacao-Disciplina.pptx`

## Experimentos de formato

-   `Semana-01-Aula.ipynb`
-   eventual versão notebook → apresentação

------------------------------------------------------------------------

# 29. Observação para a Semana 04

A utilização da busca sequencial na Semana 01 é **introdutória**.

Na Semana 04, conforme o planejamento da disciplina, o tema deverá ser
retomado de forma sistemática, incluindo:

-   busca sequencial como algoritmo de referência;
-   busca binária;
-   pré-condições da busca binária;
-   comparação entre estratégias;
-   custo das operações;
-   implicações da organização dos dados.

Assim, a Semana 01 cria a pergunta e a linguagem analítica que serão
aprofundadas posteriormente.

------------------------------------------------------------------------

# 30. Fechamento do roteiro

A Semana 01 deve ser conduzida com uma regra simples:

> **não correr para terminar o material; avançar quando o raciocínio
> estiver suficientemente construído.**

A apresentação, o Colab, os exercícios e o benchmark não são quatro
atividades separadas.

Eles são diferentes representações da mesma investigação:

> **Como uma solução computacional se comporta quando os dados crescem,
> e o que isso nos ensina sobre a maneira de organizar os dados?**

------------------------------------------------------------------------

**Versão:** 2.0 --- roteiro semanal flexível\
**EGC5310 --- Semana 01 --- 2026/2**
