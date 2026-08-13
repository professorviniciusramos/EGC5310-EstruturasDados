# EGC5310 --- Semana 01 --- Sequência Didática Detalhada

## Guia operacional de condução da aula

**Disciplina:** EGC5310 --- Tópicos Especiais em Ciência de Dados VI\
**Semestre:** 2026/2\
**Cenário:** Sistema acadêmico\
**Material principal:**
`EGC5310-EstruturasDados-S01-99-Aula-Mestre.html`\
**Fonte:** `EGC5310-EstruturasDados-S01-99-Aula-Mestre.ipynb`\
**Unidade didática:** Semana 01 --- dois encontros contínuos\
**Tempo de referência:** aproximadamente 160 minutos úteis no total

------------------------------------------------------------------------

# 1. Como usar este documento

Este arquivo é o **guia operacional do professor durante a execução da
Semana 01**.

Ele complementa o `S01-01-Roteiro.md`.

O roteiro registra a concepção pedagógica; este documento responde
principalmente:

> **O que fazer, perguntar, observar e concluir em cada momento da
> aula?**

A sequência acompanha o Notebook Mestre, mas evita depender rigidamente
da numeração dos slides. Os títulos e conceitos são referências mais
estáveis caso a apresentação seja modificada no futuro.

A regra principal é:

> **não avançar apenas porque o próximo slide existe. Avançar quando o
> movimento atual tiver cumprido sua função.**

------------------------------------------------------------------------

# 2. Antes da aula

## Verificação técnica

Antes de entrar em sala:

-   abrir o HTML renderizado localmente;
-   verificar logo e CSS;
-   testar avanço e retorno dos slides;
-   verificar fórmulas matemáticas;
-   conferir células de código e gráficos;
-   confirmar que o ambiente Python/Jupyter está disponível caso seja
    necessário executar ou modificar código;
-   manter os materiais anteriores disponíveis como contingência.

## Arquivos prioritários

1.  `S01-99-Aula-Mestre.html` --- apresentação principal;
2.  `S01-99-Aula-Mestre.ipynb` --- fonte e execução;
3.  apresentação institucional da disciplina;
4.  notebooks anteriores professor/estudante --- contingência;
5.  exercícios e soluções --- caso o ritmo permita.

------------------------------------------------------------------------

# 3. Movimento 0 --- Apresentação da disciplina e diagnóstico

## Objetivo

Apresentar rapidamente a disciplina e obter uma primeira leitura da
turma.

## Condução

Utilizar a apresentação institucional.

Apresentar:

-   proposta da disciplina;
-   organização das semanas;
-   metodologia;
-   avaliação;
-   frequência;
-   Moodle;
-   GitHub, apenas como infraestrutura de apoio;
-   Jupyter/Colab;
-   natureza predominantemente prática da disciplina.

## Diagnóstico oral

Perguntar informalmente:

-   Quem já programou em Python?
-   Quem já utilizou Jupyter Notebook?
-   Quem já utilizou Google Colab?
-   Quem conhece listas em Python?
-   Quem já ouviu falar em complexidade de algoritmos ou Big-O?
-   Quem está com notebook próprio?

Não transformar esse momento em teste formal.

## Observar

Registrar mentalmente:

-   heterogeneidade da turma;
-   estudantes sem experiência com Python;
-   estudantes muito avançados;
-   necessidade de duplas/trios;
-   problemas de infraestrutura.

## Critério para avançar

A turma compreendeu minimamente como a disciplina funcionará e o
professor possui uma primeira percepção do nível técnico.

------------------------------------------------------------------------

# 4. Movimento 1 --- Abrir a investigação

## Ponto de referência

Slides iniciais do Notebook Mestre e **"O caminho da investigação"**.

## Objetivo

Estabelecer a pergunta que dará sentido ao restante da aula.

## Pergunta principal

> **Quando uma solução que funciona deixa de ser uma boa solução?**

Não responder imediatamente.

Permitir respostas espontâneas.

Possíveis ideias que podem surgir:

-   quando fica lenta;
-   quando há muitos dados;
-   quando consome muita memória;
-   quando há muitos usuários;
-   quando não escala;
-   quando existe uma solução melhor.

Todas podem ser aproveitadas.

## Mostrar o caminho

Apresentar:

> **Problema → Dados → Operação → Solução → Custo → Limitação → Nova
> solução**

Explicar apenas o necessário:

> "Esse será um caminho recorrente na disciplina. Não começaremos
> escolhendo uma estrutura de dados. Começaremos com um problema."

