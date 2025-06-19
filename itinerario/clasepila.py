class NodoPila:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Pila:
    def __init__(self):
        self.tope = None

    def esta_vacia(self):
        return self.tope is None

    def apilar(self, elemento):
        nuevo_nodo = NodoPila(elemento)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo

    def desapilar(self):
        if self.esta_vacia():
            return None  # o lanzar excepción
        valor = self.tope.valor
        self.tope = self.tope.siguiente
        return valor

    def cima(self):
        if self.esta_vacia():
            return None
        return self.tope.valor