import heapq


def construir_grafo_libro_libro(mapa_libro_usuarios, m_minimo):
    """
    Crea grafo donde nodos son Libros. Se conectan si comparten 'm' usuarios.
    """
    isbns = list(mapa_libro_usuarios.keys())
    # Inicializar nodos
    grafo = {isbn: {} for isbn in isbns}
    
    rango = len(isbns)
    print(f"Procesando {rango} libros para buscar coincidencias... (Espere)")

    for i, a in enumerate(isbns):
        # NOTA: En datos.py usamos sets directos, asi que accedemos directo a mapa[a]
        usuarios_a = mapa_libro_usuarios[a]
        
        # Comparamos contra los siguientes para no repetir
        for b in isbns[i+1:]:
            usuarios_b = mapa_libro_usuarios[b]
            
            # Usuarios en comun
            w = len(usuarios_a & usuarios_b)

            if w >= m_minimo:
                peso = 1 / (1 + w)
                grafo[a][b] = peso
                grafo[b][a] = peso # Grafo no dirigido

    return grafo


def construir_grafo_usuario_usuario(mapa_usuario_libros, m_minimo):
    """
    Crea grafo donde nodos son Usuarios. Se conectan si comparten 'm' libros.
    """
    usuarios = list(mapa_usuario_libros.keys())
    grafo = {u: {} for u in usuarios}
    
    rango = len(usuarios)
    print(f"Procesando {rango} usuarios para buscar coincidencias... (Espere)")

    for i, a in enumerate(usuarios):
        libros_a = mapa_usuario_libros[a]
        
        for b in usuarios[i+1:]:
            libros_b = mapa_usuario_libros[b]
            
            #Libros en comun
            w = len(libros_a & libros_b)

            if w >= m_minimo:
                peso = 1 / (1 + w)
                grafo[a][b] = peso
                grafo[b][a] = peso

    return grafo


def dijkstra(grafo, inicio):
    # Inicializacion
    distancia = {n: float('inf') for n in grafo}
    previo = {n: None for n in grafo}

    if inicio not in grafo:
        return {}, {}

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
    # Proteccion por si el destino no fue alcanzado
    if destino not in previo or previo[destino] is None:
        return []
        
    while actual is not None:
        camino.append(actual)
        actual = previo[actual]
    return camino[::-1]

#Asserts
