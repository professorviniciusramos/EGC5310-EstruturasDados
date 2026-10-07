"""
EGC5310 — Semana 09
Benchmark: estratégias de merge/join

Compara:
1. nested-loop;
2. hash join (construção + consulta);
3. hash join com índice previamente construído;
4. sort-merge (ordenação + percurso);
5. sort-merge com dados previamente ordenados.

O objetivo é didático: distinguir custo de preparação do custo de junção.
"""

from __future__ import annotations

import csv
import gc
import random
import statistics
import time
from pathlib import Path

TAMANHOS = [500, 1_000, 2_500, 5_000, 10_000]
REPETICOES = 5
SEMENTE = 5310

ARQUIVO_RESULTADOS = Path(__file__).with_name(
    "EGC5310-EstruturasDados-S09-06-Benchmark-Resultados.csv"
)


def gerar_dados(n: int, semente: int):
    """Gera duas coleções com as mesmas chaves, mas em ordens independentes."""
    rng = random.Random(semente)

    chaves_esquerda = list(range(n))
    chaves_direita = list(range(n))
    rng.shuffle(chaves_esquerda)
    rng.shuffle(chaves_direita)

    esquerda = [(chave, chave * 2) for chave in chaves_esquerda]
    direita = [(chave, chave * 3) for chave in chaves_direita]

    return esquerda, direita


def nested_loop(esquerda, direita):
    """Procura cada chave da esquerda percorrendo a direita."""
    resultado = []

    for chave_e, valor_e in esquerda:
        for chave_d, valor_d in direita:
            if chave_e == chave_d:
                resultado.append((chave_e, valor_e, valor_d))
                break

    return resultado


def construir_indice_hash(direita):
    """Custo de preparação do hash join."""
    return {chave: valor for chave, valor in direita}


def consultar_indice_hash(esquerda, indice):
    """Fase de consulta quando o índice já está disponível."""
    resultado = []

    for chave, valor_e in esquerda:
        if chave in indice:
            resultado.append((chave, valor_e, indice[chave]))

    return resultado


def hash_join(esquerda, direita):
    """Hash join completo: construir índice + consultar."""
    indice = construir_indice_hash(direita)
    return consultar_indice_hash(esquerda, indice)


def ordenar_dados(esquerda, direita):
    """Custo de preparação do sort-merge."""
    esquerda_ord = sorted(esquerda, key=lambda registro: registro[0])
    direita_ord = sorted(direita, key=lambda registro: registro[0])
    return esquerda_ord, direita_ord


def percorrer_sort_merge(esquerda_ord, direita_ord):
    """Percorre duas coleções que JÁ estão ordenadas."""
    resultado = []
    i = 0
    j = 0

    while i < len(esquerda_ord) and j < len(direita_ord):
        chave_e, valor_e = esquerda_ord[i]
        chave_d, valor_d = direita_ord[j]

        if chave_e == chave_d:
            resultado.append((chave_e, valor_e, valor_d))
            i += 1
            j += 1
        elif chave_e < chave_d:
            i += 1
        else:
            j += 1

    return resultado


def sort_merge(esquerda, direita):
    """Sort-merge completo: ordenar + percorrer."""
    esquerda_ord, direita_ord = ordenar_dados(esquerda, direita)
    return percorrer_sort_merge(esquerda_ord, direita_ord)


def medir(funcao, *args):
    """Mede uma única execução usando relógio de alta resolução."""
    gc.collect()
    inicio = time.perf_counter()
    resultado = funcao(*args)
    fim = time.perf_counter()
    return fim - inicio, resultado


def validar_resultado(resultado, n):
    """Evita comparar implementações que produzam resultados incorretos."""
    if len(resultado) != n:
        raise RuntimeError(
            f"Resultado incorreto: esperado {n} correspondências, "
            f"obtidas {len(resultado)}."
        )


def resumir_tempos(tempos):
    """Mediana reduz a influência de uma execução ocasionalmente ruidosa."""
    return {
        "mediana_s": statistics.median(tempos),
        "min_s": min(tempos),
        "max_s": max(tempos),
    }


def executar():
    linhas = []

    for n in TAMANHOS:
        esquerda, direita = gerar_dados(n, SEMENTE + n)

        # Preparações feitas fora das medições dos cenários "já preparado".
        indice_pronto = construir_indice_hash(direita)
        esquerda_ord, direita_ord = ordenar_dados(esquerda, direita)

        cenarios = [
            ("nested_loop", nested_loop, (esquerda, direita)),
            ("hash_completo", hash_join, (esquerda, direita)),
            ("hash_indice_pronto", consultar_indice_hash, (esquerda, indice_pronto)),
            ("sort_merge_completo", sort_merge, (esquerda, direita)),
            (
                "sort_merge_ja_ordenado",
                percorrer_sort_merge,
                (esquerda_ord, direita_ord),
            ),
        ]

        print(f"\n=== n = {n:,} ===".replace(",", "."))

        for nome, funcao, argumentos in cenarios:
            tempos = []

            for _ in range(REPETICOES):
                tempo, resultado = medir(funcao, *argumentos)
                validar_resultado(resultado, n)
                tempos.append(tempo)

            resumo = resumir_tempos(tempos)

            linha = {
                "n": n,
                "cenario": nome,
                "repeticoes": REPETICOES,
                **resumo,
            }
            linhas.append(linha)

            print(
                f"{nome:24s} "
                f"mediana={resumo['mediana_s']:.6f}s "
                f"min={resumo['min_s']:.6f}s "
                f"max={resumo['max_s']:.6f}s"
            )

    with ARQUIVO_RESULTADOS.open("w", newline="", encoding="utf-8") as arquivo:
        campos = ["n", "cenario", "repeticoes", "mediana_s", "min_s", "max_s"]
        writer = csv.DictWriter(arquivo, fieldnames=campos)
        writer.writeheader()
        writer.writerows(linhas)

    print(f"\nResultados gravados em: {ARQUIVO_RESULTADOS}")


if __name__ == "__main__":
    executar()
