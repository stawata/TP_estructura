import heapq

class Dijkstra:
    @staticmethod
    def dijkstra(puntos_red, origen, usar):
        """
        puntos_red: dict[str, PuntoDeRed]
        origen: str
        usar: "tiempo" o "costo"
        Heap es un módulo proporciona una implementación del algoritmo de cola de montón , también conocido como algoritmo de cola de prioridad.
        Los montículos son árboles binarios en los que cada nodo padre tiene un valor menor o igual que el de cualquiera de sus hijos.
        En nuestro caso utlizamos el heap como una estructura de datos especial que permite acceder siempre al elemento más pequeño (mínimo) en tiempo
        eficiente  para insertar o quitar).
        Funcionamiento: 
        1. Creamos un diccionario (dist) que va a almacenar todos los puntos de red, utlizando el nombre como clave  y un tupla como valor, la tupla tiene 2 elementos uno es el costo
        y el otro es el tiempo.Inicializandolos con valores infinitos.
        2. Establece anterior que es un diccionario que alamcena como clave el nombre de la ciudad y como valor la ciudad previa.
        3. En el diciconario dist definimos al nodo origen con tiempo y costo 0
        4. Crea un heap que es un cola de  prioridad que almacena tuplas con un elemento(costo o tiempo) y el segundo elemento es el nombre de  la ciudad
        5. Inicializamos el algoritmo con un  while que se ejecute hasta que heap este vacio
        6.heapq.heappop es un metodo de la clase heapq que se encarga de devolverte la tupla de menor prioridad, quiere decir al tener dos tuplas se canalizara la tupla que en su
        elemento 1 sea menor que el resto.Ejemplo: heap = [(0.25, Buenos Aires),(0.02, Mar del Plata)] ==> (0.02, Mar del Plata)  
        7. Obtiene la tupla del diccionario dist posicionado en actual
        8. Realiza un FOR para itera sobre los puntos vecinos de actual, almacenara el nombre, costo nuevo y tiempo nuevo. Estos ultimos 2 valores se obtienen sumando el costo/tiempo que se obtiene 
        de puntos de red(dict) y el costo/tiempo que acontece en el diccionario local(dist) explicado del punto 7.
        9. Utiliza condicional para visualizar cual es el filtro que queremos realizar(costo o tiempo)
        10. Analiza si el costo/tiempo que se obtuvo en el punto 8 es menor que el costo/tiempo que existia en el diccionario(dist) poscionado en el punto vecino. Si  asi es el caso cambiamos 
        el valor de costo/tiempo en el diccionario (dist)
        11. Establece el previo de la ciudad actual en el diccionario anteriores
        12. Con heapq.heappush ,creamos un nuevo elemento en la cola de prioridad heap que tendra el tiempo/costo actualizado y el nombre del vecino al que modifico. 
        13. Repite el proceso
        """
        dist = {nombre: (float("inf"), float("inf")) for nombre in puntos_red}
        anterior = {nombre: None for nombre in puntos_red}
        dist[origen] = (0, 0)
        heap = [(0, origen)]  # prioridad según KPI

        while heap:
            _, actual = heapq.heappop(heap)
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
            return None, None, None, None
        
        return modo, ruta, costo_total, tiempo_total
