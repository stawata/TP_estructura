import math
from models.vehiculos_herencia import *
from algoritmo_disjtra.pilas_2 import Pila
from algoritmo_disjtra.Nodo_ciudad import NodoCiudad


class Dijkstra:
    @staticmethod
    def analizador_ruta_tiempos(grafo, solicitud, modo ):
        recorrrido = Pila()
        pila_recorrido = Dijkstra.ruta_optima(grafo,solicitud,recorrrido,modo)
        resultado = Dijkstra.camino_mas_rapido(pila_recorrido, solicitud)
        Dijkstra.mostrar_camino(resultado)
    
    @staticmethod
    def ruta_optima(grafo,solicitud,recorrido, modo):
        tiempo_acarreado = 0
        tiempo = 0
        destino = solicitud.destino.nombre
        recorrido.apilar(solicitud.origen)
        objeto_base = solicitud.origen.nombre
        llegada = True
        while llegada:
            diccionario_tiempos = {} 
            diccionario_tiempos_GLOBAL = {}
            for clave, valor in grafo.items():
                if clave == objeto_base:   
                    for ciudad in valor:
                        if recorrido.recorrer_pila(ciudad[0]): # se fija si la ciudad ya esta en la pila
                            print("Ya es parte del recorrido esa ciudad")
                            continue
                        tiempo = Dijkstra.calculador_tiempo(ciudad, tiempo, tiempo_acarreado, diccionario_tiempos,objeto_base, modo) # pasamos como parametro la velocidadmaxima y el metodo se encarga de definir cual es la menor velocidad entre la de la ruta o la nominal
                        Dijkstra.agregar_diccionario_global(diccionario_tiempos_GLOBAL, objeto_base, tiempo, ciudad)
                        if type(modo) == Camion:                                                      #Calcula el tiempo que tarda el CAMION en recorrer la conexion apartir de la distancia
                                if ciudad[2] < solicitud.peso_kg:                               #Si el peso de la solicitud es mayor que es de a conexion se descarta la ruta
                                    print("la carga excede el peso admitido por la conexion")
                                    continue
                                else:  
                                    Dijkstra.calculador_tiempo(ciudad, tiempo, tiempo_acarreado, diccionario_tiempos,objeto_base, modo)
                    diccionario_ordenado = dict(sorted(diccionario_tiempos.items(), key=lambda item: item[1][0])) #ordena el diccionario para quedarse con la ciudad de menor tiempo en el tope
                    for clave,valor in diccionario_ordenado.items():
                        if clave == destino:
                            llegada= False
                        recorrido.apilar(NodoCiudad(clave, valor[0], valor[1]))                         #apilo la ciudad 
                        objeto_base = clave                                                             #muevo la base a la ciduad de menor tiempo
                        tiempo_acarreado =  valor[0]                                                    #cambio el tiempo acarreado
                        diccionario_tiempos.pop(clave)
                        break 
        return recorrido

    @staticmethod
    def camino_mas_rapido(pila, solicitud):
        destino = solicitud.destino.nombre
        resultado, tiempo = pila.recorrer_camino( destino)
        return resultado, tiempo

    @staticmethod
    def calculador_tiempo(ciudad , tiempo, tiempo_acarreado, diccionario_tiempos,objeto_base, modo):
        tiempo = modo.calcular_tiempo(ciudad[1], ciudad[2])                                     #calcula el tiempo con la distancia, y si ciudad[2] es la velocidad maxima si es que existe
        tiempo_neto = tiempo + tiempo_acarreado
        if ciudad[0] not in diccionario_tiempos:
            diccionario_tiempos[ciudad[0]] = (tiempo_neto,objeto_base)
        elif tiempo_neto < diccionario_tiempos[ciudad[0]][0]:
            diccionario_tiempos[ciudad[0]] = (tiempo_neto,objeto_base)
        tiempo_dic = tiempo_neto - tiempo_acarreado
        return tiempo_dic
    
    @staticmethod
    def agregar_diccionario_global(diccionario_tiempos_GLOBAL, objeto_base, tiempo, ciudad):
        if objeto_base not in diccionario_tiempos_GLOBAL:
            diccionario_tiempos_GLOBAL[objeto_base] = [tiempo, ciudad[0]]
        else:
            diccionario_tiempos_GLOBAL[objeto_base].append([tiempo, ciudad[0]] )

    @staticmethod
    def mostrar_camino(resultado):
        print(f"El tiempo que tarda el recorrido es: {resultado[1]}")
        for valor in resultado[0]:
            print(f"La ciudad es: {valor.nombre}")

    @staticmethod
    def encontrar_todos_los_caminos(grafo, origen, destino, modo):
        caminos = []
        Dijkstra._dfs(grafo, origen, destino, modo, [], set(), 0, caminos)
        return caminos

    @staticmethod
    def _dfs(grafo, actual, destino, modo, camino_actual, visitados, tiempo_total, caminos):
        visitados.add(actual)
        camino_actual.append((actual, tiempo_total))

        if actual == destino:
            caminos.append(list(camino_actual))
        else:
            for vecino in grafo.get(actual, []):
                ciudad_destino = vecino[0]
                if ciudad_destino not in visitados:
                    tiempo = modo.calcular_tiempo(vecino[1], vecino[2])
                    Dijkstra._dfs(grafo, ciudad_destino, destino, modo, camino_actual, visitados, tiempo_total + tiempo, caminos)

        # backtracking
        visitados.remove(actual)
        camino_actual.pop()


