'''Esta pila es un objeto que va a llevar un  conteo de los recorridos posibles para llegar al destino. Entocnes 
el primer nodo que ingresamos es el origen y luego vamos a ir agregando nodos siempre verificando que la pila que estamos formando 
sea una que todavia no existe. Quiere decir que la base de nuestra busqueda es que va a encontrar caminos diferentes fijandose que 
la pila que vamos armando sea una que todavia no existe. '''
#from utils.loader import ConexionLoader,NodoLoader,SolicitudLoader
from pilas_2 import Nodo, Pila

class Buscar_ruta:
    def __init__(self, rutas, origen,destino ):
        nodo_origen = Nodo(origen)
        self.origen = origen
        self.destino = destino
        pila_modo = Pila()
        self.pila_recorrido = pila_modo
        self.pila_recorrido.apilar(nodo_origen)
        rutas_modo = Buscar_ruta.filtrar_por_modo(rutas)
        self.rutas_modo = rutas_modo
        self.filtrar_ruta()

    def filtrar_ruta(self):
        lista_nodo_destino = list(filter(lambda x: x[0] == self.origen, self.rutas_modo))
        for valor in lista_nodo_destino:
            if not self.pila_recorrido.recorrer(valor[1]):
                self.pila_recorrido.apilar(Nodo(valor[1]))
                self.origen = valor[1]   
                self.filtrar_ruta()    
            self.pila_recorrido.visualizar() 
      
            
    @staticmethod
    def filtrar_por_modo(rutas, modo="Automotor"):
        return list(filter(lambda x: x[2] == modo, rutas))



# nodos = NodoLoader.cargar_desde_csv("data/nodos.csv")
# solicitud = SolicitudLoader.cargar_desde_csv("solicitudes.csv")
# conexiones = ConexionLoader.cargar_desde_csv("conexiones.csv")
"""class Grafo:
    def __init__(self):
        self.adyacencias = {}  # Diccionario: nodo -> lista de (vecino, peso)

    def agregar_arista(self, origen, destino, distancia):
        if origen not in self.adyacencias:
            self.adyacencias[origen] = []
        self.adyacencias[origen].append((destino, distancia))

    def mostrar_grafo(self):
        for origen, vecinos in self.adyacencias.items():
            for destino, distancia in vecinos:
                print(f"{origen} -> {destino} ({distancia} km)")

# Crear el grafo
grafo = Grafo()

# Agregar las rutas de la red automotor (según la imagen)
grafo.agregar_arista("Zárate", "Buenos Aires", 85)
grafo.agregar_arista("Zárate", "Junín", 185)
grafo.agregar_arista("Junín", "Buenos Aires", 238)
grafo.agregar_arista("Junín", "Azul", 265)
grafo.agregar_arista("Azul", "Buenos Aires", 278)
grafo.agregar_arista("Azul", "Mar del Plata", 246)
grafo.agregar_arista("Buenos Aires", "Mar del Plata", 384)

# Mostrar el grafo
grafo.mostrar_grafo()
"""

ruta = [
    ["Zarate", "Buenos_Aires", "Automotor", 85,  ""],
    ["Zarate", "Junin", "Automotor", 185, "peso_max", 15000],
    ["Junin", "Buenos_Aires", "Automotor", 238,  ""],
    ["Junin", "Azul", "Automotor", 265,  ""],
    ["Azul", "Buenos_Aires", "Automotor", 278,  ""],
    ["Azul", "Mar_del_Plata", "Automotor", 246,  ""],
    ["Buenos_Aires", "Mar_del_Plata", "Automotor", 384,  ""]
]

solicitud = ["CARGA_001",70000,"Zarate","Mar_del_Plata"]
Buscar_ruta(ruta, solicitud[2],solicitud[3])