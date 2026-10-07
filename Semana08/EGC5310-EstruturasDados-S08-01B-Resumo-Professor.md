# EGC5310 — Semana 08 — Resumo do Professor

**Leitura de cinco minutos antes da aula**  
**Disciplina:** EGC5310 — Tópicos Especiais em Ciência de Dados VI  
**Projeto pedagógico:** Estruturas de Dados para Ciência de Dados  
**Semana:** 08 — 01 e 02/10/2026  
**Artefato:** 01B — Resumo do Professor  
**Versão:** 1.0  
**Status:** pronto para uso; alinhado ao Roteiro e à Sequência Didática  
**Última revisão:** 01/10/2026

## A ideia da semana

**Avançar da utilidade da ordenação para os mecanismos que produzem ordem.**

Pergunta central: **como diferentes estratégias ordenam os mesmos dados, e que características da entrada alteram seu trabalho?**

Fluxo: previsão → ação visual → código → prints dos estados → mecanismo → custo → experimento → aplicação real → decisão.

O Mestre precisa mostrar o código implementado e explicar suas operações. Nas chamadas ao Estudante, indicar atividade e tarefa; no retorno, discutir o resultado. Não há feedback da atividade em casa da S07: começar com diagnóstico próprio, sem presumir aprendizagem ou dificuldades.

## Tempos e atividades

| Minutos | Atividade | Foco |
|---|---|---|
| 0–10 | A1 | diagnóstico: ordem do dict, deslocamento e multiplicidade |
| 10–25 | A2 | Insertion Sort: inserir no prefixo ordenado |
| 25–55 | A3 | Merge Sort: intercalar antes de explicar recursão |
| 55–85 | A4 | Quicksort: pivô, grupos e equilíbrio |
| 85–100 | A5 | Counting Sort: frequências, n e k |
| 100–125 | A6 | previsão e benchmark controlado |
| 125–155 | A7 | UCI: ordenar registros completos com key |
| 155–160 | A8 | decisão justificada |

## Dados e saídas que você precisa lembrar

- Sequência sintética comum: `[8, 3, 7, 1, 6, 2, 5, 4]`.
- Contagem: `[3, 1, 3, 0, 5, 2, 1, 5]` → frequências `[1, 2, 1, 2, 0, 2]` → saída `[0, 1, 1, 2, 3, 3, 5, 5]`.
- Benchmark: dados sintéticos com semente registrada; variar tamanho, organização ou domínio. CSV não representa resultados UCI.
- Aplicação real: **Online Retail/UCI**, retomando S06. Uma linha é um item de transação; InvoiceNo e StockCode podem se repetir.

## Algoritmos: pergunta, mecanismo e cuidado

| Estratégia | Pergunta para a turma | Precisão necessária |
|---|---|---|
| Insertion Sort | “O que precisa deslocar para inserir este valor?” | prefixo ordenado; atual guarda o elemento fora de sua posição |
| Merge Sort | “Qual é o próximo elemento entre estas duas partes ordenadas?” | divide por posição; trabalho central na intercalação |
| Quicksort | “Que relação o pivô estabelece entre os grupos?” | divide por valor; os grupos ainda precisam de ordenação interna |
| Counting Sort | “O que significa o índice desta contagem?” | índice representa valor; k = maior_valor + 1 nesta versão |

**Insertion Sort:** um print pode mostrar `[8, 8, ...]` durante a inserção de 3. O 3 continua salvo em atual. É deslocamento, não troca. Ordenado: O(n) nessa versão; invertido: deslocamentos 1 + 2 + ... + (n−1), O(n²).

**Merge Sort:** começar por duas partes já ordenadas. Os índices apontam os próximos elementos não consumidos. Quando uma parte termina, copiar a sobra da outra. Escolher da esquerda com <= em empate preserva estabilidade. Só depois mostrar caso-base, divisão, chamadas e retorno. O(n) por nível × O(log n) níveis. A versão didática usa fatias e listas auxiliares.

**Quicksort:** laço explícito com menores/iguais/maiores. Na sequência comum, pivô 8 gera tamanhos 7/1/0; pivô 4 gera 3/1/4. Com valores distintos ordenados e primeiro elemento como pivô, aparecem partições 0/1/(n−1): pior caso O(n²). Pivô aleatório oferece O(n log n) esperado, sem garantir equilíbrio em toda chamada. Elemento central por posição não é necessariamente mediana. Todos iguais não produzem o mesmo caso adverso nesta versão de três grupos. Ela aloca listas; não atribuir memória de versões in-place.

