Carga de los datos

Lo primero que pasa en el programa es la carga de los datos en los archivos.csv. 
El archivo que tiene las clases y ellas los classmethod para dicha carga es 'utils/loader.py'.
Este archivo tiene tres clases (con sus metodos de clase):
    1. CargaNodo > carga_desde_csv() > toma como parametro la direccion del archivo 'nodo.scv'.
    2. CargaConexion > carga_desde_csv() > toma como parametros la direccion del archivo 'conexiones.scv' y la lista de objetos nodo creados anteriormente.
    3. CargaSolicitud > carga_desde_csv() > toma como parametro la direccion del archivo 'solicitud.scv' y la lista de objetos nodo creados anteriormente.
Cada funcion de carga devuelve una lista de instancias de cada clase (segun corresponda). Basicamente baja los datos y crea las instancias de los objetos.
Por ejemplo CargaNodo.carga_desde_csv('nodo.csv') devuelve una lista de instancias de la clase Nodo.
Ahora algunos detalles de como funcionan los classmethod en cuanto a validaciones:
    CargaNodo.carga_desde_csv() > Solamente valida que el archivo.csv de donde vienen los datos exista y que el nombre del nodo no este vacio.
    CargaConexion.carga_desde_csv() > Valida que el archivo exista, que las conexiones sean entre nodos que hayan sido cargados antes (sino simplemente no crea la conexion) y que los datos que sean obligatorios esten y sean del tipo que corresponda, si no estan o son de otro tipo de dato, no crea la conexion.
    CargaSolicitud.carga_desde_csv() > Valida que el archivo exista, que los datos obligatorios esten y que estos sean del tipo de dato que corresponda, y que la solicitud sea para nodos que hayan sido cargados, si no es asi, lanza un mensaje de error.

---------------------------------------------------------------------------------------------

Red de nodos

La clase `PuntoDeRed` modela un nodo en una red de transporte, como una ciudad o un centro logístico. 
Cada instancia posee un atributo `nombre` y un diccionario `vecinos`, que almacenará los nodos vecinos junto con el costo y el tiempo necesarios para alcanzarlos.

El método `constructor` es una utilidad a nivel de clase que recibe una lista de objetos `Nodo` y crea un diccionario que mapea el nombre de cada nodo a una nueva instancia de `PuntoDeRed`. 
Este método incluye validaciones para asegurarse de que la lista no esté vacía y que todos sus elementos sean instancias de la clase `Nodo`. 
Si estas condiciones no se cumplen, lanza las excepciones correspondientes (`ValueError` o `TypeError`).

El método estático `agregar_vecinos` se encarga de poblar el diccionario `vecinos` para cada `PuntoDeRed` en el diccionario proporcionado. 
Recibe tres argumentos: el diccionario de puntos, una lista de conexiones y un objeto `Solicitud` (que contiene detalles del envío). 
Este método valida sus entradas, asegurando que la solicitud y las conexiones sean del tipo correcto y que tanto el origen como el destino existan en la red.

Para cada punto en la red, el método itera sobre todas las conexiones. 
Si el punto es el origen o el destino de una conexión, determina el tipo de conexión (ferrocarril, aérea, marítima o autopista) y utiliza la clase de vehículo correspondiente para calcular el costo y el tiempo del envío. 
Estos valores se almacenan luego en el diccionario `vecinos`, asociando al nodo vecino con una tupla que contiene el costo y el tiempo. 
Esta estructura permite una planificación de rutas y una estimación de costos eficiente dentro de la red.

Un aspecto sutil es la dependencia de nombres correctos de clases y métodos tanto en las conexiones como en los vehículos, así como la suposición de que cada objeto de conexión y solicitud proporciona los atributos y métodos necesarios. 
Cualquier discrepancia o falta de implementación puede generar errores en tiempo de ejecución.



----------------------------------------------------------------------------------------------------

Dijkstra

