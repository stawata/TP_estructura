from nodo import Nodo
from validaciones import validaciones

"""Esta clase se encarga de describir que  2 ciudades conecta y la distancia que hay entre ellas. Para eso se crean clases hijas  que
 van a heredar ciertas cualidades de la clase padre como la distancia, y la ciudad orgien y destino. La clsae hija identifica el mode
de transporte que habulitea(Soporte de Modos: Un nodo puede aceptar o despachar un modo 
de transporte si al menos una conexión de dicho modo está enlazada al nodo. Si un modo de
transporte no se encuentra presente en el nodo a los fines de esa red se
considera inalcanzable.
3) """


class Conexion():
    tipo_conexion=set()
    def __init__(self, ciudad1:str, ciudad2:str,tipo:str ,distancia :float):
        validaciones.validar_float(distancia)
        Conexion.validar_ciudad(ciudad1)
        Conexion.validar_ciudad(ciudad2)
        self.ciudad1 = ciudad1
        self.ciudad2 = ciudad2
        self.distancia = distancia
        self.tipo = tipo
        #la idea es tener un conjunto con todos los tipo de conexion (fluvial, terrestre, aereo,etc)
        Conexion.tipos_conexion.append(self.tipo)

    def __str__(self):
        return f" {self.ciudad1} a {self.ciudad2} KM: {self.distancia} "

    @staticmethod
    def validar_ciudad(valor): 
        if isinstance(valor,Nodo):  
            return True
        else:
            raise ValueError("El valor debe ser una ciudad que exista")

        
class Conexion_ferroviaria(Conexion):
    def __init__(self, ciudad1,ciudad2, tipo ,distancia, velocidad_max : float):
        validaciones.validar_float(velocidad_max)
        super().__init__(ciudad1, ciudad2,tipo,distancia)
        self.velocidad_max = velocidad_max
    def __str__(self):
        return f" {self.ciudad1} a {self.ciudad2} KM: {self.distancia} "


class Conexion_autovia(Conexion):
    def __init__(self, ciudad1,ciudad2, tipo,distancia, peso_max:float):
        validaciones.validar_float(peso_max)
        super().__init__(ciudad1, ciudad2,tipo,distancia)
        self.peso_max = peso_max
    def __str__(self):
        return f" {self.ciudad1} a {self.ciudad2} KM: {self.distancia} "


class Conexion_maritima(Conexion):
    def __init__(self, ciudad1,ciudad2, tipo,distancia, tipo_tasa : str):
        validaciones.validar_str(tipo_tasa)
        super().__init__(ciudad1, ciudad2,tipo,distancia)
        self.tipo_tasa = tipo_tasa
    def __str__(self):
        return f" {self.ciudad1} a {self.ciudad2} KM: {self.distancia} "


class Conexion_aerea(Conexion):
    def __init__(self, ciudad1,ciudad2,tipo, distancia, probabilidad_mal_clima:float):
        validaciones.validar_str(probabilidad_mal_clima)
        super().__init__(ciudad1, ciudad2,tipo,distancia)
        self.probabilidad_mal_clima = probabilidad_mal_clima 

    def __str__(self):
        return f" {self.ciudad1} a {self.ciudad2} KM: {self.distancia} "

con = Conexion_aerea(None, None, 100, 0,1)