class Conexion():
    def __init__(self, ciudad1:str,ciudad2:str, distancia :int):
        Conexion.validar_int(distancia)
        Conexion.validar_str(ciudad1)
        Conexion.validar_str(ciudad2)
        self.ciudad1 = ciudad1
        self.ciudad2=ciudad2
        self.distancia = distancia

    def __str__(self):
        return f" {self.ciudad1} a {self.ciudad2} KM: {self.distancia} "

    @staticmethod
    def validar_str(valor):
        if isinstance(valor,str):
            return True
        else:
            raise ValueError("El valor debe ser str")
    @staticmethod
    def validar_int(valor):
        if isinstance(valor,int):
            return True
        else:
            raise ValueError("El valor debe int")
        
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

