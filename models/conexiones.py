from models.nodo import Nodo
from utils.validaciones import Validaciones

"""Esta clase se encarga de describir que 2 ciudades conecta y la distancia_km que hay entre ellas. Para eso se crean clases hijas que
van a heredar ciertas cualidades de la clase padre como la distancia_km, y la ciudad orgien y destino. La clase hija identifica el modo
de transporte que habilita.
"""

class Conexion():
    def __init__(self, origen, destino, distancia_km):
        if not Validaciones.validar_ciudad(origen) or not Validaciones.validar_ciudad(destino):
            raise ValueError("El origen y destino deben ser instancias de Nodo")
        if distancia_km <= 0:
            raise ValueError("La distancia debe ser un valor positivo")
        self.origen = origen
        self.destino = destino
        self.distancia_km = distancia_km

    def __str__(self):
        return f" {self.origen} a {self.destino} KM: {self.distancia_km} "

class Conexion_ferroviaria(Conexion):
    def __init__(self, origen,destino, distancia_km, restriccion):
        super().__init__(origen, destino, distancia_km)
        if restriccion:
            if restriccion <= 0:
                raise ValueError("La velocidad máxima debe ser un valor positivo")
            self.restriccion = restriccion
        else:
            self.restriccion = restriccion

    def __str__(self):
        return f" {self.origen} a {self.destino} KM: {self.distancia_km} "

class Conexion_autovia(Conexion):
    def __init__(self, origen,destino, distancia_km, restriccion):
        super().__init__(origen, destino, distancia_km)
        if restriccion:
            if restriccion <= 0:
                raise ValueError("El peso máximo debe ser un valor positivo")
            self.restriccion = restriccion
        else:
            self.restriccion = restriccion

    def __str__(self):
        return f" {self.origen} a {self.destino} KM: {self.distancia_km} "

class Conexion_maritima(Conexion):
    def __init__(self, origen,destino, distancia_km, restriccion):
        super().__init__(origen, destino, distancia_km)
        self.restriccion = restriccion

    def __str__(self):
        return f" {self.origen} a {self.destino} KM: {self.distancia_km} "

class Conexion_aerea(Conexion):
    def __init__(self, origen,destino, distancia_km, restriccion):
        super().__init__(origen, destino, distancia_km)
        if restriccion:
            if not (0 <= restriccion <= 1):
                raise ValueError("La probabilidad de mal clima debe estar entre 0 y 1")
            self.restriccion = restriccion 
        else:
            self.restriccion = restriccion

    def __str__(self):
        return f" {self.origen} a {self.destino} KM: {self.distancia_km} "