El algoritmo de Dikstra se utiliza para determinar el camino de minimo costo en un grafo. Este costo puede ser un parametro como distancia, tiempo, costo($) , etc.
El algoritmo en si funciona apartir de una red de nodos(grafo) partiendo desde el nodo de origen. Primero calcula el costo de los nodos vecinos al del origen y el punto 
base va a moverse al de menor valor. Repite la secuencia calcula el costo de los nodos vecinos y se mueve al del valor mas pequeño. Este sistema va a almacenar en cada nodo el costo 
de recorrido hacia ese nodo y cual fue su nodo anterior.

Se crea "dist" para guardar el costo y tiempo acumulado a cada punto (todos comienzan en infinito excepto el origen). Luego "anterior" que  guarda el punto anterior en el camino más corto. Por 
ultimo "heap" es la  cola de prioridad para seleccionar el próximo nodo.
Durante la ejecución del algoritmo, mientras existan nodos en la cola de prioridad, se extrae aquel con la menor prioridad (según el criterio indicado en usar, ya sea "costo" o "tiempo"). 
A continuación, se recorren todos sus vecinos inmediatos y se calcula el nuevo costo y tiempo que implicaría llegar a cada uno desde el nodo actual. Si el valor del nuevo punto es menor al previamente
registrado —de acuerdo al criterio seleccionado—, se actualiza la distancia acumulada, se guarda el punto anterior para reconstruir el camino y se añade el vecino a la cola para continuar con la exploración. 
Al finalizar, el algoritmo devuelve dos estructuras: dist, que contiene el costo y tiempo mínimos hacia cada punto de la red, y anterior, que permite reconstruir el camino óptimo desde el origen a cualquier destino.

Funcionamiento: 
1. Creamos un diccionario (dist) que va a almacenar todos los puntos de red, utlizando el nombre como clave  y un tupla como valor, la tupla tiene 2 elementos uno es el costo
y el otro es el tiempo.Inicializandolos con valores infinitos.
2. Establece anterior que es un diccionario que alamcena como clave el nombre de la ciudad y como valor la ciudad previa.
3. En el diciconario dist definimos al nodo origen con tiempo y costo 0
4. Crea un heap que es un cola de  prioridad que almacena tuplas con un elemento(costo o tiempo) y el segundo elemento es el nombre de  la ciudad
5. Inicializamos el algoritmo con un  while que se ejecute hasta que heap este vacio
6.heapq.heappop es un metodo de la clase heapq que se encarga de devolverte la tupla de menor prioridad, quiere decir al tener dos tuplas se canalizara la tupla que en su
elemento 1 sea menor que el resto.Ejemplo: heap = [(0.25, Buenos Aires),(0.02, Mar del Plata)] ==> (0.02, Mar del Plata)  
7. Obtiene la tupla del diccionario dist posicionado en actual
8. Realiza un FOR para itera sobre los puntos vecinos de actual, almacenara el nombre, costo nuevo y tiempo nuevo. Estos ultimos 2 valores se obtienen sumando el costo/tiempo que se obtiene 
de puntos de red(dict) y el costo/tiempo que acontece en el diccionario local(dist) explicado del punto 7.
9. Utiliza condicional para visualizar cual es el filtro que queremos realizar(costo o tiempo)
10. Analiza si el costo/tiempo que se obtuvo en el punto 8 es menor que el costo/tiempo que existia en el diccionario(dist) poscionado en el punto vecino. Si  asi es el caso cambiamos 
el valor de costo/tiempo en el diccionario (dist)
11. Establece el previo de la ciudad actual en el diccionario anteriores
12. Con heapq.heappush ,creamos un nuevo elemento en la cola de prioridad heap que tendra el tiempo/costo actualizado y el nombre del vecino al que modifico. 
13. Repite el proceso

Decidimos usar heap en vez de una lista porque su complejidad algoritmica es mas eficiente que una lista. Quiere decir que tarda menos tiempo. Esto lo podemos apreciar en
que el heap tiene una complejidad del tipo O(log n) en cambio si hubiesemos usado una lista seria O(n log n).En la lista cada vez que se agrega un nuevo elemento,se debe ordenar
para que el elemento de menor prioridad quede primero. En cambio en el heap mantiene el orden de prioridad independientemente de la insercion de un nuevo elemento.


