# EGC5310 — Semana 05 — Sequência Didática

## Hashing, conjuntos, dicionários e estruturas associativas

**Disciplina:** EGC5310 — Tópicos Especiais em Ciência de Dados VI  
**Semana:** S05 — 10 e 11 de setembro de 2026  
**Artefato:** 01A — Sequência Didática  
**Cenário longitudinal:** Sistema Acadêmico  
**Tempo didático de referência:** aproximadamente 160 minutos úteis  
**Fonte principal:** `EGC5310-EstruturasDados-S05-99-Aula-Mestre.ipynb`  
**Material de participação:** `EGC5310-EstruturasDados-S05-04-Estudante.ipynb`  
**Experimento:** `EGC5310-EstruturasDados-S05-05-Benchmark.py`

---

# 1. Finalidade deste documento

Este documento descreve **como conduzir a Semana 05 em sala**, movimento a movimento.

Ele complementa o Roteiro e deve permitir que o professor recupere, mesmo depois de um longo intervalo:

- a história que precisa ser construída;
- a razão pedagógica da ordem adotada;
- as perguntas que precedem cada formalização;
- os exemplos de código que devem permanecer visíveis;
- os momentos de mudança para o Notebook Estudante;
- as respostas esperadas e os erros produtivos;
- o papel restrito do benchmark da semana;
- a pergunta que deve permanecer aberta para a Semana 06.

A sequência não depende rigidamente da numeração dos slides. O Notebook Mestre poderá evoluir sem alterar a lógica pedagógica registrada aqui.

---

# 2. Ideia central da semana

A Semana 04 mostrou que uma coleção ordenada permite eliminar metade das possibilidades e realizar busca binária em `O(log n)`. Entretanto, essa solução cobra o custo de ordenar e manter a ordenação.

A Semana 05 começa com essa limitação e formula uma nova pergunta:

> **Como localizar uma matrícula rapidamente sem depender da posição do registro na coleção?**

A ideia que deve emergir é:

> **A própria chave pode ser transformada em uma indicação de onde procurar.**

Essa ideia não resolve tudo. Quando duas chaves indicam a mesma posição, surge uma colisão. Assim, a narrativa precisa passar por quatro descobertas:

1. a chave pode orientar a localização;
2. a localização calculada é apenas uma posição possível;
3. colisões exigem tratamento;
4. `dict` e `set` representam necessidades associativas diferentes.

A formalização final deve ser cuidadosa:

> **Hashing oferece recuperação próxima de `O(1)` em média/valor esperado, quando a distribuição e o gerenciamento da tabela são adequados.**

Não usar “hashing é sempre `O(1)`”.

---

# 3. Preparação antes da aula

## 3.1 Verificações técnicas

Antes da aula:

- abrir o HTML gerado pelo Notebook Mestre;
- confirmar a presença da logo na capa;
- testar o link do Colab no segundo slide;
- abrir o Notebook Estudante no Colab;
- verificar que as Atividades 1 a 7 possuem a mesma numeração no Mestre e no Estudante;
- executar as células completas do Notebook Mestre;
- manter uma versão local do Notebook Estudante;
- executar o benchmark uma vez e verificar o CSV;
- confirmar que o VisuAlgo é apenas complementar e que a aula funciona sem internet;
- deixar uma aba com a apresentação, outra com o Notebook Estudante e um terminal preparado para o benchmark.

## 3.2 Verificações didáticas

Antes da aula, lembrar:

- não começar por definições de tabela hash, `dict` ou `set`;
- não repetir a aula de busca binária;
- não apresentar `dict` antes de produzir uma colisão na tabela didática;
- não tratar colisão como acidente raro ou erro de Python;
- não apresentar o código completo antes da implementação guiada;
- não confundir posição calculada com identificação do estudante;
- não converter a aula em detalhes internos do CPython;
- não transformar o benchmark da S05 na comparação sistemática prevista para a S06.

---

# 4. Regra operacional das atividades

