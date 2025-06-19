import matplotlib.pyplot as plt
from models.conexiones import *
from models.vehiculos_herencia import Camion, Tren, Avion, Barcaza
from models.conexiones import Conexion_aerea, Conexion_autovia, Conexion_maritima, Conexion_ferroviaria
import numpy as np


class Graficos:

    @staticmethod
    def datos_ruta(ruta, tipo, conexiones, peso):
        costos = [0,]
        tiempos = [0,]
        distancias = [0,]

        '''
        voy a filtrar la conexion por tipo de automovil del camino mas eficiente
        '''
        if tipo == "automotor":
            conexiones_filtradas = list(filter(lambda x: isinstance (x, Conexion_autovia), conexiones))
            vehiculo = Camion

        elif tipo == "aereo":
            conexiones_filtradas = list(filter(lambda x: isinstance (x, Conexion_aerea), conexiones))
            vehiculo = Avion

        elif tipo == "ferroviario":
            conexiones_filtradas = list(filter(lambda x: isinstance (x, Conexion_ferroviaria), conexiones))
            vehiculo = Tren

        elif tipo == "maritimo":
            conexiones_filtradas = list(filter(lambda x: isinstance (x, Conexion_maritima), conexiones))
            vehiculo = Barcaza

        else:
            raise ValueError("Tipo de transporte inválido.")

        '''Vamos a recorrer cada ciudad de la ruta y buscar las distancia, costo y tiempo con la ciudad siguiente'''

        for i in range(len(ruta) - 1):
            origen = ruta[i]
            destino = ruta[i + 1]

            '''Aca busco la conexion que cumpla con ambas ciudades'''
            conexion = None
            for c in conexiones_filtradas:
                if (c.origen.nombre == origen and c.destino.nombre == destino) or (c.destino.nombre == origen and c.origen.nombre == destino):
                    conexion = c
                    break


            '''voy a calcular los costos y tiempos ya que la distancia es un valor que ya tengo dado'''
            '''Voy a utilizar los metodos calcular_costo y calcular_tiempo ya que los mismos contemplan las restricciones'''

            if tipo == "maritimo":
                costo = Barcaza.calcular_costo(conexion.distancia_km, peso, conexion.restriccion)

            if tipo == "aereo":
                costo = Avion.calcular_costo(conexion.distancia_km, peso)
                tiempo = Avion.calcular_tiempo(conexion.distancia_km, conexion)

            if tipo == "ferroviario":
                costo = Tren.calcular_costo(conexion.distancia_km, peso)
                tiempo = Tren.calcular_tiempo(conexion.distancia_km, conexion)

            if tipo == "automotor":
                costo = Camion.calcular_costo(conexion.distancia_km, peso)
                tiempo = Camion.calcular_tiempo(conexion.distancia_km)

            costos.append(costo)
            tiempos.append(tiempo)
            distancias.append(conexion.distancia_km)
        '''Para que el primer valor de la lista sea 0 lo agrego manualmente y uso la libreria numpy para que los valores que se encontraron 
            a lo largo del recorrido se vayan sumando y efectamente tener el valor acumulado de todo el trayecto'''
        costos_acumulados = [0] + list(np.cumsum(costos[1:]))
        tiempos_acumulados = [0] + list(np.cumsum(tiempos[1:]))
        distancias_acumuladas = [0] + list(np.cumsum(distancias[1:]))

        return costos_acumulados, tiempos_acumulados, distancias_acumuladas
        

    def Tiempo_acumulado (distancia, tiempo_barata,tiempo_rapida):

        plt.plot(tiempo_barata, distancia, marker='o')
        plt.title(f"Evolucion Tiempo opcion mas barata")
        plt.xlabel("Costo (Pesos)")
        plt.ylabel("Distancia (km)")
        plt.savefig("Evolucion_Tiempo_opcion_mas_barata.png")  

        plt.clf()

        plt.plot(tiempo_rapida, distancia, marker='o')
        plt.title(f"Evolucion Costo opcion mas rapida")
        plt.xlabel("Costo (Pesos)")
        plt.ylabel("Distancia (km)")
        plt.savefig("Evolucion_Tiempo_opcion_mas_rapida.png")  
        


    def Costo_acumulado (distancia, costo_rapida,costo_barata):
        plt.plot(costo_barata, distancia, marker='o')
        plt.title(f"Evolucion Costo opcion mas barata")
        plt.xlabel("Costo (Pesos)")
        plt.ylabel("Distancia (km)")
        plt.savefig("Evolucion_Costo_opcion_mas_barata.png")  

        plt.clf()

        plt.plot(costo_rapida, distancia, marker='o')
        plt.title(f"Evolucion Costo opcion mas rapida")
        plt.xlabel("Costo (Pesos)")
        plt.ylabel("Distancia (km)")
        plt.savefig("Evolucion_Costo_opcion_mas_rapida.png")  

    def Costo_acumulado_comparado(distancia_rapido, costo_rapido, distancia_barato, costo_barato, nombre_archivo):
        plt.figure()
        '''
        le asignas los ejes y el color
        '''
        plt.plot( distancia_rapido,costo_rapido, marker='o', linestyle='-', color='blue', label='Rápido')
        plt.plot(distancia_barato, costo_barato, marker='o', linestyle='-', color='green', label='Barato')

        
        plt.title("Comparación de Costos Acumulados")
        plt.xlabel("Distancia (km)")
        plt.ylabel("Costo (Pesos)")
        plt.legend()
        plt.savefig(f"costo_acumulado_comparado_{nombre_archivo}.png")
        '''Esto va hacer que se borre el grafico y que no se pisen en caso de tener muchas solicitudes'''

        plt.clf()

    def Tiempo_acumulado_comparado(distancia_rapido, tiempo_rapido, distancia_barato, tiempo_barato, nombre_archivo):
        plt.figure()
        plt.plot( tiempo_rapido,distancia_rapido, marker='o', linestyle='-', color='blue', label='Rápido')
        plt.plot( tiempo_barato,distancia_barato, marker='o', linestyle='-', color='green', label='Barato')

        plt.title("Comparación de Tiempos Acumulados")
        plt.ylabel("Distancia (km)")
        plt.xlabel("Tiempo (horas)")
        plt.legend()
        plt.savefig(f"tiempo_acumulado_comparado_{nombre_archivo}.png")
        plt.clf()


