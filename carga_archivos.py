import csv

def importar_nodos(path: str): # Importa los Nodos/Ciudades como una lista de strings
    nodos = []
    with open(path, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            nombre = fila['nombre'].strip()
            nodos.append(nombre)
    return nodos


def importar_conexiones(path: str) -> list[dict]:
    conexiones = []
    with open(path, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            # Limpieza de campos
            origen = fila['origen'].strip()
            destino = fila['destino'].strip()
            tipo = fila['tipo'].strip()
            distancia_km = float(fila['distancia_km'].strip()) if fila['distancia_km'].strip() else None
            restriccion = fila['restriccion'].strip() if fila['restriccion'] and fila['restriccion'].strip() else None
            valor_str = fila['valor_restriccion'].strip() if fila['valor_restriccion'] else ""

            # Intento de conversión segura
            try:
                valor_restriccion = float(valor_str) if valor_str else None
            except ValueError:
                valor_restriccion = None  # Si no se puede convertir, se ignora

            conexion = {
                'origen': origen,
                'destino': destino,
                'tipo': tipo,
                'distancia_km': distancia_km,
                'restriccion': restriccion,
                'valor_restriccion': valor_restriccion
            }
            conexiones.append(conexion)
    return conexiones


def importar_solicitudes(path: str): # Importa las Solicitudes de la misma manera que las conexiones (lista de diccionarios)
    solicitudes = []
    with open(path, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            solicitud = {
                'id': fila['id_carga'].strip(),
                'peso': float(fila['peso_kg']),
                'origen': fila['origen'].strip(),
                'destino': fila['destino'].strip()
            }
            solicitudes.append(solicitud)
    return solicitudes


try:
    nodos = importar_nodos('archivos_ejemplo/nodos.csv')
    conexiones = importar_conexiones('archivos_ejemplo/conexiones.csv')
    solicitudes = importar_solicitudes('archivos_ejemplo/solicitudes.csv')

    print(solicitudes)
except:
    print('Hubo un error en la ejecucion')