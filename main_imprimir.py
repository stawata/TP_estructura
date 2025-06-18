from models.vehiculos_herencia import *
from utils.loader import NodoLoader, ConexionLoader, SolicitudLoader
from utils.grafos import *
from itinerario.buscar_ruta import Buscar_ruta

def mostrar():
    ciudades=NodoLoader.cargar_desde_csv("data/nodos.csv") #no hace falta leerlo devuelta
    solicitud=SolicitudLoader.cargar_desde_csv("data/solicitudes.csv", ciudades) #no hace falta leerlo devuelta
    tipos_conexion={Camion: Conexion_autovia, Tren: Conexion_ferroviaria, Avion: Conexion_aerea, Barcaza:Conexion_maritima}
    vehiculos=obtener_vehiculos_default()
    conexiones_totales=ConexionLoader.cargar_desde_csv("data/conexiones.csv", ciudades)


    for s in solicitud:
        caminos_totales=[]
        for vehiculo in vehiculos:
            tipo_conexion=tipos_conexion[vehiculo]
            conexiones_filtradas=list(filter(lambda x: isinstance(x, tipo_conexion), conexiones_totales))
            grafo=armar_grafo(ciudades,conexiones_filtradas)
            buscador=Buscar_ruta(grafo,vehiculo)
            caminos=buscador.buscar_caminos(s)
            caminos_totales.extend(caminos)
        # Mostrar los resultados
        Buscar_ruta.mostrar_resultados(caminos_totales)

mostrar()