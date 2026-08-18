# EGC5310-EstruturasDados --- Guia de Desenvolvimento das Próximas Semanas

**Disciplina:** EGC5310 --- Tópicos Especiais em Ciência de Dados VI\
**Projeto pedagógico:** Estruturas de Dados\
**Finalidade:** orientar a preparação das semanas S02--S18 e preservar
as decisões tomadas após a Semana 01\
**Status:** referência operacional para produção semanal\
**Versão:** 1.0\
**Data:** 16/08/2026

------------------------------------------------------------------------

# 1. Finalidade

Este documento registra como o desenvolvimento dos materiais da
disciplina deve prosseguir após a execução da Semana 01.

Ele deve ser consultado antes de iniciar uma nova semana para evitar que
decisões já tomadas sejam rediscutidas ou que a arquitetura da
disciplina seja alterada sem necessidade.

A **semana** continua sendo a unidade de planejamento. Os dois encontros
não devem ser artificialmente divididos em "aula teórica" e "aula
prática". Discussão, código, experimentação, exercícios e formalização
devem aparecer quando forem didaticamente necessários.

------------------------------------------------------------------------

# 2. Ponto de partida de cada nova semana

Ao receber a solicitação para desenvolver a **Semana XX**, o primeiro
passo é consultar os documentos vigentes da disciplina, especialmente:

1.  **Plano de Ensino / ementa / cronograma**, para identificar o
    conteúdo previsto para a semana;
2.  **Documentos-Base**, para preservar metodologia, CPMD, padrão
    semanal, convenções e arquitetura;
3.  **materiais e revisão da semana anterior**, principalmente
    observações registradas depois da aula;
4.  quando pertinente, materiais já produzidos em semanas anteriores,
    para preservar continuidade conceitual e exemplos.

Não se deve inventar um novo tema semanal quando o cronograma já
estabelece o conteúdo.

------------------------------------------------------------------------

# 3. Princípio didático

O desenvolvimento deve partir do problema e não da estrutura de dados
isoladamente.

Fluxo preferencial:

**problema → solução inicial → observação → custo → limitação →
formalização → estrutura/algoritmo adequado → experimento →
interpretação → nova pergunta**

Os conceitos formais devem aparecer quando ajudam a compreender o
problema ou comparar soluções.

A disciplina deve integrar continuamente:

-   problema;
-   representação dos dados;
-   implementação;
-   análise de operações;
-   ordem de grandeza;
-   benchmark quando fizer sentido;
-   interpretação dos resultados;
-   exercícios;
-   reflexão sobre adequação da solução.

------------------------------------------------------------------------

# 4. Dois formatos de aula em experimentação

Durante as próximas semanas serão explorados **dois formatos**, sem
decidir antecipadamente que um deles substituirá o outro.

## Formato A --- PPTX + notebooks separados

Componentes principais:

-   apresentação em PPTX;
-   notebook **Aula**, utilizado pelo professor;
-   notebook **Estudante**, derivado da mesma narrativa e preparado para
    participação ativa.

Padrão:

`EGC5310-EstruturasDados-SXX-02-Slides.pptx`

`EGC5310-EstruturasDados-SXX-03-Aula.ipynb`

`EGC5310-EstruturasDados-SXX-04-Estudante.ipynb`

Os slides devem funcionar como sequência visual contínua da semana. Não
devem ser pensados como "slides da quinta" e "slides da sexta".

Quando um slide depender de código ou experimento, deve indicar
claramente o notebook e a seção correspondente.

O notebook Estudante deve conter, quando pertinente:

-   TODOs;
-   previsões antes da execução;
-   pequenas implementações;
-   perguntas de interpretação;
-   experimentos;
-   conclusões escritas pelo estudante.

## Formato B --- Notebook mestre + Quarto

Neste formato, um **Notebook Mestre** concentra a narrativa completa da
semana:

-   explicações;
-   perguntas;
-   código;
-   imagens e diagramas;
-   experimentos;
-   transições didáticas;
-   atividades;
-   referências necessárias para a apresentação.

O notebook mestre funciona como **fonte de conteúdo**.

A apresentação é gerada a partir dele com **Quarto + Reveal.js**,
seguindo as convenções técnicas já testadas.

Importante: evitar inserir no notebook mestre configurações de `format`
que voltem a provocar conflitos de renderização. A configuração de
apresentação deve permanecer fora do conteúdo quando essa separação for
necessária.

O objetivo deste formato é testar se uma fonte única reduz:

-   duplicação de conteúdo;
-   inconsistências entre slides e notebook;
-   esforço de manutenção;
-   dificuldade de retomar a disciplina em ofertas futuras.

------------------------------------------------------------------------

# 5. Regra para escolha do formato em cada semana

