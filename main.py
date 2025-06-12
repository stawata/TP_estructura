from utils.loader import NodoLoader, ConexionLoader, SolicitudLoader
from algoritmo_disjtra.pilas_2 import Pila
from algoritmo_disjtra.Nodo_pais import NodoPais
from models.solicitud import Solicitud 
from models.vehiculos_herencia import *
from utils.validaciones import Validaciones
from models.conexiones import *
from utils.grafos import * 
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
    
    #ESTO SE BORRA SE USA UNA FUNCION 
    def armar_grafo(self, ruta): #Armar un metodo para pasar de lista de listas a diccionario
        #De la linea 32 a la 38 es igual que de la 40 a la 46
        grafo = {}
        indices = [0, 2, 3, 4, 5] 
        for lista in ruta:
            if lista[0] not in grafo: 
                grafo[lista[0]] =  [lista[1:]]
                self.agregar_conexion(grafo, lista[0], lista[1], [lista[i] for i in indices if i < len(lista)])
            else:
                grafo[lista[0]].append(lista[1:])
                self.agregar_conexion(grafo, lista[0], lista[1], [lista[i] for i in indices if i < len(lista)])

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
                        if recorrido.recorrer_pila(ciudad[0]): # se fija si la ciudad ya esta en la pila
                            print("Ya es parte del recorrido esa ciudad")
                            continue
                        elif ciudad[3] == "peso_max":   # esta restriccion es propia de automotor debemos cambiar dependiendo el vehiculo
                            if ciudad[-1] < solicitud.peso_kg:   
                                print("la carga excede el peso admitido por la conexion")
                                continue
                            else:  #Hasta la 76 es lo mismo que de la 78 a la 83
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
                        recorrido.apilar(NodoPais(clave, valor[0], valor[1])) 
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
    def filtrar_por_modo(rutas, modo):
        if type(modo)== Camion:
            buscador = "Automotor"
            return list(filter(lambda x: x[2] == buscador, rutas))


    @staticmethod
    def mostrar_camino(resultado):
        print(f"El tiempo que tarda el recorrido es: {resultado[1]}")
        for valor in resultado[0]:
            print(f"La ciudad es: {valor.nombre}")

    @staticmethod
    def agregar_conexion(grafo, origen, destino, datos):
        if destino not in grafo:
            inverso = datos[1:]
            inverso.insert(0, origen)
            grafo[destino] = [inverso]
        else:
            grafo[destino].append(datos)

def main():
    try:
        # Ciudades = NodoLoader.cargar_desde_csv("data/nodos.csv")
        # Conexiones = ConexionLoader.cargar_desde_csv("data/conexiones.csv", Ciudades)
        # Solicitudes = SolicitudLoader.cargar_desde_csv("data/solicitudes.csv", Ciudades)
             
        ruta = [
        ["Zarate", "Buenos_Aires", "Automotor", 85,  ""],
        ["Zarate", "Junin", "Automotor", 185, "peso_max", 15000],
        ["Junin", "Buenos_Aires", "Automotor", 238,  ""],
        ["Junin", "Azul", "Automotor", 265,  ""],
        ["Azul", "Buenos_Aires", "Automotor", 278,  ""],
        ["Azul", "Mar_del_Plata", "Automotor", 246,  ""],
        ["Buenos_Aires", "Mar_del_Plata", "Automotor", 384,  ""]
    ]

        solicitud_1 = Solicitud("CARGA_001",70000,NodoPais("Zarate",0, None),NodoPais("Mar_del_Plata",0, None))
        camion_1 = Camion()
        recorrido = Grafo(ruta, solicitud_1, camion_1)




    except FileNotFoundError as e:
        print(f"Error al cargar los archivos: {e}")

    print("Ciudades cargadas:")
    # for ciudad in Ciudades:
    #     print(ciudad)
    # print("\nConexiones cargadas:")
    # for conexion in Conexiones:
    #     print(conexion)
    # print("\nSolicitudes cargadas:")
    # for solicitud in Solicitudes:
    #     print(solicitud)

#ACA TENGO EN UNA LISTA LOS VALORES QUE LEI 
nodos = NodoLoader.cargar_desde_csv("data/nodos.csv")
conexiones= ConexionLoader.cargar_desde_csv("data/conexiones.csv", nodos)

#ACA VOY HACER LAS CONEXIONES DETODOS LOS VEHICLOS 
conexiones_ferroviarias_totales = list(filter(lambda x : isinstance(x,Conexion_ferroviaria), conexiones))


#ACA VOY A TENER LOS GRAFOS DE CADA VEHICULO
grafo_tren= armar_grafo(nodos, conexiones_ferroviarias_totales)

#ESTO ES PATRA VISUALIZAR DESPUES SE PUEDE BORRAR
for key, values in grafo_tren.items():
    print(f"Llave: {key}")
    for i in values: 
        print("valores:",i[0], i[1], i[2])