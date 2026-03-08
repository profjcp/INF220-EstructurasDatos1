# ejemplos/02_pila_estatica_dinamica.py
# Unidad III: Pila (Stack) - Variantes Estática y Dinámica
# =========================================================

from typing import Any, Optional
from abc import ABC, abstractmethod


# ==============================================================
# INTERFAZ (ADT Pila)
# ==============================================================

class ADTPila(ABC):
    """
    Interfaz del ADT Pila.
    Política: LIFO - Last In, First Out.
    """
    
    @abstractmethod
    def apilar(self, dato: Any) -> None:
        """Agrega un elemento en el tope."""
        pass
    
    @abstractmethod
    def desapilar(self) -> Any:
        """Quita y retorna el elemento del tope."""
        pass
    
    @abstractmethod
    def tope(self) -> Any:
        """Retorna el tope sin quitar."""
        pass
    
    @abstractmethod
    def esta_vacia(self) -> bool:
        pass
    
    @abstractmethod
    def __len__(self) -> int:
        pass


class PilaVaciaError(Exception):
    """Excepción para operaciones sobre pila vacía."""
    pass


class PilaLlenaError(Exception):
    """Excepción para inserción en pila estática llena."""
    pass


# ==============================================================
# PILA ESTÁTICA (sobre array de capacidad fija)
# ==============================================================

class PilaEstatica(ADTPila):
    """
    Pila implementada sobre un array de tamaño fijo.
    
    El tope siempre es el último elemento insertado (índice tamanio-1).
    
    Complejidades: todas las operaciones son O(1).
    Limitación: capacidad máxima fija.
    """
    
    def __init__(self, capacidad: int):
        """
        Args:
            capacidad: Número máximo de elementos.
        """
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor a 0")
        self._datos = [None] * capacidad
        self._capacidad = capacidad
        self._tope_idx = -1  # -1 significa pila vacía
    
    def apilar(self, dato: Any) -> None:
        """O(1). Lanza PilaLlenaError si está llena."""
        if self._tope_idx >= self._capacidad - 1:
            raise PilaLlenaError(f"Pila llena (cap={self._capacidad})")
        self._tope_idx += 1
        self._datos[self._tope_idx] = dato
    
    def desapilar(self) -> Any:
        """O(1). Lanza PilaVaciaError si está vacía."""
        if self.esta_vacia():
            raise PilaVaciaError("No se puede desapilar: pila vacía")
        dato = self._datos[self._tope_idx]
        self._datos[self._tope_idx] = None  # liberar referencia
        self._tope_idx -= 1
        return dato
    
    def tope(self) -> Any:
        """O(1)."""
        if self.esta_vacia():
            raise PilaVaciaError("Pila vacía")
        return self._datos[self._tope_idx]
    
    def esta_vacia(self) -> bool:
        return self._tope_idx == -1
    
    def esta_llena(self) -> bool:
        return self._tope_idx >= self._capacidad - 1
    
    def __len__(self) -> int:
        return self._tope_idx + 1
    
    def __str__(self) -> str:
        elementos = [str(self._datos[i]) for i in range(self._tope_idx + 1)]
        return f"Pila(tope→ [{' | '.join(reversed(elementos))}] ←base, cap={self._capacidad})"


# ==============================================================
# PILA DINÁMICA (sobre lista enlazada)
# ==============================================================

class PilaDinamica(ADTPila):
    """
    Pila implementada sobre lista enlazada.
    
    El tope = cabeza de la lista. Apilar = insertar al inicio. O(1).
    Sin límite de capacidad.
    """
    
    class _Nodo:
        __slots__ = ['dato', 'siguiente']
        def __init__(self, dato: Any):
            self.dato = dato
            self.siguiente: Optional['PilaDinamica._Nodo'] = None
    
    def __init__(self):
        self._tope_nodo: Optional[PilaDinamica._Nodo] = None
        self._tamanio: int = 0
    
    def apilar(self, dato: Any) -> None:
        """O(1). Sin límite de capacidad."""
        nuevo = self._Nodo(dato)
        nuevo.siguiente = self._tope_nodo
        self._tope_nodo = nuevo
        self._tamanio += 1
    
    def desapilar(self) -> Any:
        """O(1)."""
        if self.esta_vacia():
            raise PilaVaciaError("No se puede desapilar: pila vacía")
        dato = self._tope_nodo.dato
        self._tope_nodo = self._tope_nodo.siguiente
        self._tamanio -= 1
        return dato
    
    def tope(self) -> Any:
        """O(1)."""
        if self.esta_vacia():
            raise PilaVaciaError("Pila vacía")
        return self._tope_nodo.dato
    
    def esta_vacia(self) -> bool:
        return self._tope_nodo is None
    
    def __len__(self) -> int:
        return self._tamanio
    
    def __str__(self) -> str:
        elementos = []
        actual = self._tope_nodo
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return f"Pila(tope→ [{' | '.join(elementos)}] ←base)"