-------------------------------------------------------------------------------------------------------
BuscarRuta
La clase BuscarRuta se encarga de encontrar todos los caminos posibles entre una ciudad de origen y una de destino en una red de transporte, considerando el tipo de vehículo disponible y las restricciones asociadas a cada conexión.
La clase se instancia recibiendo como parámetro las conexiones posibles para un tipo de vehículo, organizadas en una estructura de tipo diccionario, donde la clave es el nombre de la ciudad y el valor es una lista de tuplas que contienen la ciudad vecina y el objeto Conexion.
Luego, la función que busca todos los caminos utiliza una estrategia de búsqueda en profundidad mediante una pila, explorando todas las rutas posibles desde el origen.
Decidimos implementar la búsqueda en profundidad con pila, ya que permite recorrer completamente cada posible camino antes de retroceder y explorar alternativas.

Para ello, se crea un ciclo que se ejecuta mientras la pila no esté vacía. Inicialmente, se apila una tupla que contiene el nodo actual (el origen) y el camino recorrido hasta ese momento (que empieza solo con el origen). Al desapilar, si el nodo actual no coincide con el destino, se buscan los vecinos de dicho nodo en el diccionario que se ingresó por parametro comparando, clave del diccionario con el nombre del nodo actual y, por cada uno, se apila una nueva tupla actualizando el nodo actual con la ciudad vecina y agregando esta nueva ciudad al camino que es la lista con el recorrido que vamos hasta ahora. 
Cuando se alcanza el destino, se recorre el camino completo, comparando devuelta el nombre de cada ciudad con las claves del diccionario, y extrayendo por cada una el objeto conexion que nos da la distancia y restriccion de cada tramo, asi podemos ir calculando el costo y el tiempo total tramo por tramo, en base a los métodos definidos en la clase del vehículo.
Finalmente creamos un diccionario con camino, tiempo total y costo total como claves y se agrega a una lista final que guardara cada diccionario.
Este proceso se repite hasta que la pila queda vacía, lo que significa que ya se han explorado todas las posibles rutas entre el origen y el destino.

-------------------------------------------------------------------------------------------------------

Graficos 

Para hacer los gráficos del trabajo usamos matplotlib, que es una librería que te permite mostrar los datos de forma visual. Elegimos hacer gráficos lineales porque nos parecía la mejor forma de ver cómo iban creciendo los costos, tiempos y distancias a medida que la carga avanza.
El problema que tuvimos al principio fue que nuestro algoritmo solo sumaba esos valores y no los guardaba por tramo. 
Así que creamos un método llamado datos_ruta, que recorre la ruta elegida y, según el tipo de transporte (camión, tren, avión, etc.), busca la conexión correspondiente y calcula el costo, el tiempo y la distancia para cada tramo. Todo eso lo vamos guardando en listas para después poder graficarlo.
si la solicitud elegida hace mdq --> bs.as --> junin en la lista se va a guaardar, distancia, tiempo y costo por trayecto. 
Luego utilizamos numpy para modificar estas listas que se se acumule las variables con los valores del tramo anterior. Al usar numpy tambien tuvimos que agregar el primer valor "0" de manera manual 
para que los graficos arranquen desde este punto. 

En vez de que el gráfico se muestre en pantalla de manera abrupta, preferimos que se guarde como imagen (un .png) en la carpeta del proyecto. Cada solicitud tiene su propio gráfico, así no se pisan y podés verlos cuando quieras.
También hicimos que el usuario pueda elegir qué solicitud quiere ver, y en base a eso se generan los gráficos automáticamente. Además, si hay más de un itinerario (por ejemplo, el más barato y el más rápido), mostramos una comparación de los dos para que se vea bien la diferencia entre tiempo y costo.

-------------------------------------------------------------------------------------------------------

Vehiculo

Clase base  que modela un vehículo genérico para transporte, definiendo los atributos esenciales y métodos abstractos que deberán ser implementados por las subclases específicas (ejemplo: Camión, Tren, Avión y Barcaza).

Los atributos son:
 `modo`: Modo de transporte ("automotor", "ferroviario", "aereo", "maritimo").
 `velocidad_nominal`: Velocidad máxima del vehículo en km/h.
 `capacidad`: Capacidad máxima de carga en kilogramos.
 `costo_fijo`: Costo base por uso del vehículo.
 `costo_km`: Costo por kilómetro recorrido.
 `costo_kg`: Costo por kilogramo transportado.

