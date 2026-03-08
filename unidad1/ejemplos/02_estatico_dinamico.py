# ejemplos/02_estatico_dinamico.py
# Unidad I: Array Estático vs Lista Dinámica + Persistencia
# ==========================================================

import json
import pickle
import os
import time
from typing import Any, Optional


# ==============================================================
# DATO ESTÁTICO: Array de capacidad fija
# ==============================================================

class ArrayEstatico:
    """
    Array de tamaño fijo. Simula el comportamiento de un array
    estático (como en C/Java) usando una lista Python pre-asignada.
    
    El tamaño se define al crearse y NO puede cambiar.
    Acceso por índice en O(1).
    """
    
    def __init__(self, capacidad: int):
        """
        Args:
            capacidad: Número máximo de elementos. Fijo para siempre.
        """
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor a 0")
        self._datos = [None] * capacidad
        self._capacidad = capacidad
        self._tamanio = 0
    
    def agregar(self, dato: Any) -> None:
        """
        Agrega al final. O(1) amortizado.
        
        Raises:
            OverflowError: Si el array ya está lleno.
        """
        if self._tamanio >= self._capacidad:
            raise OverflowError(
                f"Array lleno (capacidad máxima: {self._capacidad})"
            )
        self._datos[self._tamanio] = dato
        self._tamanio += 1
    
    def obtener(self, indice: int) -> Any:
        """Acceso directo por índice. O(1)."""
        if not (0 <= indice < self._tamanio):
            raise IndexError(f"Índice {indice} fuera de rango")
        return self._datos[indice]
    
    def modificar(self, indice: int, dato: Any) -> None:
        """Modifica el valor en la posición dada. O(1)."""
        if not (0 <= indice < self._tamanio):
            raise IndexError(f"Índice {indice} fuera de rango")
        self._datos[indice] = dato
    
    def esta_lleno(self) -> bool:
        return self._tamanio >= self._capacidad
    
    def __len__(self) -> int:
        return self._tamanio
    
    def __str__(self) -> str:
        contenido = [str(self._datos[i]) for i in range(self._tamanio)]
        vacios = ['_'] * (self._capacidad - self._tamanio)
        return f"[{', '.join(contenido + vacios)}]  ({self._tamanio}/{self._capacidad})"


# ==============================================================
# DATO DINÁMICO: Lista enlazada simple
# ==============================================================

class _Nodo:
    """Nodo interno para la lista dinámica."""
    __slots__ = ['dato', 'siguiente']  # optimización de memoria
    
    def __init__(self, dato: Any):
        self.dato = dato
        self.siguiente: Optional['_Nodo'] = None


class ListaDinamica:
    """
    Lista enlazada simple. Crece y se reduce en tiempo de ejecución.
    Sin límite de tamaño (limitada solo por la RAM disponible).
    
    Inserción al inicio: O(1)
    Acceso por índice: O(n)
    """
    
    def __init__(self):
        self._cabeza: Optional[_Nodo] = None
        self._tamanio: int = 0
    
    def agregar_inicio(self, dato: Any) -> None:
        """Inserta al inicio. O(1)."""
        nuevo = _Nodo(dato)
        nuevo.siguiente = self._cabeza
        self._cabeza = nuevo
        self._tamanio += 1
    
    def agregar_final(self, dato: Any) -> None:
        """Inserta al final. O(n)."""
        nuevo = _Nodo(dato)
        if self._cabeza is None:
            self._cabeza = nuevo
        else:
            actual = self._cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._tamanio += 1
    
    def obtener(self, indice: int) -> Any:
        """Acceso por índice. O(n)."""
        if not (0 <= indice < self._tamanio):
            raise IndexError(f"Índice {indice} fuera de rango")
        actual = self._cabeza
        for _ in range(indice):
            actual = actual.siguiente
        return actual.dato
    
    def eliminar_inicio(self) -> Any:
        """Elimina y retorna el primer elemento. O(1)."""
        if self._cabeza is None:
            raise IndexError("Lista vacía")
        dato = self._cabeza.dato
        self._cabeza = self._cabeza.siguiente
        self._tamanio -= 1
        return dato
    
    def a_lista(self) -> list:
        """Convierte a lista Python para serialización."""
        resultado = []
        actual = self._cabeza
        while actual:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado
    
    @classmethod
    def desde_lista(cls, datos: list) -> 'ListaDinamica':
        """Reconstruye la lista desde una lista Python."""
        lista = cls()
        for dato in reversed(datos):
            lista.agregar_inicio(dato)
        return lista
    
    def __len__(self) -> int:
        return self._tamanio
    
    def __str__(self) -> str:
        partes = []
        actual = self._cabeza
        while actual:
            partes.append(str(actual.dato))
            actual = actual.siguiente
        return " → ".join(partes) + " → None"


# ==============================================================
# DATO PERSISTENTE: guardar y cargar con JSON y Pickle
# ==============================================================

