from models.nodo import Nodo

class Validaciones():
    @staticmethod
    def validar_float(valor):
        if isinstance(valor,float):
            return True
        else:
            return False
        
    @staticmethod
    def validar_str(valor):
        if isinstance(valor,str):
            return True
        else:
            return
        
    @staticmethod
    def validar_int(valor):
        if isinstance(valor,int):
            return True
        else:
            return False
    
    @staticmethod
    def validar_ciudad(valor): 
        if isinstance(valor, Nodo):  
            return True
        else:
            return False

    @staticmethod
    def validar_lista_conexiones(lista):
        """        Valida si la lista es una lista de instancias de Conexion.
        Args:
            lista (list): Lista a validar.
        Returns:
            bool: True si la lista es válida, False en caso contrario.
        """
         # Verifica si la lista es una instancia de list y si todos los elementos son instancias de Conexion
         # Esto incluye las subclases de Conexion como Conexion_ferroviaria, Conexion_aerea, etc.
        if isinstance(lista, list):
            return True
        else:
            return False
    
    @staticmethod
    def verificar_origen_destino(puntos_de_red, solicitud):
        """
        Verifica si el origen y el destino de la solicitud están en los puntos de red.
        Args:
            puntos_de_red (dict): Diccionario de puntos de red.
            solicitud (Solicitud): Objeto de solicitud que contiene información sobre el origen y el destino.
        Returns:
            bool: True si ambos están en los puntos de red, False en caso contrario.
        """
        return (solicitud.origen.nombre in puntos_de_red and solicitud.destino.nombre in puntos_de_red)