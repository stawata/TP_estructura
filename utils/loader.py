import csv
from typing import List 
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
                nodos.append(Nodo(nombre=row["nombre"], modos=row["modos"].split('|')))
        return nodos

class ConexionLoader:
    @staticmethod
    def cargar_desde_csv(path: str, nodos: list): # Carga las conexiones desde un archivo CSV y devuelve una lista de instancias de Conexion
        conexiones = []
        nodos_dict = {nodo.nombre: nodo for nodo in nodos}
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["origen"] in nodos_dict.keys and row["destino"] in nodos_dict.keys:
                    if row["modo"].lower() == "ferroviaria":
                        conexiones.append(Conexion_ferroviaria(
                        origen=nodos_dict[row["origen"]],
                        destino=nodos_dict[row["destino"]],
                        distancia=float(row["distancia"]),        
                        restriccion_peso=float(row["restriccion_peso"]) if row["restriccion_peso"] else None,
                        velocidad_maxima=float(row["velocidad_maxima"]) if row["velocidad_maxima"] else None,
                        probabilidad_mal_clima=float(row["probabilidad_mal_clima"]) if row["probabilidad_mal_clima"] else None
                    ))
                    elif row["modo"].lower() == "aerea" or row["modo"].lower() == "aérea":
                        conexiones.append(Conexion_aerea(
                        origen=nodos_dict[row["origen"]],
                        destino=nodos_dict[row["destino"]],
                        distancia=float(row["distancia"]),        
                        restriccion_peso=float(row["restriccion_peso"]) if row["restriccion_peso"] else None,
                        velocidad_maxima=float(row["velocidad_maxima"]) if row["velocidad_maxima"] else None,
                        probabilidad_mal_clima=float(row["probabilidad_mal_clima"]) if row["probabilidad_mal_clima"] else None
                    ))
                    elif row["modo"].lower() == "maritima" or row["modo"].lower() == "fluvial":
                        conexiones.append(Conexion_maritima(
                        origen=nodos_dict[row["origen"]],
                        destino=nodos_dict[row["destino"]],
                        distancia=float(row["distancia"]),        
                        restriccion_peso=float(row["restriccion_peso"]) if row["restriccion_peso"] else None,
                        velocidad_maxima=float(row["velocidad_maxima"]) if row["velocidad_maxima"] else None,
                        probabilidad_mal_clima=float(row["probabilidad_mal_clima"]) if row["probabilidad_mal_clima"] else None
                    ))
                    elif row["modo"].lower() == "automotor":
                        conexiones.append(Conexion_autovia(
                        origen=nodos_dict[row["origen"]],
                        destino=nodos_dict[row["destino"]],
                        distancia=float(row["distancia"]),        
                        restriccion_peso=float(row["restriccion_peso"]) if row["restriccion_peso"] else None,
                        velocidad_maxima=float(row["velocidad_maxima"]) if row["velocidad_maxima"] else None,
                        probabilidad_mal_clima=float(row["probabilidad_mal_clima"]) if row["probabilidad_mal_clima"] else None
                    ))
        return conexiones

class SolicitudLoader:
    @staticmethod
    def cargar_desde_csv(path: str) -> List[Solicitud]:
        solicitudes = []
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                solicitudes.append(Solicitud(
                    id=row["id"],
                    peso=float(row["peso"]),
                    origen=row["origen"],
                    destino=row["destino"]
                ))
        return solicitudes
