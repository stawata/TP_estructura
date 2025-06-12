import math
from models.vehiculos import *
from models.conexiones import *
from models.nodo import *
from collections import defaultdict

def calcular_vehiculos_requeridos(peso_carga, capacidad_vehiculo):
    return math.ceil(peso_carga / capacidad_vehiculo)

def calcular_tiempo(distancia, velocidad):
    return distancia / velocidad 

def calcular_costo_tramo(distancia, peso, vehiculo):
    cant_veh = calcular_vehiculos_requeridos(peso, vehiculo.capacidad)
    return cant_veh * (
        vehiculo.costo_fijo +
        vehiculo.costo_km * distancia +
        vehiculo.costo_kg * peso
    )

def construir_grafo(conexiones, nodos):
    """
    Construye un grafo dirigido a partir de las conexiones.
    
    Parámetros:
        conexiones (list[Conexion]): Lista de objetos conexión.
        nodos_dict (dict[str, Nodo]): Diccionario de nodos por nombre.

    Retorna:
        dict[str, list[Conexion]]: Grafo donde cada nodo apunta a las conexiones salientes.
    """
    nodos_dict = {n.nombre: n for n in nodos}
    grafo = defaultdict(list)
    for conexion in conexiones:
        if conexion.origen in nodos_dict and conexion.destino in nodos_dict:
            grafo[conexion.origen].append(conexion)
    return grafo

def obtener_conexiones_validas(nodo, conexiones, solicitud, vehiculos):
    conexiones_validas = []
    for conexion in conexiones:
        for veh in vehiculos:
            if veh.modo == conexion.tipo and conexion.es_valida(veh, solicitud.peso):
                conexiones_validas.append((conexion, veh))
    return conexiones_validas