**Counting Sort:** inteiros não negativos. n = quantidade de elementos; k = tamanho da tabela de contagem, não quantidade de valores distintos. Custo O(n + k). Domínio enorme pode inviabilizar a estratégia. Esta reconstrução ordena números; não preserva por si só atributos associados a registros. Não aplicar diretamente a preços fracionários.

**Hashing:** posições hash não precisam preservar ordem numérica. Não apresentá-lo como algoritmo de ordenação. Bucket/Radix são extensões opcionais, sem implementação obrigatória.

## Prints: observar e explicar

Usar mostrar_passos=True apenas com entradas pequenas e limitar profundidade recursiva. Mostrar:

- inserção: atual, deslocamento e posição final;
- merge: divisão, escolha de origem e resultado intercalado;
- quicksort: pivô, grupos e tamanhos;
- contagem: tabela e reconstrução;
- UCI: 8 registros antes/depois com id, código, país e valor.

**Prints desligados no benchmark.** Contar operações em execução separada. Um recorte visual não comprova ordenação da saída inteira.

## Benchmark: não perder a interpretação

Pedir hipótese antes de executar: efeito de entrada ordenada no Insertion Sort; primeiro pivô em entrada ordenada; divisão equilibrada do Merge Sort; crescimento de k no Counting Sort.

Começar com n = 100, 300, 600. Cada repetição recebe cópia equivalente preparada fora do cronômetro; alocações internas fazem parte do algoritmo medido. Validar saída antes de medir, usar mediana e registrar ambiente/repetições. Não ampliar automaticamente o caso recursivo adverso nem elevar limite de recursão.

Sorted é referência prática otimizada. Diferença de tempo não se explica apenas por Big-O. Perguntar sempre: **“Qual mecanismo explica o resultado?”**

## Atividade final UCI: o essencial

Fonte: https://archive.ics.uci.edu/dataset/352/online+retail. Reutilizar `Online Retail.xlsx` ou obter ZIP oficial. Manter cópia previamente baixada; carregar uma vez e fora do benchmark.

1. Criar id_linha antes dos filtros. Selecionar quantidade/preço presentes e positivos e excluir InvoiceNo iniciado por C/c para este exercício. Registrar o recorte.
2. Calcular valor_item = Quantity × UnitPrice. É valor do item, não total da fatura. Floats são usados na exploração didática, não como contabilidade exata.
3. Usar primeiros 200 registros válidos; adaptar Merge Sort com key. **Comparar a chave, transportar o registro inteiro.**
4. Conferir ordem de todos os pares adjacentes, tamanho, Counter de ids e equivalência dos registros completos com sorted. IDs isoladamente não verificam integridade de atributos.
5. Ordenar até 10.000 registros por país crescente e valor decrescente usando `key=lambda r: (r['Country'], -r['valor_item'])`. Reverse=True inverteria ambos os critérios.

Recorte didático não é amostra representativa. Se faltarem empates, demonstrar estabilidade com registros sintéticos identificados. Entrega: implementação curta, previsões, prints, verificações e justificativa de 4–6 linhas.

## Se faltar tempo

Fornecer recursão pronta; reduzir configurações do benchmark; entregar carregamento e filtros prontos. Preservar compreensão do mecanismo, comparação por key, verificação e síntese. Pausa possível após particionamento do Quicksort.

## Antes de entrar em sala

Conferir Mestre/renderização e códigos legíveis; Estudante e Professor na mesma ordem; XLSX disponível; links Colab; prints pequenos; benchmark sem tracing. Na produção seguinte, recuperar diretamente dos Mestres S01–S03 os recursos de código e rastreamento que o professor valorizou.

## Fechamento

Pedir uma estratégia para registros reais e outra para inteiros em domínio pequeno, com condição e verificação. A frase que precisam defender:

> **Ordenar exige critério, estratégia e preservação da informação; o custo depende da implementação e das propriedades dos dados.**

Ponte para S09: intercalação de listas ordenadas será retomada em integração; não equivale a join relacional. Registrar aprendizagem apenas depois de observá-la em aula.

**Referências de continuidade:** Roteiro S08 e Sequência Didática S08; Chen (2015), Online Retail, https://doi.org/10.24432/C5BW33; Goodrich et al. (2013); Cormen et al. (2022).
