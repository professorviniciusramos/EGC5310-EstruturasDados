# EGC5310 — Estruturas de Dados

## Semana 05 — Hashing, conjuntos, dicionários e estruturas associativas

**Disciplina:** EGC5310 — Tópicos Especiais em Ciência de Dados VI  
**Oferta:** 2026/2  
**Datas previstas:** 10 e 11 de setembro de 2026  
**Unidade:** II — Estratégias para recuperação eficiente de dados  
**Artefato:** roteiro autocontido para condução da semana  
**Versão:** 1.0  
**Status:** pronto para uso

## 1. Posição da semana na disciplina

A Semana 05 dá continuidade direta à discussão iniciada nas quatro semanas anteriores:

- S01: a busca sequencial tornou visível o custo `O(n)`;
- S02: a representação passou a ser escolhida a partir do problema e das operações;
- S03: inserção, remoção, busca e ordenação mostraram custos distintos;
- S04: a busca binária reduziu a recuperação para `O(log n)`, desde que os dados permaneçam ordenados pela chave;
- S05: a própria chave passa a orientar a localização, introduzindo hashing, colisões, `dict` e `set`;
- S06: as estratégias serão comparadas por experimento sistemático.

Não realizar benchmark formal nesta semana. A pergunta experimental deve permanecer aberta para a S06.

## 2. Problema orientador

O Sistema Acadêmico armazena registros identificados pela matrícula:

```python
estudantes = [
    {"matricula": 20260123, "nome": "Ana", "curso": "CD"},
    {"matricula": 20260481, "nome": "Bruno", "curso": "CC"},
]
```

O sistema precisa recuperar estudantes repetidamente, cadastrar novos registros e impedir matrículas duplicadas.

> **Como localizar uma matrícula rapidamente sem depender da posição do registro na coleção?**

A pergunta deve aparecer antes dos termos “hash”, “tabela hash”, `dict` e `set`.

## 3. Resultados de aprendizagem

Ao final da semana, espera-se que o estudante consiga:

1. distinguir chave de posição ou índice;
2. explicar por que a busca binária depende de ordenação e o hashing não utiliza esse mecanismo;
3. interpretar uma função hash como transformação de uma chave em uma posição possível;
4. calcular `chave % tamanho` e prever posições;
5. identificar e explicar colisões;
6. completar inserção e busca em uma tabela hash didática com encadeamento;
7. usar `dict` para associar matrícula a registro;
8. usar `set` para pertencimento e unicidade;
9. escolher entre `list`, `dict` e `set` pela operação predominante;
10. interpretar `O(n)`, `O(log n)` e `O(1)` médio sem tratar Big-O como tempo absoluto;
11. distinguir o modelo didático da implementação real do `dict` de Python.

## 4. Conhecimentos prévios e apoios

Conhecimentos mobilizados: listas, dicionários como registros, funções, laços `for`, condicionais, `len`, operador `%`, busca sequencial, busca binária e Big-O qualitativo.

Se necessário, explicar `%` com divisão inteira: `172 = 17 × 10 + 2`; portanto, `172 % 10 == 2`. Não pressupor compreensão de list comprehensions: ao usar `[[] for _ in range(10)]`, explicar que são criadas dez listas internas independentes. Alertar que `[[]] * 10` reutilizaria a mesma lista e seria inadequado.

## 5. Visão geral dos 160 minutos úteis

| Movimento | Tempo | Função pedagógica |
|---|---:|---|
| 1. Limitação herdada da S04 | 10 min | reabrir o problema sem repetir busca binária |
| 2. Inventar uma localização | 15 min | construir a ideia antes do vocabulário |
| 3. Primeira tabela didática | 20 min | tornar o mecanismo visível em código |
| 4. Provocar colisão | 15 min | produzir a necessidade de tratamento |
| 5. Implementação guiada | 25 min | completar inserção e busca |
| 6. Da implementação ao `dict` | 20 min | relacionar mecanismo e abstração nativa |
| 7. Por que existe `set`? | 15 min | distinguir associação de pertencimento |
| 8. Escolha da estrutura | 15 min | justificar pela operação predominante |
| 9. Complexidade | 15 min | formalizar depois do mecanismo |
| 10. Síntese e ponte | 10 min | preparar a pergunta experimental da S06 |

Os tempos são referências. A mudança entre encontros pode ocorrer após a colisão ou durante a implementação guiada, conforme o ritmo da turma.

## 6. Condução detalhada

### Movimento 1 — A solução da S04 ainda cobra um preço

Retome uma lista ordenada por matrícula. Pergunte: “Se a busca custa `O(log n)`, o problema está completamente resolvido?” Registre respostas antes de mostrar a inserção.

Código a discutir:

```python
matriculas_ordenadas = [102, 118, 135, 149, 163]
matriculas_ordenadas.append(121)
matriculas_ordenadas.sort()
```

Ideias esperadas: buscar ficou barato; manter a ordem tem custo; inserções frequentes podem exigir reorganização; a posição do estudante muda.

