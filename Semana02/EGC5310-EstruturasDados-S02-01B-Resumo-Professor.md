# EGC5310 — Semana 02 — Resumo do Professor

## Representação de dados e caracterização de problemas computacionais

**Leia 5 minutos antes da aula.**

---

# 1. A ideia da semana em uma frase

> **A representação dos dados deve ser escolhida em função do problema e das operações que precisamos realizar.**

---

# 2. De onde estamos vindo

Na Semana 01, partimos de uma representação já pronta dos registros acadêmicos e investigamos uma operação:

> localizar um estudante pela matrícula.

A turma viu que:

> **uma solução pode funcionar e ainda assim deixar de ser adequada quando o volume de dados cresce.**

Nesta semana, recuamos uma etapa:

> **Por que os dados estavam representados daquela maneira?**

---

# 3. A pergunta central

> **Existe uma única forma correta de representar os dados de um problema?**

A resposta que deve emergir é:

> **Não. A adequação depende dos dados, das operações e das restrições do problema.**

---

# 4. A história que precisa acontecer

A sequência conceitual da semana é:

> **problema → dados → representação → operações → consequências → trabalho esperado → caracterização**

Não apresentar estruturas prontas cedo demais.

O estudante precisa primeiro perceber que:

1. os dados do mundo real precisam ser representados;
2. existem diferentes formas de representar a mesma informação;
3. uma representação pode facilitar algumas operações e dificultar outras;
4. portanto, não existe “a melhor estrutura” sem perguntar:
   > **melhor para fazer o quê?**

---

# 5. Como começar

Mostrar rapidamente os registros usados na Semana 01:

```python
estudantes = [
    {"matricula": 1023, "nome": "Ana", "curso": "Ciência de Dados"},
    {"matricula": 1047, "nome": "Bruno", "curso": "Ciência de Dados"},
    {"matricula": 1082, "nome": "Carla", "curso": "Engenharia"},
]
```

Perguntar:

> **“Na semana passada nós procuramos estudantes nesses dados. Mas por que eles estavam organizados assim?”**

Depois:

> **“Essa é a única forma possível?”**

Não fazer revisão extensa de busca sequencial ou Big-O.

---

# 6. Primeiro contraste importante

Comparar:

```python
[1082, "Carla", "Engenharia"]
```

com:

```python
{
    "matricula": 1082,
    "nome": "Carla",
    "curso": "Engenharia"
}
```

Perguntar:

> “As duas guardam as mesmas informações?”

> “Expressam essas informações da mesma forma?”

> “O que significa `registro[2]`?”

> “E `registro["curso"]`?”

Não concluir:

> “dicionário é melhor”.

A conclusão é apenas:

> **os mesmos dados podem ser representados de maneiras diferentes.**

---

# 7. Atividade 1

O estudante deve propor sua própria representação para um estudante contendo:

- matrícula;
- nome;
- curso;
- semestre de ingresso;
- situação.

A apresentação deve mostrar claramente:

> **AGORA É COM VOCÊ → Notebook Estudante · Atividade 1**

O estudante deve:

- implementar;
- acessar atributos;
- justificar a escolha.

Pergunta importante durante a circulação:

> **“Por que você escolheu essa representação?”**

---

# 8. Fazer o problema crescer

Depois, incluir disciplinas cursadas:

- código;
- nome;
- semestre;
- nota;
- situação.

Perguntar:

> **“Onde colocamos isso?”**

> **“Uma disciplina é apenas mais um atributo do estudante?”**

> **“A nota pertence à disciplina ou à relação daquele estudante com aquela disciplina?”**

Não transformar isso em aula de modelagem de banco de dados.

A ideia é fazer aparecer:

- entidade;
- atributo;
- coleção;
- relação.

---

# 9. O ponto mais importante da semana

Perguntar:

> **“O que precisamos fazer com esses dados?”**

Exemplos:

- localizar pela matrícula;
- obter curso;
- listar estudantes por curso;
- listar disciplinas;
- inserir estudante;
- atualizar informação.

Então:

> **“A representação que escolhemos favorece todas essas operações igualmente?”**

Aqui deve emergir:

> **dados + operações → requisitos da representação**

---

# 10. Introdução ao custo

Esta semana **precisa falar de custo**, mas apenas intuitivamente.

Comparar:

```python
estudantes = [
    {"matricula": 1023, "nome": "Ana"},
    {"matricula": 1047, "nome": "Bruno"},
    {"matricula": 1082, "nome": "Carla"},
]
```

com:

```python
estudantes = {
    1023: {"nome": "Ana"},
    1047: {"nome": "Bruno"},
    1082: {"nome": "Carla"},
}
```

Perguntar:

> **“Para encontrar 1082, fazemos o mesmo tipo de trabalho?”**

Não explicar hashing.

