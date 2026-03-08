# ejemplos/03_cola_bicola_hash.py
# Unidad III: Cola Circular, Bicola y Tabla Hash
# ================================================

from typing import Any, Optional


# ==============================================================
# COLA CIRCULAR ESTÁTICA
# ==============================================================

class ColaCircularEstatica:
    """
    Cola implementada sobre array circular de capacidad fija.
    Política: FIFO - First In, First Out.
    
    El truco circular: cuando fondo llega al final del array,
    vuelve al índice 0 (si hay espacio libre al inicio).
    
    Esto evita el problema de 'desplazamiento' al desencolar.
    """
    
    def __init__(self, capacidad: int):
        self._datos = [None] * capacidad
        self._capacidad = capacidad
        self._frente = 0     # índice del próximo a desencolar
        self._fondo = 0      # índice donde se insertará el próximo
        self._tamanio = 0
    
    def encolar(self, dato: Any) -> None:
        """O(1). Lanza OverflowError si está llena."""
        if self._tamanio >= self._capacidad:
            raise OverflowError("Cola llena")
        self._datos[self._fondo] = dato
        self._fondo = (self._fondo + 1) % self._capacidad  # ← magia circular
        self._tamanio += 1
    
    def desencolar(self) -> Any:
        """O(1). Lanza IndexError si está vacía."""
        if self._tamanio == 0:
            raise IndexError("Cola vacía")
        dato = self._datos[self._frente]
        self._datos[self._frente] = None
        self._frente = (self._frente + 1) % self._capacidad  # ← magia circular
        self._tamanio -= 1
        return dato
    
    def frente(self) -> Any:
        """Consulta sin quitar. O(1)."""
        if self._tamanio == 0:
            raise IndexError("Cola vacía")
        return self._datos[self._frente]
    
    def esta_vacia(self) -> bool:
        return self._tamanio == 0
    
    def esta_llena(self) -> bool:
        return self._tamanio >= self._capacidad
    
    def __len__(self) -> int:
        return self._tamanio
    
    def __str__(self) -> str:
        if self._tamanio == 0:
            return "Cola(vacía)"
        elementos = []
        idx = self._frente
        for _ in range(self._tamanio):
            elementos.append(str(self._datos[idx]))
            idx = (idx + 1) % self._capacidad
        return f"Cola(frente→ [{', '.join(elementos)}] ←fondo)"


# ==============================================================
# COLA DINÁMICA
# ==============================================================

class ColaDinamica:
    """
    Cola implementada con lista enlazada.
    Mantiene punteros al frente (para desencolar O(1))
    y al fondo (para encolar O(1)).
    """
    
    class _Nodo:
        __slots__ = ['dato', 'siguiente']
        def __init__(self, dato):
            self.dato = dato
            self.siguiente = None
    
    def __init__(self):
        self._frente_nodo = None
        self._fondo_nodo = None
        self._tamanio = 0
    
    def encolar(self, dato: Any) -> None:
        """O(1): agrega al fondo."""
        nuevo = self._Nodo(dato)
        if self._fondo_nodo:
            self._fondo_nodo.siguiente = nuevo
        else:
            self._frente_nodo = nuevo
        self._fondo_nodo = nuevo
        self._tamanio += 1
    
    def desencolar(self) -> Any:
        """O(1): quita del frente."""
        if not self._frente_nodo:
            raise IndexError("Cola vacía")
        dato = self._frente_nodo.dato
        self._frente_nodo = self._frente_nodo.siguiente
        if not self._frente_nodo:
            self._fondo_nodo = None
        self._tamanio -= 1
        return dato
    
    def frente(self) -> Any:
        if not self._frente_nodo:
            raise IndexError("Cola vacía")
        return self._frente_nodo.dato
    
    def esta_vacia(self) -> bool:
        return self._frente_nodo is None
    
    def __len__(self) -> int:
        return self._tamanio
    
    def __str__(self) -> str:
        elementos = []
        actual = self._frente_nodo
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return f"Cola(frente→ [{', '.join(elementos)}] ←fondo)"


