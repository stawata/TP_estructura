# generales
import math

# utils
from utils.loader import NodoLoader, ConexionLoader, SolicitudLoader
from utils.grafos import * 
from utils.validaciones import Validaciones

# models
from models.solicitud import * 
from models.vehiculos_herencia import *
from models.conexiones import *
from models.PuntoDeRed import PuntoDeRed

# algoritmos
from algoritmo_disjtra.pilas_2 import Pila
from algoritmo_disjtra.Nodo_pais import NodoPais
from planner.dijkstra_c import Dijkstra

def main():
    ciudades=NodoLoader.cargar_desde_csv("data/nodos.csv")
    conexiones=ConexionLoader.cargar_desde_csv("data/conexiones.csv", ciudades)
    solicitud=SolicitudLoader.cargar_desde_csv("data/solicitudes.csv", ciudades)

    # filtro las conexiones para que solo queden las ferroviarias (esto habria que hacerlo con todos los tipos de conexiones)
    conexiones = list(filter(lambda x: isinstance(x, Conexion_ferroviaria), conexiones))

    # creo los puntos de red a partir de las ciudades y las conexiones entre ellas (solo las ferroviarias)
    puntos_red = PuntoDeRed.constructor(ciudades)
    print("Puntos de red creados:", puntos_red)
    PuntoDeRed.agregar_vecinos(puntos_red, conexiones, solicitud[0])
    for punto in puntos_red.values():
        print(f"Punto de red {punto.nombre} tiene vecinos: {punto.vecinos}")

    # aplico el algoritmo de Dijkstra para encontrar la ruta más corta desde la ciudad origen a la ciudad destino
    distancias, anteriores = Dijkstra.dijkstra(puntos_red, solicitud[0].origen.nombre, usar="costo")
    print("Distancias desde el origen:", distancias)
    print("Nodos anteriores:", anteriores)

main()

