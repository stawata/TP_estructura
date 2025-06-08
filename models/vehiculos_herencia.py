from models.vehiculos import Vehiculo
from models.solicitud import Solicitud
import random

class Camion(Vehiculo):
    def __init__(self):
        #El costo_kg varia segun la carga de la solicitud, ver como hacer
        super().__init__(modo="automotor",velocidad_nominal= 80,capacidad= 30000,costo_fijo= 30,costo_km= 5,costo_kg=None) #Le pongo None porque total lo calculo despues
        
    def calcular_tiempo(self,distancia):
        return distancia / self.velocidad_nominal
    
    def calcular_costo(self, distancia, peso):
        cantidad = self.cantidad_necesaria(peso)
        if peso < 15000:
            costo_kg = 1
        else: 
            costo_kg = 2

        return cantidad * (self.costo_fijo + self.costo_km * distancia + costo_kg * peso)

    def puede_usar_conexion(self, conexion, peso):
        if not super().puede_usar_conexion(conexion, peso):
            return False
        if hasattr(conexion, "peso_max") and conexion.peso_max is not None:
            if peso > conexion.peso_max:
                return False
        return True


class Tren(Vehiculo):
    def __init__(self):
        super().__init__(modo= "ferroviario", velocidad_nominal=100, capacidad=150000, costo_fijo=100, costo_kg=3, costo_km=None)

    def calcular_tiempo(self, distancia, conexion=None):
        if conexion and hasattr(conexion, "velocidad_max") and conexion.velocidad_max is not None:
            velocidad = min(self.velocidad_nominal, conexion.velocidad_max)
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
        
        return cantidad * (self.costo_fijo + costo_km * distancia + self.costo_kg * peso)
    
    

class Avion(Vehiculo):
    def __init__(self):
        super().__init__(modo="aereo", velocidad_nominal=600, capacidad=5000 , costo_fijo=750 , costo_km= 40, costo_kg= 10)

    def calcular_tiempo(self, distancia, conexion):
        prob = conexion.probabilidad_mal_clima #Aca me voy a buscar la probabilidad de lluvia, si hubiera
        llueve = random.random() < prob #Si el random que genero me da menor a la probababilidad, va a llover 
        if llueve:
            velocidad = 400
        else:
            velocidad = self.velocidad_nominal
        
        return distancia / velocidad

    def calcular_costo(self, distancia, peso):
        cantidad = self.cantidad_necesaria(peso)
        return cantidad * (self.costo_fijo + self.costo_km * distancia + self.costo_kg * peso)

class Barcaza(Vehiculo):
    def __init__(self):
        #El costo fijo varia segun la tasa fluvial o marítima1
        super().__init__(modo="maritimo", velocidad_nominal= 40, capacidad=100000 , costo_fijo=None, costo_km= 15, costo_kg= 2)

    def calcular_tiempo(self,distancia):    
        return distancia / self.velocidad_nominal
    
    def calcular_costo(self, distancia, peso, conexion):
        cantidad = self.cantidad_necesaria(peso)
    
        if conexion.tipo_tasa == "fluvial":
            costo_fijo = 500
        else:
            costo_fijo = 1500

        return cantidad * (costo_fijo + self.costo_km * distancia + self.costo_kg * peso)
