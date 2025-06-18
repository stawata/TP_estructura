import math
#from validaciones.validaciones import validaciones

class Vehiculo():
    """
    Clase base para representar un vehículo de transporte.
    Atributos:
        modo: Modo de transporte (e.g., "terrestre", "aereo", "maritimo").
        velocidad_nominal: Velocidad máxima del vehículo en km/h.
        capacidad: Capacidad de carga del vehículo en kg.
        costo_fijo: Costo fijo asociado al uso del vehículo.
        costo_km: Costo por kilómetro recorrido.
        costo_kg: Costo por kilogramo transportado.
    """
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
        """
        Calcula la cantidad de vehículos necesarios para transportar un peso dado.
        """
        return math.ceil(peso/self.capacidad)
        
    def calcular_tiempo(self,distancia, restriccion):
        """
        Calcula el tiempo de viaje en horas, considerando restricciones de velocidad.
        """
        raise NotImplementedError("Este método debe ser implementado por las subclases.")
        
    def calcular_costo(self,distancia,peso):
        """
        Calcula el costo total del transporte.
        """
        raise NotImplementedError("Este método debe ser implementado por las subclases.")
        
    def puede_usar_conexion(self, conexion, peso=None):
        """
        Verifica si el vehículo puede usar una conexión dada, considerando restricciones de peso.
        """
        return conexion.tipo == self.modo
    

    def velocidad(self, conexion):
        """
        Calcula la velocidad efectiva del vehículo en una conexión dada, considerando restricciones específicas.
        """
        if self.modo == "ferroviario" and conexion.velocidad_maxima is not None:
            return min(self.velocidad_nominal, conexion.velocidad_maxima)
        elif self.modo == "aereo" and conexion.prob_mal_clima is not None:
            return self.velocidad_nominal * (1 - conexion.prob_mal_clima)
        else:
            return self.velocidad_nominal




