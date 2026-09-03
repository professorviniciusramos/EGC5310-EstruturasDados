# EGC5310 — Estruturas de Dados

## Semana 04 — Organizar para buscar: busca sequencial e busca binária

**Arquivo:** `EGC5310-EstruturasDados-S04-01-Roteiro.md`  
**Disciplina:** EGC5310 — Tópicos Especiais em Ciência de Dados VI  
**Projeto pedagógico:** Estruturas de Dados  
**Semana:** S04  
**Artefato:** 01 — Roteiro  
**Versão:** 1.0  
**Status:** Planejado para implementação  
**Última revisão:** 02/09/2026  
**Carga útil planejada:** aproximadamente 160 minutos  
**Formato em teste:** Notebook Mestre + Quarto/Reveal.js + Notebook Estudante  
**Cenário longitudinal:** Sistema Acadêmico

---

## 1. Propósito da semana

A Semana 04 marca a passagem da introdução qualitativa à busca, iniciada na S01, para o estudo sistemático de duas estratégias: **busca sequencial** e **busca binária**.

O objetivo não é apresentar a busca binária como um código mais sofisticado a ser memorizado. A semana deve mostrar que ela se torna possível porque uma decisão anterior foi tomada sobre os dados: **mantê-los ordenados segundo a chave de busca**.

A pergunta central será:

> **Quando vale a pena organizar os dados para buscar mais rapidamente?**

Essa pergunta conecta busca, representação, operações e custo. A solução adequada depende não apenas do número de registros, mas também da frequência das consultas, da frequência das atualizações e do custo de preparar ou manter a organização necessária.

A mudança pedagógica deliberada da S04 é:

> **Os estudantes devem descobrir partes da solução antes de receberem sua formalização.**

Consequentemente, a narrativa seguirá predominantemente o ciclo:

> **problema → pergunta → previsão → visualização → atividade → código → resultado → formalização**

e evitará longos blocos de exposição seguidos apenas por exemplos prontos.

---

## 2. Relação com as semanas anteriores

### Semana 01 — Quanto custa procurar?

A busca sequencial tornou visível o trabalho computacional. Os estudantes relacionaram tamanho da entrada, número de comparações e crescimento linear `O(n)`.

Na S04, essa solução não deve ser reapresentada extensamente. Ela funciona como **controle conceitual e experimental** para comparar uma nova estratégia.

### Semana 02 — Como representar os dados?

Foi consolidada a progressão:

> **problema → dados → operações → representação**

e a pergunta:

> **Melhor para fazer o quê?**

Na S04, a representação inclui uma propriedade decisiva: os registros podem estar desordenados ou ordenados pela matrícula.

### Semana 03 — Quanto custam as operações?

Foram discutidas inserção, remoção, ordenação, operações em lote e sequências de operações. A ideia central foi:

> **Não existe “o custo de uma estrutura”. Existe o custo de uma operação, sobre uma representação, dentro de uma sequência de operações.**

A S04 acrescenta outra consequência:

> **Uma busca mais barata pode depender de trabalho realizado antes da busca.**

Ordenar custa; manter a ordenação durante inserções também custa. O ganho da busca binária deve ser interpretado nesse contexto.

### Evidências que orientam a S04

As evidências registradas até aqui indicam que:

- a turma está recebendo pouco desafio;
- as aulas ficaram excessivamente expositivas;
- exemplos de código, isoladamente, não produziram o aprofundamento desejado;
- são necessários mais recursos visuais para apoiar a compreensão de mecanismos;
- a previsão antes da execução funcionou e deve ser mantida;
- as chamadas explícitas para o Notebook Estudante são percebidas;
- a turma é heterogênea e a maioria precisa de exemplos guiados;
- o formato Notebook Mestre + Quarto ainda deve ser testado com um desenho didático mais investigativo.

Essas evidências justificam o uso de desafios graduados, execução manual, visualizações próprias e recurso interativo externo.

