# EGC5310 — Semana 08 — Roteiro

**Disciplina:** EGC5310 — Tópicos Especiais em Ciência de Dados VI  
**Projeto pedagógico:** Estruturas de Dados para Ciência de Dados  
**Semana:** 08 — 01 e 02 de outubro de 2026  
**Artefato:** 01 — Roteiro  
**Versão:** 1.0  
**Status:** planejamento aprovado; produção dos demais artefatos em sequência  
**Última revisão:** 01/10/2026  
**Tempo:** aproximadamente 160 minutos úteis

## 1. Intenção da semana

Conteúdo previsto: ordenação de dados e análise experimental. A turma já utilizou ordenação como preparação para busca e discutiu deslocamento em listas. Agora deve investigar estratégias que produzem ordem: inserção, divisão/intercalação, particionamento por pivô e contagem por domínio.

Pergunta central: **Como diferentes estratégias ordenam os mesmos dados, e que características da entrada alteram seu trabalho?**

Não há feedback disponível da atividade realizada em casa na S07. Não registrar domínio dos conteúdos, dificuldades ou resultados dessa atividade como observações. A abertura da S08 produzirá um diagnóstico próprio, breve, sem substituir a futura devolutiva da avaliação.

## 2. Resultados de aprendizagem

O estudante deverá explicar o mecanismo de cada estratégia; acompanhar estados intermediários do código; relacionar instruções a comparações, deslocamentos, partições e intercalações; distinguir tamanho da entrada de tamanho do domínio; interpretar benchmark; ordenar registros reais mantendo suas associações e multiplicidade; justificar critérios e limitações.

Insertion Sort é referência breve. Merge Sort e Quicksort constituem o núcleo. Counting Sort introduz a exploração das propriedades das chaves. Radix Sort e Bucket Sort podem ser mencionados no mapa de estratégias, sem implementação obrigatória. Hashing aparece como contraste: distribuição em buckets não implica ordem.

## 3. Origem e papel dos dados

### 3.1 Exemplos didáticos: dados sintéticos explícitos

Sequência comum: `[8, 3, 7, 1, 6, 2, 5, 4]`. São dados fictícios escolhidos para permitir rastreamento manual e leitura das saídas. Reutilizá-la no Insertion Sort, Merge Sort e Quicksort. Acrescentar casos vazio, unitário, repetido, ordenado e invertido nas verificações.

Para Counting Sort: `[3, 1, 3, 0, 5, 2, 1, 5]`, inteiros não negativos em domínio pequeno. Não aplicar essa versão a preços fracionários nem converter preços arbitrariamente para inteiros apenas para fazê-la funcionar.

### 3.2 Benchmark: entradas sintéticas controladas

Gerar entradas reproduzíveis com semente registrada. Variar uma dimensão por vez: n, organização inicial ou k. Nomear a origem como sintética no CSV. Esses dados permitem controlar condições que o dataset real não oferece diretamente.

### 3.3 Atividade final: dados reais de repositório online

Fonte: **Online Retail, UCI Machine Learning Repository**, também utilizado na S06. Não é necessário introduzir um novo domínio nem depender dos datasets da avaliação S07.

