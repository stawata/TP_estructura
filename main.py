from utils.loader import NodoLoader, ConexionLoader, SolicitudLoader

Ciudades = NodoLoader.cargar_desde_csv("data/nodos.csv")
Conexiones = ConexionLoader.cargar_desde_csv("data/conexiones.csv", Ciudades)
Solicitudes = SolicitudLoader.cargar_desde_csv("data/solicitudes.csv", Ciudades)

print("Ciudades cargadas:")
for ciudad in Ciudades:
    print(ciudad.nombre)
print("\nConexiones cargadas:")
for conexion in Conexiones:
    print(conexion)
print("\nSolicitudes cargadas:")
for solicitud in Solicitudes:
    print(solicitud)

