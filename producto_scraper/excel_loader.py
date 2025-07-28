import pandas as pd

def cargar_codigos(path_excel):
    df = pd.read_excel(path_excel)
    return df["CODIGO"].astype(str).tolist()
