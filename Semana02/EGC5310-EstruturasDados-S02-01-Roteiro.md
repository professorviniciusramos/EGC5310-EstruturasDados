# EGC5310 — Semana 02 — Roteiro Didático

## Representação de dados e caracterização de problemas computacionais

**Disciplina:** EGC5310 — Tópicos Especiais em Ciência de Dados VI  
**Projeto pedagógico:** Estruturas de Dados  
**Semana:** S02 — 20 e 21 de agosto de 2026  
**Artefato:** 01 — Roteiro Didático  
**Semestre:** 2026/2  
**Carga semanal prevista:** 4 h-aula, distribuídas em dois encontros  
**Tempo didático de referência:** aproximadamente 160 minutos úteis  
**Cenário longitudinal:** Sistema acadêmico  
**Unidade didática:** a semana, e não cada encontro isoladamente  
**Formato principal em experimentação:** Notebook Mestre → Quarto → Reveal.js + Notebook Estudante  
**Notebook Mestre:** `EGC5310-EstruturasDados-S02-99-Aula-Mestre.ipynb`  
**Versão:** 1.0  
**Status:** Planejamento

---

# 1. Finalidade deste roteiro

Este documento registra a concepção pedagógica da **Semana 02 como uma única sequência didática contínua**.

A semana parte da conclusão construída na Semana 01:

> **A forma como organizamos os dados influencia o custo das operações.**

Na Semana 01, uma representação dos registros acadêmicos foi utilizada para investigar uma operação de busca. O foco esteve no comportamento da solução quando o volume de dados cresce.

Na Semana 02, o raciocínio recua deliberadamente uma etapa:

> **Antes de escolher ou analisar um algoritmo, como decidimos representar computacionalmente os dados do problema?**

A semana deverá fazer o estudante perceber que uma representação computacional não é neutra nem existe isoladamente. Sua adequação depende:

- dos dados envolvidos;
- das operações que precisam ser realizadas;
- do volume esperado;
- das relações entre os dados;
- das restrições do problema;
- do trabalho exigido pelas operações.

O **custo das operações aparece nesta semana de maneira qualitativa e intuitiva**, preparando sua investigação sistemática na Semana 03.

Não se pretende ainda realizar uma comparação formal e completa dos custos das operações.

---

# 2. Relação com o Plano de Ensino

O Plano de Ensino estabelece para a Semana 02:

> **Representação de dados e caracterização de problemas computacionais.**

A semana pertence à **Unidade I — Caracterização de problemas de manipulação de dados**, que contempla:

- representação de dados;
- operações fundamentais;
- caracterização de problemas;
- restrições computacionais;
- experimentação inicial.

O objetivo específico mais diretamente relacionado à semana é compreender como diferentes formas de representação influenciam as operações realizadas sobre os dados e caracterizar problemas considerando operações predominantes, requisitos e restrições computacionais.

A Semana 02 concentra-se principalmente em:

> **representação + caracterização**

A Semana 03 avançará para:

> **operações fundamentais + experimentação inicial**

Portanto, a S02 deve criar a **necessidade intelectual** da S03, sem antecipar seu desenvolvimento sistemático.

---

# 3. Relação com a Semana 01

Na Semana 01, o cenário do sistema acadêmico apresentou registros contendo inicialmente:

- matrícula;
- nome;
- curso.

O problema orientador foi localizar um estudante pela matrícula.

A busca sequencial permitiu construir progressivamente a cadeia:

> **problema → dados → operação → solução → custo → crescimento → limitação**

A pergunta central era:

> **Quando uma solução que funciona deixa de ser uma boa solução?**

A Semana 02 não deve reiniciar essa narrativa.

Ela deve começar recuperando uma decisão que passou praticamente despercebida:

> **Nós já recebemos os estudantes organizados de uma determinada maneira. Mas quem decidiu que os dados deveriam ser representados assim?**

Essa pergunta estabelece a transição:

**Semana 01**

> Temos dados organizados dessa maneira.  
> Como podemos operar sobre eles?

**Semana 02**

> Por que os dados estão organizados dessa maneira?  
> Poderiam estar organizados de outra?

**Semana 03**

> Dadas nossas representações e operações, como podemos investigar sistematicamente o trabalho necessário para realizá-las?

---

# 4. Problema orientador

O cenário continua sendo o **Sistema Acadêmico**.

