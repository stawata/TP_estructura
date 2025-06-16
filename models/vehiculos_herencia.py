from models.vehiculos import Vehiculo
from models.solicitud import Solicitud
import random
from collections import namedtuple #Es una tupla mas facil de acceder, mas entendible en realidad

Costos = namedtuple("Costos", ["fijo", "km", "kg"])

class Camion(Vehiculo):
    def __init__(self):
        super().__init__(modo="automotor", velocidad_nominal=80, capacidad=30000,
                         costo_fijo=None, costo_km=None, costo_kg=None)  # solo para completar
        self.costos = Costos(fijo=30, km=5, kg=None) 

    
    def calcular_tiempo(self,distancia):
        return distancia / self.velocidad_nominal
    
    def calcular_costo(self, distancia, peso):
        cantidad = self.cantidad_necesaria(peso)
        if peso < 15000:
            costo_kg = 1
        else: 
            costo_kg = 2

        return cantidad * (self.costos.fijo + self.costos.km * distancia + costo_kg * peso)

    def puede_usar_conexion(self, conexion, peso):
        if not super().puede_usar_conexion(conexion, peso):
            return False
        if hasattr(conexion, "peso_max") and conexion.peso_max is not None:
            if peso > conexion.peso_max:
                return False
        return True


class Tren(Vehiculo):
    def __init__(self):
        super().__init__(modo="ferroviario", velocidad_nominal=100, capacidad=150000,
                         costo_fijo=None, costo_km=None, costo_kg=None)
        self.costos = Costos(fijo=100, km=None, kg=3)

    def calcular_tiempo(self, distancia,velocidad_max ):
        if velocidad_max is not None:
            velocidad = min(self.velocidad_nominal, velocidad_max)
        else:
            velocidad = self.velocidad_nominal
        return distancia / velocidad
    #Calculaa el tiempo segun tenga velocidad maxima la conexion o no
    
    def calcular_costo(self, distancia, peso):
        cantidad = self.cantidad_necesaria(peso)
        if distancia < 200:
            costo_km = 20
        else:
            costo_km = 15
        
        return cantidad * (self.costos.fijo + costo_km * distancia + self.costos.kg * peso)    
    

class Avion(Vehiculo):
    def __init__(self):
        super().__init__(modo="aereo", velocidad_nominal=600, capacidad=5000,
                         costo_fijo=None, costo_km=None, costo_kg=None)
        self.costos = Costos(fijo=750, km=40, kg=10)

    def calcular_tiempo(self, distancia,probabilidad_mal_clima):
        prob = probabilidad_mal_clima #Aca me voy a buscar la probabilidad de lluvia, si hubiera
        llueve = random.random() < prob #Si el random que genero me da menor a la probababilidad, va a llover 
        if llueve:
            velocidad = 400
        else:
            velocidad = self.velocidad_nominal
        
        return distancia / velocidad

    def calcular_costo(self, distancia, peso):
        cantidad = self.cantidad_necesaria(peso)
        return cantidad * (self.costos.fijo + self.costos.km * distancia + self.costos.kg * peso)

class Barcaza(Vehiculo):
    def __init__(self):
        #El costo fijo varia segun la tasa fluvial o marítima1
        super().__init__(modo="maritimo", velocidad_nominal=40, capacidad=100000,
                         costo_fijo=None, costo_km=None, costo_kg=None)
        self.costos = Costos(fijo=None, km=15, kg=2)

    def calcular_tiempo(self,distancia):    
        return distancia / self.velocidad_nominal
    
    def calcular_costo(self, distancia, peso, conexion):
        cantidad = self.cantidad_necesaria(peso)
    
        if conexion.tipo_tasa == "fluvial":
            costo_fijo = 500
        else:
            costo_fijo = 1500

        return cantidad * (costo_fijo + self.costos.km * distancia + self.costos.kg * peso)

def obtener_vehiculos_default():
    return [Camion(), Tren(), Avion(), Barcaza()]