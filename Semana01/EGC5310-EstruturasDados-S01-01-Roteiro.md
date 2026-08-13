# EGC5310 --- Semana 01 --- Roteiro Didático

## Do problema ao custo computacional

**Disciplina:** EGC5310 --- Tópicos Especiais em Ciência de Dados VI\
**Semestre:** 2026/2\
**Carga semanal prevista:** 4 h-aula, distribuídas em dois encontros\
**Tempo didático de referência:** aproximadamente 80 minutos úteis por
encontro\
**Cenário longitudinal desta etapa:** Sistema acadêmico\
**Unidade didática:** a semana, e não cada encontro isoladamente\
**Formato principal da oferta 2026/2:** Notebook Mestre → Quarto →
Reveal.js

------------------------------------------------------------------------

# 1. Finalidade deste roteiro

Este documento registra a concepção pedagógica da **Semana 01 como uma
única sequência didática contínua**.

A semana não é organizada como uma separação rígida entre "aula teórica"
e "aula prática". Os dois encontros dão continuidade à mesma
investigação:

> **Como uma solução computacional se comporta quando os dados crescem,
> e o que isso nos ensina sobre a maneira de organizar os dados?**

A narrativa pode ser interrompida ao final do primeiro encontro e
retomada, no segundo, exatamente do ponto em que foi interrompida.

Os tempos são referências de planejamento, não blocos rígidos. Na
primeira oferta, a Semana 01 também possui função diagnóstica: observar
conhecimentos prévios, fluência em Python, familiaridade com notebooks,
ritmo da turma e adequação dos materiais.

Portanto, **não é obrigatório concluir todo o conteúdo previsto**. A
prioridade é preservar a construção do raciocínio.

------------------------------------------------------------------------

# 2. Relação com o Plano de Ensino

O Plano de Ensino caracteriza a Semana 01 como:

> **Apresentação da disciplina. Diagnóstico. Introdução aos problemas de
> manipulação de dados.**

A busca sequencial é utilizada como **problema introdutório e
instrumento para observar custo computacional**.

Seu uso nesta semana não substitui o tratamento sistemático das
estratégias de busca previsto posteriormente no semestre. A comparação
formal entre busca sequencial, busca binária e suas pré-condições
permanece para a etapa correspondente do cronograma.

Nesta semana, a busca sequencial serve para construir a primeira cadeia
de raciocínio da disciplina:

> **problema → dados → operação → solução → custo → crescimento →
> limitação → nova solução**

------------------------------------------------------------------------

# 3. Objetivos de aprendizagem

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

## Não é objetivo da Semana 01

-   memorizar tabelas de complexidade;
-   dominar formalmente análise assintótica;
-   estudar todas as estruturas de dados;
-   comparar sistematicamente busca sequencial e busca binária;
-   aprofundar metodologia de benchmarking;
-   dominar Git/GitHub ou Quarto.

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

A matrícula `1082` é utilizada nos primeiros exemplos.

O problema deve aparecer **antes** de definições abstratas de estrutura
de dados ou complexidade.

------------------------------------------------------------------------

# 5. Pergunta central da semana

A pergunta que orienta a narrativa é:

> **Quando uma solução que funciona deixa de ser uma boa solução?**

Ela permite discutir situações em que:

-   uma solução funciona adequadamente com poucos registros;
-   o volume de dados cresce;
-   a frequência das operações aumenta;
-   uma rotina correta passa a apresentar limitações;
-   torna-se necessário reconsiderar algoritmo ou organização dos dados.

A disciplina não deve aparecer como uma coleção de estruturas para
memorizar. As estruturas devem surgir como **respostas a necessidades
computacionais**.

------------------------------------------------------------------------

# 6. Princípio didático

A sequência deve seguir, tanto quanto possível:

> **problema → hipótese/ideia dos estudantes → solução → observação das
> operações → formalização → experimento → interpretação → nova
> pergunta**

A formalização matemática não deve anteceder a experiência que lhe dá
significado.

Assim:

-   primeiro surge a busca;
-   depois observamos as comparações;
-   depois definimos `n`;
-   depois descrevemos `T(n)`;
-   depois introduzimos a ordem de crescimento;
-   por fim retornamos ao problema e discutimos sua limitação.

------------------------------------------------------------------------

# 7. Materiais da Semana 01

