# EGC5310 --- Estruturas de Dados para Ciência de Dados

**Semana:** 06\
**Artefato:** 01 --- Roteiro\
**Tema:** Representação, operações e custo com dados reais\
**Duração prevista:** 160 minutos úteis\
**Formato:** Notebook Mestre + Quarto/Reveal.js + Notebook Estudante +
Notebook Professor\
**Status:** Revisado após consolidação dos notebooks da S06

## 1. Ideia central da semana

A Semana 06 não apresenta uma nova estrutura como resposta pronta. Ela
integra o que foi construído nas semanas anteriores e desloca a pergunta
de:

> "Qual é a complexidade desta estrutura?"

para:

> **"Dado um problema e um conjunto de operações, como a representação
> dos dados altera o trabalho necessário?"**

A semana usa um único conjunto de dados real, **Online Retail (UCI)**,
para que os estudantes mantenham o domínio do problema e mudem
deliberadamente a representação e a operação.

A conclusão desejada não é "`dict` é melhor", "`set` é melhor" ou "NumPy
é melhor". A conclusão é:

> **a estrutura vem depois da pergunta e do padrão de operações.**

## 2. Continuidade com as semanas anteriores

A S06 recupera diretamente:

-   busca sequencial e custo O(n);
-   busca binária, ordenação e O(log n);
-   hashing, colisões, `dict` e `set`;
-   distinção entre Big-O e quantidade concreta de operações;
-   DataFrame e processamento em lote;
-   escolha de representação em função das operações.

O avanço conceitual da semana é mostrar **por que** comportamentos
diferentes aparecem, inclusive olhando para mecanismos internos que
Python normalmente esconde:

-   `list` como array dinâmico de referências;
-   tamanho lógico × capacidade;
-   `append`, over-allocation e custo amortizado;
-   `set` e `dict` apoiados em hashing;
-   trabalho escondido em `in`, `&`, `-` e `|`;
-   processamento em massa e a distinção entre classe assintótica e tempo concreto de execução.

## 3. Dataset e duas cardinalidades

Utilizar o **Online Retail da UCI**.

É indispensável explicitar que:

-   o arquivo possui aproximadamente 541 mil **linhas transacionais**;
-   uma linha não corresponde a um produto distinto;
-   `StockCode` reaparece em várias transações;
-   para as atividades de busca por produto será construída uma visão
    `código → descrição` com uma entrada por código;
-   para clientes e processamento em massa voltaremos ao dataset
    transacional completo.

Essa distinção evita interpretar o benchmark de produtos distintos como
se estivesse operando sobre 541 mil chaves únicas.

## 4. Resultados de aprendizagem

Ao final da semana, espera-se que o estudante consiga:

1.  escolher inicialmente uma estrutura e explicitar a propriedade que
    motivou a escolha;
2.  implementar busca sequencial, busca binária e consulta por `dict`
    para o mesmo problema;
3.  distinguir custo de preparação e custo de consulta;
4.  explicar por que busca por intervalo favorece uma representação
    ordenada;
5.  utilizar `set` quando o problema possuir semântica genuinamente
    conjuntista;
6.  explicar conceitualmente o trabalho realizado em `x in A`, `A & B`,
    `A - B` e `A | B`;
7.  distinguir tamanho lógico e capacidade interna de uma `list`;
8.  explicar por que `append()` é O(1) amortizado e não uma operação de
    custo idêntico em todas as chamadas;
9.  reconhecer que remoção de elementos não implica desalocação
    proporcional imediata;
10. comparar custo de inserção quando diferentes propriedades precisam
    ser preservadas;
11. explicar por que duas soluções O(n) podem ter tempos concretos muito
    diferentes;
12. rever uma decisão inicial a partir de evidências experimentais.

## 5. Estrutura da aula

  ------------------------------------------------------------------------
                  Tempo Movimento        Atividade        Evidência
                                                          principal
  --------------------- ---------------- ---------------- ----------------
              0--12 min problema e       1                escolhas
                        hipótese                          iniciais
                                                          justificadas

             12--30 min mesma pergunta,  2                sequencial,
                        três                              binária e `dict`
                        representações                    

             30--53 min custo de         3                benchmark por n
                        preparar ×                        e quantidade de
                        consultar                         consultas

             53--73 min mudança da       4                consulta por
                        operação                          intervalo

             73--93 min problema         5                `in`,
                        conjuntista                       interseção,
                                                          união e
                                                          diferenças

            93--115 min estrutura        6                degraus de
                        interna da                        alocação e
                        `list`                            remoção

           115--133 min custo de manter  7                `append`,
                        propriedades                      `insort`,
                                                          `dict`, `set`

           133--151 min mudança para     8                Python × NumPy
                        processamento em                  
                        massa                             

           151--160 min decisão revista  9                nova escolha
                                                          justificada
  ------------------------------------------------------------------------

