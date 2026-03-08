# ejemplos/01_pep8_y_docstrings.py
# Unidad 0: PEP 8, Docstrings y Buenas Prácticas
# ================================================
# Este archivo muestra cómo escribir código Python profesional.

from typing import Any, Optional


# ==============================================================
# ANTES vs DESPUÉS: comparación de estilo
# ==============================================================

# ❌ MAL: código ilegible, sin docstrings, nombres pobres
class n:
    def __init__(self, x):
        self.x = x
        self.n = None
    def i(self, v):
        t = n(v)
        t.n = self.x
        self.x = t


# ✅ BIEN: código limpio, con docstrings y nombres descriptivos
class Nodo:
    """
    Nodo genérico para estructuras de datos enlazadas.
    
    Atributos:
        dato: El valor almacenado en este nodo.
        siguiente: Referencia al siguiente nodo en la cadena.
    """
    
    def __init__(self, dato: Any):
        """Crea un nodo con el dato dado y sin enlace siguiente."""
        self.dato = dato
        self.siguiente: Optional['Nodo'] = None
    
    def __repr__(self) -> str:
        """Representación para debugging."""
        return f"Nodo({self.dato!r})"
    
    def __str__(self) -> str:
        """Representación legible para el usuario."""
        return str(self.dato)


# ==============================================================
# EXCEPCIONES PERSONALIZADAS
# ==============================================================

class EstructuraVaciaError(Exception):
    """Excepción para operaciones sobre estructuras vacías."""
    pass


class DesbordamientoError(Exception):
    """Excepción para inserción en estructuras con capacidad fija."""
    pass


# ==============================================================
# CLASE CON BUENAS PRÁCTICAS COMPLETAS
# ==============================================================

