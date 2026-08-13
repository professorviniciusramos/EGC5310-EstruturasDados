# EGC5310 --- Semana 01 --- Resumo do Professor

## Leia 5 minutos antes da aula

**Semana:** 01 --- Do problema ao custo computacional\
**Cenário:** Sistema acadêmico\
**Material principal:**
`EGC5310-EstruturasDados-S01-99-Aula-Mestre.html`

------------------------------------------------------------------------

# 1. A ideia da aula em uma frase

> **Não começar ensinando Big-O. Fazer Big-O surgir da necessidade de
> explicar quanto trabalho uma solução realiza quando os dados
> crescem.**

A aula deve parecer uma investigação, não uma sequência de definições.

------------------------------------------------------------------------

# 2. A história que precisa acontecer

A narrativa inteira é esta:

> **Problema → solução → funciona → quanto trabalho? → comparar casos →
> definir n → descrever T(n) → observar crescimento → introduzir Big-O →
> distinguir crescimento de tempo → experimentar → encontrar uma
> limitação → perguntar se podemos organizar melhor os dados.**

Se essa história estiver clara, a aula está no caminho certo.

------------------------------------------------------------------------

# 3. Pergunta central

Começar e retornar sempre que necessário a:

> **Quando uma solução que funciona deixa de ser uma boa solução?**

Mensagem de fundo:

> **correto não significa necessariamente adequado.**

------------------------------------------------------------------------

# 4. Primeiro problema

Sistema acadêmico.

Temos uma pequena coleção de estudantes.

Perguntar:

> **Como encontrar a matrícula 1082?**

**Não mostrar o código imediatamente.**

Deixar os estudantes descreverem a solução.

A ideia que deve surgir:

1.  examinar um estudante;
2.  comparar a matrícula;
3.  avançar se não for;
4.  parar quando encontrar;
5.  chegar ao final se não existir.

Só depois transformar isso em Python.

------------------------------------------------------------------------

# 5. Depois que o código funcionar

Perguntar:

> **Funciona. Então o problema está resolvido?**

Não responder.

Mudar a pergunta:

> **Quanto trabalho foi necessário?**

Contar comparações.

Esse é o momento em que a aula deixa de ser apenas programação e passa a
ser análise do algoritmo.

------------------------------------------------------------------------

# 6. Casos que precisam aparecer

Comparar:

-   primeiro;
-   intermediário;
-   último;
-   inexistente.

Ideia:

-   primeiro pode exigir 1 comparação;
-   último pode exigir percorrer toda a coleção;
-   inexistente também pode exigir percorrer toda a coleção.

Introduzir informalmente:

-   melhor caso;
-   pior caso.

Não dizer apenas:

> "busca sequencial é O(n)".

Quando chegar a Big-O, falar em **pior caso O(n)**.

------------------------------------------------------------------------

# 7. Fazer n surgir naturalmente

Perguntar:

> "E se tivéssemos mil estudantes?"

Depois:

> "Como representamos o tamanho da coleção sem escolher um número
> específico?"

Então:

> **n = número de estudantes na coleção**

Predizer antes de executar:

-   10 estudantes → até aproximadamente 10 comparações;
-   100 → aproximadamente 100;
-   1.000 → aproximadamente 1.000.

------------------------------------------------------------------------

# 8. T(n) e Big-O

`T(n)` vem **depois** da contagem.

Ideia:

> **T(n) descreve o trabalho em função do tamanho da entrada.**

Depois mostrar crescimento linear.

Só então introduzir:

> **Big-O descreve como o custo cresce quando n cresce.**

Para esta aula basta a intuição de:

-   `O(1)`;
-   `O(n)`;
-   `O(n²)`.

Não entrar em definição assintótica formal.

------------------------------------------------------------------------

# 9. Cuidado conceitual mais importante

> **Big-O não é cronômetro.**

Perguntar:

> "Mesmo algoritmo, mesmo n e mesmo pior caso: os tempos serão
> exatamente iguais?"

Não necessariamente.

Depois:

> "E o número de comparações?"

Estruturalmente, deve seguir a previsão do algoritmo.

Mensagem:

> **tempo observado ≠ ordem de crescimento**

O cronômetro é evidência experimental; Big-O comunica crescimento.

------------------------------------------------------------------------

# 10. Experimento

Antes de executar:

> **Hipótese: no pior caso, o número de comparações da busca sequencial
> cresce linearmente com n.**

Perguntar:

> "O que esperamos observar?"

Depois executar.

Observar:

-   `n`;
-   comparações;
-   tempo;
-   gráfico.

