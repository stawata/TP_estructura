class Pila:
    def __init__(self):
        self.elementos = []

    def esta_vacia(self):
        return len(self.elementos) == 0

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        else:
            return None  # O lanzar excepción

    def cima(self):
        if not self.esta_vacia():
            return self.elementos[-1]
        else:
            return None