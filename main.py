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
    ciudades=NodoLoader.cargar_desde_csv("data_extra/gran_red/nodos.csv")
    conexiones=ConexionLoader.cargar_desde_csv("data_extra/gran_red/conexiones.csv", ciudades)
    solicitud=SolicitudLoader.cargar_desde_csv("data_extra/gran_red/solicitudes.csv", ciudades)

    # filtro las conexiones para que solo queden las ferroviarias (esto habria que hacerlo con todos los tipos de conexiones)
    conexiones = list(filter(lambda x: isinstance(x, Conexion_ferroviaria), conexiones))

    # creo los puntos de red a partir de las ciudades y las conexiones entre ellas (solo las ferroviarias)
    puntos_red = PuntoDeRed.constructor(ciudades)
    PuntoDeRed.agregar_vecinos(puntos_red, conexiones, solicitud[0])

    # aplico el algoritmo de Dijkstra para encontrar la ruta más corta desde la ciudad origen a la ciudad destino
    ruta_mas_barata = Dijkstra.ruta_mas_corta(puntos_red, solicitud[0].origen.nombre, solicitud[0].destino.nombre, usar="costo")
    ruta_mas_rapida = Dijkstra.ruta_mas_corta(puntos_red, solicitud[0].origen.nombre, solicitud[0].destino.nombre, usar="tiempo")
    print("Ruta más barata:", ruta_mas_barata[0], "con costo:", ruta_mas_barata[1], '(en unidades monetarias)')
    print("Ruta más rápida:", ruta_mas_rapida[0], "con tiempo:", ruta_mas_rapida[1]*60, '(en minutos)')

if __name__ == "__main__":
    main()

