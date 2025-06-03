import math

class Vehiculo():
    def __init__(self,modo,velocidad_nominal,capacidad,costo_fijo,costo_km,costo_kg):
       self.modo=modo
       self.velocidad_nominal=velocidad_nominal
       self.capacidad=capacidad
       self.costo_fijo=costo_fijo
       self.costo_km=costo_km
       self.costo_kg=costo_kg
      
    def __str__(self):
        return f"Este vehículo tiene el modo: {self.modo}"
    
    def cantidad_necesaria(self,peso):
        """Aca ves segun la capacidad del vehiculo cuantas unidades necesitas del mismo, nos sirve para calcular el costo en las hijas"""
        
        return math.ceil(peso/self.capacidad)
        
    def calcular_tiempo(self,distancia):
        """Calcula el tiempo que tarda el vehículo en recorrer una cierta distancia (en km)."""
        """Acá que tener cuidado con las condiciones especiales de cada uno para esta funcion"""
        
        raise NotImplementedError("Este método debe ser implementado por las subclases.")
        
    def calcular_costo(self,distancia,peso):
        """Calcula el costo total de utilizar el vehículo en un tramo, dado una distancia y una cantidad de carga."""
        
        raise NotImplementedError("Este método debe ser implementado por las subclases.")
        
    def puede_usar_conexion(self):
        """Evalúa si el vehículo puede usar una conexión determinada, según las restricciones propias del vehículo y del tramo"""
        
        raise NotImplementedError("Este método debe ser implementado por las subclases.")


#Esta clase trabaja con Conexion para validar si puede recorrerla en la funcion "puede_usar_conexion"
#Ademas, con Solicitud para ver si puede cumplir el pedido y uso peso
