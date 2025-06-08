#from nodo import Ciudad
#from models.nodo import Nodo
#from validaciones.validaciones import validaciones

class Solicitud:
    def __init__(self,id_carga,peso_kg,origen,destino):
        # validaciones.validar_str(origen)
        # validaciones.validar_str(destino)
        # validaciones.validar_float(peso_kg)
        # validaciones.validar_int(id_carga)
        self.id_carga=id_carga
        self.peso_kg=peso_kg
        if Solicitud.validar_ciudad(origen) and Solicitud.validar_ciudad(destino):
            self.origen=origen
            self.destino=destino
        else:
            raise ValueError("El valor debe ser una ciudad que exista")

    def getid_carga(self):
        return self.id_carga
    def getpeso_kg(self):
        return self.peso_kg
    def getorigen(self):
        return self.origen
    def getdestino(self):
        return self.destino

    def __str__(self):
        return f"id_carga: {self.getid_carga()}, capacidad: {self.getpeso_kg()}, origen: {self.getorigen()}, destino: {self.getdestino()}"
    
    # @staticmethod
    # def validar_ciudad(valor): 
    #     if isinstance(valor,Nodo):  
    #          return True
    #     else:
    #          return False
