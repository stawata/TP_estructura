from pilas import Pila

class Buscar_ruta:
    def __init__(self,conexiones):
        self.conexiones=conexiones #guarda la lista de objetos conexion

    def buscar_caminos(self,solicitud): #Guarda desde solicitud el origen y destino
        origen=solicitud[2]
        destino=solicitud[3]

        caminos_encontrados=[] #aca se van a guardar las alternativas de camino
        pila=Pila()
        pila.apilar((origen,[origen])) #origen nos muestra donde estamos parados actualmente y [origen] es la lista con el camino recorrido

        while  not pila.esta_vacia():  #mientras que haya caminos posibles (la pila no este vacia) seguimos buscando
            nodo_actual,camino=pila.desapilar() #nos da la ciudad donde estemos parados y compara si ya es el destino

            if nodo_actual==destino:
                caminos_encontrados.append(camino) #Cuando encuentra un nodo igual al destino guarda el camino
                continue

            for conexion in self.conexiones:
                ciudad_origen=conexion[0]
                ciudad_destino=conexion[1]
                if ciudad_origen==nodo_actual and ciudad_destino not in camino: #agregamos otro tramo de camino por que todavia no se llego al destino
                    nuevo_camino=camino+[ciudad_destino]
                    pila.apilar((ciudad_destino, nuevo_camino))
            
        return caminos_encontrados
    
#ruta = [
#    ["Zarate", "Buenos_Aires", "Automotor", 85,  ""],
#    ["Zarate", "Junin", "Automotor", 185, "peso_max", 15000],
#    ["Junin", "Buenos_Aires", "Automotor", 238,  ""],
#    ["Junin", "Azul", "Automotor", 265,  ""],
#    ["Azul", "Buenos_Aires", "Automotor", 278,  ""],
#    ["Azul", "Mar_del_Plata", "Automotor", 246,  ""],
#    ["Buenos_Aires", "Mar_del_Plata", "Automotor", 384,  ""]
#]

#solicitud = ["CARGA_001",70000,"Zarate","Mar_del_Plata"]

#buscador = Buscar_ruta(ruta)
#caminos = buscador.buscar_caminos(solicitud)

# Mostrar resultados
#for i, camino in enumerate(caminos):
#    print(f"Camino {i+1}: {' → '.join(camino)}")



