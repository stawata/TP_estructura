class Ciudad: 
    ciudades_disponibles = []
    def __init__(self, nombre):
        self.nombre = nombre
        Ciudad.ciudades_disponibles.append(nombre)
        #LA IDEA ES ACA PONER LOS TRANSPORTES EN LOS QUE PODES LLEGAR A LA CIUDAD
        #es necesario saber los transportes ??????
        self.transportes_disponibles=[]

    def __str__(Self):
        return f"{Self.nombre}"
    