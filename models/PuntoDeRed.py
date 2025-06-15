from models.conexiones import ConexionFerroviaria, ConexionAerea, ConexionMaritima
from models.vehiculos_herencia import Tren, Avion, Camion
from models.solicitud import Solicitud

class PuntoDeRed:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vecinos = {}  # {punto_vecino: peso}

    def agregar_vecinos(self, conexiones, solicitud):
        for conexion in conexiones:
            if conexion.origen == self.nombre or conexion.destino == self.nombre:
                if isinstance(conexion, ConexionFerroviaria):
                        costo = Tren.calcular_costo(conexion.distancia_km, solicitud.peso_kg)
                        tiempo = Tren.calcular_tiempo(conexion.distancia_km, conexion)
                elif isinstance(conexion, ConexionAerea):
                        costo = Avion.calcular_costo(conexion.distancia_km, solicitud.peso_kg)
                        tiempo = Avion.calcular_tiempo(conexion.distancia_km, conexion)
                elif isinstance(conexion, ConexionMaritima):
                        costo = Camion.calcular_costo(conexion.distancia_km, solicitud.peso_kg)
                        tiempo = Camion.calcular_tiempo(conexion.distancia_km)
                if conexion.origen == self.nombre:
                    self.vecinos[conexion.destino] = (costo, tiempo)
                elif conexion.destino == self.nombre:
                    self.vecinos[conexion.origen] = (costo, tiempo)
