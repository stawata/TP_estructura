from models.nodo import Nodo
from utils.validaciones import *

"""Esta clase se encarga de describir que  2 ciudades conecta y la distancia_km que hay entre ellas. Para eso se crean clases hijas  que
 van a heredar ciertas cualidades de la clase padre como la distancia_km, y la ciudad orgien y destino. La clsae hija identifica el mode
de transporte que habulitea(Soporte de Modos: Un nodo puede aceptar o despachar un modo 
de transporte si al menos una conexión de dicho modo está enlazada al nodo. Si un modo de
transporte no se encuentra presente en el nodo a los fines de esa red se
considera inalcanzable.
3) """

class Conexion():
    def __init__(self, origen:str, destino:str, distancia_km :float):
        validaciones.validar_float(distancia_km)
        self.origen = origen
        self.destino = destino
        self.distancia_km = distancia_km

    def __str__(self):
        return f" {self.origen} a {self.destino} KM: {self.distancia_km} "

    @staticmethod
    def validar_ciudad(valor): 
        if isinstance(valor,Nodo):  
            return True
        else:
            raise ValueError("El valor debe ser una ciudad que exista")

        
class Conexion_ferroviaria(Conexion):
    def __init__(self, origen,destino, distancia_km, velocidad_max : float):
        super().__init__(origen, destino,distancia_km)
        self.velocidad_max = velocidad_max
    def __str__(self):
        return f" {self.origen} a {self.destino} KM: {self.distancia_km} "


class Conexion_autovia(Conexion):
    def __init__(self, origen,destino, distancia_km, peso_max:float):
        super().__init__(origen, destino,distancia_km)
        self.peso_max = peso_max
    def __str__(self):
        return f" {self.origen} a {self.destino} KM: {self.distancia_km} "


class Conexion_maritima(Conexion):
    def __init__(self, origen,destino, distancia_km, tipo_tasa : str):
        super().__init__(origen, destino,distancia_km)
        self.tipo_tasa = tipo_tasa
    def __str__(self):
        return f" {self.origen} a {self.destino} KM: {self.distancia_km} "


class Conexion_aerea(Conexion):
    def __init__(self, origen,destino, distancia_km, probabilidad_mal_clima:float):
        super().__init__(origen, destino,distancia_km)
        self.probabilidad_mal_clima = probabilidad_mal_clima 

    def __str__(self):
        return f" {self.origen} a {self.destino} KM: {self.distancia_km} "
