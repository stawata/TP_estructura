class Ciudad: 
    ciudades_disponibles = []
    def __init__(self, nombre):
        self.nombre = nombre
        Ciudad.ciudades_disponibles.append(nombre)

    def __str__(Self):
        return f"{Self.nombre}"
    

lista = ["caba", "pinamar"]

for i in range(len (lista)):
    objeto = Ciudad(lista[i])

print (Ciudad.ciudades_disponibles)