import heapq

class Dijkstra:
    @staticmethod
    def dijkstra(puntos_red, origen, usar="tiempo"):
        """
        puntos_red: dict[str, PuntoDeRed]
        origen: str (nombre del punto de inicio)
        usar: "tiempo" o "costo", define qué KPI se va a optimizar
        """
        dist = {nombre: float("inf") for nombre in puntos_red}
        anterior = {nombre: None for nombre in puntos_red}
        dist[origen] = 0
        heap = [(0, origen)]  # (distancia acumulada, nombre del punto actual)

        while heap:
            actual_dist, actual = heapq.heappop(heap)
            for vecino, (costo, tiempo) in puntos_red[actual].vecinos.items():
                peso = tiempo if usar == "tiempo" else costo
                nueva_dist = actual_dist + peso
                if nueva_dist < dist[vecino.nombre]:
                    dist[vecino.nombre] = nueva_dist
                    anterior[vecino.nombre] = actual
                    heapq.heappush(heap, (nueva_dist, vecino.nombre))

        return dist, anterior
    
    @staticmethod
    def ruta_mas_corta(puntos_red, origen, destino, usar="tiempo"):
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
        return ruta, distancias[destino]
