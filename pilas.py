class Pila():
    def __init__(self):
        self.rutas=[]

    def esta_vacia(self):
        return len(self.rutas) == 0
    
    def apilar(self,ruta):
        self.rutas.append(ruta)

    def cima(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.rutas[-1]

    def mostrar(self):
        print("Pila:", self.rutas[::-1]) 

