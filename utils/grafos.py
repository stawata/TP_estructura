#from..utils.loaders import *
from models.conexiones import Conexion

def armar_grafo(ciudades,conexiones):
        grafo = {}
        #aca voy a tener una lista con todas mis ciudades, que voy hacer que sean la key del grafo 
        
        for ciudad in ciudades:
            valores = list(filter(lambda x: x.destino ==ciudad or x.origen == ciudad, conexiones))
            grafo[ciudad] = valores
        return grafo


#PRIMERO VOY A BUSCAR DE TODAS LAS CONEXIONES SE UN TIPO DE VEHICULO 
#POR CADA CIUDAD VOY HACER UN DICCIONARIO 




