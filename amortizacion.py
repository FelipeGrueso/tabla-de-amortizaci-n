import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def tabla(capital, tasa, plazo, seguro = 0):
    cuota = round(capital / ((((1+tasa)** plazo)-1)/(tasa * (1 + tasa)** plazo)), 2)
    df = pd.DataFrame()
    df["Capital"] = None
    df["Intereses"] = None
    df["Cuota"] = None
##    df["Seguro"] = None
    df["Saldo"] = None
    fila0 = { 'Capital': float(capital), 'Intereses': 0, "Cuota": 0, "Saldo": float(capital)}#, "Seguro": 0}
    df = df.append(fila0, ignore_index=True)

    
    for i in range(plazo):
        nueva_fila = { 'Capital': capital, 'Intereses': round(capital * tasa, 2), "Cuota": cuota, "Saldo": round(capital + (capital * tasa) - cuota, 2)}#, "Seguro": seguro}
        df = df.append(nueva_fila, ignore_index=True)
        capital = nueva_fila["Saldo"]


    print(df)
    
    fig, ax =plt.subplots(figsize=(12,4))
    ax.axis('tight')
    ax.axis('off')
    the_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center')


    pp = PdfPages("Tabla de amortización.pdf")
    pp.savefig(fig, bbox_inches='tight')
    pp.close()

tabla(5000000, 0.05, 6 )
