import matplotlib.pyplot as plt

class GraficosTorta:
    def __init__(self, caminos_totales):
        self.caminos = self.formatear_camino_totales(caminos_totales)

    @staticmethod
    def formatear_camino_totales(caminos_totales):
        """Transforma lista de tuplas (vehiculo, datos) en lista de diccionarios unificados."""
        formateados = []
        for vehiculo, datos in caminos_totales:
            datos["vehiculo"] = vehiculo
            formateados.append(datos)
        return formateados

    def agrupar_por_vehiculo(self, clave):
        """Agrupa por tipo de vehículo y suma la clave especificada (tiempo o costo)."""
        agrupado = {}
        for camino in self.caminos:
            vehiculo = camino["vehiculo"]
            agrupado[vehiculo] = agrupado.get(vehiculo, 0) + camino[clave]
        return agrupado


    def graficar(self, clave="costo_total"):
        """Muestra gráfico de torta."""
        datos = self.agrupar_por_vehiculo(clave)
        etiquetas = list(datos.keys())
        valores = list(datos.values())

        if not valores or sum(valores) == 0:
            print(f"No hay datos válidos para graficar por '{clave}'")
            return

        plt.figure(figsize=(8, 6))
        plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=140)
        plt.title(f"Distribución de {clave.replace('_', ' ')} por tipo de vehículo")
        plt.axis('equal')
        plt.show()