Os tempos são referências. A qualidade da interpretação é mais
importante que concluir todos os benchmarks.

## 6. Condução das atividades

### Atividade 1 --- escolha antes da medida

Apresentar cinco tipos de operação:

-   busca por código exato;
-   busca por intervalo;
-   inserção;
-   comparação de grupos de clientes;
-   processamento em massa.

Perguntar:

> "Qual estrutura você escolheria para cada operação? Por quê?"

Não corrigir imediatamente. Registrar a hipótese para retornar a ela no
final.

**Observar:** tendência de responder `dict` para tudo após a S05.

### Atividade 2 --- uma pergunta, três representações

Problema:

> "Dado um `StockCode`, qual é sua descrição?"

Implementar obrigatoriamente:

-   lista + busca sequencial;
-   lista ordenada + busca binária;
-   `dict`.

Antes do código, perguntar:

-   qual pode percorrer quase todos os produtos?
-   qual depende de uma propriedade adicional?
-   qual exige construir uma estrutura por hashing?
-   o que acontece para chave ausente?

Após a execução, não concluir "`dict` venceu". Dizer:

> "Até agora fizemos apenas busca por chave exata."

### Atividade 3 --- custo total

Introduzir:

> **custo total = preparação + quantidade de consultas × custo da
> consulta**

Medir separadamente preparação e consultas.

Perguntar antes:

-   o que esperamos com uma consulta?
-   e com 100?
-   e com 10.000?
-   o ponto de cruzamento é universal?

Reforçar: Big-O descreve crescimento; benchmark mede uma implementação
em um ambiente concreto.

### Atividade 4 --- o problema mudou: intervalo

Problema:

> recuperar códigos lexicograficamente entre `"22000"` e `"22999"`.

Comparar:

-   varredura da lista;
-   lista ordenada com limite inferior e percurso de `k` resultados;
-   `dict` varrendo chaves.

Formalização esperada:

-   varreduras: O(n);
-   ordenada: O(log n + k), depois de preparada.

Frase de transição:

> **"O `dict` não ficou pior. A pergunta mudou."**

### Exploração intermediária --- repetição, multiplicidade e composição

Retomar o dataset transacional antes de entrar em `set`.

Usar `InvoiceNo` para mostrar que uma mesma venda aparece em várias linhas porque contém vários itens. A repetição, portanto, pode ser **informação**, e não um problema a ser eliminado.

Comparar:

-   lista de registros: preserva as ocorrências;
-   `set`: preserva unicidade e elimina multiplicidade;
-   `dict[invoice] = produto`: uma nova atribuição para a mesma chave substitui o valor anterior;
-   `dict[invoice] = list(...)`: representa naturalmente uma relação 1:N.

Perguntas para a turma:

-   "O que perderíamos se deduplicássemos `InvoiceNo`?"
-   "O problema é que `dict` não aceita vários valores ou que precisamos decidir o que o valor associado à chave representa?"
-   "Podemos combinar estruturas?"

Chegada conceitual:

> estruturas podem ser compostas; uma chave de `dict` está associada a um valor, e esse valor pode ser uma lista ou outra estrutura.

### Atividade 5 --- `set` quando o problema é conjunto

Antes da execução, explicitar a notação:

-   `A & B`: interseção --- elementos nos dois conjuntos;
-   `A | B`: união --- elementos em pelo menos um dos conjuntos;
-   `A - B`: diferença --- elementos de A que não estão em B;
-   `A ^ B`: diferença simétrica --- elementos em exatamente um dos conjuntos.


Criar:

-   A = clientes com compras no Reino Unido;
-   B = clientes com linha de quantidade ≥ 10.

Explorar:

-   `x in A`;
-   `A & B`;
-   `A | B`;
-   `A - B`;
-   `A ^ B`.

Não justificar `set` apenas pelo pertencimento. Explicar que `dict`
também faz pertencimento por hashing; `set` é natural aqui porque
queremos representar **coleções únicas e realizar álgebra de
conjuntos**.

