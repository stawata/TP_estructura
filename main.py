from utils.loader import NodoLoader, ConexionLoader, SolicitudLoader

try:
    Ciudades = NodoLoader.cargar_desde_csv("data/nodos.csv")
    Conexiones = ConexionLoader.cargar_desde_csv("data/conexiones.csv", Ciudades)
    Solicitudes = SolicitudLoader.cargar_desde_csv("data/solicitudes.csv", Ciudades)
except FileNotFoundError as e:
    print(f"Error al cargar los archivos: {e}")

print("Ciudades cargadas:")
for ciudad in Ciudades:
    print(ciudad)
print("\nConexiones cargadas:")
for conexion in Conexiones:
    print(conexion)
print("\nSolicitudes cargadas:")
for solicitud in Solicitudes:
    print(solicitud)


