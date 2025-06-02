import csv
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
    
    @classmethod
    def leer_archivo(cls, file):
        instancias=[]
        try:
            with open(file,"r",encoding="utf-8") as archivo:
                lector=csv.reader(archivo)
                next(lector)
                for fila in lector:
                    if len(fila) != 4:
                        raise ValueError(f"Fila inválida (faltan datos): {fila}")
                    id_carga,peso_kg,origen,destino=fila
                    if not peso_kg.isdigit():      #revisar por si el peso tiene que ser un float hay que validar de otra manera
                        raise ValueError(f"Fila inválida (el peso no es un numero): {fila}")
                    #deberia validar si el origen y el destino existen

                    instancia=cls(id_carga,peso_kg,origen,destino)
                    instancias.append(instancia)

        except FileNotFoundError:
            print(f"El archivo {file} no existe")
        return instancias
    
file="solicitudes.csv"
try:
    solicitudes = Solicitud.leer_archivo(file)
    for solicitud in solicitudes:
        print(solicitud)
except ValueError as e:
    print("Error de validación: ", e)

