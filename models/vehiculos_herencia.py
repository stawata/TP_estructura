from models.vehiculos import Vehiculo
from models.solicitud import Solicitud
from models.conexiones import *
import random
import math
from collections import namedtuple 

Costos = namedtuple("Costos", ["fijo", "km", "kg"])
"""
Costos es una tupla que almacena los costos asociados a un vehículo.
Atributos:
    fijo: Costo fijo del vehículo.
    km: Costo por kilómetro recorrido.
    kg: Costo por kilogramo transportado (opcional, puede ser None).
De esta manera, se pueden definir los costos de cada vehículo de forma clara y accederlos mas legiblemente para humanos.
"""

class Camion(Vehiculo):
    """
    Clase que representa un camión, hereda de Vehiculo.
    Atributos de clase:
        velocidad_nominal: Velocidad máxima del camión en km/h.
        capacidad: Capacidad de carga del camión en kg.
        costos: Costos asociados al uso del camión.
    """
    velocidad_nominal = 80
    capacidad = 30000
    costos = Costos(fijo=30, km=5, kg=None)


    @classmethod
    def calcular_costo(cls, distancia, peso):
        """
        Calcula el costo total del transporte.
        """
        cantidad = cls.cantidad_necesaria(peso)
        if peso < 15000:
            costo_kg = 1
        else:
            costo_kg = 2
        return (cantidad * (cls.costos.fijo + cls.costos.km * distancia) + costo_kg * peso)


class Tren(Vehiculo):
    """
    Clase que representa un tren, hereda de Vehiculo.
    Atributos de clase:
        velocidad_nominal: Velocidad máxima del tren en km/h.
        capacidad: Capacidad de carga del tren en kg.
        costos: Costos asociados al uso del tren.
    """
    velocidad_nominal = 100
    capacidad = 150000
    costos = Costos(fijo=100, km=None, kg=3)

    @classmethod
    def calcular_tiempo(cls, distancia, restriccion):
        """
        Calcula el tiempo de viaje en horas, considerando restricciones de velocidad.
        Si la conexión tiene una restricción, se ajusta la velocidad nominal.""" 
        if restriccion is not None:
            velocidad = min(cls.velocidad_nominal, restriccion)
        else:
            velocidad = cls.velocidad_nominal
        return distancia / velocidad

    @classmethod
    def calcular_costo(cls, distancia, peso):
        """
        Calcula el costo total del transporte.
        El costo depende de la distancia y el peso, con un costo fijo y por kilómetro."""
        cantidad = cls.cantidad_necesaria(peso)
        if distancia < 200:
            costo_km = 20
        else:
            costo_km = 15
        return cantidad * (cls.costos.fijo + costo_km * distancia) + cls.costos.kg * peso
     

class Avion(Vehiculo):
    """
    Clase que representa un avión, hereda de Vehiculo.
    Atributos de clase:
        velocidad_nominal: Velocidad máxima del avión en km/h.
        capacidad: Capacidad de carga del avión en kg.
        costos: Costos asociados al uso del avión.
    """
    velocidad_nominal = 600
    capacidad = 5000
    costos = Costos(fijo=750, km=40, kg=10)

    @classmethod
    def calcular_tiempo(cls, distancia, restriccion):
        """
        Calcula el tiempo de viaje en horas, considerando restricciones de velocidad.
        Si la restriccion es un objeto de conexión, extrae el atributo .restriccion;
        si es un float, lo usa directamente como probabilidad.
        Si la probabilidad es None, vacía o no válida, asume 0.0.
        """
        
        prob = restriccion

        if prob is None or prob == "" or (isinstance(prob, str) and prob.lower() == "none"):
            prob = 0.0

        try:
            prob = float(prob)
        except Exception:
            prob = 0.0

        llueve = random.random() < prob
        velocidad = 400 if llueve else cls.velocidad_nominal
        return distancia / velocidad

    @classmethod
    def calcular_costo(cls, distancia, peso):
        """
        Calcula el costo total del transporte.
        El costo depende de la distancia y el peso, con un costo fijo y por kilómetro."""
        cantidad = cls.cantidad_necesaria(peso)
        if distancia < 1000:
            costo_km = 50
        else:
            costo_km = 40
        return cantidad * (cls.costos.fijo + costo_km * distancia) + cls.costos.kg * peso


class Barcaza(Vehiculo):
    """
    Clase que representa una barcaza, hereda de Vehiculo.
    Atributos de clase: 
        velocidad_nominal: Velocidad máxima de la barcaza en km/h.
        capacidad: Capacidad de carga de la barcaza en kg.
        costos: Costos asociados al uso de la barcaza.
    """
    velocidad_nominal = 40
    capacidad = 100000
    costos = Costos(fijo=None, km=15, kg=2)


    @classmethod
    def calcular_costo(cls, distancia, peso, restriccion):
        """
        Calcula el costo total del transporte.
        Si la restricción es "fluvial", se aplica un costo fijo diferente.
        """
        cantidad = cls.cantidad_necesaria(peso)

        if restriccion == "fluvial":
            costo_fijo = 500
        else:
            costo_fijo = 1500

        return cantidad * (costo_fijo + cls.costos.km * distancia) + cls.costos.kg * peso
    

def obtener_vehiculos_default():
    """Obtiene una lista de los vehículos por defecto.
    Returns:
        list: Lista de clases de vehículos.
    """
    return [Camion, Tren, Avion, Barcaza]

obtener_vehiculos_default()