## Mensagem que precisa ficar

> **Correto não significa necessariamente adequado.**

## Transição

> "Vamos começar com um problema muito simples."

------------------------------------------------------------------------

# 5. Movimento 2 --- O sistema acadêmico

## Ponto de referência

Slides com os registros dos estudantes.

## Objetivo

Criar um problema suficientemente simples para que a turma consiga
pensar primeiro no algoritmo e só depois no código.

## Apresentação

Mostrar a pequena coleção contendo estudantes como:

-   1023 --- Ana;
-   1047 --- Bruno;
-   1082 --- Carla;
-   1091 --- Diego.

## Pergunta

> **Como encontrar a matrícula 1082?**

## Regra importante

**Não mostrar a solução imediatamente.**

Solicitar uma descrição:

-   oral;
-   passo a passo;
-   pseudocódigo;
-   eventualmente código, se alguém espontaneamente propuser.

## Respostas esperadas

Algo equivalente a:

1.  olhar o primeiro estudante;
2.  comparar a matrícula;
3.  se não for a procurada, olhar o próximo;
4.  repetir;
5.  retornar quando encontrar;
6.  informar ausência se chegar ao final.

## Se a turma responder muito rapidamente

Perguntar:

> "O que exatamente o computador precisa fazer?"

Isso força a explicitação das operações.

## Se houver dificuldade

Executar oralmente:

> "1023 é 1082? Não. E agora?"

Continuar até que a lógica apareça.

## Evidência para avançar

A turma consegue explicar a busca sem depender da sintaxe Python.

------------------------------------------------------------------------

# 6. Movimento 3 --- Transformar a ideia em algoritmo

## Ponto de referência

Código da busca sequencial.

## Objetivo

Mostrar que a implementação é a formalização de uma ideia que a turma
acabou de construir.

## Condução

Percorrer o código lentamente.

Destacar:

-   coleção;
-   laço `for`;
-   estudante atual;
-   comparação da matrícula;
-   `return`;
-   situação de elemento inexistente.

## Perguntas

> "Qual é a entrada?"

> "O que está sendo comparado?"

> "Quando o algoritmo para?"

> "O que acontece se a matrícula não existir?"

## Se houver estudantes com dificuldade de Python

Não interromper toda a narrativa para uma revisão completa.

Explicar apenas:

-   iteração;
-   comparação;
-   retorno.

Registrar a necessidade de revisão para atividades futuras.

## Executar

Testar inicialmente:

``` python
buscar_por_matricula(estudantes, 1082)
```

## Pergunta após funcionar

> **Funciona. Então o problema está resolvido?**

Esperar.

Não antecipar Big-O.

## Transição

> "Antes de responder, precisamos observar quanto trabalho essa solução
> realizou."

------------------------------------------------------------------------

# 7. Movimento 4 --- Contar o trabalho

## Ponto de referência

**"Quanto trabalho foi necessário?"**

## Objetivo

Fazer o custo surgir da execução.

## Condução

Percorrer visualmente a busca por `1082`.

A sequência deve evidenciar as comparações realizadas.

Perguntar:

> **Quantas comparações foram necessárias?**

Esperar a turma contar.

Resultado:

> **3 comparações.**

## Evitar

Não dizer ainda:

> "Isso é O(n)."

Ainda não.

## Pergunta seguinte

> "Será sempre 3?"

Essa pergunta prepara os casos.

------------------------------------------------------------------------

# 8. Movimento 5 --- Primeiro, intermediário, último e inexistente

## Ponto de referência

Slide **"O algoritmo realiza a mesma quantidade de trabalho?"**

## Objetivo

Mostrar que o custo depende do caso.

A apresentação está organizada em duas ideias:

### Encontra antes do final

-   primeiro;
-   intermediário.

### Percorre toda a coleção

-   último;
-   inexistente.

## Condução

Antes de revelar cada quantidade, perguntar à turma.

### Primeiro elemento

> "Se procurarmos 1023?"

Esperado:

> **1 comparação.**

### Intermediário

> "E um elemento encontrado no meio?"

Esperado:

> depende da posição; no exemplo, **3 comparações**.

### Último

> "E se for o último?"

Esperado:

> precisamos percorrer toda a coleção.

### Inexistente

> "E se a matrícula não existir?"

Esperado:

> também precisamos percorrer toda a coleção.

## Conceitos a introduzir verbalmente

Sem formalismo excessivo:

-   melhor caso;
-   pior caso.

## Pergunta importante

