class validaciones():
    @staticmethod
    def validar_float(valor):
        if isinstance(valor,float):
            return True
        else:
            raise ValueError("El valor debe ser float")
        
    @staticmethod
    def validar_str(valor):
        if isinstance(valor,str):
            return True
        else:
            raise ValueError("El valor debe ser str")
        
    @staticmethod
    def validar_int(valor):
        if isinstance(valor,int):
            return True
        else:
            raise ValueError("El valor debe ser int")
        
    # @staticmethod
    # def validar_lista(valor):
    #     if isinstance(valor,list):
    #         return True
    #     else:
    #         raise ValueError("El valor debe ser una lista")
        