O importante é confirmar:

> **comparações ∝ n**

Não exigir que o tempo dobre exatamente quando `n` dobra.

------------------------------------------------------------------------

# 11. Onde a aula deve chegar conceitualmente

No final, o estudante deve conseguir reconstruir algo próximo de:

> "Criamos uma busca que funciona. No pior caso ela pode examinar todos
> os n elementos. O trabalho cresce linearmente com o tamanho da
> entrada, por isso descrevemos esse comportamento como O(n). O tempo
> medido pode variar, mas a estrutura do algoritmo permanece. Se os
> dados crescerem muito, talvez precisemos organizar os dados de outra
> maneira."

------------------------------------------------------------------------

# 12. Pergunta de fechamento

Escalar mentalmente:

> "E se tivermos milhões de estudantes e muitas consultas?"

Depois:

> **Podemos organizar os dados de outra maneira?**

Não ensinar busca binária, hashing ou árvores agora.

Se os estudantes sugerirem essas ideias, acolher.

A pergunta aberta é parte do fechamento.

------------------------------------------------------------------------

# 13. O que NÃO fazer

-   Não começar definindo Big-O.
-   Não transformar a aula em tabela de complexidades.
-   Não antecipar formalmente busca binária.
-   Não aprofundar prova assintótica.
-   Não deixar uma dificuldade individual de Python interromper toda a
    narrativa.
-   Não executar antes de pedir uma previsão quando houver oportunidade.
-   Não confundir tempo medido com complexidade.
-   Não correr apenas para chegar ao último slide.

------------------------------------------------------------------------

# 14. Se faltar tempo

Pode parar tranquilamente:

### Depois da implementação

> "Temos uma solução. Agora precisamos descobrir quanto trabalho ela
> realiza."

### Depois dos casos

> "A posição altera o trabalho. Vamos investigar o que acontece quando
> os dados crescem."

### Depois de T(n)

> "Já descrevemos o custo. Falta uma linguagem para descrever como ele
> cresce."

### Depois de Big-O

> "Temos uma previsão. Agora precisamos testá-la."

A semana é a unidade didática. Não criar encerramento artificial no meio
da narrativa.

------------------------------------------------------------------------

# 15. Se houver problema técnico

Ordem de contingência:

1.  HTML autocontido;
2.  Notebook Mestre;
3.  notebooks anteriores;
4.  PPTX anterior;
5.  quadro.

> **A ferramenta pode falhar; a narrativa da aula não depende dela.**

------------------------------------------------------------------------

# 16. O que observar na turma

Durante a aula, prestar atenção a:

-   domínio de Python;
-   compreensão de `for`;
-   capacidade de formular algoritmo antes do código;
-   significado atribuído a `n`;
-   compreensão da contagem de operações;
-   confusão entre Big-O e tempo;
-   ritmo da turma;
-   participação;
-   necessidade de duplas/trios;
-   funcionamento do Notebook Mestre como instrumento didático.

Registrar depois da aula.

------------------------------------------------------------------------

# 17. Frases úteis para conduzir a aula

Quando a turma tentar antecipar:

> **"Antes de programar: qual é o algoritmo?"**

Depois da solução:

> **"Funciona. Mas quanto trabalho fizemos?"**

Antes de executar:

> **"Qual é a nossa previsão?"**

Ao introduzir `n`:

> **"O que muda quando a coleção cresce?"**

Ao introduzir Big-O:

> **"Não estamos tentando prever segundos; estamos descrevendo
> crescimento."**

No experimento:

> **"O resultado confirma nossa hipótese?"**

No fechamento:

> **"A solução está errada ou apenas começa a ficar inadequada?"**

E finalmente:

> **"Podemos organizar os dados de outra maneira?"**

------------------------------------------------------------------------

# 18. Se lembrar de apenas cinco coisas

1.  **Comece pelo problema, não por Big-O.**
2.  **Faça os estudantes proporem a busca antes de mostrar código.**
3.  **Conte operações antes de formalizar `T(n)` e `O(n)`.**
4.  **Peça previsão antes de executar o experimento.**
5.  **Termine com a necessidade de organizar melhor os dados.**

------------------------------------------------------------------------

# 19. Fechamento que precisa permanecer

> **Uma solução correta pode deixar de ser adequada quando os dados
> crescem.**

> **A forma como organizamos os dados influencia o custo das
> operações.**

Essa é a ponte da Semana 01 para o restante de EGC5310.

------------------------------------------------------------------------

**Versão:** 1.0\
**EGC5310 --- Semana 01 --- Resumo do Professor --- 2026/2**