Não dizer simplesmente:

> “dicionário é O(1)”.

Em seguida, mudar a operação:

> **“E se eu quiser todos os estudantes de Ciência de Dados?”**

Pergunta-chave:

> **“Mais rápido para qual operação?”**

A conclusão deve ser:

> **uma representação pode favorecer uma operação sem favorecer todas.**

---

# 11. Atividade 2

Apresentar diferentes representações e diferentes operações.

Antes de executar, pedir que o estudante preveja:

- qual representação parece mais adequada;
- qual parece exigir menos trabalho;
- por quê.

Mostrar:

> **AGORA É COM VOCÊ → Notebook Estudante · Atividade 2**

A lógica é:

> **previsão → execução → interpretação**

Não é benchmark.

---

# 12. A ficha de caracterização

Ela deve aparecer depois da investigação, não antes.

Construir:

> **PROBLEMA → DADOS → OPERAÇÕES → REPRESENTAÇÃO → TRABALHO ESPERADO → VOLUME → RESTRIÇÕES**

Lembrar:

### Problema
O que precisa ser resolvido?

### Dados
Que informações existem?

### Operações
O que precisamos fazer?

### Representação
Como organizar os dados?

### Trabalho esperado
Quantos elementos parece necessário observar?  
É preciso percorrer? Comparar? Reorganizar?

### Volume
10 registros ou 10 milhões?

### Restrições
Consultas frequentes? Inserções? Memória? Simplicidade?

---

# 13. Trade-off

Se surgir naturalmente, introduzir:

> **trade-off**

Uma escolha pode favorecer:

- clareza;
- acesso;
- inserção;
- consulta;
- simplicidade;
- desempenho.

Não existe escolha sem consequência.

---

# 14. Atividade 3

Pedir:

> **“Escolha uma representação e justifique.”**

A justificativa deve mencionar:

- dados;
- operação predominante;
- consequência da escolha.

Não aceitar como suficiente:

> “porque é mais fácil”

ou:

> “porque dicionário é melhor”.

Responder com:

> **“Melhor para fazer o quê?”**

---

# 15. O que NÃO fazer

Evitar:

- catálogo de listas, tuplas, sets e dicionários;
- aula formal de hashing;
- tabelas prontas de complexidade;
- aprofundamento de Big-O;
- benchmark formal;
- antecipar busca binária;
- apresentar uma estrutura como universalmente melhor;
- transformar a aula em modelagem de banco de dados.

---

# 16. O que observar

A aula está funcionando se os estudantes começam a dizer coisas como:

> “Depende da operação.”

> “Essa representação facilita a busca por matrícula.”

> “Para listar por curso talvez seja diferente.”

> “Se os dados crescerem, o trabalho pode mudar.”

> “A escolha tem consequência.”

Essas respostas são mais importantes que a sintaxe perfeita.

---

# 17. As transições para o Notebook Estudante

Não esquecer:

> **APRESENTAÇÃO → CHAMADA VISUAL → NOTEBOOK ESTUDANTE → ATIVIDADE → DISCUSSÃO → RETORNO À APRESENTAÇÃO**

As chamadas precisam aparecer claramente no Reveal.js.

Não deixar o estudante adivinhar quando deve abrir seu notebook.

---

# 18. Se faltar tempo

Priorizar:

1. representação não é única;
2. representação depende das operações;
3. introdução qualitativa ao trabalho necessário;
4. Atividade 1;
5. Atividade 2;
6. ficha de caracterização;
7. pergunta final para a S03.

A Atividade 3 pode ser reduzida.

---

# 19. Como terminar

Retomar:

> **“Existe uma única forma correta de representar os dados?”**

Depois:

> **“Dissemos várias vezes que uma operação parece exigir mais ou menos trabalho.”**

Pausa.

Perguntar:

> **“Mas ‘parece’ é suficiente?”**

E encerrar com:

> **“Como podemos comparar sistematicamente o trabalho necessário para realizar essas operações quando o volume de dados cresce?”**

Não responder completamente.

Essa é a entrada da Semana 03.

---

# 20. Se lembrar de apenas cinco coisas

1. **Não comece pela estrutura; comece pelo problema.**
2. **Pergunte sempre: “melhor para fazer o quê?”**
3. **Faça os estudantes trabalharem no Notebook Estudante e sinalize claramente as transições.**
4. **Introduza custo apenas como trabalho esperado, sem formalizar demais.**
5. **Termine deixando aberta a pergunta que leva à Semana 03: como comparar sistematicamente os custos das operações?**

---

# 21. Frase final para levar à sala

> **Representar dados é fazer uma escolha. Escolhas só fazem sentido quando sabemos o que precisamos fazer com os dados.**

---

**EGC5310 — Semana 02 — Resumo do Professor — 2026/2**