# EGC5310 — Semana 02 — Sequência Didática

## Representação de dados e caracterização de problemas computacionais

**Disciplina:** EGC5310 — Tópicos Especiais em Ciência de Dados VI  
**Semana:** S02 — 20 e 21 de agosto de 2026  
**Artefato:** 01A — Sequência Didática  
**Cenário longitudinal:** Sistema Acadêmico  
**Tempo didático de referência:** aproximadamente 160 minutos úteis  
**Fonte principal:** `EGC5310-EstruturasDados-S02-99-Aula-Mestre.ipynb`  
**Material de participação:** `EGC5310-EstruturasDados-S02-04-Estudante.ipynb`

---

# 1. Finalidade deste documento

Este documento descreve **como conduzir a Semana 02 em sala**.

Ele complementa o Roteiro Didático e deve permitir que o professor, mesmo depois de um longo intervalo, recupere rapidamente:

- a história que deve ser construída;
- a sequência dos movimentos;
- as perguntas que devem ser feitas;
- os momentos de código;
- os momentos de participação dos estudantes;
- as respostas que não devem ser antecipadas;
- as evidências de compreensão que devem ser observadas;
- as transições entre apresentação e Notebook Estudante;
- a pergunta que deve permanecer aberta para a Semana 03.

A sequência não depende rigidamente da numeração dos slides.

Os slides podem ser reorganizados sem alterar a lógica descrita aqui.

---

# 2. Ideia central da semana

A Semana 01 partiu de uma representação já existente e investigou uma operação sobre ela.

A Semana 02 pergunta:

> **Por que os dados foram representados daquela maneira?**

A história da semana deve conduzir progressivamente à conclusão:

> **Uma representação de dados deve ser avaliada em relação às operações que precisamos realizar.**

E, no final:

> **Representações diferentes podem fazer uma mesma operação exigir diferentes quantidades de trabalho.**

A segunda afirmação não deve ser completamente desenvolvida nesta semana.

Ela deve produzir a pergunta que abrirá a Semana 03.

---

# 3. Preparação antes da aula

## Verificações técnicas

Antes da aula:

- abrir o Notebook Mestre;
- verificar a renderização Quarto/Reveal.js;
- confirmar que todas as células necessárias foram executadas;
- verificar se o Notebook Estudante abre corretamente;
- verificar compatibilidade com Google Colab;
- conferir se as atividades possuem a mesma numeração na apresentação e no Notebook Estudante;
- testar as chamadas visuais para o Notebook Estudante;
- confirmar que nenhuma configuração `format` foi reintroduzida no Notebook Mestre;
- manter uma versão local funcional dos materiais.

## Verificações didáticas

Antes da aula, lembrar:

- não transformar a semana em revisão da S01;
- não transformar a semana em catálogo de estruturas Python;
- não explicar antecipadamente qual representação é “melhor”;
- não ensinar hashing ao mostrar dicionários;
- não aprofundar Big-O;
- introduzir custo como **trabalho esperado**, não como tabela de complexidades;
- deixar a pergunta sobre comparação sistemática de custos aberta para a S03.

---

# 4. Regra operacional para atividades

Sempre que a narrativa chegar a uma atividade do estudante, seguir o ciclo:

> **APRESENTAÇÃO → CHAMADA VISUAL → NOTEBOOK ESTUDANTE → TEMPO DE TRABALHO → DISCUSSÃO → RETORNO À APRESENTAÇÃO**

A apresentação deverá mostrar explicitamente:

> **AGORA É COM VOCÊ → Notebook Estudante · Atividade N**

Não continuar explicando enquanto os estudantes deveriam estar trabalhando.

Após a atividade, sinalizar também verbalmente o retorno:

> “Vamos voltar para a apresentação e comparar as soluções.”

Essa alternância deverá ser testada deliberadamente nesta semana.

---

# 5. Movimento 1 — Recuperar a Semana 01 sem revisá-la

**Tempo de referência:** 0–10 min

## Apresentar

Mostrar novamente uma pequena coleção de estudantes semelhante à utilizada na S01:

