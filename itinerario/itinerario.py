class Itinerarrio():
    def __init__(self, solucion, modo, itinerario, costo_total, tiempo_total):
        self.solucion = solucion
        self.modo = modo
        self.itinerario = itinerario
        self.costo_total = costo_total
        self.tiempo_total = tiempo_total
    
    @staticmethod
    def creador_de_rutas(pila):
        pass