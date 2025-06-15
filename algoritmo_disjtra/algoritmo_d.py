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
        cantidad_vehiculos = 0
        tiempo = 0
        if solicitud.peso_kg > modo.capacidad:
            cantidad_vehiculos = math.ceil(solicitud.peso_kg / modo.capacidad)
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
                        if type(modo) == Tren:
                            Dijkstra.calculador_tiempo(ciudad, tiempo, tiempo_acarreado, diccionario_tiempos,objeto_base, modo, diccionario_tiempos_GLOBAL) # pasamos como parametro la velocidadmaxima y el metodo se encarga de definir cual es la menor velocidad entre la de la ruta o la nominal
                        elif type(modo) == Camion:                                                      #Calcula el tiempo que tarda el CAMION en recorrer la conexion apartir de la distancia
                            if ciudad[2] != None:
                                if ciudad[2] < solicitud.peso_kg:                               #Si el peso de la solicitud es mayor que es de a conexion se descarta la ruta
                                    print("la carga excede el peso admitido por la conexion")
                                    continue
                                else:  
                                    Dijkstra.calculador_tiempo(ciudad, tiempo, tiempo_acarreado, diccionario_tiempos,objeto_base, modo)
                            else:
                                Dijkstra.calculador_tiempo(ciudad, tiempo, tiempo_acarreado, diccionario_tiempos,objeto_base, modo)
                        elif type(modo) == Avion:
                            Dijkstra.calculador_tiempo(ciudad, tiempo, tiempo_acarreado, diccionario_tiempos,objeto_base, modo) #Calcula el tiempo que tarda el avion en recorrer la conexion apartir de la distancia
                        elif type(modo) == Barcaza:
                            Dijkstra.calculador_tiempo(ciudad, tiempo, tiempo_acarreado, diccionario_tiempos,objeto_base, modo) #Calcula el tiempo que tarda el BARCO en recorrer la conexion apartir de la distancia 
                    diccionario_ordenado = dict(sorted(diccionario_tiempos.items(), key=lambda item: item[1][0]))
                    for clave,valor in diccionario_ordenado.items():
                        if clave == destino:
                            llegada= False
                        recorrido.apilar(NodoCiudad(clave, valor[0], valor[1])) 
                        objeto_base = clave
                        tiempo_acarreado =  valor[0]
                        diccionario_tiempos.pop(clave)
                        break 
        return recorrido



    @staticmethod
    def camino_mas_rapido(pila, solicitud):
        destino = solicitud.destino.nombre
        resultado, tiempo = pila.recorrer_camino( destino)
        return resultado, tiempo

    @staticmethod
    def calculador_tiempo(ciudad , tiempo, tiempo_acarreado, diccionario_tiempos,objeto_base, modo,diccionario_tiempos_GLOBAL):
        tiempo = modo.calcular_tiempo(ciudad[1], ciudad[2])                                     #calcula el tiempo con la distancia, y si ciudad[2] es la velocidad maxima si es que existe
        tiempo_neto = tiempo + tiempo_acarreado
        if ciudad[0] not in diccionario_tiempos:
            diccionario_tiempos[ciudad[0]] = (tiempo_neto,objeto_base)
        elif tiempo_neto < diccionario_tiempos[ciudad[0]][0]:
            diccionario_tiempos[ciudad[0]] = (tiempo_neto,objeto_base)
        Dijkstra.agregar_diccionario_global(diccionario_tiempos_GLOBAL, objeto_base, tiempo, ciudad)
    
    @staticmethod
    def agregar_diccionario_global(diccionario_tiempos_GLOBAL, objeto_base, tiempo, ciudad):
        if objeto_base not in diccionario_tiempos_GLOBAL:
            diccionario_tiempos_GLOBAL[objeto_base] = [tiempo, ciudad[0]]
        else:
            diccionario_tiempos_GLOBAL[objeto_base].extend([tiempo, ciudad[0]])


    @staticmethod
    def mostrar_camino(resultado):
        print(f"El tiempo que tarda el recorrido es: {resultado[1]}")
        for valor in resultado[0]:
            print(f"La ciudad es: {valor.nombre}")



