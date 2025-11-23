# Módulo 7: Grafos Ponderados  
**Proyecto Final — Estructuras de Datos Avanzadas I (2026-1)**

---

## Integrantes  
- **Carlos Alberto Guadarrama Dávila**
- **Ortega Ortega Genaro Raziel**

---

## Objetivo del módulo  
Construir grafos ponderados a partir de datos de usuarios y libros, y aplicar el **algoritmo de Dijkstra** para obtener caminos mínimos entre nodos seleccionados.  
El módulo genera grafos basados en similitud y analiza relaciones entre entidades mediante distancias inversamente proporcionales al nivel de coincidencia.

---

## Estructuras de datos y algoritmos implementados

### 1. **Grafo ponderado (diccionarios de adyacencia)**  
Los grafos se representan como:

grafo = {
    nodo1: { vecino1: peso1, vecino2: peso2, ... },
    nodo2: { vecino1: peso1, vecino3: peso3, ... },
    ...
}



### 2. Construcción del grafo Libro–Libro
Dos libros se conectan si al menos **m** usuarios calificaron ambos.

**Peso utilizado:**

d = 1/(1 + w)


- **w:** usuarios en común  
- **d:** distancia (menor = más similares)

**Ejemplo:**

b1 → [u1, u2, u5, u7]
b2 → [u2, u3, u5]

w = 2
d = 1 / (1 + 2) = 0.333


---

### 4. Algoritmo de Dijkstra
Implementado mediante un **min-heap**.

| Elemento | Complejidad |
|---------|-------------|
| Extracción del heap | O(log V) |
| Relajación de aristas | O(E log V) |
| **Total** | **O((V + E) log V)** |

---

## Complejidad del módulo

### Construcción de grafos Libro–Libro / Usuario–Usuario

Comparación entre todos los pares:

O(n^2)

Donde:  
- **n:** número de libros o usuarios  
- **c:** costo de calcular intersección  

Con filtros (ej. 1000 elementos), el rendimiento es adecuado.
## Entradas y salidas

### Entradas
- Mapa libro–usuarios o usuario–libros desde:
  - Archivos `.csv`
  - Archivos `.pkl`
- `m_minimo`: coincidencias mínimas  
- Nodo inicial para Dijkstra  

### Salidas
- Grafos `.pkl`
- Mensajes en terminal indicando:
  - Caminos mínimos
  - Pesos acumulados
  - Tiempo de ejecución
  - Número de nodos y aristas  
  - Archivos generados  
  - Log JSON por línea en `logs.log`  

**Ejemplo de log:**
{
  "timestamp": "2025-10-29T18:45:10",
  "module": "graph_weighted",
  "algorithm": "dijkstra",
  "records": 1000,
  "time": 0.87,
  "memory": "14MB"
}

---
## Descripción de funciones

### 1. `construir_grafo_libro_libro(mapa_libro_usuarios, m_minimo)`
Genera el grafo Libro–Libro.

### 2. `construir_grafo_usuario_usuario(mapa_usuario_libros, m_minimo)`
Genera el grafo Usuario–Usuario.

### 3. `dijkstra(grafo, inicio)`
Devuelve distancias y predecesores.

### 4. `reconstruir(previo, destino)`
Reconstruye la ruta mínima.

---

## Reflexión
El módulo identifica similitudes mediante distancias inversas a coincidencias.  
Dijkstra con min-heap permite buen rendimiento incluso con grafos medianos.  
Los caminos obtenidos reflejan relaciones reales en los datos.

---

## Conclusiones
- Los grafos ponderados representan similitudes de forma efectiva.  
- La distancia \(1 / (1 + w)\) es intuitiva y útil.  
- Dijkstra es adecuado para grafos no dirigidos con pesos positivos.  
- El módulo cumple con los requerimientos de construcción, análisis y logging.  
- Es una base sólida para futuros módulos de recomendación o visualización.