O sistema precisa armazenar inicialmente informações sobre estudantes, como:

- matrícula;
- nome;
- curso.

Entretanto, os requisitos começam a crescer.

Além de localizar um estudante pela matrícula, o sistema deverá ser capaz de responder perguntas como:

- Qual é o curso de determinado estudante?
- Quais estudantes pertencem a determinado curso?
- Quais disciplinas determinado estudante cursou?
- Quais foram suas notas?
- Qual é sua situação em determinada disciplina?
- Como incluir um novo estudante?
- Como alterar uma informação existente?

A pergunta orientadora da semana é:

> **Como devemos representar os dados de um problema para realizar adequadamente as operações de que precisamos?**

Essa pergunta deve anteceder qualquer tentativa de apresentar listas, dicionários ou outras estruturas como soluções prontas.

---

# 5. Pergunta central da semana

A pergunta que deve permanecer visível durante a narrativa é:

> **Existe uma única forma correta de representar os dados de um problema?**

A expectativa é que, progressivamente, a turma perceba que **não**.

Diferentes representações podem:

- armazenar as mesmas informações;
- tornar o código mais ou menos compreensível;
- facilitar determinadas operações;
- dificultar outras;
- exigir diferentes quantidades de trabalho;
- tornar explícitas ou implícitas determinadas relações.

A questão, portanto, não é simplesmente:

> **“Qual estrutura é melhor?”**

mas:

> **“Melhor para quais dados, quais operações e quais condições?”**

---

# 6. Resultados de aprendizagem

Ao final da Semana 02, espera-se que o estudante seja capaz de:

1. distinguir o problema do mundo real de sua representação computacional;
2. identificar entidades, atributos e relações relevantes em um problema simples;
3. reconhecer que o mesmo conjunto de informações pode possuir diferentes representações computacionais;
4. propor representações simples utilizando recursos básicos de Python;
5. identificar as operações necessárias sobre os dados antes de escolher uma representação;
6. comparar qualitativamente vantagens e limitações de representações alternativas;
7. reconhecer que diferentes operações podem ser favorecidas por diferentes representações;
8. relacionar representação, operações, volume de dados e restrições;
9. perceber intuitivamente que representações diferentes podem exigir quantidades diferentes de trabalho para realizar uma mesma operação;
10. justificar uma escolha de representação com base nas características do problema.

Não é necessário que o estudante domine formalmente todos esses elementos ao final da semana. A intenção é estabelecer uma forma de raciocinar que será retomada continuamente durante o semestre.

---

# 7. O que não é objetivo da Semana 02

Não é objetivo desta semana:

- ensinar sistematicamente todas as estruturas nativas de Python;
- apresentar listas, tuplas, conjuntos e dicionários como um catálogo para memorização;
- ensinar hashing;
- concluir que dicionários são sempre superiores a listas;
- aprofundar busca sequencial ou introduzir formalmente busca binária;
- formalizar o custo de todas as operações;
- produzir tabelas de complexidade;
- realizar benchmark formal;
- aprofundar análise assintótica;
- antecipar o conteúdo específico da Semana 03;
- transformar a caracterização do problema em modelagem formal de banco de dados.

Listas, dicionários e outras representações poderão aparecer **como meios para investigar o problema**, não como o conteúdo isolado da semana.

---

# 8. Princípio didático

A sequência deverá seguir aproximadamente:

> **problema → dados → representação inicial → operações necessárias → limitação → representação alternativa → comparação → trabalho esperado → caracterização → nova pergunta**

A formalização deve surgir depois da necessidade.

A pergunta:

> **“Como vamos representar?”**

deve aparecer antes de:

> **“Qual estrutura Python vamos utilizar?”**

Da mesma maneira:

> **“O que precisamos fazer com esses dados?”**

deve aparecer antes de:

> **“Qual representação é melhor?”**

---

# 9. Movimento 1 — Retomar a Semana 01 pela representação

A semana deve começar com uma retomada muito curta.

Recuperar os registros acadêmicos utilizados anteriormente.

Por exemplo:

```python
estudantes = [
    {"matricula": 1023, "nome": "Ana", "curso": "Ciência de Dados"},
    {"matricula": 1047, "nome": "Bruno", "curso": "Ciência de Dados"},
    {"matricula": 1082, "nome": "Carla", "curso": "Engenharia"},
]
```

Não revisar detalhadamente busca sequencial, `T(n)` ou Big-O.