```python
estudantes = [
    {"matricula": 1023, "nome": "Ana", "curso": "Ciência de Dados"},
    {"matricula": 1047, "nome": "Bruno", "curso": "Ciência de Dados"},
    {"matricula": 1082, "nome": "Carla", "curso": "Engenharia"},
]
```

## Perguntar

> “O que fizemos com esses dados na semana passada?”

Esperar que apareçam ideias como:

- procurar;
- buscar matrícula;
- percorrer;
- comparar;
- busca sequencial.

Não gastar tempo reconstruindo toda a análise.

Depois perguntar:

> **“Mas por que os dados estavam organizados dessa maneira?”**

Pausa.

> **“Quem decidiu que um estudante seria representado assim?”**

Finalmente:

> **“Essa é a única maneira possível?”**

## Objetivo

Deslocar o objeto de investigação:

**S01:** operação sobre uma representação.

**S02:** a própria representação.

## Observar

Os estudantes percebem que a estrutura utilizada na S01 foi uma **escolha**?

Se isso aparecer espontaneamente, avançar.

---

# 6. Movimento 2 — Separar realidade e representação

**Tempo de referência:** 10–25 min

## Apresentar

No mundo do problema:

> Estudante  
> matrícula = 1082  
> nome = Carla  
> curso = Engenharia

Perguntar:

> **“Isso existe dessa maneira dentro do computador?”**

Conduzir para:

> Precisamos representar essas informações.

Mostrar:

```python
estudante = [1082, "Carla", "Engenharia"]
```

Perguntar:

> “Funciona?”

A resposta é sim.

Depois:

```python
estudante[2]
```

Perguntar:

> **“O que significa o 2?”**

Não responder imediatamente.

Em seguida mostrar:

```python
estudante = {
    "matricula": 1082,
    "nome": "Carla",
    "curso": "Engenharia"
}
```

e:

```python
estudante["curso"]
```

## Perguntas

> “As duas representações guardam as mesmas informações?”

> “As duas expressam essas informações da mesma maneira?”

> “Qual delas permite entender melhor o significado de cada valor?”

> “Isso significa que uma delas é sempre melhor?”

A última pergunta deve ficar em aberto.

## Conclusão provisória

> **Os mesmos dados podem ser representados de maneiras diferentes.**

Ainda não concluir:

> “dicionários são melhores”.

---

# 7. Movimento 3 — Atividade 1: representar antes de receber a solução

**Tempo de referência:** 25–45 min

## Apresentar o problema

Um estudante possui:

- matrícula;
- nome;
- curso;
- semestre de ingresso;
- situação acadêmica.

Perguntar:

> **“Como vocês representariam esse estudante em Python?”**

Não mostrar solução.

## Chamada

### AGORA É COM VOCÊ → Notebook Estudante · Atividade 1

Pedir que os estudantes:

1. proponham uma representação;
2. implementem;
3. recuperem dois atributos;
4. escrevam uma frase justificando a escolha.

## Durante a atividade

Circular pela sala.

Não corrigir imediatamente representações diferentes.

Perguntar individualmente:

> “Por que você escolheu isso?”

> “Como você acessaria o curso?”

> “Se eu acrescentar um atributo, o que muda?”

## Observar

- quem utiliza lista;
- quem utiliza dicionário;
- quem tenta criar classe;
- quem apresenta dificuldades básicas de Python;
- quem justifica semanticamente;
- quem justifica apenas pela familiaridade.

## Retorno

Dizer:

> **“Vamos voltar para a apresentação. Não estamos procurando ainda uma única resposta correta.”**

Selecionar algumas alternativas para discussão.

---

# 8. Movimento 4 — Funcionar não significa ser adequado

**Tempo de referência:** 45–60 min

Apresentar duas ou três representações possíveis.

Perguntar sobre cada uma:

> “Ela consegue armazenar os dados?”

Se sim:

> **“Então ela funciona. Isso significa que ela é adequada?”**

Recuperar discretamente a S01:

> “Na semana passada já vimos que uma solução pode funcionar e ainda assim merecer investigação.”

Agora acrescentar:

> **“O mesmo vale para a representação.”**

## Pergunta importante

> **“Adequada para quê?”**

Essa pergunta deve começar a aparecer repetidamente.