> "Último e inexistente são problemas diferentes, mas realizam
> aproximadamente a mesma quantidade de trabalho. Por quê?"

## Evidência para avançar

A turma percebe que:

> **a posição do elemento interfere no trabalho realizado.**

------------------------------------------------------------------------

# 9. Movimento 6 --- Introduzir n

## Objetivo

Passar do exemplo concreto para uma entrada de tamanho variável.

## Pergunta

> "Nossa coleção tem quatro estudantes. E se tivesse mil?"

Depois:

> "Como podemos representar o tamanho da coleção sem escolher um número
> específico?"

Introduzir:

> **n = tamanho da entrada**

No problema:

> **n = número de estudantes na coleção**

## Predição

Perguntar antes de executar:

> "No pior caso, quantas comparações teremos para 10 estudantes?"

> "E para 100?"

> "E para 1.000?"

Esperado:

-   aproximadamente 10;
-   aproximadamente 100;
-   aproximadamente 1.000.

## Mensagem

> **Quando n cresce, o trabalho cresce.**

Ainda não é necessário nomear a classe de complexidade.

------------------------------------------------------------------------

# 10. Movimento 7 --- T(n)

## Ponto de referência

Slide **"T(n)"**.

## Objetivo

Dar linguagem matemática a uma relação já observada.

Apresentar:

> `T(n)` representa a quantidade de trabalho necessária para uma entrada
> de tamanho `n`.

A apresentação mostra a ideia em duas linhas para facilitar a leitura.

Depois:

\[ T(n)=a`\cdot `{=tex}n+b \]

e, conceitualmente:

\[ T(n)`\propto `{=tex}n \]

## Explicação curta

Não aprofundar constantes.

Dizer algo equivalente a:

> "Não estamos tentando prever quantos segundos serão necessários.
> Estamos descrevendo como a quantidade de trabalho muda quando a
> entrada cresce."

## Pergunta

> "Se dobrarmos n, o que esperamos que aconteça com a quantidade de
> comparações no pior caso?"

Esperado:

> aproximadamente dobra.

## Evidência para avançar

A turma consegue associar `n` ao tamanho da coleção e `T(n)` ao
trabalho.

------------------------------------------------------------------------

# 11. Movimento 8 --- Introduzir Big-O

## Objetivo

Apresentar Big-O como linguagem de crescimento, e não como tabela para
memorizar.

## Condução

Apresentar a ideia:

> **Big-O descreve como o custo cresce quando n cresce.**

Usar o gráfico qualitativo com:

-   `O(1)`;
-   `O(n)`;
-   `O(n²)`.

## Não aprofundar

Não é necessário nesta semana:

-   definição formal com constantes;
-   limites;
-   prova assintótica;
-   Θ;
-   Ω.

## Perguntas

> "Qual dessas curvas se parece com o comportamento que acabamos de
> observar?"

Esperado:

> `O(n)`.

> "Por quê?"

Esperado:

> porque o número de comparações cresce aproximadamente na mesma
> proporção que `n`.

## Mensagem

> **Big-O é uma linguagem para falar sobre crescimento.**

------------------------------------------------------------------------

# 12. Movimento 9 --- Retornar à busca

## Ponto de referência

Slide **"E a nossa busca?"**

## Objetivo

Aplicar imediatamente a linguagem recém-introduzida.

### Melhor caso

Elemento na primeira posição:

> 1 comparação.

Relacionar a:

> `O(1)`.

### Pior caso

Último ou inexistente:

> até `n` comparações.

Relacionar a:

> `O(n)`.

## Cuidado verbal

Evitar:

> "Busca sequencial é O(n)."

Preferir:

> "No pior caso, a busca sequencial apresenta crescimento O(n)."

## Pergunta

> "Por que o melhor caso pode ser O(1) se a coleção tiver um milhão de
> elementos?"

Esperado:

> porque, se o elemento estiver na primeira posição, uma comparação
> basta.

------------------------------------------------------------------------

# 13. Movimento 10 --- Big-O não é cronômetro

## Ponto de referência

Slide **"Big-O não é cronômetro"**.

## Objetivo

Evitar uma confusão conceitual desde a primeira semana.

O slide estabelece:

> **Mesmo algoritmo. Mesmo n. Mesmo pior caso.**

Perguntar:

> "Os tempos de execução serão exatamente iguais?"

Esperado:

> não necessariamente.

Depois:

> "E o número de comparações?"

Esperado:

> deve permanecer estruturalmente o mesmo para aquele caso.

