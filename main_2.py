
# generales
import math

# utils
from utils.loader import NodoLoader, ConexionLoader, SolicitudLoader

# models
from models.itinerario import Itinerario

def main():

    ciudades=NodoLoader.cargar_desde_csv("data_extra/distancia_1km/nodos.csv")
    solicitud=SolicitudLoader.cargar_desde_csv("data_extra/distancia_1km/solicitudes.csv", ciudades)
    conexiones=ConexionLoader.cargar_desde_csv("data_extra/distancia_1km/conexiones.csv", ciudades)
    
    itinerario_rapido, itinerario_barato = Itinerario.creador_itinerario(solicitud, conexiones, ciudades)

    print("Itinerario más rápido:")
    print(itinerario_rapido)
    print("\nItinerario más barato:")   
    print(itinerario_barato)

main()
