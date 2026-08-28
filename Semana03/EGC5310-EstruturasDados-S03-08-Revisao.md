# EGC5310 — Estruturas de Dados
## Semana 03 — Revisão e registro pós-aula

**Arquivo:** `EGC5310-EstruturasDados-S03-08-Revisao.md`

**Tema da semana:** Operações sobre dados: inserir, remover, ordenar e medir.

Este documento deve ser preenchido **após a execução da Semana 03**. Seu objetivo é registrar evidências para o planejamento da Semana 04 e para a evolução do formato Notebook Mestre + Quarto/Reveal.js + Notebook Estudante.

Não preencher com expectativas antes da aula. Quando uma informação não puder ser observada, registrar **“não observado”** ou **“não sei”**.

---

# 1. Síntese da proposta executada

A Semana 03 foi planejada para avançar da pergunta da S02:

> **Como representar os dados para aquilo que queremos fazer?**

para:

> **O que acontece quando realizamos diferentes operações sobre essas representações?**

A semana deveria investigar:

- acesso;
- inserção;
- remoção;
- ordenação;
- sequência de operações;
- custo amortizado;
- benchmark;
- processamento em lote;
- `list` × `DataFrame`;
- JSON como representação/intercâmbio;
- diferença entre Big-O e tempo medido.

A formulação conceitual de fechamento prevista era:

> **Não existe “o custo de uma estrutura”. Existe o custo de uma operação, sobre uma representação, dentro de uma sequência de operações.**

---

# 2. Narrativa didática

Registrar:

- O abandono da busca sequencial como problema principal evitou sensação de repetição?
- O problema de inserção/remoção foi compreendido como uma evolução natural da S02?
- `append()` foi uma boa provocação inicial?
- A passagem de código → mecanismo → Big-O funcionou?
- A ideia de que “uma linha de código não representa uma quantidade fixa de trabalho” ficou clara?
- A progressão `list` → sequência de operações → benchmark → DataFrame → JSON funcionou?
- A comparação entre representações pareceu integrada ao problema ou um bloco separado?
- A formulação final sobre operação + representação + sequência foi compreendida?
- A ponte para busca sequencial × busca binária despertou interesse para a S04?

**Registro:**

> Preencher após a aula.

---

# 3. Profundidade conceitual

A S03 foi deliberadamente mais profunda que S01 e S02, mas sem antecipar estruturas futuras.

Registrar:

- O nível de aprofundamento foi adequado para estudantes do segundo semestre?
- Tamanho × capacidade foi compreendido?
- O mecanismo de deslocamento em `insert(0, ...)` e `pop(0)` foi compreendido?
- “Custo amortizado” ajudou ou acrescentou complexidade excessiva?
- `O(n log n)` pôde ser mencionado sem exigir explicação prematura de algoritmos de ordenação?
- O primeiro contato com `O(n²)` por concatenações sucessivas foi compreendido?
- A turma distinguiu mecanismo, modelo assintótico e medição experimental?
- Algum conceito deveria ser retomado na S04?

**Registro:**

> Preencher após a aula.

---

# 4. Python e `lambda`

Na S02, classes e objetos foram a principal dificuldade de Python. Por isso, a S03 deveria utilizar prioritariamente listas, dicionários e funções simples.

Registrar:

- Listas e dicionários continuaram suficientemente familiares?
- Foi necessário explicar alguma sintaxe não prevista?
- A função nomeada com `def` antes da `lambda` funcionou?
- Os estudantes compreenderam `key=obter_nota`?
- A equivalência entre:

```python
def obter_nota(aluno):
    return aluno["nota"]
```

e:

```python
lambda aluno: aluno["nota"]
```

ficou clara?
- Dois momentos/slides foram suficientes para introduzir `lambda`?
- A `lambda` desviou a atenção da discussão sobre ordenação?
- Vale utilizar `lambda` naturalmente nas próximas semanas ou ainda é necessário reforço?

**Registro:**

> Preencher após a aula.

---

# 5. Operações em `list`

Registrar:

- Os estudantes já conheciam `append()`?
- Já conheciam `insert()`?
- Já conheciam `pop()`?
- A diferença entre inserir/remover no início e no final foi intuitiva?
- Os diagramas de deslocamento ajudaram?
- A turma conseguiu prever quais operações dependeriam de `n`?
- Houve alguma interpretação equivocada importante?
- A tabela de operações foi útil como formalização posterior?

**Registro:**

> Preencher após a aula.

---

# 6. Notebook Estudante

Na S02, as chamadas visuais foram percebidas e a previsão antes da execução funcionou, mas os estudantes não realizavam uma transição explícita de volta à apresentação.

Registrar:

