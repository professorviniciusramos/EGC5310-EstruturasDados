#!/usr/bin/env python3
"""Benchmark didático da S04: busca sequencial × busca binária.

Produz EGC5310-EstruturasDados-S04-05-Benchmark.csv no mesmo diretório.
"""
from __future__ import annotations

import csv
import statistics
import time
from pathlib import Path

TAMANHOS = [100, 1_000, 10_000, 100_000, 1_000_000]
REPETICOES = 11
SAIDA = Path(__file__).with_name("EGC5310-EstruturasDados-S04-05-Benchmark.csv")


def busca_sequencial(dados, alvo):
    comparacoes = 0
    for indice, valor in enumerate(dados):
        comparacoes += 1
        if valor == alvo:
            return indice, comparacoes
    return -1, comparacoes


def busca_binaria(dados, alvo):
    inicio, fim, comparacoes = 0, len(dados) - 1, 0
    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1
        if dados[meio] == alvo:
            return meio, comparacoes
        if dados[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1, comparacoes


def medir(funcao, dados, alvo):
    tempos = []
    retorno = None
    for _ in range(REPETICOES):
        inicio = time.perf_counter_ns()
        retorno = funcao(dados, alvo)
        tempos.append(time.perf_counter_ns() - inicio)
    indice, comparacoes = retorno
    return indice, comparacoes, int(statistics.median(tempos)), min(tempos), max(tempos)


def main():
    linhas = []
    for n in TAMANHOS:
        dados = list(range(n))
        casos = [("ultimo", n - 1), ("inexistente", -1)]
        for caso, alvo in casos:
            esperado = n - 1 if caso == "ultimo" else -1
            for algoritmo, funcao in [("sequencial", busca_sequencial), ("binaria", busca_binaria)]:
                indice, comparacoes, mediana, minimo, maximo = medir(funcao, dados, alvo)
                assert indice == esperado
                linhas.append({
                    "n": n, "caso": caso, "algoritmo": algoritmo,
                    "comparacoes": comparacoes, "repeticoes": REPETICOES,
                    "tempo_ns_mediano": mediana, "tempo_ns_min": minimo,
                    "tempo_ns_max": maximo,
                })
    with SAIDA.open("w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=linhas[0].keys())
        escritor.writeheader(); escritor.writerows(linhas)
    print(f"{len(linhas)} linhas gravadas em {SAIDA.name}")


if __name__ == "__main__":
    main()