Sempre que chegar a uma atividade, seguir o ciclo:

> **PERGUNTA → PREVISÃO → CHAMADA VISUAL → NOTEBOOK ESTUDANTE → TEMPO DE TRABALHO → DISCUSSÃO → RETORNO À APRESENTAÇÃO**

A apresentação possui chamadas explícitas:

> **ATIVIDADE N → Abra o Notebook Estudante**

Ao chegar a uma chamada:

1. interromper a exposição;
2. indicar a atividade e o resultado esperado;
3. pedir que a previsão seja registrada antes da execução;
4. conceder tempo real de trabalho;
5. circular pela sala com perguntas, sem entregar imediatamente o código;
6. selecionar duas ou três respostas para discussão;
7. anunciar verbalmente o retorno à apresentação.

Se os estudantes estiverem em duplas, pedir que um digite e o outro explique o significado de cada decisão. Alternar os papéis nas atividades seguintes.

---

# 5. Movimento 1 — Recuperar a limitação da busca binária

**Tempo de referência:** 0–10 min

## Apresentar

Retomar uma lista ordenada por matrícula:

```python
matriculas_ordenadas = [102, 118, 135, 149, 163]
matriculas_ordenadas.append(121)
matriculas_ordenadas.sort()
```

## Perguntar

> “Na Semana 04, o que tornou possível descartar metade dos dados?”

Resposta esperada:

- a ordenação pela mesma chave pesquisada.

Em seguida:

> “Temos busca `O(log n)`. O problema está completamente resolvido?”

Ideias esperadas:

- inserir pode exigir preservar ou restaurar a ordem;
- ordenar tem custo;
- posições podem mudar;
- muitas atualizações alteram o equilíbrio entre preparação e consulta.

## Objetivo

Usar a S04 como ponto de partida, não como conteúdo a ser repetido. A turma precisa perceber que busca binária é boa, mas não elimina o custo de organização.

## Transição

Mostrar os registros acadêmicos e perguntar:

> **“Se a matrícula identifica exatamente um estudante, por que precisamos percorrer ou dividir uma coleção para encontrá-lo?”**

Não responder. Avançar para a invenção da função de localização.

---

# 6. Movimento 2 — Inventar uma função de localização

**Tempo de referência:** 10–25 min

## Apresentar

Desenhar dez posições no quadro:

```text
posição     0  1  2  3  4  5  6  7  8  9
conteúdo    ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
```

Propor:

```python
def hash_simples(matricula, tamanho=10):
    return matricula % tamanho
```

Se `%` causar dúvida, explicar pela divisão:

```text
127 = 12 × 10 + 7
127 % 10 = 7
```

## Perguntar

> “Onde ficariam as matrículas 101, 114, 127 e 139?”

> “A matrícula 127 virou 7?”

Resposta esperada para a segunda pergunta:

- não; 127 continua sendo a chave;
- 7 é uma posição produzida pela função.

## ATIVIDADE 1 — Prever posições

### Chamada

> **Abra o Notebook Estudante → Atividade 1. Não execute antes de preencher a previsão.**

### Produção esperada

| matrícula | posição |
|---:|---:|
| 101 | 1 |
| 114 | 4 |
| 127 | 7 |
| 139 | 9 |

### Perguntas durante a atividade

> “O que permanece como identificação do estudante?”

> “O que mudaria se a tabela tivesse sete posições?”

> “A função devolve uma posição válida para qualquer matrícula?”

## Formalizar depois da atividade

- **chave:** dado do domínio usado para identificar ou acessar;
- **função hash:** transformação da chave;
- **posição:** localização possível dentro da tabela.

Não discutir ainda qualidade de funções hash em profundidade.

---

# 7. Movimento 3 — Construir a primeira tabela didática

**Tempo de referência:** 25–45 min

## Apresentar código visível

```python
tabela = [None] * 10

def inserir_sem_colisao(tabela, matricula, estudante):
    posicao = matricula % len(tabela)
    tabela[posicao] = (matricula, estudante)
```

