from vehiculos import Vehiculo
from clase_solicitud import Solicitud

class Camion(Vehiculo):
    def __init__(self,costo_kg):
        #El costo_kg varia segun la carga de la solicitud, ver como hacer
        super().__init__(modo="automotor",velocidad_nominal= 80,capacidad= 30000,costo_fijo= 30,costo_km= 5,costo_kg=costo_kg)
        

class Tren(Vehiculo):
    def __init__(self):
        super().__init__(modo= "ferroviario", velocidad_nominal=100, capacidad=150000, costo_fijo=100, costo_km=20, costo_kg=3)

class Avion(Vehiculo):
    #aca hay un metodo en caso de malas condiciones climaticas
    def __init__(self):
        super().__init__(modo="aereo", velocidad_nominal= 5000, capacidad=5000 , costo_fijo=750 , costo_km= 40, costo_kg= 10)

    

class Barcaza(Vehiculo):
    def __init__(self):
        super().__init__(modo="maritimo", velocidad_nominal= 40, capacidad=100000 , costo_fijo= 500, costo_km= 15, costo_kg= 2)