## 7.1 Apresentação institucional

`EGC5310-Apresentacao-Disciplina.pptx`

Utilizada no início do primeiro encontro para apresentar:

-   disciplina;
-   professor;
-   objetivos;
-   metodologia;
-   avaliação;
-   frequência;
-   Moodle/AVA;
-   ambiente computacional;
-   principais marcos do semestre.

É independente da narrativa computacional da Semana 01.

## 7.2 Notebook Mestre

`EGC5310-EstruturasDados-S01-99-Aula-Mestre.ipynb`

É a **fonte estruturante da aula experimental de 2026/2**.

Integra:

-   narrativa;
-   perguntas;
-   elementos visuais;
-   código;
-   experimentos;
-   formalização;
-   atividades e transições conceituais.

O notebook é renderizado pelo **Quarto** em uma apresentação
**Reveal.js**.

A versão HTML renderizada pode ser utilizada diretamente em sala,
inclusive sem necessidade de renderização no momento da aula.

## 7.3 Materiais anteriores preservados

Os materiais produzidos anteriormente continuam válidos:

-   slides em PPTX;
-   notebook do professor;
-   notebook do estudante;
-   exercícios;
-   soluções;
-   benchmark.

Eles constituem material complementar e também uma alternativa
operacional caso o formato Notebook Mestre/Reveal.js apresente
problemas.

A adoção do Notebook Mestre nesta primeira semana é, portanto, uma
**avaliação de formato didático**, não a eliminação dos materiais
anteriores.

------------------------------------------------------------------------

# 8. Regra operacional da aula

Com o Notebook Mestre, apresentação e código fazem parte de uma mesma
narrativa.

A condução geral é:

> **apresentação → pergunta → discussão/atividade → código ou
> experimento quando necessário → interpretação → continuidade**

Não é necessário alternar sistematicamente entre arquivos diferentes.

Quando um slide abrir uma exploração, a narrativa permanece naquele
ponto até que a exploração cumpra sua função.

Terminada a exploração, avança-se para o próximo movimento.

Se o primeiro encontro terminar no meio da sequência, o segundo encontro
começa a partir daquele ponto, com uma breve retomada oral.

------------------------------------------------------------------------

# 9. Movimentos conceituais da Semana 01

A descrição operacional detalhada dos movimentos deve ser mantida em
documento próprio de **Sequência Didática**. Este roteiro registra a
arquitetura conceitual.

## Movimento 0 --- Apresentação e diagnóstico

Apresentar a disciplina e conhecer minimamente a turma.

Observar especialmente:

-   experiência prévia com Python;
-   uso de Jupyter/Colab;
-   conhecimentos prévios de algoritmos;
-   disponibilidade de notebook;
-   possibilidade de trabalho em duplas/trios.

O diagnóstico é informal e não constitui avaliação classificatória.

## Movimento 1 --- Pergunta da disciplina

Introduzir:

> **Quando uma solução que funciona deixa de ser uma boa solução?**

Apresentar o caminho da investigação:

> **Problema → Dados → Operação → Solução → Custo → Limitação → Nova
> solução**

A mensagem fundamental é que "funcionar" e "ser adequado" não são
necessariamente equivalentes.

## Movimento 2 --- Sistema acadêmico

Apresentar a pequena coleção de estudantes e perguntar:

> **Como encontrar o estudante de matrícula 1082?**

Não apresentar código imediatamente.

Permitir formulação oral, descrição passo a passo ou pseudocódigo.

## Movimento 3 --- Primeira solução

Construir/executar uma busca sequencial simples.

Perguntar:

> **Funciona. Então o problema está resolvido?**

Garantir que a maioria compreenda entrada, repetição, comparação e
retorno, sem exigir domínio sintático perfeito.

## Movimento 4 --- Da correção para o custo

Observar o percurso realizado pela busca.

Perguntar:

> **Quanto trabalho foi necessário?**

Comparar busca pelo primeiro, intermediário, último e elemento
inexistente.

A quantidade de operações deve emergir da execução antes da
formalização.

## Movimento 5 --- Tamanho da entrada e crescimento

Definir:

> **n = tamanho da entrada**

No cenário:

> **n = quantidade de estudantes na coleção**

Antes de executar para coleções maiores, pedir previsões.

