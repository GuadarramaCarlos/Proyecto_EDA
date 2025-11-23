import csv
from collections import defaultdict

# Configuracion de filtros (Segun PDF)
MAX_USUARIOS = 1000   # Subconjunto filtrado
MIN_RATINGS_LIBRO = 35 # Libros con al menos X calificaciones para ser considerados

def cargar_nombres_libros():
    """
    Carga Books.csv para tener un diccionario {ISBN: Titulo}.
    Sirve para mostrar resultados bonitos en el Main.
    """
    titulos = {}
    print("... Cargando catalogo de libros (Books.csv)")
    try:
        # 'latin-1' es necesario para este dataset especifico de Kaggle
        with open("Books.csv", "r", encoding="latin-1") as f:
            reader = csv.DictReader(f)
            for row in reader:
                titulos[row["ISBN"]] = row["Book-Title"]
    except FileNotFoundError:
        print("AVISO: No se encontro Books.csv. Se mostraran solo ISBNs.")
    return titulos

def obtener_datos_filtrados():
    """
    Lee Ratings.csv y genera los mapas necesarios para los grafos.
    Filtra solo los usuarios mas activos.
    """
    print("... Leyendo Ratings.csv y aplicando filtros")
    
    # 1. Identificar a los usuarios mas activos (Top 1000)
    conteo_usuarios = defaultdict(int)
    registros_raw = [] # Guardamos en memoria para no leer el CSV dos veces

    try:
        with open("Ratings.csv", "r", encoding="latin-1") as f:
            reader = csv.DictReader(f)
            for row in reader:
                uid = row["User-ID"]
                registros_raw.append(row)
                conteo_usuarios[uid] += 1
    except FileNotFoundError:
        print("ERROR : No se encuentra Ratings.csv")
        return None, None, {}

    # Ordenamos usuarios por actividad y tomamos los MAX_USUARIOS
    top_usuarios = sorted(conteo_usuarios, key=conteo_usuarios.get, reverse=True)[:MAX_USUARIOS]
    set_top_usuarios = set(top_usuarios) # Convertir a set para busqueda rapida

    print(f"Filtro aplicado: Trabajando con los {len(set_top_usuarios)} usuarios mas activos.")

    # 2. Construir los mapas usando solo esos usuarios
    # Mapa Libro -> {Usuarios}
    mapa_libro_usuarios = defaultdict(set)
    # Mapa Usuario -> {Libros}
    mapa_usuario_libros = defaultdict(set)

    for row in registros_raw:
        uid = row["User-ID"]
        isbn = row["ISBN"]

        if uid in set_top_usuarios:
            mapa_libro_usuarios[isbn].add(uid)
            mapa_usuario_libros[uid].add(isbn)

    #Quitar libros con muy poquitos ratings en este subgrupo
    libros_validos = {isbn for isbn, users in mapa_libro_usuarios.items() if len(users) >= MIN_RATINGS_LIBRO}
    
    # Reconstruimos mapa_libro_usuarios solo con validos
    mapa_libro_final = {k: v for k, v in mapa_libro_usuarios.items() if k in libros_validos}
    
    print(f"Datos listos: {len(mapa_libro_final)} libros y {len(mapa_usuario_libros)} usuarios cargados.")
    
    titulos = cargar_nombres_libros()
    
    return mapa_libro_final, mapa_usuario_libros, titulos