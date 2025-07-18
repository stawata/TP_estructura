from itinerario.clasepila import Pila
from models.solicitud import Solicitud 
from utils.grafos import *
from models.vehiculos_herencia import *
import models.nodo as Nodo


class Buscar_ruta:
    tipos_vehiculo={"ferroviaria":Tren, "automotor":Camion, "aerea":Avion, "maritimo":Barcaza} #Diccionario que relaciona el tipo de vehiculo con la clase correspondiente
    def __init__(self,grafo,tipo_vehiculo,dicc_nodos):
        self.grafo=grafo #guarda la lista de objetos conexion
        self.vehiculo=tipo_vehiculo
        self.dicc_nodos=dicc_nodos

    def buscar_caminos(self,solicitud): #Guarda desde solicitud el origen y destino
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
                    for vecino, conexion in self.grafo[ciudad1]:
                        if vecino != ciudad2:
                            continue  # Evita seguir si no es el tramo correcto

                        if self.vehiculo == Barcaza:
                            tiempo_tramo = self.vehiculo.calcular_tiempo(conexion.distancia_km)
                            costo_tramo = self.vehiculo.calcular_costo(conexion.distancia_km, peso, conexion.restriccion)
                        else:
                            tiempo_tramo = self.vehiculo.calcular_tiempo(conexion.distancia_km, conexion.restriccion)
                            costo_tramo = self.vehiculo.calcular_costo(conexion.distancia_km, peso)

                        #Aplica peaje solo al tramo correcto
                        nodo_destino = self.dicc_nodos.get(ciudad2)
                        porcentaje_peaje = nodo_destino.get_porcentaje_peaje()
                        costo_tramo *= (1 + porcentaje_peaje)

                        tiempo_total += tiempo_tramo
                        costo_total += costo_tramo



                caminos_encontrados.append({"camino": camino,"tiempo_total":round(tiempo_total,2),"costo_total":round(costo_total,2),"vehiculo":self.vehiculo}) #Cuando encuentra un nodo igual al destino guarda el camino
                continue

            for vecino,conexion in self.grafo.get(nodo_actual,[]):
                if vecino not in camino:   #evita ciclos
                    #validamos si el nodo acepta el peso
                    nodo_obj=self.dicc_nodos.get(vecino)
                    if nodo_obj and peso<=nodo_obj.peso_maximo:
                        nuevo_camino=camino+[vecino]
                        pila.apilar((vecino, nuevo_camino))
        if not caminos_encontrados:
            caminos_encontrados.append({"camino": [], "tiempo_total": 0, "costo_total": 0, "vehiculo": self.vehiculo}) #Si no hay caminos posibles, devuelve una lista vacia
        return caminos_encontrados

    @classmethod
    def mostrar_resultados(self,caminos_encontrados):
        print(f"{'Solución':<10} {'Modo':<12} {'Itinerario':<50} {'Costo total':>15} {'Tiempo total [horas]':>20}")
        print("-" * 110)

        letra = ord('A')

        for camino in caminos_encontrados:
            if camino["camino"]==[]:
                # Si el camino está vacío, significa que no hay ruta disponible
                modo = camino["vehiculo"].__name__
                print(f"{chr(letra):<10} {modo:<12} No disponible, no sale de ese origen")
                letra += 1
            else:
                modo = camino["vehiculo"].__name__
                itinerario = " - ".join(camino["camino"])
                costo = f"${camino['costo_total']:.3f}"
                tiempo = round(camino["tiempo_total"], 2)

                print(f"{chr(letra):<10} {modo:<12} {itinerario:<50} {costo:>15} {tiempo:>20}")
                letra += 1
            