Depois:

```python
def buscar_sem_colisao(tabela, matricula):
    posicao = matricula % len(tabela)
    item = tabela[posicao]
    if item is not None and item[0] == matricula:
        return item[1]
    return None
```

## Construir a leitura do código

Perguntar linha a linha:

> “Qual informação entra na função?”

> “Qual linha decide onde procurar?”

> “Por que guardamos `(matricula, estudante)` e não apenas o estudante?”

Resposta esperada:

- precisamos confirmar a chave, pois a posição é apenas candidata.

## Observar

Os estudantes conseguem distinguir:

- `matricula`, valor do problema;
- `posicao`, resultado calculado;
- `tabela[posicao]`, acesso à estrutura?

Se houver confusão, repetir com uma matrícula e uma tabela menor no quadro.

## Pergunta de suspensão

> “Agora resolvemos definitivamente o problema?”

Não confirmar. Avançar para as chaves 102 e 172.

---

# 8. Movimento 4 — Produzir a colisão como falha concreta

**Tempo de referência:** 45–60 min

## Apresentar sem nomear

```text
102 % 10 = 2
172 % 10 = 2
```

Perguntar:

> “O que acontecerá se inserirmos Ana com a matrícula 102 e Bruno com a matrícula 172?”

## ATIVIDADE 2 — Provocar uma colisão

### Chamada

> **Abra o Notebook Estudante → Atividade 2. Registre a previsão antes de executar.**

### Produção esperada

Os estudantes devem prever e observar que:

- as duas chaves indicam a posição 2;
- a segunda atribuição sobrescreve a primeira;
- o programa executa sem lançar exceção;
- a estrutura fica logicamente incorreta;
- buscar 102 retorna `None`.

### Discussão

Perguntar:

> “O programa rodou. Isso significa que a solução está correta?”

> “Qual requisito foi violado?”

> “O que podemos guardar na posição 2 para preservar os dois registros?”

## Formalizar

Somente depois da falha, apresentar:

> **Colisão ocorre quando chaves distintas são mapeadas para a mesma posição.**

Frase importante:

> **Colisão é esperada. O erro é não tratá-la.**

## Propostas que podem surgir

- procurar outra posição;
- aumentar a tabela;
- guardar uma lista em cada posição;
- rejeitar a segunda chave.

Não descartar propostas imediatamente. Explicar que existem estratégias diferentes, mas a semana utilizará encadeamento por ser visual e didaticamente simples.

---

# 9. Movimento 5 — Implementação guiada com encadeamento

**Tempo de referência:** 60–85 min

## Apresentar a representação

```python
tabela = [[] for _ in range(10)]
```

Explicar que a expressão cria dez listas internas independentes. Mostrar brevemente por que não usar:

```python
tabela = [[]] * 10
```

Não aprofundar o modelo de referências se isso desviar a aula; basta dizer que essa segunda forma reutiliza a mesma lista.

## ATIVIDADE 3 — Implementar inserção e busca

### Chamada

> **Abra o Notebook Estudante → Atividade 3. Complete primeiro a versão essencial.**

### Estrutura a completar

```python
def inserir(tabela, matricula, estudante):
    posicao = matricula % len(tabela)
    tabela[posicao].append((matricula, estudante))
```

```python
def buscar(tabela, matricula):
    posicao = matricula % len(tabela)
    for chave, estudante in tabela[posicao]:
        if chave == matricula:
            return estudante
    return None
```

### Perguntas durante a circulação

> “Em qual bucket o laço começa?”

> “A função percorre a tabela inteira?”

> “Por que ainda comparamos a matrícula?”

> “O que deve retornar quando não encontra?”

> “O teste verifica apenas que o código executa ou também verifica o resultado?”

### Testes esperados

- dois registros permanecem no bucket 2;
- 102 e 172 podem ser recuperados;
- uma matrícula ausente retorna `None`.

## Desafio guiado: atualização

Depois da versão essencial, pedir que a inserção substitua o registro quando a mesma matrícula reaparecer:

