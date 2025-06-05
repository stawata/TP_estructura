from nodo import Nodo

"""Esta clase se encarga de describir que  2 ciudades conecta y la distancia que hay entre ellas. Para eso se crean clases hijas  que
 van a heredar ciertas cualidades de la clase padre como la distancia, y la ciudad orgien y destino. La clsae hija identifica el mode
de transporte que habulitea(Soporte de Modos: Un nodo puede aceptar o despachar un modo 
de transporte si al menos una conexión de dicho modo está enlazada al nodo. Si un modo de
transporte no se encuentra presente en el nodo a los fines de esa red se
considera inalcanzable.
3) """


class Conexion():
    def __init__(self, ciudad1:str, ciudad2:str, distancia :int, restriccion: str, valor_restriccion: str):
        Conexion.validar_int(distancia)
        Conexion.validar_ciudad(ciudad1)
        Conexion.validar_ciudad(ciudad2)
        self.ciudad1 = ciudad1
        self.ciudad2 = ciudad2
        self.distancia = distancia
        self.restriccion = restriccion
        self.valor_restriccion = valor_restriccion 

    def get_ciudad1(self):
        return self.ciudad1

    def get_ciudad2(self):
        return self.ciudad2    

    def __str__(self):
        return f" {self.ciudad1} a {self.ciudad2} KM: {self.distancia} "

    @staticmethod
    def validar_ciudad(valor): 
        if isinstance(valor,Nodo):  
            return True
        else:
            raise ValueError("El valor debe ser una ciudad que exista")
    @staticmethod
    def validar_int(valor):
        if isinstance(valor,int):
            return True
        else:
            raise ValueError("El valor debe int")
        
class Conexion_ferroviaria(Conexion):
    #la idea es poner conexion totales es guardar todas las conexiones para despues poder analizarlas
    #todas las herencias tendran sus propias conexiones
    conexiones_totales=[]
    def __init__(self, ciudad1,ciudad2, distancia, vel_maxima:float):
        super().__init__(ciudad1, ciudad2,distancia)
        self.vel_maxima = vel_maxima 
        Conexion_ferroviaria.conexiones_totales.append(self)

    def __str__(self):
        return f" {self.ciudad1} a {self.ciudad2} KM: {self.distancia} "


class Conexion_autovia(Conexion):
    conexiones_totales=[]
    def __init__(self, ciudad1,ciudad2, distancia, peso_max:float):
        super().__init__(ciudad1, ciudad2,distancia)
        self.peso_max = peso_max
        Conexion_autovia.conexiones_totales.append(self)


    def __str__(self):
        return f" {self.ciudad1} a {self.ciudad2} KM: {self.distancia} "


class Conexion_maritima(Conexion):
    conexiones_totales=[]

    def __init__(self, ciudad1,ciudad2, distancia, tipo_tasa:str):
        super().__init__(ciudad1, ciudad2,distancia)
        self.tipo_tasa = tipo_tasa
        Conexion_maritima.conexiones_totales.append(self)

    def __str__(self):
        return f" {self.ciudad1} a {self.ciudad2} KM: {self.distancia} "
    


class Conexion_aerea(Conexion):
    conexiones_totales=[]

    def __init__(self, ciudad1,ciudad2, distancia,probabilidad_mal_clima:float ):
        super().__init__(ciudad1, ciudad2,distancia)
        self.probabilidad_mal_clima = probabilidad_mal_clima
        Conexion_aerea.conexiones_totales.append(self)

    def __str__(self):
        return f" {self.ciudad1} a {self.ciudad2} KM: {self.distancia} "

