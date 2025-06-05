from vehiculos import Vehiculo
from clase_solicitud import Solicitud

class Camion(Vehiculo):
    def __init__(self,costo_kg):
        #El costo_kg varia segun la carga de la solicitud, ver como hacer
        super().__init__(modo="automotor",velocidad_nominal= 80,capacidad= 30000,costo_fijo= 30,costo_km= 5,costo_kg=costo_kg)
        

class Tren(Vehiculo):
    def __init__(self,costo_km):
        #El costo_km varia segun la distancia del tramo
        super().__init__(modo= "ferroviario", velocidad_nominal=100, capacidad=150000, costo_fijo=100, costo_kg=3, costo_km=costo_km)

class Avion(Vehiculo):
    def __init__(self,velocidad_nominal):
        #aca hay un metodo en caso de malas condiciones climaticas
        super().__init__(modo="aereo", velocidad_nominal= velocidad_nominal, capacidad=5000 , costo_fijo=750 , costo_km= 40, costo_kg= 10)

class Barcaza(Vehiculo):
    def __init__(self,costo_fijo):
        #El costo fijo varia segun la tasa fluvial o marítima1
        super().__init__(modo="maritimo", velocidad_nominal= 40, capacidad=100000 , costo_fijo=costo_fijo, costo_km= 15, costo_kg= 2)