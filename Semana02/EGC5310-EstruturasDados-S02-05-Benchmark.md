# EGC5310 — Semana 02 — Benchmark

## Representação de dados e trabalho observado

**Disciplina:** EGC5310 — Tópicos Especiais em Ciência de Dados VI  
**Semana:** S02 — 20 e 21 de agosto de 2026  
**Artefato:** 05 — Benchmark  
**Arquivos associados:**

- `EGC5310-EstruturasDados-S02-05-Benchmark.py`
- `EGC5310-EstruturasDados-S02-05-Benchmark.csv`

---

# 1. Finalidade

Este benchmark é um **material de apoio ao professor**.

Ele não transforma a Semana 02 em uma aula formal de análise de desempenho.

A função pedagógica é tornar observável a ideia construída em aula:

> **representações diferentes podem alterar o trabalho necessário para realizar uma operação.**

O foco da S02 continua sendo qualitativo:

- problema;
- dados;
- operações;
- representação;
- trabalho esperado;
- volume;
- restrições.

A análise sistemática de custos será aprofundada na Semana 03.

---

# 2. O que é comparado

O benchmark trabalha com duas operações.

## Operação A — localizar estudante pela matrícula

São comparadas três representações/estratégias:

1. **lista + busca sequencial**;
2. **dicionário indexado pela matrícula**;
3. **lista ordenada + `bisect`**.

A pergunta é:

> **Quando a operação é localizar pela matrícula, a forma de organização dos dados altera o comportamento observado?**

## Operação B — listar estudantes por curso

São comparadas:

1. lista;
2. dicionário indexado pela matrícula.

Neste caso, nenhuma das duas representações possui uma organização específica por curso.

A pergunta é:

> **Uma representação que favorece consulta por matrícula também favorece automaticamente consulta por curso?**

---

# 3. Volumes utilizados

O script gera coleções com:

- 100 registros;
- 1.000 registros;
- 10.000 registros;
- 100.000 registros.

Isso permite observar o efeito do aumento de volume sem ainda introduzir uma formalização completa.

---

# 4. Como executar

No terminal:

```bash
python EGC5310-EstruturasDados-S02-05-Benchmark.py
```

O script cria:

```text
EGC5310-EstruturasDados-S02-05-Benchmark.csv
```

Os tempos são obtidos com `time.perf_counter_ns()`.

Para reduzir flutuações:

- cada cenário é executado diversas vezes;
- é utilizada a mediana;
- as buscas por matrícula utilizam vários alvos existentes em posições diferentes.

---

# 5. Como ler o CSV

As colunas são:

## `n`

Número de estudantes.

## `operacao`

Operação realizada:

- `buscar_matricula`;
- `listar_por_curso`.

## `representacao`

Estratégia utilizada.

## `tempo_mediano_ns_por_lote`

Tempo mediano do lote medido.

## `operacoes_por_lote`

Quantidade de operações realizadas em cada lote.

Para busca por matrícula são feitas várias consultas por lote, porque uma única consulta pode ser rápida demais para produzir uma medição estável.

## `tempo_aprox_ns_por_operacao`

Estimativa do tempo por operação individual.

---

# 6. Interpretação esperada — busca por matrícula

A tendência esperada é:

## Lista + busca sequencial

O tempo tende a aumentar de maneira bastante perceptível conforme `n` cresce.

Isso é coerente com o código:

```python
for estudante in lista:
    if estudante["matricula"] == alvo:
        ...
```

O programa pode precisar examinar vários elementos.

## Dicionário por chave

O crescimento observado tende a ser muito menor para consultas pela matrícula:

```python
dicionario.get(alvo)
```

Isso não significa que o trabalho desapareceu.

Significa que a estrutura foi organizada para oferecer uma operação de acesso por chave.

## Lista ordenada + `bisect`

A organização prévia dos dados permite uma estratégia de busca que não precisa percorrer sequencialmente toda a coleção.

Na S02, a interpretação deve permanecer qualitativa.

Não é necessário transformar os resultados em uma aula formal de classes de complexidade.

---

# 7. Interpretação esperada — listar por curso

Ao executar:

```python
for estudante in lista:
    if estudante["curso"] == "CD":
        ...
```

ou:

```python
for matricula, estudante in dicionario.items():
    if estudante["curso"] == "CD":
        ...
```

a operação continua examinando os registros.

Assim, o fato de o dicionário ser conveniente para matrícula **não elimina o percurso quando o atributo pesquisado é outro**.

Este é um dos resultados pedagogicamente mais importantes da semana:

> **“mais rápido” precisa sempre ser acompanhado de “para qual operação?”**

---

# 8. O que não concluir

Não utilizar este benchmark para afirmar isoladamente:

> “dicionário é sempre melhor que lista”.

Também não concluir:

> “`bisect` é sempre melhor”.

As medições dependem:

- da operação;
- da representação;
- do volume;
- da implementação;
- do ambiente;
- do hardware;
- da versão do Python;
- de custos de construção e manutenção que não estão todos medidos aqui.

---

# 9. Limitações do experimento

Este benchmark não mede:

- memória;
- custo de construção de todas as estruturas;
- custo de manter uma lista ordenada após inserções;
- custo de manter índices adicionais;
- árvores explicitamente;
- concorrência;
- cache;
- persistência em disco;
- banco de dados.

Ele foi deliberadamente mantido pequeno porque sua função é **didática**, não de avaliação de desempenho de produção.

---

# 10. Uso sugerido em sala

O benchmark pode ser utilizado depois dos exemplos de código do Bloco 6.

Fluxo recomendado:

1. pedir uma previsão;
2. executar o script;
3. abrir o CSV;
4. observar tendências;
5. perguntar:
   > **“O resultado é igual para todas as operações?”**
6. evitar formalizar completamente o crescimento;
7. guardar a pergunta quantitativa para a Semana 03.

---

# 11. Perguntas para discussão

- Qual estratégia parece mais sensível ao aumento de `n`?
- O dicionário apresenta a mesma vantagem para busca por curso?
- Que propriedade dos dados o `bisect` aproveita?
- O benchmark mede o custo de manter os dados ordenados?
- O fato de uma operação aparecer em uma única linha de Python significa que seu custo é zero?
- Se consultas por curso fossem predominantes, deveríamos manter outra organização?

---

# 12. Ponte para a Semana 03

A Semana 02 termina dizendo:

> **“Esta operação parece exigir mais trabalho.”**

O benchmark permite acrescentar:

> **“Conseguimos observar essa diferença experimentalmente.”**

A Semana 03 deverá avançar para:

> **Como comparar e descrever sistematicamente o custo das operações quando o tamanho da entrada cresce?**
