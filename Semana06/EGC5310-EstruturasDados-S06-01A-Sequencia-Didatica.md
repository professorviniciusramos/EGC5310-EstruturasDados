# EGC5310 --- Semana 06

**Artefato:** 01A --- Sequência Didática\
**Tema:** Representação, operações e custo\
**Duração:** aproximadamente 160 minutos úteis\
**Status:** Revisado e sincronizado com os Notebooks Mestre, Estudante e
Professor

## 1. Função desta sequência

Este documento descreve a progressão didática da S06: intervenções,
perguntas, respostas esperadas, momentos de código e transições.

A aula não deve parecer uma coleção de nove exercícios. As atividades
são **pontos de chegada** de discussões e experimentos.

Progressão geral:

> **escolher → implementar → medir → explicar por dentro → mudar a
> operação → escolher novamente**

## 2. Abertura --- criar uma decisão antes de ensinar a resposta

Apresentar o Online Retail e cinco necessidades de uma loja:

1.  recuperar descrição por código;
2.  recuperar produtos em uma faixa;
3.  inserir novos produtos;
4.  comparar grupos de clientes;
5.  calcular valores sobre muitas transações.

### Pergunta

> "Vocês usariam a mesma estrutura para todas essas operações?"

Em seguida:

> "Escolham agora. Não precisam acertar. Precisamos de uma hipótese para
> testar."

### Respostas esperadas

Provavelmente aparecerão `list`, `dict` e DataFrame. Depois da S05,
`dict` pode dominar as respostas.

### Intervenção

Não corrigir. Perguntar apenas:

> "Qual propriedade da estrutura fez você escolhê-la?"

### Transição

> "Vamos manter os dados e testar primeiro uma única pergunta: encontrar
> um produto pelo código."

Abrir Notebook Estudante --- Atividade 1 e depois Atividade 2.

------------------------------------------------------------------------

## 3. Busca exata --- três implementações obrigatórias

Construir uma visão `StockCode → Description`.

Explicar antes que o dataset possui linhas transacionais repetidas e que
a visão de produtos distintos é menor.

### Perguntas antes do código

> "Se os pares estiverem numa lista comum, o que sabemos sobre a posição
> de um código?"

Resposta esperada: nada.

> "Se estiverem ordenados pelo código, que informação nova possuímos?"

Resposta: a ordem permite descartar regiões.

> "Se construirmos `dict[codigo] = descricao`, qual mecanismo estudado
> na S05 aparece?"

Resposta: hashing.

### Implementação

Todos implementam:

-   busca sequencial;
-   busca binária;
-   consulta ao `dict`.

### Depois da execução

Perguntar:

> "Podemos concluir que `dict` é a melhor estrutura?"

Se responderem sim:

> "Melhor para qual operação?"

### Transição

> "Ainda falta uma coisa: quanto custou deixar os dados prontos para
> cada consulta?"

------------------------------------------------------------------------

## 4. Preparar também custa

Apresentar:

`custo total = preparação + consultas`

Não tratar a expressão como fórmula universal de desempenho; ela é um
modelo para separar dois tipos de trabalho.

### Previsões

Perguntar:

-   "Com uma consulta, ordenar pode compensar?"
-   "E se consultarmos 10.000 vezes?"
-   "Construir um `dict` é gratuito?"
-   "O ponto em que compensa será igual em qualquer computador?"

### Experimento

Executar o benchmark com as mesmas consultas para as estratégias.

### O que observar

Os estudantes devem distinguir:

-   tempo de preparação;
-   tempo das consultas;
-   crescimento com n;
-   influência da quantidade de consultas.

### Formalização

Recuperar:

-   sequencial: O(n);
-   binária: O(log n), após ordenação;
-   `dict`: O(1) médio para consulta, após construção.

### Transição

> "Se a pergunta continuar sendo chave exata, hashing é muito atraente.
> Vamos mudar a pergunta."

------------------------------------------------------------------------

## 5. Intervalo --- fazer `dict` perder a vantagem natural sem dizer que ele é ruim

Perguntar:

> "Quero todos os códigos entre `22000` e `22999`. Onde eles estão no
> `dict`?"

Esperado: hashing não organiza chaves por proximidade/ordem.

