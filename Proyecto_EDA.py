#Importacion de la libreria csv para el uso de la misma
import csv
#Uso para la implementacion de Dijsktra
import heapq    
#Uso del filtrado por parte de Carlos
#funcion grafo usuario-usuario con parametros mapa_libro_usuarios, distancia minima
def construir_grafo_libro_libro(mapa_libro_usuarios, m_minimo):
    #Listado de libros
    isbns = list(mapa_libro_usuarios.keys())
    grafo = {}

    for isbn in isbns:
        grafo[isbn] = {}

    #Comparacion de todos los libros con todos
    for i in range(len(isbns)):
        for j in range(i + 1, len(isbns)):
            a = isbns[i]
            b = isbns[j]

            #Usuarios que calificaron cada libro
            usuarios_a = set(mapa_libro_usuarios[a]["usuarios"])
            usuarios_b = set(mapa_libro_usuarios[b]["usuarios"])

            #Usuarios que calificaron ambos libros (intersección)
            comun = usuarios_a.intersection(usuarios_b)
            w = len(comun)

            # Si comparten al menos m usuarios se agrega la arista
            if w >= m_minimo:
                #Cálculo del peso según d = 1/(1+w)
                peso = 1 / (1 + w)
                grafo[a][b] = peso
                grafo[b][a] = peso

    return grafo
#funcion grafo usuario-usuario con parametros mapa_usariolibros, distancia minima
def construir_grafo_libro(mapa_usuario_libros, m_minimo):
    usuarios=list(mapa_usuario_libros.keys())
    grafo={}
    #Inicializar nodos
    for u in usuarios:
        grafo[u] = {}

    #Comparación de usuarios entre sí
    for i in range(len(usuarios)):
        for j in range(i + 1, len(usuarios)):
            a = usuarios[i]
            b = usuarios[j]
            #Mando de los set de libros calificados por usario a y b
            libros_a = set(mapa_usuario_libros[a])
            libros_b = set(mapa_usuario_libros[b])

            #Libros en común(uso de la funcion "intersection")
            comun = libros_a.intersection(libros_b)
            w = len(comun)
            # Si comparten al menos m usuarios se agrega la arista
            #Dos libros se conectan si comparten al menos m usuarios
            if w >= m_minimo:
                peso = 1 / (1 + w)
                #Cálculo del peso según d = 1/(1+w)
                grafo[a][b] = peso
                grafo[b][a] = peso
    return grafo

#Aplicacion de algoritmo Dijsktra
def dijkstra(grafo, inicio):
    distancia = {}
    previo = {}

    for nodo in grafo:
        distancia[nodo] = float('inf')
        previo[nodo] = None

    distancia[inicio] = 0

    Q = []
    heapq.heappush(Q, (0, inicio))
    #Implementación del algoritmo de Dijkstra (Uso de mini heap)
    while Q:
        distancia_actual, u = heapq.heappop(Q)

        if distancia_actual > distancia[u]:
            continue

        for v, peso in grafo[u].items():
            nueva_distancia = distancia[u] + peso
            #Relajación de la arista (Dijkstra)
            if nueva_distancia < distancia[v]:
                distancia[v] = nueva_distancia
                previo[v] = u
                heapq.heappush(Q, (nueva_distancia, v))

    return distancia, previo

#Reconstruccion del camino
def reconstruir(previo, destino):
    camino = []
    actual = destino
    #Reconstrucción del camino mínimo desde Dijkstra
    while actual is not None:
        camino.append(actual)
        actual = previo[actual]

    return camino[::-1]



