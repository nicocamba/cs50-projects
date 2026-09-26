def algoritmo_a_estrella(vertice_inicial, vertice_final):
    distancias = G[vertice_inicial]
    vertices_visitados = [0] * len(G)
    ruta = [-1] * len(G)

    ruta[vertice_inicial] = vertice_inicial

    while True:
        min_distancia = 10000
        vertice_actual = None

        for v in range(len(G)):
            if not vertices_visitados[v] and distancias[v] < min_distancia:
                min_distancia = distancias[v]
                vertice_actual = v

        if vertice_actual is None:
            break

        vertices_visitados[vertice_actual] = 1

        for v in range(len(G)):
            distancia_nueva = distancias[vertice_actual] + G[vertice_actual][v]
            if not vertices_visitados[v] and distancia_nueva < distancias[v]:
                distancias[v] = distancia_nueva
                ruta[v] = vertice_actual

    return ruta