- As chamadas visuais foram percebidas?
- O botão/link no Notebook Mestre foi útil?
- Os estudantes abriram o notebook no momento esperado?
- A transição ocorreu sem demora excessiva?
- A atividade de previsão foi efetivamente realizada antes da execução?
- Os estudantes registraram hipóteses ou apenas responderam oralmente?
- As atividades estavam claramente identificadas?
- Houve necessidade de alternância excessiva entre materiais?
- A retomada da projeção pelo professor funcionou naturalmente?
- O Notebook Estudante está se consolidando como material útil ou ainda parece artificial?
- Alguma atividade deveria estar diretamente no Notebook Mestre em vez do Notebook Estudante?

**Registro:**

> Preencher após a aula.

---

# 7. Benchmark

Na S02, o benchmark planejado não chegou a ser realizado. Na S03 ele foi incorporado ao núcleo da semana.

Registrar:

- O benchmark foi efetivamente executado?
- Quanto tempo consumiu?
- Os estudantes formularam hipóteses antes das medições?
- `append()` × `insert(0, ...)` produziu diferença visualmente útil?
- `pop()` × `pop(0)` produziu diferença visualmente útil?
- O experimento DataFrame incremental × lote foi suficientemente marcante?
- Os tamanhos de entrada estavam adequados?
- Algum experimento demorou excessivamente?
- Houve ruído que dificultou a interpretação?
- A mediana das repetições foi compreendida?
- A turma percebeu que benchmark não prova Big-O?
- A pergunta “como a diferença muda com `n`?” foi mais produtiva do que “qual foi mais rápido?”?
- O benchmark deve continuar como elemento recorrente das próximas semanas?
- O benchmark oficial e o executado pelos estudantes produziram tendências semelhantes?

**Registro:**

> Preencher após a aula.

---

# 8. DataFrame

Este bloco deveria responder explicitamente por que DataFrames são tão frequentes em Ciência de Dados sem tratá-los como universalmente melhores.

Registrar:

- A pergunta “por que todo mundo usa DataFrame?” gerou discussão?
- Os estudantes já utilizavam pandas/DataFrame anteriormente?
- Eles associavam DataFrame automaticamente a qualquer problema com dados?
- A ideia de abstração tabular ficou clara?
- Operações por coluna, filtro e `groupby` ajudaram a justificar a importância do DataFrame?
- A turma compreendeu por que processamento em lote é importante?
- A comparação incremental × lote foi convincente?
- A turma compreendeu que DataFrame não é necessariamente melhor para inserções registro a registro?
- A distinção entre “mesma classe Big-O” e “mesmo tempo” ficou clara?
- Vetorização e código compilado foram suficientes como explicação qualitativa?
- Alguma explicação entrou prematuramente em detalhes de pandas/NumPy?

**Registro:**

> Preencher após a aula.

---

# 9. JSON

Registrar:

- Os estudantes já conheciam JSON?
- Eles tratavam JSON como uma estrutura equivalente a `list` ou DataFrame?
- A distinção entre formato de intercâmbio e estrutura em memória ficou clara?
- O fluxo JSON → `list`/`dict` → DataFrame → JSON ajudou?
- A noção de serialização/desserialização foi compreendida?
- A discussão de parsing aproximadamente `O(m)` foi adequada?
- A pergunta “qual é o Big-O do JSON?” ajudou a reforçar que complexidade pertence à operação?
- Esse bloco pareceu necessário ou poderia ser reduzido em uma próxima oferta?

**Registro:**

> Preencher após a aula.

---

# 10. Tempo

Registrar com a maior precisão possível:

- Onde terminou o primeiro encontro?
- Onde começou o segundo encontro?
- Quanto tempo aproximadamente foi gasto em atividades?
- Quanto tempo aproximadamente foi gasto no benchmark?
- Qual bloco consumiu mais tempo do que o previsto?
- Qual bloco foi mais rápido do que o previsto?
- Algum conteúdo foi apenas comentado?
- Algum conteúdo não foi realizado?
- Os exercícios extras foram utilizados?
- A síntese final foi realizada com tempo suficiente?
- A ponte para a S04 foi realizada?

**Registro:**

> Preencher após a aula.

---

# 11. Notebook Mestre + Quarto/Reveal.js

A S03 constitui mais um teste do formato.

Na S02 foram observados:

- funcionamento razoável do formato;
- códigos duplicados no slide apenas para mostrar saída;
- necessidade de link para o Notebook Estudante também no Mestre;
- transição de retorno feita naturalmente pelo professor, e não pelos estudantes.

Registrar:

- A renderização ocorreu sem problemas?
- Algum slide apresentou sobreposição?
- Algum código ficou pequeno?
- Alguma tabela ficou grande demais?
- Algum resultado de célula ficou visualmente inadequado?
- Houve duplicação de código/saída?
- Uma célula com código + resultado funcionou melhor?
- Diagramas em texto funcionaram na projeção?
- O link para o Notebook Estudante funcionou?
- A navegação durante a aula foi natural?
- Houve necessidade de editar o notebook ou HTML durante a aula?
- O formato parece melhor, igual ou pior que na S02?
- Já existem evidências suficientes para consolidar esse formato ou é necessário continuar testando?

