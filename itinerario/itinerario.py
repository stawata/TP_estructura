class Itinerario():
    def __init__(self, solucion, modo, itinerario, costo_total, tiempo_total):
        self.solucion = solucion
        self.modo = modo
        self.itinerario = itinerario
        self.costo_total = costo_total
        self.tiempo_total = tiempo_total
    
    @staticmethod
    def creador_de_rutas(pila):
        pass

    def agregar_diccionario_global(diccionario_tiempos_GLOBAL, objeto_base, tiempo, ciudad):
        if objeto_base not in diccionario_tiempos_GLOBAL:
            diccionario_tiempos_GLOBAL[objeto_base] = [tiempo, ciudad[0]]
        else:
            diccionario_tiempos_GLOBAL[objeto_base].extend([tiempo, ciudad[0]])
