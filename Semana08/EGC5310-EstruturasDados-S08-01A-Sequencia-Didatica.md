# EGC5310 — Semana 08 — Sequência Didática

**Disciplina:** EGC5310 — Tópicos Especiais em Ciência de Dados VI  
**Projeto pedagógico:** Estruturas de Dados para Ciência de Dados  
**Semana:** 08 — 01 e 02/10/2026  
**Artefato:** 01A — Sequência Didática  
**Versão:** 1.0  
**Status:** pronta para orientar a produção do Mestre e dos notebooks  
**Última revisão:** 01/10/2026  
**Referência:** S08-01-Roteiro.md, validado pelo professor  
**Duração:** 160 minutos úteis

## 1. Função deste documento

Detalhar como conduzir a construção do raciocínio: o que apresentar, quando perguntar, que resposta esperar, como intervir e como passar ao próximo problema. O Roteiro estabelece objetivos e organização; este documento explicita a mediação. Respostas esperadas são hipóteses pedagógicas, não resultados observados da turma.

Na S07 houve atividade em casa e ainda não há feedback. Não atribuir aos alunos domínio ou dificuldades com base nessa atividade. Registrar evidências apenas quando surgirem no diagnóstico e nas tarefas da S08.

A semana é uma sequência contínua. Código, perguntas, exemplos visuais e interpretação ficam no Notebook Mestre, com chamadas explícitas para o Estudante. Não transformar a apresentação em uma lista de links para implementação externa.

## 2. Mapa da progressão

| Minutos | Atividade | Questão que conduz o bloco | Evidência a recolher |
|---|---|---|---|
| 0–10 | A1 — Diagnóstico | O que significa produzir uma ordem? | três respostas individuais |
| 10–25 | A2 — Inserção | Como ampliar uma parte já ordenada? | previsão, trecho preenchido e explicação de um deslocamento |
| 25–55 | A3 — Intercalação | Como combinar duas partes ordenadas? | escolhas justificadas e explicação de caso-base |
| 55–85 | A4 — Pivô | Dividir por posição e por valor produz o mesmo tipo de parte? | partições e previsão de equilíbrio |
| 85–100 | A5 — Contagem | É necessário comparar pares quando o domínio é pequeno? | frequências, reconstrução e definição de k |
| 100–125 | A6 — Benchmark | Que hipótese cada medida permite investigar? | previsão e interpretação dos resultados |
| 125–155 | A7 — UCI | Como ordenar registros mantendo suas associações? | implementação com key e verificações |
| 155–160 | A8 — Síntese | Qual estratégia atende a qual condição? | justificativa técnica individual |

Regra recorrente: perguntar antes de executar; mostrar código após compreender a ação; ler os prints para explicar estados; formalizar custo após identificar trabalho; terminar a atividade com interpretação.

## 3. A1 — Diagnóstico e abertura (0–10 min)

### Apresentar

Projetar a sequência sintética `[8, 3, 7, 1, 6, 2, 5, 4]`. Identificar explicitamente sua origem fictícia. Anunciar: vamos investigar estratégias que produzem ordem; os números pequenos permitem acompanhar todas as ações. Dados reais entram no fim.

Pedir três respostas individuais, antes da discussão:

1. Se inserirmos chaves 8, 3 e 7 em um dict, ele estará ordenado numericamente?
2. Se busca binária encontra a posição de inserção, desaparece o custo de deslocar elementos de uma list?
3. Ordenar `[3, 1, 3]` permite descartar uma das ocorrências de 3?

### Esperar e intervir

| Resposta esperada | Erro possível | Intervenção |
|---|---|---|
| ordem de inserção e ordem numérica são propriedades diferentes | dict é ordenado, logo ordena valores | pedir que escrevam a sequência de chaves e depois a sequência numérica |
| localizar posição e abrir espaço são trabalhos diferentes | O(log n) vale para toda a inserção | desenhar a posição encontrada e perguntar onde ficam os elementos seguintes |
| ordenar preserva ocorrências | repetidos devem ser eliminados | perguntar se duas vendas do mesmo valor são uma única venda |

