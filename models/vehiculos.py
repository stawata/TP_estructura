import math
#from validaciones.validaciones import validaciones

class Vehiculo():
    def __init__(self,modo,velocidad_nominal,capacidad,costo_fijo,costo_km,costo_kg):
    #    validaciones.validar_str(modo)
    #    validaciones.validar_float(velocidad_nominal)
    #    validaciones.validar_float(capacidad)
    #    validaciones.validar_float(costo_fijo)
    #    validaciones.validar_float(costo_kg)
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
        #no se calcula aca porque cada vehiculo tiene una restriccion
        """Calcula el costo total de utilizar el vehículo en un tramo, dado una distancia y una cantidad de carga."""

        raise NotImplementedError("Este método debe ser implementado por las subclases.")
        
    def puede_usar_conexion(self, conexion, peso=None):
        return conexion.tipo == self.modo
    """Evalúa si el vehículo puede usar una conexión determinada, según las restricciones propias del vehículo y del tramo"""

    def velocidad(self, conexion):
        if self.modo == "ferroviario" and conexion.velocidad_maxima is not None:
            return min(self.velocidad_nominal, conexion.velocidad_maxima)
        elif self.modo == "aereo" and conexion.prob_mal_clima is not None:
            # Ejemplo simple: si hay 30% de mal clima, reducimos 30% la velocidad
            return self.velocidad_nominal * (1 - conexion.prob_mal_clima)
        else:
            return self.velocidad_nominal


#Esta clase trabaja con Conexion para validar si puede recorrerla en la funcion "puede_usar_conexion"
#Ademas, con Solicitud para ver si puede cumplir el pedido y uso peso
