# generales
import math

# utils
from utils.loader import NodoLoader, ConexionLoader, SolicitudLoader
from utils.grafos import * 
from utils.validaciones import Validaciones
from utils.dfs import DFS

# models
from models.solicitud import * 
from models.vehiculos_herencia import *
from models.conexiones import *
from models.PuntoDeRed import PuntoDeRed
from models.nodo import Nodo
from models.itinerario import Itinerario
from models.graficos import *


# algoritmos
from planner.dijkstra_c import Dijkstra

#itinerario
from itinerario.buscar_ruta import *

def main():

    ciudades=NodoLoader.cargar_desde_csv("data/nodos.csv")
    solicitud=SolicitudLoader.cargar_desde_csv("data/solicitudes.csv", ciudades)

    def itinerario_x_modo(modo):
        conexiones=ConexionLoader.cargar_desde_csv("data/conexiones.csv", ciudades)
        if modo not in ["aereo", "automotor", "maritimo", "ferroviario"]:
            raise ValueError("Modo de transporte no válido. Debe ser 'aereo', 'ferroviario', 'automotor' o 'maritimo'.")
        if modo == "aereo":
            conexiones = list(filter(lambda x: isinstance(x, Conexion_aerea), conexiones))
        elif modo == "automotor":   
            conexiones = list(filter(lambda x: isinstance(x, Conexion_autovia), conexiones))
        elif modo == "ferroviario":
            conexiones = list(filter(lambda x: isinstance(x, Conexion_ferroviaria), conexiones))
        elif modo == "maritimo":    
            conexiones = list(filter(lambda x: isinstance(x, Conexion_maritima), conexiones))

        puntos_red = PuntoDeRed.constructor(ciudades)
        PuntoDeRed.agregar_vecinos(puntos_red, conexiones, solicitud[0])    

        itinerario_maritimo_tiempo = Dijkstra.ruta_mas_corta(puntos_red, solicitud[0].origen.nombre, solicitud[0].destino.nombre, "tiempo", modo)
        itinerario_maritimo_costo = Dijkstra.ruta_mas_corta(puntos_red, solicitud[0].origen.nombre, solicitud[0].destino.nombre, "costo", modo)
        
        return itinerario_maritimo_tiempo, itinerario_maritimo_costo

    itinerario_tiempo, itinerario_costo = itinerario_x_modo("ferroviario")
    if itinerario_tiempo is None or itinerario_costo is None:
        print("No se encontró un itinerario válido.")
        return
    print(itinerario_tiempo)
    print(itinerario_costo)



    #probar los itinerarios        
    tipos_conexion = {Camion: Conexion_autovia,Tren: Conexion_ferroviaria,Avion: Conexion_aerea, Barcaza: Conexion_maritima}
    vehiculos = obtener_vehiculos_default()
    conexiones_totales = ConexionLoader.cargar_desde_csv("data/conexiones.csv", ciudades)
    caminos_totales = []

    for clase_vehiculo in vehiculos:
        tipo_conexion = tipos_conexion[clase_vehiculo]
        conexiones_filtradas = list(filter(lambda x: isinstance(x, tipo_conexion), conexiones_totales))
        grafo = armar_grafo(ciudades, conexiones_filtradas)
        buscador = Buscar_ruta(grafo, clase_vehiculo)

        for s in solicitud:
            caminos = buscador.buscar_caminos(s)
            caminos_totales.extend(caminos)

    print(caminos_totales)
    Buscar_ruta.mostrar_resultados(caminos_totales)

main()