## Evidência de compreensão

O estudante começa a perceber que não consegue avaliar adequação sem conhecer **o que será feito com os dados**.

---

# 9. Movimento 5 — Fazer o problema crescer

**Tempo de referência:** 60–80 min

Agora informar:

> “O sistema acadêmico precisa guardar também as disciplinas cursadas.”

Uma disciplina cursada pode possuir:

- código;
- nome;
- semestre;
- nota;
- situação.

Perguntar:

> **“Onde colocamos isso?”**

Permitir propostas.

Depois:

> “Disciplina é um atributo simples do estudante?”

> “Um estudante pode cursar quantas disciplinas?”

> “Uma disciplina pode possuir quantos estudantes?”

> “A nota pertence à disciplina ou à relação daquele estudante com aquela disciplina?”

Não aprofundar modelagem de bancos de dados.

## Objetivo

Fazer aparecer intuitivamente:

- entidade;
- atributo;
- coleção;
- relação;
- multiplicidade.

## Frase de transição

> **“Representar dados não é apenas colocar valores dentro de variáveis. Precisamos representar também a organização existente entre eles.”**

---

# 10. Possível interrupção entre os encontros

Este é um ponto natural para eventual encerramento do primeiro encontro.

Se o tempo terminar antes ou depois deste movimento, não forçar o fechamento.

No encontro seguinte, recuperar rapidamente:

> **“Na última aula percebemos que representar um estudante era simples até o problema começar a crescer.”**

E continuar.

Não fazer uma nova introdução completa.

---

# 11. Movimento 6 — Começar pelas operações

**Tempo de referência:** 80–100 min

Apresentar as necessidades do sistema:

1. localizar estudante pela matrícula;
2. obter o curso;
3. listar estudantes de determinado curso;
4. listar disciplinas de um estudante;
5. inserir estudante;
6. atualizar uma informação.

Perguntar:

> **“A representação que escolhemos facilita todas essas operações igualmente?”**

Esperar.

Depois:

> **“Podemos decidir se uma representação é adequada sem saber o que faremos com os dados?”**

Construir com a turma:

> **DADOS + OPERAÇÕES → REQUISITOS DA REPRESENTAÇÃO**

## Ponto-chave

Não apresentar ainda a estrutura como resposta.

A ordem de raciocínio deve ser:

1. problema;
2. dados;
3. operações;
4. representação possível.

Não:

1. conheço um dicionário;
2. vou usar um dicionário;
3. depois vejo se funciona.

---

# 12. Movimento 7 — Introduzir intuitivamente o trabalho necessário

**Tempo de referência:** 100–115 min

Apresentar:

```python
estudantes = [
    {"matricula": 1023, "nome": "Ana"},
    {"matricula": 1047, "nome": "Bruno"},
    {"matricula": 1082, "nome": "Carla"},
]
```

Perguntar:

> **“Para encontrar 1082, o que precisamos fazer?”**

A turma já conhece a resposta da S01.

Agora apresentar:

```python
estudantes = {
    1023: {"nome": "Ana"},
    1047: {"nome": "Bruno"},
    1082: {"nome": "Carla"},
}
```

Perguntar:

> **“Parece que precisamos fazer o mesmo tipo de trabalho?”**

Não explicar hashing.

Não apresentar `O(1)`.

Não fazer tabela de complexidade.

## Alterar imediatamente a operação

Perguntar:

> **“Agora quero todos os estudantes de Ciência de Dados. Qual representação ganhou?”**

Se alguém disser “dicionário é mais rápido”, perguntar:

> **“Mais rápido para qual operação?”**

Essa é uma das perguntas mais importantes da aula.

## Conclusão

> **Uma representação pode favorecer determinadas operações sem favorecer todas.**

---

# 13. Movimento 8 — Atividade 2: prever antes de executar

**Tempo de referência:** 115–130 min

Apresentar duas representações do mesmo conjunto de dados.

Fornecer operações como:

- localizar matrícula;
- listar estudantes por curso;
- inserir estudante;
- alterar informação.

## Chamada

### AGORA É COM VOCÊ → Notebook Estudante · Atividade 2

