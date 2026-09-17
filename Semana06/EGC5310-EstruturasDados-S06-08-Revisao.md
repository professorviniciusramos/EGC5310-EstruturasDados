# EGC5310 --- Estruturas de Dados para Ciência de Dados

## Semana 06 --- Revisão e registro pós-aula

**Artefato:** 08 --- Revisão\
**Status:** Instrumento para preenchimento após a aula\
**Regra:** não preencher expectativas como se fossem observações. Quando
não houver evidência, registrar **não observado**.

## 1. Síntese da proposta

Narrativa planejada:

> escolha inicial → implementações obrigatórias → medida → mecanismo
> interno → mudança da operação → nova escolha

Pergunta central:

> **Como a representação dos mesmos dados favorece algumas operações e
> encarece outras?**

## 2. Dataset e contexto

-   O carregamento do Online Retail funcionou?
-   O download direto foi confiável?
-   Foi necessária cópia local/upload?
-   O tempo de leitura interferiu na aula?
-   Os estudantes compreenderam a diferença entre \~541 mil linhas
    transacionais e produtos distintos?
-   A visão `StockCode → Description` ficou clara?

**Registro:**

> Preencher após a aula.

## 3. Atividade 1 --- hipótese inicial

-   Os estudantes realmente escolheram antes de receber as comparações?
-   `dict` apareceu como resposta automática?
-   As justificativas mencionavam propriedades ou apenas Big-O?
-   Houve estudantes que escolheram estruturas diferentes para operações
    diferentes?
-   As hipóteses foram preservadas para retorno na Atividade 9?

**Registro:**

> Preencher após a aula.

## 4. Atividade 2 --- três buscas

-   A busca sequencial foi implementada sem dificuldade?
-   A busca binária recuperou adequadamente a S04?
-   Houve confusão com limites ou comparação de strings?
-   Os estudantes compreenderam a construção do `dict`?
-   Conseguiram explicar o comportamento para chave ausente?
-   Apareceu a conclusão precoce "`dict` é sempre melhor"?

**Registro:**

> Preencher após a aula.

## 5. Atividade 3 --- preparação × consulta

-   As previsões foram registradas antes do benchmark?
-   Os estudantes distinguiram preparação de consulta?
-   A quantidade de consultas alterou a interpretação?
-   Houve tentativa de encontrar um ponto de cruzamento universal?
-   A diferença entre Big-O e tempo medido ficou clara?
-   Os tamanhos escolhidos produziram diferenças observáveis?
-   O benchmark consumiu tempo excessivo?

**Registro:**

> Preencher após a aula.

## 6. Atividade 4 --- intervalo

-   A mudança de operação produziu surpresa?
-   Os estudantes perceberam por que hashing não organiza naturalmente
    intervalos?
-   O limite inferior foi compreendido?
-   A expressão O(log n + k) fez sentido?
-   Ficou claro que a faixa é lexicográfica?
-   A turma conseguiu dizer "o `dict` não piorou; a pergunta mudou"?

**Registro:**

> Preencher após a aula.

## 7. Exploração intermediária --- multiplicidade e composição

-   Os estudantes perceberam que `InvoiceNo` repetido pode representar informação e não erro?
-   Ficou clara a diferença entre preservar ocorrências e preservar apenas unicidade?
-   Entenderam que `dict[invoice] = produto` sobrescreve o valor anterior?
-   Conseguiram compreender `dict[invoice] = list(...)` como composição de estruturas e relação 1:N?
-   Alguém afirmou que "`dict` não permite vários valores"? Como a formulação foi corrigida?
-   Evidência observada:

## 8. Atividade 5 --- `set`

-   `A | B` (união) foi compreendido?
-   `A ^ B` (diferença simétrica) exigiu explicação adicional?
-   A turma conseguiu distinguir união, interseção, diferença e diferença simétrica?

-   O problema de clientes tornou a semântica de conjunto natural?
-   Os estudantes distinguiram `set` de `dict`?
-   Ficou claro que ambos podem realizar pertencimento por hashing?
-   `&`, `|`, `-` e `^` foram compreendidos semanticamente?
-   A direção de `A - B` foi compreendida?
-   Os estudantes perceberam que uma linha Python pode esconder vários
    lookups?
-   A explicação de hash → posição → comparação → probing foi
    suficiente?

**Registro:**

> Preencher após a aula.

## 9. Atividade 6 --- `list`, `append` e memória

-   O desenho array de referências ajudou?
-   Os estudantes distinguiram referências e objetos?
-   Tamanho lógico × capacidade ficou claro?
-   Alguém acreditava que Python sempre dobra a lista?
-   O experimento com `sys.getsizeof()` mostrou degraus visíveis?
-   A remoção mostrou comportamento diferente da expectativa?
-   O conceito de over-allocation foi compreendido?
-   O(1) amortizado resolveu a dúvida de que O(1) significaria sempre o
    mesmo número de operações?
-   A limitação de `sys.getsizeof()` foi compreendida?

**Registro:**

> Preencher após a aula.

## 10. Atividade 7 --- inserções

-   A turma distinguiu encontrar posição de inserir fisicamente?
-   Ficou claro por que `bisect.insort` continua O(n)?
-   Os estudantes perceberam que `append`, `dict`, `set` e lista
    ordenada não preservam a mesma semântica?
-   A discussão sobre custo de manutenção apareceu naturalmente?

**Registro:**

> Preencher após a aula.

## 11. Atividade 8 --- Python × NumPy