Não existe, neste momento, um formato vencedor.

Ao preparar uma nova semana, deve-se verificar qual formato será testado
naquela semana ou se ambos serão produzidos para comparação.

A escolha deve considerar a experiência real das semanas anteriores, e
não preferência abstrata por uma ferramenta.

Devem ser observados:

-   fluidez durante a aula;
-   quantidade de trocas entre janelas;
-   facilidade de retomada;
-   clareza para os estudantes;
-   esforço de preparação;
-   esforço de manutenção;
-   qualidade da apresentação;
-   integração com código;
-   facilidade de reutilização futura.

------------------------------------------------------------------------

# 6. Fluxo de produção semanal

O fluxo-base permanece:

**Planejamento → Roteiro → Slides/Notebook Mestre → Notebook Aula →
Notebook Estudante → Benchmark (quando necessário) → Exercícios →
Soluções → Revisão → Publicação**

O fluxo pode variar levemente conforme o formato experimental da semana,
mas os papéis pedagógicos dos artefatos devem ser preservados.

## Etapa 1 --- Planejamento e narrativa

-   consultar ementa/cronograma;
-   identificar o conteúdo da semana;
-   verificar pré-requisitos;
-   recuperar observações da semana anterior;
-   definir problema orientador;
-   definir resultados de aprendizagem;
-   fechar a narrativa didática.

## Etapa 2 --- Roteiro

Produzir:

`EGC5310-EstruturasDados-SXX-01-Roteiro.md`

O roteiro deve ser suficientemente detalhado para permitir que o
professor retome a semana anos depois e compreenda:

-   o que pretendia ensinar;
-   por que a sequência foi escolhida;
-   o que deve perguntar;
-   quando utilizar código;
-   quando realizar atividades;
-   o que observar nos estudantes;
-   como encerrar a semana.

## Etapa 3 --- Material principal de apresentação

Conforme o experimento da semana:

-   produzir/revisar o PPTX; ou
-   produzir o Notebook Mestre e renderizar com Quarto.

Antes de gerar o arquivo final, apresentar a estrutura/conteúdo para
validação quando houver mudanças relevantes na narrativa.

## Etapa 4 --- Notebooks

No Formato A:

-   Notebook Aula completo;
-   Notebook Estudante derivado e orientado à participação.

No Formato B:

-   Notebook Mestre como fonte;
-   avaliar, conforme a experiência, quais derivações são realmente
    necessárias para professor e estudante.

Não alterar a arquitetura permanentemente apenas porque um teste
funcionou em uma semana. A decisão deve resultar de experiência
acumulada.

## Etapa 5 --- Benchmark

Produzir somente quando contribuir para o objetivo didático.

Quando houver:

`EGC5310-EstruturasDados-SXX-05-Benchmark.py`

`EGC5310-EstruturasDados-SXX-05-Benchmark.csv`

`EGC5310-EstruturasDados-SXX-05-Benchmark.md`

O `.py` executa o experimento; o `.csv` registra os resultados; o `.md`
explica ao professor o propósito, a execução e a interpretação esperada.

## Etapa 6 --- Exercícios

Produzir:

`EGC5310-EstruturasDados-SXX-06-Exercicios.md`

Os exercícios devem fazer parte da sequência didática e podem ser
intercalados com exposição, código e discussão.

## Etapa 7 --- Soluções

Produzir:

`EGC5310-EstruturasDados-SXX-07-Solucoes.md`

As soluções devem registrar não apenas a resposta, mas:

-   raciocínio esperado;
-   interpretações possíveis;
-   erros comuns;
-   pontos que merecem discussão em sala.

## Etapa 8 --- Revisão

Produzir:

`EGC5310-EstruturasDados-SXX-08-Revisao.md`

Verificar:

-   coerência entre artefatos;
-   nomenclatura;
-   funcionamento do código;
-   compatibilidade com Colab;
-   referências entre slides/notebooks;
-   links;
-   consistência conceitual;
-   viabilidade no tempo disponível;
-   pendências que realmente bloqueiam a aula.

------------------------------------------------------------------------

# 7. Depois de cada semana executada

Após ministrar a semana, registrar observações no material de revisão ou
no documento definido para esse fim.

Registrar apenas evidências úteis, por exemplo:

-   partes que demoraram mais ou menos que o previsto;
-   conceitos que geraram dificuldade;
-   exercícios que funcionaram bem ou mal;
-   problemas no Colab;
-   problemas na apresentação;
-   qualidade das transições entre PPTX e notebook;
-   qualidade da experiência com Quarto;
-   necessidade de exemplos adicionais;
-   conteúdo que não foi abordado;
-   reação dos estudantes;
-   alterações recomendadas para a próxima oferta.

