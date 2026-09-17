"""Benchmarks didáticos S06. Uso: python ...py --xlsx 'Online Retail.xlsx'.
Sem --xlsx usa fixture sintética APENAS para testar o roteiro técnico.
"""
import argparse, csv, pathlib, random, statistics, sys, timeit
import numpy as np
import pandas as pd

def sequencial(base, chave):
    for k, v in base:
        if k == chave: return v
    return None

def binaria(base, chave):
    a,b=0,len(base)-1
    while a<=b:
        m=(a+b)//2
        if base[m][0]==chave: return base[m][1]
        if base[m][0]<chave: a=m+1
        else: b=m-1
    return None

def medir(fn): return statistics.median(timeit.repeat(fn, number=1, repeat=3))

def executar(df, destino, origem):
    produtos={}
    for k,v in zip(df.StockCode,df.Description):
        if pd.notna(k) and pd.notna(v): produtos[str(k)]=str(v)
    dados=list(produtos.items())
    rng=random.Random(5310); saida=[]
    for n in [500,2000,4000]:
        base=dados[:min(n,len(dados))]
        ordenada=sorted(base); indice=dict(base); chaves=list(indice)
        perguntas=[chaves[rng.randrange(len(chaves))] if i%2 else 'CODIGO_AUSENTE' for i in range(10000)]
        for nome, prepara, consulta in [
            ('list',lambda:list(base), lambda x:sequencial(base,x)),
            ('ordenada',lambda:sorted(base),lambda x:binaria(ordenada,x)),
            ('dict',lambda:dict(base),lambda x:indice.get(x))]:
            prep=medir(prepara)
            for q in [1,10,100,1000,10000]:
                custo=medir(lambda:[consulta(k) for k in perguntas[:q]])
                saida.append([origem,'busca',len(base),q,nome,prep,custo,prep+custo])
    for n in [1000,10000,100000,min(len(df),500000)]:
        p=df.UnitPrice.fillna(0).to_numpy(dtype=float)[:n]
        q=df.Quantity.fillna(0).to_numpy(dtype=float)[:n]
        lp,lq=p.tolist(),q.tolist()
        py=medir(lambda:sum(lp[i]*lq[i] for i in range(len(lp))))
        npy=medir(lambda:float(np.sum(p*q)))
        saida.extend([[origem,'lote',n,1,'Python',0,py,py],[origem,'lote',n,1,'NumPy',0,npy,npy]])
    with open(destino,'w',newline='',encoding='utf-8') as f:
        w=csv.writer(f);w.writerow(['origem','experimento','n','consultas','estrutura','preparo_s','operacao_s','total_s']);w.writerows(saida)
    print('Geradas',len(saida),'linhas em',destino)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--xlsx',type=pathlib.Path)
    parser.add_argument('--csv',type=pathlib.Path,default=pathlib.Path(__file__).with_suffix('.csv'))
    args=parser.parse_args()
    if args.xlsx:
        df=pd.read_excel(args.xlsx,engine='openpyxl'); origem='UCI Online Retail'
    else:
        rng=random.Random(5310)
        n=12000
        df=pd.DataFrame({'StockCode':[f'{i%4000:05d}' for i in range(n)],'Description':['Produto']*n,'Quantity':[rng.randint(1,10) for _ in range(n)],'UnitPrice':[rng.random()*10 for _ in range(n)]}); origem='fixture sintética; NÃO são resultados UCI'
    executar(df,args.csv,origem)
