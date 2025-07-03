from models.conexiones import Conexion_ferroviaria, Conexion_aerea, Conexion_maritima, Conexion_autovia
from models.solicitud import Solicitud
from models.nodo import Nodo
from utils.validaciones import Validaciones

class PuntoDeRed:
    def __init__(punto, nombre):
        """Creamos un objeto del tipo puntodeRed, el cual representa a una ciudad y sus conexiones"""
        punto.nombre = nombre
        punto.vecinos = {}  # {punto_vecino: peso}
        
    @staticmethod
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
        if not puntos_de_red:
            raise ValueError("El diccionario de puntos de red no puede estar vacío.")
        
        if not Validaciones.validar_lista_conexiones(conexiones):
            raise TypeError("La lista de conexiones debe ser una lista de instancias de Conexion.")
        if not Validaciones.verificar_origen_destino(puntos_de_red, solicitud):
            raise ValueError("El origen y el destino de la solicitud deben estar en los puntos de red.")
        
        for punto in puntos_de_red.values():
            for conexion in conexiones:
                costo = None
                tiempo = None
                if conexion.origen.nombre == punto.nombre or conexion.destino.nombre == punto.nombre:
                    costo = conexion.calcular_costo(solicitud.peso_kg)
                    tiempo = conexion.calcular_tiempo()
                    if costo is not None and tiempo is not None:
                        if conexion.origen.nombre == punto.nombre:
                            punto.vecinos[puntos_de_red[conexion.destino.nombre]] = (costo, tiempo)
                        elif conexion.destino.nombre == punto.nombre:
                            punto.vecinos[puntos_de_red[conexion.origen.nombre]] = (costo,tiempo)