---

## 3. Problema orientador

O Sistema Acadêmico armazena registros de estudantes identificados por matrícula.

Uma consulta isolada pergunta:

> **Encontre o estudante de matrícula X.**

Com poucos registros, percorrer uma lista é suficiente. Para tornar a decisão estrutural relevante, a escala do cenário será ampliada:

- até **1.000.000 de registros**;
- até **100.000 consultas por matrícula**;
- inserções e atualizações com frequências diferentes conforme o cenário.

A pergunta não será apenas:

> Como encontrar um estudante?

Ela evoluirá para:

> **Como devemos organizar os dados se precisamos procurar muitas vezes?**

Ao final, três cenários serão confrontados:

- **Cenário A:** dados chegam continuamente e quase nunca são consultados;
- **Cenário B:** dados são carregados uma vez e consultados milhões de vezes;
- **Cenário C:** inserções e consultas acontecem continuamente.

O estudante deverá perceber que não existe uma resposta universal: o padrão de operações altera a decisão.

---

## 4. Resultados de aprendizagem

Ao final da semana, o estudante deverá ser capaz de:

1. reconstruir o funcionamento da busca sequencial;
2. executar manualmente uma busca binária em uma coleção pequena e ordenada;
3. explicar visualmente por que cada comparação permite eliminar aproximadamente metade do intervalo restante;
4. identificar a ordenação pela chave pesquisada como pré-condição da busca binária;
5. reconhecer que “estar ordenado” depende do atributo usado na busca;
6. implementar uma busca binária iterativa em Python;
7. explicar o papel das variáveis `inicio`, `fim` e `meio`;
8. reconhecer e tratar corretamente a condição de elemento inexistente;
9. relacionar a busca sequencial ao comportamento `O(n)` e a busca binária a `O(log n)`;
10. explicar intuitivamente a origem do logaritmo como número de divisões sucessivas por dois;
11. estimar a ordem de grandeza do número de comparações para diferentes valores de `n`;
12. formular previsões antes de executar um experimento;
13. comparar teoria, contagem de comparações e tempo observado;
14. interpretar um benchmark sem confundir tempo medido com complexidade assintótica;
15. reconhecer que ordenar e manter a ordenação também têm custo;
16. decidir, de maneira argumentada, quando o investimento em organização pode compensar consultas mais baratas;
17. explicar o mecanismo de um algoritmo sem depender exclusivamente do código.

---

## 5. Conceitos e limites de aprofundamento

### Conceitos centrais

- busca sequencial;
- busca binária;
- intervalo de busca;
- descarte de possibilidades;
- dados ordenados por uma chave;
- melhor caso e pior caso;
- número de comparações;
- `O(n)`;
- `O(log n)`;
- custo de preparação;
- padrão de operações;
- benchmark e ruído experimental.

### Conceitos que podem ser mencionados sem aprofundamento

- `log₂(n)`;
- inserção em posição ordenada;
- custo total de ordenar uma vez e consultar muitas vezes;
- funções prontas da biblioteca padrão;
- índices de bancos de dados como ponte futura.

### Não aprofundar nesta semana

- prova formal de complexidade;
- busca binária recursiva como implementação principal;
- árvores binárias de busca;
- hashing;
- índices B-tree ou internals de SGBDs;
- algoritmos específicos de ordenação;
- fórmulas fechadas de ponto de equilíbrio com constantes desconhecidas;
- detalhes internos de `bisect`.

---

# 6. Narrativa didática detalhada

## Movimento 1 — O problema muda quando a consulta se repete

**Tempo de referência: 10 min**

### Objetivo

Retomar o cenário sem repetir a aula de busca sequencial da S01 e introduzir a frequência de operações como variável relevante.

### Abertura visual

Mostrar uma coleção pequena e desordenada de matrículas:

```text
[42] [11] [73] [25] [90] [58] [31]
```

Perguntar:

