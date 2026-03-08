# Unidad IV · Algoritmos: Recorridos y Manipulación de Estructuras

## 🎯 Objetivo

Analizar y aplicar los algoritmos fundamentales que operan sobre estructuras de datos: recorridos BFS y DFS, e inserción/eliminación en listas, pilas, colas y tablas hash.

---

## 1. Recorrido en Amplitud (BFS)

El **BFS (Breadth First Search)** visita los nodos nivel por nivel. Usa una **cola** para recordar los nodos pendientes.

### BFS sobre un árbol

```
Árbol:
        A
       / \
      B   C
     / \   \
    D   E   F

BFS: A → B → C → D → E → F
(Nivel 0) → (Nivel 1) → (Nivel 2)
```

**Algoritmo:**
```
1. Encolar la raíz
2. Mientras la cola no esté vacía:
   a. Desencolar nodo actual
   b. Procesar el nodo actual
   c. Encolar todos los hijos del nodo actual
```

### BFS sobre un grafo

La única diferencia es que hay que controlar los nodos **visitados** (para evitar ciclos).

```python
def bfs(grafo, inicio):
    visitados = set()
    cola = ColaDinamica()
    cola.encolar(inicio)
    visitados.add(inicio)
    
    while not cola.esta_vacia():
        nodo = cola.desencolar()
        procesar(nodo)
        for vecino in grafo[nodo]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.encolar(vecino)
```

**Complejidad:** O(V + E) donde V = vértices, E = aristas.  
**Aplicación:** Camino más corto sin pesos.

---

## 2. Recorrido en Profundidad (DFS)

El **DFS (Depth First Search)** va tan profundo como puede antes de retroceder. Usa **recursión** (o una pila explícita).

### DFS sobre un árbol

```
Árbol:
        A
       / \
      B   C
     / \   \
    D   E   F

DFS (pre-orden): A → B → D → E → C → F
```

**Algoritmo recursivo:**
```
dfs(nodo):
    procesar(nodo)
    para cada hijo de nodo:
        dfs(hijo)
```

### Variantes del DFS en árboles binarios

```
          A
         / \
        B   C
       / \
      D   E

Pre-orden  (raíz, izq, der): A B D E C
En-orden   (izq, raíz, der): D B E A C  ← produce lista ordenada en ABB
Post-orden (izq, der, raíz): D E B C A  ← útil para eliminar árbol
```

---

## 3. Análisis de Algoritmos de Manipulación

### 3.1 Inserción y Eliminación en Listas

| Operación | Lista Simple | Lista Doble | Comentario |
|-----------|-------------|-------------|------------|
| Insertar al inicio | O(1) | O(1) | Cambiar cabeza |
| Insertar al final | O(n) | O(1)* | *Si hay puntero al último |
| Insertar en posición k | O(k) | O(min(k, n-k)) | Recorrer hasta k |
| Eliminar inicio | O(1) | O(1) | Avanzar cabeza |
| Eliminar final | O(n) | O(1)* | *Si hay puntero al último |
| Eliminar nodo dado | O(n) | O(1) | O(1) si tenemos el nodo |
| Buscar | O(n) | O(n) | Recorrido lineal |

### 3.2 Inserción y Eliminación en Pilas y Colas

Todas las operaciones básicas son **O(1)**:

| Estructura | Operación | Complejidad |
|-----------|-----------|-------------|
| Pila | apilar / desapilar | O(1) |
| Cola | encolar / desencolar | O(1) |
| Bicola | insertar/eliminar extremo | O(1) |

### 3.3 Inserción y Búsqueda en Tablas Hash

| Operación | Promedio | Peor caso | Comentario |
|-----------|---------|-----------|------------|
| Insertar | O(1) | O(n) | Peor caso: todas colisionan |
| Buscar | O(1) | O(n) | |
| Eliminar | O(1) | O(n) | |

El peor caso se evita con una buena **función hash** y manteniendo el **factor de carga < 0.75**.

---

## 4. Comparativa: ¿Cuándo usar cada estructura?

```
¿Necesito acceso por índice rápido?
    → Array / Lista estática

¿Necesito insertar/eliminar mucho al inicio?
    → Lista enlazada

¿Necesito LIFO (deshacer, llamadas recursivas)?
    → Pila

¿Necesito FIFO (colas de espera, BFS)?
    → Cola

¿Necesito insertar/eliminar en ambos extremos?
    → Bicola

¿Necesito buscar por clave rápidamente?
    → Tabla Hash

¿Necesito los datos ordenados?
    → Lista ordenada / ABB (ED II)
```

---

## 📁 Archivos de esta unidad

| Archivo | Descripción |
|---------|-------------|
| [`ejemplos/01_bfs_estructuras.py`](./ejemplos/01_bfs_estructuras.py) | BFS sobre árbol y grafo con Cola |
| [`ejemplos/02_dfs_estructuras.py`](./ejemplos/02_dfs_estructuras.py) | DFS recursivo e iterativo |
| [`ejemplos/03_analisis_complejidad.py`](./ejemplos/03_analisis_complejidad.py) | Medición de tiempos reales |
| [`ejercicios/enunciados.md`](./ejercicios/enunciados.md) | Ejercicios propuestos |