Perguntar:

> **Na semana passada discutimos como procurar um estudante. Mas por que os estudantes estavam representados dessa maneira?**

Em seguida:

> **Essa é a única forma possível?**

O objetivo é transformar algo que na S01 era dado em objeto de investigação na S02.

---

# 10. Movimento 2 — Mundo real não é representação computacional

Apresentar conceitualmente:

**Mundo do problema**

> Estudante  
> matrícula: 1082  
> nome: Carla  
> curso: Engenharia

O computador não possui naturalmente a entidade conceitual “estudante”.

É necessário representá-la.

Uma possibilidade:

```python
[1082, "Carla", "Engenharia"]
```

Outra:

```python
{
    "matricula": 1082,
    "nome": "Carla",
    "curso": "Engenharia"
}
```

Perguntar:

> **As duas representações contêm as mesmas informações?**

Depois:

> **Elas expressam essas informações da mesma maneira?**

E:

> **O que significa `registro[2]`?**

comparado com:

```python
registro["curso"]
```

A discussão deve introduzir a ideia de que representação envolve não apenas armazenar valores, mas também expressar sua **organização e significado**.

---

# 11. Movimento 3 — Primeira atividade no Notebook Estudante

Apresentar um estudante contendo, por exemplo:

- matrícula;
- nome;
- curso;
- semestre de ingresso;
- situação.

Não fornecer imediatamente uma representação.

Solicitar:

> **Como você representaria computacionalmente esse estudante em Python?**

O estudante deve:

1. propor uma representação;
2. implementá-la;
3. acessar pelo menos dois atributos;
4. escrever uma justificativa curta para sua escolha.

## Regra operacional da apresentação

Neste ponto, o Notebook Mestre/Reveal.js deverá apresentar uma chamada visual explícita:

> **AGORA É COM VOCÊ → Notebook Estudante · Atividade 1**

A indicação deve tornar inequívoco que o estudante deve sair da posição passiva da apresentação e trabalhar em seu próprio notebook.

Depois da atividade, retornar à apresentação para discutir alternativas.

---

# 12. Movimento 4 — Uma representação pode funcionar e ainda ser inadequada

Comparar algumas soluções possíveis dos estudantes.

Evitar classificar imediatamente uma representação como “certa” ou “errada”.

Perguntar:

> **Ela armazena as informações necessárias?**

Se sim:

> **Então ela funciona. Mas isso basta?**

Retomar uma ideia importante da Semana 01:

> **Uma solução funcionar não significa necessariamente que seja a solução mais adequada.**

Agora, porém, o objeto da análise não é apenas o algoritmo.

É também a **representação dos dados**.

---

# 13. Movimento 5 — O problema cresce

Adicionar novas necessidades ao Sistema Acadêmico.

Um estudante agora possui disciplinas cursadas.

Para cada vínculo com uma disciplina, podem ser necessários:

- código da disciplina;
- nome;
- semestre;
- nota;
- situação.

Perguntar:

> **Onde colocamos essas informações?**

Depois:

> **O que é um estudante? O que é uma disciplina? O que pertence ao estudante e o que pertence à relação entre estudante e disciplina?**

O objetivo não é ensinar modelagem entidade-relacionamento.

O objetivo é fazer o estudante perceber:

- entidades;
- atributos;
- coleções;
- relações;
- multiplicidade;
- necessidade de representar estrutura, e não apenas valores isolados.

---

# 14. Movimento 6 — Representação depende das operações

Retornar à pergunta fundamental:

> **O que precisamos fazer com os dados?**

Apresentar operações como:

1. localizar estudante pela matrícula;
2. obter o curso de um estudante;
3. listar estudantes de um curso;
4. listar disciplinas cursadas por um estudante;
5. inserir novo estudante;
6. atualizar situação de um estudante.

A turma deve perceber que não é possível discutir adequação da representação sem saber **quais operações serão realizadas**.

Construir explicitamente:

> **dados + operações → requisitos da representação**

---

# 15. Movimento 7 — Introdução intuitiva ao custo das operações

Este movimento é essencial para preparar a Semana 03.

Não formalizar ainda uma tabela de complexidades.

Comparar, por exemplo:

```python
estudantes = [
    {"matricula": 1023, "nome": "Ana"},
    {"matricula": 1047, "nome": "Bruno"},
    {"matricula": 1082, "nome": "Carla"},
]
```