Metodos principales:
 `cantidad_necesaria(peso)`: Calcula cuántas unidades del vehículo se necesitan según la carga.
 `calcular_tiempo(distancia, restriccion)`: Método abstracto para calcular tiempo del trayecto (a implementar en subclases).
 `calcular_costo(distancia, peso)`: Método abstracto para calcular costo del trayecto (a implementar en subclases).
 `puede_usar_conexion(conexion, peso)`: Verifica si el vehículo puede utilizar la conexión dada considerando restricciones específicas.

-------------------------------------------------------------------------------------------------------

Vehiculos_herencia

Este módulo extiende la clase base `Vehiculo` definiendo subclases específicas para cada modo de transporte. 
Cada subclase implementa métodos para el cálculo específico del tiempo y costo según sus restricciones y características particulares.

Subclases definidas: Cada una tiene velocidad nominal, capacidad y los metodos especificos de cada una

1. Camión:
    Métodos específicos para calcular costos (según peso) y tiempos sin restricciones adicionales.

2. Tren:
    Métodos específicos considerando restricciones de velocidad en conexiones ferroviarias.

3. Avión:
    Métodos específicos considerando probabilidades de mal clima que afectan la velocidad efectiva.

4. Barcaza:
    Métodos específicos que diferencian entre conexiones marítimas y fluviales con costos distintos.

Cada subclase implementa sus propios métodos de cálculo, proporcionando un manejo robusto y modular que facilita agregar nuevos tipos de vehículos sin afectar la estructura general.

-------------------------------------------------------------------------------------------------------

mainSistema

Es el archivo principal del sistema que coordina y ejecuta el flujo general del programa mediante una interfaz de línea de comandos (CLI). 
Este módulo permite cargar datos desde archivos CSV, gestionar solicitudes de transporte y visualizar itinerarios óptimos junto con gráficos comparativos.

Las funciones principales son:

 `menu()`: Muestra el menú principal y gestiona la interacción del usuario.
 `mostrar_todas_alternativas(solicitud, ciudades, conexiones)`: Procesa y presenta todas las rutas posibles para una solicitud dada, incluyendo diferentes modos de transporte y sus costos/tiempos asociados.
 `main()`: Coordina la carga de datos inicial desde archivos CSV, permite al usuario seleccionar solicitudes específicas, ejecuta cálculos para obtener rutas óptimas (más rápidas y más baratas), y genera gráficos automáticamente.

El flujo es:
1. Carga inicial: Usuarios cargan nodos, conexiones y solicitudes desde CSV.
2. Visualización y procesamiento de solicitudes: El usuario selecciona qué solicitudes procesar, visualizando todas las alternativas.
3. Optimización de rutas: Usa algoritmo Dijkstra para determinar rutas óptimas según tiempo o costo.
4. Gráficos: Genera visualizaciones que muestran la evolución de costos y tiempos, facilitando la comparación entre rutas más rápidas y económicas.

Este diseño modular y extensible facilita la interacción con el usuario, 
la gestión eficiente de grandes conjuntos de datos, y proporciona claridad en la presentación de resultados optimizados.


------------------------------------------------------------------------------------------------------------

Conexiones

Este módulo define la lógica de las conexiones entre ciudades dentro del sistema, modelando distintos modos de transporte mediante herencia de clases. La clase base Conexion representa una conexión genérica entre dos nodos, indicando el origen, destino y la distancia en kilómetros. A partir de ella, se definen clases hijas específicas para cada tipo de transporte: 
    Conexion_ferroviaria: Añade una restricción de velocidad máxima.
    Conexion_autovia: Considera un peso máximo permitido.
    Conexion_maritima: Permite definir restricciones propias del entorno marítimo
    Conexion_aerea: Incorpora una probabilidad de mal clima expresada como valor entre 0 y 1. 
Todas las conexiones validan que el origen y destino sean instancias válidas de la clase Nodo, y que la distancia sea un valor positivo.


-------------------------------------------------------------------------------------------------------------