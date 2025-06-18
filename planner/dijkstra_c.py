import heapq
from models.itinerario import Itinerario

class Dijkstra:
    @staticmethod
    def dijkstra(puntos_red, origen, usar):
        """
        puntos_red: dict[str, PuntoDeRed]
        origen: str
        usar: "tiempo" o "costo"
        """
        dist = {nombre: (float("inf"), float("inf")) for nombre in puntos_red}
        anterior = {nombre: None for nombre in puntos_red}
        dist[origen] = (0, 0)
        heap = [(0, origen)]  # prioridad según KPI

        while heap:
            prioridad, actual = heapq.heappop(heap)
            costo_actual, tiempo_actual = dist[actual]

            for vecino, (costo, tiempo) in puntos_red[actual].vecinos.items():
                nombre_vecino = vecino.nombre
                nuevo_costo = costo_actual + costo
                nuevo_tiempo = tiempo_actual + tiempo

                if usar == "costo":
                    nueva_prio = nuevo_costo
                else:
                    nueva_prio = nuevo_tiempo

                costo_guardado, tiempo_guardado = dist[nombre_vecino]

                if nueva_prio < (costo_guardado if usar == "costo" else tiempo_guardado):
                    dist[nombre_vecino] = (nuevo_costo, nuevo_tiempo)
                    anterior[nombre_vecino] = actual
                    heapq.heappush(heap, (nueva_prio, nombre_vecino))

        return dist, anterior

    
    @staticmethod
    def ruta_mas_corta(puntos_red, origen, destino, usar, modo):
        """
        puntos_red: dict[str, PuntoDeRed]
        origen: str (nombre del punto de inicio)
        destino: str (nombre del punto de destino)
        usar: "tiempo" o "costo", define qué KPI se va a optimizar
        """
        distancias, anteriores = Dijkstra.dijkstra(puntos_red, origen, usar)
        ruta = []
        actual = destino
        while actual is not None:
            ruta.append(actual)
            actual = anteriores[actual]
        ruta.reverse()
        costo_total, tiempo_total = distancias[destino]
        if costo_total == float("inf") or tiempo_total == float("inf"):
            return None
        return Itinerario(modo, ruta, costo_total, tiempo_total)  