O estudante deve perceber que, no pior caso da busca sequencial, o
número de comparações acompanha `n`.

## Movimento 6 --- Formalização

Introduzir `T(n)` como descrição do custo em função do tamanho da
entrada.

Construir a relação de crescimento linear e introduzir `O(n)` como ordem
de crescimento.

Apresentar qualitativamente `O(1)`, `O(n)` e `O(n²)` apenas para
contrastar comportamentos.

Não apresentar definição assintótica formal nesta semana.

## Movimento 7 --- Retorno à busca

Classificar intuitivamente:

-   melhor caso: `O(1)`;
-   pior caso: `O(n)`.

A pergunta central é:

> **Por quê?**

Evitar a formulação isolada "busca sequencial é O(n)" sem explicitar o
caso analisado.

## Movimento 8 --- Big-O não é cronômetro

Distinguir:

> **tempo de execução observado ≠ ordem de crescimento**

Comparar execuções e discutir por que tempos podem variar entre
execuções ou computadores enquanto o comportamento estrutural do
algoritmo permanece.

## Movimento 9 --- Experimento

Testar a hipótese:

> **Se n aumentar, o número de comparações da busca sequencial crescerá
> linearmente no pior caso.**

Usar entradas crescentes e observar:

-   número de comparações;
-   tempo observado;
-   relação entre aumento de `n` e aumento das comparações.

O experimento deve confirmar a previsão estrutural, sem exigir
proporcionalidade exata do tempo medido.

## Movimento 10 --- O problema continua

Retornar à limitação:

> **A solução funciona, mas no pior caso precisamos examinar n
> elementos.**

Escalar mentalmente para milhões de registros e muitas consultas.

Encerrar com a pergunta:

> **Podemos organizar os dados de outra maneira?**

A conclusão desejada é:

> **A forma como os dados estão organizados pode alterar o custo das
> operações.**

Essa necessidade alimenta o restante da disciplina.

------------------------------------------------------------------------

# 10. Predizer antes de executar

Sempre que possível, solicitar uma previsão antes da execução.

Exemplos:

-   quantas comparações esperamos?
-   o que ocorre quando `n` é multiplicado por 10?
-   o tempo também aumentará exatamente 10 vezes?
-   primeiro, último e inexistente possuem o mesmo custo?

A execução deve servir para **testar uma hipótese**, não apenas para
produzir uma saída.

------------------------------------------------------------------------

# 11. Papel do código

O código não é apresentado como fim em si mesmo.

Nesta semana, ele cumpre três funções:

1.  tornar uma solução executável;
2.  permitir observar e contar operações;
3.  produzir evidências para discutir crescimento.

Dificuldades sintáticas individuais não devem interromper excessivamente
a narrativa conceitual. Quando necessário, utilizar duplas/trios e apoio
pontual.

------------------------------------------------------------------------

# 12. Papel da matemática

A matemática deve formalizar uma ideia já observada.

A sequência esperada é:

> execução → comparações → `n` → `T(n)` → crescimento → `O(n)`

`T(n)` representa o custo em função do tamanho da entrada.

A notação Big-O é introduzida como linguagem para comunicar **ordem de
crescimento**, sem aprofundamento formal nesta semana.

------------------------------------------------------------------------

# 13. Big-O e tempo observado

Desde a primeira semana deve ser evitada a associação:

> `O(n)` = "n segundos"

O tempo observado depende de fatores como ambiente, hardware, carga do
sistema e detalhes de implementação.

A contagem de operações permite observar uma propriedade estrutural do
algoritmo.

O cronômetro é evidência experimental útil, mas não é a própria ordem de
crescimento.

------------------------------------------------------------------------

# 14. Gestão do tempo

A Semana 01 possui aproximadamente dois encontros de 80 minutos úteis.

Uma distribuição de referência pode ser:

  Movimento                                    Faixa aproximada
  ------------------------------------------ ------------------
  apresentação da disciplina + diagnóstico           20--35 min
  problema e formulação inicial                      15--25 min
  primeira execução e exploração do código           20--35 min
  observação e contagem                              15--25 min
  crescimento e formalização                         20--30 min
  tempo e experimento                                20--35 min
  fechamento                                         10--15 min

A soma pode exceder o tempo disponível.

Isso é deliberado.

O roteiro contém mais possibilidades do que precisam necessariamente ser
executadas. A prioridade é preservar a progressão conceitual.

