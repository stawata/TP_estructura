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

# algoritmos
from algoritmo_disjtra.pilas_2 import Pila
from algoritmo_disjtra.Nodo_ciudad import NodoCiudad
from algoritmo_disjtra.algoritmo_d import Dijkstra

# def main():
#     ciudades=NodoLoader.cargar_desde_csv("data/nodos.csv")
#     conexiones=ConexionLoader.cargar_desde_csv("data/conexiones.csv", ciudades)
#     solicitud=SolicitudLoader.cargar_desde_csv("data/solicitudes.csv", ciudades)





#ACA TENGO EN UNA LISTA LOS VALORES QUE LEI 
nodos=NodoLoader.cargar_desde_csv("data/nodos.csv")
conexiones=ConexionLoader.cargar_desde_csv("data/conexiones.csv", nodos)

#prueba con datagrande
# nodos=NodoLoader.cargar_desde_csv("data_extra/gran_red/nodos.csv")
# conexiones=ConexionLoader.cargar_desde_csv("data_extra/gran_red/conexiones.csv", nodos)


#ACA VOY HACER LAS CONEXIONES DE TODOS LOS VEHICLOS 
conexiones_ferroviarias_totales = list(filter(lambda x : isinstance(x,Conexion_ferroviaria), conexiones))
conexiones_autovia_totales = list(filter(lambda x : isinstance(x,Conexion_autovia), conexiones))
conexiones_maritimas_totales = list(filter(lambda x : isinstance(x,Conexion_maritima), conexiones))
conexiones_aereas_totales = list(filter(lambda x : isinstance(x,Conexion_aerea), conexiones))



#ACA VOY A TENER LOS GRAFOS DE CADA VEHICULO
grafo_tren=armar_grafo(nodos, conexiones_ferroviarias_totales)
grafo_autovia=armar_grafo(nodos, conexiones_autovia_totales)
grafo_maritima = armar_grafo(nodos,  conexiones_maritimas_totales)
grafo_aerea=armar_grafo(nodos, conexiones_aereas_totales)

solicitud_1 = Solicitud("CARGA_001",70000,NodoCiudad("zarate",0, None),NodoCiudad("mar_del_plata",0, None))
camion_1 = Camion()
tren_1 = Tren()
avion_1 = Avion()
barzaza_1 = Barcaza()
#caminos = DFS.encontrar_todos_los_caminos(grafo_autovia,solicitud_1, camion_1)
recorrido = Dijkstra.analizador_ruta_tiempos(grafo_maritima, solicitud_1, barzaza_1)
#ESTO ES PATRA VISUALIZAR DESPUES SE PUEDE BORRAR
# for key, values in grafo_tren.items():
#     print(f"Llave: {key}")
#     for i in values: 
#         print("valores:",i[0], i[1], i[2])


