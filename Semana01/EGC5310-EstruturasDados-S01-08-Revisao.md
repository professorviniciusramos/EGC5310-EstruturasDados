# EGC5310-EstruturasDados-S01-08-Revisao

**Disciplina:** EGC5310 — Tópicos Especiais em Ciência de Dados VI  
**Projeto pedagógico:** Estruturas de Dados  
**Semana:** S01  
**Artefato:** 08 — Revisão  
**Versão:** 2.0  
**Status:** Pronta para execução  
**Última revisão:** 11/08/2026

## 1. Objetivo

Este documento registra a revisão de consistência da Semana 01, considerando as decisões pedagógicas, operacionais e de organização consolidadas até a véspera da primeira aula.

## 2. Estado geral

A Semana 01 segue a narrativa:

**problema → busca sequencial → contagem de comparações → tamanho da entrada → melhor/pior caso → T(n) → O(n) → tempo observado → experimento → limitação → nova pergunta**

A semana é uma sequência contínua, sem separação rígida entre teoria e prática.

## 3. Convenções vigentes

**Repositório:** `EGC5310-EstruturasDados`

**Padrão de nomes:** `EGC5310-EstruturasDados-SXX-NN-Nome.ext`

Arquivos da Semana 01:

- `EGC5310-EstruturasDados-S01-01-Roteiro.md`
- `EGC5310-EstruturasDados-S01-02-Slides.pptx`
- `EGC5310-EstruturasDados-S01-03-Aula.ipynb`
- `EGC5310-EstruturasDados-S01-04-Estudante.ipynb`
- `EGC5310-EstruturasDados-S01-05-Benchmark.py`
- `EGC5310-EstruturasDados-S01-05-Benchmark.csv`
- `EGC5310-EstruturasDados-S01-05-Benchmark.md`
- `EGC5310-EstruturasDados-S01-06-Exercicios.md`
- `EGC5310-EstruturasDados-S01-07-Solucoes.md`
- `EGC5310-EstruturasDados-S01-08-Revisao.md`

**Ambiente computacional:** Google Colab  
**Acesso inicial:** AVA  
**GitHub:** evolução posterior

## 4. Roteiro

- [x] Semana tratada como sequência única.
- [x] Problema orientador claro.
- [x] Busca sequencial usada como exemplo introdutório.
- [x] Integra slides, Colab, atividades e benchmark.
- [x] Ritmo flexível.
- [x] Prevê interrupção e retomada.

**Status:** consistente.

## 5. Apresentação institucional

- [x] Disciplina e professor.
- [x] Objetivos e metodologia.
- [x] AVA e Google Colab.
- [x] GitHub como evolução futura.
- [x] Avaliação.
- [x] Aprovação com **MF ≥ 6,0**.
- [x] Frequência mínima de **75%**.
- [x] Sem REC.

**Status:** pronta para uso.

## 6. Slides da Semana 01

Os 17 slides formam uma única sequência para toda a semana.

- [x] Podem ser interrompidos em qualquer ponto.
- [x] Podem ser retomados no encontro seguinte.
- [x] Integram discussão, Colab e atividades.
- [x] Não exigem conclusão integral no primeiro encontro.

**Status:** especificação pedagógica validada; finalização visual externa.

## 7. Notebook Aula

Arquivo: `EGC5310-EstruturasDados-S01-03-Aula.ipynb`

- [x] Busca sequencial.
- [x] Contagem de comparações.
- [x] Melhor e pior caso.
- [x] T(n) e O(n).
- [x] Tempo observado.
- [x] Experimento de crescimento.
- [x] Funcionamento validado.

**Status:** pronto.

## 8. Notebook Estudante

Arquivo: `EGC5310-EstruturasDados-S01-04-Estudante.ipynb`

- [x] Derivado do notebook Aula.
- [x] Mantém o mesmo cenário.
- [x] Possui TODOs.
- [x] Possui espaços de interpretação.
- [x] Inclui experimento e conclusão.

