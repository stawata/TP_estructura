from models.vehiculos_herencia import *
class DFS:
    @staticmethod
    def encontrar_todos_los_caminos(grafo, solicitud, modo):
        caminos = []
        DFS._dfs(grafo, solicitud.origen.nombre, solicitud.destino.nombre, modo, [], set(), 0, caminos)
        return caminos

    @staticmethod
    def _dfs(grafo, actual, destino, modo, camino_actual, visitados, tiempo_total, caminos):
        visitados.add(actual)
        camino_actual.append((actual, tiempo_total))

        if actual == destino:
            caminos.append(list(camino_actual))
        else:
            for vecino in grafo.get(actual, []):  #Recorro todos los vecinos del nodo actual, si los tiene. Si no tiene, no recorro nada.
                ciudad_destino = vecino[0]
                distancia = vecino[1]
                restriccion = vecino[2]

                if ciudad_destino not in visitados:
                    # Verificamos restricciones (por ejemplo, peso para Camión
                    if restriccion is not None and type(modo) == Camion and restriccion > modo.capacidad:
                        continue
                    tiempo = modo.calcular_tiempo(distancia, restriccion)
                    DFS._dfs(grafo, ciudad_destino, destino, modo, camino_actual, visitados, tiempo_total + tiempo, caminos)

        # backtrack
        visitados.remove(actual)
        camino_actual.pop()
        return caminos
