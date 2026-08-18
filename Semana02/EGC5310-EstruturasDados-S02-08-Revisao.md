# EGC5310 — Semana 02 — Revisão

## Representação de dados e caracterização de problemas computacionais

**Disciplina:** EGC5310 — Tópicos Especiais em Ciência de Dados VI  
**Semana:** S02 — 20 e 21 de agosto de 2026  
**Artefato:** 08 — Revisão  

---

# 1. A pergunta da semana

Na Semana 01, recebemos os dados já organizados e investigamos uma operação de busca.

Na Semana 02, recuamos uma etapa:

> **Como decidimos a forma de representar um problema no computador?**

A principal conclusão foi:

> **Não existe uma representação que seja “melhor” isoladamente. Precisamos perguntar: melhor para fazer o quê?**

---

# 2. Representar é fazer uma escolha

Um mesmo estudante pode ser representado de diferentes maneiras.

Por exemplo:

```python
estudante = [1082, "Carla", "Engenharia"]
```

ou:

```python
estudante = {
    "matricula": 1082,
    "nome": "Carla",
    "curso": "Engenharia"
}
```

As duas representações armazenam as mesmas informações principais.

Mas elas não organizam essas informações da mesma forma.

Na primeira:

```python
estudante[2]
```

Na segunda:

```python
estudante["curso"]
```

A segunda representação torna o significado do campo mais explícito.

Isso, entretanto, **não significa que dicionários sejam sempre melhores que listas**.

A escolha depende do problema.

---

# 3. Estruturas diferentes podem representar coisas diferentes

No microcaso do álbum de figurinhas vimos várias possibilidades.

## Uma figurinha

```python
figurinha = [37, "Goleiro", "Brasil", False]
```

ou:

```python
figurinha = {
    "numero": 37,
    "jogador": "Goleiro",
    "selecao": "Brasil",
    "repetida": False
}
```

## Quais figurinhas possuímos

```python
tenho = {1, 2, 5, 8, 13}
```

## Quantidades

```python
import numpy as np

quantidades = np.array([1, 0, 2, 1, 3])
```

Também vimos que podemos criar uma representação própria por meio de uma classe.

O ponto não era memorizar todas essas estruturas.

O ponto era perceber:

> **a estrutura escolhida depende também daquilo que estamos tentando representar.**

---

# 4. Funcionar não significa ser adequado

Uma representação pode armazenar corretamente todos os dados e ainda assim não ser a escolha mais adequada para determinada necessidade.

Por isso, depois de perguntar:

> **Os dados cabem nessa representação?**

precisamos perguntar:

> **O que precisamos fazer com esses dados?**

---

# 5. As operações importam

No Sistema Acadêmico, algumas operações possíveis são:

- localizar estudante pela matrícula;
- obter seu curso;
- listar estudantes de determinado curso;
- listar disciplinas cursadas;
- inserir estudante;
- atualizar informações.

A representação precisa ser analisada em relação a essas operações.

Uma ideia central da semana foi:

> **DADOS + OPERAÇÕES → REQUISITOS DA REPRESENTAÇÃO**

---

# 6. Lista e dicionário: a operação muda a análise

Considere:

```python
estudantes_lista = [
    {"matricula": 1023, "nome": "Ana", "curso": "CD"},
    {"matricula": 1047, "nome": "Bruno", "curso": "CD"},
    {"matricula": 1082, "nome": "Carla", "curso": "Engenharia"},
    {"matricula": 1125, "nome": "Daniel", "curso": "CD"},
]
```

Para procurar uma matrícula:

```python
for estudante in estudantes_lista:
    if estudante["matricula"] == 1082:
        print(estudante)
        break
```

Agora considere:

```python
estudantes_dict = {
    1023: {"nome": "Ana", "curso": "CD"},
    1047: {"nome": "Bruno", "curso": "CD"},
    1082: {"nome": "Carla", "curso": "Engenharia"},
    1125: {"nome": "Daniel", "curso": "CD"},
}
```

A consulta por matrícula pode ser escrita como:

```python
estudantes_dict.get(1082)
```

A matrícula foi utilizada como chave da representação.

Mas, se mudarmos a pergunta para:

> **Quais estudantes pertencem ao curso de Ciência de Dados?**

podemos novamente precisar percorrer os registros:

```python
for matricula, estudante in estudantes_dict.items():
    if estudante["curso"] == "CD":
        print(estudante)
```

Portanto:

> **uma representação pode favorecer uma operação sem favorecer todas.**

---

# 7. O trabalho pode estar explícito ou encapsulado

Na lista, vemos explicitamente:

```python
for estudante in estudantes_lista:
```

No dicionário, vemos:

```python
estudantes_dict.get(1082)
```

Isso não significa que nenhum trabalho seja realizado no segundo caso.

Significa que parte do trabalho está sendo realizada pela própria estrutura e por sua implementação.

Assim:

> **o código que escrevemos nem sempre revela todos os detalhes do trabalho realizado internamente.**

---

# 8. Organização dos dados permite outras estratégias

Também observamos estruturas e estratégias que ainda não precisamos saber implementar.

## Árvore

Em uma árvore organizada adequadamente, uma comparação pode indicar em qual direção continuar:

