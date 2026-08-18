# EGC5310 — Semana 02 — Soluções Comentadas

## Representação de dados e caracterização de problemas computacionais

**Disciplina:** EGC5310 — Tópicos Especiais em Ciência de Dados VI  
**Semana:** S02 — 20 e 21 de agosto de 2026  
**Artefato:** 07 — Soluções Comentadas  
**Correspondente a:** `EGC5310-EstruturasDados-S02-06-Exercicios.md`

---

# Orientação geral

Estas soluções não devem ser lidas como um gabarito de respostas únicas.

Na Semana 02, parte importante da aprendizagem está em **justificar escolhas**. Em vários exercícios, mais de uma representação pode ser defensável.

A pergunta central para avaliar uma resposta é:

> **A justificativa relaciona os dados, a operação que precisa ser realizada e as consequências da representação escolhida?**

A pergunta-guia continua sendo:

> **Melhor para fazer o quê?**

---

# Exercício 1 — A mesma informação, representações diferentes

## a) Lista

Uma possibilidade:

```python
livro = [501, "Estruturas de Dados", "A. Silva", 2024, True]
```

## b) Dicionário

```python
livro = {
    "codigo": 501,
    "titulo": "Estruturas de Dados",
    "autor": "A. Silva",
    "ano": 2024,
    "disponivel": True
}
```

## c) Recuperar o autor

Na lista:

```python
livro[2]
```

No dicionário:

```python
livro["autor"]
```

## d) Qual deixa o significado mais explícito?

O dicionário deixa o significado dos campos mais explícito porque a chave `"autor"` faz parte da própria representação.

Na lista, precisamos saber previamente que a posição `2` corresponde ao autor.

## e) Isso significa que o dicionário é sempre superior?

Não.

A conclusão correta não é:

> “dicionários são melhores que listas”.

A conclusão é:

> **essas representações possuem características diferentes e precisam ser avaliadas em função do problema e das operações.**

Uma lista pode ser perfeitamente adequada quando a ordem é importante, quando os elementos são tratados como uma sequência ou quando a posição possui significado natural.

### Erro comum

Responder apenas:

> “Dicionário é melhor porque é mais fácil.”

A justificativa precisa indicar **em que sentido** ele é mais adequado.

---

# Exercício 2 — O que estamos representando?

## Código A

```python
jogador = [10, "Rafael", "Brasil", 8]
```

Parece representar **um jogador individual**.

A estrutura é posicional. Operações naturais incluem acessar ou modificar valores por posição.

O significado de cada posição não está explícito no próprio código.

Por exemplo, precisamos saber que:

- posição `0` = número;
- posição `1` = nome;
- posição `2` = seleção;
- posição `3` = gols.

---

## Código B

```python
convocados = {2, 5, 8, 10, 14, 21}
```

Representa uma **coleção de números de jogadores convocados**.

Uma operação natural é verificar pertencimento:

```python
10 in convocados
```

Também podem surgir operações entre conjuntos.

Aqui, o conjunto não representa os dados completos de um jogador.

---

## Código C

```python
gols_por_jogo = [2, 0, 1, 3, 1]
```

Representa uma **sequência de quantidades**, provavelmente associadas aos jogos em determinada ordem.

Operações naturais:

- percorrer;
- somar;
- calcular média;
- acessar a quantidade de determinado jogo pela posição.

O significado da posição depende do contexto: é necessário saber a qual jogo cada posição corresponde.

---

## Código D

```python
jogador = {
    "numero": 10,
    "nome": "Rafael",
    "selecao": "Brasil",
    "gols": 8
}
```

Representa um **jogador individual**, como o Código A.

A diferença é que os atributos são explicitamente identificados pelas chaves.

Uma operação natural:

```python
jogador["selecao"]
```

### Ponto principal

Os códigos A e D representam aproximadamente o mesmo conceito, mas de maneiras diferentes.

B e C representam **outros aspectos do domínio**.

Isso reforça:

> **escolhemos uma representação em função daquilo que queremos representar e manipular.**

---

# Exercício 3 — Estrutura adequada para qual operação?

## a) Localizar matrícula `1082`

O dicionário é mais conveniente na representação apresentada:

```python
estudantes_dict.get(1082)
```

A matrícula foi usada diretamente como chave.

Na lista, precisamos procurar entre os registros.

---

## b) Listar todos do curso `"CD"`

Nenhuma das duas representações apresentadas possui um índice específico por curso.

