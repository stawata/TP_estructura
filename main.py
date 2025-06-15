from utils.loader import NodoLoader, ConexionLoader, SolicitudLoader
from algoritmo_disjtra.Nodo_ciudad import NodoCiudad
from algoritmo_disjtra.algoritmo_d import Dijkstra
from models.solicitud import Solicitud 
from models.vehiculos_herencia import *
from utils.validaciones import Validaciones
from models.conexiones import *
from utils.grafos import * 


def main():
    try:
        # Ciudades = NodoLoader.cargar_desde_csv("data/nodos.csv")
        # Conexiones = ConexionLoader.cargar_desde_csv("data/conexiones.csv", Ciudades)
        # Solicitudes = SolicitudLoader.cargar_desde_csv("data/solicitudes.csv", Ciudades)
        pass





    except FileNotFoundError as e:
        print(f"Error al cargar los archivos: {e}")

    print("Ciudades cargadas:")
    # for ciudad in Ciudades:
    #     print(ciudad)
    # print("\nConexiones cargadas:")
    # for conexion in Conexiones:
    #     print(conexion)
    # print("\nSolicitudes cargadas:")
    # for solicitud in Solicitudes:
    #     print(solicitud)

#ACA TENGO EN UNA LISTA LOS VALORES QUE LEI 
nodos = NodoLoader.cargar_desde_csv("data/nodos.csv")
conexiones= ConexionLoader.cargar_desde_csv("data/conexiones.csv", nodos)

#ACA VOY HACER LAS CONEXIONES DE TODOS LOS VEHICLOS 
conexiones_ferroviarias_totales = list(filter(lambda x : isinstance(x,Conexion_ferroviaria), conexiones))
#conexiones_autovia_totales = list(filter(lambda x : isinstance(x,Conexion_autovia), conexiones))




#ACA VOY A TENER LOS GRAFOS DE CADA VEHICULO
#grafo del CONEXIONES FERROVIARIAS
grafo_tren= armar_grafo(nodos, conexiones_ferroviarias_totales)
#grafo del CONEXIONES AUTOMOTOR(CAMION)
#grafo_autovia= armar_grafo(nodos, conexiones_autovia_totales)

#ACA VOY A EJECUTAR EL ALGORITMO DE DIKSTRA
solicitud_1 = Solicitud("CARGA_001",70000,NodoCiudad("zarate",0, None),NodoCiudad("mar_del_plata",0, None))
camion_1 = Camion()
tren_1 = Tren()
recorrido = Dijkstra.analizador_ruta_tiempos(grafo_tren, solicitud_1, tren_1)


#ESTO ES PATRA VISUALIZAR DESPUES SE PUEDE BORRAR
# for key, values in grafo_tren.items():
#     print(f"Llave: {key}")
#     for i in values: 
#         print("valores:",i[0], i[1], i[2])

