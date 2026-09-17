# EGC5310 — Semana 05 — Resumo do Professor

## Hashing, conjuntos, dicionários e estruturas associativas

**Leia 5 minutos antes da aula.**

**Pergunta central:** **Como localizar uma matrícula rapidamente sem depender da posição do registro na coleção?**  
**Cenário:** Sistema Acadêmico  
**Carga útil:** aproximadamente 160 minutos

---

# 1. Ideia que deve permanecer ao final

> **A chave pode ser transformada em uma indicação de onde procurar, mas a posição calculada não elimina colisões nem a necessidade de confirmar a chave.**

Consequências:

- `dict` representa diretamente uma associação **chave → valor**;
- `set` representa **pertencimento e unicidade**;
- hashing oferece recuperação `O(1)` **em média/valor esperado**, sob condições adequadas;
- a estrutura deve ser escolhida pela operação predominante.

Não dizer que hashing é sempre `O(1)`.

---

# 2. De onde estamos vindo

Na S04, a turma aprendeu:

- busca sequencial: `O(n)`;
- busca binária: `O(log n)`;
- a busca binária exige dados ordenados pela mesma chave;
- ordenar e manter a ordem também custa.

Começar perguntando:

> **“Temos busca `O(log n)`. O problema está completamente resolvido?”**

Depois:

> **“Se a matrícula identifica exatamente um estudante, por que ainda precisamos percorrer ou dividir uma coleção?”**

Não repetir a aula de busca binária.

---

# 3. Regra pedagógica da semana

Usar continuamente:

> **pergunta → previsão → execução → falha/resultado → explicação → formalização**

Não apresentar `dict` no início. A turma precisa primeiro:

1. inventar uma localização;
2. construir uma tabela simples;
3. fazê-la falhar por colisão;
4. implementar o tratamento;
5. somente então reconhecer a abstração oferecida por `dict`.

Nas atividades, parar a exposição e mudar explicitamente para o Notebook Estudante.

---

# 4. Sequência essencial

## 1. Limitação da S04 — 10 min

Mostrar que uma inserção pode exigir preservar a ordem:

```python
matriculas_ordenadas.append(121)
matriculas_ordenadas.sort()
```

Mensagem: busca binária é eficiente, mas a organização tem custo.

## 2. Inventar a localização — 15 min

Apresentar dez posições e:

```python
def hash_simples(matricula, tamanho=10):
    return matricula % tamanho
```

**Atividade 1:** prever as posições de 101, 114, 127 e 139 antes de executar.

Formalizar:

- matrícula = chave;
- `% 10` = função didática;
- resultado = posição possível.

## 3. Primeira tabela — 20 min

```python
tabela = [None] * 10

def inserir_sem_colisao(tabela, matricula, estudante):
    posicao = matricula % len(tabela)
    tabela[posicao] = (matricula, estudante)
```

Perguntar por que a matrícula precisa permanecer junto ao registro.

## 4. Produzir a colisão — 15 min

```text
102 % 10 = 2
172 % 10 = 2
```

**Atividade 2:** prever e executar as duas inserções.

O segundo registro sobrescreve o primeiro. O programa roda, mas a solução está incorreta.

Só depois nomear:

> **Colisão: chaves distintas mapeadas para a mesma posição.**

Frase-chave:

> **Colisão é esperada. O erro é não tratá-la.**

## 5. Encadeamento e implementação — 25 min

```python
tabela = [[] for _ in range(10)]
```

**Atividade 3:** completar inserção e busca.

Perguntas durante a circulação:

> “Qual linha calcula o bucket?”

> “Por que ainda comparamos matrículas?”

> “A busca percorre toda a tabela ou apenas o bucket?”

Ideia essencial:

> **O hash indica o bucket; a comparação confirma a chave.**

## 6. Da tabela didática ao `dict` — 20 min

```python
por_matricula = {}
for estudante in estudantes:
    por_matricula[estudante["matricula"]] = estudante
```

**Atividade 4:** construir o índice, consultar uma chave existente e uma ausente e prever a atualização de chave repetida.

Não dizer que o `dict` real é idêntico ao encadeamento construído. A implementação didática mostra o mecanismo; Python usa uma implementação otimizada.

## 7. Por que `set`? — 15 min