Não dar uma nova aula completa de hashing. Corrigir o pré-requisito e recolher uma frase ou resposta que indique o estado atual da compreensão.

### Transição

“Já sabemos que ordem não aparece só porque armazenamos os dados. Vamos construir uma parte ordenada e descobrir como fazê-la crescer.”

## 4. A2 — Insertion Sort (10–25 min)

### 4.1 Ação antes da função

Mostrar `[3, 8 | 7, 1, 6, 2, 5, 4]`, com o prefixo destacado. Perguntar: onde entra 7? O que precisa mover? Esperar: 8 desloca para a direita, 7 ocupa sua posição anterior e o prefixo passa a ter três elementos ordenados.

Mostrar a função curta no Mestre. Identificar i como o próximo elemento, atual como o valor salvo e j como a posição examinada à esquerda. Não começar pela memorização dos índices.

### 4.2 Ler o estado temporário

Para inserir 3 na entrada inicial, a situação passa por:

| Estado | Lista | Variável atual |
|---|---|---:|
| início | `[8, 3, 7, 1, 6, 2, 5, 4]` | 3 |
| após deslocar 8 | `[8, 8, 7, 1, 6, 2, 5, 4]` | 3 |
| após inserir atual | `[3, 8, 7, 1, 6, 2, 5, 4]` | 3 |

Perguntar: “O 3 desapareceu?” Esperar: continua salvo em atual. Se houver confusão, acompanhar a atribuição que salvou esse valor antes do while. Explicar que um estado intermediário não precisa ter todas as propriedades da saída final.

Os prints devem marcar início da inserção, origem/destino de cada deslocamento e posição final. Ativar mostrar_passos apenas na sequência pequena.

### 4.3 Chamada da atividade

**AGORA É COM VOCÊ → Notebook Estudante · Atividade 2**

Tarefa: prever a inserção do valor 1; completar o deslocamento e a inserção final; executar; explicar por que atual é necessário. Exigir uma previsão curta antes de rodar.

Ao retornar, perguntar qual propriedade vale após cada iteração externa. Esperar: o prefixo até i está ordenado e contém os mesmos elementos daquele prefixo original.

### 4.4 Custo e transição

Comparar entrada ordenada e invertida com valores distintos. Na ordenada, o while não desloca; ainda existe uma passagem pelo laço externo e testes. Na invertida, o número de deslocamentos cresce como 1 + 2 + ... + (n−1). Relacionar melhor caso O(n) e pior caso O(n²) a essa versão.

“Estamos inserindo em uma parte que cresce. E se ordenarmos partes menores e depois as reunirmos?”

## 5. A3 — Merge Sort (25–55 min)

### 5.1 Primeiro intercalar, depois dividir

Apresentar `[1, 3, 7, 8]` e `[2, 4, 5, 6]`, já ordenadas. Perguntar qual valor deve ser o primeiro e por que podemos ignorar temporariamente o restante de cada lista. Esperar: o menor elemento ainda disponível está no início de uma das duas partes ordenadas.

Avançar manualmente até obter `[1, 2, 3, 4]`. Pedir o estado dos índices: i = 2 e j = 2, se começaram em zero. Associar índice ao próximo elemento não consumido, não ao último colocado.

### 5.2 Código da intercalação

Mostrar no Mestre o while que compara esquerda[i] e direita[j]. Perguntar em qual lista resultado recebe o elemento e qual índice avança. Exibir print após cada escolha: origem, elemento e resultado parcial.

Depois perguntar: “Se uma parte acabar, o que fazemos com a outra?” Esperar: acrescentar os elementos restantes na ordem atual. Não reiniciar a ordenação nem descartar a sobra. Explicar as fatias finais e o fato de também terem custo proporcional ao que copiam.