```python
for indice, (chave, _) in enumerate(bucket):
    if chave == matricula:
        bucket[indice] = (matricula, estudante)
        return
```

Alertar: sem o `return`, a função atualiza e depois também acrescenta uma cópia.

## Evidência de compreensão

O estudante deve ser capaz de dizer:

> “O hash indica o bucket; a comparação dentro do bucket confirma a chave.”

---

# 10. Possível fronteira entre os encontros

Se for necessário encerrar o primeiro encontro, o melhor ponto é depois de produzir a colisão ou durante a implementação guiada.

## Encerramento possível

> “A chave nos levou rapidamente a uma posição, mas duas chaves chegaram ao mesmo lugar. Amanhã precisamos concluir uma estrutura que preserve e recupere todos os registros.”

## Retomada possível

Reapresentar em dois minutos:

```text
102 → bucket 2
172 → bucket 2
```

Perguntar:

> “Qual informação o hash forneceu e qual trabalho ainda permaneceu?”

Continuar a implementação. Não refazer todos os movimentos anteriores.

---

# 11. Movimento 6 — Da tabela didática ao `dict`

**Tempo de referência:** 85–105 min

## Transição conceitual

Escrever:

```text
matrícula → registro do estudante
```

Perguntar:

> “Qual relação o nosso problema precisa representar diretamente?”

Depois apresentar:

```python
por_matricula = {}

for estudante in estudantes:
    por_matricula[estudante["matricula"]] = estudante
```

## ATIVIDADE 4 — Construir e consultar um `dict`

### Chamada

> **Abra o Notebook Estudante → Atividade 4. Construa o índice sem compreensão de dicionário.**

### Produção esperada

- construir `por_matricula`;
- consultar uma matrícula existente;
- consultar uma matrícula ausente com `.get()`;
- prever o efeito de atribuir um novo valor à mesma chave.

## Perguntar

> “Que operação do problema esta representação expressa diretamente?”

> “`por_matricula[matricula]` usa a matrícula como posição da lista?”

> “O que acontece se uma matrícula já existente for cadastrada novamente?”

## Formalizar com limites

- `dict` associa chave a valor;
- cada chave possui uma associação vigente;
- `.get(chave)` permite consulta segura quando a ausência é possível;
- a construção a partir da lista percorre `n` registros;
- buscas repetidas podem compensar esse custo de preparação;
- a implementação real de Python é otimizada e não é idêntica ao encadeamento didático;
- preservação da ordem de inserção não significa ordenação pelas chaves.

## VisuAlgo opcional

Somente agora, se houver conexão e utilidade, abrir o módulo de Hash Table do VisuAlgo no modo *Separate Chaining*.

Inserir `12`, `22` e `32`, observar o mesmo bucket e buscar `22`. Limitar a demonstração a poucos minutos.

---

# 12. Movimento 7 — Fazer surgir a necessidade de `set`

**Tempo de referência:** 105–120 min

## Apresentar o novo requisito

> “Arquivos de fontes diferentes podem trazer a mesma matrícula. Precisamos saber se ela já apareceu.”

Perguntar:

> **“Precisamos de matrícula → estudante ou apenas saber se a matrícula pertence ao conjunto das processadas?”**

Comparar:

```python
processadas = []
```

com:

```python
processadas = set()
```

## ATIVIDADE 5 — Detectar duplicatas com `set`

### Chamada

> **Abra o Notebook Estudante → Atividade 5. Explique primeiro por que basta pertencimento.**

### Código esperado

```python
processadas = set()
duplicadas = []

for matricula in matriculas_recebidas:
    if matricula in processadas:
        duplicadas.append(matricula)
    else:
        processadas.add(matricula)
```

### Resultado esperado

```python
[102, 118]
```

## Formalizar

- `dict`: chave → valor;
- `set`: elementos únicos e pertencimento;
- `list`: sequência, repetições e ordem.

Não definir `set` apenas como “lista sem repetição”. Essa formulação esconde a operação predominante de pertencimento.

