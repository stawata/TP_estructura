'''Esta pila es un objeto que va a llevar un  conteo de los recorridos posibles para llegar al destino. Entocnes 
el primer nodo que ingresamos es el origen y luego vamos a ir agregando nodos siempre verificando que la pila que estamos formando 
sea una que todavia no existe. Quiere decir que la base de nuestra busqueda es que va a encontrar caminos diferentes fijandose que 
la pila que vamos armando sea una que todavia no existe. '''
#from utils.loader import ConexionLoader,NodoLoader,SolicitudLoader
from algoritmo_disjtra.pilas_2 import Pila
from models.nodo import Nodo
from models.solicitud import Solicitud 
from models.vehiculos_herencia import *
from utils.validaciones import validaciones
import math


class Grafo:
    def __init__(self, rutas, solicitud, modo ):
        rutas = Grafo.filtrar_por_modo(rutas,modo)
        grafo = self.armar_grafo(rutas)
        self.grafo = grafo
        recorrrido = Pila()
        dijstra = self.ruta_optima(solicitud,recorrrido,modo)
        resultado = Grafo.camino_mas_rapido(dijstra, solicitud)
        Grafo.mostrar_camino(resultado)
        



    def armar_grafo(self, ruta):
        grafo = {}
        indices = [0, 2, 3, 4, 5] 
        for lista in ruta:
            if lista[0] not in grafo: 
                grafo[lista[0]] =  [lista[1:]]
                if lista[1] not in grafo:
                    inverso = lista[2:]
                    inverso.insert(0, lista[0])  
                    grafo[lista[1]] = [inverso]  
                else:
                    grafo[lista[1]].append([lista[i] for i in indices if i < len(lista)])
            else:
                grafo[lista[0]].append(lista[1:])
                if lista[1] not in grafo:
                    inverso = lista[2:]
                    inverso.insert(0, lista[0])  
                    grafo[lista[1]] = [inverso]   
                else:
                    grafo[lista[1]].append([lista[i] for i in indices if i < len(lista)])
        return grafo

    def ruta_optima(self,solicitud,recorrido, modo):
        tiempo_acarreado = 0
        cantidad_vehiculos = 0
        if solicitud.peso_kg > modo.capacidad:
            cantidad_vehiculos = math.ceil(solicitud.peso_kg / modo.capacidad)
        destino = solicitud.destino.nombre
        recorrido.apilar(solicitud.origen)
        objeto_base = solicitud.origen.nombre
        llegada = True
        while llegada:
            diccionario_tiempos = {} 
            for clave, valor in self.grafo.items():
                if clave == objeto_base:   
                    for ciudad in valor:
                        if recorrido.recorrer_pila(ciudad[0]):
                            print("Ya es parte del recorrido esa ciudad")
                            continue
                        elif ciudad[3] == "peso_max":
                            if ciudad[-1] < solicitud.peso_kg:
                                print("la carga excede el peso admitido por la conexion")
                                continue
                            else:  
                                tiempo = modo.calcular_tiempo(ciudad[2])
                                tiempo_neto = tiempo + tiempo_acarreado
                                if ciudad[0] not in diccionario_tiempos:
                                    diccionario_tiempos[ciudad[0]] = (tiempo_neto,objeto_base)
                                elif tiempo_neto < diccionario_tiempos[ciudad[0]][0]:
                                    diccionario_tiempos[ciudad[0]] = (tiempo_neto,objeto_base)
                        else:
                            tiempo = modo.calcular_tiempo(ciudad[2])
                            tiempo_neto = tiempo + tiempo_acarreado
                            if ciudad[0] not in diccionario_tiempos:
                                diccionario_tiempos[ciudad[0]] = (tiempo_neto,objeto_base)
                            elif tiempo_neto < diccionario_tiempos[ciudad[0]][0]:
                                diccionario_tiempos[ciudad[0]] = (tiempo_neto,objeto_base)
                    diccionario_ordenado = dict(sorted(diccionario_tiempos.items(), key=lambda item: item[1][0]))
                    for clave,valor in diccionario_ordenado.items():
                        if clave == destino:
                            llegada= False
                        recorrido.apilar(Nodo(clave, valor[0], valor[1])) 
                        objeto_base = clave
                        tiempo_acarreado =  valor[0]
                        diccionario_tiempos.pop(clave)
                        break 
        recorrido.visualizar()
        return recorrido


    @staticmethod
    def camino_mas_rapido(pila, solicitud):
        origen = solicitud.origen.nombre
        destino = solicitud.destino.nombre
        resultado, tiempo = pila.recorrer_camino( destino)
        return resultado, tiempo


    @staticmethod
    def filtrar_por_modo(rutas, modo):
        if type(modo)== Camion:
            buscador = "Automotor"
            return list(filter(lambda x: x[2] == buscador, rutas))


    @staticmethod
    def mostrar_camino(resultado):
        print(f"El tiempo que tarda el recorrido es: {resultado[1]}")
        for valor in resultado[0]:
            print(f"La ciudad es: {valor.nombre}")



# nodos = NodoLoader.cargar_desde_csv("data/nodos.csv")
# solicitud = SolicitudLoader.cargar_desde_csv("solicitudes.csv")
# conexiones = ConexionLoader.cargar_desde_csv("conexiones.csv")

# grafo_info = {
#     "Zarate": [("Buenos Aires", 85, 100), ("Junin", 185, 80)],
#     "Buenos Aires": [("Zarate", 85, 100), ("Junin", 238, 90), ("Azul", 278, 110), ("Mar del Plata", 384, 120)],
#     "Junin": [("Zarate", 185, 80), ("Buenos Aires", 238, 90), ("Azul", 265, 100)],
#     "Azul": [("Junin", 265, 100), ("Buenos Aires", 278, 110), ("Mar del Plata", 246, 100)],
#     "Mar del Plata": [("Buenos Aires", 384, 120), ("Azul", 246, 100)]
# }

ruta = [
    ["Zarate", "Buenos_Aires", "Automotor", 85,  ""],
    ["Zarate", "Junin", "Automotor", 185, "peso_max", 15000],
    ["Junin", "Buenos_Aires", "Automotor", 238,  ""],
    ["Junin", "Azul", "Automotor", 265,  ""],
    ["Azul", "Buenos_Aires", "Automotor", 278,  ""],
    ["Azul", "Mar_del_Plata", "Automotor", 246,  ""],
    ["Buenos_Aires", "Mar_del_Plata", "Automotor", 384,  ""]
]

solicitud_1 = Solicitud("CARGA_001",70000,Nodo("Zarate",0, None),Nodo("Mar_del_Plata",0, None))
camion_1 = Camion()
recorrido = Grafo(ruta, solicitud_1, camion_1)