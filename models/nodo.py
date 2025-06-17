
class Nodo: 
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(Self):
        return f"{Self.nombre}"

    def __eq__(self, other):
        return isinstance(other, Nodo) and self.nombre == other.nombre

    def __hash__(self):
        return hash(self.nombre)