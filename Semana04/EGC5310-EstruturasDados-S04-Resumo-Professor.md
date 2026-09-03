# EGC5310 — Estruturas de Dados

## Semana 04 — Resumo do professor para leitura em 5 minutos

**Tema:** busca sequencial × busca binária  
**Pergunta central:** **Quando vale a pena organizar os dados para buscar mais rapidamente?**  
**Cenário:** Sistema Acadêmico  
**Carga útil:** aproximadamente 160 minutos

---

## 1. Ideia que deve permanecer ao final

A busca binária não é apenas uma busca sequencial mais rápida. Ela consegue eliminar aproximadamente metade das possibilidades a cada comparação porque recebe uma informação estrutural adicional: **os dados estão ordenados pela mesma chave usada na busca**.

Portanto:

> **A eficiência está na relação entre algoritmo, organização dos dados e padrão de operações.**

Ordenar e manter a ordenação também custa. A busca binária tende a ser vantajosa quando o investimento em organização é compensado por muitas consultas.

---

## 2. Mudança pedagógica desta semana

As semanas anteriores ficaram excessivamente expositivas e pouco desafiadoras. Hoje, evitar explicar a solução antes de os estudantes investigarem.

Usar continuamente:

> **pergunta → previsão → visualização → atividade → código → resultado → formalização**

Nenhuma exposição contínua deve durar muito mais que 10–15 minutos. Antes de revelar cada novo estado da busca, perguntar:

> **Qual parte pode ser descartada e por quê?**

---

## 3. Sequência essencial

### 1. Problema e escala — 10 min

Começar com a coleção desordenada e perguntar onde está a matrícula `73`. Depois ampliar para um milhão de registros e cem mil consultas.

Não revisar longamente a busca sequencial. Ela é apenas a referência `O(n)`.

### 2. Jogo humano — 15 min

Um estudante escolhe um número entre 1 e 100. A turma recebe respostas “maior”, “menor” ou “igual”. Perguntar qual tentativa elimina mais possibilidades.

Só nomear **busca binária** depois que surgir a ideia de escolher o meio.

### 3. Visualização — 15 min

Mostrar `inicio`, `meio`, `fim`, valor examinado e região descartada. Insistir que o descarte só é seguro por causa da ordenação.

### 4. Notebook Estudante — Atividade 1 — 15 min

Usar a chamada explícita do slide e o botão do Colab. Os estudantes devem prever as posições examinadas e preencher `inicio`, `fim` e `meio` antes da execução.

### 5. Implementação — 15 min

Construir coletivamente:

```python
while inicio <= fim:
    meio = (inicio + fim) // 2
```

Perguntar qual limite muda em cada caso. Destacar `meio + 1` e `meio - 1` como garantia de progresso.

### 6. Pré-condição — 10 min

Executar em dados desordenados e mostrar que um elemento existente pode não ser encontrado. Pergunta principal:

> O código está errado ou sua pré-condição foi violada?

Ordenação por nome não autoriza busca binária por matrícula.

### 7. `O(log n)` — 10 min

Partir de:

```text
1.000.000 → 500.000 → 250.000 → ... → 1
```

Chegar intuitivamente a aproximadamente 20 comparações. Não exigir cálculo formal de logaritmo.

### 8. Previsão e benchmark — 30 min

Antes de medir, os estudantes preenchem a tabela para `100` até `1.000.000` registros.

No benchmark, separar:

- número de comparações;
- tempo medido.

Mensagem:

> **Big-O explica a tendência de crescimento; o cronômetro mede uma execução concreta.**

Ruído temporal não contradiz a análise. Para entradas pequenas, constantes podem dominar.

### 9. Então devemos ordenar tudo? — 15 min

Não. Comparar:

- muitas inserções e poucas consultas;
- carga única e milhões de consultas;
- inserções e consultas contínuas.

Pedir justificativas usando frequência das operações e custo de organização.

### 10. Fechamento — 5 min

Pergunta de saída no Notebook Estudante:

> **Por que a busca binária não é apenas uma busca sequencial mais rápida?**

---

## 4. Pontos que não podem desaparecer por falta de tempo

1. execução manual da busca binária;
2. previsão antes do código;
3. ordenação como pré-condição;
4. explicação intuitiva de `O(log n)`;
5. previsão antes do benchmark;
6. interpretação do benchmark;
7. discussão de que ordenar também custa.

Se necessário, reduzir o jogo humano, executar menos escalas ou discutir apenas dois cenários finais.

---

## 5. Erros conceituais a observar

- confundir índice com matrícula;
- atualizar `inicio = meio` ou `fim = meio`;
- acreditar que qualquer ordenação serve;
- concluir que busca binária é sempre melhor;
- interpretar `O(log n)` como custo constante;
- inferir complexidade a partir de um único tempo.

---

## 6. Operação dos materiais

- O Notebook Mestre é `EGC5310-EstruturasDados-S04-99-Aula-Mestre.ipynb`.
- Toda chamada de atividade possui link para o Notebook Estudante no Colab.
- O professor retoma a projeção após as atividades; não é necessário exigir navegação formal de retorno.
- O VisuAlgo é complementar. A aula não depende de internet.
- Se o primeiro encontro terminar após a previsão do benchmark, retomar com: **“Construímos uma previsão; agora produziremos evidências.”**

---

## 7. Frases de apoio

> Funcionar não significa ser adequado em qualquer escala.

> Cada comparação da busca binária vale mais porque a ordem permite descartar possibilidades.

> A pré-condição não é um detalhe de implementação.

> Comparações explicam o mecanismo; tempo mostra uma execução concreta.

> Organizar pode economizar trabalho depois, mas organizar também custa.