com:

```python
estudantes = {
    1023: {"nome": "Ana"},
    1047: {"nome": "Bruno"},
    1082: {"nome": "Carla"},
}
```

Perguntar:

> **Se queremos encontrar o estudante 1082, parece que fazemos o mesmo tipo de trabalho nas duas representações?**

Não introduzir hashing formalmente.

Não afirmar simplesmente:

> “dicionário é O(1)”.

O objetivo é provocar a percepção de que a organização dos dados modifica o **trabalho necessário para realizar uma operação**.

Em seguida, alterar a operação:

> **E se quisermos listar todos os estudantes de Ciência de Dados?**

Isso impede a conclusão simplista de que uma representação é universalmente superior.

---

# 16. Movimento 8 — Segunda atividade no Notebook Estudante

Fornecer duas ou mais representações pequenas do mesmo conjunto de dados.

Apresentar operações distintas, por exemplo:

- localizar por matrícula;
- listar por curso;
- inserir estudante;
- alterar curso.

Antes de executar qualquer código, solicitar:

> **Para cada operação, qual representação parece mais adequada?**

E:

> **Em qual delas você espera realizar mais trabalho? Por quê?**

## Chamada visual obrigatória

A apresentação deverá indicar:

> **AGORA É COM VOCÊ → Notebook Estudante · Atividade 2**

O estudante deverá registrar sua **previsão antes da execução**.

Depois, poderá realizar pequenas operações e confrontar a previsão com o comportamento observado.

O objetivo ainda não é benchmark.

O objetivo é estabelecer:

> **previsão → execução → interpretação**

---

# 17. Movimento 9 — Caracterizar antes de escolher

A partir das atividades anteriores, construir uma estrutura simples de caracterização de problemas.

A ficha inicial da disciplina será:

> **PROBLEMA → DADOS → OPERAÇÕES → REPRESENTAÇÃO → TRABALHO ESPERADO → VOLUME → RESTRIÇÕES**

## Problema

O que o sistema precisa resolver?

## Dados

Quais informações existem?

Quais entidades, atributos e relações são relevantes?

## Operações

O que precisamos fazer com esses dados?

Pesquisar? Inserir? Atualizar? Percorrer? Relacionar? Agrupar?

## Representação

Como esses dados estão organizados computacionalmente?

## Trabalho esperado

Qual trabalho parece ser necessário para realizar as operações?

Perguntas qualitativas:

- precisamos olhar um elemento?
- vários elementos?
- talvez todos?
- precisamos comparar valores?
- precisamos reorganizar informações?
- uma operação parece mais simples do que outra?

## Volume

Estamos falando de:

- dez registros?
- mil?
- um milhão?

## Restrições

Existem requisitos ou limitações relevantes?

Por exemplo:

- consultas frequentes;
- atualizações frequentes;
- memória;
- legibilidade;
- simplicidade;
- necessidade de preservar determinada organização.

Esta ficha deverá ser reutilizada nas semanas seguintes.

---

# 18. Movimento 10 — Aplicação da caracterização

Apresentar um pequeno requisito do Sistema Acadêmico.

Por exemplo:

> O sistema possui estudantes identificados por matrícula. Consultas por matrícula são muito frequentes. Também precisamos listar estudantes por curso e incluir novos estudantes regularmente.

Solicitar à turma que caracterize:

**Problema:**  
**Dados:**  
**Operações:**  
**Representação possível:**  
**Trabalho esperado:**  
**Volume:**  
**Restrições:**

O objetivo não é obter uma resposta única.

O objetivo é praticar o **processo de caracterização**.

---

# 19. Movimento 11 — A ideia de trade-off

A discussão deve conduzir à percepção de que uma escolha pode favorecer determinada necessidade e não outra.

Introduzir a palavra **trade-off** apenas se ajudar a sintetizar a discussão.

Exemplos qualitativos:

- representação simples × representação mais expressiva;
- acesso conveniente por um atributo × necessidade de percorrer por outro;
- facilidade de inserção × facilidade de consulta;
- legibilidade × economia de memória;
- simplicidade de implementação × desempenho.

Não é necessário aprofundar cada dimensão.

A mensagem principal é:

> **Escolhas computacionais têm consequências.**

---

# 20. Movimento 12 — Terceira atividade: justificar uma decisão

Apresentar um problema pequeno e solicitar:

> **Escolha uma representação para os dados e justifique sua decisão.**

A justificativa não pode ser apenas:

> “porque é mais fácil”

ou:

> “porque dicionário é melhor”.

Ela deve mencionar pelo menos:

- características dos dados;
- operação predominante;
- alguma consequência da escolha.

## Chamada visual

> **AGORA É COM VOCÊ → Notebook Estudante · Atividade 3**

Esta atividade começa a desenvolver uma competência que deverá permanecer durante todo o semestre:

> **justificar tecnicamente uma decisão computacional.**

---

# 21. Introdução ao custo sem antecipar a Semana 03

A S02 não deve terminar sem discutir trabalho computacional.

Entretanto, a linguagem deve permanecer predominantemente qualitativa.

Perguntas adequadas:

> **Quantos elementos parece que precisamos observar?**

> **Precisamos percorrer a coleção inteira?**

> **Essa operação parece exigir mais trabalho quando a coleção cresce?**

> **A representação muda esse trabalho?**

> **Uma representação favorece todas as operações?**

Evitar transformar este momento em uma aula formal de:

- `T(n)`;
- Big-O;
- tabelas de complexidade;
- medição sistemática de tempo;
- benchmarking.

Esses elementos já foram apresentados intuitivamente na S01 e serão retomados quando necessários.

Na Semana 03, a pergunta passará de:

> **“Parece exigir mais trabalho?”**

para:

> **“Como podemos observar, comparar e analisar sistematicamente esse trabalho?”**

---

# 22. Fechamento da semana

Retomar a pergunta central:

> **Existe uma única forma correta de representar os dados de um problema?**

A resposta esperada é:

> **Não. A adequação depende dos dados, das operações e das restrições do problema.**

Construir a síntese:

> **Não escolhemos uma representação isoladamente.**

> **Primeiro caracterizamos o problema.**

> **Identificamos os dados.**

> **Identificamos as operações.**

> **Propomos uma representação.**

> **E perguntamos quais consequências essa escolha produz.**

---

# 23. Pergunta de transição para a Semana 03

Encerrar deixando deliberadamente uma questão sem resposta completa.

Apresentar duas representações e diferentes operações.

Então perguntar:

> **Como podemos comparar de maneira sistemática o trabalho necessário para realizar essas operações quando o volume de dados cresce?**

Não responder completamente.

Essa pergunta constitui a ponte para a Semana 03:

> **Operações fundamentais sobre conjuntos de dados e experimentação inicial.**

A S02 cria a necessidade.

A S03 deverá fornecer instrumentos para investigar essa necessidade.

---

# 24. Distribuição temporal de referência

Os tempos não constituem blocos rígidos.

| Tempo acumulado aproximado | Movimento |
|---:|---|
| 0–10 min | Retomada da S01 pela representação |
| 10–25 min | Mundo real × representação computacional |
| 25–40 min | Comparação inicial de representações |
| 40–55 min | Atividade 1 — propor representação |
| 55–70 min | Discussão das alternativas |
| 70–80 min | Crescimento do problema |
| 80–95 min | Entidades, atributos, coleções e relações |
| 95–110 min | Representação × operações |
| 110–125 min | Custo intuitivo + Atividade 2 |
| 125–140 min | Caracterização do problema |
| 140–150 min | Trade-offs + justificativa |
| 150–160 min | Síntese e pergunta para S03 |

O encontro poderá terminar em qualquer ponto adequado.

No segundo encontro, continuar do ponto em que a investigação tiver sido interrompida.

---

# 25. Papel do Notebook Estudante

Nesta semana, o Notebook Estudante deve assumir papel mais explícito na narrativa.

Ele não será apenas uma versão incompleta do Notebook Mestre.

Deverá conter momentos em que o estudante:

- propõe representações;
- completa estruturas;
- prevê consequências;
- executa pequenas operações;
- compara alternativas;
- registra interpretações;
- justifica decisões.

A apresentação deverá indicar claramente quando o estudante deve utilizá-lo.

Fluxo esperado:

> **APRESENTAÇÃO → PERGUNTA → NOTEBOOK ESTUDANTE → PRODUÇÃO → DISCUSSÃO → APRESENTAÇÃO**

As transições devem fazer parte da narrativa da aula.

---

# 26. Regra para as chamadas ao Notebook Estudante

