# EGC5310 — Estruturas de Dados

## Semana 05 — Exercícios

**Tema:** hashing, conjuntos, dicionários e estruturas associativas  
**Versão:** 1.0  
**Status:** pronto para uso

## Orientações

Responda primeiro sem executar o código quando o enunciado solicitar previsão. Justifique escolhas pela operação predominante, não apenas pelo nome da estrutura.

## Exercício 1 — Previsão de posições

Considere uma tabela com 10 posições e `h(chave) = chave % 10`.

1. Calcule a posição das matrículas `121`, `134`, `147`, `154`, `181` e `194`.
2. Indique os pares que colidem.
3. Explique por que os resultados não provam que `% 10` distribui bem qualquer conjunto de matrículas.

## Exercício 2 — Chave não é posição

Explique a diferença entre:

- a matrícula `20260123`;
- o resultado `20260123 % 10`;
- a posição em que o registro aparece em uma lista de estudantes.

Inclua um exemplo no qual a posição na lista muda, mas a chave não muda.

## Exercício 3 — Diagnóstico de corrupção lógica

Analise:

```python
tabela = [None] * 10

def inserir(tabela, matricula, nome):
    posicao = matricula % len(tabela)
    tabela[posicao] = (matricula, nome)

inserir(tabela, 102, "Ana")
inserir(tabela, 172, "Bruno")
```

1. O programa gera erro?
2. Qual é o conteúdo de `tabela[2]` ao final?
3. Qual requisito do sistema foi violado?
4. Proponha uma representação simples que preserve os dois registros.

## Exercício 4 — Complete a busca por encadeamento

Complete a função:

```python
def buscar(tabela, matricula):
    posicao = ______________________________

    for chave_existente, estudante in ______________________________:
        if ______________________________:
            return estudante

    return None
```

Explique por que a comparação de chaves continua necessária mesmo após calcular a posição.

## Exercício 5 — Corrija a atualização

Esta inserção permite duas entradas com a mesma matrícula no mesmo bucket:

```python
def inserir(tabela, matricula, estudante):
    posicao = matricula % len(tabela)
    tabela[posicao].append((matricula, estudante))
```

Altere a função para substituir o registro existente quando a matrícula já estiver no bucket e inserir somente quando for uma matrícula nova.

## Exercício 6 — Da lista ao índice associativo

Dada a lista:

```python
estudantes = [
    {"matricula": 102, "nome": "Ana", "curso": "CD"},
    {"matricula": 118, "nome": "Bruno", "curso": "CC"},
    {"matricula": 131, "nome": "Carla", "curso": "CD"},
]
```

1. Construa `por_matricula`, um `dict` que associe matrícula ao registro completo.
2. Consulte com segurança a matrícula `118`.
3. Consulte com segurança a matrícula `999` sem provocar `KeyError`.
4. Explique o custo de construir o índice e por que ele pode compensar em consultas repetidas.

## Exercício 7 — Duplicatas entre fontes

As matrículas recebidas foram:

```python
matriculas = [102, 118, 131, 102, 145, 118, 170]
```

Escreva código com `set` que produza, na ordem da segunda ocorrência, a lista `[102, 118]`. Explique por que converter diretamente para `set` não produz essa mesma informação.

## Exercício 8 — Escolha da estrutura

Escolha `list`, `set` ou `dict` e justifique:

1. manter registros na ordem exata de chegada, inclusive repetições;
2. recuperar dados de uma disciplina pelo código;
3. verificar se um CPF integra uma lista de bloqueio;
4. contar quantas vezes cada categoria aparece;
5. guardar as cinco últimas medições em ordem.

Se houver mais de uma alternativa possível, explicite o requisito adicional que mudaria sua escolha.

## Exercício 9 — Corrija as afirmações

Reescreva cada afirmação para torná-la tecnicamente adequada.

1. “Uma tabela hash nunca tem colisões.”
2. “Busca em `dict` é sempre `O(1)`.”
3. “`O(1)` significa exatamente uma instrução.”
4. “Um `set` é um `dict` que associa cada chave ao registro completo.”
5. “Como `dict` é rápido, deve substituir qualquer lista.”

## Exercício 10 — Caso de Ciência de Dados

Um pipeline recebe 500 mil eventos. Cada evento possui `id_evento`, `id_usuario` e `tipo`. O pipeline precisa:

- preservar todos os eventos na ordem de chegada;
- rejeitar um `id_evento` já processado;
- recuperar rapidamente o perfil de um usuário por `id_usuario`.

Proponha uma combinação de estruturas, indicando o papel de cada uma. Não é obrigatório que uma única estrutura satisfaça todos os requisitos.

## Exercício 11 — Construir a pergunta experimental

Formule um experimento para comparar busca sequencial, busca binária e consulta em `dict`. Indique:

1. variável independente;
2. métricas;
3. cenários de busca;
4. custos de preparação que precisam ser registrados;
5. pelo menos duas ameaças à validade.

Não execute o benchmark nesta semana.