Solicitar que, **antes de executar**, o estudante registre:

1. qual representação escolheria para cada operação;
2. qual parece exigir menos trabalho;
3. por quê.

Depois permitir pequenas execuções.

## Pergunta após execução

> **“Sua previsão mudou?”**

> **“O que você observou?”**

## Objetivo

Estabelecer:

> **PREVISÃO → EXECUÇÃO → INTERPRETAÇÃO**

Não medir sistematicamente tempo.

Não fazer benchmark.

---

# 14. Movimento 9 — Construir a ficha de caracterização

**Tempo de referência:** 130–145 min

Agora formalizar parcialmente aquilo que já apareceu.

Não apresentar a ficha no início da aula.

Ela deve surgir como síntese.

Construir:

> **PROBLEMA → DADOS → OPERAÇÕES → REPRESENTAÇÃO → TRABALHO ESPERADO → VOLUME → RESTRIÇÕES**

Percorrer rapidamente cada item.

## Problema

> “O que precisa ser resolvido?”

## Dados

> “Que informações temos?”

## Operações

> “O que precisamos fazer com elas?”

## Representação

> “Como vamos organizá-las computacionalmente?”

## Trabalho esperado

> “O que parece ser necessário para realizar essas operações?”

Usar linguagem qualitativa:

- um elemento;
- vários;
- todos;
- comparar;
- percorrer;
- reorganizar.

## Volume

> “Dez registros ou dez milhões?”

## Restrições

> “Há alguma condição que afete nossa decisão?”

## Objetivo

Dar nome e organização ao processo de raciocínio desenvolvido durante a aula.

---

# 15. Movimento 10 — Aplicar a ficha

Apresentar:

> “O sistema possui estudantes identificados por matrícula. Consultas por matrícula são frequentes. Também precisamos listar estudantes por curso e incluir novos estudantes regularmente.”

Construir coletivamente ou em pequenos grupos:

**Problema:**  
**Dados:**  
**Operações:**  
**Representação:**  
**Trabalho esperado:**  
**Volume:**  
**Restrições:**

Não buscar uma resposta única.

Perguntar:

> **“O que muda se a operação predominante mudar?”**

Essa pergunta é mais importante que a representação escolhida.

---

# 16. Movimento 11 — Introduzir trade-offs

Mostrar que decisões podem favorecer aspectos diferentes.

Exemplos:

- clareza × compactação;
- acesso por determinado atributo × busca por outro;
- facilidade de inserção × facilidade de consulta;
- simplicidade × desempenho.

Perguntar:

> **“Existe uma escolha sem consequências?”**

Introduzir, se apropriado:

> **trade-off**

Explicar apenas como:

> ganhar alguma coisa em determinada dimensão pode significar aceitar uma desvantagem em outra.

Não transformar o conceito em exposição longa.

---

# 17. Movimento 12 — Atividade 3: justificar

**Tempo de referência:** 145–152 min

Apresentar um pequeno requisito.

Por exemplo:

> Um sistema precisa armazenar estudantes e realiza principalmente consultas por matrícula. Eventualmente precisa listar estudantes por curso.

## Chamada

### AGORA É COM VOCÊ → Notebook Estudante · Atividade 3

Solicitar:

> **“Escolha uma representação e justifique.”**

A justificativa deve mencionar:

- os dados;
- pelo menos uma operação predominante;
- uma consequência da escolha.

## Não aceitar como justificativa suficiente

> “porque é mais fácil”

> “porque dicionário é melhor”

> “porque Python tem essa estrutura”

Perguntar:

> **“Melhor para fazer o quê?”**

---

# 18. Movimento 13 — Síntese da semana

**Tempo de referência:** 152–156 min

Retomar a pergunta:

> **“Existe uma única forma correta de representar os dados?”**

Construir com a turma:

1. temos um problema;
2. identificamos os dados;
3. identificamos as operações;
4. escolhemos uma representação;
5. avaliamos suas consequências.

Mostrar novamente:

> **PROBLEMA → DADOS → OPERAÇÕES → REPRESENTAÇÃO → TRABALHO ESPERADO → VOLUME → RESTRIÇÕES**

Perguntar:

> **“O que está faltando para tomarmos decisões melhores?”**

Esperar ideias relacionadas a:

- medir;
- comparar;
- analisar;
- saber quanto custa;
- testar com mais dados.

Não corrigir rapidamente se essas palavras aparecerem de formas diferentes.

É exatamente a direção desejada.

---

# 19. Movimento 14 — Criar a necessidade da Semana 03

**Tempo de referência:** 156–160 min

Retomar duas representações diferentes.

Perguntar:

> **“Dissemos várias vezes que uma operação parece exigir mais ou menos trabalho.”**

Pausa.

Depois:

> **“Mas ‘parece’ é suficiente?”**

E finalmente:

> **“Como podemos comparar de maneira sistemática o trabalho necessário para realizar essas operações quando o volume de dados cresce?”**

Não responder.

Encerrar.

A última ideia da S02 deve ser uma pergunta.

A primeira ideia da S03 poderá ser a retomada dessa pergunta.

---

# 20. Perguntas importantes da semana

Não é necessário usar todas literalmente, mas estas perguntas orientam a condução:

> “Por que representamos os dados assim?”

> “Essa é a única forma?”

> “Funciona. Mas é adequada?”

> “Adequada para quê?”

> “O que precisamos fazer com esses dados?”

> “Essa representação favorece todas as operações?”

> “Quanto trabalho parece ser necessário?”

> “O que acontece quando o volume cresce?”

> “Mais rápido para qual operação?”

> “O que muda se a operação predominante mudar?”

> “Qual é a consequência da sua escolha?”

> “Como você justificaria essa decisão?”

> “'Parece mais rápido' é suficiente?”

> “Como poderíamos comparar isso sistematicamente?”

---

# 21. Respostas que não devem ser antecipadas

Evitar fornecer cedo demais:

- “use dicionário”;
- “dicionário é O(1)”;
- “lista é O(n)”;
- “hashing resolve”;
- “esta é a melhor estrutura”;
- tabelas prontas de complexidade.

A narrativa depende de os estudantes perceberem primeiro o **problema da escolha**.

A formalização deverá responder a uma necessidade que já apareceu.

---

# 22. Evidências de aprendizagem

## Evidência 1

O estudante consegue propor mais de uma representação possível para os mesmos dados.

## Evidência 2

Consegue explicar uma diferença entre:

```python
registro[2]
```

e:

```python
registro["curso"]
```

sem reduzir a explicação apenas à sintaxe.

## Evidência 3

Quando perguntado:

> “Qual representação é melhor?”

responde espontaneamente algo próximo de:

> “Depende do que precisamos fazer.”

## Evidência 4

Consegue identificar operações relevantes antes de escolher a representação.

## Evidência 5

Percebe que uma representação pode favorecer uma operação e não outra.

## Evidência 6

Consegue utilizar linguagem qualitativa sobre trabalho computacional:

- percorrer;
- comparar;
- olhar vários elementos;
- olhar todos;
- acessar diretamente;
- reorganizar.

## Evidência 7

Consegue justificar uma escolha mencionando problema, dados ou operações.

---

# 23. Sinais de dificuldade

Observar se os estudantes:

- tratam representação como sinônimo de sintaxe Python;
- acreditam que existe uma estrutura universalmente melhor;
- escolhem estruturas apenas por familiaridade;
- confundem dado com posição;
- apresentam dificuldade com estruturas aninhadas;
- não conseguem identificar as operações do problema;
- concluem que “mais rápido” é propriedade absoluta da estrutura;
- repetem Big-O da S01 sem relacioná-lo ao problema atual.

Nesses casos, voltar ao exemplo concreto.

Evitar responder com mais formalização abstrata.

---

# 24. Se faltar tempo

Priorizar:

1. realidade × representação;
2. Atividade 1;
3. representação × operações;
4. introdução qualitativa ao trabalho;
5. Atividade 2;
6. ficha de caracterização;
7. pergunta final para S03.

A Atividade 3 pode ser:

- reduzida;
- feita oralmente;
- incorporada aos exercícios;
- deixada para consolidação posterior.

Não sacrificar a pergunta final da S03 para concluir todas as atividades.

---

