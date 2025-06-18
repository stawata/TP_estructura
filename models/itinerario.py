class Itinerario():
    def __init__(self, modo, itinerario, costo_total, tiempo_total):
        """
        Clase que representa un itinerario de viaje.
        :param modo: El modo de transporte utilizado (por ejemplo, "coche", "tren", etc.).
        :param itinerario: Una lista de ciudades que componen el itinerario.
        :param costo_total: El costo total del itinerario.
        :param tiempo_total: El tiempo total del itinerario.
        """
        self.modo = modo
        self.itinerario = itinerario
        self.costo_total = costo_total
        self.tiempo_total = tiempo_total
    
    def __str__(self):
        return f"Itinerario: {self.modo}, Ciudades: {' --> '.join(self.itinerario)}, Costo Total: {self.costo_total}, Tiempo Total: {self.tiempo_total}"


