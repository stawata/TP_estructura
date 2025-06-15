import csv

from models.nodo import Nodo
from models.conexiones import Conexion, Conexion_ferroviaria, Conexion_aerea, Conexion_maritima, Conexion_autovia
from models.solicitud import Solicitud

class NodoLoader:
    @staticmethod
    def cargar_desde_csv(path: str): # Carga los nodos desde un archivo CSV y devuelve una lista de instancias de Nodo
        nodos = []
        if not path.endswith('.csv'):
            raise ValueError("El archivo debe ser un CSV válido")
        if not path:
            raise ValueError("La ruta del archivo no puede ser None o vacía")
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    if row["nombre"]:
                        nodos.append(Nodo(nombre=row["nombre"].lower()))
                except (KeyError, ValueError) as e:
                    print(f"Error al procesar la fila {row}: {e}")
                    continue
        return nodos

class ConexionLoader:
    @staticmethod
    def cargar_desde_csv(path: str, nodos: list): # Carga las conexiones desde un archivo CSV y devuelve una lista de instancias de Conexion
        conexiones = []
        nodos_dict = {nodo.nombre: nodo for nodo in nodos}
        if path is None or not path.endswith('.csv'):
            raise ValueError("El archivo debe ser un CSV válido")
        if not path:
            raise ValueError("La ruta del archivo no puede ser None o vacía")
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    if row["origen"] and row["destino"] and row["tipo"] and row["distancia_km"]: # Verifica que los campos obligatorios estén presentes
                        if row["origen"].lower() in nodos_dict.keys() and row["destino"].lower() in nodos_dict.keys():
                                origen=nodos_dict[row["origen"].lower()]
                                destino=nodos_dict[row["destino"].lower()]
                                distancia_km=float(row["distancia_km"])
                                if row["tipo"].lower() == "ferroviaria":
                                    conexiones.append(Conexion_ferroviaria(origen, destino, distancia_km,   
                                    restriccion=float(row["valor_restriccion"]) if row["valor_restriccion"] else None
                                ))
                                elif row["tipo"].lower() == "aerea" or row["tipo"].lower() == "aérea":
                                    conexiones.append(Conexion_aerea(origen, destino, distancia_km,        
                                    restriccion=float(row["valor_restriccion"]) if row["valor_restriccion"] else None
                                ))
                                elif row["tipo"].lower() == "maritima" or row["tipo"].lower() == "fluvial":
                                    conexiones.append(Conexion_maritima(origen, destino, distancia_km,
                                    restriccion=row["valor_restriccion"].lower() if row["valor_restriccion"] else None    
                                ))
                                elif row["tipo"].lower() == "automotor":
                                    conexiones.append(Conexion_autovia(origen, destino, distancia_km,       
                                    restriccion=float(row["valor_restriccion"]) if row["valor_restriccion"] else None
                                ))
                except (ValueError, KeyError) as e:
                    print(f"Error al procesar la fila {row}: {e}")
                    continue
        return conexiones

class SolicitudLoader:
    @staticmethod
    def cargar_desde_csv(path: str, nodos: list): # Carga las solicitudes desde un archivo CSV y devuelve una lista de instancias de Solicitud
        solicitudes = []
        nodos_dict = {nodo.nombre: nodo for nodo in nodos}
        if path is None or not path.endswith('.csv'):
            raise ValueError("El archivo debe ser un CSV válido")
        if not path:
            raise ValueError("La ruta del archivo no puede ser None o vacía")
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    if row["id_carga"] and row["peso_kg"] and row["origen"] and row["destino"]:
                        if row["origen"].lower() in nodos_dict.keys() and row["destino"].lower() in nodos_dict.keys():
                            solicitudes.append(Solicitud(
                                id_carga=row["id_carga"],
                                peso_kg=float(row["peso_kg"]),
                                origen=nodos_dict[row["origen"].lower()],
                                destino=nodos_dict[row["destino"].lower()]
                            ))
                        else:
                            raise ValueError(f"Ciudad no encontrada en nodos: {row['origen']} o {row['destino']}")
                except (ValueError, KeyError) as e:
                    print(f"Error al procesar la fila {row}: {e}")
                    continue
        return solicitudes