```python
if alvo < no.matricula:
    return buscar(no.esquerda, alvo)

return buscar(no.direita, alvo)
```

A ideia importante é:

> **a organização dos dados pode permitir descartar possibilidades durante uma busca.**

## Dados ordenados

Considere:

```python
matriculas = [1023, 1047, 1082, 1125, 1201, 1350]
```

A ordenação é uma informação adicional que pode ser aproveitada por determinadas estratégias.

Não estudamos ainda formalmente essas estratégias.

O objetivo foi perceber:

> **organizar os dados de uma maneira diferente pode mudar a forma como uma operação é realizada.**

---

# 9. Trabalho esperado

Nesta semana ainda não fizemos uma análise formal do custo das operações.

Utilizamos uma ideia qualitativa:

> **trabalho esperado**

Perguntas úteis:

- precisamos olhar um elemento?
- vários?
- todos?
- precisamos comparar?
- percorrer?
- reorganizar?
- podemos descartar parte das possibilidades?

Também começamos a perguntar:

> **O que acontece quando o volume cresce?**

Uma solução que parece adequada para 10 registros pode exigir outra análise quando temos 10 milhões.

---

# 10. Caracterizando um problema computacional

A ficha construída na semana foi:

> **PROBLEMA → DADOS → OPERAÇÕES → REPRESENTAÇÃO → TRABALHO ESPERADO → VOLUME → RESTRIÇÕES**

## Problema

O que precisa ser resolvido?

## Dados

Que informações existem?

## Operações

O que precisamos fazer com elas?

## Representação

Como podemos organizar os dados?

## Trabalho esperado

Que tipo de trabalho parece necessário para realizar as operações?

## Volume

Quantos elementos esperamos manipular?

## Restrições

Que condições precisam ser consideradas?

---

# 11. Trade-offs

Escolhas computacionais possuem consequências.

Exemplos discutidos:

- facilitar uma operação pode não facilitar outra;
- manter dados ordenados pode ajudar determinadas buscas, mas a organização também precisa ser mantida;
- uma representação compacta pode deixar o significado dos campos menos explícito;
- uma estrutura adicional pode favorecer uma consulta, mas criar trabalho adicional de manutenção.

Por isso, trade-off não significa:

> **“uma solução está errada”.**

Significa:

> **uma escolha produz benefícios em algumas dimensões e consequências em outras.**

---

# 12. Cinco ideias para lembrar

## 1.

> **Dados do mundo real precisam ser representados computacionalmente.**

## 2.

> **A mesma informação pode ser representada de diferentes maneiras.**

## 3.

> **A escolha depende das operações que precisamos realizar.**

## 4.

> **Uma representação pode favorecer uma operação sem favorecer todas.**

## 5.

> **O volume e as restrições também influenciam a adequação da escolha.**

---

# 13. Verifique se você consegue responder

Sem consultar os materiais, tente responder:

### 1.

Por que:

```python
estudante["curso"]
```

pode comunicar mais significado que:

```python
estudante[2]
```

### 2.

Um dicionário indexado por matrícula facilita automaticamente uma consulta por curso?

### 3.

Por que não podemos concluir simplesmente que:

> “dicionários são mais rápidos que listas”?

### 4.

Que diferença existe entre representar **uma figurinha** e representar **quais figurinhas você possui**?

### 5.

O que significa “trabalho esperado” nesta semana?

### 6.

Por que o volume dos dados importa?

### 7.

O que significa dizer que existe um trade-off?

### 8.

Complete:

> **Uma representação é adequada quando...**

---

# 14. Miniatividade de revisão

Considere:

```python
produtos = {
    1001: {"nome": "Teclado", "categoria": "Periféricos"},
    1002: {"nome": "Monitor", "categoria": "Vídeo"},
    1003: {"nome": "Mouse", "categoria": "Periféricos"},
}
```

Responda mentalmente ou em poucas linhas.

## a)

Qual operação essa organização parece favorecer?

## b)

Como você localizaria o produto `1002`?

## c)

Como listaria todos os produtos da categoria `"Periféricos"`?

## d)

As duas operações exigem o mesmo tipo de trabalho?

## e)

Se a consulta por categoria fosse muito frequente, que pergunta deveríamos fazer sobre a representação?

---

# 15. A pergunta que ficou aberta

Durante a Semana 02 utilizamos expressões como:

> **“parece exigir menos trabalho”**

e:

> **“precisa percorrer mais elementos”**

Essas descrições são úteis, mas ainda são qualitativas.

A pergunta que levamos para a próxima semana é:

> **Como podemos comparar sistematicamente o trabalho necessário para realizar diferentes operações quando o volume de dados cresce?**

---

# 16. Preparação para a Semana 03

Não é necessário antecipar fórmulas.

Chegue à próxima semana sabendo reconhecer situações como:

### Percurso

```python
for elemento in dados:
    ...
```

### Acesso por chave

```python
dados[chave]
```

### Comparação e decisão

```python
if alvo < valor:
    ...
```

E, principalmente, esteja preparado para perguntar:

> **Quanto trabalho cada operação realiza quando o tamanho dos dados muda?**

---

# Frase final

> **Melhor para fazer o quê?**

Na próxima semana, acrescentaremos outra pergunta:

> **E quanto trabalho é necessário para fazer isso?**