Em empate, usar <= para escolher da esquerda. Com registros sintéticos rotulados, por exemplo `(2, 'A')` à esquerda e `(2, 'B')` à direita, demonstrar que escolher da esquerda preserva a ordem anterior de A e B. Comparar apenas a chave numérica; não deixar a comparação de tuplas decidir o desempate silenciosamente.

### 5.3 Chamada da atividade

**AGORA É COM VOCÊ → Notebook Estudante · Atividade 3**

Tarefa: intercalar `[1, 4, 7]` com `[2, 4, 6]`; registrar os primeiros quatro elementos; completar avanço dos índices e sobras; justificar a origem do 4 escolhido primeiro.

Resultado numérico esperado: `[1, 2, 4, 4, 6, 7]`. Na sequência de escolhas, o 4 da esquerda precede o da direita.

### 5.4 Introduzir a recursão

Voltar à sequência comum, ainda desordenada. Mostrar divisão por posição, até partes de tamanho 1. Prints indicam nível e partes; limitar profundidade exibida. Mostrar a função recursiva em separado: caso-base, ponto médio, chamadas e intercalação.

Perguntas: “Como garantimos que termina?” — os tamanhos diminuem até 0 ou 1. “Por que uma parte de tamanho 1 já está ordenada?” — não existe par fora de ordem. “Quando a lista de tamanho 8 fica ordenada?” — ao intercalar as duas metades já ordenadas.

Erro possível: achar que a divisão já ordenou os dados. Intervenção: mostrar a metade `[8, 3, 7, 1]` após a primeira divisão e pedir que apontem a ordem.

### 5.5 Custo e transição

Somar elementos processados em cada nível de intercalação e observar trabalho O(n). A divisão em metades produz O(log n) níveis. Não exigir solução formal de recorrência. As fatias e listas auxiliares da implementação são parte da explicação: ela não é in-place.

“A divisão por posição equilibra tamanhos. Podemos dividir usando os valores em vez das posições?”

## 6. A4 — Quicksort (55–85 min)

### 6.1 Particionar sem ordenar internamente

Escolher primeiro elemento da sequência comum: pivô 8. Pedir os grupos antes de executar. Esperar menores = `[3, 7, 1, 6, 2, 5, 4]`, iguais = `[8]`, maiores = `[]`. Os menores ainda estão desordenados.

Experimentar pivô 4 na mesma entrada: menores = `[3, 1, 2]`, iguais = `[4]`, maiores = `[8, 7, 6, 5]`. Mostrar que esse passo estabelece relação entre os grupos, não ordem interna em cada grupo.

### 6.2 Código e rastreamento

Usar um laço explícito com if/elif/else, mantendo cada ocorrência no grupo correspondente. Mostrar print do pivô, grupos e seus tamanhos após o particionamento. Ao combinar, imprimir o resultado do nível. As chamadas recursivas vão para menores e maiores; iguais não volta à recursão.

Perguntar: “Por que usar um grupo de iguais?” Esperar: preservar multiplicidade e tratar esses valores sem recursão adicional. Em `[4, 4, 4, 4]`, a versão de três grupos encerra após uma partição; isso não é o caso adverso usado para expor o comportamento quadrático.

### 6.3 Chamada da atividade

**AGORA É COM VOCÊ → Notebook Estudante · Atividade 4**

Tarefa: completar as condições dos grupos; particionar a sequência comum com pivôs 8 e 4; registrar tamanhos; prever qual escolha tende a gerar menor profundidade nesse exemplo. Resultado: pivô 4 produz divisão mais equilibrada. Não concluir que 4 seria universalmente melhor.

### 6.4 Caso adverso

Usar `[1, 2, 3, 4, 5, 6, 7, 8]` com primeiro elemento como pivô. Mostrar partições 0/1/7 e depois 0/1/6. Pedir a previsão do passo seguinte. Relacionar O(n²) ao trabalho aproximadamente n + (n−1) + ... em partições muito desequilibradas.

