from models.nodo import Nodo
from utils.validaciones import Validaciones

"""Esta clase se encarga de describir que  2 ciudades conecta y la distancia_km que hay entre ellas. Para eso se crean clases hijas  que
 van a heredar ciertas cualidades de la clase padre como la distancia_km, y la ciudad orgien y destino. La clsae hija identifica el mode
de transporte que habulitea(Soporte de Modos: Un nodo puede aceptar o despachar un modo 
de transporte si al menos una conexión de dicho modo está enlazada al nodo. Si un modo de
transporte no se encuentra presente en el nodo a los fines de esa red se
considera inalcanzable.
3) """

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
    
    def es_valida(self, vehiculo, peso_carga):
        if self.tipo != vehiculo.modo:
            return False

        if self.tipo == "automotor" and self.peso_maximo_kg is not None:
            return peso_carga <= self.peso_maximo_kg

        return True  # Para ferroviario, aéreo y marítimo (restricciones específicas ya consideradas en velocidad)


        
class Conexion_ferroviaria(Conexion):
    def __init__(self, origen,destino, distancia_km, velocidad_max):
        super().__init__(origen, destino,distancia_km)
        if velocidad_max:
            if velocidad_max <= 0:
                raise ValueError("La velocidad máxima debe ser un valor positivo")
            self.velocidad_max = velocidad_max
        else:
            self.velocidad_max = velocidad_max


    def __str__(self):
        return f" {self.origen} a {self.destino} KM: {self.distancia_km} "


class Conexion_autovia(Conexion):
    conexiones_autoviai_totales=[]

    def __init__(self, origen,destino, distancia_km, peso_max):
        super().__init__(origen, destino,distancia_km)
        if peso_max:
            if peso_max <= 0:
                raise ValueError("El peso máximo debe ser un valor positivo")
            self.peso_max = peso_max
        else:
            self.peso_max = peso_max


    def __str__(self):
        return f" {self.origen} a {self.destino} KM: {self.distancia_km} "


class Conexion_maritima(Conexion):

    def __init__(self, origen,destino, distancia_km, tipo_tasa):
        super().__init__(origen, destino,distancia_km)
        self.tipo_tasa = tipo_tasa


    def __str__(self):
        return f" {self.origen} a {self.destino} KM: {self.distancia_km} "


class Conexion_aerea(Conexion):
    def __init__(self, origen,destino, distancia_km, probabilidad_mal_clima):
        super().__init__(origen, destino,distancia_km)
        if probabilidad_mal_clima:
            if not (0 <= probabilidad_mal_clima <= 1):
                raise ValueError("La probabilidad de mal clima debe estar entre 0 y 1")
            self.probabilidad_mal_clima = probabilidad_mal_clima 
        else:
            self.probabilidad_mal_clima = probabilidad_mal_clima

    def __str__(self):
        return f" {self.origen} a {self.destino} KM: {self.distancia_km} "
