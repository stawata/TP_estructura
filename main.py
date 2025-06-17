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

# algoritmos
from planner.dijkstra_c import Dijkstra

def main():
    ciudades=NodoLoader.cargar_desde_csv("data/nodos.csv")
    conexiones=ConexionLoader.cargar_desde_csv("data/conexiones.csv", ciudades)
    solicitud=SolicitudLoader.cargar_desde_csv("data/solicitudes.csv", ciudades)

    # filtro las conexiones para que solo queden las marítimas
    conexiones = list(filter(lambda x: isinstance(x, Conexion_maritima), conexiones))

    # creo los puntos de red a partir de las ciudades y las conexiones entre ellas (solo las marítimas)
    puntos_red = PuntoDeRed.constructor(ciudades)
    PuntoDeRed.agregar_vecinos(puntos_red, conexiones, solicitud[0])    

    # aplico el algoritmo de Dijkstra para encontrar la ruta más corta desde la ciudad origen a la ciudad destino
    itinerario_maritimo_tiempo = Dijkstra.ruta_mas_corta(puntos_red, solicitud[0].origen.nombre, solicitud[0].destino.nombre, "tiempo", "maritimo")
    itinerario_maritimo_costo = Dijkstra.ruta_mas_corta(puntos_red, solicitud[0].origen.nombre, solicitud[0].destino.nombre, "costo", "maritimo")
    print("Itinerario marítimo por tiempo:")
    print(itinerario_maritimo_tiempo)
    print("Itinerario marítimo por costo:")
    print(itinerario_maritimo_costo)

main()