**Registro:**

> Preencher após a aula.

---

# 12. Slides e densidade

A apresentação foi planejada com aproximadamente 45–47 unidades/segmentos leves, priorizando uma ideia ou ação por slide.

Registrar:

- A quantidade pareceu excessiva?
- A densidade por slide foi adequada?
- Houve sensação de corrida?
- Quais slides/blocos poderiam ser condensados?
- Quais precisariam ser divididos?
- Houve algum bloco superficial apesar da quantidade de slides?
- Houve algum bloco aprofundado além do necessário?
- Os slides de código foram legíveis?
- As perguntas antes das respostas ajudaram a manter participação?

**Registro:**

> Preencher após a aula.

---

# 13. Evidências de aprendizagem

Registrar exemplos concretos, quando possível:

- Algum estudante explicou corretamente por que `insert(0, x)` custa mais que `append(x)`?
- Algum estudante utilizou espontaneamente Big-O para justificar uma operação?
- A turma conseguiu distinguir `O(n)` de tempo cronometricamente maior?
- Alguém percebeu que duas soluções `O(n)` podem ter constantes muito diferentes?
- Os estudantes conseguiram explicar por que lote é importante para DataFrame?
- Conseguiram explicar por que JSON não concorre diretamente com DataFrame?
- Houve perguntas que revelaram mudança de compreensão?
- Que erro conceitual apareceu mais de uma vez?

**Evidências observadas:**

> Preencher após a aula.

---

# 14. Exercícios

Registrar:

- Houve tempo para exercícios além do Notebook Estudante?
- Quais exercícios foram realizados?
- Quais pareceram mais adequados?
- Quais foram difíceis demais?
- Quais foram fáceis demais?
- Algum exercício deve ser reaproveitado na abertura da S04?
- Os exercícios devem ser reduzidos ou ampliados na próxima semana?

**Registro:**

> Preencher após a aula.

---

# 15. Decisões para a Semana 04

Preencher somente depois da aula.

### Manter

> Preencher.

### Modificar

> Preencher.

### Retirar

> Preencher.

### Retomar conceitualmente

> Preencher.

### Dificuldades de Python que precisam ser consideradas

> Preencher.

### Evidências sobre o formato da aula

> Preencher.

---

# 16. Questões específicas para orientar a S04

A Semana 04 deverá avançar para busca sequencial × busca binária. Antes de produzi-la, responder:

1. A turma está pronta para comparar algoritmos de busca de maneira mais formal?
2. `O(1)`, `O(n)`, `O(n log n)` e `O(n²)` estão suficientemente diferenciados?
3. É necessário retomar a ideia de dados ordenados antes da busca binária?
4. A ordenação apresentada na S03 criou uma ponte natural para a S04?
5. A turma consegue prever comportamento antes de executar?
6. O benchmark deve voltar a aparecer na S04?
7. O Notebook Estudante deve continuar com o mesmo papel?
8. A S04 pode aprofundar implementação de algoritmos ou ainda é necessário privilegiar mecanismos visuais?
9. Que parte da S03 deve aparecer na retomada inicial da S04?
10. Há alguma evidência da aula que exija alterar o planejamento previsto no cronograma?

**Respostas:**

> Preencher após a aula.

---

# 17. Registro pós-aula resumido

Este bloco deve ser preenchido ao final, mesmo que as seções anteriores tenham sido respondidas.

## Narrativa

- A progressão da semana funcionou?
- O que funcionou melhor?
- O que funcionou pior?
- Onde houve maior participação?

## Notebook Estudante

- As chamadas funcionaram?
- As previsões foram realizadas?
- A separação entre Mestre e Estudante está funcionando?

## Python

- Quais dificuldades apareceram?
- `lambda` foi compreendida?
- pandas exigiu explicações adicionais?

## Benchmark

- Foi realizado?
- Qual experimento foi mais útil?
- Quanto tempo consumiu?
- Deve ser mantido nas próximas semanas?

## Tempo

- Onde terminou o primeiro encontro?
- O que foi reduzido?
- O que não foi realizado?

## Formato

- Notebook Mestre + Quarto funcionou?
- Houve problemas visuais?
- Houve código duplicado?
- O formato deve ser mantido na S04?

## Conteúdo

- DataFrame foi compreendido além de “uma tabela”?
- JSON foi corretamente distinguido de estrutura em memória?
- A relação operação → mecanismo → complexidade ficou clara?

## Principal evidência para a próxima semana

> Registrar em uma ou duas frases a evidência mais importante que deverá orientar a produção da S04.