---

# 13. Movimento 8 — Escolher a estrutura pela operação

**Tempo de referência:** 120–135 min

## ATIVIDADE 6 — Escolher e justificar

Apresentar os casos um de cada vez:

1. guardar estudantes na ordem de chegada;
2. localizar estudante pela matrícula;
3. impedir matrícula duplicada;
4. percorrer todos na ordem recebida;
5. associar código de disciplina a informações.

### Chamada

> **Abra o Notebook Estudante → Atividade 6. Toda escolha precisa citar a operação predominante.**

### Respostas de referência

| Caso | Estrutura principal | Justificativa |
|---|---|---|
| ordem de chegada | `list` | sequência e repetições |
| matrícula → registro | `dict` | associação por chave |
| impedir repetição | `set` | pertencimento/unicidade |
| percurso na ordem recebida | `list` | preservação da sequência |
| disciplina → informações | `dict` | associação por código |

## Discussão

Aceitar alternativas quando o estudante explicitar requisitos adicionais. Não aceitar apenas “é mais rápido”.

Pergunta útil:

> “Que mudança no requisito faria você escolher outra estrutura?”

Conclusão:

> **A estrutura adequada é aquela que representa diretamente as operações e restrições mais importantes do problema.**

---

# 14. Movimento 9 — Formalizar a complexidade

**Tempo de referência:** 135–150 min

## Consolidar os mecanismos

| Estratégia | Mecanismo | Busca típica |
|---|---|---:|
| lista sem índice | examinar sucessivamente | `O(n)` |
| lista ordenada + busca binária | descartar metade | `O(log n)` |
| tabela hash adequada | calcular posição e examinar bucket curto | `O(1)` médio/esperado |

## Perguntar

> “`O(1)` significa uma instrução?”

> “Significa tempo zero?”

> “Significa que não existem colisões?”

> “O cálculo da posição elimina qualquer comparação?”

## ATIVIDADE 7 — Interpretar `O(1)`

### Chamada

> **Abra o Notebook Estudante → Atividade 7. Corrija a afirmação usando ‘médio/esperado’ e ‘crescimento’.**

Afirmação a corrigir:

> “`O(1)` significa que o `dict` sempre encontra o valor com uma única instrução e nunca tem colisões.”

### Resposta esperada

> Em condições adequadas, a busca possui custo médio/esperado cujo crescimento dominante não acompanha proporcionalmente o aumento de `n`. Isso não significa uma única instrução, tempo zero ou ausência de colisões.

## Caso adverso

Desenhar:

```text
bucket 2 → 102 → 172 → 242 → 312 → ...
```

Explicar que calcular o bucket ainda é constante, mas percorrer um bucket de tamanho `n` pode produzir comportamento `O(n)`.

---

# 15. Movimento 10 — Benchmark de colisões e ponte para a S06

**Tempo de referência:** 150–160 min, ajustável

O benchmark da S05 compara duas tabelas didáticas com:

- o mesmo número de chaves;
- a mesma quantidade de buckets;
- taxa de carga igual a 1;
- distribuições radicalmente diferentes.

## Antes de executar

Apresentar os cenários:

- `distribuidas`: chaves `0, 1, ..., n-1`;
- `concentradas`: chaves `indice * n + 2`.

Perguntar:

> “Quantos buckets ficarão ocupados?”

> “Qual será o maior bucket?”

> “Quantas comparações exigirá a busca pelo último elemento?”

## Executar

```bash
python EGC5310-EstruturasDados-S05-05-Benchmark.py
```

Se o tempo for curto, utilizar apenas `n = 100` e `n = 100.000` ou abrir o CSV previamente gerado.

## Interpretar

Priorizar:

1. buckets ocupados;
2. maior bucket;
3. colisões;
4. comparações;
5. somente depois, tempo.

Conclusão esperada:

> **O hash pode calcular uma posição em tempo constante, mas uma distribuição ruim aumenta o trabalho dentro do bucket.**

