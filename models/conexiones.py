from models.nodo import Nodo
from validaciones.validaciones import validaciones

"""Esta clase se encarga de describir que  2 ciudades conecta y la distancia que hay entre ellas. Para eso se crean clases hijas  que
 van a heredar ciertas cualidades de la clase padre como la distancia, y la ciudad orgien y destino. La clsae hija identifica el mode
de transporte que habulitea(Soporte de Modos: Un nodo puede aceptar o despachar un modo 
de transporte si al menos una conexión de dicho modo está enlazada al nodo. Si un modo de
transporte no se encuentra presente en el nodo a los fines de esa red se
considera inalcanzable.
3) """


class Conexion():
    def __init__(self, ciudad1:str, ciudad2:str, distancia :float):
        validaciones.validar_float(distancia)
        Conexion.validar_ciudad(ciudad1)
        Conexion.validar_ciudad(ciudad2)
        self.ciudad1 = ciudad1
        self.ciudad2 = ciudad2
        self.distancia = distancia

    def __str__(self):
        return f" {self.ciudad1} a {self.ciudad2} KM: {self.distancia} "

    @staticmethod
    def validar_ciudad(valor): 
        if isinstance(valor,Nodo):  
            return True
        else:
            raise ValueError("El valor debe ser una ciudad que exista")

        
class Conexion_ferroviaria(Conexion):
    def __init__(self, ciudad1,ciudad2, distancia):
        super().__init__(ciudad1, ciudad2,distancia)
    
    def __str__(self):
        return f" {self.ciudad1} a {self.ciudad2} KM: {self.distancia} "


class Conexion_autovia(Conexion):
    def __init__(self, ciudad1,ciudad2, distancia):
        super().__init__(ciudad1, ciudad2,distancia)

    def __str__(self):
        return f" {self.ciudad1} a {self.ciudad2} KM: {self.distancia} "


class Conexion_maritima(Conexion):
    def __init__(self, ciudad1,ciudad2, distancia):
        super().__init__(ciudad1, ciudad2,distancia)

    def __str__(self):
        return f" {self.ciudad1} a {self.ciudad2} KM: {self.distancia} "


class Conexion_aerea(Conexion):
    def __init__(self, ciudad1,ciudad2, distancia):
        super().__init__(ciudad1, ciudad2,distancia)

    def __str__(self):
        return f" {self.ciudad1} a {self.ciudad2} KM: {self.distancia} "

