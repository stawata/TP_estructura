class Vehiculo():
    def __init__(self,modo,velocidad,capacidad,costo_fijo,costo_km,costo_kg):
       self.modo=modo
       self.velocidad=velocidad
       self.capacidad=capacidad
       self.costo_fijo=costo_fijo
       self.costo_km=costo_km
       self.costo_kg=costo_kg
      
    def __str__(self):
        return f"{self.nombre}"
    
    def calcular_tiempo():
        pass
        """Calcula el tiempo que tarda el vehículo en recorrer una cierta distancia (en km)."""
    
    def calcular_costo():
        pass
        """Calcula el costo total de utilizar el vehículo en un tramo, dado una distancia y una cantidad de carga."""

    def puede_usar_conexion():
        pass
        """Evalúa si el vehículo puede usar una conexión determinada, según las restricciones propias del vehículo y del tramo"""