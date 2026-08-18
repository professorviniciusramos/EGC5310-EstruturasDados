import csv
import random
import statistics
import time
from bisect import bisect_left
from pathlib import Path

OUTPUT = Path(__file__).with_name("EGC5310-EstruturasDados-S02-05-Benchmark.csv")

SIZES = [100, 1_000, 10_000, 100_000]
REPEATS = 7
LOOKUPS_PER_REPEAT = 200

def build_data(n):
    lista = [
        {
            "matricula": i,
            "nome": f"Estudante {i}",
            "curso": "CD" if i % 5 == 0 else "Outro",
        }
        for i in range(n)
    ]

    dicionario = {
        e["matricula"]: {
            "nome": e["nome"],
            "curso": e["curso"],
        }
        for e in lista
    }

    matriculas_ordenadas = [e["matricula"] for e in lista]

    return lista, dicionario, matriculas_ordenadas

def busca_lista(lista, alvo):
    for estudante in lista:
        if estudante["matricula"] == alvo:
            return estudante
    return None

def busca_bisect(matriculas, alvo):
    pos = bisect_left(matriculas, alvo)
    if pos < len(matriculas) and matriculas[pos] == alvo:
        return matriculas[pos]
    return None

def filtro_curso_lista(lista, curso):
    return [e for e in lista if e["curso"] == curso]

def filtro_curso_dict(dicionario, curso):
    return [
        (matricula, estudante)
        for matricula, estudante in dicionario.items()
        if estudante["curso"] == curso
    ]

def tempo_medio_ns(func, *args, repeats=REPEATS, calls=1):
    amostras = []

    for _ in range(repeats):
        inicio = time.perf_counter_ns()
        for _ in range(calls):
            func(*args)
        fim = time.perf_counter_ns()
        amostras.append((fim - inicio) / calls)

    return statistics.median(amostras)

def main():
    random.seed(5310)
    rows = []

    for n in SIZES:
        lista, dicionario, matriculas = build_data(n)

        # Busca por matrícula: usa alvos existentes em posições variadas.
        alvos = [random.randrange(n) for _ in range(LOOKUPS_PER_REPEAT)]

        def executar_buscas_lista():
            for alvo in alvos:
                busca_lista(lista, alvo)

        def executar_buscas_dict():
            for alvo in alvos:
                dicionario.get(alvo)

        def executar_buscas_bisect():
            for alvo in alvos:
                busca_bisect(matriculas, alvo)

        # Cada função abaixo já executa LOOKUPS_PER_REPEAT buscas.
        t_lista = tempo_medio_ns(executar_buscas_lista)
        t_dict = tempo_medio_ns(executar_buscas_dict)
        t_bisect = tempo_medio_ns(executar_buscas_bisect)

        rows.extend([
            {
                "n": n,
                "operacao": "buscar_matricula",
                "representacao": "lista_busca_sequencial",
                "tempo_mediano_ns_por_lote": round(t_lista, 2),
                "operacoes_por_lote": LOOKUPS_PER_REPEAT,
                "tempo_aprox_ns_por_operacao": round(t_lista / LOOKUPS_PER_REPEAT, 2),
            },
            {
                "n": n,
                "operacao": "buscar_matricula",
                "representacao": "dicionario_por_chave",
                "tempo_mediano_ns_por_lote": round(t_dict, 2),
                "operacoes_por_lote": LOOKUPS_PER_REPEAT,
                "tempo_aprox_ns_por_operacao": round(t_dict / LOOKUPS_PER_REPEAT, 2),
            },
            {
                "n": n,
                "operacao": "buscar_matricula",
                "representacao": "lista_ordenada_bisect",
                "tempo_mediano_ns_por_lote": round(t_bisect, 2),
                "operacoes_por_lote": LOOKUPS_PER_REPEAT,
                "tempo_aprox_ns_por_operacao": round(t_bisect / LOOKUPS_PER_REPEAT, 2),
            },
        ])

        # Filtro por curso: operação que exige examinar a coleção em ambas.
        t_filtro_lista = tempo_medio_ns(filtro_curso_lista, lista, "CD")
        t_filtro_dict = tempo_medio_ns(filtro_curso_dict, dicionario, "CD")

        rows.extend([
            {
                "n": n,
                "operacao": "listar_por_curso",
                "representacao": "lista",
                "tempo_mediano_ns_por_lote": round(t_filtro_lista, 2),
                "operacoes_por_lote": 1,
                "tempo_aprox_ns_por_operacao": round(t_filtro_lista, 2),
            },
            {
                "n": n,
                "operacao": "listar_por_curso",
                "representacao": "dicionario",
                "tempo_mediano_ns_por_lote": round(t_filtro_dict, 2),
                "operacoes_por_lote": 1,
                "tempo_aprox_ns_por_operacao": round(t_filtro_dict, 2),
            },
        ])

    with OUTPUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "n",
                "operacao",
                "representacao",
                "tempo_mediano_ns_por_lote",
                "operacoes_por_lote",
                "tempo_aprox_ns_por_operacao",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Benchmark concluído. Resultados em: {OUTPUT}")

if __name__ == "__main__":
    main()