Comparar com pivô aleatório, separando regra de escolha e mecanismo de partição. Usar semente reproduzível. Não prometer divisão equilibrada em toda chamada: a melhoria é esperada probabilisticamente. Elemento central por posição não equivale à mediana dos valores.

Contrastar com Merge Sort em uma tabela: posição versus valor; equilíbrio garantido pela divisão versus dependência do pivô; intercalar versus particionar. Explicar que esta versão didática de Quicksort aloca grupos e concatena listas. Não lhe atribuir automaticamente propriedades de memória de versões in-place.

### Transição e pausa possível

Se o encontro terminar aqui, registrar: “Na próxima etapa, vamos tentar ordenar sem comparar pares de valores.” Retomar com a partição produzida, sem reiniciar a semana.

## 7. A5 — Counting Sort (85–100 min)

### 7.1 Mudar o domínio

Apresentar `[3, 1, 3, 0, 5, 2, 1, 5]` como inteiros não negativos. Perguntar se é necessário compará-los dois a dois quando sabemos que os valores estão entre 0 e 5.

Exibir contagens de tamanho 6: `[1, 2, 1, 2, 0, 2]`. Perguntar o significado de contagens[3]. Esperar: existem duas ocorrências do valor 3, não que o terceiro elemento da entrada seja 2.

Mostrar inicialização, incremento e reconstrução em trechos de código. Os prints exibem a tabela após contar e a saída parcial após cada valor com frequência positiva. Resultado esperado: `[0, 1, 1, 2, 3, 3, 5, 5]`.

### 7.2 Chamada da atividade

**AGORA É COM VOCÊ → Notebook Estudante · Atividade 5**

Completar incremento e reconstrução; explicar n = 8 e k = 6; prever o efeito de acrescentar um valor 1.000.000. Na versão adotada k é maior_valor + 1, não quantidade de valores distintos. Antes de alocar um domínio enorme, discutir a previsão.

### 7.3 Limites e transição

O custo é O(n + k): ler/escrever elementos e inicializar/percorrer domínio. A versão trabalha com inteiros não negativos; índices negativos de Python não tornam valores negativos compatíveis com ela. Reconstruir números não preserva automaticamente os atributos de registros.

Retomar hashing: índice de contagem tem correspondência ordenada com valor; posição hash não precisa preservar essa relação. Bucket Sort pode ser citado como distribuição por faixas seguida de ordenação interna. Radix Sort pode ser citado como etapas por componentes da chave, sem tarefa adicional.

“Agora temos previsões sobre mecanismos. Vamos medi-las sob condições controladas.”

## 8. A6 — Benchmark (100–125 min)

### 8.1 Hipóteses antes de medir

**AGORA É COM VOCÊ → Notebook Estudante · Atividade 6**

Pedir previsões escritas:

- entrada ordenada reduzirá os deslocamentos do Insertion Sort;
- entrada ordenada com valores distintos desfavorecerá Quicksort de primeiro pivô;
- Merge Sort continuará dividindo por posição em partes semelhantes;
- aumentar k mantendo n fixo acrescentará custo e espaço ao Counting Sort.

Não exigir tempos em milissegundos. Pedir direção da mudança e mecanismo responsável.

### 8.2 Execução

Explicar origem sintética e seed. Usar n = 100, 300, 600 inicialmente, sem ampliar automaticamente o caso recursivo adverso. Validar saída contra sorted antes de medir. Cada repetição recebe cópia equivalente preparada fora do cronômetro. Prints e contadores ficam desativados no ensaio de tempo; alocações internas do algoritmo são parte da execução medida.

Mostrar no Mestre apenas o trecho central do cronômetro, a tabela e gráficos necessários à interpretação. Registrar mediana, repetições e ambiente no CSV. As contagens instrumentadas são resultados de ensaio separado. Download e leitura de dados não integram esse experimento.

