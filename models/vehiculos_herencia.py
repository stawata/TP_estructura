from models.vehiculos import Vehiculo
from models.solicitud import Solicitud
from models.conexiones import *
import random
import math
from collections import namedtuple #Es una tupla mas facil de acceder, mas entendible en realidad

Costos = namedtuple("Costos", ["fijo", "km", "kg"])

class Camion(Vehiculo):
    """Clase que representa un camión, hereda de Vehiculo."""
    velocidad_nominal = 80
    capacidad = 30000
    costos = Costos(fijo=30, km=5, kg=None)

    @classmethod
    def calcular_tiempo(cls, distancia, restriccion=None):
        return (distancia / cls.velocidad_nominal)

    @classmethod
    def cantidad_necesaria(cls, peso):
        return math.ceil(peso / cls.capacidad)

    @classmethod
    def calcular_costo(cls, distancia, peso):
        cantidad = cls.cantidad_necesaria(peso)
        if peso < 15000:
            costo_kg = 1
        else:
            costo_kg = 2
        return (cantidad * (cls.costos.fijo + cls.costos.km * distancia) + costo_kg * peso)

    @classmethod
    def puede_usar_conexion(cls, conexion, peso):
        if hasattr(conexion, "peso_max") and conexion.peso_max is not None:
            if peso > conexion.peso_max:
                return False
        return True


class Tren(Vehiculo):
    velocidad_nominal = 100
    capacidad = 150000
    costos = Costos(fijo=100, km=None, kg=3)  # el km depende de la distancia, lo calculamos dentro del método

    @classmethod
    def calcular_tiempo(cls, distancia, conexion): 
        if conexion and getattr(conexion, "restriccion", None) is not None:
            velocidad = min(cls.velocidad_nominal, conexion.restriccion)
        else:
            velocidad = cls.velocidad_nominal
        return distancia / velocidad

    @classmethod
    def cantidad_necesaria(cls, peso):
        return math.ceil(peso / cls.capacidad)

    @classmethod
    def calcular_costo(cls, distancia, peso):
        cantidad = cls.cantidad_necesaria(peso)
        if distancia < 200:
            costo_km = 20
        else:
            costo_km = 15
        return cantidad * (cls.costos.fijo + costo_km * distancia + cls.costos.kg * peso)
     

class Avion(Vehiculo):
    velocidad_nominal = 600
    capacidad = 5000
    costos = Costos(fijo=750, km=40, kg=10)

    @classmethod
    def calcular_tiempo(cls, distancia, conexion):
        prob = conexion.restriccion  # Se accede desde la conexión
        llueve = random.random() < prob
        if llueve:
            velocidad = 400
        else:
            velocidad = cls.velocidad_nominal

        return distancia / velocidad

    @classmethod
    def cantidad_necesaria(cls, peso):
        return math.ceil(peso / cls.capacidad)

    @classmethod
    def calcular_costo(cls, distancia, peso):
        cantidad = cls.cantidad_necesaria(peso)
        return cantidad * (cls.costos.fijo + cls.costos.km * distancia + cls.costos.kg * peso)


class Barcaza(Vehiculo):
    velocidad_nominal = 40
    capacidad = 100000
    costos = Costos(fijo=None, km=15, kg=2)

    @classmethod
    def calcular_tiempo(cls, distancia, restriccion=None):
        return distancia / cls.velocidad_nominal

    @classmethod
    def cantidad_necesaria(cls, peso):
        return math.ceil(peso / cls.capacidad)

    @classmethod
    def calcular_costo(cls, distancia, peso, conexion):
        cantidad = cls.cantidad_necesaria(peso)

        if conexion.restriccion == "fluvial":
            costo_fijo = 500
        else:
            costo_fijo = 1500

        return cantidad * (costo_fijo + cls.costos.km * distancia + cls.costos.kg * peso)


def obtener_vehiculos_default():
    """Obtiene una lista de los vehículos por defecto.
    Returns:
        list: Lista de clases de vehículos.
    """
    return [Camion, Tren, Avion, Barcaza]

obtener_vehiculos_default() # Llamada para inicializar la lista de vehículos por defecto