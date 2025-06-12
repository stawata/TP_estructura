
import  Conexion_ferroviaria

def armar_grafo(self, conexiones):
        grafo = {}
        
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
        return grafo


#PRIMERO VOY A BUSCAR DE TODAS LAS CONEXIONES SE UN TIPO DE VEHICULO 
#POR CADA CIUDAD VOY HACER UN DICCIONARIO 

grafo_tren= armar_grafo(conexiones_ferroviarias_totales)
