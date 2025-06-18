 #from..utils.loaders import *
from models.conexiones import *

def armar_grafo(ciudades,conexiones):
    grafo = {}
    #aca voy a tener una lista con todas mis ciudades, que voy hacer que sean la key del grafo 
    
    for ciudad in ciudades:
        valores = list(filter(lambda x: x.destino ==ciudad or x.origen == ciudad, conexiones))
        value=[]
        for valor in valores :
                if valor.destino == ciudad:
                    value.append((valor.origen.nombre, valor.distancia_km, valor.restriccion)) # esto crea el grafo para la conexion ferroviaria es para ferroviaria, y le pasa todos los parametros como atributos
                if valor.origen == ciudad:
                    value.append((valor.destino.nombre, valor.distancia_km, valor.restriccion))

        grafo[ciudad.nombre] = value
    return grafo