Mostrar conceitualmente:

`x → hash(x) → posição candidata → comparação → eventual probing`

Para `A & B`, `A - B` e `A | B`, revelar o trabalho escondido por trás
de uma única linha de Python.

### Atividade 6 --- `list`, `append` e memória

Antes do experimento, mostrar visualmente:

-   `list` como array dinâmico contíguo de referências;
-   objetos referenciados podendo estar em outras regiões;
-   tamanho lógico × capacidade;
-   `append` com capacidade disponível;
-   `append` quando não há capacidade;
-   redimensionamento e over-allocation.

Não ensinar que Python "sempre dobra" a lista.

Executar crescimento e remoção registrando `len()` e `sys.getsizeof()`
somente quando o tamanho em bytes mudar.

Perguntar:

-   a memória muda em todo `append`?
-   aparecem degraus?
-   remover metade implica reduzir metade da memória?
-   por que evitar redimensionar a cada operação?

Usar o resultado para introduzir O(1) amortizado.

### Atividade 7 --- inserção e manutenção

Comparar 200 inserções com:

-   `append`;
-   `bisect.insort`, explicitando seu propósito: inserir mantendo uma `list` já ordenada;
-   atribuição em `dict`;
-   `set.add`.

Ponto central:

> encontrar a posição em O(log n) não significa inserir em O(log n) em
> um array dinâmico.

`insort` ainda pode deslocar referências: O(n).

Também destacar que as quatro estruturas não preservam a mesma
semântica.

### Atividade 8 --- agora precisamos tocar todos os dados

Mudar explicitamente a natureza do problema:

> "Até agora queríamos encontrar/manter elementos. E se precisarmos
> calcular sobre centenas de milhares de valores?"

Calcular `Quantity × UnitPrice` com:

-   laço Python;
-   NumPy vetorizado.

Ambos percorrem quantidade proporcional a n: O(n).

Discutir:

-   `list`: referências para objetos Python;
-   `dtype`;
-   execução vetorizada em código otimizado;
-   custo de conversão como preparação.

Mensagem:

> **Big-O não é cronômetro.**

### Atividade 9 --- escolha novamente

Voltar literalmente à Atividade 1.

Pedir:

> "Você manteria sua escolha? Para quais operações? O que mudaria?"

A justificativa deve incluir:

-   propriedade útil;
-   preparação;
-   consulta;
-   manutenção;
-   limitação;
-   evidência observada.

Encerrar com a pergunta:

> "Se mantivermos simultaneamente um `dict` e uma estrutura ordenada,
> qual novo problema de engenharia aparece?"

Resposta esperada: sincronização/consistência entre representações.

## 7. Mediação

O padrão de mediação da semana é:

**problema → hipótese → implementação → previsão → execução →
interpretação → mecanismo → custo → decisão**

Os slides intermediários do Notebook Mestre são parte essencial da aula.
Eles devem levar à atividade e, depois, explicar o resultado observado.
Não saltar de atividade em atividade.

## 8. Preparação técnica

Antes da aula:

-   executar integralmente Notebook Estudante e Notebook Professor;
-   verificar download da UCI e manter o XLSX oficial disponível
    localmente;
-   testar `openpyxl`, pandas, NumPy e matplotlib;
-   testar benchmarks no ambiente da aula;
-   conferir links do Colab;
-   renderizar o Mestre com Quarto;
-   revisar logo, links e chamadas visuais;
-   manter Mestre, Estudante e Professor abertos.

## 9. Pontos de precisão

Não afirmar:

-   que `dict` é sempre melhor;
-   que `set` deve ser usado só porque `in` é O(1) médio;
-   que O(1) significa uma quantidade fixa de instruções;
-   que `append` sempre tem o mesmo custo;
-   que Python sempre dobra a capacidade da `list`;
-   que remover metade dos elementos libera metade da memória;
-   que `bisect.insort` insere em O(log n);
-   que NumPy possui Big-O melhor no experimento de soma;
-   que `sys.getsizeof()` mede recursivamente os objetos da lista.

## 10. Critério de sucesso

A semana será bem-sucedida se os estudantes conseguirem explicar, com
exemplos da própria aula, a frase:

> **"Não escolhemos uma estrutura apenas pelo nome da complexidade;
> escolhemos uma representação a partir das operações que precisamos
> realizar e dos custos que estamos dispostos a assumir."**