# ==============================================================
# BICOLA DINÁMICA (Deque)
# ==============================================================

class BicolaDinamica:
    """
    Bicola (Deque): inserción y eliminación en ambos extremos.
    Implementada con lista doblemente enlazada para O(1) en todos los extremos.
    
    Puede comportarse como:
    - Pila: usar solo insertar_fondo / eliminar_fondo
    - Cola: usar insertar_fondo / eliminar_frente
    """
    
    class _Nodo:
        __slots__ = ['dato', 'siguiente', 'anterior']
        def __init__(self, dato):
            self.dato = dato
            self.siguiente = None
            self.anterior = None
    
    def __init__(self):
        self._frente = None
        self._fondo = None
        self._tamanio = 0
    
    def insertar_frente(self, dato: Any) -> None:
        """Inserta al frente. O(1)."""
        nuevo = self._Nodo(dato)
        if self._frente is None:
            self._frente = self._fondo = nuevo
        else:
            nuevo.siguiente = self._frente
            self._frente.anterior = nuevo
            self._frente = nuevo
        self._tamanio += 1
    
    def insertar_fondo(self, dato: Any) -> None:
        """Inserta al fondo. O(1)."""
        nuevo = self._Nodo(dato)
        if self._fondo is None:
            self._frente = self._fondo = nuevo
        else:
            self._fondo.siguiente = nuevo
            nuevo.anterior = self._fondo
            self._fondo = nuevo
        self._tamanio += 1
    
    def eliminar_frente(self) -> Any:
        """Quita y retorna del frente. O(1)."""
        if self._frente is None:
            raise IndexError("Bicola vacía")
        dato = self._frente.dato
        self._frente = self._frente.siguiente
        if self._frente:
            self._frente.anterior = None
        else:
            self._fondo = None
        self._tamanio -= 1
        return dato
    
    def eliminar_fondo(self) -> Any:
        """Quita y retorna del fondo. O(1)."""
        if self._fondo is None:
            raise IndexError("Bicola vacía")
        dato = self._fondo.dato
        self._fondo = self._fondo.anterior
        if self._fondo:
            self._fondo.siguiente = None
        else:
            self._frente = None
        self._tamanio -= 1
        return dato
    
    def esta_vacia(self) -> bool:
        return self._tamanio == 0
    
    def __len__(self) -> int:
        return self._tamanio
    
    def __str__(self) -> str:
        elementos = []
        actual = self._frente
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return f"Bicola([{' ⟺ '.join(elementos)}])"


# ==============================================================
# TABLA HASH con encadenamiento
# ==============================================================