### 8.3 Discussão

Perguntar: “O dado confirma a hipótese? Qual linha ou mecanismo explica a diferença?” Se os tempos forem ruidosos, discutir resolução, repetição e tamanho antes de modificar a explicação teórica. Não tratar tempo isolado como demonstração de Big-O.

Sorted serve de referência prática otimizada. Não dizer que a diferença entre ele e um algoritmo Python didático é causada apenas pela ordem de crescimento. Não apresentar o CSV sintético como resultado dos dados UCI.

Transição: “Nos experimentos, ordenamos números. Em uma venda, o valor precisa continuar associado ao item certo.”

## 9. A7 — Repositório online e registros reais (125–155 min)

### 9.1 Obter e compreender (aproximadamente 7 min)

Apresentar fonte oficial Online Retail/UCI e atribuição de Chen (2015). Link: https://archive.ics.uci.edu/dataset/352/online+retail. Reutilizar XLSX já disponível ou baixá-lo do ZIP oficial. Preparar cópia previamente para falha de rede. A leitura pode consumir tempo; executar uma única vez e fornecer a célula de obtenção pronta.

Antes dos filtros, criar id_linha a partir da posição original. Mostrar colunas e 5 linhas. Perguntar se InvoiceNo identifica um item único. Esperar: uma fatura pode conter várias linhas; não eliminar repetidos apenas por terem mesma fatura ou produto.

Selecionar quantidade/preço presentes e positivos e excluir InvoiceNo iniciado por C/c para este cenário de vendas positivas. Registrar totais e motivo do filtro. Não apresentar esse recorte como limpeza universal. Calcular valor_item = Quantity × UnitPrice, distinguindo valor do item e total da fatura. Usar os primeiros 200 registros válidos, sem afirmar representatividade estatística.

### 9.2 Adaptar o algoritmo (aproximadamente 10 min)

**AGORA É COM VOCÊ → Notebook Estudante · Atividade 7**

Fornecer estrutura do Merge Sort com parâmetro key. Estudante completa a comparação na intercalação:

```python
if key(esquerda[i]) <= key(direita[j]):
    resultado.append(esquerda[i])
    i += 1
```

Mostrar que comparação usa uma chave, enquanto append transporta o registro inteiro. Key deve ser passada às chamadas recursivas e à intercalação. Professor contém versão resolvida; Mestre mostra o trecho e uma chamada por valor_item.

Perguntar: “O que perdemos se ordenarmos só os preços?” Esperar: a associação com identificador, produto, país e quantidade. Se o aluno propuser reorganizar cada coluna separadamente, usar dois registros de valores distintos para demonstrar a troca indevida de associações.

Para rastreamento, extrair primeiro 8 registros e identificar esse recorte na saída. Mostrar antes/depois id_linha, StockCode, Country e valor_item. Ordenar separadamente os 200 com prints desligados.

### 9.3 Verificar além da aparência (aproximadamente 6 min)

Conferir ordem em todos os pares adjacentes; len da entrada/saída; Counter dos id_linha; equivalência com sorted por mesma key. Na construção desses registros, ids únicos identificam ocorrências; manter os registros originais evita alterar seus atributos. Verificação de id sozinha não prova que os atributos permaneceram intactos: a equivalência dos registros completos com o resultado de referência complementa a conferência.

Perguntar: “Os primeiros 8 valores ordenados provam que todos os 200 estão ordenados?” Esperar: não. Se não houver empate no recorte, demonstrar estabilidade com registros sintéticos explicitamente rotulados.

### 9.4 Novo requisito e interpretação (aproximadamente 7 min)

Pedir país crescente e valor decrescente dentro de cada país. Usar até 10.000 registros válidos e sorted com:

```python
key=lambda registro: (registro['Country'], -registro['valor_item'])
```

