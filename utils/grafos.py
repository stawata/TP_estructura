 #from..utils.loaders import *
from models.conexiones import *

def armar_grafo(ciudades,conexiones):
    grafo = {}
    #aca voy a tener una lista con todas mis ciudades, que voy hacer que sean la key del grafo 
    
    for ciudad in ciudades:
        valores = list(filter(lambda x: x.destino ==ciudad or x.origen == ciudad, conexiones))
        value=[]
        for conexion in valores :
            if conexion.origen == ciudad:
                vecino=conexion.destino.nombre # esto crea el grafo para la conexion ferroviaria es para ferroviaria, y le pasa todos los parametros como atributos
            if conexion.destino== ciudad:
                    vecino=conexion.origen.nombre
            value.append((vecino, conexion))

        grafo[ciudad.nombre] = value
    return grafo


