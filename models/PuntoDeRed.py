from models.conexiones import Conexion_ferroviaria, Conexion_aerea, Conexion_maritima, Conexion_autovia
from models.vehiculos_herencia import Tren, Avion, Camion, Barcaza
from models.solicitud import Solicitud
from models.nodo import Nodo

class PuntoDeRed:
    def __init__(punto, nombre):
        """Creamos un objeto del tipo puntodeRed, el cual representa a una ciudad y sus conexiones"""
        punto.nombre = nombre
        punto.vecinos = {}  # {punto_vecino: peso}

    def constructor(nodos):
        """
        Constructor que recibe una lista de nodos y los inicializa como puntos de red.
        """
        puntos_de_red = {}
        if not nodos:
            raise ValueError("La lista de nodos no puede estar vacía.")
        if not all(isinstance(nodo, Nodo) for nodo in nodos):
            raise TypeError("Todos los elementos de la lista deben ser instancias de Nodo.")
        for nodo in nodos:
            puntos_de_red[nodo.nombre] = PuntoDeRed(nodo.nombre)
        return puntos_de_red

    @staticmethod
    def agregar_vecinos(puntos_de_red, conexiones, solicitud):
        """
        Agrega vecinos al punto de red actual basándose en las conexiones y la solicitud.
        puntos_de_red: dict[str, PuntoDeRed] - Diccionario de puntos de red.
        conexiones: list[Conexion] - Lista de conexiones entre puntos de red.
        solicitud: Solicitud - Objeto de solicitud que contiene información sobre el peso y el destino.
        """
        if not isinstance(solicitud, Solicitud):
            raise TypeError("La solicitud debe ser una instancia de Solicitud.")
        if not isinstance(conexiones, list) or not all(isinstance(conexion, (Conexion_ferroviaria, Conexion_aerea, Conexion_maritima, Conexion_autovia)) for conexion in conexiones):
            raise TypeError("Las conexiones deben ser una lista de instancias de Conexion_ferroviaria, Conexion_aerea, Conexion_autovia o Conexion_maritima.")
        if not puntos_de_red:
            raise ValueError("El diccionario de puntos de red no puede estar vacío.")
        if solicitud.destino.nombre not in puntos_de_red.keys():
            raise ValueError("El destino de la solicitud no está en los puntos de red.")
        if solicitud.origen.nombre not in puntos_de_red.keys():
            raise ValueError("El origen de la solicitud no está en los puntos de red.")
        for punto in puntos_de_red.values():
            for conexion in conexiones:
                costo = None
                tiempo = None
                if conexion.origen.nombre == punto.nombre or conexion.destino.nombre == punto.nombre:
                    if isinstance(conexion, Conexion_ferroviaria):
                        costo = Tren.calcular_costo(conexion.distancia_km, solicitud.getpeso_kg())
                        tiempo = Tren.calcular_tiempo(conexion.distancia_km, conexion)
                    elif isinstance(conexion, Conexion_aerea):
                        costo = Avion.calcular_costo(conexion.distancia_km, solicitud.getpeso_kg())
                        tiempo = Avion.calcular_tiempo(conexion.distancia_km, conexion)
                    elif isinstance(conexion, Conexion_maritima):
                        costo = Barcaza.calcular_costo(conexion.distancia_km, solicitud.getpeso_kg(), conexion)
                        tiempo = Barcaza.calcular_tiempo(conexion.distancia_km)
                    elif isinstance(conexion, Conexion_autovia):
                        if conexion.restriccion is not None:
                            if solicitud.getpeso_kg() <= conexion.restriccion:
                                costo = Camion.calcular_costo(conexion.distancia_km, solicitud.getpeso_kg())
                                tiempo = Camion.calcular_tiempo(conexion.distancia_km)
                        else:
                            costo = Camion.calcular_costo(conexion.distancia_km, solicitud.getpeso_kg())
                            tiempo = Camion.calcular_tiempo(conexion.distancia_km)
                    if costo is not None and tiempo is not None:
                        if conexion.origen.nombre == punto.nombre:
                            punto.vecinos[puntos_de_red[conexion.destino.nombre]] = (costo, tiempo)
                        elif conexion.destino.nombre == punto.nombre:
                            punto.vecinos[puntos_de_red[conexion.destino.nombre]] = (costo, tiempo)
