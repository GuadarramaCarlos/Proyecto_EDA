import csv
import heapq

def construir_grafo_libro_libro(mapa_libro_usuarios, m_minimo):
    isbns = list(mapa_libro_usuarios.keys())
    grafo = {isbn: {} for isbn in isbns}

    for i, a in enumerate(isbns):
        usuarios_a = set(mapa_libro_usuarios[a]["usuarios"])
        for b in isbns[i+1:]:
            usuarios_b = set(mapa_libro_usuarios[b]["usuarios"])
            w = len(usuarios_a & usuarios_b)

            if w >= m_minimo:
                peso = 1 / (1 + w)
                grafo[a][b] = peso
                grafo[b][a] = peso

    return grafo


def construir_grafo_libro(mapa_usuario_libros, m_minimo):
    usuarios = list(mapa_usuario_libros.keys())
    grafo = {u: {} for u in usuarios}

    for i, a in enumerate(usuarios):
        libros_a = set(mapa_usuario_libros[a])
        for b in usuarios[i+1:]:
            libros_b = set(mapa_usuario_libros[b])
            w = len(libros_a & libros_b)

            if w >= m_minimo:
                peso = 1 / (1 + w)
                grafo[a][b] = peso
                grafo[b][a] = peso

    return grafo


def dijkstra(grafo, inicio):
    distancia = {n: float('inf') for n in grafo}
    previo = {n: None for n in grafo}

    distancia[inicio] = 0
    Q = [(0, inicio)]

    while Q:
        dist_u, u = heapq.heappop(Q)

        if dist_u > distancia[u]:
            continue

        for v, peso in grafo[u].items():
            nueva = distancia[u] + peso
            if nueva < distancia[v]:
                distancia[v] = nueva
                previo[v] = u
                heapq.heappush(Q, (nueva, v))

    return distancia, previo


def reconstruir(previo, destino):
    camino = []
    actual = destino
    while actual is not None:
        camino.append(actual)
        actual = previo[actual]
    return camino[::-1]
