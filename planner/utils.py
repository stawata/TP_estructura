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

def construir_grafo(conexiones, nodos_dict):
    """
    Construye un grafo dirigido desde una lista de conexiones,
    asegurando coincidencia robusta entre nombres de nodos.
    """
    grafo = defaultdict(list)

    for conexion in conexiones:
        origen = conexion.origen.nombre.strip().lower()
        destino = conexion.destino.nombre.strip().lower()

        if origen in nodos_dict and destino in nodos_dict:
            grafo[origen].append(conexion)

    return grafo

def obtener_conexiones_validas(nodo, conexiones, solicitud, vehiculos):
    conexiones_validas = []
    for conexion in conexiones:
        for veh in vehiculos:
            if veh.modo == conexion.tipo and conexion.es_valida(veh, solicitud.peso):
                conexiones_validas.append((conexion, veh))
    return conexiones_validas
