from models.PuntoDeRed import PuntoDeRed
from models.conexiones import Conexion_aerea, Conexion_autovia, Conexion_ferroviaria, Conexion_maritima
from planner.dijkstra_c import Dijkstra

class Itinerario():
    def __init__(self, modo, itinerario, costo_total, tiempo_total):
        """
        Clase que representa un itinerario de viaje.
        :param modo: El modo de transporte utilizado (por ejemplo, "coche", "tren", etc.).
        :param itinerario: Una lista de ciudades que componen el itinerario.
        :param costo_total: El costo total del itinerario.
        :param tiempo_total: El tiempo total del itinerario.
        """
        self.modo = modo
        self.itinerario = itinerario
        self.costo_total = costo_total
        self.tiempo_total = tiempo_total
    
    def __str__(self):
        return f"Itinerario: {self.modo}, Ciudades: {' --> '.join(self.itinerario)}, Costo Total: {self.costo_total} pesos, Tiempo Total: {self.tiempo_total} horas"

    @staticmethod
    def itinerario_x_modo(modo, solicitud, conexiones, ciudades):
        """Este metodo crea el itinerario mas barato y menos costoso de la solicitud segun el modo de transporte"""
        if modo not in ["aereo", "automotor", "maritimo", "ferroviario"]:
            raise ValueError("Modo de transporte no válido. Debe ser 'aereo', 'ferroviario', 'automotor' o 'maritimo'.")
        if modo == "aereo":
            conexiones = list(filter(lambda x: isinstance(x, Conexion_aerea), conexiones))
        elif modo == "automotor":   
            conexiones = list(filter(lambda x: isinstance(x, Conexion_autovia), conexiones))
        elif modo == "ferroviario":
            conexiones = list(filter(lambda x: isinstance(x, Conexion_ferroviaria), conexiones))
        elif modo == "maritimo":    
            conexiones = list(filter(lambda x: isinstance(x, Conexion_maritima), conexiones))

        puntos_red = PuntoDeRed.constructor(ciudades)
        PuntoDeRed.agregar_vecinos(puntos_red, conexiones, solicitud[0])    

        modo, ruta, costo_total, tiempo_total = Dijkstra.ruta_mas_corta(puntos_red, solicitud[0].origen.nombre, solicitud[0].destino.nombre, "tiempo", modo)
        if ruta is None or costo_total is None or tiempo_total is None:
            return None, None
        itinerario_tiempo = Itinerario(modo, ruta, costo_total, tiempo_total)
        modo, ruta, costo_total, tiempo_total = Dijkstra.ruta_mas_corta(puntos_red, solicitud[0].origen.nombre, solicitud[0].destino.nombre, "costo", modo)
        if ruta is None or costo_total is None or tiempo_total is None:
            return None, None
        itinerario_costo = Itinerario(modo, ruta, costo_total, tiempo_total)

        return itinerario_tiempo, itinerario_costo

    @staticmethod
    def creador_itinerario(solicitud, conexiones, ciudades):
        """Este metodo crea una lista donde se almacenaran los itinerarios de la solicitud segun el modo de transporte
          y retorna el itinerario mas rapido y el mas barato"""
        lista_modos = ["ferroviario", "maritimo", "automotor", "aereo"]
        lista_itinerarios = []
        for valor in lista_modos:
            itinerario_tiempo, itinerario_costo = Itinerario.itinerario_x_modo(valor, solicitud, conexiones, ciudades)
            if itinerario_tiempo is None or itinerario_costo is None:
                print(f"No se encontró un itinerario válido para el modo {valor}.")
                continue
            lista_itinerarios.append(itinerario_tiempo)
            lista_itinerarios.append(itinerario_costo)
        itinerario_rapido = sorted(lista_itinerarios, key=lambda x: x.tiempo_total)
        itinerario_barato = sorted(lista_itinerarios, key=lambda x: x.costo_total)
        return itinerario_rapido[0], itinerario_barato[0]