import pandas as pd

def importar_nodos(path: str):
    return pd.read_csv(path)

def importar_conexiones(path: str):
    df = pd.read_csv(path)
    df['valor_restriccion'] = pd.to_numeric(df['valor_restriccion'], errors='coerce')
    return df

def importar_solicitudes(path: str):
    df = pd.read_csv(path)
    df['peso_kg'] = pd.to_numeric(df['peso_kg'], errors='coerce')
    return df

nodos = importar_nodos('archivos_ejemplo/nodos.csv')
conexiones = importar_conexiones('archivos_ejemplo/conexiones.csv')
solicitudes = importar_solicitudes('archivos_ejemplo/solicitudes.csv')

print(solicitudes)