### Previsão

Comparar mentalmente:

-   lista comum;
-   lista ordenada;
-   `dict`.

### Implementação

A lista ordenada usa:

1.  busca do limite inferior;
2.  percurso até ultrapassar o limite superior.

### Formalização

-   varredura: O(n);
-   ordenada: O(log n + k), após preparação.

### Pergunta de síntese

> "O `dict` piorou?"

Resposta desejada: não; a operação mudou.

### Transição

> "Agora vamos mudar não só a operação, mas a própria natureza da
> informação que queremos representar."

------------------------------------------------------------------------

## 6. Repetição e multiplicidade --- o que precisamos preservar?

Antes de transformar os dados em conjuntos, recuperar o dataset transacional.

Mostrar algumas linhas com o mesmo `InvoiceNo` e produtos diferentes.

### Perguntas

- "Por que `InvoiceNo` aparece repetido?"
- "Se eu remover essas repetições, o que perco?"
- "Uma lista preserva essa informação?"
- "O que acontece se eu fizer `d[invoice] = produto` três vezes para a mesma chave?"

### Conflito

A nova atribuição no `dict` substitui o valor anterior. Isso não significa que `dict` seja incapaz de representar uma venda com vários itens.

Mudar a representação:

```python
vendas[invoice] = [
    (produto1, quantidade1),
    (produto2, quantidade2)
]
```

### Formalização

Uma chave de `dict` está associada a um valor. O valor pode ser outra estrutura.

Introduzir explicitamente a ideia de **composição de estruturas** e de relação 1:N.

### Transição

> "Agora vamos fazer o contrário: há situações em que queremos deliberadamente esquecer quantas vezes algo apareceu e trabalhar apenas com elementos únicos."

## 7. `set` --- quando o problema é um conjunto

Definir:

-   A = clientes do Reino Unido;
-   B = clientes com linha de quantidade ≥ 10.

Perguntar antes da sintaxe:

> "Quais clientes pertencem aos dois grupos?"

> "Quais estão em A mas não em B?"

> "Quais estão em pelo menos um?"

Só então introduzir:

-   `A & B`;
-   `A - B`;
-   `A | B`;
-   `A ^ B`.

### Pergunta crítica

> "Por que não usar `dict`?"

Resposta esperada: poderíamos usar hashing para pertencimento, mas aqui
não precisamos de valor associado; queremos representar conjuntos únicos
e operar semanticamente com eles.

### Abrir a abstração

Explicitar antes de usar:

- `A & B`: interseção;
- `A | B`: união;
- `A - B`: diferença;
- `A ^ B`: diferença simétrica, isto é, está em exatamente um dos grupos.

Para `^`, mostrar também `(A - B) | (B - A)`.



Para `x in A`:

`x → hash(x) → posição candidata → comparação → eventual probing`

Para `A & B`:

percorrer elementos + vários testes de pertencimento.

Para `A - B`:

percorrer A + testar ausência em B.

Para `A | B`:

construir resultado preservando unicidade.

### Pergunta

> "`A & B` é uma linha. Então é O(1)?"

Resposta: não.

### Transição

> "Python escondeu bastante trabalho. `list.append()` também parece uma
> única operação. O que será que ela esconde?"

------------------------------------------------------------------------

## 8. `list` --- da abstração à memória

Mostrar:

``` text
list
[ref][ref][ref][ref][   ][   ]
  ↓    ↓    ↓    ↓
 obj  obj  obj  obj
```

Explicar:

-   referências contíguas;
-   objetos não necessariamente contíguos;
-   tamanho lógico;
-   capacidade.

### Simulação 1 --- há espaço

`append(x)` coloca uma referência no próximo slot livre.

### Simulação 2 --- não há espaço

Perguntar:

> "Ele cria exatamente mais uma posição?"

Explicar over-allocation.

Não ensinar "dobra sempre".

Explicar que o redimensionamento pode conseguir ampliar o bloco ou
exigir outro espaço e movimentação das referências.

### Pergunta

> "Então `append` é realmente O(1)?"

Resposta a construir: uma chamada pode ser cara; uma sequência tem custo
O(1) amortizado por inserção.

### Experimento

