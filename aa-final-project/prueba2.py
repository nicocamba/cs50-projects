import math

#Código que implementa el algoritmo A* para buscar de forma eficiente la ruta más corta entre
#las poblaciones gallegas más importantes

#Estas poblaciones seán las siguientes:
#0)Barco de Valdeorras, 1)Ourense, 2)Bande, 3)Monforte, 4)Verín, 5)Lalín, 6)Lugo, 7)Ribadeo, 8)Viveiro
#9)Ferrol, 10)Coruña, 11)Santiago, 12) Finisterra, 13)Ribeira, 14)Pontevedra, 15)Vigo, 16)Ribadavia,
#17)Cerdedo, 18)La estrada, 19)Arzúa

#Matriz de incidencia respetando los índices anteriores(el elemento (i,j) representa la distancia de la carretera
#para ir desde i) hasta j)). Las poblaciones no conectadas dan como resultado 10000
G = [[0, 10000, 10000, 71, 100, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],
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
[10000, 10000, 10000, 10000, 10000, 41, 66, 151, 133, 89, 74, 37, 10000, 10000, 10000, 10000, 10000, 67, 10000, 0]]

#Debemos elegir el punto inicial y el final (en principio lo hará el usuario desde la página web)
vertice_inicial = 1
vertice_final = 12

#Se define un vector con las distancias al vertice inicial
distancias = G[vertice_inicial]
distancias_heuristica = distancias

coordenadas = [[42.41643, -6.98557], [42.33579, -7.86388], [42.03081, -7.97291], [42.51902, -7.51581], [41.94026, -7.43495],
[42.66115, -8.11103], [43.00974, -7.55676], [43.53368, -7.04035], [43.66426, -7.59453], [43.48965, -8.21935], [43.36234, -8.41154],
[42.87686, -8.54417], [42.90780, -9.26503], [42.55406, -8.99225], [42.42988, -8.64462], [42.24060, -8.72073],
[42.28885, -8.14205], [42.53276, -8.39033], [42.68990, -8.49094], [42.92969, -8.16078]]

#Ayudandonos de estas coordenadas calcularemos las distancias de las poblaciones a la población de destino
#Supondremos que la tierra es plana (podemos hacerlo pues solo estamos considerando Galicia)
#Un grado equivale a 78.85 km en la latitud de Burdeos (similar a la gallega)
heuristica = []
n = 0
for n in range(len(G)):
    heuristica.append(0)
m = 0
for m in range(len(G)):
    heuristica[m] = round(math.sqrt(math.pow((coordenadas[m][0] - coordenadas[vertice_final][0])*78.85, 2) + math.pow((coordenadas[m][1] - coordenadas[vertice_final][1])*78.85, 2)))

#Se define a su vez un vector que contiene los vertices ya optimizados(visitados), conteiene un 1 si ya esta visitado
#y un 0 si aún no lo está
#Debemos también definir el vector que contiene el camino, en este caso contendrá el índice del vértice anterior
vertices_visitados = []
ruta = []
completado = []
i = 0
for i in range(len(G)):
    vertices_visitados.append(0)
    ruta.append(1000)
    completado.append(1)

ruta[vertice_inicial] = vertice_inicial

#Ya tenemos inicializado el esquema del algoritmo, ahora necesitamos los bucles
while vertices_visitados != completado:
    j = 0
    v = 0
    min = 5000
    w = 0
    for j in range(len(G)):
        #Hay que añadir la h aqui, desde el que vienes
        if vertices_visitados[j] == 0 and distancias_heuristica[j] + heuristica[j]  < min:
            min = distancias_heuristica[j] + heuristica[j]
            w = j
            vertices_visitados[w] = 1
    for v in range(len(G)):
        if distancias_heuristica[w] + G[w][v] <= distancias_heuristica[v]:
            distancias[v] = distancias[w] + G[w][v]
            distancias_heuristica[v] = distancias_heuristica[w] + G[w][v]
            if v!= w:
                ruta[v] = w

    if w == vertice_final:
        break
print(ruta)
print(distancias)

