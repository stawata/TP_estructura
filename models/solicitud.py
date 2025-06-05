class Solicitud:
    def __init__(self,id_carga,peso_kg,origen,destino):
        self.id_carga=id_carga
        self.peso_kg=peso_kg
        self.origen=origen
        self.destino=destino

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
    

