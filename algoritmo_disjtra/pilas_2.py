'''Esta pila es un objeto que va a llevar un  conteo de los recorridos posibles para llegar al destino. Entocnes 
el primer nodo que ingresamos es el origen y luego vamos a ir agregando nodos siempre verificando que la pila que estamos formando 
sea una que todavia no existe. Quiere decir que la base de nuestra busqueda es que va a encontrar caminos diferentes fijandose que 
la pila que vamos armando sea una que todavia no existe. '''

class Pila:
    def __init__(self):
        self.cima = None  # Dirección al nodo en la cima de la pila

    def esVacia(self):
        return self.cima is None

    def apilar(self, dato):
        nuevo_nodo = dato
        nuevo_nodo.siguiente = self.cima
        self.cima = nuevo_nodo

    
    def recorrer_pila(self, objeto):
        actual = self.cima
        while actual is not None:
            if objeto == actual.nombre:
                return True
            actual = actual.siguiente
        return False
        
    def recorrer_camino(self, destino):
        actual = self.cima
        tiempo = 0
        camino_optimo = list()
        while actual is not None:
            if destino == actual.nombre:
                camino_optimo.append(actual)
                destino = actual.previo
                if tiempo == 0: tiempo += actual.tiempo
            actual = actual.siguiente
        return camino_optimo, tiempo


    
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