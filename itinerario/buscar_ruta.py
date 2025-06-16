from itinerario.clasepila import Pila
from models.solicitud import Solicitud 
from utils.grafos import *
from models.vehiculos_herencia import *


class Buscar_ruta:
    tipos_vehiculo={"ferroviaria":Tren, "automotor":Camion, "aerea":Avion,"fluvial":Barcaza}
    def __init__(self,grafo,tipo_vehiculo):
        self.grafo=grafo #guarda la lista de objetos conexion
        self.vehiculo=self.tipos_vehiculo[tipo_vehiculo]()
    def buscar_caminos(self,solicitud): #Guarda desde solicitud el origen y destino
        #ACA TENDRIAMOS QUE TRABAJAR SOBRE EL OBJETO DE UNA CLASE 
        origen=solicitud.getorigen()
        destino=solicitud.getdestino()
        peso=solicitud.getpeso_kg( )

        caminos_encontrados=[] #aca se van a guardar las alternativas de camino
        pila=Pila()                    #Cada entrada en la pila es una tupla: la ciudad actual y el camino recorrido hasta ahora
        pila.apilar((origen,[origen])) #origen nos muestra donde estamos parados actualmente y [origen] es la lista con el camino recorrido

        while  not pila.esta_vacia():  #mientras que haya caminos posibles (la pila no este vacia) seguimos buscando
            nodo_actual,camino=pila.desapilar() #nos da la ciudad donde estemos parados y compara si ya es el destino

            if nodo_actual==destino:
                #calculat costo y tiempo
                tiempo_total=0
                costo_total=0
                for i in range(len(camino)-1):
                    ciudad1=camino[i]
                    ciudad2=camino[i+1]
                    for vecino, distancia, restriccion in self.grafo[ciudad1]:
                        distancia=float(distancia)
                        if restriccion is not None:
                            restriccion = float(restriccion)
                        if vecino==ciudad2:
                            print(f"Tipo de vehículo: {type(self.vehiculo)} | distancia: {distancia} | restriccion: {restriccion}")
                            tiempo_total+=self.vehiculo.calcular_tiempo(distancia,restriccion)
                            costo_total+=self.vehiculo.calcular_costo(distancia,peso)
                caminos_encontrados.append({"camino": camino,"tiempo_total":round(tiempo_total,2),"costo_total":round(costo_total,2),"vehiculo":self.vehiculo.__class__.__name__}) #Cuando encuentra un nodo igual al destino guarda el camino
                continue

            for vecino,distancia, otro_valor in self.grafo.get(nodo_actual,[]):
                if vecino not in camino:   #evita ciclos
                    nuevo_camino=camino+[vecino]
                    pila.apilar((vecino, nuevo_camino))

                #con este de abajo revisas el camino de manera inversa 

                #if ciudad_destino == nodo_actual and ciudad_origen not in camino:
                #    nuevo_camino = camino + [ciudad_origen]
                #    pila.apilar((ciudad_origen, nuevo_camino))

        return caminos_encontrados

    def mostrar_resultados(self,caminos_encontrados):
        print(f"{'Solución':<10} {'Modo':<12} {'Itinerario':<50} {'Costo total':>15} {'Tiempo total [min]':>20}")
        print("-" * 110)

        letra = ord('A')
        for camino in caminos_encontrados:
            if not camino:
                modo = camino["vehiculo"]
                print(f"{chr(letra):<10} {modo:<12} No disponible, no sale de ese origen")
            else:
                modo = camino["vehiculo"]
                itinerario = " - ".join(camino["camino"])
                costo = f"${camino['costo_total']:.3f}"
                tiempo = int(camino["tiempo_total"]*60)  # ver si hay que pasar a horas

                print(f"{chr(letra):<10} {modo:<12} {itinerario:<50} {costo:>15} {tiempo:>20}")
            letra += 1
#esto de aca es una prueba luego se borra

#grafo_info = {
#     "Zarate": [("Buenos Aires", 85, 100), ("Junin", 185, 80)],
#     "Buenos Aires": [("Zarate", 85, 100), ("Junin", 238, 90), ("Azul", 278, 110), ("Mar del Plata", 384, 120)],
#     "Junin": [("Zarate", 185, 80), ("Buenos Aires", 238, 90), ("Azul", 265, 100)],
#     "Azul": [("Junin", 265, 100), ("Buenos Aires", 278, 110), ("Mar del Plata", 246, 100)],
#     "Mar del Plata": [("Buenos Aires", 384, 120), ("Azul", 246, 100)]
 #}

#vehiculos={"Automotor", "Ferroviaria"}
 
#solicitud = Solicitud("CARGA_001",70000,"Zarate","Mar_del_Plata")

#buscador = Buscar_ruta(grafo_info,"ferroviaria")
#caminos = buscador.buscar_caminos(solicitud)

# Mostrar resultados
#buscador.mostrar_resultados(caminos)


