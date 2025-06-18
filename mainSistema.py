from utils.loader import NodoLoader, ConexionLoader, SolicitudLoader
from models.itinerario import Itinerario

def menu():
    """
    Muestra el menú principal y devuelve la opción seleccionada.
    """
    print("\n====== Sistema de Transporte CLI ======")
    print("1. Cargar datos de red")
    print("2. Mostrar solicitudes disponibles")
    print("3. Procesar una solicitud")
    print("4. Procesar todas las solicitudes")
    print("5. Graficos de conexiones (en construcción)")
    print("6. Salir")
    print("========================================")
    return input("Seleccione una opción: ")

def main():
    """
    Función principal que ejecuta el sistema de transporte CLI.
    Permite cargar datos, mostrar solicitudes y procesar itinerarios.
    """
    ciudades = []
    conexiones = []
    solicitudes = []

    while True:
        opcion = menu()

        if opcion == "1":
            """
            Carga los datos de nodos, conexiones y solicitudes desde archivos CSV.
            """
            try:
                ciudades = NodoLoader.cargar_desde_csv("data/nodos.csv")
                conexiones = ConexionLoader.cargar_desde_csv("data/conexiones.csv", ciudades)
                solicitudes = SolicitudLoader.cargar_desde_csv("data_extra/muchas_solicitudes/solicitudes.csv", ciudades)
                print("Datos cargados correctamente.")
            except Exception as e:
                print("Error cargando los datos:", e)

        elif opcion == "2":
            """
            Muestra las solicitudes disponibles.
            """
            if not solicitudes:
                print("No hay solicitudes cargadas.")
            else:
                for idx, s in enumerate(solicitudes):
                    print(f"{idx+1}. {s}")

        elif opcion == "3":
            """
            Procesa una solicitud específica seleccionada por el usuario.
            """
            if not solicitudes:
                print("No hay solicitudes cargadas.")
                continue
            try:
                idx = int(input("Ingrese el número de solicitud a procesar: ")) - 1
                if idx < 0 or idx >= len(solicitudes):
                    print("Número inválido.")
                    continue
                s = [solicitudes[idx]]
                itinerario_rapido, itinerario_barato = Itinerario.creador_itinerario(s, conexiones, ciudades)
                print("\n🕒 Itinerario más rápido:\n", itinerario_rapido)
                print("\n💸 Itinerario más barato:\n", itinerario_barato)
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "4":
            """
            Procesa todas las solicitudes cargadas y muestra los itinerarios.
            """
            if not solicitudes:
                print("No hay solicitudes cargadas.")
                continue
            for i, s in enumerate(solicitudes):
                print(f"\nSolicitud {i+1}: {s}")
                itinerario_rapido, itinerario_barato = Itinerario.creador_itinerario([s], conexiones, ciudades)
                print("🕒 Más rápido:", itinerario_rapido)
                print("💸 Más barato:", itinerario_barato)

        elif opcion == "5":
            print("Funcionalidad de gráficos en construcción. Próximamente disponible")
        
        elif opcion == "6":
            print("¡Hasta luego! Gracias por usar el sistema de transporte.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