## Ponte para a S06

Recuperar:

```python
buscar_lista(...)
buscar_binaria(...)
por_matricula.get(...)
```

Perguntar:

> **“Qual estratégia é mais rápida na prática e como podemos compará-las de maneira justa?”**

Registrar os controles sugeridos:

- tamanho dos dados;
- chaves existentes e ausentes;
- posição do alvo na lista;
- custo de ordenar;
- custo de construir o `dict`;
- número de consultas;
- repetições;
- comparações e tempo.

Não responder à pergunta. Ela deve abrir a Semana 06.

---

# 16. Correspondência das atividades

| Atividade | Mestre | Estudante | Evidência esperada |
|---:|---|---|---|
| 1 | prever posições | tabela de previsões | distingue chave e posição |
| 2 | provocar colisão | previsão, execução e explicação | reconhece corrupção lógica |
| 3 | implementar encadeamento | inserção, busca e testes | compreende bucket e confirmação da chave |
| 4 | construir `dict` | índice e consultas | reconhece chave → valor |
| 5 | usar `set` | duplicatas | reconhece pertencimento/unicidade |
| 6 | escolher estrutura | tabela justificada | decide pela operação predominante |
| 7 | interpretar `O(1)` | correção escrita | distingue crescimento e tempo literal |

---

# 17. Erros conceituais e intervenções

## Chave é confundida com posição

Intervenção:

> “A matrícula muda quando mudamos o tamanho da tabela? E a posição calculada?”

## Colisão é tratada como erro excepcional

Intervenção:

> “O código lançou exceção ou perdeu informação silenciosamente?”

## O estudante remove uma chave colidente

Intervenção:

> “As matrículas são diferentes e válidas. Qual requisito autoriza descartar uma delas?”

## Busca percorre toda a tabela

Intervenção:

> “Que informação o hash nos forneceu? Podemos começar diretamente pelo bucket indicado?”

## `dict` é descrito como lista mais rápida

Intervenção:

> “Qual associação esta estrutura expressa que uma sequência não expressa diretamente?”

## `set` é descrito somente como remoção de duplicatas

Intervenção:

> “Qual pergunta fazemos repetidamente: qual é o valor associado ou este elemento já pertence?”

## `O(1)` é interpretado como um passo

Intervenção:

> “Big-O informa o número exato de instruções ou como o trabalho cresce quando `n` cresce?”

---

# 18. Ajustes conforme o tempo

## Se faltar tempo

Preservar obrigatoriamente:

1. distinção entre chave e posição;
2. colisão produzida concretamente;
3. implementação guiada de inserção e busca;
4. transição para `dict`;
5. distinção entre `dict` e `set`;
6. interpretação cuidadosa de `O(1)`;
7. pergunta de ponte para a S06.

Reduzir, nesta ordem:

1. demonstração do VisuAlgo;
2. quantidade de casos da Atividade 6;
3. tamanhos executados no benchmark;
4. desafio de atualização da Atividade 3.

## Se sobrar tempo

- comparar `[[] for _ in range(10)]` e `[[]] * 10`;
- testar outra capacidade para a tabela didática;
- discutir o efeito de uma chave duplicada no `dict`;
- pedir aos grupos que proponham uma distribuição menos extrema para o benchmark;
- formular ameaças à validade para o experimento da S06.

---

# 19. Evidências a registrar depois da aula

No arquivo de Revisão, registrar:

- se a colisão produziu surpresa e discussão;
- se os estudantes diferenciaram chave e posição;
- onde houve maior dificuldade na implementação guiada;
- se `dict` apareceu como consequência do problema ou como sintaxe isolada;
- se a necessidade de `set` ficou clara;
- se as justificativas da Atividade 6 citaram operações;
- se “`O(1)` médio/esperado” foi compreendido;
- se o benchmark ajudou ou consumiu tempo excessivo;
- quais hipóteses concretas ficaram para a S06;
- o ponto real de término e retomada entre os encontros.

