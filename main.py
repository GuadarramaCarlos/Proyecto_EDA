import time
import json
import pickle
import datetime
import datos       # Import de Persona 1
import algoritmos  # Import de Persona 2
# Importa para la validacion de la memoria usuaria
import psutil
import os
#Funcion para verificar la memoria (real) usada
def memoria_usada_mb():
    proceso = psutil.Process(os.getpid())
    memoria_bytes = proceso.memory_info().rss  # RAM real usada
    return round(memoria_bytes / (1024 * 1024), 2)


def guardar_log(modulo, algoritmo, num_elementos, tiempo):
    """
    Escribe en logs.log cumpliendo el formato JSON.
    """
    registro = {
        "timestamp": datetime.datetime.now().isoformat(),
        "module": modulo,
        "algorithm": algoritmo,
        "records": num_elementos,
        "time": round(tiempo, 4)
    }
    try:
        with open("logs.log", "a", encoding="utf-8") as f:
            f.write(json.dumps(registro) + "\n")
        print(" -> Log registrado exitosamente.")
    except Exception as e:
        print(f"Error al guardar log: {e}")

def guardar_pkl(grafo, nombre_archivo):
    try:
        with open(nombre_archivo, "wb") as f:
            pickle.dump(grafo, f)
        print(f" -> Grafo guardado en archivo: {nombre_archivo}")
    except Exception as e:
        print(f"Error guardando PKL: {e}")


def main():
    print("=== SISTEMA DE GRAFOS PONDERADOS (Mod. 7) ===")
    
    #Llama a datos.py
    mapa_libros, mapa_usuarios, titulos = datos.obtener_datos_filtrados()
    
    if not mapa_libros:
        print("No hay datos para procesar. Saliendo.")
        return

    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Generar Grafo Libro-Libro (Similitud)")
        print("2. Generar Grafo Usuario-Usuario (Similitud)")
        print("3. Salir")
        
        opcion = input("Seleccione opcion: ")
        
        if opcion == "3":
            break
            
        grafo = {}
        nombre_algoritmo = ""
        archivo_salida = ""
        elementos_base = 0
        
        m_filtro = 3 
        
        inicio_proceso = time.time()
        
        if opcion == "1":
            print(f"\nGenerando Grafo de Libros (m={m_filtro})...")
            grafo = algoritmos.construir_grafo_libro_libro(mapa_libros, m_filtro)
            nombre_algoritmo = "dijkstra_libros"
            archivo_salida = "grafo_libros.pkl"
            elementos_base = len(mapa_libros)
        
        elif opcion == "2":
            print(f"\nGenerando Grafo de Usuarios (m={m_filtro})...")
            grafo = algoritmos.construir_grafo_usuario_usuario(mapa_usuarios, m_filtro)
            nombre_algoritmo = "dijkstra_usuarios"
            archivo_salida = "grafo_usuarios.pkl"
            elementos_base = len(mapa_usuarios)
            
        else:
            print("Opcion no valida.")
            continue
            
        fin_construccion = time.time()
        tiempo_construccion = fin_construccion - inicio_proceso
        print(f"Grafo construido con {len(grafo)} nodos y muchas aristas.")
        
        if len(grafo) > 0:
            # Tomamos el primer nodo disponible del grafo para probar
            nodo_inicio = list(grafo.keys())[0]
            print(f"\nEjecutando Dijkstra desde el nodo: {nodo_inicio}")
            
            # Si es libro, mostrar titulo
            if opcion == "1" and nodo_inicio in titulos:
                print(f"Libro: '{titulos[nodo_inicio]}'")

            distancias, previo = algoritmos.dijkstra(grafo, nodo_inicio)
            
            # Buscar un destino alcanzable para mostrar el camino
            destino_ejemplo = None
            for nodo, dist in distancias.items():
                if dist > 0 and dist != float('inf'):
                    destino_ejemplo = nodo
                    break # Encontramos uno, salimos
            
            if destino_ejemplo:
                camino = algoritmos.reconstruir(previo, destino_ejemplo)
                print("\n--- RESULTADO CAMINO MAS CORTO ---")
                
                if opcion == "1": # Mostrar titulos si son libros
                    t_origen = titulos.get(nodo_inicio, nodo_inicio)
                    t_dest = titulos.get(destino_ejemplo, destino_ejemplo)
                    print(f"De: {t_origen}")
                    print(f"A:  {t_dest}")
                else:
                    print(f"De usuario {nodo_inicio} a usuario {destino_ejemplo}")
                    
                print(f"Distancia (Similitud inversa): {distancias[destino_ejemplo]:.4f}")
                print(f"Pasos: {len(camino)}")
            else:
                print("El nodo inicial no tiene conexiones fuertes con otros nodos (Islas).")

        tiempo_total = time.time() - inicio_proceso
        print(f"\nTiempo total de ejecucion: {tiempo_total:.4f} seg")
        
        # Asserts
        assert isinstance(grafo, dict), "ERROR: El grafo no es un diccionario."
        assert len(grafo) > 0, "ERROR: El grafo esta vacio."
        assert elementos_base > 0, "ERROR: No hay elementos base para construir el grafo."
        #Guardar archivos y logs
        guardar_pkl(grafo, archivo_salida)
        guardar_log("grafos_ponderados", nombre_algoritmo, elementos_base, tiempo_total)
        
        
        #Presion al final de las opciones 1 y 2
        if opcion in ("1", "2"):
            summary = {
                "timestamp": datetime.datetime.now().isoformat(),
                "module": "Grafos ponderados",
                "algorithm": nombre_algoritmo,
                "fields": ["Author", "Title"] if opcion == "1" else ["UserID"],
                "records": elementos_base,
                "time": round(tiempo_total, 4),
                "memory": f"{memoria_usada_mb()} MB"
            }
            print("\nResumen final de ejecucion:")
            print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()