Essas observações devem ser consideradas **antes de preparar a semana
seguinte** quando tiverem impacto sobre a continuidade didática.

------------------------------------------------------------------------

# 8. O que não fazer

Durante a produção das próximas semanas:

-   não redesenhar a arquitetura sem necessidade operacional real;
-   não criar novos tipos de documentos apenas por antecipação;
-   não alterar nomenclaturas já congeladas;
-   não separar artificialmente os encontros em teoria e prática;
-   não produzir benchmark quando ele não acrescentar valor;
-   não obrigar que todo o conteúdo planejado seja concluído se a
    aprendizagem exigir mais tempo;
-   não transformar a disciplina em uma sequência de estruturas
    apresentadas sem problema motivador;
-   não assumir que um único teste com PPTX ou Quarto determina o
    formato definitivo.

------------------------------------------------------------------------

# 9. Critério de evolução

As decisões futuras sobre PPTX, notebooks separados, Notebook Mestre e
Quarto devem ser tomadas com base nas evidências coletadas durante a
oferta.

O objetivo da experimentação é encontrar um processo que seja
simultaneamente:

-   pedagogicamente claro;
-   simples de executar em sala;
-   simples de manter;
-   reutilizável em futuras ofertas;
-   adequado à integração entre explicação e programação.

------------------------------------------------------------------------

# 10. Prompt para iniciar uma nova semana

Copiar o texto abaixo e substituir `XX` pelo número da semana.

------------------------------------------------------------------------

## PROMPT

Estamos iniciando o desenvolvimento dos materiais da **Semana XX** da
disciplina **EGC5310-EstruturasDados**.

Consulte primeiro o **Plano de Ensino, a ementa e o cronograma da
disciplina** para identificar exatamente o conteúdo previsto para a
Semana XX. Consulte também os **Documentos-Base** do projeto e os
materiais/revisão da semana anterior que forem relevantes para preservar
continuidade e incorporar as evidências obtidas em sala.

Mantenha as decisões arquiteturais e pedagógicas já consolidadas. A
**semana é a unidade didática**, sem separação artificial entre aula
teórica e prática. A narrativa deve partir de um **problema concreto**,
avançando para implementação, análise, formalização, experimentação e
interpretação conforme necessário.

Continuamos experimentando dois formatos de produção:

1.  **PPTX + Notebook Aula + Notebook Estudante**;
2.  **Notebook Mestre como fonte de conteúdo + apresentação gerada com
    Quarto/Reveal.js**.

Não escolha definitivamente um formato sem evidências. Considere as
observações registradas nas semanas anteriores.

Antes de gerar todos os artefatos, apresente:

1.  o conteúdo previsto na ementa/cronograma para a Semana XX;
2.  a relação desse conteúdo com o que já foi trabalhado;
3.  o problema orientador proposto;
4.  os resultados de aprendizagem;
5.  a narrativa didática da semana;
6.  a proposta de distribuição dos aproximadamente **160 minutos úteis
    da semana**;
7.  quais artefatos serão necessários, incluindo se haverá benchmark;
8.  qual dos dois formatos de aula será testado nessa semana e por quê,
    considerando as evidências já registradas.

Após minha validação, avance **um artefato por vez**, seguindo a
nomenclatura oficial:

`EGC5310-EstruturasDados-SXX-01-Roteiro.md`

`EGC5310-EstruturasDados-SXX-02-Slides.pptx` (quando aplicável)

`EGC5310-EstruturasDados-SXX-03-Aula.ipynb`

`EGC5310-EstruturasDados-SXX-04-Estudante.ipynb`

`EGC5310-EstruturasDados-SXX-05-Benchmark.py/.csv/.md` (quando
necessário)

`EGC5310-EstruturasDados-SXX-06-Exercicios.md`

`EGC5310-EstruturasDados-SXX-07-Solucoes.md`

`EGC5310-EstruturasDados-SXX-08-Revisao.md`

Se utilizarmos o **Notebook Mestre + Quarto**, preserve o padrão técnico
já validado no projeto e não reintroduza configurações de formatação no
notebook que possam gerar conflitos com a renderização.

Não redesenhe a arquitetura da disciplina nem crie novos documentos sem
necessidade. O objetivo agora é **produzir e executar a Semana XX** com
base na arquitetura existente e nas evidências das semanas anteriores.

------------------------------------------------------------------------

# 11. Uso deste guia

Este arquivo deve funcionar como memória operacional do processo.

Quando houver dúvida sobre "como produzir a próxima semana", consultar
primeiro:

1.  este guia;
2.  os Documentos-Base;
3.  o Plano de Ensino;
4.  a revisão da semana anterior.

A arquitetura permanece estável. O que deve evoluir é a qualidade dos
materiais e da execução em sala a partir das evidências acumuladas.
