class Planificador:
    def __init__(self, nodos, conexiones, vehiculos):
        self.nodos = nodos
        self.conexiones = conexiones
        self.vehiculos = vehiculos

    def generar_itinerarios(self, solicitud):
        raise NotImplementedError("Este método debe ser implementado en la subclase.")


