
class Nodo: 
    def __init__(self, nombre, peso_maximo, porcentaje):
        self.nombre = nombre
        self.peso_maximo = float(peso_maximo)
        self.porcentaje = float(porcentaje)

    def __str__(Self):
        return f"{Self.nombre}"

    def __eq__(self, other):
        return isinstance(other, Nodo) and self.nombre == other.nombre

    def get_porcentaje_peaje(self):
        return (self.porcentaje or 0) / 100

    def __hash__(self):
        return hash(self.nombre)