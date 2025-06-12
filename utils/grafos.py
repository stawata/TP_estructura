
#from..utils.loaders import *
from models.conexiones import Conexion


def armar_grafo(ciudades,conexiones):
        grafo = {}
        #aca voy a tener una lista con todas mis ciudades, que voy hacer que sean la key del grafo 
        

        for ciudad in ciudades:
            valores = list(filter(lambda x: x.destino ==ciudad or x.origen == ciudad, conexiones))
            value=[]
            for valor in valores :
                if valor.destino == ciudad:
                    value.append([valor.origen, valor.distancia_km, valor.velocidad_max])
                if valor.origen == ciudad:
                    value.append([valor.destino, valor.distancia_km, valor.velocidad_max])

            grafo[ciudad] = value

