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

        