> Onde está a matrícula 73?

Depois ampliar a situação:

```text
1.000.000 de registros
100.000 consultas
```

Perguntar:

> O que poderíamos saber ou fazer sobre os dados para evitar começar do início em todas as consultas?

### Condução

- aceitar propostas como ordenar, usar dicionário, banco de dados ou índice;
- registrar as ideias sem antecipar estruturas futuras;
- focar na hipótese de **ordenar os registros**;
- destacar que a busca sequencial continua correta, mas talvez seja inadequada para o padrão de uso.

### Evidência esperada

O estudante reconhece que a quantidade de consultas é parte do problema, não apenas a quantidade de registros.

### Transição

> Se os dados estiverem ordenados, cada comparação poderá fornecer mais informação do que apenas “é” ou “não é”.

---

## Movimento 2 — Jogo humano: descobrir reduzindo possibilidades

**Tempo de referência: 15 min**

### Objetivo

Fazer a estratégia surgir antes do nome e do código.

### Atividade coletiva

Um estudante escolhe mentalmente um número inteiro entre 1 e 100. Outro estudante ou a turma tenta descobri-lo. Para cada tentativa, só são permitidas as respostas:

- maior;
- menor;
- igual.

Primeiro, aceitar uma ou duas tentativas não sistemáticas. Depois provocar:

> Qual tentativa elimina o maior número possível de candidatos, independentemente da resposta?

Registrar uma possível sequência:

```text
100 → 50 → 25 → 12 → 6 → 3 → 1
```

### Perguntas

- o que aconteceu com o conjunto de possibilidades após cada resposta?
- por que escolher um extremo é pouco informativo?
- por que o meio é especial?
- quantas tentativas seriam suficientes no pior caso?

### Cuidados

- ainda não apresentar pseudocódigo;
- não transformar o jogo em competição longa;
- deixar explícito que as respostas “maior/menor” só são úteis porque existe uma ordem.

### Formalização inicial

Somente ao final, nomear:

> Essa estratégia de reduzir repetidamente o intervalo pela metade é a ideia central da **busca binária**.

---

## Movimento 3 — Tornar visível o intervalo de busca

**Tempo de referência: 15 min**

### Objetivo

Converter a intuição do jogo em um mecanismo aplicável a uma coleção de registros.

### Coleção visual

```text
índice       0    1    2    3    4    5    6    7    8    9   10
matrícula   11   18   25   31   42   57   63   71   84   92   97
```

Procurar `84`.

Em cada passo, mostrar:

- `inicio`;
- `fim`;
- `meio`;
- valor examinado;
- região descartada;
- região que permanece ativa.

Sequência esperada:

```text
meio = 5  → valor 57 → descartar índices 0..5
meio = 8  → valor 84 → encontrado
```

Depois procurar um valor inexistente, por exemplo `70`, até que `inicio > fim`.

### Regra visual para o Notebook Mestre

- região ativa: cor principal;
- posição examinada: destaque forte;
- região descartada: cinza e menor contraste;
- alvo: cor distinta;
- no máximo uma decisão nova por quadro/slide.

Não usar apenas diagramas textuais na apresentação. O Notebook deverá gerar diagramas HTML/CSS ou imagens vetoriais simples que permaneçam legíveis na projeção.

### Recurso externo

