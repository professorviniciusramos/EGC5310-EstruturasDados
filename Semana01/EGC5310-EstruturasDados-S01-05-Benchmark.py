"""
EGC5310 — Semana 01
Benchmark: crescimento da busca sequencial no pior caso

Objetivo
--------
Relacionar tamanho da entrada, número de comparações e tempo observado
para a busca sequencial no pior caso.

O experimento usa matrícula inexistente para garantir que todos os n
registros sejam examinados.

Arquivo: Semana-01-Benchmark.py
"""

from time import perf_counter
from statistics import median
from csv import DictWriter
from pathlib import Path


TAMANHOS = [1_000, 10_000, 100_000, 1_000_000]
REPETICOES = 7
AQUECIMENTOS = 2


def gerar_estudantes(n):
    """Gera n registros acadêmicos sintéticos."""
    return [
        {
            "matricula": 100000 + i,
            "nome": f"Estudante {i:06d}",
            "curso": "Ciência de Dados" if i % 3 else "Engenharia",
        }
        for i in range(n)
    ]


def buscar(estudantes, matricula):
    """Busca sequencial simples."""
    for estudante in estudantes:
        if estudante["matricula"] == matricula:
            return estudante
    return None


def buscar_contando(estudantes, matricula):
    """Busca sequencial instrumentada com contagem de comparações."""
    comparacoes = 0

    for estudante in estudantes:
        comparacoes += 1
        if estudante["matricula"] == matricula:
            return estudante, comparacoes

    return None, comparacoes


def medir_tempo(dados, matricula, repeticoes=REPETICOES, aquecimentos=AQUECIMENTOS):
    """Retorna a mediana do tempo de execução após execuções de aquecimento."""
    for _ in range(aquecimentos):
        buscar(dados, matricula)

    tempos = []
    for _ in range(repeticoes):
        inicio = perf_counter()
        buscar(dados, matricula)
        tempos.append(perf_counter() - inicio)

    return median(tempos), tempos


def executar_benchmark():
    """Executa o benchmark principal da Semana 01."""
    resultados = []

    for n in TAMANHOS:
        dados = gerar_estudantes(n)

        # Matrícula impossível nos dados gerados: garante pior caso.
        matricula_inexistente = -1

        _, comparacoes = buscar_contando(dados, matricula_inexistente)
        tempo_mediano, tempos = medir_tempo(dados, matricula_inexistente)

        resultados.append(
            {
                "n": n,
                "comparacoes": comparacoes,
                "tempo_mediano_s": tempo_mediano,
                "tempo_min_s": min(tempos),
                "tempo_max_s": max(tempos),
            }
        )

        # Libera explicitamente a coleção antes do próximo tamanho.
        del dados

    return resultados


def imprimir_resultados(resultados):
    print("\nEGC5310 — Semana 01")
    print("Benchmark da busca sequencial — pior caso\n")

    cabecalho = (
        f"{'n':>12} | {'comparações':>12} | "
        f"{'tempo mediano (s)':>18} | {'mín (s)':>10} | {'máx (s)':>10}"
    )
    print(cabecalho)
    print("-" * len(cabecalho))

    for r in resultados:
        print(
            f"{r['n']:>12,d} | "
            f"{r['comparacoes']:>12,d} | "
            f"{r['tempo_mediano_s']:>18.8f} | "
            f"{r['tempo_min_s']:>10.8f} | "
            f"{r['tempo_max_s']:>10.8f}"
        )

    print("\nRazões de crescimento")
    print("-" * 72)

    for anterior, atual in zip(resultados, resultados[1:]):
        razao_n = atual["n"] / anterior["n"]
        razao_comp = atual["comparacoes"] / anterior["comparacoes"]
        razao_tempo = atual["tempo_mediano_s"] / anterior["tempo_mediano_s"]

        print(
            f"{anterior['n']:>9,d} → {atual['n']:>9,d}: "
            f"n ×{razao_n:>4.1f} | "
            f"comparações ×{razao_comp:>4.1f} | "
            f"tempo ×{razao_tempo:>6.2f}"
        )

    print("\nInterpretação esperada")
    print("-" * 72)
    print(
        "• No pior caso, comparações = n.\n"
        "• Quando n é multiplicado por 10, o número de comparações também é.\n"
        "• O padrão estrutural observado é linear: O(n).\n"
        "• O tempo tende a aumentar com n, mas sua razão pode oscilar entre execuções.\n"
        "• Portanto, tempo observado e ordem de crescimento não são equivalentes."
    )


def salvar_csv(resultados, caminho="Semana-01-Benchmark-Resultados.csv"):
    """Salva os resultados brutos do benchmark."""
    campos = [
        "n",
        "comparacoes",
        "tempo_mediano_s",
        "tempo_min_s",
        "tempo_max_s",
    ]

    with open(caminho, "w", newline="", encoding="utf-8") as arquivo:
        writer = DictWriter(arquivo, fieldnames=campos)
        writer.writeheader()
        writer.writerows(resultados)

    return Path(caminho)


if __name__ == "__main__":
    resultados = executar_benchmark()
    imprimir_resultados(resultados)
    caminho_csv = salvar_csv(resultados)
    print(f"\nResultados salvos em: {caminho_csv}")