Sempre que houver uma atividade que exija ação do estudante no notebook, o Notebook Mestre deverá gerar uma indicação visual explícita na apresentação.

Padrão conceitual:

> **AGORA É COM VOCÊ → Notebook Estudante · Atividade N**

A chamada deverá:

- ser visualmente reconhecível;
- utilizar padrão consistente;
- identificar a atividade correspondente;
- não ocupar necessariamente um slide exclusivo;
- indicar claramente que há mudança de instrumento.

A Sequência Didática deverá registrar também essas transições.

---

# 27. Benchmark

Não está previsto benchmark formal para a Semana 02.

Não serão necessários:

`EGC5310-EstruturasDados-S02-05-Benchmark.py`

`EGC5310-EstruturasDados-S02-05-Benchmark.csv`

`EGC5310-EstruturasDados-S02-05-Benchmark.md`

Pequenas execuções comparativas podem ocorrer dentro dos notebooks.

Elas terão função de **exploração didática**, não de benchmark sistemático.

A experimentação formal passa a ganhar maior importância na Semana 03.

---

# 28. Artefatos previstos

## Planejamento e condução

- `EGC5310-EstruturasDados-S02-01-Roteiro.md`
- `EGC5310-EstruturasDados-S02-01A-Sequencia-Didatica.md`
- `EGC5310-EstruturasDados-S02-01B-Resumo-Professor.md`

## Fonte principal da aula

- `EGC5310-EstruturasDados-S02-99-Aula-Mestre.ipynb`

O Notebook Mestre é a fonte da narrativa e da apresentação gerada por Quarto/Reveal.js.

Não inserir no notebook configurações de `format` que possam recriar conflitos de renderização.

## Participação do estudante

- `EGC5310-EstruturasDados-S02-04-Estudante.ipynb`

## Atividades complementares

- `EGC5310-EstruturasDados-S02-06-Exercicios.md`
- `EGC5310-EstruturasDados-S02-07-Solucoes.md`

## Revisão

- `EGC5310-EstruturasDados-S02-08-Revisao.md`

---

# 29. O que observar durante a execução

## Compreensão conceitual

Observar se os estudantes:

- distinguem dado de representação;
- conseguem identificar entidades e atributos;
- percebem que existem representações alternativas;
- relacionam representação às operações;
- conseguem justificar uma escolha;
- percebem intuitivamente diferenças de trabalho computacional.

## Python

Observar:

- familiaridade com listas;
- familiaridade com dicionários;
- acesso a elementos;
- criação de estruturas aninhadas;
- dificuldades de sintaxe que possam interferir na discussão conceitual.

Não transformar dificuldades pontuais de Python no conteúdo principal da semana.

## Dinâmica

Observar:

- participação nas atividades;
- qualidade das justificativas;
- tempo necessário para trocar entre apresentação e Notebook Estudante;
- clareza das chamadas visuais;
- necessidade de trabalho em duplas ou trios.

## Formato Notebook Mestre / Reveal.js

Avaliar especialmente:

- se as chamadas ao Notebook Estudante são percebidas;
- se a transição apresentação → atividade é natural;
- se o retorno à apresentação funciona;
- se há excesso de troca de janelas;
- se o formato favorece a participação;
- se o Notebook Mestre continua simples de manter.

Essas observações deverão alimentar `S02-08-Revisao.md`.

---

# 30. Critério de sucesso da Semana 02

A semana terá cumprido sua função se o estudante sair dela compreendendo que:

> **dados não chegam ao programa com uma representação inevitável; nós fazemos escolhas sobre como representá-los.**

E que:

> **essas escolhas precisam ser avaliadas em função das operações que o problema exige.**

Mais importante ainda, deve surgir naturalmente a percepção:

> **representações diferentes podem fazer uma mesma operação exigir diferentes quantidades de trabalho.**

Não é necessário ainda saber comparar formalmente todos esses custos.

É necessário perceber que **há algo a comparar**.

---

# 31. Regra final para o professor

Se a turma perguntar:

> **“Então qual representação é melhor?”**

evitar responder imediatamente com o nome de uma estrutura.

Devolver:

> **“Melhor para fazer o quê?”**

Essa pergunta sintetiza a Semana 02.

E deve preparar a pergunta da semana seguinte:

> **“Quanto custa fazer isso?”**

---

**Versão:** 1.0  
**EGC5310 — Semana 02 — Roteiro Didático — 2026/2**