Na lista:

```python
resultado = []

for estudante in estudantes_lista:
    if estudante["curso"] == "CD":
        resultado.append(estudante)
```

No dicionário:

```python
resultado = []

for matricula, estudante in estudantes_dict.items():
    if estudante["curso"] == "CD":
        resultado.append(estudante)
```

Nos dois casos, é natural percorrer os registros.

Portanto, não devemos concluir que o dicionário é automaticamente melhor para essa operação.

---

## c) Alterar o nome da matrícula `1047`

No dicionário:

```python
estudantes_dict[1047]["nome"] = "Novo nome"
```

A matrícula permite localizar diretamente o registro na representação utilizada.

Na lista, primeiro precisamos localizar o estudante.

---

## d) Percorrer todos e imprimir nomes

As duas representações permitem fazer isso.

Lista:

```python
for estudante in estudantes_lista:
    print(estudante["nome"])
```

Dicionário:

```python
for estudante in estudantes_dict.values():
    print(estudante["nome"])
```

Ambas exigem percorrer a coleção.

---

## e) Inserir novo estudante

Dicionário:

```python
estudantes_dict[1201] = {
    "nome": "Eva",
    "curso": "CD"
}
```

Lista:

```python
estudantes_lista.append({
    "matricula": 1201,
    "nome": "Eva",
    "curso": "CD"
})
```

As duas oferecem operações simples de inserção nesse exemplo.

A escolha não deve ser decidida apenas pela inserção.

### Síntese

A representação em dicionário está especialmente alinhada à operação:

> **localizar por matrícula**

porque a matrícula foi escolhida como chave.

Essa mesma organização não cria automaticamente uma forma direta de:

> **localizar por curso**.

---

# Exercício 4 — Torne o trabalho visível

Uma implementação possível:

```python
def buscar_matricula(estudantes, matricula):
    comparacoes = 0

    for estudante in estudantes:
        comparacoes += 1

        if estudante["matricula"] == matricula:
            return estudante, comparacoes

    return None, comparacoes
```

Teste:

```python
for alvo in [1023, 1082, 1125, 9999]:
    resultado, comparacoes = buscar_matricula(estudantes_lista, alvo)
    print(alvo, comparacoes, resultado)
```

Com os quatro registros apresentados:

- `1023`: 1 comparação;
- `1082`: 3 comparações;
- `1125`: 4 comparações;
- `9999`: 4 comparações.

## a)

Não. O número de comparações depende da posição do elemento ou de sua ausência.

## b)

Se estiver no início, poucas comparações são necessárias.

## c)

Se estiver no final, percorremos todos os elementos anteriores antes de encontrá-lo.

## d)

Se não existir, precisamos percorrer toda a coleção para concluir que ele não está presente.

## e)

Sem Big-O, uma boa descrição é:

> **à medida que a coleção cresce, uma busca desse tipo pode precisar examinar uma quantidade cada vez maior de estudantes.**

### Importante

Não é necessário formalizar a análise nesta semana.

A S02 procura tornar o **trabalho visível**.

---

# Exercício 5 — O trabalho que não aparece no código

## a)

O percurso aparece explicitamente em:

```python
for estudante in estudantes_lista:
```

No dicionário, vemos apenas:

```python
estudantes_dict.get(1082)
```

## b)

Não.

O computador continua realizando operações.

A diferença é que não estamos implementando explicitamente a estratégia de acesso no nosso código.

## c)

Uma conclusão importante:

> **o código escrito pelo programador não revela necessariamente todos os detalhes do trabalho realizado internamente pela estrutura.**

A estrutura de dados e sua implementação oferecem operações que encapsulam parte desse trabalho.

## d)

Porque a vantagem observada está associada à operação de consulta pela **chave utilizada na organização do dicionário**.

Se mudarmos a operação — por exemplo, procurar todos os estudantes de determinado curso — talvez seja necessário percorrer os registros novamente.

### Frase importante

> **O trabalho não desapareceu; parte dele foi transferida para a estrutura e sua implementação.**

---

# Exercício 6 — Uma estrutura desconhecida pode ser compreendida

Código:

```python
def buscar(no, alvo):
    if no is None:
        return None

    if alvo == no.valor:
        return no

    if alvo < no.valor:
        return buscar(no.esquerda, alvo)

    return buscar(no.direita, alvo)
```

## a)

Não.

Depois de uma comparação, o código escolhe uma direção.

## b)

Continua a busca pela parte esquerda:

```python
return buscar(no.esquerda, alvo)
```

## c)

O código parece aproveitar uma **organização dos valores que permite decidir uma direção a partir da comparação**.

Não é necessário, nesta semana, formalizar todas as propriedades de uma árvore binária de busca.

## d)

Na busca:

```python
for valor in valores:
```

os elementos são examinados sequencialmente.

Na árvore, cada comparação pode indicar onde continuar.

## e)

A solução com `for` percorre os elementos na sequência da coleção.

### Ponto didático

O estudante não precisa saber implementar uma árvore para reconhecer:

> **a organização dos dados permite uma estratégia de busca diferente.**

---

# Exercício 7 — Dados ordenados mudam o problema?

```python
matriculas = [1023, 1047, 1082, 1125, 1201, 1350]
```

## a)

Além dos valores, existe uma propriedade importante:

> **eles estão ordenados.**

## b)

Sim.

Um algoritmo pode utilizar a ordem para decidir onde continuar procurando.

## c)

Não da mesma forma.

Se a estratégia depende da ordenação, perder essa propriedade impede utilizar a mesma lógica.

## d)

Surge um trade-off:

> **manter os dados organizados pode favorecer determinadas operações, mas criar ou preservar essa organização também pode exigir trabalho.**

Por exemplo, novas inserções podem exigir cuidados para manter a ordem.

### Ponte conceitual

A representação não influencia apenas a consulta.

Também precisamos considerar:

- construção;
- inserção;
- atualização;
- manutenção da organização.

---

# Exercício 8 — Caracterização de um problema

Não existe uma única resposta.

Uma caracterização possível:

## Problema

Representar o catálogo de uma plataforma de streaming de forma que as operações frequentes possam ser realizadas adequadamente.

## Dados

Para cada título:

- identificador;
- nome;
- gênero;
- ano;
- avaliação média.

## Operações

- localizar pelo identificador;
- listar por gênero;
- inserir;
- atualizar avaliação.

## Representação possível

Uma possibilidade inicial:

```python
catalogo = {
    101: {
        "nome": "Filme A",
        "genero": "Drama",
        "ano": 2025,
        "avaliacao": 8.1
    }
}
```

O identificador é utilizado como chave.

## Trabalho esperado

Para localizar pelo identificador, a representação oferece acesso pela chave.

Para listar por gênero, com essa representação simples, ainda precisamos examinar os registros.

Inserções e atualizações podem ser realizadas utilizando o identificador.

## Volume

Com 100 registros, uma solução simples pode parecer suficiente.

Com 10 milhões, diferenças no trabalho necessário para operações frequentes tornam-se muito mais relevantes.

## Restrições

Exemplos:

- consultas por identificador muito frequentes;
- inclusão de novos títulos;
- atualização das avaliações;
- consultas por gênero;
- memória disponível;
- necessidade de simplicidade de manutenção.

### Observação

Outra representação pode ser defendida.

O critério é a qualidade da justificativa.

---

# Exercício 9 — Uma representação, duas operações

## a) Localizar identificador `103`

```python
filmes[103]
```

ou:

```python
filmes.get(103)
```

## b) Listar dramas

```python
dramas = []

for identificador, filme in filmes.items():
    if filme["genero"] == "Drama":
        dramas.append(filme)
```

## c)

A consulta pelo identificador utiliza diretamente a organização do dicionário.

## d)

A consulta por gênero ainda percorre os registros.

## e)

O exemplo mostra claramente:

> **uma representação pode estar organizada para favorecer uma operação específica sem oferecer a mesma vantagem para todas as outras.**

Se consultas por gênero fossem extremamente frequentes, poderíamos considerar uma organização adicional específica para gênero.

Isso, porém, introduziria novas consequências e responsabilidades de manutenção.

---

# Exercício 10 — Decisão justificada

Uma resposta possível:

> Eu utilizaria inicialmente um dicionário em que o identificador do usuário fosse a chave e os demais atributos fossem armazenados no valor associado. Essa organização está alinhada às duas operações predominantes: localizar um usuário pelo identificador e atualizar seu e-mail após localizá-lo. A escolha, entretanto, não resolve automaticamente a consulta por cidade. Para listar todos os usuários de Florianópolis, por exemplo, ainda seria necessário percorrer os registros ou manter uma organização adicional por cidade. Como o sistema possui aproximadamente 500 mil usuários, a frequência de cada operação deve ser considerada antes de adicionar estruturas auxiliares.