- Página oficial: https://archive.ics.uci.edu/dataset/352/online+retail
- Download oficial: https://archive.ics.uci.edu/static/public/352/online+retail.zip
- Arquivo: `Online Retail.xlsx`.
- Referência: Chen, D. (2015). Online Retail [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5BW33.
- Licença informada pela fonte: CC BY 4.0; preservar atribuição.

Uma linha corresponde a um item de transação, não a um produto único nem ao valor total de uma fatura. Manter `InvoiceNo`, `StockCode`, `Quantity`, `UnitPrice` e `Country`. Criar `id_linha` a partir da posição no arquivo original, antes dos filtros. Esse identificador distingue ocorrências; `InvoiceNo` e `StockCode` podem se repetir.

Para o cenário didático de vendas positivas, selecionar quantidade e preço presentes e positivos e excluir códigos de fatura iniciados por C/c. Registrar linhas lidas e removidas. O recorte é uma decisão do exercício, não uma limpeza universal nem uma análise financeira completa.

Derivar `valor_item = Quantity * UnitPrice`. Não chamar essa medida de valor do pedido. Usar floats para a exploração didática, sem apresentar os resultados como contabilidade monetária exata.

Carregar o arquivo uma vez. A leitura do XLSX não integra o cronômetro da ordenação. Usar os primeiros 200 registros válidos, na ordem original, para implementação; mostrar apenas 8 nos prints. Para aplicação nativa, usar até 10.000 registros válidos, sem extrapolar conclusões para o arquivo completo. O recorte é didático, não amostra representativa.

O notebook deverá permitir download oficial e reutilização do arquivo local. Se houver falha de rede, o professor disponibiliza o mesmo XLSX previamente baixado. Nunca substituir dados reais por sintéticos sem informar. Os blocos com exemplos sintéticos continuam executáveis independentemente da rede.

## 4. Organização do Notebook Mestre

Preservar `S08-99-Aula-Mestre.ipynb` como fonte para Quarto/Reveal.js. Recuperar as características das S01–S03: código visível, perguntas antes da execução, exemplos guiados, estados intermediários, discussão do mecanismo e atividades integradas. Na produção do Mestre, consultar essas versões diretamente antes de definir seus recursos de apresentação.

Cada bloco deve seguir: problema pequeno → previsão → execução visual → código → rastreamento → custo → atividade → interpretação. Não substituir o código por uma indicação genérica de abrir outro notebook.

Funções pequenas aparecem completas; funções maiores são explicadas por responsabilidade e depois reunidas no notebook. Evitar um slide com toda a recursão, a intercalação e a instrumentação juntas. Usar nomes em português e saídas curtas. Manter configurações de apresentação fora do conteúdo conforme o padrão vigente; não reintroduzir metadados de format conflitantes.

Chamadas: **AGORA É COM VOCÊ → Notebook Estudante · Atividade X**, com tarefa explícita. Após cada atividade, retornar ao Mestre para discutir saída, trecho responsável, erro comum e transição. As versões Mestre, Estudante e Professor devem compartilhar algoritmos, dados e numeração das atividades.

## 5. Prints estratégicos

As funções receberão `mostrar_passos=False`. Para recursão, registrar nível e limitar a impressão por profundidade. Tracing é usado apenas em entradas pequenas. Não imprimir toda a coleção em cada iteração.

| Algoritmo | Momento do print | Informação exibida | Pergunta |
|---|---|---|---|
| Insertion Sort | antes da inserção | i, atual e prefixo ordenado | Qual valor precisa encontrar posição? |
| Insertion Sort | após deslocamento | origem, destino e estado | O valor atual já foi inserido? |
| Insertion Sort | após inserção | posição final e lista | Qual propriedade foi restaurada? |
| Merge Sort | após divisão | nível, esquerda e direita | O que a divisão garante? |
| Intercalação | após escolha | origem do elemento e resultado parcial | Por que este elemento é o próximo? |
| Merge Sort | ao retornar | resultado intercalado | Como as soluções menores compõem a maior? |
| Quicksort | após particionamento | pivô, três grupos e tamanhos | Os subproblemas ficaram equilibrados? |
| Quicksort | ao combinar | resultado do nível | Onde ocorreu o trabalho de comparação? |
| Counting Sort | após contagem | tabela índice/frequência | O que significa o índice? |
| Counting Sort | durante reconstrução | valor, frequência e saída parcial | Estamos percorrendo n ou k? |
| Dados UCI | antes/depois | 8 registros com id, código e valor | As associações foram preservadas? |

Em um deslocamento do Insertion Sort pode haver duplicação temporária no array: o elemento salvo em `atual` ainda não voltou à posição final. Explicar esse estado; não descrevê-lo como perda de informação.

Na atividade real, os prints mostram um recorte de 8 registros, explicitamente identificado. Mostrar os primeiros 8 de uma lista maior não demonstra que toda ela está ordenada: complementar com verificações programáticas.

**Todos os prints permanecem desativados no benchmark.** A contagem instrumentada de operações ocorre em execução separada da medição de tempo.

## 6. Progressão e tempo

| Minutos | Bloco | Atividade e evidência |
|---|---|---|
| 0–10 | diagnóstico | A1: ordem de inserção, deslocamento e multiplicidade |
| 10–25 | Insertion Sort | A2: prever inserção, completar trecho e explicar prints |
| 25–55 | Merge Sort | A3: intercalar partes; acompanhar código e chamadas |
| 55–85 | Quicksort | A4: particionar, variar pivô e comparar tamanhos |
| 85–100 | Counting Sort | A5: contar, reconstruir e explicar n e k |
| 100–125 | experimento | A6: prever resultados, executar benchmark curto e interpretar |
| 125–155 | aplicação UCI | A7: obter dados, adaptar algoritmo para registros e verificar |
| 155–160 | síntese | A8: justificar estratégia, critério e limitação |

Os encontros são partes de uma sequência contínua. Um ponto possível de pausa é após o particionamento do Quicksort. Retomar a hipótese pendente no encontro seguinte. Se faltar tempo, reduzir configurações do benchmark e fornecer a função recursiva pronta; preservar a aplicação real e a síntese.

## 7. Orientações por bloco

### A1 — Diagnóstico

Perguntar se ordem de inserção de dict é ordem de valor, se uma posição encontrada em O(log n) elimina deslocamentos na lista e se valores iguais podem ser descartados. Pedir respostas individuais curtas. Corrigir apenas os pré-requisitos necessários ao próximo bloco.

### A2 — Inserção

Usar laço explícito, salvar `atual`, deslocar elementos maiores e inserir no ponto adequado. Pedir previsão antes da execução. Contrastar ordenado e invertido. Relacionar melhor caso linear e pior caso quadrático à implementação que encerra a procura assim que encontra a posição.

### A3 — Dividir e intercalar

Começar com duas listas já ordenadas. Construir a função de intercalação antes da recursão. Mostrar os dois índices, as escolhas e o tratamento dos elementos restantes. Usar <= para escolher da esquerda em empate e discutir estabilidade. Explicar caso-base e término da recursão. Relacionar trabalho linear por nível e quantidade logarítmica de níveis. A versão didática cria listas auxiliares e fatias; mencionar esse custo sem confundir com uma versão in-place.

### A4 — Pivô e partição

Versão didática com laço explícito e três grupos: menores, iguais e maiores. O grupo de iguais preserva repetidos e não volta à recursão. Escolher primeiro elemento como pivô para expor o caso adverso com valores distintos ordenados; comparar com pivô aleatório em experimento separado e com semente definida. Não equiparar primeiro elemento ou elemento central a pivô aleatório.

Contrastar Merge Sort: divide por posição e trabalha na intercalação; Quicksort divide por valor e trabalha no particionamento. Os grupos podem ter tamanhos muito diferentes. As listas auxiliares da versão didática precisam aparecer na discussão de memória. No benchmark, limitar o caso adverso para evitar profundidade recursiva excessiva; não aumentar o limite de recursão como solução pedagógica.

### A5 — Contagem

Usar apenas inteiros não negativos. Mostrar tabela de tamanho k = maior_valor + 1. Distinguir custo de ler n elementos, inicializar/percorrer k posições e escrever n elementos. A versão que reconstrói números não é suficiente para ordenar registros mantendo atributos associados: essa extensão exigiria outro tratamento. Comparar domínio pequeno e esparso. Retomar hash como contraste, sem afirmar que posições hash têm ordem numérica.

### A6 — Benchmark

Não tratar sorted como implementação equivalente aos códigos didáticos: é ferramenta otimizada para referência prática. Comparar curvas e mecanismos sem atribuir toda diferença de tempo à complexidade. Para cada repetição, preparar cópia independente da mesma entrada fora do cronômetro; manter esse contrato em todos os algoritmos. Allocação interna própria do algoritmo faz parte da operação. Usar mediana e registrar repetições, seed, versão Python, n, domínio, organização e estratégia.

Validar resultado contra sorted antes das medições. Instrumentação e prints ficam fora do ensaio cronometrado. Entradas iniciais sugeridas: n = 100, 300, 600 para os algoritmos didáticos, ampliando só quando viável. Pivô aleatório pode receber tamanhos adicionais, sem forçar as mesmas escalas no caso adverso. Não inventar resultados nem apresentar CSV sintético como resultado UCI.

### A7 — Aplicação final com UCI

Problema: apresentar itens de vendas positivas por valor crescente, mantendo identificadores e país; depois ordenar por país e valor decrescente.

1. Obter o XLSX da fonte oficial; registrar fonte, leitura e filtros.
2. Criar registros com id_linha e valor_item; mostrar recorte inicial.
3. Adaptar Merge Sort e sua intercalação para receber `key`, comparando `key(registro)` e preservando o registro inteiro. O Professor contém solução completa; o Estudante completa as comparações centrais.
4. Ordenar os 200 registros por valor_item. Executar tracing apenas para 8 registros.
5. Conferir com `sorted(registros, key=lambda r: r['valor_item'])`.
6. Validar ordem de todas as chaves e preservação do multiconjunto de id_linha; verificar contagem total. Discutir estabilidade nos empates; se não houver empate no recorte, usar exemplo sintético identificado.
7. Usar ordenação nativa com chave `(Country, -valor_item)` para país crescente e valor decrescente; não usar reverse=True para inverter simultaneamente critérios de direções diferentes.
8. Explicar por que Counting Sort, na versão da aula, não atende diretamente a preços fracionários e registros associados.

Entregáveis na atividade: código da chave/intercalação, previsões, prints pequenos, verificações e justificativa de 4–6 linhas. Não exigir implementação completa de todos os algoritmos do zero.

### A8 — Fechamento

Pedir: qual estratégia usaria para registros reais, qual para inteiros em domínio pequeno e que evidência apoia a decisão? Recuperar equilíbrio de partições, domínio e preservação dos registros. Preparar a S09: intercalar listas ordenadas será retomado em integração; não confundir essa intercalação com join relacional.

## 8. Artefatos da produção

Todos usam o prefixo `EGC5310-EstruturasDados-S08-`:

- `01-Roteiro.md`: este documento.
- `01A-Sequencia-Didatica.md`: intervenções, respostas esperadas e transições detalhadas.
- `01B-Resumo-Professor.md`: leitura de cinco minutos.
- `99-Aula-Mestre.ipynb`: narrativa com códigos, prints e chamadas de atividades; apresentação derivada por Quarto.
- `04-Estudante.ipynb`: previsões, implementações curtas, interpretação e aplicação real; link Colab.
- `09-Professor.ipynb`: soluções na mesma ordem do Estudante.
- `05-Benchmark.py`, `05-Benchmark.csv`, `05-Benchmark.md`: execução, resultados reais do ensaio e interpretação.
- `06-Exercicios.md`, `07-Solucoes.md`, `08-Revisao.md`.

Produzir um artefato por vez. Não gerar PPTX adicional sem necessidade. Revisão pós-aula permanece para preenchimento: expectativas não são feedback observado.

## 9. Verificação antes da aula

Conferir funções em entradas vazias, unitárias, repetidas, ordenadas e invertidas; preservação de elementos; estabilidade onde reivindicada; ausência de prints em medição; limites do caso recursivo adverso; download e leitura do XLSX; filtros e identificadores; equivalência das implementações entre artefatos; renderização de código e saídas sem cortes; chamadas de atividades e links Colab; tempo de execução compatível com a aula.

Na revisão conceitual, verificar: O(n + k) com k definido; comportamento do Quicksort ligado à regra de pivô; memória vinculada à implementação apresentada; limites da contagem para registros; nenhuma afirmação de que hashing ordena; nenhuma inferência de aprendizagem a partir da atividade em casa sem feedback.

## 10. Referências

- Chen, D. (2015). Online Retail [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5BW33. Página consultada em 01/10/2026.
- Goodrich, M. T.; Tamassia, R.; Goldwasser, M. H. Data Structures and Algorithms in Python. Wiley, 2013.
- Cormen, T. H. et al. Introduction to Algorithms. 4. ed. MIT Press, 2022.
- Plano de Ensino EGC5310 — 2026/2 e Guia de Desenvolvimento das Próximas Semanas da disciplina.
