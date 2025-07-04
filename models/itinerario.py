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
        return f"Modo: {self.modo}\n Ciudades: {' --> '.join(self.itinerario)}\n Costo Total: {self.costo_total} pesos\n Tiempo Total: {self.tiempo_total} horas"

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

        conexiones_validas, ciudades_filtradas = Itinerario.filtrador_ciudades_por_peso_admitido(ciudades,solicitud,conexiones)
        puntos_red = PuntoDeRed.constructor(ciudades_filtradas)
        PuntoDeRed.agregar_vecinos(puntos_red, conexiones_validas, solicitud[0])    
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
    def filtrador_ciudades_por_peso_admitido(ciudades,solicitud,conexiones):
        peso_carga = solicitud[0].getpeso_kg()
        ciudades_filtradas = list(filter(lambda x: x.peso_maximo is None or x.peso_maximo >= peso_carga, ciudades))
        nombre_validos = list(map(lambda x:x.nombre, ciudades_filtradas))
        conexiones_validas = list(filter(lambda x: x.origen.nombre in nombre_validos and x.destino.nombre in nombre_validos, conexiones))
        return conexiones_validas, ciudades_filtradas
    
    @staticmethod
    def procesar_modo(valor, solicitud, conexiones, ciudades):
        itinerario_tiempo, itinerario_costo = Itinerario.itinerario_x_modo(valor, solicitud, conexiones, ciudades)
        if itinerario_tiempo is None or itinerario_costo is None:
            print(f"No se encontró un itinerario válido para el modo {valor}.")
            return []
        return [itinerario_tiempo, itinerario_costo]

    @staticmethod
    def creador_itinerario(solicitud, conexiones, ciudades):
        """Este metodo crea una lista donde se almacenaran los itinerarios de la solicitud segun el modo de transporte
          y retorna el itinerario mas rapido y el mas barato"""
        lista_modos = ["ferroviario", "maritimo", "automotor", "aereo"]
        lista_itinerarios = []
        itinerarios_generados = map(lambda valor: Itinerario.procesar_modo(valor, solicitud, conexiones, ciudades), lista_modos)
        for sublista in itinerarios_generados:
            lista_itinerarios.extend(sublista)
        
        if not lista_itinerarios:
            raise ValueError("No se encontraron itinerarios válidos para la solicitud.")
        
        itinerario_rapido = sorted(lista_itinerarios, key=lambda x: x.tiempo_total)
        itinerario_barato = sorted(lista_itinerarios, key=lambda x: x.costo_total)
        return itinerario_rapido[0], itinerario_barato[0]