Apresentar:

> **TEMPO OBSERVADO ≠ ORDEM DE CRESCIMENTO**

## Explicação

O tempo pode variar por:

-   hardware;
-   carga do computador;
-   sistema operacional;
-   interpretador;
-   processos concorrentes;
-   ruído de medição.

A ordem de crescimento descreve uma propriedade estrutural do
comportamento do algoritmo.

## Mensagem essencial

> **O cronômetro produz evidência experimental; Big-O descreve
> crescimento.**

------------------------------------------------------------------------

# 14. Movimento 11 --- Formular a hipótese

## Objetivo

Transformar a próxima execução em experimento.

Antes de executar para entradas maiores, formular explicitamente:

> **Hipótese: no pior caso da busca sequencial, o número de comparações
> cresce linearmente com n.**

Perguntar:

> "O que esperamos observar se essa hipótese estiver correta?"

Respostas esperadas:

-   para 100 elementos, aproximadamente 100 comparações;
-   para 1.000, aproximadamente 1.000;
-   para 10.000, aproximadamente 10.000;
-   gráfico aproximadamente linear.

## Regra

**Predizer antes de executar.**

------------------------------------------------------------------------

# 15. Movimento 12 --- Experimento

## Objetivo

Produzir evidência empírica para a hipótese.

Utilizar a célula que gera coleções de diferentes tamanhos.

Executar a busca no pior caso.

Registrar:

-   `n`;
-   comparações;
-   tempo.

## Perguntas durante a execução

> "As comparações confirmam nossa previsão?"

> "O tempo cresce exatamente na mesma proporção?"

> "Se não crescer exatamente, nossa análise estava errada?"

A última pergunta é importante.

Esperado:

> não; o tempo observado possui ruído e depende do ambiente.

## Gráfico

Observar o gráfico:

> **n × número de comparações**

Perguntar:

> "Qual forma aparece?"

Esperado:

> aproximadamente uma reta.

Relacionar novamente a:

> `O(n)`.

------------------------------------------------------------------------

# 16. Movimento 13 --- Escalar mentalmente o problema

## Objetivo

Fazer a limitação aparecer sem introduzir prematuramente outra
estrutura.

Passar de:

-   4 estudantes;
-   milhares de estudantes;

para:

-   centenas de milhares;
-   milhões de estudantes;
-   muitas consultas.

Perguntar:

> "Uma busca que percorre potencialmente todos os registros continua
> sendo aceitável em qualquer situação?"

Não há necessidade de resposta única.

Pode depender de:

-   tamanho;
-   frequência;
-   requisitos;
-   contexto.

## Pergunta final

> **Podemos organizar os dados de outra maneira?**

Não desenvolver busca binária formalmente.

Se alguém sugerir:

-   ordenar;
-   índice;
-   dicionário;
-   hash;
-   árvore;

acolher a ideia.

Responder algo como:

> "Exatamente. A organização dos dados começa a fazer parte da solução."

------------------------------------------------------------------------

# 17. Movimento 14 --- Fechamento

## Reconstruir a narrativa

Solicitar que a turma ajude a reconstruir:

1.  tínhamos um problema;
2.  construímos uma solução;
3.  a solução funcionou;
4.  observamos suas operações;
5.  contamos o trabalho;
6.  definimos `n`;
7.  descrevemos `T(n)`;
8.  observamos crescimento linear;
9.  usamos `O(n)` para comunicar esse crescimento;
10. distinguimos crescimento de tempo medido;
11. testamos uma hipótese;
12. encontramos uma limitação;
13. perguntamos se outra organização dos dados pode ajudar.

## Frase de fechamento

> **Uma solução correta pode deixar de ser adequada quando os dados
> crescem. A forma como organizamos os dados influencia o custo das
> operações.**

## Não antecipar demais

Evitar transformar o fechamento em uma aula sobre:

-   busca binária;
-   hashing;
-   árvores;
-   índices.

A pergunta deve permanecer aberta para alimentar o semestre.

------------------------------------------------------------------------

# 18. Se o tempo acabar

A sequência foi deliberadamente planejada com mais possibilidades do que
cabem rigidamente em dois encontros.

## Bom ponto de parada 1

Após a implementação:

> "Temos uma solução que funciona. Agora precisamos descobrir quanto
> trabalho ela realiza."

## Bom ponto de parada 2

Após os casos:

> "Descobrimos que a posição interfere no trabalho. Vamos investigar
> como isso se comporta quando a coleção cresce."