**Status:** pronto.

## 9. Benchmark

Arquivos:

- `EGC5310-EstruturasDados-S01-05-Benchmark.py`
- `EGC5310-EstruturasDados-S01-05-Benchmark.md`

- [x] Pior caso garantido por matrícula inexistente.
- [x] Comparações = n.
- [x] Mede tempos.
- [x] Documento MD possui leitura pré-aula.
- [x] Distingue benchmark de Big-O.

**Status:** pronto.

## 10. Exercícios

Arquivo: `EGC5310-EstruturasDados-S01-06-Exercicios.md`

Cobertura:

- busca passo a passo;
- instrumentação;
- predição;
- T(n);
- O(1), O(n), O(n²);
- tempo versus Big-O;
- adequação da solução;
- mini-investigação.

**Status:** consistente.

## 11. Soluções

Arquivo: `EGC5310-EstruturasDados-S01-07-Solucoes.md`

- [x] Todas as atividades possuem solução.
- [x] Há raciocínio esperado.
- [x] Há erros comuns.
- [x] Tempos não são tratados como respostas únicas.

**Status:** consistente.

## 12. Coerência entre artefatos

Todos os materiais utilizam o mesmo cenário:

**buscar um estudante pela matrícula em uma coleção acadêmica.**

Todos convergem para:

- tamanho da entrada;
- número de operações;
- melhor/pior caso;
- crescimento linear;
- O(n);
- tempo observado;
- necessidade de reconsiderar a organização dos dados.

Pergunta final:

> **Podemos organizar os dados de outra maneira para reduzir o custo da operação?**

**Status:** consistente.

## 13. Pendências antes da primeira aula

### Obrigatórias

- [ ] Renomear fisicamente os arquivos.
- [ ] Organizar a pasta `Semana01`.
- [ ] Subir materiais para o repositório.
- [ ] Colocar no AVA os links dos Colabs.
- [ ] Testar os links em modo estudante.
- [ ] Disponibilizar a apresentação institucional.
- [ ] Disponibilizar o PPTX final da Semana 01.

### Recomendadas

- [ ] Executar o notebook Aula uma vez no Colab.
- [ ] Abrir o notebook Estudante por link limpo.
- [ ] Testar compartilhamento em navegador anônimo.
- [ ] Manter cópia local dos notebooks.
- [ ] Manter slides também localmente.

## 14. Itens que não bloqueiam a Semana 01

Podem ser adiados:

- autocorreção via GitHub;
- GitHub Classroom;
- notebook integrado;
- conversão notebook → apresentação;
- refinamentos de arquitetura;
- automação de releases.

## 15. Critério de sucesso operacional

A semana está pronta quando:

1. professor abre a apresentação;
2. professor abre o notebook Aula;
3. estudantes abrem o notebook Estudante;
4. links do AVA funcionam;
5. a aula pode ocorrer mesmo sem GitHub finalizado.

## 16. Critério de sucesso pedagógico

A Semana 01 cumpre sua função se os estudantes conseguirem explicar que uma busca sequencial pode estar correta, mas no pior caso examina `n` elementos, apresenta crescimento linear `O(n)`, e que tempo medido não é a própria complexidade.

## 17. Estado final

- Planejamento pedagógico: **PRONTO**
- Materiais computacionais: **PRONTOS**
- Exercícios e soluções: **PRONTOS**
- Benchmark: **PRONTO**
- Apresentação institucional: **PRONTA**
- Slides da Semana 01: **EM FINALIZAÇÃO VISUAL**
- Repositório: **EM ORGANIZAÇÃO**
- AVA: **EM PUBLICAÇÃO**

## 18. Decisão final

A Semana 01 entra agora em **modo de execução**.

Novas mudanças de arquitetura, nomenclatura ou metodologia só devem ocorrer se forem necessárias para viabilizar a aula.

Melhorias não essenciais devem ser registradas para revisão posterior.

**Versão:** 2.0  
**Status:** Pronta para execução
