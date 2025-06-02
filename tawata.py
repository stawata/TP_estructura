class Conexion():
    def __init__(self, nombre:str, distancia :int):
        Conexion.validar_int(distancia)
        Conexion.validar_str(nombre)
        self.nombre = nombre
        self.distancia = distancia

    def __str__(self):
        return f"Esta es la ruta{self.nombre} de distancia {self.distancia} km"

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
    def __init__(self, nombre, distancia):
        super().__init__(nombre, distancia)
    
    def __str__(self):
        return f"Esta es la ruta ferroviaria{self.nombre} de distancia {self.distancia} km"


class Conexion_autovia(Conexion):
    def __init__(self, nombre, distancia):
        super().__init__(nombre, distancia)

    def __str__(self):
        return f"Esta es la ruta de autovía {self.nombre} de distancia {self.distancia} km"


class Conexion_maritima(Conexion):
    def __init__(self, nombre, distancia):
        super().__init__(nombre, distancia)

    def __str__(self):
        return f"Esta es la ruta marítima {self.nombre} de distancia {self.distancia} km"


class Conexion_aerea(Conexion):
    def __init__(self, nombre, distancia):
        super().__init__(nombre, distancia)

    def __str__(self):
        return f"Esta es la ruta aérea {self.nombre} de distancia {self.distancia} km"

ruta_12 = Conexion_aerea("las vegas", 54)

print(ruta_12)