Usar, após a visualização própria, uma animação de busca binária no [VisuAlgo](https://visualgo.net/en/bst) ou em página equivalente disponível no momento da aula.

O recurso externo deve:

- complementar o material;
- permitir avanço passo a passo;
- ser testado antes da aula;
- possuir alternativa autocontida no Notebook Mestre caso não haja acesso à internet.

---

## Movimento 4 — Notebook Estudante: prever o caminho

**Tempo de referência: 15 min**

### Chamada visual obrigatória

A apresentação deve exibir de forma explícita:

> **ATIVIDADE — Abra agora o Notebook Estudante: Atividade 1 — Quais posições serão examinadas?**

O Notebook Mestre deverá conter botão/link direto para o Notebook Estudante.

### Desafio

Fornecer uma coleção ordenada com 31 elementos e um alvo existente. Antes de executar qualquer código, cada estudante ou dupla deverá registrar:

1. o primeiro índice examinado;
2. o valor encontrado nesse índice;
3. a metade descartada;
4. a próxima posição examinada;
5. a sequência completa de índices até localizar o alvo;
6. a quantidade de comparações.

Em seguida, repetir rapidamente com um alvo inexistente.

### Níveis de apoio

- **apoio 1:** tabela para preencher `inicio`, `fim` e `meio`;
- **apoio 2:** fórmula `meio = (inicio + fim) // 2`;
- **extensão:** prever o maior número de comparações possível com 31 elementos.

### Evidência esperada

O estudante consegue justificar cada descarte usando a ordenação e não apenas reproduzir uma sequência decorada.

### Retorno

O professor retoma a projeção e reconstrói uma das soluções com contribuições da turma.

---

## Movimento 5 — Da execução manual ao algoritmo

**Tempo de referência: 15 min**

### Objetivo

Mapear as decisões já realizadas para uma implementação iterativa simples.

### Código incompleto inicial

```python
def busca_binaria(matriculas, alvo):
    inicio = 0
    fim = len(matriculas) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        valor = matriculas[meio]

        # completar as decisões

    return -1
```

### Construção coletiva

Perguntar antes de revelar cada bloco:

- quando retornamos `meio`?
- se `valor < alvo`, qual região pode ser descartada?
- por que o novo `inicio` é `meio + 1`?
- se `valor > alvo`, como muda `fim`?
- o que significa sair do `while`?

### Implementação resultante

```python
def busca_binaria(matriculas, alvo):
    inicio = 0
    fim = len(matriculas) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        valor = matriculas[meio]

        if valor == alvo:
            return meio
        elif valor < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1
```

### Instrumentação

Criar uma segunda versão que também devolva ou registre o número de comparações e, para coleções pequenas, o caminho percorrido.

### Erros a explorar deliberadamente

- usar `while inicio < fim` e perder casos de um elemento;
- atualizar `inicio = meio` ou `fim = meio`, impedindo progresso;
- esquecer o caso inexistente;
- executar a função sobre dados desordenados e obter resultado incorreto.

Os erros devem ser usados para raciocínio, não apenas corrigidos pelo professor.

---

## Movimento 6 — A pré-condição não é detalhe

**Tempo de referência: 10 min**

### Experimento curto

Executar a busca binária em uma coleção propositalmente desordenada.

Exemplo:

```python
matriculas = [11, 18, 84, 31, 42, 57, 63, 71, 25, 92, 97]
```

Perguntar:

> Se o algoritmo não encontra um elemento que existe, o código está necessariamente errado?

### Mensagem central

> **A correção de um algoritmo pode depender de pré-condições sobre os dados.**

Explicitar que a coleção precisa estar ordenada **pela mesma chave utilizada na comparação**. Uma lista de estudantes ordenada por nome não sustenta busca binária por matrícula.

### Ponte para S03

> Obter essa propriedade e preservá-la custa trabalho.

---

## Movimento 7 — De onde vem `O(log n)`?

**Tempo de referência: 10 min**

### Construção intuitiva

Partir de `1.000.000` de registros:

```text
1.000.000 → 500.000 → 250.000 → 125.000 → ... → 1
```

Perguntar:

> Quantas vezes podemos dividir aproximadamente um milhão por dois até restar uma possibilidade?

Apresentar a comparação:

| `n` | busca sequencial — pior caso | busca binária — aprox. |
|---:|---:|---:|
| 10 | 10 | 4 |
| 100 | 100 | 7 |
| 1.000 | 1.000 | 10 |
| 1.000.000 | 1.000.000 | 20 |
| 1.000.000.000 | 1.000.000.000 | 30 |

### Formalização

Usar `log₂(n)` como resposta à pergunta:

> **Quantas divisões sucessivas por dois são necessárias para reduzir `n` a aproximadamente 1?**

Associar:

```text
busca sequencial → O(n)
busca binária    → O(log n)
```

Não exigir cálculo algébrico de logaritmos. O foco é compreender o mecanismo de redução.

---

## Movimento 8 — Desafio de escala

**Tempo de referência: 10 min**

### Chamada visual obrigatória

> **ATIVIDADE — Notebook Estudante: Atividade 2 — Um milhão de registros.**

### Atividade

Antes de executar, preencher:

| `n` | grande diferença esperada? | comparações sequenciais | comparações binárias estimadas |
|---:|---|---:|---:|
| 100 |  |  |  |
| 1.000 |  |  |  |
| 10.000 |  |  |  |
| 100.000 |  |  |  |
| 1.000.000 |  |  |  |

Perguntas:

- em que escala a diferença parece conceitualmente marcante?
- o que deve crescer em linha aproximadamente reta quando representado contra `n`?
- qual estratégia deve parecer quase achatada na mesma escala?

As respostas serão confrontadas com o benchmark.

### Ponto natural de interrupção

Se o primeiro encontro terminar neste ponto, a retomada será:

> **Construímos uma previsão teórica. Agora vamos produzir evidências experimentais.**

---

## Movimento 9 — Benchmark: sequencial × binária

**Tempo de referência: 20 min**

### Objetivo

Confrontar as previsões com duas medidas diferentes:

- número de comparações;
- tempo medido.

### Tamanhos iniciais

```text
10², 10³, 10⁴, 10⁵, 10⁶
```

Os valores devem ser validados no ambiente final. O experimento não pode consumir tempo excessivo nem depender de uma única execução.

### Condições

- usar os mesmos dados ordenados;
- buscar alvos comparáveis;
- incluir caso existente próximo ao final e caso inexistente;
- repetir medições de tempo;
- usar mediana;
- registrar ambiente e parâmetros;
- contar comparações independentemente do cronômetro.

### Sequência didática

1. recuperar as previsões da Atividade 2;
2. executar primeiro uma escala pequena;
3. verificar a correção dos resultados;
4. executar as escalas maiores;
5. registrar CSV;
6. gerar tabela e gráfico;
7. interpretar a tendência.

### Perguntas de interpretação

- a contagem de comparações corresponde ao mecanismo previsto?
- a diferença aumenta com `n`?
- o gráfico de tempo é perfeitamente regular?
- ruído no tempo contradiz a análise assintótica?
- por que uma execução pequena pode não mostrar grande vantagem temporal?
- a busca binária poderia ser mais lenta em algum teste muito pequeno?
- isso altera sua ordem de crescimento?

### Mensagem central

> **Big-O explica a tendência de crescimento; o benchmark mostra o comportamento de implementações concretas em condições concretas.**

---

## Movimento 10 — A provocação: então devemos ordenar tudo?

**Tempo de referência: 15 min**

### Objetivo

Evitar a conclusão simplista de que busca binária é sempre a melhor escolha.

### Custos a tornar visíveis

- ordenar inicialmente;
- inserir mantendo a ordem;
- reordenar após alterações;
- armazenar ou manter estruturas auxiliares;
- realizar poucas ou muitas consultas.

### Cenários para decisão

#### Cenário A — muitas inserções, poucas consultas

Os dados chegam continuamente, mas uma consulta por matrícula é rara.

Pergunta:

> O custo de manter a coleção ordenada será recuperado pelas consultas?

#### Cenário B — carga única, muitas consultas

Um conjunto histórico é carregado uma vez e consultado milhões de vezes.

Pergunta:

> Faz sentido pagar uma vez pelo preparo e economizar em cada consulta?

#### Cenário C — inserções e consultas contínuas

O sistema recebe novos registros e também realiza muitas consultas.

Pergunta:

> Que propriedade gostaríamos de preservar sem reorganizar toda a coleção a cada alteração?

Não apresentar ainda a resposta estrutural completa. Usar a questão como ponte para conteúdos futuros.

### Decisão em duplas

Cada dupla deverá escolher uma estratégia preliminar para um cenário e justificá-la usando:

- volume de dados;
- frequência de inserções;
- frequência de buscas;
- pré-condição;
- custos conhecidos.

### Formalização

> **Uma operação mais eficiente pode depender de preparação e manutenção. A escolha exige observar o conjunto de operações do problema.**

---

## Movimento 11 — Síntese e saída

**Tempo de referência: 5 min**

### Síntese coletiva

Completar oralmente:

1. A busca sequencial examina...
2. A busca binária elimina...
3. A busca binária exige...
4. `O(log n)` aparece porque...
5. Ordenar pode compensar quando...

### Registro final curto

No Notebook Estudante:

> Em no máximo três frases, responda: **por que a busca binária não é apenas uma busca sequencial mais rápida?**

### Ponte

> Se queremos pesquisar rapidamente e também alterar os dados continuamente, que estruturas podem nos ajudar a preservar uma organização útil?

---

# 7. Distribuição dos aproximadamente 160 minutos

| Tempo | Movimento | Predominância | Evidência produzida |
|---:|---|---|---|
| 0–10 | problema e escala | discussão | hipóteses iniciais |
| 10–25 | jogo humano | participação | estratégia de redução |
| 25–40 | intervalo visual | visualização | explicação dos descartes |
| 40–55 | Atividade 1 | estudantes | caminho previsto |
| 55–70 | implementação coletiva | código | função executável |
| 70–80 | pré-condição | experimento curto | falha em dados desordenados |
| 80–90 | origem de `O(log n)` | formalização | estimativa de comparações |
| 90–100 | Atividade 2 | estudantes | hipóteses para o benchmark |
| 100–120 | benchmark | experimento | CSV, tabela e gráfico |
| 120–135 | interpretação | discussão | relação teoria × medição |
| 135–150 | ordenar custa | decisão em duplas | justificativa por cenário |
| 150–155 | compartilhamento | discussão | comparação de decisões |
| 155–160 | síntese e saída | registro | resposta de fechamento |

Os tempos são referências flexíveis. Nenhum bloco predominantemente expositivo deverá ultrapassar aproximadamente 10–15 minutos sem uma pergunta, previsão, manipulação visual ou ação dos estudantes.

---

# 8. Plano para os dois encontros

A semana permanece uma unidade contínua. A divisão abaixo é apenas operacional.

## Possível encerramento do primeiro encontro

Ponto preferencial: após a Atividade 2, com as previsões do benchmark registradas.

Fechamento:

> Hoje descobrimos uma estratégia e formulamos uma previsão. No próximo encontro, verificaremos até onde a evidência sustenta nossa explicação.

## Retomada do segundo encontro

Não repetir toda a implementação. Recuperar em até cinco minutos:

- o que é descartado em cada passo;
- por que a ordem é necessária;
- as previsões registradas.

Em seguida, iniciar o benchmark.

## Alternativa se o ritmo for mais lento

- preservar obrigatoriamente execução manual, implementação mínima, pré-condição, `O(log n)` e benchmark;
- reduzir a quantidade de casos do jogo humano;
- executar apenas parte das escalas do benchmark em sala e mostrar o CSV validado;
- realizar somente dois dos três cenários finais, deixando o terceiro como exercício.

Não retirar a previsão anterior ao benchmark nem a interpretação posterior.

---

# 9. Orientações para o Notebook Mestre e a apresentação

O Notebook Mestre será a fonte de conteúdo e da apresentação Quarto/Reveal.js.

## Regras técnicas

- não incluir metadados de formato no notebook que possam reintroduzir conflito com a renderização;
- utilizar o padrão técnico e o CSS já validados;
- manter códigos legíveis na projeção;
- evitar células com saídas excessivamente longas;
- testar links e navegação antes da aula;
- oferecer alternativa local para todo recurso externo;
- evitar sobreposição de textos e tabelas densas.

## Regras visuais

- uma decisão ou transformação principal por slide;
- regiões descartadas devem perder contraste progressivamente;
- `inicio`, `meio` e `fim` devem usar codificação visual consistente;
- evitar diagramas apenas em texto quando o mecanismo espacial for relevante;
- apresentar `n` versus `log₂(n)` por tabela e gráfico;
- reservar telas limpas para perguntas antes de revelar respostas;
- sinalizar explicitamente toda mudança para o Notebook Estudante;
- inserir links visíveis para recursos de visualização, inclusive VisuAlgo.

## Regra de interação

Antes de revelar o próximo estado de uma busca, perguntar:

> Qual parte pode ser descartada e por quê?

---

# 10. Notebook Estudante

O Notebook Estudante deverá conter, no mínimo:

1. **Atividade 1 — Quais posições serão examinadas?**
   - preenchimento manual de `inicio`, `fim`, `meio`;
   - alvo existente e alvo inexistente;
   - previsão antes da execução.

2. **Atividade de implementação**
   - função parcialmente completa;
   - condições e atualizações como lacunas;
   - testes mínimos fornecidos.

3. **Atividade 2 — Um milhão de registros**
   - tabela de previsões para busca sequencial e binária;
   - hipótese sobre o gráfico.

4. **Benchmark orientado**
   - execução controlada;
   - registro ou leitura dos resultados;
   - perguntas de interpretação.

5. **Decisão por cenário**
   - escolher entre não ordenar, ordenar uma vez ou manter uma organização;
   - justificar pelas operações predominantes.

6. **Síntese de saída**
   - resposta curta sobre por que a busca binária não é apenas “mais rápida”.

As respostas conceituais não devem ser preenchidas previamente. As chamadas do Mestre devem usar exatamente os mesmos nomes e números das atividades.

---

# 11. Benchmark da semana

O benchmark é necessário e integra o núcleo da S04.

## Arquivos previstos

- `EGC5310-EstruturasDados-S04-05-Benchmark.py`
- `EGC5310-EstruturasDados-S04-05-Benchmark.csv`
- `EGC5310-EstruturasDados-S04-05-Benchmark.md`

## Implementações comparadas

- busca sequencial instrumentada;
- busca binária iterativa instrumentada.

## Variáveis registradas

- tamanho `n`;
- algoritmo;
- tipo de alvo;
- repetição;
- número de comparações;
- tempo medido;
- mediana do tempo.

## Resultados visuais

- tabela comparativa;
- gráfico do número de comparações;
- gráfico do tempo em escala adequada;
- possibilidade de escala logarítmica quando ajudar a leitura, com explicação explícita.

## Validação necessária

- ambas as funções devem devolver o mesmo resultado;
- os dados da busca binária devem estar ordenados;
- os tamanhos devem executar em tempo compatível com a aula;
- o caso inexistente deve ser controlado;
- a contagem de comparações deve ser verificada manualmente em entradas pequenas;
- resultados oficiais devem ser reproduzíveis por semente ou geração determinística.

---

# 12. Avaliação formativa e evidências

Durante a aula, observar se o estudante:

- usa a ordenação para justificar um descarte;
- diferencia índice de valor;
- atualiza corretamente os limites;
- identifica o caso de alvo inexistente;
- prevê antes de executar;
- explica `O(log n)` por reduções sucessivas;
- distingue comparações de tempo medido;
- reconhece o custo de preparar os dados;
- utiliza o padrão de operações para justificar uma escolha.

## Perguntas diagnósticas-chave

1. Se o valor do meio é menor que o alvo, por que podemos descartar também o próprio meio?
2. A busca binária funciona se a lista estiver ordenada por nome e a busca for por matrícula?
3. Com um milhão de registros, por que o pior caso não exige meio milhão de comparações?
4. Se a busca binária foi mais lenta para dez elementos em uma medição, ela deixa de ser `O(log n)`?
5. Se haverá apenas uma consulta, compensa sempre ordenar primeiro?

## Erros conceituais a registrar

- confundir posição com matrícula;
- acreditar que a busca binária testa “qualquer metade”;
- imaginar que ordenação é opcional;
- interpretar `log n` como constante;
- concluir complexidade por um único tempo;
- afirmar que a busca binária é sempre a melhor escolha.

---

# 13. Materiais e preparação do professor

Antes da aula:

- renderizar e revisar integralmente a apresentação;
- conferir legibilidade em tela de projeção;
- testar a visualização externa e preparar alternativa local;
- executar o benchmark no ambiente utilizado em sala;
- verificar os tempos máximos;
- conferir o CSV e os gráficos oficiais;
- testar todas as células do Notebook Mestre;
- testar o Notebook Estudante do início ao fim;
- confirmar os links entre Mestre e Estudante;
- preparar a coleção física ou visual do jogo humano;
- ter uma versão pequena da tabela `inicio`–`fim`–`meio` para reconstrução no quadro;
- marcar o ponto provável de interrupção entre os encontros.

---

# 14. Artefatos da Semana 04

Serão produzidos, um por vez:

- `EGC5310-EstruturasDados-S04-01-Roteiro.md`;
- `EGC5310-EstruturasDados-S04-03-Aula.ipynb`;
- `EGC5310-EstruturasDados-S04-04-Estudante.ipynb`;
- `EGC5310-EstruturasDados-S04-05-Benchmark.py`;
- `EGC5310-EstruturasDados-S04-05-Benchmark.csv`;
- `EGC5310-EstruturasDados-S04-05-Benchmark.md`;
- `EGC5310-EstruturasDados-S04-06-Exercicios.md`;
- `EGC5310-EstruturasDados-S04-07-Solucoes.md`;
- `EGC5310-EstruturasDados-S04-08-Revisao.md`.

Não haverá PPTX independente nesta semana. A apresentação será gerada a partir do Notebook Mestre com Quarto/Reveal.js.

---

# 15. Critérios de sucesso da semana

A semana será considerada bem-sucedida se:

- a maior parte dos estudantes conseguir executar manualmente ao menos uma busca binária;
- os estudantes justificarem descartes usando a ordenação;
- a implementação surgir das decisões já compreendidas;
- as previsões forem registradas antes do benchmark;
- o benchmark for efetivamente executado e interpretado;
- a turma perceber o contraste entre `n` e `log n`;
- a discussão final impedir a conclusão “devemos ordenar tudo”;
- houver maior participação e desafio do que nas semanas anteriores;
- os recursos visuais ajudarem a explicar o mecanismo sem depender do código;
- o formato Notebook Mestre + Quarto sustentar a alternância entre investigação, visualização e execução.

---

# 16. Síntese conceitual para o professor

A S04 não é uma aula sobre decorar duas funções de busca. É uma investigação sobre como **informação estrutural nos dados** muda o trabalho necessário para responder a uma consulta.

A busca sequencial sabe apenas se o elemento atual corresponde ao alvo. A busca binária extrai mais informação de cada comparação porque a coleção está ordenada: além de saber que o meio não é o alvo, ela sabe em qual metade o alvo ainda poderia estar.

Por isso:

> **A eficiência da busca binária não está apenas no código. Está na relação entre algoritmo e organização dos dados.**

O contraste `O(n)` × `O(log n)` deve ser marcante, mas não encerrar a discussão. O fechamento correto é:

> **Organizar pode reduzir muito o custo das consultas, mas organizar e manter a organização também custa. A decisão depende do padrão de operações.**
