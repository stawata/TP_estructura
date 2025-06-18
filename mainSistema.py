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
                En formato lista para poder usar el método creador_itinerario que espera una lista de solicitudes."""
                
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
                itinerario_rapido, itinerario_barato = Itinerario.creador_itinerario([solicitud], conexiones, ciudades)
                print("\n🕒 Más rápido:\n", itinerario_rapido)
                print("\n💸 Más barato:\n", itinerario_barato,"\n")
                print("-"*20+"Siguiente solicitud"+"-"*20)
            print("Todas las solicitudes procesadas.")


        elif opcion == "5":
            '''se va a contemplar que puede haber muchas solicitudes y voy a buscar el peso de cada una'''
            '''voy a necesitar el peso para poder calcular los costos'''
             
            '''
            como puedo tener muchas solicitudes voy a tener que calcular el itinerario y trabajr sobre eso
            '''
            try : 
                numero= int(input("Ingrese el NUMERO de la solicitud que desea cargar:"))
                if numero <0: 
                    raise ValueError ("Error el numero debe ser POSITIVO")
                if numero > len(solicitudes):
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
            
                    costos, tiempos, distancias = Graficos.datos_ruta( itinerario_rapido.itinerario, itinerario_rapido.modo, conexiones, peso)         
                    #Graficos.Tiempo_acumulado(distancias,tiempos, nombre_archivo)
                    #Graficos.Costo_acumulado(distancias, costos, nombre_archivo)
                    

                    costo_barata, tiempo_barato, distancia_barata= Graficos.datos_ruta( itinerario_barato.itinerario, itinerario_barato.modo, conexiones, peso)
                    #nombre_archivo= str(solicitudes[num_usuario].getid_carga())+ "Costo barato"
                    #Graficos.Costo_acumulado(distancia_barata, costo_barata, nombre_archivo)
                    
                    
                    Graficos.Costo_acumulado_comparado(distancias, costos, distancia_barata,costo_barata, nombre_archivo )
                    Graficos.Tiempo_acumulado_comparado(distancias, tiempos, distancia_barata,tiempo_barato, nombre_archivo )


            except ValueError as e : 
                print(e)
        
        elif opcion == "6":
            print("¡Hasta luego! Gracias por usar el sistema de transporte.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
