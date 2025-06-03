from vehiculos import Vehiculo

class Camion(Vehiculo):
    def __init__(self, modo, velocidad_nominal, capacidad, costo_fijo, costo_km, costo_kg):
        super().__init__(modo, velocidad_nominal, capacidad, costo_fijo, costo_km, costo_kg)

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