# 25. Se sobrar tempo

Não antecipar a Semana 03 formalmente.

Usar novos requisitos do Sistema Acadêmico.

Exemplos:

> “Agora precisamos localizar estudantes também pelo CPF.”

> “Agora precisamos listar estudantes por semestre de ingresso.”

> “Agora há dez milhões de registros.”

> “Agora inserções acontecem continuamente.”

Perguntar sempre:

> **“Isso altera nossa decisão?”**

O tempo adicional deve aprofundar a caracterização, não antecipar estruturas futuras.

---

# 26. Papel do professor durante as atividades

Durante as atividades, evitar transformar circulação pela sala em correção individual de código.

Priorizar perguntas:

> “Por que?”

> “O que essa posição significa?”

> “Que operação você está tentando favorecer?”

> “O que aconteceria se tivéssemos mais dados?”

> “Sua representação ainda funcionaria?”

> “Qual consequência você aceita nessa escolha?”

A intenção é fazer o estudante **explicitar seu modelo mental**.

---

# 27. Relação com o CPMD

A semana deve reforçar competências iniciais do ciclo:

**Problema → Dados → Operações → Hipóteses**

O Sistema Acadêmico continua como cenário da primeira metade do semestre.

Não é necessário construir um sistema completo.

A cada semana, o cenário fornece um problema de manipulação de dados que permite investigar uma decisão computacional.

Nesta semana, a decisão investigada é:

> **como representar os dados diante das operações necessárias.**

---

# 28. Registro pós-aula

Após a execução da S02, registrar no documento de revisão:

## Narrativa

- A retomada da S01 funcionou?
- A pergunta sobre representação foi compreendida?
- A progressão problema → dados → operações → representação ficou clara?
- A introdução qualitativa ao custo foi suficiente?
- A pergunta final criou interesse para S03?

## Notebook Estudante

- Os estudantes perceberam as chamadas visuais?
- Abriram o notebook no momento correto?
- Houve demora excessiva na transição?
- As atividades estavam claramente identificadas?
- A previsão antes da execução funcionou?

## Python

- Quais dificuldades apareceram?
- Listas e dicionários eram familiares?
- Estruturas aninhadas foram excessivamente complexas?
- Foi necessário ensinar sintaxe não planejada?

## Tempo

- Onde terminou o primeiro encontro?
- Quanto tempo cada atividade efetivamente consumiu?
- O que foi reduzido?
- O que não foi realizado?

## Formato

- Notebook Mestre + Quarto funcionou melhor que na S01?
- As chamadas ao Notebook Estudante reduziram a desconexão entre materiais?
- Houve excesso de troca entre janelas?
- Alguma chamada deveria estar em slide próprio?
- O retorno do Notebook Estudante à apresentação foi natural?

## Continuidade

Registrar explicitamente a última pergunta deixada para a turma:

> **“Como podemos comparar sistematicamente o trabalho necessário para realizar essas operações quando o volume de dados cresce?”**

Essa informação deverá ser consultada antes de preparar a execução da Semana 03.

---

# 29. Mapa rápido da condução

Se for necessário recuperar a sequência rapidamente:

**1.** Mostrar dados da S01.  
**2.** Perguntar por que estavam representados assim.  
**3.** Comparar duas representações.  
**4.** Estudante propõe uma representação.  
**5.** Fazer o problema crescer.  
**6.** Perguntar quais operações serão necessárias.  
**7.** Relacionar representação e trabalho esperado.  
**8.** Estudante prevê antes de executar.  
**9.** Construir a ficha de caracterização.  
**10.** Discutir trade-offs.  
**11.** Pedir justificativa de uma escolha.  
**12.** Perguntar se “parece mais rápido” é suficiente.  
**13.** Deixar a comparação sistemática para a S03.

---

# 30. Frase-guia do professor

Se durante a aula houver dúvida sobre qual direção seguir, retornar à pergunta:

> **“Melhor para fazer o quê?”**

Ela reconecta:

**problema → dados → operações → representação → consequências**

e mantém a Semana 02 dentro de seu objetivo.

---

**Versão:** 1.0  
**EGC5310 — Semana 02 — Sequência Didática — 2026/2**