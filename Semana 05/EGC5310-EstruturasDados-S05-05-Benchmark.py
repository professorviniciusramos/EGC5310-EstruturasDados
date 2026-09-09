#!/usr/bin/env python3
"""Benchmark didático da S05: distribuição, colisões e custo de busca.

Produz EGC5310-EstruturasDados-S05-05-Benchmark.csv no mesmo diretório.
O objetivo é observar o mecanismo de colisão em uma tabela hash didática
com encadeamento, sem antecipar a comparação completa da Semana 06.
"""
from __future__ import annotations

import csv
import statistics
import time
from pathlib import Path

TAMANHOS = [100, 1_000, 10_000, 100_000]
REPETICOES = 11
SAIDA = Path(__file__).with_name("EGC5310-EstruturasDados-S05-05-Benchmark.csv")


def criar_tabela(tamanho: int) -> list[list[int]]:
    """Cria buckets independentes para encadeamento separado."""
    return [[] for _ in range(tamanho)]


def inserir(tabela: list[list[int]], chave: int) -> None:
    posicao = chave % len(tabela)
    tabela[posicao].append(chave)


def buscar_contando(tabela: list[list[int]], chave: int) -> tuple[bool, int]:
    """Retorna se encontrou e quantas chaves do bucket foram comparadas."""
    posicao = chave % len(tabela)
    comparacoes = 0
    for chave_existente in tabela[posicao]:
        comparacoes += 1
        if chave_existente == chave:
            return True, comparacoes
    return False, comparacoes


def construir(chaves: list[int], tamanho_tabela: int) -> tuple[list[list[int]], int]:
    inicio = time.perf_counter_ns()
    tabela = criar_tabela(tamanho_tabela)
    for chave in chaves:
        inserir(tabela, chave)
    tempo = time.perf_counter_ns() - inicio
    return tabela, tempo


def medir_busca(
    tabela: list[list[int]], chave: int
) -> tuple[bool, int, int, int, int]:
    tempos: list[int] = []
    retorno: tuple[bool, int] | None = None

    for _ in range(REPETICOES):
        inicio = time.perf_counter_ns()
        retorno = buscar_contando(tabela, chave)
        tempos.append(time.perf_counter_ns() - inicio)

    assert retorno is not None
    encontrado, comparacoes = retorno
    return (
        encontrado,
        comparacoes,
        int(statistics.median(tempos)),
        min(tempos),
        max(tempos),
    )


def estatisticas_buckets(tabela: list[list[int]]) -> tuple[int, int, float, int]:
    comprimentos = [len(bucket) for bucket in tabela]
    ocupados = [comprimento for comprimento in comprimentos if comprimento > 0]
    colisoes = sum(max(0, comprimento - 1) for comprimento in comprimentos)
    media_ocupados = statistics.mean(ocupados) if ocupados else 0.0
    return colisoes, len(ocupados), media_ocupados, max(comprimentos, default=0)


def gerar_chaves(n: int, cenario: str) -> list[int]:
    if cenario == "distribuidas":
        return list(range(n))
    if cenario == "concentradas":
        # Todas produzem resto 2 quando divididas por n.
        return [indice * n + 2 for indice in range(n)]
    raise ValueError(f"Cenário desconhecido: {cenario}")


def main() -> None:
    linhas: list[dict[str, int | float | str | bool]] = []

    for n in TAMANHOS:
        for cenario in ["distribuidas", "concentradas"]:
            chaves = gerar_chaves(n, cenario)
            tabela, tempo_construcao = construir(chaves, tamanho_tabela=n)
            colisoes, ocupados, media, maior_bucket = estatisticas_buckets(tabela)

            casos = [
                ("existente_ultimo", chaves[-1], True),
                ("inexistente_mesmo_bucket", n * n + 2, False),
            ]

            for caso, alvo, esperado in casos:
                encontrado, comparacoes, mediana, minimo, maximo = medir_busca(
                    tabela, alvo
                )
                assert encontrado == esperado
                linhas.append(
                    {
                        "n": n,
                        "cenario": cenario,
                        "tamanho_tabela": n,
                        "taxa_carga": 1.0,
                        "colisoes": colisoes,
                        "buckets_ocupados": ocupados,
                        "comprimento_medio_buckets_ocupados": round(media, 2),
                        "maior_bucket": maior_bucket,
                        "caso_busca": caso,
                        "comparacoes": comparacoes,
                        "repeticoes": REPETICOES,
                        "tempo_construcao_ns": tempo_construcao,
                        "tempo_busca_ns_mediano": mediana,
                        "tempo_busca_ns_min": minimo,
                        "tempo_busca_ns_max": maximo,
                    }
                )

    with SAIDA.open("w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=linhas[0].keys())
        escritor.writeheader()
        escritor.writerows(linhas)

    print(f"{len(linhas)} linhas gravadas em {SAIDA.name}")


if __name__ == "__main__":
    main()

