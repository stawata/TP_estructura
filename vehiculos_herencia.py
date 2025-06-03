from vehiculos import Vehiculo
from clase_solicitud import Solicitud

class Camion(Vehiculo):
    def __init__(self,costo_kg):
        #El costo_kg varia segun la carga de la solicitud, ver como hacer
        super().__init__(modo="automotor",velocidad_nominal= 80,capacidad= 30000,costo_fijo= 30,costo_km= 5,costo_kg=costo_kg)
        

class Tren(Vehiculo):
    def __init__(self, modo, velocidad_nominal, capacidad, costo_fijo, costo_km, costo_kg):
        super().__init__(modo, velocidad_nominal, capacidad, costo_fijo, costo_km, costo_kg)

class Avion(Vehiculo):
    #aca hay un metodo en caso de malas condiciones climaticas
    def __init__(self, modo, velocidad_nominal, capacidad, costo_fijo, costo_km, costo_kg):
        super().__init__(modo, velocidad_nominal, capacidad, costo_fijo, costo_km, costo_kg)

    

class Barcaza(Vehiculo):
    def __init__(self, modo, velocidad_nominal, capacidad, costo_fijo, costo_km, costo_kg):
        super().__init__(modo, velocidad_nominal, capacidad, costo_fijo, costo_km, costo_kg)