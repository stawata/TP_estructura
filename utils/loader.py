import csv
from typing import List

from models import Nodo, Conexion, Solicitud  # Deberías definir estas clases en otro archivo

class NodoLoader:
    @staticmethod
    def cargar_desde_csv(path: str) -> List[Nodo]:
        nodos = []
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                nodos.append(Nodo(nombre=row["nombre"], modos=row["modos"].split('|')))
        return nodos

class ConexionLoader:
    @staticmethod
    def cargar_desde_csv(path: str) -> List[Conexion]:
        conexiones = []
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                conexiones.append(Conexion(
                    origen=row["origen"],
                    destino=row["destino"],
                    modo=row["modo"],
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
