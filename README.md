# Sistema de Construcción de Grafos y Búsqueda de Caminos con Dijkstra

Este proyecto implementa un conjunto de funciones para:

1. **Construir grafos basados en similitudes**  
   - Entre libros, a partir de usuarios que los han calificado.  
   - Entre usuarios, a partir de los libros que ambos han calificado.

2. **Calcular rutas más cortas** mediante el **algoritmo de Dijkstra**.

3. **Reconstruir el camino mínimo** desde un nodo de inicio hasta un destino.

Además, se incluye un archivo separado con **pruebas unitarias (pytest)** para validar el funcionamiento del código original.

---

## Contenido del proyecto

### 1. `original.py`
Contiene las siguientes funciones principales:

### **a) construir_grafo_libro_libro(mapa_libro_usuarios, m_minimo)**
Construye un grafo donde:
- Cada nodo es un **libro (ISBN)**.
- Se crea una arista entre dos libros si **comparten al menos `m_minimo` usuarios**.
- El peso entre dos libros se calcula como:

\[
d = \frac{1}{1 + w}
\]

donde `w` es la cantidad de usuarios en común.

Es útil para sistemas de recomendación basados en similitud de usuarios.

---

### **b) construir_grafo_libro(mapa_usuario_libros, m_minimo)**
Construye un grafo donde:
- Cada nodo es un **usuario**.
- Dos usuarios se conectan cuando **comparten al menos `m_minimo` libros**.
- El peso se calcula igual que en la función anterior.

Permite modelar similitudes entre usuarios según sus gustos.

---

### **c) dijkstra(grafo, inicio)**
Implementa el **algoritmo de Dijkstra** usando una **cola de prioridad (heap)**.

Retorna:
- `distancia`: tabla con la distancia mínima desde el nodo inicio hacia todos los demás.
- `previo`: diccionario para reconstruir caminos.

---

### **d) reconstruir(previo, destino)**
Reconstruye la **ruta mínima** obtenida por Dijkstra desde el nodo de inicio hasta el nodo final.

---

## 2. `test_codigo_original.py`
Archivo de pruebas unitarias que verifica:

- Construcción correcta de grafos de libros.
- Construcción correcta de grafos de usuarios.
- Funcionamiento del algoritmo de Dijkstra.
- Reconstrucción correcta del camino mínimo.

Se ejecuta con:


