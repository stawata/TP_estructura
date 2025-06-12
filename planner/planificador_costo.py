import heapq
from planificadores.planificador_base import Planificador
from planificadores.utils import construir_grafo, calcular_costo_tramo, calcular_vehiculos_requeridos

class PlanificadorCosto(Planificador):
    def generar_itinerarios(self, solicitud):
        nodos_dict = {n.nombre: n for n in self.nodos}
        grafo = construir_grafo(self.conexiones, nodos_dict)
        origen = solicitud.origen
        destino = solicitud.destino
        peso = solicitud.peso

        # heap: (costo acumulado, nodo actual, camino recorrido [(Conexion, Vehiculo)])
        heap = [(0, origen, [])]
        visitados = set()

        while heap:
            costo_actual, nodo_actual, camino = heapq.heappop(heap)
            if nodo_actual == destino:
                return self._formatear_itinerario(camino, costo_actual)

            if nodo_actual in visitados:
                continue
            visitados.add(nodo_actual)

            for conexion in grafo[nodo_actual]:
                for veh in self.vehiculos:
                    if veh.modo == conexion.tipo and conexion.es_valida(veh, peso):
                        costo_tramo = calcular_costo_tramo(conexion.distancia_km, peso, veh)
                        nuevo_camino = camino + [(conexion, veh)]
                        heapq.heappush(heap, (costo_actual + costo_tramo, conexion.destino, nuevo_camino))

        return None  # No hay camino

    def _formatear_itinerario(self, camino, costo_total):
        return {
            "itinerario": [(c.origen, c.destino, v.tipo) for c, v in camino],
            "costo_total": costo_total,
            "kpi": "costo"
        }

