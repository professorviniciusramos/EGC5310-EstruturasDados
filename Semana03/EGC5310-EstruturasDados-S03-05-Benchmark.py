
import time
import statistics
import pandas as pd
import platform

REPETICOES_LISTA = 9
REPETICOES_DF = 3

def medir(funcao, repeticoes=7):
    tempos = []
    for _ in range(repeticoes):
        inicio = time.perf_counter()
        funcao()
        tempos.append(time.perf_counter() - inicio)
    return statistics.median(tempos)

def benchmark_listas():
    tamanhos = [1_000, 10_000, 100_000, 500_000]
    linhas = []

    for n in tamanhos:
        base = list(range(n))

        def testar_append():
            lista = base.copy()
            lista.append(-1)

        def testar_insert_inicio():
            lista = base.copy()
            lista.insert(0, -1)

        def testar_pop_final():
            lista = base.copy()
            lista.pop()

        def testar_pop_inicio():
            lista = base.copy()
            lista.pop(0)

        linhas.extend([
            {"experimento": "lista_insercao", "operacao": "append", "n": n,
             "tempo_s": medir(testar_append, REPETICOES_LISTA)},
            {"experimento": "lista_insercao", "operacao": "insert_inicio", "n": n,
             "tempo_s": medir(testar_insert_inicio, REPETICOES_LISTA)},
            {"experimento": "lista_remocao", "operacao": "pop_final", "n": n,
             "tempo_s": medir(testar_pop_final, REPETICOES_LISTA)},
            {"experimento": "lista_remocao", "operacao": "pop_inicio", "n": n,
             "tempo_s": medir(testar_pop_inicio, REPETICOES_LISTA)},
        ])

    return linhas

def gerar_registros(n):
    return [
        {
            "matricula": i,
            "curso": "CD" if i % 2 == 0 else "CC",
            "nota": (i * 13) % 101 / 10,
        }
        for i in range(n)
    ]

def dataframe_incremental(registros):
    if not registros:
        return pd.DataFrame(columns=["matricula", "curso", "nota"])

    df = pd.DataFrame([registros[0]])

    for registro in registros[1:]:
        novo = pd.DataFrame([registro])
        df = pd.concat([df, novo], ignore_index=True)

    return df

def dataframe_em_lote(registros):
    return pd.DataFrame(registros)

def benchmark_dataframe():
    tamanhos = [100, 500, 1_000, 2_000]
    linhas = []

    for n in tamanhos:
        registros = gerar_registros(n)

        linhas.extend([
            {"experimento": "dataframe_construcao", "operacao": "incremental", "n": n,
             "tempo_s": medir(lambda: dataframe_incremental(registros), REPETICOES_DF)},
            {"experimento": "dataframe_construcao", "operacao": "lote", "n": n,
             "tempo_s": medir(lambda: dataframe_em_lote(registros), REPETICOES_DF)},
        ])

    return linhas

def main():
    linhas = benchmark_listas() + benchmark_dataframe()
    df = pd.DataFrame(linhas)

    df["python"] = platform.python_version()
    df["pandas"] = pd.__version__
    df["plataforma"] = platform.system()

    df.to_csv(
        "EGC5310-EstruturasDados-S03-05-Benchmark.csv",
        index=False
    )

    print(df.to_string(index=False))

if __name__ == "__main__":
    main()