-   A mudança para processamento em massa ficou clara?
-   Os estudantes previram O(n) para as duas soluções?
-   Houve surpresa com a diferença de tempo?
-   Conseguiram explicar a diferença sem atribuir Big-O diferente?
-   `dtype`, homogeneidade e representação compacta ficaram claros?
-   O custo de conversão foi lembrado como preparação?
-   A ponte para Pandas foi feita? Ajudou ou desviou?

**Registro:**

> Preencher após a aula.

## 12. Atividade 9 --- decisão revista

-   Houve tempo suficiente para voltar à hipótese inicial?
-   Os estudantes mudaram escolhas?
-   Quem manteve a escolha apresentou justificativa mais forte?
-   As respostas finais mencionaram operação, preparação, manutenção ou
    limitação?
-   A possibilidade de múltiplas representações apareceu?
-   O problema de sincronização/consistência foi reconhecido?

**Registro:**

> Preencher após a aula.

## 13. Notebook Mestre + Quarto

-   A logo apareceu corretamente na abertura?
-   O link do Mestre para o Colab funcionou?
-   As chamadas das atividades apontaram claramente para o Notebook
    Estudante?
-   Os links para o Colab do Estudante funcionaram?
-   Os slides intermediários foram suficientes para levar às atividades?
-   Houve algum salto abrupto de conceito para exercício?
-   Algum slide ficou excessivamente textual?
-   Diagramas de `list`, hashing, multiplicidade/composição e `bisect.insort` ficaram legíveis?
-   Houve sobreposição, corte ou fonte inadequada?
-   O render ocorreu sem conflito de metadados?

**Registro:**

> Preencher após a aula.

## 14. Notebook Estudante

-   Os TODOs estavam adequados ao nível do segundo semestre?
-   Houve "caça aos TODOs" em vez de raciocínio?
-   As previsões foram realmente escritas?
-   O volume de implementação foi adequado?
-   Alguma atividade precisava de mais scaffolding?
-   Alguma atividade entregava resposta demais?
-   A alternância Mestre → Estudante foi fluida?
-   O badge/link do Colab funcionou?

**Registro:**

> Preencher após a aula.

## 15. Notebook Professor

-   Foi possível conduzir a aula olhando principalmente o Notebook
    Professor?
-   A ordem estava sincronizada com o Estudante?
-   As soluções estavam imediatamente acessíveis?
-   "Pergunta", "resultado esperado", "erro comum" e "discussão"
    ajudaram?
-   Alguma solução precisava de explicação adicional?
-   Houve necessidade de procurar informação em outro documento durante
    uma atividade?
-   Os tempos de execução previstos foram adequados?

**Registro:**

> Preencher após a aula.

## 16. Ritmo e tempo

-   Onde terminou o primeiro encontro?
-   Onde começou o segundo?
-   Qual atividade excedeu o tempo?
-   Qual poderia ser encurtada sem perda conceitual?
-   Houve tempo suficiente para interpretação após os benchmarks?
-   A Atividade 9 foi preservada?
-   Houve ao menos cinco minutos de síntese?

**Registro:**

> Preencher após a aula.

## 17. Evidências concretas de aprendizagem

Registrar frases, respostas, códigos ou decisões que mostrem se os
estudantes conseguiram:

-   dizer "melhor para qual operação?";
-   distinguir preparação e consulta;
-   justificar ordenação para intervalos;
-   justificar `set` pela semântica;
-   explicar O(1) médio sem tratá-lo como número fixo de operações;
-   explicar O(1) amortizado;
-   distinguir tamanho e capacidade;
-   explicar deslocamento na inserção ordenada;
-   explicar Python × NumPy sem alterar indevidamente o Big-O;
-   rever a escolha inicial a partir das evidências.

**Evidências:**

> Preencher após a aula.

## 18. Erros conceituais observados

Marcar apenas os que efetivamente apareceram:

-   [ ] `dict` é sempre a melhor estrutura.
-   [ ] `set` é melhor que `dict` sempre que existe `in`.
-   [ ] uma linha de Python = uma operação.
-   [ ] O(1) = exatamente uma operação.
-   [ ] `append` custa sempre exatamente o mesmo.
-   [ ] Python sempre dobra a `list`.
-   [ ] remover metade = liberar metade da memória.
-   [ ] repetição sempre significa dado duplicado a remover.
-   [ ] `set` preserva quantidade de ocorrências.
-   [ ] `dict` não pode representar uma chave associada a vários elementos.
-   [ ] `A ^ B` significa união.
-   [ ] `bisect.insort` = O(log n).
-   [ ] NumPy é mais rápido porque seria O(1).
-   [ ] `sys.getsizeof()` mede todos os objetos.
-   [ ] outro: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_.

**Comentários:**

> Preencher após a aula.

## 19. Decisões para a Semana 07

### Manter

> Preencher.

### Modificar

> Preencher.

### Retomar

> Preencher.

### Retirar

> Preencher.

### Conteúdo que precisa ser retomado explicitamente

> Preencher.

### Principal evidência para orientar a próxima semana

> Registrar em uma ou duas frases.

## 20. Avaliação do novo Notebook Professor

A S06 introduziu o Notebook Professor como artefato operacional
adicional.

Após a aula, decidir com base em evidência:

-   facilitou a condução?
-   reduziu procura por soluções?
-   aumentou o custo de manutenção?
-   houve divergência entre Estudante e Professor?
-   vale repetir na S07?
-   deve tornar-se parte permanente da arquitetura ou permanecer
    experimental?

**Decisão provisória após a aula:**

> Preencher.
