<<<<<<< HEAD
#from..utils.loaders import *
from models.conexiones import Conexion
=======
<<<<<<< HEAD
>>>>>>> b2e10e6 (conexiones atributos de clase)

def armar_grafo(ciudades,conexiones):
        grafo = {}
        #aca voy a tener una lista con todas mis ciudades, que voy hacer que sean la key del grafo 
        
<<<<<<< HEAD
        for ciudad in ciudades:
            valores = list(filter(lambda x: x.destino ==ciudad or x.origen == ciudad, conexiones))
            value=[]
            for valor in valores :
                if valor.destino == ciudad:
                    value.append([valor.origen, valor.distancia_km, valor.velocidad_max])
                if valor.origen == ciudad:
                    value.append([valor.destino, valor.distancia_km, valor.velocidad_max])

            grafo[ciudad] = value
=======
=======
from models.conexiones import Conexion_ferroviaria

    def armar_grafo(self, ruta):
        grafo = {}
>>>>>>> ff03e0d (conexiones atributos de clase)
        indices = [0, 2, 3, 4, 5] 
        for lista in ruta:
            if lista[0] not in grafo: 
                grafo[lista[0]] =  [lista[1:]]
                if lista[1] not in grafo:
                    inverso = lista[2:]
                    inverso.insert(0, lista[0])  
                    grafo[lista[1]] = [inverso]  
                else:
                    grafo[lista[1]].append([lista[i] for i in indices if i < len(lista)])
            else:
                grafo[lista[0]].append(lista[1:])
                if lista[1] not in grafo:
                    inverso = lista[2:]
                    inverso.insert(0, lista[0])  
                    grafo[lista[1]] = [inverso]   
                else:
                    grafo[lista[1]].append([lista[i] for i in indices if i < len(lista)])
>>>>>>> b2e10e6 (conexiones atributos de clase)
        return grafo

<<<<<<< HEAD

#PRIMERO VOY A BUSCAR DE TODAS LAS CONEXIONES SE UN TIPO DE VEHICULO 
#POR CADA CIUDAD VOY HACER UN DICCIONARIO 

<<<<<<< HEAD



=======
grafo_tren= armar_grafo(conexiones_ferroviarias_totales)
=======
#la idea es que por cada tipo de conexion haga un grafo 

grafo_trenes = armar_grafo(conexiones_totales_ferroviarias)

>>>>>>> ff03e0d (conexiones atributos de clase)
>>>>>>> b2e10e6 (conexiones atributos de clase)
