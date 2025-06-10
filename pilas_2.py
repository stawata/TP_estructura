from models.nodo import *

class Pila:
    def __init__(self):
        self.cima = None  # Dirección al nodo en la cima de la pila

    def esVacia(self):
        return self.cima is None

    def apilar(self, dato):
        nuevo_nodo = dato
        nuevo_nodo.siguiente = self.cima
        self.cima = nuevo_nodo

    def desapilar(self):
        if self.esVacia():
            print("La pila está vacía. No se puede desapilar.")
            return None
        dato = self.cima.dato
        self.cima = self.cima.siguiente
        return dato
    
    def recorrer_pila(self, objeto):
        actual = self.cima
        while actual is not None:
            if objeto == actual.nombre:
                return True
            actual = actual.siguiente
        return False
        

    def visualizar(self):
        actual = self.cima
        elementos = []
        while actual is not None:
            print(actual.nombre + str(actual.tiempo) + str(actual.previo))
            actual = actual.siguiente


    def recorrer(self, objeto):
        actual = self.cima
        while actual != None:
            if actual == objeto: 
                return True
            else: 
                actual = actual.siguiente  
        return False
    
    # def concantenar(self, elemento):
    #     valor = 0
    #     agrupado = ""
    #     while valor < len(elemento):
    #         if elemento[valor] == " ":  
    #             self.apilar(agrupado)
    #             agrupado = ""
    #             valor += 1
    #         else:
    #             agrupado += elemento[valor]
    #             valor += 1
    #     suma = self.cima.siguiente.dato + self.cima.dato  
    #     print(suma)