def guardar_json(datos: list, archivo: str) -> None:
    """Guarda una lista en formato JSON (texto legible)."""
    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)
    print(f"  ✓ Guardado en '{archivo}'")


def cargar_json(archivo: str) -> list:
    """Carga datos desde un archivo JSON."""
    with open(archivo, 'r', encoding='utf-8') as f:
        return json.load(f)


def guardar_pickle(objeto: Any, archivo: str) -> None:
    """Guarda cualquier objeto Python con Pickle (binario)."""
    with open(archivo, 'wb') as f:
        pickle.dump(objeto, f)
    print(f"  ✓ Guardado en '{archivo}'")


def cargar_pickle(archivo: str) -> Any:
    """Carga un objeto desde un archivo Pickle."""
    with open(archivo, 'rb') as f:
        return pickle.load(f)


# ==============================================================
# DEMO COMPARATIVO
# ==============================================================

def demo_estatico():
    print("=" * 50)
    print("1. DATO ESTÁTICO: Array de capacidad 5")
    print("=" * 50)
    
    arr = ArrayEstatico(capacidad=5)
    for v in [10, 20, 30]:
        arr.agregar(v)
    print(f"   Después de insertar 10,20,30: {arr}")
    
    arr.modificar(1, 99)
    print(f"   Modificar índice 1 a 99:      {arr}")
    print(f"   Acceso índice 0 (O(1)):        {arr.obtener(0)}")
    
    # Intentar llenar
    arr.agregar(40)
    arr.agregar(50)
    print(f"   Array lleno:                   {arr}")
    
    try:
        arr.agregar(60)  # ¡Error!
    except OverflowError as e:
        print(f"   ✓ OverflowError: {e}")


def demo_dinamico():
    print("\n" + "=" * 50)
    print("2. DATO DINÁMICO: Lista enlazada (sin límite)")
    print("=" * 50)
    
    lista = ListaDinamica()
    for v in [10, 20, 30, 40, 50, 60, 70]:  # ¡no hay límite!
        lista.agregar_final(v)
    print(f"   Lista con 7 elementos: {lista}")
    
    eliminado = lista.eliminar_inicio()
    print(f"   Eliminar inicio ({eliminado}):  {lista}")


def demo_persistencia():
    print("\n" + "=" * 50)
    print("3. DATO PERSISTENTE: Guardar y cargar")
    print("=" * 50)
    
    # Crear una lista dinámica
    lista = ListaDinamica()
    for v in ["Bolivia", "Python", "ED1", "Estructuras"]:
        lista.agregar_final(v)
    print(f"   Lista original: {lista}")
    
    # Guardar como JSON
    datos = lista.a_lista()
    guardar_json(datos, "/tmp/lista_ed1.json")
    
    # Guardar como Pickle (el objeto completo)
    guardar_pickle(lista, "/tmp/lista_ed1.pkl")
    
    # Cargar desde JSON
    datos_cargados = cargar_json("/tmp/lista_ed1.json")
    lista_restaurada = ListaDinamica.desde_lista(datos_cargados)
    print(f"   Lista desde JSON:    {lista_restaurada}")
    
    # Cargar desde Pickle
    lista_pickle = cargar_pickle("/tmp/lista_ed1.pkl")
    print(f"   Lista desde Pickle:  {lista_pickle}")
    
    # Comparar tamaños de archivo
    tam_json = os.path.getsize("/tmp/lista_ed1.json")
    tam_pkl = os.path.getsize("/tmp/lista_ed1.pkl")
    print(f"\n   Tamaño JSON:   {tam_json} bytes (texto legible)")
    print(f"   Tamaño Pickle: {tam_pkl} bytes (binario)")


def demo_comparativa_rendimiento():
    print("\n" + "=" * 50)
    print("4. COMPARATIVA: Acceso por índice")
    print("=" * 50)
    
    N = 10_000
    
    # Array estático
    arr = ArrayEstatico(N)
    for i in range(N):
        arr.agregar(i)
    
    inicio = time.perf_counter()
    for _ in range(1000):
        _ = arr.obtener(N - 1)
    t_arr = time.perf_counter() - inicio
    
    # Lista dinámica
    lista = ListaDinamica()
    for i in range(N):
        lista.agregar_final(i)
    
    inicio = time.perf_counter()
    for _ in range(1000):
        _ = lista.obtener(N - 1)
    t_lista = time.perf_counter() - inicio
    
    print(f"   {N:,} elementos, 1000 accesos al último:")
    print(f"   Array estático: {t_arr*1000:.2f} ms  (O(1) por acceso)")
    print(f"   Lista dinámica: {t_lista*1000:.2f} ms  (O(n) por acceso)")
    print(f"   → El array es ~{t_lista/t_arr:.0f}x más rápido para acceso aleatorio")


if __name__ == "__main__":
    demo_estatico()
    demo_dinamico()
    demo_persistencia()
    demo_comparativa_rendimiento()
