# ejemplos/01_bfs_dfs_algoritmos.py
# Unidad IV: BFS y DFS usando las estructuras del curso
# ======================================================
# Este archivo implementa BFS y DFS reutilizando las estructuras
# Cola y Pila que ya aprendimos. Así se ve cómo los algoritmos
# dependen de la estructura de datos subyacente.

from collections import deque
from typing import Any, Optional, List, Dict


# ==============================================================
# ÁRBOL GENÉRICO (para demostrar recorridos)
# ==============================================================

class NodoArbol:
    """Nodo de un árbol con múltiples hijos."""
    
    def __init__(self, dato: Any):
        self.dato = dato
        self.hijos: List['NodoArbol'] = []
    
    def agregar_hijo(self, nodo: 'NodoArbol') -> None:
        self.hijos.append(nodo)
    
    def __repr__(self):
        return f"Nodo({self.dato})"


# ==============================================================
# BFS (Búsqueda en Amplitud) - usa Cola
# ==============================================================

def bfs_arbol(raiz: NodoArbol) -> List[Any]:
    """
    BFS sobre un árbol genérico. Recorre nivel por nivel.
    Usa una COLA (FIFO) para procesar nodos en orden de llegada.
    
    Visualización:
              A          ← Nivel 0
            / | \\
           B  C  D       ← Nivel 1
          /\\     \\
         E  F     G      ← Nivel 2
    
    BFS: A, B, C, D, E, F, G
    
    Returns:
        Lista de datos en orden BFS.
    """
    if raiz is None:
        return []
    
    resultado = []
    cola = deque([raiz])   # ← COLA: FIFO
    
    while cola:
        nodo = cola.popleft()         # desencolar del frente
        resultado.append(nodo.dato)
        
        for hijo in nodo.hijos:       # encolar al fondo
            cola.append(hijo)
    
    return resultado


def bfs_por_niveles(raiz: NodoArbol) -> List[List[Any]]:
    """
    BFS que agrupa los nodos por nivel.
    
    Returns:
        Lista de listas: [[nivel0], [nivel1], [nivel2], ...]
    """
    if raiz is None:
        return []
    
    niveles = []
    cola = deque([raiz])
    
    while cola:
        # Todos los nodos actuales en la cola son del mismo nivel
        tamanio_nivel = len(cola)
        nivel_actual = []
        
        for _ in range(tamanio_nivel):
            nodo = cola.popleft()
            nivel_actual.append(nodo.dato)
            for hijo in nodo.hijos:
                cola.append(hijo)
        
        niveles.append(nivel_actual)
    
    return niveles


def bfs_grafo(grafo: Dict, inicio: Any) -> List[Any]:
    """
    BFS sobre un grafo representado como diccionario de adyacencia.
    Controla nodos visitados para manejar ciclos.
    
    Returns:
        Lista de nodos en orden BFS.
    """
    visitados = set()
    resultado = []
    cola = deque([inicio])
    visitados.add(inicio)
    
    while cola:
        nodo = cola.popleft()
        resultado.append(nodo)
        
        for vecino in grafo.get(nodo, []):
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)
    
    return resultado


def camino_bfs(grafo: Dict, inicio: Any, destino: Any) -> Optional[List]:
    """
    Encuentra el camino más corto (en número de aristas) usando BFS.
    
    Returns:
        Lista de nodos del camino, o None si no existe.
    """
    if inicio == destino:
        return [inicio]
    
    visitados = {inicio: None}  # nodo → predecesor
    cola = deque([inicio])
    
    while cola:
        nodo = cola.popleft()
        for vecino in grafo.get(nodo, []):
            if vecino not in visitados:
                visitados[vecino] = nodo
                if vecino == destino:
                    # Reconstruir camino
                    camino = []
                    actual = destino
                    while actual is not None:
                        camino.append(actual)
                        actual = visitados[actual]
                    return list(reversed(camino))
                cola.append(vecino)
    
    return None


# ==============================================================
# DFS (Búsqueda en Profundidad) - usa Pila (recursión)
# ==============================================================

def dfs_preorden(raiz: NodoArbol) -> List[Any]:
    """
    DFS Pre-orden: raíz → hijos (de izquierda a derecha).
    El primer elemento siempre es la raíz.
    """
    if raiz is None:
        return []
    resultado = [raiz.dato]
    for hijo in raiz.hijos:
        resultado.extend(dfs_preorden(hijo))
    return resultado


def dfs_postorden(raiz: NodoArbol) -> List[Any]:
    """
    DFS Post-orden: hijos → raíz.
    La raíz siempre es el último elemento.
    Útil para: calcular tamaños de subárboles, eliminar árboles.
    """
    if raiz is None:
        return []
    resultado = []
    for hijo in raiz.hijos:
        resultado.extend(dfs_postorden(hijo))
    resultado.append(raiz.dato)
    return resultado


