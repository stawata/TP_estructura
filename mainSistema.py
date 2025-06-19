from utils.loader import NodoLoader, ConexionLoader, SolicitudLoader
from models.itinerario import Itinerario
from models.graficos import *


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
    
def mostrar_todas_alternativas(solicitud, ciudades, conexiones):
    from models.vehiculos_herencia import obtener_vehiculos_default, Camion, Tren, Avion, Barcaza
    from models.conexiones import Conexion_aerea, Conexion_autovia, Conexion_maritima, Conexion_ferroviaria
    from utils.grafos import armar_grafo
    from itinerario.buscar_ruta import Buscar_ruta

    tipos_conexion = {Camion: Conexion_autovia, Tren: Conexion_ferroviaria, Avion: Conexion_aerea, Barcaza: Conexion_maritima}
    vehiculos = obtener_vehiculos_default()
    caminos_totales = []

    for vehiculo in vehiculos:
        tipo_conexion = tipos_conexion[vehiculo]
        conexiones_filtradas = list(filter(lambda x: isinstance(x, tipo_conexion), conexiones))
        grafo = armar_grafo(ciudades, conexiones_filtradas)
        buscador = Buscar_ruta(grafo, vehiculo)
        caminos = buscador.buscar_caminos(solicitud)
        # Guardar el tipo de vehículo junto con el camino
        for c in caminos:
            caminos_totales.append((vehiculo.__name__, c))

    print(f"\n========= Se encontraron {len(caminos_totales)} rutas posibles entre origen y destino =========\n")
    if not caminos_totales:
        print("No hay rutas posibles para esta solicitud.\n")
        return

    Buscar_ruta.mostrar_resultados([c[1] for c in caminos_totales])
    print("=" * 80)



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
                ciudades = NodoLoader.cargar_desde_csv("data_extra/muchas_solicitudes/nodos.csv")
                conexiones = ConexionLoader.cargar_desde_csv("data_extra/muchas_solicitudes/conexiones.csv", ciudades)
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
                """
                Muestra una lista numerada de las solicitudes cargadas.
                Para cada solicitud, se imprime su descripción con el str que esta definido en la clase Solicitud.
                """
                for indice, solicitud in enumerate(solicitudes):
                    print(f"{indice+1}. {solicitud}")

        elif opcion == "3":
            """
            Procesa una solicitud específica seleccionada por el usuario.
            """
            if not solicitudes:
                print("No hay solicitudes cargadas.")
                continue
            try:
                indice = int(input("Ingrese el número de solicitud a procesar: ")) - 1
                """
                El usuario me indica el número de la solicitud que quiere procesar.
                """
                if indice < 0 or indice >= len(solicitudes):
                    """
                    Verifica si el índice es válido.
                    Si no es válido, muestra un mensaje de error y vuelve al menú.
                    """
                    print("Número inválido.")
                    continue
                s = [solicitudes[indice]]
                print(f"\nProcesando solicitud: {s[0]}\n")
                """
                Armo la solicitud con el índice indicado por el usuario. 
                En formato lista para poder usar el método creador_itinerario que espera una lista de solicitudes.               
                """
                mostrar_todas_alternativas(s[0], ciudades, conexiones)
                print("Ahora van los itinerarios óptimos...")

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
            for indice, solicitud in enumerate(solicitudes):
                print(f"\nSolicitud {indice+1}: {solicitud}\n")
                
                mostrar_todas_alternativas(solicitud, ciudades, conexiones)
                print("Ahora van los itinerarios óptimos...")

                itinerario_rapido, itinerario_barato = Itinerario.creador_itinerario([solicitud], conexiones, ciudades)
                print("\n🕒 Más rápido:\n", itinerario_rapido)
                print("\n💸 Más barato:\n", itinerario_barato,"\n")
                print("-"*20+"Siguiente solicitud"+"-"*20)
            print("Todas las solicitudes procesadas.")


        elif opcion == "5":
            """
            se va a contemplar que puede haber muchas solicitudes y voy a buscar el peso de cada una
            voy a necesitar el peso para poder calcular los costos
            """
            try : 
                numero= int(input("Ingrese el NUMERO de la solicitud que desea cargar:"))
                if numero <0: 
                    raise ValueError ("Error el numero debe ser POSITIVO")
                if numero > len(solicitudes) or numero <= 0:
                    raise ValueError ("Error no existe esa solicitud")
                else:
                    '''
                    se contempla de que si el usuario elige 1 va a ser la primero por lo tanto el indice de python seria 0
                    se va a buscar el peso de esa solicitud
                    '''
                    num_usuario = numero -1 
                    peso = solicitudes[num_usuario].getpeso_kg()
                    nombre_archivo= str(solicitudes[num_usuario].getid_carga())+ "Costo rapido"

                    itinerario_rapido, itinerario_barato = Itinerario.creador_itinerario([solicitudes[num_usuario]], conexiones, ciudades)
                    '''
                    Obtiene los valores en una lista de cada ruta para poder hacer los graficos
                    '''
            
                    costo_rapida, tiempo_rapida, distancia_rapida = Graficos.datos_ruta( itinerario_rapido.itinerario, itinerario_rapido.modo, conexiones, peso)         
                    costo_barata, tiempo_barato, distancia_barata= Graficos.datos_ruta( itinerario_barato.itinerario, itinerario_barato.modo, conexiones, peso)
                    
                    """
                    Este grafico muetsra la evolucion de los costos tanto para la opcion mas barata como la mas rapida
                    
                    Graficos.Costo_acumulado(distancia_rapida, costo_barata,costo_rapida )
                    Graficos.Tiempo_acumulado(distancia_rapida, tiempo_barato,tiempo_rapida )
                   
                    
                    Se hace una compracion en el mismo grafico de las dos opciones (mas barata y mas rapida)
                    """
                    Graficos.Costo_acumulado_comparado(distancia_rapida, costo_rapida, distancia_barata,costo_barata, nombre_archivo )
                    Graficos.Tiempo_acumulado_comparado(distancia_rapida, tiempo_rapida, distancia_barata,tiempo_barato, nombre_archivo )

                    
            except ValueError as e : 
                print(e)
        
        elif opcion == "6":
            print("¡Hasta luego! Gracias por usar el sistema de transporte.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
