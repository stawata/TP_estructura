#from validaciones import validaciones

class Nodo: 
    ciudades_disponibles = []
    def __init__(self, nombre):
        #validaciones.validar_str(nombre)
        self.nombre = nombre
        Nodo.ciudades_disponibles.append(nombre)
        #LA IDEA ES ACA PONER LOS TRANSPORTES EN LOS QUE PODES LLEGAR A LA CIUDAD
        #es necesario saber los transportes ??????

    def __str__(Self):
        return f"{Self.nombre}"
    