class TablaHash:
    """
    Tabla hash con resolución de colisiones por encadenamiento.
    Cada celda contiene una lista de pares (clave, valor).
    
    Redimensiona automáticamente cuando el factor de carga > 0.75.
    
    Complejidades:
        Promedio: O(1) para insertar, buscar, eliminar
        Peor caso: O(n) si todas las claves colisionan
    """
    
    CAPACIDAD_INICIAL = 8
    FACTOR_CARGA_MAX = 0.75
    
    def __init__(self):
        self._capacidad = self.CAPACIDAD_INICIAL
        self._tabla = [[] for _ in range(self._capacidad)]
        self._tamanio = 0
    
    def _hash(self, clave) -> int:
        """Función hash: mapea la clave a un índice válido."""
        return hash(clave) % self._capacidad
    
    def insertar(self, clave: Any, valor: Any) -> None:
        """
        Inserta o actualiza el par (clave, valor).
        Si la clave ya existe, actualiza su valor.
        """
        if self._factor_carga() > self.FACTOR_CARGA_MAX:
            self._redimensionar()
        
        idx = self._hash(clave)
        for i, (k, _) in enumerate(self._tabla[idx]):
            if k == clave:
                self._tabla[idx][i] = (clave, valor)  # actualizar
                return
        
        self._tabla[idx].append((clave, valor))   # insertar nuevo
        self._tamanio += 1
    
    def buscar(self, clave: Any) -> Optional[Any]:
        """
        Retorna el valor asociado a la clave, o None si no existe.
        """
        idx = self._hash(clave)
        for k, v in self._tabla[idx]:
            if k == clave:
                return v
        return None
    
    def eliminar(self, clave: Any) -> bool:
        """Elimina la clave. Retorna True si existía."""
        idx = self._hash(clave)
        for i, (k, _) in enumerate(self._tabla[idx]):
            if k == clave:
                self._tabla[idx].pop(i)
                self._tamanio -= 1
                return True
        return False
    
    def contiene(self, clave: Any) -> bool:
        return self.buscar(clave) is not None
    
    def _factor_carga(self) -> float:
        return self._tamanio / self._capacidad
    
    def _redimensionar(self) -> None:
        """Duplica la capacidad y reinserta todos los pares."""
        pares_viejos = [(k, v) for bucket in self._tabla for k, v in bucket]
        self._capacidad *= 2
        self._tabla = [[] for _ in range(self._capacidad)]
        self._tamanio = 0
        for k, v in pares_viejos:
            self.insertar(k, v)
    
    def __len__(self) -> int:
        return self._tamanio
    
    def __str__(self) -> str:
        pares = [(k, v) for bucket in self._tabla for k, v in bucket]
        contenido = ", ".join(f"{k!r}:{v!r}" for k, v in pares)
        return (f"TablaHash({{{contenido}}}, "
                f"cap={self._capacidad}, "
                f"carga={self._factor_carga():.2f})")


# ==============================================================
# DEMO
# ==============================================================

if __name__ == "__main__":
    print("=== COLA CIRCULAR ESTÁTICA ===")
    cola = ColaCircularEstatica(4)
    for v in [10, 20, 30]:
        cola.encolar(v)
    print(f"Encolado 10,20,30: {cola}")
    print(f"Desencolar: {cola.desencolar()} → {cola}")
    cola.encolar(40)
    cola.encolar(50)
    print(f"Encolado 40,50:    {cola}")
    
    print("\n=== COLA DINÁMICA ===")
    cd = ColaDinamica()
    for v in ['A', 'B', 'C', 'D']:
        cd.encolar(v)
    print(f"Cola: {cd}")
    print(f"Desencolar 2 veces: {cd.desencolar()}, {cd.desencolar()}")
    print(f"Cola: {cd}")
    
    print("\n=== BICOLA DINÁMICA ===")
    bic = BicolaDinamica()
    bic.insertar_fondo(2)
    bic.insertar_fondo(3)
    bic.insertar_frente(1)
    bic.insertar_fondo(4)
    print(f"Bicola: {bic}")
    print(f"Eliminar frente: {bic.eliminar_frente()} → {bic}")
    print(f"Eliminar fondo:  {bic.eliminar_fondo()} → {bic}")
    
    print("\n=== TABLA HASH ===")
    th = TablaHash()
    pares = [
        ("Bolivia", "Sucre"),
        ("Argentina", "Buenos Aires"),
        ("Brasil", "Brasilia"),
        ("Perú", "Lima"),
        ("Chile", "Santiago"),
        ("Colombia", "Bogotá"),
        ("Ecuador", "Quito"),
        ("Paraguay", "Asunción"),
    ]
    for k, v in pares:
        th.insertar(k, v)
    
    print(f"Tamaño: {len(th)}")
    print(f"Capital de Bolivia: {th.buscar('Bolivia')}")
    print(f"Capital de Brasil:  {th.buscar('Brasil')}")
    print(f"¿Existe Uruguay?    {th.contiene('Uruguay')}")
    
    th.insertar("Bolivia", "La Paz (sede gobierno)")
    print(f"Bolivia actualizado: {th.buscar('Bolivia')}")
    
    th.eliminar("Chile")
    print(f"Después de eliminar Chile, ¿existe? {th.contiene('Chile')}")
    print(f"\n{th}")
