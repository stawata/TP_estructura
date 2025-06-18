import matplotlib.pyplot as plt
from models.conexiones import *

class Graficos:

    def datos_ruta (ruta, tipo , conexiones):
        costos=[]
        tiempos=[]
        distancias=[]

        if tipo == "automotor":
            conexion_filtrada= list(filter(lambda x: isinstance(x,Conexion_autovia ), conexiones ))
        if tipo == "aereo":
            conexion_filtrada= list(filter(lambda x: isinstance(x,Conexion_aerea ), conexiones ))
        if tipo == "ferroviario":
            conexion_filtrada= list(filter(lambda x: isinstance(x,Conexion_ferroviaria ), conexiones ))
        if tipo == "automotor":
            conexion_filtrada= list(filter(lambda x: isinstance(x,Conexion_maritima ), conexiones ))

        print(conexion_filtrada)

        '''for i in range(len(ruta)-1):
            origen= ruta[i]
            destino = ruta[i+1]

        punto_origen= puntos_red[origen]

        for vecino in punto_origen.vecinos:
            if vecino.nombre == destino:
                datos = punto_origen.vecinos[vecino]
                if len(datos)>=3:
                    costo, tiempo , distancia = datos 
                    costos.append(costo)
                    tiempos.append(tiempo)
                    distancias.append(distancia)'''

        #return costos, tiempos, distancias


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


    def Costo_acumulado (distancia, costo, tiempo):
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