def dfs_iterativo(raiz: NodoArbol) -> List[Any]:
    """
    DFS iterativo usando una PILA explícita (sin recursión).
    Equivalente al DFS recursivo pero usa memoria del heap en vez del call stack.
    """
    if raiz is None:
        return []
    
    resultado = []
    pila = [raiz]  # ← PILA: LIFO
    
    while pila:
        nodo = pila.pop()         # desapilar del tope
        resultado.append(nodo.dato)
        
        # Apilar hijos en reversa para procesar de izquierda a derecha
        for hijo in reversed(nodo.hijos):
            pila.append(hijo)
    
    return resultado


def dfs_grafo(grafo: Dict, inicio: Any) -> List[Any]:
    """DFS sobre grafo con control de visitados."""
    visitados = set()
    resultado = []
    
    def _dfs(nodo):
        visitados.add(nodo)
        resultado.append(nodo)
        for vecino in grafo.get(nodo, []):
            if vecino not in visitados:
                _dfs(vecino)
    
    _dfs(inicio)
    return resultado


def detectar_ciclo_dfs(grafo: Dict) -> bool:
    """
    Detecta si el grafo dirigido tiene ciclos usando DFS con 3 colores.
    
    Blanco (0): no visitado
    Gris (1): en proceso (en la pila de recursión actual)
    Negro (2): completamente procesado
    
    Un ciclo existe si encontramos un vecino GRIS (regresamos a un nodo
    que ya está en la pila de recursión actual).
    """
    BLANCO, GRIS, NEGRO = 0, 1, 2
    color = {v: BLANCO for v in grafo}
    
    def _dfs(v) -> bool:
        color[v] = GRIS
        for vecino in grafo.get(v, []):
            if color[vecino] == GRIS:
                return True   # ¡ciclo encontrado!
            if color[vecino] == BLANCO and _dfs(vecino):
                return True
        color[v] = NEGRO
        return False
    
    return any(_dfs(v) for v in grafo if color[v] == BLANCO)


# ==============================================================
# COMPARATIVA: BFS vs DFS
# ==============================================================

def comparar_bfs_dfs(grafo: Dict, inicio: Any) -> None:
    """Muestra la diferencia de orden entre BFS y DFS."""
    print(f"  BFS desde {inicio}: {bfs_grafo(grafo, inicio)}")
    print(f"  DFS desde {inicio}: {dfs_grafo(grafo, inicio)}")


# ==============================================================
# DEMO
# ==============================================================

if __name__ == "__main__":
    # ---- Construir árbol de prueba ----
    #         A
    #       / | \
    #      B  C  D
    #     /\     \
    #    E  F     G
    
    raiz = NodoArbol('A')
    b, c, d = NodoArbol('B'), NodoArbol('C'), NodoArbol('D')
    e, f, g = NodoArbol('E'), NodoArbol('F'), NodoArbol('G')
    raiz.agregar_hijo(b); raiz.agregar_hijo(c); raiz.agregar_hijo(d)
    b.agregar_hijo(e); b.agregar_hijo(f)
    d.agregar_hijo(g)
    
    print("=" * 50)
    print("ÁRBOL:")
    print("        A")
    print("      / | \\")
    print("     B  C  D")
    print("    /\\     \\")
    print("   E  F     G")
    print()
    
    print(f"BFS (por niveles):    {bfs_arbol(raiz)}")
    print(f"BFS agrupado:         {bfs_por_niveles(raiz)}")
    print(f"DFS pre-orden:        {dfs_preorden(raiz)}")
    print(f"DFS post-orden:       {dfs_postorden(raiz)}")
    print(f"DFS iterativo:        {dfs_iterativo(raiz)}")
    
    # ---- Grafo ----
    grafo = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    print("\n" + "=" * 50)
    print("GRAFO no dirigido:")
    print("  A-B, A-C, B-D, B-E, C-F, E-F")
    print()
    comparar_bfs_dfs(grafo, 'A')
    
    print(f"\n  Camino más corto A→F: {camino_bfs(grafo, 'A', 'F')}")
    print(f"  Camino más corto A→D: {camino_bfs(grafo, 'A', 'D')}")
    
    # ---- Detección de ciclos ----
    print("\n" + "=" * 50)
    print("DETECCIÓN DE CICLOS:")
    
    dag = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
    ciclico = {'A': ['B'], 'B': ['C'], 'C': ['A']}  # A→B→C→A
    
    print(f"  DAG  (A→B,A→C,B→D,C→D):  ¿ciclo? {detectar_ciclo_dfs(dag)}")
    print(f"  Ciclo (A→B→C→A):         ¿ciclo? {detectar_ciclo_dfs(ciclico)}")
    
    # ---- Clave: BFS usa Cola, DFS usa Pila ----
    print("\n" + "=" * 50)
    print("CLAVE CONCEPTUAL:")
    print("  BFS usa COLA  (FIFO) → procesa por niveles")
    print("  DFS usa PILA  (LIFO) → va profundo antes de ampliar")