## Bom ponto de parada 3

Após `T(n)`:

> "Já conseguimos descrever o custo em função do tamanho da entrada.
> Agora precisamos de uma linguagem para descrever seu crescimento."

## Bom ponto de parada 4

Após Big-O:

> "Temos uma previsão teórica. No próximo encontro vamos testá-la."

A prioridade é **não correr artificialmente para o último slide**.

------------------------------------------------------------------------

# 19. Se a turma estiver muito rápida

Possibilidades de expansão, nesta ordem:

1.  pedir aos estudantes que modifiquem a busca;
2.  instrumentar manualmente a contagem de comparações;
3.  testar matrículas em diferentes posições;
4.  testar elemento inexistente;
5.  aumentar os tamanhos de entrada;
6.  repetir medições de tempo;
7.  discutir por que os tempos variam;
8.  utilizar exercícios já preparados.

Não introduzir conteúdo futuro apenas para preencher tempo.

------------------------------------------------------------------------

# 20. Se houver dificuldade com Python

Prioridade:

> **preservar o raciocínio algorítmico.**

Estratégias:

-   executar o código coletivamente;
-   formar duplas/trios;
-   explicar somente as construções necessárias;
-   permitir que estudantes descrevam o algoritmo oralmente;
-   separar dificuldade sintática de dificuldade conceitual.

Registrar as dificuldades para orientar as próximas semanas.

------------------------------------------------------------------------

# 21. Se houver problema técnico com o Notebook Mestre

Ordem de contingência:

1.  utilizar o HTML autocontido já renderizado;
2.  abrir o `.ipynb` diretamente;
3.  utilizar os notebooks anteriores;
4.  utilizar os slides PPTX anteriores;
5.  conduzir a sequência no quadro, se necessário.

A narrativa pedagógica independe da ferramenta.

------------------------------------------------------------------------

# 22. Checklist conceitual antes de encerrar a semana

Verificar se a maioria consegue explicar, ainda que informalmente:

-   [ ] qual problema foi resolvido;
-   [ ] como funciona a busca sequencial;
-   [ ] o que está sendo contado;
-   [ ] por que primeiro e último possuem custos diferentes;
-   [ ] o que significa `n`;
-   [ ] o que significa `T(n)`;
-   [ ] por que o pior caso cresce linearmente;
-   [ ] o significado intuitivo de `O(n)`;
-   [ ] por que Big-O não é tempo em segundos;
-   [ ] por que uma solução correta pode apresentar limitação;
-   [ ] por que a organização dos dados pode importar.

Não é necessário que todos dominem formalmente cada item.

------------------------------------------------------------------------

# 23. Registro pós-aula

Preencher preferencialmente logo após o segundo encontro.

## Execução

**Data(s):**

**Até onde a sequência chegou:**

**Tempo efetivamente utilizado:**

**Ponto em que houve maior discussão:**

------------------------------------------------------------------------

## Turma

**Nível de Python observado:**

**Principais dificuldades técnicas:**

**Principais dificuldades conceituais:**

**Participação oral:**

**Funcionamento de duplas/trios:**

------------------------------------------------------------------------

## Conteúdo

**Conceitos compreendidos rapidamente:**

**Conceitos que exigiram mais tempo:**

**Confusões recorrentes:**

**Perguntas inesperadas dos estudantes:**

------------------------------------------------------------------------

## Notebook Mestre / Reveal.js

**HTML funcionou adequadamente:**

**Código ficou legível:**

**Elementos visuais ajudaram:**

**Slides/células a corrigir:**

**Problemas de navegação/apresentação:**

**Vale manter o formato na Semana 02?**

------------------------------------------------------------------------

## Ajustes futuros

**O que retirar:**

**O que acrescentar:**

**O que simplificar:**

**O que deve permanecer exatamente como está:**

**Implicações para a Semana 02:**

------------------------------------------------------------------------

# 24. Regra final para o professor

Se houver dúvida entre:

> **terminar os slides**

e

> **deixar a turma construir o raciocínio**,

priorizar a segunda opção.

A apresentação é suporte da investigação.

O objetivo da Semana 01 não é chegar ao último slide, mas fazer o
estudante compreender por que, em Estruturas de Dados, precisamos
perguntar:

> **como os dados estão organizados, quais operações precisamos realizar
> e quanto essas operações custam quando a entrada cresce?**

------------------------------------------------------------------------

**Versão:** 1.0\
**EGC5310 --- Semana 01 --- Sequência Didática Detalhada --- 2026/2**
