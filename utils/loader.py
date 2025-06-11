import csv

from models.nodo import Nodo
from models.conexiones import Conexion, Conexion_ferroviaria, Conexion_aerea, Conexion_maritima, Conexion_autovia
from models.solicitud import Solicitud

class NodoLoader:
    @staticmethod
    def cargar_desde_csv(path: str): # Carga los nodos desde un archivo CSV y devuelve una lista de instancias de Nodo
        nodos = []
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                nodos.append(Nodo(nombre=row["nombre"].lower()))
        return nodos

class ConexionLoader:
    @staticmethod
    def cargar_desde_csv(path: str, nodos: list): # Carga las conexiones desde un archivo CSV y devuelve una lista de instancias de Conexion
        conexiones = []
        nodos_dict = {nodo.nombre: nodo for nodo in nodos}
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["origen"].lower() in nodos_dict.keys() and row["destino"].lower() in nodos_dict.keys():
                    if row["tipo"].lower() == "ferroviaria":
                        conexiones.append(Conexion_ferroviaria(
                        origen=nodos_dict[row["origen"].lower()],
                        destino=nodos_dict[row["destino"].lower()],
                        distancia_km=float(row["distancia_km"]),        
                        velocidad_max=float(row["valor_restriccion"]) if row["valor_restriccion"] else None,
                    ))
                    elif row["tipo"].lower() == "aerea" or row["tipo"].lower() == "aérea":
                        conexiones.append(Conexion_aerea(
                        origen=nodos_dict[row["origen"].lower()],
                        destino=nodos_dict[row["destino"].lower()],
                        distancia_km=float(row["distancia_km"]),        
                        probabilidad_mal_clima=float(row["valor_restriccion"]) if row["valor_restriccion"] else None
                    ))
                    elif row["tipo"].lower() == "maritima" or row["tipo"].lower() == "fluvial":
                        conexiones.append(Conexion_maritima(
                        origen=nodos_dict[row["origen"].lower()],
                        destino=nodos_dict[row["destino"].lower()],
                        distancia_km=float(row["distancia_km"]),
                        tipo_tasa=row["valor_restriccion"].lower() if row["valor_restriccion"] else None,    
                    ))
                    elif row["tipo"].lower() == "automotor":
                        conexiones.append(Conexion_autovia(
                        origen=nodos_dict[row["origen"].lower()],
                        destino=nodos_dict[row["destino"].lower()],
                        distancia_km=float(row["distancia_km"]),        
                        peso_max=float(row["valor_restriccion"]) if row["valor_restriccion"] else None,
                    ))
        return conexiones

class SolicitudLoader:
    @staticmethod
    def cargar_desde_csv(path: str, nodos: list):
        solicitudes = []
        nodos_dict = {nodo.nombre: nodo for nodo in nodos}
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["origen"].lower() in nodos_dict.keys() and row["destino"].lower() in nodos_dict.keys():
                    solicitudes.append(Solicitud(
                        id_carga=row["id_carga"],
                        peso_kg=float(row["peso_kg"]),
                        origen=nodos_dict[row["origen"].lower()],
                        destino=nodos_dict[row["destino"].lower()]
                    ))
        return solicitudes
