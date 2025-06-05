import csv
from clase_ciudad import Ciudad
from clase_solicitud import Solicitud
from conexiones import *

def importar_nodos(path: str): # Importa los Nodos/Ciudades como una lista de strings
    nodos = []
    with open(path, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            nombre = fila['nombre'].strip()
            nodos.append(nombre)
    return nodos


def importar_conexiones(path: str): # Importa las conexiones como lista de diccionarios donde cada diccionario tiene en forma de clave-valor todos los datos de cada conexion
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


def construir_ciudades(lista_nombres: list[str]): # Toma el diccionario de importar_nodos() y genera un diccionario con las ciudades generadas
    return {nombre: Ciudad(nombre) for nombre in lista_nombres}


def construir_conexiones(lista_conexiones: list[dict], ciudades: list[dict]): # Toma la lista de diccionarios de importacion_conexiones() y el diccionario con las ciudades ya creadas, y crea una lista con todas las instancias de conexiones
    instancias = []
    for c in lista_conexiones:
        ciudad1 = ciudades[c['origen']]
        ciudad2 = ciudades[c['destino']]
        distancia = int(c['distancia_km'])
        tipo = c['tipo'].lower()

        if tipo == "ferroviaria":
            conexion = Conexion_ferroviaria(ciudad1, ciudad2, distancia)
        elif tipo == "automotor":
            conexion = Conexion_autovia(ciudad1, ciudad2, distancia)
        elif tipo == "fluvial":
            conexion = Conexion_maritima(ciudad1, ciudad2, distancia)
        elif tipo == "aerea" or tipo == "aérea":
            conexion = Conexion_aerea(ciudad1, ciudad2, distancia)
        else:
            raise ValueError(f"Tipo de conexión desconocido: {tipo}")

        instancias.append(conexion)
    return instancias


def construir_solicitudes(lista_solicitudes: list[dict]): # Toma la lista de diccionarios de importar_solicitudes() y genera una lista de solicitudes
    return [
        Solicitud(
            s['id'],
            s['peso'],
            s['origen'],
            s['destino'])
        for s in lista_solicitudes
    ]


try:
    # Importo los datos
    nodos = importar_nodos('archivos_ejemplo/nodos.csv')
    conexiones = importar_conexiones('archivos_ejemplo/conexiones.csv')
    solicitudes = importar_solicitudes('archivos_ejemplo/solicitudes.csv')
    print(solicitudes)

    # Creo las instancias
    ciudades = construir_ciudades(nodos)
    lista_conexiones =  construir_conexiones(conexiones, ciudades)
    lista_solicitudes = construir_solicitudes(solicitudes)

    print(ciudades)
    print(lista_conexiones)
    print(lista_solicitudes)
except:
    print('Hubo un error en la ejecucion')

print(lista_conexiones)