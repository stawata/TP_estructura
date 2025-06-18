# generales
import math

# utils
from utils.loader import NodoLoader, ConexionLoader, SolicitudLoader

# models
from models.itinerario import Itinerario

def main():

    ciudades=NodoLoader.cargar_desde_csv("data/nodos.csv")
    conexiones=ConexionLoader.cargar_desde_csv("data/conexiones.csv", ciudades)
    solicitud=SolicitudLoader.cargar_desde_csv("data/solicitudes.csv", ciudades)
    
    itinerario_rapido, itinerario_barato = Itinerario.creador_itinerario(solicitud, conexiones, ciudades)

    print("Itinerario más rápido:")
    print(itinerario_rapido)
    print("\nItinerario más barato:")   
    print(itinerario_barato)

main()

