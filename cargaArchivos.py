import pandas as pd

def leer_csv(ruta_archivo, separador=',', codificacion='utf-8', decimal='.', columnas=None):
    """
    Lee un archivo CSV y devuelve un DataFrame de Pandas.

    Parámetros:
    - ruta_archivo (str): Ruta al archivo CSV.
    - separador (str): Caracter que separa las columnas (por defecto ',').
    - codificacion (str): Codificación del archivo (por defecto 'utf-8').
    - decimal (str): Separador decimal, útil para números con ',' (por defecto '.').
    - columnas (list[str]): Lista opcional de columnas a importar.

    Retorna:
    - DataFrame con los datos del archivo.
    """
    try:
        df = pd.read_csv(ruta_archivo, sep=separador, encoding=codificacion, decimal=decimal, usecols=columnas)
        return df
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

""" PRUEBA """

df = leer_csv('archivos_ejemplo/conexiones.csv', separador=',', decimal='.')

if df is not None:
    df.fillna('None', inplace=True)
    print(df.head())
