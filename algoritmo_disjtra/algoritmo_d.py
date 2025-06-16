import math
from models.vehiculos_herencia import *
from algoritmo_disjtra.pilas_2 import Pila
from algoritmo_disjtra.Nodo_ciudad import NodoCiudad


class Dijkstra:
    @staticmethod
    def analizador_ruta_tiempos(grafo, solicitud, modo ):
        recorrrido = Pila()         # creamos una pila para almacenar todas los nodos que vayamos recorriendo
        respuesta = Dijkstra.origen_destino(grafo, solicitud) #validamos que si el destino o el origen no tienen ninguna conexion no puede relaizarse dikstra
        if not respuesta:
            raise ValueError("El grafo tiene una ciudad en el origen o destino que esta a la deriva")  #verificamos que el grafo no este a la deriva
        pila_recorrido = Dijkstra.ruta_optima(grafo,solicitud,recorrrido,modo)              #calculamos la ruta optima de tiempo
        resultado = Dijkstra.camino_mas_rapido(pila_recorrido, solicitud)                       #enlazamos los caminos, observando el previo de cada nodo
        Dijkstra.mostrar_camino(resultado)                                                            #mostramos el camino mas rapido
    
    @staticmethod
    def ruta_optima(grafo,solicitud,recorrido, modo):
        tiempo_acarreado = 0
        tiempo = 0
        destino = solicitud.destino.nombre          
        recorrido.apilar(solicitud.origen)                  #Almacenamos en la pila el nodo de origen
        objeto_base = solicitud.origen.nombre               #nos paramos en el nodo de origen como objeto base
        llegada = True
        while llegada:
            diccionario_tiempos = {}                    # es este diccionario almacenamos el tiempo que conllve la ciudad
            for clave, valor in grafo.items():              #empezamos a iterar sobre el grafo
                if clave == objeto_base:                    #vemos si la clave coincide con el objeto base que definimos anteriormente
                    for conexion in valor:
                        if recorrido.recorrer_pila(conexion[0]): # se fija si la ciudad ya esta en la pila
                            print("Ya es parte del recorrido esa ciudad")
                            continue
                        tiempo = Dijkstra.calculador_tiempo(conexion, tiempo, tiempo_acarreado, diccionario_tiempos,objeto_base, modo) # pasamos como parametro la velocidadmaxima y el metodo se encarga de definir cual es la menor velocidad entre la de la ruta o la nominal
                    if type(modo) == Camion:                                                      #Calcula el tiempo que tarda el CAMION en recorrer la conexion apartir de la distancia
                        if conexion[2] < solicitud.peso_kg:                               #Si el peso de la solicitud es mayor que es de a conexion se descarta la ruta
                            print("la carga excede el peso admitido por la conexion")
                            continue
                        else:  
                            Dijkstra.calculador_tiempo(conexion, tiempo, tiempo_acarreado, diccionario_tiempos,objeto_base, modo)
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
    def origen_destino(grafo, solicitud):
        origen = solicitud.origen.nombre
        destino = solicitud.destino.nombre
        estado = True
        for clave, valor in grafo.items():
            if clave == origen or clave == destino:
                if valor == []:
                    estado = False
        return estado



    @staticmethod
    def camino_mas_rapido(pila, solicitud):
        destino = solicitud.destino.nombre
        resultado, tiempo = pila.recorrer_camino( destino)
        return resultado, tiempo

    @staticmethod
    def calculador_tiempo(conexion , tiempo, tiempo_acarreado, diccionario_tiempos,objeto_base, modo):
        tiempo = modo.calcular_tiempo(conexion[1], conexion[2])                                     #calcula el tiempo con la distancia, y si ciudad[2] es la velocidad maxima si es que existe
        tiempo_neto = tiempo + tiempo_acarreado
        if conexion[0] not in diccionario_tiempos:
            diccionario_tiempos[conexion[0]] = (tiempo_neto,objeto_base)
        elif tiempo_neto < diccionario_tiempos[conexion[0]][0]:
            diccionario_tiempos[conexion[0]] = (tiempo_neto,objeto_base)
        tiempo_dic = tiempo_neto - tiempo_acarreado
        return tiempo_dic
    
    @staticmethod
    def mostrar_camino(resultado):
        print(f"El tiempo que tarda el recorrido es: {resultado[1]}")
        for valor in resultado[0]:
            print(f"La ciudad es: {valor.nombre}")



