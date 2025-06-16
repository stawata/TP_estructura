from clasepila import Pila
from models.solicitud import Solicitud 
from utils.grafos import *
from models.vehiculos_herencia import *

tipos_vehiculo={"ferroviaria":Tren, "automotor":Camion, "aerea":Avion,"fluvial":Barcaza}
class Buscar_ruta:
    def __init__(self,grafo,tipo_vehiculo):
        self.grafo=grafo #guarda la lista de objetos conexion
        self.vehiculo=tipos_vehiculo[tipo_vehiculo]
    def buscar_caminos(self,solicitud): #Guarda desde solicitud el origen y destino
        #ACA TENDRIAMOS QUE TRABAJAR SOBRE EL OBJETO DE UNA CLASE 
        origen=solicitud.getorigen()
        destino=solicitud.getdestino()

        caminos_encontrados=[] #aca se van a guardar las alternativas de camino
        pila=Pila()                    #Cada entrada en la pila es una tupla: la ciudad actual y el camino recorrido hasta ahora
        pila.apilar((origen,[origen])) #origen nos muestra donde estamos parados actualmente y [origen] es la lista con el camino recorrido

        while  not pila.esta_vacia():  #mientras que haya caminos posibles (la pila no este vacia) seguimos buscando
            nodo_actual,camino=pila.desapilar() #nos da la ciudad donde estemos parados y compara si ya es el destino

            if nodo_actual==destino:
                caminos_encontrados.append(camino) #Cuando encuentra un nodo igual al destino guarda el camino
                continue

            for vecino,distancia, otro_valor in self.grafo.get(nodo_actual,[]):
                if vecino not in camino:   #evita ciclos
                    nuevo_camino=camino+[vecino]
                    pila.apilar((vecino, nuevo_camino))

                #con este de abajo revisas el camino de manera inversa 

                #if ciudad_destino == nodo_actual and ciudad_origen not in camino:
                #    nuevo_camino = camino + [ciudad_origen]
                #    pila.apilar((ciudad_origen, nuevo_camino))
            #calcular tiempos y costos
            resultados=[]
            for camino in caminos_encontrados:
                tiempo_total=0
                costo_total=0
                for i in range(len(camino)-1):
                    ciudad1=camino[i]
                    ciudad2=camino[i+1]
                    for vecino, distancia, velocidad in self.grafo[ciudad1]:
                        if vecino==ciudad2:
                            tiempo_total+=self.vehiculo.calcular_tiempo(distancia,vecino)

        return caminos_encontrados

#esto de aca es una prueba luego se borra

grafo_info = {
     "Zarate": [("Buenos Aires", 85, 100), ("Junin", 185, 80)],
     "Buenos Aires": [("Zarate", 85, 100), ("Junin", 238, 90), ("Azul", 278, 110), ("Mar del Plata", 384, 120)],
     "Junin": [("Zarate", 185, 80), ("Buenos Aires", 238, 90), ("Azul", 265, 100)],
     "Azul": [("Junin", 265, 100), ("Buenos Aires", 278, 110), ("Mar del Plata", 246, 100)],
     "Mar del Plata": [("Buenos Aires", 384, 120), ("Azul", 246, 100)]
 }

vehiculos={"Automotor", "Ferroviaria"}

solicitud = Solicitud("CARGA_001",70000,"Zarate","Mar_del_Plata")

buscador = Buscar_ruta(grafo_info)
caminos = buscador.buscar_caminos(solicitud)

# Mostrar resultados
for i, camino in enumerate(caminos):
    print(f"Camino {i+1}: {' → '.join(camino)}")