------------------------------------------------------------------------

# 15. Onde interromper?

O encontro pode terminar em qualquer ponto conceitualmente estável.

Exemplos:

### Após a primeira implementação

> "Temos uma solução que funciona. No próximo encontro vamos perguntar
> quanto trabalho ela realiza."

### Após a contagem

> "Já sabemos que a posição interfere no custo. Vamos investigar o que
> acontece quando os dados crescem."

### Após `T(n)`

> "Já conseguimos descrever o custo. O próximo passo será abstrair como
> ele cresce."

Não criar um encerramento artificial apenas porque o tempo terminou.

------------------------------------------------------------------------

# 16. Como retomar?

No segundo encontro, fazer uma retomada oral breve.

Exemplo:

> "No encontro anterior começamos com uma busca por matrícula,
> construímos uma solução e chegamos à seguinte questão..."

Continuar a narrativa.

Não é necessário retornar sistematicamente aos slides anteriores.

------------------------------------------------------------------------

# 17. Critérios para permanecer ou avançar

## Permanecer mais tempo quando

-   muitos estudantes apresentam dificuldade para executar o ambiente;
-   há dificuldade generalizada com o `for`;
-   a turma não compreendeu o que está sendo contado;
-   `n` ainda aparece apenas como símbolo sem significado;
-   Big-O está sendo confundido com tempo;
-   uma discussão está produzindo hipóteses pedagogicamente úteis;
-   uma atividade revela dificuldade conceitual importante.

## Avançar quando

-   a maioria consegue explicar a ideia central;
-   os erros restantes são individuais;
-   a atividade começa a repetir o mesmo raciocínio;
-   o próximo movimento ajuda a consolidar o atual.

------------------------------------------------------------------------

# 18. Evidências de aprendizagem

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

# 19. Critério de sucesso

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

Não é necessário que todos utilizem exatamente essa formulação.

------------------------------------------------------------------------

# 20. Diagnóstico a registrar após a semana

Após a execução, registrar brevemente:

## Python

-   nível geral;
-   principais dificuldades;
-   necessidade de revisão;
-   presença de estudantes muito avançados.

## Ambiente computacional

-   acesso e execução funcionaram?
-   houve problemas de equipamento?
-   houve dificuldades com notebook/Jupyter/Colab?
-   duplas/trios foram necessárias?

## Dinâmica

-   participação oral;
-   funcionamento das duplas/trios;
-   ritmo das perguntas;
-   atividades longas ou curtas demais.

## Conteúdo

-   até onde a narrativa avançou;
-   conceitos que exigiram mais tempo;
-   conceitos compreendidos rapidamente;
-   confusões recorrentes.

## Notebook Mestre / Reveal.js

-   apresentação funcionou em sala?
-   código ficou legível?
-   alternância entre narrativa e execução foi natural?
-   elementos visuais ajudaram?
-   quais slides/células precisam de ajuste?
-   o formato deve ser mantido na Semana 02?

Essas observações devem orientar a próxima semana e futuras ofertas.

------------------------------------------------------------------------

# 21. Relação com a etapa posterior de busca

A busca sequencial nesta semana é **introdutória**.

Na etapa do semestre destinada às estratégias de busca, o tema deverá
ser retomado sistematicamente, incluindo:

-   busca sequencial como referência;
-   busca binária;
-   pré-condições da busca binária;
-   comparação entre estratégias;
-   custo das operações;
-   implicações da organização dos dados.

Assim, a Semana 01 cria a pergunta e a linguagem analítica que serão
aprofundadas posteriormente.

------------------------------------------------------------------------

# 22. Fechamento do roteiro

A Semana 01 deve ser conduzida segundo uma regra simples:

> **não correr para terminar o material; avançar quando o raciocínio
> estiver suficientemente construído.**

Apresentação, código, exercícios e experimentos não constituem
atividades independentes.

São diferentes momentos da mesma investigação:

> **Como uma solução computacional se comporta quando os dados crescem,
> e o que isso nos ensina sobre a maneira de organizar os dados?**

------------------------------------------------------------------------

**Versão:** 3.0 --- roteiro pedagógico atualizado para Notebook
Mestre/Quarto/Reveal.js\
**EGC5310 --- Semana 01 --- 2026/2**