Novo requisito: detectar matrícula já processada.

Perguntar:

> **“Precisamos associar matrícula a registro ou apenas saber se ela já apareceu?”**

```python
processadas = set()
```

**Atividade 5:** produzir a lista de matrículas duplicadas.

Distinção:

- `dict`: chave → valor;
- `set`: pertencimento/unicidade;
- `list`: sequência, ordem e repetições.

## 8. Escolher a estrutura — 15 min

**Atividade 6:** escolher `list`, `dict` ou `set` para pequenos casos.

Não aceitar apenas “porque é mais rápido”. Exigir:

> **“Qual é a operação predominante?”**

## 9. Complexidade — 15 min

| Estratégia | Mecanismo | Busca típica |
|---|---|---:|
| sequencial | examinar sucessivamente | `O(n)` |
| binária | descartar metade ordenada | `O(log n)` |
| hashing | calcular posição e examinar bucket curto | `O(1)` médio/esperado |

**Atividade 7:** corrigir a frase que interpreta `O(1)` como uma instrução e ausência de colisões.

Mostrar o caso adverso:

```text
bucket 2 → 102 → 172 → 242 → 312 → ...
```

O cálculo da posição continua constante, mas percorrer o bucket pode aproximar-se de `O(n)`.

## 10. Benchmark e ponte — 10 min

O benchmark compara:

- chaves distribuídas;
- chaves concentradas no mesmo bucket;
- mesmo `n`, mesma capacidade e mesma taxa de carga.

Antes de executar, perguntar:

> “Quantos buckets ficarão ocupados?”

> “Qual será o maior bucket?”

> “Quantas comparações serão necessárias?”

Interpretar primeiro colisões, maior bucket e comparações; somente depois, tempo.

Não comparar ainda sequencial × binária × `dict`. Encerrar perguntando:

> **“Como desenhar uma comparação justa entre as três estratégias, incluindo o custo de preparação?”**

Essa é a abertura da S06.

---

# 5. Pontos que não podem desaparecer

Se faltar tempo, preservar:

1. chave ≠ posição;
2. colisão descoberta pela sobrescrita;
3. implementação guiada de inserção e busca;
4. `dict` depois do mecanismo;
5. `set` surgindo da necessidade de pertencimento;
6. `O(1)` sempre acompanhado de médio/esperado;
7. pergunta experimental para a S06.

Reduzir primeiro:

- VisuAlgo;
- número de cenários da escolha de estruturas;
- quantidade de tamanhos executados no benchmark;
- desafio de atualização da inserção.

---

# 6. Erros conceituais a observar

- confundir matrícula com índice;
- achar que `% 10` transforma permanentemente a chave;
- acreditar que chaves diferentes não podem produzir a mesma posição;
- considerar correto qualquer programa que execute sem erro;
- percorrer a tabela inteira depois de calcular o bucket;
- afirmar que `dict` ordena pelas chaves;
- definir `set` apenas como “lista sem repetição”;
- concluir que `dict` substitui qualquer lista;
- interpretar `O(1)` como tempo zero ou uma instrução;
- generalizar a implementação didática como descrição exata do CPython.

---

# 7. Operação dos materiais

- Mestre: `EGC5310-EstruturasDados-S05-99-Aula-Mestre.ipynb`.
- Estudante: `EGC5310-EstruturasDados-S05-04-Estudante.ipynb`.
- Benchmark: `EGC5310-EstruturasDados-S05-05-Benchmark.py`.
- O link do Colab está no segundo slide e nas chamadas das atividades.
- O VisuAlgo é opcional e só deve aparecer depois do encadeamento.
- Se o primeiro encontro terminar após a colisão, retomar com:

> **“A chave indicou onde procurar, mas duas chaves chegaram ao mesmo lugar. Como preservamos as duas?”**

---

# 8. Frases de apoio

> A chave pertence ao problema; a posição é calculada pela estrutura.

> A função hash indica onde começar a procurar.

> Colisão é esperada. O erro é não tratá-la.

> O hash indica o bucket; a comparação confirma a chave.

> `dict` expressa associação; `set` expressa pertencimento.

> `O(1)` descreve crescimento médio/esperado, não uma instrução literal.

> Uma estrutura é adequada para determinadas operações, não para todos os problemas.