Crescer e remover 5.000 elementos, registrando mudanças de
`sys.getsizeof()`.

### Interpretação

Perguntar:

-   "Mudou a cada `append`?"
-   "Por que aparecem degraus?"
-   "Quando removemos, os degraus descem nos mesmos pontos?"
-   "Por que não devolver memória a cada `pop`?"

### Transição

> "Agora sabemos que até uma inserção aparentemente simples depende da
> propriedade que a estrutura mantém."

------------------------------------------------------------------------

## 9. Inserções --- o preço de preservar propriedades

Comparar:

-   `append`;
-   `bisect.insort`;
-   `dict[chave] = valor`;
-   `set.add`.

### Antes da pergunta-chave

Explicar o problema resolvido por `bisect.insort`: inserir um novo elemento em uma lista já ordenada sem perder a ordenação.

Separar no quadro:

`localizar posição O(log n)` + `abrir espaço/deslocar O(n)` → operação total O(n).

### Pergunta-chave

> "Se `bisect` encontra a posição em O(log n), por que a inserção não é
> O(log n)?"

Resposta: encontrar posição e abrir espaço são trabalhos diferentes;
inserir no meio do array exige deslocar referências.

### Outro cuidado

Perguntar:

> "As quatro estruturas guardam a mesma coisa?"

Não. O `set` do experimento guarda códigos, o `dict` associa código e
descrição, e a lista ordenada preserva uma relação de ordem.

### Transição

> "Até aqui quase todas as perguntas envolviam localizar ou manter
> elementos. Agora vamos tocar todos os registros."

------------------------------------------------------------------------

## 10. NumPy --- quando o problema muda para processamento em massa

Perguntar:

> "Quanto custa calcular `Quantity × UnitPrice` para n transações?"

Implementar primeiro com Python.

Depois NumPy.

### Previsão

> "Qual o Big-O do laço?"

O(n).

> "Qual o Big-O da operação vetorizada, se todos os n valores precisam
> participar?"

Também O(n).

### Conflito cognitivo

Executar e observar diferença concreta.

Perguntar:

> "Se os dois são O(n), por que os tempos são tão diferentes?"

### Explicação suficiente para esta semana

`np.array(...)` cria um array NumPy (`numpy.ndarray`), mas sua implementação interna não é conteúdo desta semana.

A explicação necessária é apenas que NumPy oferece operações otimizadas sobre arrays e permite expressar o processamento em lote sem escrever explicitamente o laço elemento a elemento em Python.

O conflito conceitual permanece:

- laço Python: O(n);
- operação NumPy sobre n valores: O(n);
- tempos concretos podem ser muito diferentes.

### Cuidado

Se a conversão `list → ndarray` não estiver no tempo da operação, dizer
explicitamente que ela é custo de preparação.

### Ponte opcional

Mostrar a expressão Pandas equivalente, sem transformar o bloco em aula
de Pandas.

### Transição

> "Já mudamos várias vezes de resposta porque mudamos a operação. Vamos
> voltar à escolha feita no começo."

------------------------------------------------------------------------

## 11. Fechamento --- escolha revista

Reabrir a Atividade 1.

Pedir para cada estudante reescrever:

`operação → estrutura → propriedade → custo/limitação → evidência`

### Perguntas finais

> "Há uma estrutura universalmente melhor?"

> "Se busca exata e intervalo forem ambas muito frequentes, poderíamos
> manter duas representações?"

> "Qual problema aparece se mantivermos duas?"

Resposta esperada: sincronização e consistência.

### Síntese do professor

> **Estruturas de dados são decisões sobre como organizar informação
> para favorecer determinadas operações. Toda escolha traz propriedades,
> custos e limitações.**

## 12. Evidências a observar

Ao longo da aula, registrar se os estudantes:

-   abandonam respostas do tipo "`dict` porque é O(1)" sem contexto;
-   distinguem preparação e consulta;
-   reconhecem a utilidade da ordenação para intervalos;
-   justificam `set` pela semântica de conjunto;
-   explicam que uma linha Python pode esconder muitas operações;
-   entendem O(1) amortizado;
-   distinguem Big-O de tempo concreto;
-   revisam a escolha inicial com argumentos melhores.