class ListaEnlazadaSimple:
    """
    Lista enlazada simple con buenas prácticas aplicadas.
    
    Cada nodo apunta al siguiente. El último nodo apunta a None.
    
    Complejidades:
        insertar al inicio: O(1)
        insertar al final:  O(n)
        buscar:             O(n)
        eliminar:           O(n)
    
    Ejemplo de uso:
        >>> lista = ListaEnlazadaSimple()
        >>> lista.insertar_inicio(10)
        >>> lista.insertar_inicio(20)
        >>> print(lista)
        20 → 10 → None
    """
    
    def __init__(self):
        """Inicializa la lista vacía."""
        self._cabeza: Optional[Nodo] = None
        self._tamanio: int = 0
    
    # ----------------------------------------------------------
    # Propiedades
    # ----------------------------------------------------------
    
    def esta_vacia(self) -> bool:
        """Retorna True si la lista no tiene elementos."""
        return self._cabeza is None
    
    def __len__(self) -> int:
        """Retorna la cantidad de elementos."""
        return self._tamanio
    
    def __bool__(self) -> bool:
        """Permite usar la lista en expresiones booleanas."""
        return not self.esta_vacia()
    
    # ----------------------------------------------------------
    # Inserción
    # ----------------------------------------------------------
    
    def insertar_inicio(self, dato: Any) -> None:
        """
        Inserta un elemento al inicio de la lista. O(1).
        
        Args:
            dato: El valor a insertar.
        """
        nuevo = Nodo(dato)
        nuevo.siguiente = self._cabeza
        self._cabeza = nuevo
        self._tamanio += 1
    
    def insertar_final(self, dato: Any) -> None:
        """
        Inserta un elemento al final de la lista. O(n).
        
        Args:
            dato: El valor a insertar.
        """
        nuevo = Nodo(dato)
        
        if self.esta_vacia():
            self._cabeza = nuevo
        else:
            actual = self._cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        
        self._tamanio += 1
    
    # ----------------------------------------------------------
    # Búsqueda
    # ----------------------------------------------------------
    
    def buscar(self, dato: Any) -> bool:
        """
        Busca un elemento en la lista. O(n).
        
        Args:
            dato: El valor a buscar.
        
        Returns:
            True si el elemento existe, False en caso contrario.
        """
        actual = self._cabeza
        while actual is not None:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False
    
    def obtener(self, indice: int) -> Any:
        """
        Retorna el elemento en la posición dada. O(n).
        
        Args:
            indice: Posición (0-based).
        
        Returns:
            El dato en esa posición.
        
        Raises:
            IndexError: Si el índice está fuera de rango.
        """
        if indice < 0 or indice >= self._tamanio:
            raise IndexError(f"Índice {indice} fuera de rango [0, {self._tamanio - 1}]")
        
        actual = self._cabeza
        for _ in range(indice):
            actual = actual.siguiente
        return actual.dato
    
    # ----------------------------------------------------------
    # Eliminación
    # ----------------------------------------------------------
    
    def eliminar_inicio(self) -> Any:
        """
        Elimina y retorna el primer elemento. O(1).
        
        Returns:
            El dato eliminado.
        
        Raises:
            EstructuraVaciaError: Si la lista está vacía.
        """
        if self.esta_vacia():
            raise EstructuraVaciaError("No se puede eliminar: lista vacía")
        
        dato = self._cabeza.dato
        self._cabeza = self._cabeza.siguiente
        self._tamanio -= 1
        return dato
    
    def eliminar(self, dato: Any) -> bool:
        """
        Elimina la primera ocurrencia del dato. O(n).
        
        Returns:
            True si eliminó, False si no encontró el dato.
        """
        if self.esta_vacia():
            return False
        
        # Caso especial: eliminar la cabeza
        if self._cabeza.dato == dato:
            self._cabeza = self._cabeza.siguiente
            self._tamanio -= 1
            return True
        
        # Buscar el nodo anterior al que se quiere eliminar
        anterior = self._cabeza
        actual = self._cabeza.siguiente
        while actual is not None:
            if actual.dato == dato:
                anterior.siguiente = actual.siguiente
                self._tamanio -= 1
                return True
            anterior = actual
            actual = actual.siguiente
        
        return False
    
    # ----------------------------------------------------------
    # Visualización
    # ----------------------------------------------------------
    
    def __str__(self) -> str:
        """Representación visual de la lista."""
        elementos = []
        actual = self._cabeza
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " → ".join(elementos) + " → None"
    
    def __repr__(self) -> str:
        return f"ListaEnlazadaSimple({list(self)})"
    
    def __iter__(self):
        """Permite iterar la lista con for."""
        actual = self._cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente


# ==============================================================
# DEMO
# ==============================================================

def main():
    print("=== Demo: Buenas Prácticas en Python ===\n")
    
    lista = ListaEnlazadaSimple()
    
    # Insertar elementos
    for valor in [30, 20, 10]:
        lista.insertar_inicio(valor)
    lista.insertar_final(40)
    lista.insertar_final(50)
    
    print(f"Lista: {lista}")
    print(f"Tamaño: {len(lista)}")
    print(f"¿Vacía? {lista.esta_vacia()}")
    
    # Acceso por índice
    print(f"\nElemento en índice 0: {lista.obtener(0)}")
    print(f"Elemento en índice 2: {lista.obtener(2)}")
    
    # Manejo de errores
    try:
        lista.obtener(99)
    except IndexError as e:
        print(f"\n✓ Error capturado correctamente: {e}")
    
    # Búsqueda
    print(f"\n¿Existe 20? {lista.buscar(20)}")
    print(f"¿Existe 99? {lista.buscar(99)}")
    
    # Iteración (gracias a __iter__)
    print(f"\nIterando la lista: ", end="")
    for dato in lista:
        print(dato, end=" ")
    print()
    
    # Eliminación
    lista.eliminar(20)
    print(f"\nDespués de eliminar 20: {lista}")
    
    primero = lista.eliminar_inicio()
    print(f"Después de eliminar inicio ({primero}): {lista}")


if __name__ == "__main__":
    main()