### Por que é uma boa resposta?

Ela menciona:

- os dados;
- a operação predominante;
- a representação;
- uma consequência positiva;
- uma limitação.

### Resposta insuficiente

> “Usaria dicionário porque é mais rápido.”

Falta responder:

> **mais rápido para quê e em função de qual organização?**

---

# Exercício 11 — Identifique o trade-off

## a) Dados ordenados

Benefício:

- a ordem pode ser aproveitada por determinadas estratégias de busca.

Possível custo:

- manter a ordem durante inserções ou alterações pode exigir trabalho adicional.

---

## b) Representação compacta por posições

Benefício:

- representação simples e compacta.

Possível custo:

- o significado dos campos pode ficar implícito e depender do conhecimento das posições.

---

## c) Estrutura para matrícula

Benefício:

- favorece consultas por matrícula.

Limitação:

- não oferece necessariamente a mesma vantagem para consultas por curso.

---

## d) Estrutura simples para poucos dados

Benefícios:

- facilidade de implementação;
- clareza;
- menor complexidade da solução.

Possível limitação:

- se o volume crescer muito, o trabalho de algumas operações pode se tornar relevante.

### Síntese

Trade-off não significa que uma solução está errada.

Significa:

> **uma decisão produz benefícios em algumas dimensões e consequências em outras.**

---

# Exercício 12 — Fechamento conceitual

## a)

“Funciona” significa que a representação consegue armazenar os dados e permitir alguma solução.

Isso não responde se ela é adequada para:

- as operações frequentes;
- o volume;
- as restrições;
- a manutenção necessária.

---

## b)

Porque “mais rápida” não é uma propriedade útil sem especificar:

> **mais rápida para qual operação, sob quais condições e com qual organização dos dados?**

---

## c)

Uma resposta possível:

> Os dados descrevem aquilo que precisa ser representado. As operações descrevem aquilo que precisamos fazer com esses dados. A representação organiza os dados de determinada maneira e essa organização influencia o trabalho necessário para realizar as operações.

---

## d)

Uma formulação possível:

> **Uma representação é adequada quando sua organização é coerente com os dados, com as operações relevantes e com as restrições do problema.**

Outras formulações justificadas são aceitáveis.

---

## e)

A pergunta que permanece é:

> **Como comparar sistematicamente o trabalho necessário para realizar diferentes operações quando o volume de dados cresce?**

Essa pergunta conduz à Semana 03.

---

# Desafio opcional — Proponha outra representação

Não existe solução única.

Uma resposta adequada deve apresentar quatro elementos.

## 1. Organização

Exemplo:

> No sistema acadêmico, manter uma estrutura principal por matrícula e uma estrutura auxiliar agrupando matrículas por curso.

Conceitualmente:

```python
por_matricula = {
    1023: {"nome": "Ana", "curso": "CD"},
    1047: {"nome": "Bruno", "curso": "CD"},
    1082: {"nome": "Carla", "curso": "Engenharia"},
}

por_curso = {
    "CD": {1023, 1047},
    "Engenharia": {1082},
}
```

## 2. Operação favorecida

- `por_matricula`: consulta por matrícula;
- `por_curso`: identificação dos estudantes de um curso.

## 3. Limitação

Agora temos informação relacionada em mais de uma estrutura.

Ao mudar o curso de um estudante, por exemplo, precisamos manter ambas coerentes.

## 4. Conhecimento adicional

Precisamos definir:

- como inserir;
- como remover;
- como atualizar;
- como garantir consistência entre as estruturas.

### Ponto importante

A estrutura adicional pode melhorar uma operação, mas cria um novo custo:

> **manter a organização adicional.**

Essa é uma forma concreta de trade-off.

---

# Síntese das soluções

Ao final da Semana 02, o estudante não precisa concluir:

> “dicionário é melhor que lista”

ou:

> “árvore é melhor que dicionário”.

A conclusão esperada é mais importante:

> **uma estrutura organiza os dados de determinada maneira; essa organização favorece certas operações e produz consequências para outras.**

Por isso, a sequência de raciocínio deve ser:

> **PROBLEMA → DADOS → OPERAÇÕES → REPRESENTAÇÃO → TRABALHO ESPERADO → VOLUME → RESTRIÇÕES**

E a pergunta que permanece para a próxima semana é:

> **Como transformar a ideia qualitativa de “trabalho esperado” em uma comparação mais sistemática?**