Explicar comparação lexicográfica: primeiro país; valor decide dentro do mesmo país. Reverse=True inverteria os dois critérios. Para nomes de países presentes como strings, usar a ordem padrão de comparação e não apresentá-la como colação linguística localizada.

Pedir justificativa de 4–6 linhas: fonte, critério, algoritmo/ferramenta, preservação dos registros e limite do ensaio. Não aplicar Counting Sort diretamente a valores fracionários nem arredondar sem um requisito que autorize mudança de significado.

## 10. A8 — Síntese (155–160 min)

**AGORA É COM VOCÊ → Notebook Estudante · Atividade 8**

Resposta individual: escolher uma estratégia para registros reais com valores fracionários e uma para inteiros em domínio pequeno; explicar como entrada/pivô/domínio podem mudar a decisão; indicar uma verificação necessária.

Esperar justificativas específicas, não apenas “mais rápido”. Exemplos aceitáveis: ordenação nativa com key para registros; contagem quando n e k tornam o domínio viável; explicação de desempenho adverso do primeiro pivô. Uma decisão diferente é aceitável se respeitar requisitos e apresentar evidência.

Fechar com: “Ordenação exige estratégia, critério e preservação da informação. O comportamento depende da implementação e das propriedades da entrada.” A intercalação será retomada na S09; distinguir sua função da de join relacional.

## 11. Gestão do ritmo e intervenções

| Situação observada | Ajuste autorizado | Preservar |
|---|---|---|
| dificuldade com índices | rastrear mais uma escolha em lista pequena | propriedade que cada índice representa |
| recursão ocupa tempo excessivo | fornecer função recursiva pronta e explicar uma chamada/retorno | caso-base, redução e intercalação |
| benchmark demorado | reduzir tamanhos/configurações e usar resultados já executados identificados | hipótese e interpretação |
| falha de rede | carregar o XLSX oficial previamente obtido | origem real e atribuição |
| pouco tempo na aplicação | fornecer carregamento/filtros prontos | comparação por key, registro inteiro e verificações |

Não resolver falta de tempo apagando a interpretação final. Não aumentar limite de recursão para forçar o caso adverso. Não exigir que todos implementem todos os algoritmos do zero.

## 12. Critérios para produzir o Mestre

Consultar Mestres S01–S03 antes de finalizar o design. Código e rastreamento devem ser legíveis nos slides; separar funções e saída quando excederem espaço. Para cada A1–A8, ter chamada explícita, pergunta antes da execução e slide de retorno com interpretação. Prints devem usar as mesmas variáveis da implementação exibida.

Os nomes das funções, regras de pivô, keys, dados, filtros e verificações precisam coincidir em Mestre, Estudante, Professor e benchmark. Evitar resultados extensos ou saídas truncadas que ocultem a ação em discussão. Renderização final deverá conferir código, tabelas e prints sem cortes.

## 13. Evidências a registrar depois da aula

Registrar no arquivo de Revisão respostas ou trechos de código efetivamente observados: distinção entre divisão por posição/valor; interpretação de atual; índices da intercalação; efeito do pivô; diferença entre n e k; comparação da chave mantendo o registro; distinção entre print ilustrativo e verificação completa. Anotar onde a primeira aula parou e os ajustes de tempo realizados.

Até a execução, essas evidências permanecem **não observadas**. A análise da atividade da S07 será registrada quando houver acesso às respostas.

## 14. Referências de continuidade

- EGC5310-EstruturasDados-S08-01-Roteiro.md, versão validada.
- Plano de Ensino EGC5310 — 2026/2; Guia de Desenvolvimento das Próximas Semanas.
- Chen, D. (2015). Online Retail [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5BW33.
- Goodrich, Tamassia e Goldwasser (2013), Data Structures and Algorithms in Python.
- Cormen et al. (2022), Introduction to Algorithms, 4. ed.