Pergunta de transição: “Se a matrícula já identifica exatamente um estudante, por que procurar por posições sucessivas?”

### Movimento 2 — Inventar uma função de localização

Desenhe dez posições, de 0 a 9, e proponha que a matrícula determine onde o registro pode ficar:

```python
def hash_simples(matricula, tamanho=10):
    return matricula % tamanho
```

Use as matrículas `101`, `114`, `127` e `139`. Antes de executar, peça os restos e as posições. Só depois nomeie: matrícula é a **chave**; a função de localização é uma **função hash**; a lista é a base da **tabela hash**.

**ATIVIDADE 1 — Prever posições.** Orientar a mudança ao Notebook Estudante. Não permitir execução antes do registro das previsões.

Erros previsíveis: confundir matrícula com índice; achar que `% 10` retorna o último algarismo por regra especial; concluir que qualquer função serve igualmente bem. Explique que o exemplo é deliberadamente simples e deve apenas distribuir chaves pelas posições válidas.

### Movimento 3 — Primeira tabela hash didática

Mostre uma implementação sem colisões:

```python
tabela_inicial = [None] * 10

def inserir_sem_colisao(tabela, matricula, estudante):
    posicao = matricula % len(tabela)
    tabela[posicao] = (matricula, estudante)

def buscar_sem_colisao(tabela, matricula):
    posicao = matricula % len(tabela)
    item = tabela[posicao]
    if item is not None and item[0] == matricula:
        return item[1]
    return None
```

Pergunte por que é necessário guardar a matrícula junto ao registro. Resposta esperada: a posição é apenas candidata; precisamos confirmar a chave procurada.

### Movimento 4 — Fazer a solução falhar antes de nomear a falha

Insira `102` e `172`. Ambas produzem posição 2. A segunda sobrescreve a primeira na implementação inicial.

Perguntas:

- O código executou sem erro? Sim.
- A estrutura permaneceu correta? Não.
- O que foi perdido? O registro associado a 102.
- Que soluções a turma propõe? Outra posição, uma coleção por posição, aumentar a tabela etc.

Somente então formalize **colisão**: duas chaves distintas mapeadas para a mesma posição. Reforce que colisão não é erro excepcional; toda implementação correta precisa tratá-la.

**ATIVIDADE 2 — Provocar e explicar a colisão.** Mudança para o Notebook Estudante.

### Movimento 5 — Encadeamento didático

Apresente buckets como listas independentes:

```python
def criar_tabela(tamanho=10):
    return [[] for _ in range(tamanho)]
```

Formato de cada item: `(matricula, estudante)`. Complete coletivamente:

```python
def inserir(tabela, matricula, estudante):
    posicao = matricula % len(tabela)
    for indice, (chave_existente, _) in enumerate(tabela[posicao]):
        if chave_existente == matricula:
            tabela[posicao][indice] = (matricula, estudante)
            return
    tabela[posicao].append((matricula, estudante))
```

```python
def buscar(tabela, matricula):
    posicao = matricula % len(tabela)
    for chave_existente, estudante in tabela[posicao]:
        if chave_existente == matricula:
            return estudante
    return None
```

**ATIVIDADE 3 — Implementar inserção e busca.** O Notebook Estudante oferece primeiro a versão essencial e depois um teste de atualização. Circular entre grupos e perguntar o significado de cada linha. Não fornecer a resposta completa imediatamente.

Ponto de formalização: hashing não eliminou comparações; restringiu-as ao bucket indicado. Muitas colisões aumentam o trabalho.

### Movimento 6 — Da implementação didática ao `dict`

Depois de os estudantes entenderem os buckets, mostre a abstração nativa:

```python
por_matricula = {}
for estudante in estudantes:
    por_matricula[estudante["matricula"]] = estudante

por_matricula[20260123]
```

Pergunte: “Que operação do problema esta representação expressa diretamente?” Resposta: associar uma chave única a um valor/registro.

**ATIVIDADE 4 — Construir e consultar um `dict`.** Pedir previsão sobre o que ocorre com chave duplicada: a associação anterior é substituída. Distinguir “impedir duplicatas” de “sobrescrever silenciosamente”.

Cuidados conceituais:

- `dict` não é a tabela didática escrita em Python linha por linha;
- Python implementa uma tabela hash otimizada, com detalhes internos diferentes;
- chaves precisam ser hashable; nesta semana, matrículas inteiras são adequadas;
- ordem de iteração preservada por Python moderno não significa ordenação pela chave;
- consulta, inserção e pertencimento têm custo médio/esperado próximo de `O(1)`, não garantia universal de uma instrução.

