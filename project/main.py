from flask import Flask, render_template, request
import math

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

Poblaciones = ["Barco de Valdeorras", "Ourense", "Bande", "Monforte", "Verín", "Lalín", "Lugo", "Ribadeo", "Viveiro", "Ferrol", "Coruña", "Santiago",
"Finisterra", "Ribeira", "Pontevedra", "Vigo", "Ribadavia", "Cerdedo", "La_Estrada", "Arzúa"]

poblacion_inicial = None
poblacion_final = None

# Matriz de incidencia respetando los índices anteriores (el elemento (i, j) representa la distancia de la carretera
# para ir desde i) hasta j)). Las poblaciones no conectadas dan como resultado 10000

G = [
    [0, 10000, 10000, 71, 100, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],
    [10000, 0, 40, 47, 69, 54, 93, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 29, 65, 10000, 10000],
    [10000, 40, 0, 10000, 67, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 109, 56, 10000, 10000, 10000],
    [71, 47, 10000, 0, 10000, 65, 66, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 101, 10000, 10000],
    [100, 69, 67, 10000, 0, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],
    [10000, 54, 10000, 65, 10000, 0, 70, 10000, 160, 122, 115, 52, 10000, 10000, 10000, 10000, 60, 39, 39, 41],
    [10000, 93, 10000, 66, 10000, 70, 0, 72, 104, 112, 101, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 66],
    [10000, 10000, 10000, 10000, 10000, 10000, 72, 0, 64, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 151],
    [10000, 10000, 10000, 10000, 10000, 160, 104, 64, 0, 61, 10000, 156, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 133],
    [10000, 10000, 10000, 10000, 10000, 122, 112, 10000, 61, 0, 54, 95, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 89],
    [10000, 10000, 10000, 10000, 10000, 115, 101, 10000, 10000, 54, 0, 69, 104, 10000, 10000, 10000, 10000, 10000, 10000, 74],
    [10000, 10000, 10000, 10000, 10000, 52, 10000, 10000, 156, 95, 69, 0, 82, 64, 63, 10000, 10000, 10000, 27, 37],
    [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 104, 82, 0, 97, 126, 10000, 10000, 10000, 10000, 10000],
    [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 64, 97, 0, 71, 10000, 137, 81, 68, 10000],
    [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 63, 126, 71, 0, 28, 10000, 30, 44, 10000],
    [10000, 10000, 109, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 28, 0, 67, 10000, 10000, 10000],
    [10000, 29, 56, 10000, 10000, 60, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 137, 10000, 67, 0, 56, 10000, 10000],
    [10000, 65, 10000, 101, 10000, 39, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 81, 30, 10000, 56, 0, 25, 67],
    [10000, 10000, 10000, 10000, 10000, 39, 10000, 10000, 10000, 10000, 10000, 27, 10000, 68, 44, 10000, 10000, 25, 0, 10000],
    [10000, 10000, 10000, 10000, 10000, 41, 66, 151, 133, 89, 74, 37, 10000, 10000, 10000, 10000, 10000, 67, 10000, 0]
]

# Definimos las coordenadas de las Poblaciones:
coordenadas = [
    [42.41643, -6.98557], [42.33579, -7.86388], [42.03081, -7.97291], [42.51902, -7.51581], [41.94026, -7.43495],
    [42.66115, -8.11103], [43.00974, -7.55676], [43.53368, -7.04035], [43.66426, -7.59453], [43.48965, -8.21935],
    [43.36234, -8.41154], [42.87686, -8.54417], [42.90780, -9.26503], [42.55406, -8.99225], [42.42988, -8.64462],
    [42.24060, -8.72073], [42.28885, -8.14205], [42.53276, -8.39033], [42.68990, -8.49094], [42.92969, -8.16078]
]

# Función para calcular la distancia heurística A* entre dos poblaciones
def calcular_heuristica(poblacion_actual, poblacion_destino):
    distancia = round(math.sqrt(
        (coordenadas[poblacion_actual][0] - coordenadas[poblacion_destino][0]) * 78.85**2 +
        (coordenadas[poblacion_actual][1] - coordenadas[poblacion_destino][1]) * 78.85**2))
    return distancia

# Función que implementa el algoritmo A* para encontrar la ruta más corta
def algoritmo_a_estrella(vertice_inicial, vertice_final):
    if vertice_inicial < 0 or vertice_final < 0 or vertice_inicial >= len(G) or vertice_final >= len(G):
        raise ValueError("Los índices de las poblaciones seleccionadas son inválidos.")

    distancias = [10000] * len(G)
    distancias[vertice_inicial] = 0
    vertices_visitados = [False] * len(G)
    ruta = [-1] * len(G)

    while True:
        min_distancia = 10000
        vertice_actual = None

        for v in range(len(G)):
            if not vertices_visitados[v] and distancias[v] < min_distancia:
                min_distancia = distancias[v]
                vertice_actual = v

        if vertice_actual is None or vertice_actual == vertice_final:
            break

        vertices_visitados[vertice_actual] = True

        for v in range(len(G)):
            distancia_nueva = distancias[vertice_actual] + G[vertice_actual][v]
            if not vertices_visitados[v] and distancia_nueva < distancias[v]:
                distancias[v] = distancia_nueva
                ruta[v] = vertice_actual

    # Construir la ruta óptima desde el vertice_final hasta el vertice_inicial
    camino = []
    v = vertice_final
    while v != -1:
        camino.append(v)
        v = ruta[v]
    camino.reverse()

    return camino

@app.route('/', methods=['GET', 'POST'])
def index():
    global poblacion_inicial, poblacion_final, ruta_optima

    # Inicializamos ruta_optima
    ruta_optima = None

    if request.method == 'POST':
        poblacion_inicial = request.form.get('Poblacion-Inicial')
        poblacion_final = request.form.get('Poblacion-Final')

        # Verificar si las poblaciones ingresadas existen en la lista Poblaciones
        if poblacion_inicial not in Poblaciones or poblacion_final not in Poblaciones:
            return render_template('index.html', Poblaciones=Poblaciones, error="Población no válida.")

        # Convierte las poblaciones a índices numéricos para usarlos en la matriz G
        vertice_inicial = Poblaciones.index(poblacion_inicial)
        vertice_final = Poblaciones.index(poblacion_final)

        # Calcula la ruta más corta utilizando el algoritmo A*
        ruta_optima = algoritmo_a_estrella(vertice_inicial, vertice_final)

        # Redirige a la página de resultados (busqueda.html) para mostrar la ruta y las imágenes
        return render_template('busqueda.html', Poblaciones=Poblaciones, poblacion_inicial=poblacion_inicial, poblacion_final=poblacion_final, ruta_optima=ruta_optima)

    return render_template('index.html', Poblaciones=Poblaciones)

@app.route('/busqueda')
def busqueda():
    global poblacion_inicial, poblacion_final, Poblaciones

    if poblacion_inicial is None or poblacion_final is None:
        return render_template('busqueda.html', Poblaciones=Poblaciones, error="Debes seleccionar poblaciones primero.")

    # Pasar la lista de poblaciones a la plantilla busqueda.html
    return render_template('busqueda.html', Poblaciones=Poblaciones, poblacion_inicial=poblacion_inicial, poblacion_final=poblacion_final)

if __name__ == "__main__":
    app.debug = True
    app.run()
