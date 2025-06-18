import matplotlib.pyplot as plt
from models.conexiones import *
from models.vehiculos_herencia import Camion, Tren, Avion, Barcaza
from models.conexiones import Conexion_aerea, Conexion_autovia, Conexion_maritima, Conexion_ferroviaria


class Graficos:

    @staticmethod
    def datos_ruta(ruta, tipo, conexiones, peso):
        costos = []
        tiempos = []
        distancias = []

        '''voy a filtrar la conexion por tipo de automovil del camino mas eficiente'''
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
                costo = vehiculo.calcular_costo(conexion.distancia_km, peso, conexion.restriccion)

            elif tipo == "aereo":
                costo = vehiculo.calcular_costo(conexion.distancia_km, peso)
                tiempo = vehiculo.calcular_tiempo(conexion.distancia_km, conexion)

            elif tipo == "ferroviario":
                costo = vehiculo.calcular_costo(conexion.distancia_km, peso)
                tiempo = vehiculo.calcular_tiempo(conexion.distancia_km, conexion)
            else:
                costo = vehiculo.calcular_costo(conexion.distancia_km, peso)
                tiempo = vehiculo.calcular_tiempo(conexion.distancia_km)

            costos.append(costo)
            tiempos.append(tiempo)
            distancias.append(conexion.distancia_km)

        return costos, tiempos, distancias
        

    def Tiempo_acumulado (distancia, tiempo):

        ''' Datos de ejemplo
        distancia_acumulada = [0, 50, 100, 150, 200]
        tiempo_acumulado = [0, 1, 2.5, 4, 5.5]'''

        plt.plot(tiempo, distancia, marker='o')
        plt.title("Distancia Acumulada vs Tiempo Acumulado")
        plt.xlabel("Tiempo (horas)")
        plt.ylabel("Distancia (km)")

        ''' Esto va hacer que el grafico se guarde en un archivo aparte y no lo muestre de manera abrupta   '''  
        plt.savefig("distancia_vs_tiempo.png")  
        # Si no querés que lo muestre en pantalla, no pongas plt.show()


    def Costo_acumulado (distancia, costo):
        plt.plot(costo, distancia, marker='o')
        plt.title("Distancia Acumulada vs Costo Acumulado")
        plt.xlabel("Costo (Pesos)")
        plt.ylabel("Distancia (km)")
        plt.savefig("distancia_vs_costo.png")  


    def Costo_Tiempo (distancia, costo, tiempo):
        plt.title("Costo vs Tiempo")
        plt.ylabel("Tiempo (rojo) /Costo (verde)")
        plt.xlabel("Distancia (km)")

        plt.plot( distancia,tiempo, color = "green", linewidth= 3, label="porcentajke")
        plt.plot( distancia,costo, color = "red", linewidth= 3, label ="porcentajke")
        pass

#SON VALORES D EPRUEBA HAY QUE BORRARLOS"
'''plt.clf()
d=[10,90,130]
t = [23,33,67]
c = [300,350,900]
Graficos.Costo_Tiempo(d,c,t)
'''