Como reforço opcional, após a implementação, abrir o módulo [Hash Table do VisuAlgo](https://visualgo.net/en/hashtable) no modo de separate chaining. Limitar a demonstração a inserir `12`, `22` e `32`, observar o mesmo bucket e realizar uma busca. Não depender do recurso.

### Movimento 7 — Por que existe `set`?

Novo requisito: arquivos de fontes diferentes podem repetir uma matrícula. Para detectar repetição, precisamos guardar todo o registro?

```python
processadas = set()
for matricula in [102, 118, 102, 131]:
    if matricula in processadas:
        print("duplicada:", matricula)
    else:
        processadas.add(matricula)
```

Formalize:

- `dict`: chave → valor;
- `set`: apenas pertencimento/unicidade de elementos;
- `list`: sequência, ordem e repetições.

**ATIVIDADE 5 — Detectar duplicatas com `set`.** Solicitar explicação em palavras antes do código.

### Movimento 8 — Escolher pela operação predominante

Apresente os casos um de cada vez e exija justificativa:

1. guardar estudantes na ordem de chegada → `list`;
2. localizar registro pela matrícula → `dict`;
3. saber se matrícula já foi processada → `set`;
4. percorrer todos na ordem recebida → `list`;
5. associar código de disciplina a dados → `dict`.

**ATIVIDADE 6 — Escolher e justificar.** Aceitar alternativas apenas quando a justificativa explicitar requisitos adicionais. Exemplo: um `dict` também pode ser percorrido, mas se a única necessidade for sequência de chegada e duplicatas forem legítimas, `list` comunica melhor o problema.

### Movimento 9 — Complexidade como interpretação

Consolidar:

| Estratégia | Mecanismo | Busca típica |
|---|---|---:|
| lista sem índice | examinar sucessivamente | `O(n)` |
| lista ordenada + binária | descartar metade | `O(log n)` |
| tabela hash adequada | calcular posição e examinar bucket curto | `O(1)` médio/esperado |

Não dizer “hashing é sempre `O(1)`”. Apresente o caso extremo: se todas as chaves caírem no mesmo bucket, a busca percorre esse bucket e pode aproximar-se de `O(n)`. Explique que distribuição, tamanho/capacidade, colisões e redimensionamentos influenciam o comportamento.

**ATIVIDADE 7 — Interpretar complexidade.** Pedir que os estudantes corrijam: “`O(1)` significa que a busca usa exatamente uma instrução e nunca há colisões.”

Resposta esperada: custo médio não cresce proporcionalmente a `n` sob condições adequadas; há um número constante de etapas dominantes em média, mas o tempo absoluto e o número exato de instruções variam.

### Movimento 10 — Fechamento e ponte para a S06

Recupere as três operações conceituais:

```python
buscar_lista(estudantes, matricula)
buscar_binaria(matriculas_ordenadas, matricula)
por_matricula.get(matricula)
```

Pergunte: “Qual é mais rápida na prática?” Não encerre com palpite. Liste o que um experimento justo deverá controlar: tamanho dos dados, chaves existentes/ausentes, custo de preparação, repetições e métrica. Esta é a ponte explícita para a S06.

## 7. Atividades Mestre ↔ Estudante

| Nº | Chamada no Mestre | Produção do estudante |
|---:|---|---|
| 1 | prever posições | tabela de restos e posições |
| 2 | provocar colisão | execução e explicação da perda |
| 3 | implementar encadeamento | funções `inserir` e `buscar` |
| 4 | construir `dict` | índice e consulta segura |
| 5 | usar `set` | detecção de repetidas |
| 6 | escolher estrutura | decisões justificadas |
| 7 | interpretar complexidade | correção de afirmação equivocada |

## 8. Concepções equivocadas a observar

- “Chave e índice são a mesma coisa.” A chave pertence ao domínio; o índice é uma posição calculada.
- “Duas chaves não podem ter o mesmo hash.” Podem; isso é colisão.
- “Colisão significa que o programa lança erro.” A versão ingênua pode executar e corromper logicamente os dados.
- “`dict` ordena pelas chaves.” Preservar ordem de inserção não equivale a ordenar.
- “`set` associa chave a registro.” `set` representa pertencimento; `dict` representa associação.
- “`O(1)` significa um passo ou tempo zero.” Big-O descreve crescimento assintótico, não cronômetro nem contagem literal.
- “A tabela didática é a implementação real do Python.” Ela é um modelo conceitual simplificado.

## 9. Observações práticas

- Manter o Notebook Mestre projetado e o Estudante aberto em outra aba.
- No segundo slide, testar o link do Colab antes da aula.
- Usar o quadro para as dez posições e apagar/sobrescrever 102 ao inserir 172; o erro visual ajuda a produzir a noção de colisão.
- Formar duplas na Atividade 3; pedir ao estudante que não digita que explique o código.
- Se faltar tempo, reduzir o VisuAlgo e um caso da Atividade 6. Não retirar colisão, implementação guiada, `dict`, `set` ou a interpretação de `O(1)`.
- Se sobrar tempo, discutir por que `[[]] * 10` cria buckets compartilhados, sem transformar isso em requisito de Python avançado.
- Encerrar registrando hipóteses para a S06, sem executar benchmark formal.