# ==============================================================
# APLICACIONES DE LA PILA
# ==============================================================

def verificar_parentesis(expresion: str) -> bool:
    """
    Verifica que los paréntesis, corchetes y llaves estén balanceados.
    
    Ejemplos válidos:   {[()]}   (a + b) * [c - d]
    Ejemplos inválidos: {[}]     (()
    
    Usa una Pila para recordar los caracteres de apertura.
    """
    pila = PilaDinamica()
    apertura = set('([{')
    cierre = set(')]}')
    pares = {')': '(', ']': '[', '}': '{'}
    
    for char in expresion:
        if char in apertura:
            pila.apilar(char)
        elif char in cierre:
            if pila.esta_vacia():
                return False
            if pila.desapilar() != pares[char]:
                return False
    
    return pila.esta_vacia()


def evaluar_postfija(expresion: str) -> float:
    """
    Evalúa una expresión en notación postfija (Notación Polaca Inversa).
    
    Ejemplo: "3 4 + 2 *" = (3 + 4) * 2 = 14
    Ejemplo: "5 1 2 + 4 * + 3 -" = 14
    
    Algoritmo: recorrer tokens; si número → apilar; si operador → desapilar 2, operar, apilar resultado.
    """
    pila = PilaDinamica()
    operadores = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
    }
    
    for token in expresion.split():
        if token in operadores:
            b = pila.desapilar()
            a = pila.desapilar()
            pila.apilar(operadores[token](a, b))
        else:
            pila.apilar(float(token))
    
    return pila.desapilar()


# ==============================================================
# DEMO
# ==============================================================

if __name__ == "__main__":
    print("=" * 50)
    print("PILA ESTÁTICA (capacidad=4)")
    print("=" * 50)
    pe = PilaEstatica(4)
    for v in [10, 20, 30]:
        pe.apilar(v)
    print(f"Después de apilar 10,20,30: {pe}")
    print(f"Tope: {pe.tope()}")
    print(f"Desapilar: {pe.desapilar()} → {pe}")
    
    try:
        for v in [40, 50, 60]:
            pe.apilar(v)
    except PilaLlenaError as e:
        print(f"✓ Error esperado: {e}")
    
    print("\n" + "=" * 50)
    print("PILA DINÁMICA (sin límite)")
    print("=" * 50)
    pd = PilaDinamica()
    for v in [10, 20, 30, 40, 50, 60]:
        pd.apilar(v)
    print(f"Después de apilar 6 elementos: {pd}")
    print(f"Tamaño: {len(pd)}")
    
    print("\n" + "=" * 50)
    print("APLICACIÓN 1: Verificar paréntesis balanceados")
    print("=" * 50)
    casos = [
        ("{[()]}", True),
        ("(a + b) * [c - d]", True),
        ("{[}]", False),
        ("(()", False),
        ("", True),
    ]
    for expr, esperado in casos:
        resultado = verificar_parentesis(expr)
        estado = "✓" if resultado == esperado else "✗"
        print(f"{estado} '{expr}' → {'Válido' if resultado else 'Inválido'}")
    
    print("\n" + "=" * 50)
    print("APLICACIÓN 2: Notación postfija (RPN)")
    print("=" * 50)
    expresiones = [
        ("3 4 +", 7),
        ("3 4 + 2 *", 14),
        ("5 1 2 + 4 * + 3 -", 14),
        ("2 3 4 * +", 14),
    ]
    for expr, esperado in expresiones:
        resultado = evaluar_postfija(expr)
        estado = "✓" if resultado == esperado else "✗"
        print(f"{estado} '{expr}' = {resultado:.0f}  (esperado: {esperado})")
