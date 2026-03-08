# ejemplos/01_polinomio_conjuntos_matriz.py
# Unidad II: ADT Polinomio, Conjuntos y Matriz Dispersa
# ======================================================

from typing import Any, Dict, List, Optional, Tuple


# ==============================================================
# ADT POLINOMIO (representación con lista de términos)
# ==============================================================

class Termino:
    """Un término de un polinomio: coeficiente * x^exponente."""
    
    def __init__(self, coeficiente: float, exponente: int):
        if exponente < 0:
            raise ValueError("El exponente debe ser >= 0")
        self.coeficiente = coeficiente
        self.exponente = exponente
    
    def __repr__(self):
        return f"Termino({self.coeficiente}, {self.exponente})"


class Polinomio:
    """
    ADT Polinomio usando lista de términos no-cero ordenados por exponente.
    
    Ejemplo: 3x⁴ - 2x² + 5x - 1 se representa como:
        [(3,4), (-2,2), (5,1), (-1,0)]
    
    Operaciones: evaluar, sumar, restar, multiplicar, derivar.
    """
    
    def __init__(self):
        """Crea el polinomio cero: P(x) = 0"""
        self._terminos: List[Termino] = []  # ordenados por exponente desc
    
    @classmethod
    def desde_coeficientes(cls, coefs: list) -> 'Polinomio':
        """
        Crea un polinomio desde lista de coeficientes.
        coefs[i] es el coeficiente de x^i.
        
        Ejemplo: [−1, 5, −2, 0, 3] → 3x⁴ - 2x² + 5x - 1
        """
        p = cls()
        for exp, coef in enumerate(coefs):
            if coef != 0:
                p._terminos.append(Termino(coef, exp))
        p._terminos.sort(key=lambda t: t.exponente, reverse=True)
        return p
    
    def agregar_termino(self, coef: float, exp: int) -> None:
        """Agrega o acumula un término al polinomio."""
        for t in self._terminos:
            if t.exponente == exp:
                t.coeficiente += coef
                if t.coeficiente == 0:
                    self._terminos.remove(t)
                return
        if coef != 0:
            self._terminos.append(Termino(coef, exp))
            self._terminos.sort(key=lambda t: t.exponente, reverse=True)
    
    def grado(self) -> int:
        """Retorna el mayor exponente del polinomio."""
        if not self._terminos:
            return 0
        return self._terminos[0].exponente
    
    def evaluar(self, x: float) -> float:
        """
        Calcula P(x) usando el Método de Horner. O(n).
        
        Ejemplo: 3x² + 2x + 1 evaluado en x=2:
            Horner: ((3)*2 + 2)*2 + 1 = 17
        """
        if not self._terminos:
            return 0.0
        
        resultado = 0.0
        for termino in self._terminos:
            resultado += termino.coeficiente * (x ** termino.exponente)
        return resultado
    
    def sumar(self, otro: 'Polinomio') -> 'Polinomio':
        """Retorna P(x) + Q(x)."""
        resultado = Polinomio()
        for t in self._terminos:
            resultado.agregar_termino(t.coeficiente, t.exponente)
        for t in otro._terminos:
            resultado.agregar_termino(t.coeficiente, t.exponente)
        return resultado
    
    def restar(self, otro: 'Polinomio') -> 'Polinomio':
        """Retorna P(x) - Q(x)."""
        resultado = Polinomio()
        for t in self._terminos:
            resultado.agregar_termino(t.coeficiente, t.exponente)
        for t in otro._terminos:
            resultado.agregar_termino(-t.coeficiente, t.exponente)
        return resultado
    
    def multiplicar(self, otro: 'Polinomio') -> 'Polinomio':
        """Retorna P(x) × Q(x). O(n×m)."""
        resultado = Polinomio()
        for t1 in self._terminos:
            for t2 in otro._terminos:
                resultado.agregar_termino(
                    t1.coeficiente * t2.coeficiente,
                    t1.exponente + t2.exponente
                )
        return resultado
    
    def derivar(self) -> 'Polinomio':
        """Retorna P'(x) (derivada). Regla: d/dx(ax^n) = n*a*x^(n-1)."""
        resultado = Polinomio()
        for t in self._terminos:
            if t.exponente > 0:
                resultado.agregar_termino(t.coeficiente * t.exponente, t.exponente - 1)
        return resultado
    
    def __str__(self) -> str:
        if not self._terminos:
            return "0"
        partes = []
        for t in self._terminos:
            c = t.coeficiente
            e = t.exponente
            if e == 0:
                partes.append(f"{c:+g}")
            elif e == 1:
                partes.append(f"{c:+g}x")
            else:
                partes.append(f"{c:+g}x^{e}")
        return " ".join(partes).lstrip('+').strip()


# ==============================================================
# ADT CONJUNTO
# ==============================================================

class Conjunto:
    """
    ADT Conjunto: colección sin orden ni duplicados.
    Implementado sobre set de Python, exponiendo operaciones matemáticas.
    """
    
    def __init__(self, elementos=None):
        self._datos = set(elementos) if elementos else set()
    
    def agregar(self, elemento: Any) -> None:
        """Agrega un elemento (si no existe, no hace nada)."""
        self._datos.add(elemento)
    
    def eliminar(self, elemento: Any) -> bool:
        """Elimina un elemento. Retorna False si no existía."""
        if elemento in self._datos:
            self._datos.discard(elemento)
            return True
        return False
    
    def contiene(self, elemento: Any) -> bool:
        """Retorna True si el elemento pertenece al conjunto."""
        return elemento in self._datos
    
    def union(self, otro: 'Conjunto') -> 'Conjunto':
        """A ∪ B: todos los elementos de A o B."""
        return Conjunto(self._datos | otro._datos)
    
    def interseccion(self, otro: 'Conjunto') -> 'Conjunto':
        """A ∩ B: solo los elementos en A y en B."""
        return Conjunto(self._datos & otro._datos)
    
    def diferencia(self, otro: 'Conjunto') -> 'Conjunto':
        """A - B: elementos de A que NO están en B."""
        return Conjunto(self._datos - otro._datos)
    
    def diferencia_simetrica(self, otro: 'Conjunto') -> 'Conjunto':
        """A △ B: elementos en A o B pero no en ambos."""
        return Conjunto(self._datos ^ otro._datos)
    
    def es_subconjunto(self, otro: 'Conjunto') -> bool:
        """A ⊆ B: True si todos los elementos de A están en B."""
        return self._datos <= otro._datos
    
    def esta_vacio(self) -> bool:
        return len(self._datos) == 0
    
    def __len__(self) -> int:
        return len(self._datos)
    
    def __str__(self) -> str:
        return "{" + ", ".join(str(e) for e in sorted(self._datos, key=str)) + "}"


# ==============================================================
# ADT MATRIZ DISPERSA (con diccionario de coordenadas)
# ==============================================================

class MatrizDispersa:
    """
    Matriz dispersa: solo almacena los valores NO-cero.
    Eficiente cuando la mayoría de elementos son cero.
    
    Representación interna: diccionario {(fila,col): valor}
    
    Para una matriz 1000×1000 con 100 valores no-cero:
        Matriz estándar: 1,000,000 celdas
        Matriz dispersa: 100 entradas en diccionario
    """
    
    def __init__(self, filas: int, columnas: int):
        """
        Args:
            filas: Número de filas.
            columnas: Número de columnas.
        """
        if filas <= 0 or columnas <= 0:
            raise ValueError("Dimensiones deben ser positivas")
        self._filas = filas
        self._columnas = columnas
        self._datos: Dict[Tuple[int,int], float] = {}
    
    def _validar(self, i: int, j: int) -> None:
        if not (0 <= i < self._filas and 0 <= j < self._columnas):
            raise IndexError(f"Posición ({i},{j}) fuera de rango {self._filas}×{self._columnas}")
    
    def obtener(self, i: int, j: int) -> float:
        """Retorna el valor en (i,j). Retorna 0 si no está almacenado."""
        self._validar(i, j)
        return self._datos.get((i, j), 0.0)
    
    def establecer(self, i: int, j: int, valor: float) -> None:
        """
        Establece el valor en (i,j).
        Si valor==0, elimina la entrada para ahorrar memoria.
        """
        self._validar(i, j)
        if valor == 0:
            self._datos.pop((i, j), None)
        else:
            self._datos[(i, j)] = valor
    
    def sumar(self, otra: 'MatrizDispersa') -> 'MatrizDispersa':
        """Suma dos matrices dispersas. O(no-ceros de ambas)."""
        if self._filas != otra._filas or self._columnas != otra._columnas:
            raise ValueError("Las matrices deben tener las mismas dimensiones")
        resultado = MatrizDispersa(self._filas, self._columnas)
        for (i, j), v in self._datos.items():
            resultado.establecer(i, j, v)
        for (i, j), v in otra._datos.items():
            resultado.establecer(i, j, resultado.obtener(i, j) + v)
        return resultado
    
    def transponer(self) -> 'MatrizDispersa':
        """Retorna la matriz transpuesta."""
        resultado = MatrizDispersa(self._columnas, self._filas)
        for (i, j), v in self._datos.items():
            resultado.establecer(j, i, v)
        return resultado
    
    def densidad(self) -> float:
        """Porcentaje de elementos no-cero."""
        total = self._filas * self._columnas
        return (len(self._datos) / total) * 100
    
    def no_ceros(self) -> int:
        """Cantidad de elementos no-cero."""
        return len(self._datos)
    
    def imprimir(self) -> None:
        """Imprime la matriz completa (solo para matrices pequeñas)."""
        for i in range(self._filas):
            fila = []
            for j in range(self._columnas):
                fila.append(f"{self.obtener(i,j):5.0f}")
            print(" ".join(fila))
    
    def __str__(self) -> str:
        return (f"MatrizDispersa({self._filas}×{self._columnas}, "
                f"{self.no_ceros()} no-ceros, "
                f"densidad={self.densidad():.1f}%)")


# ==============================================================
# DEMO
# ==============================================================

if __name__ == "__main__":
    # ---- Polinomio ----
    print("=" * 50)
    print("ADT POLINOMIO")
    print("=" * 50)
    
    # P(x) = 3x⁴ - 2x² + 5x - 1
    P = Polinomio.desde_coeficientes([-1, 5, -2, 0, 3])
    # Q(x) = x² + 2x + 4
    Q = Polinomio.desde_coeficientes([4, 2, 1])
    
    print(f"P(x) = {P}")
    print(f"Q(x) = {Q}")
    print(f"P(2) = {P.evaluar(2)}")
    print(f"P+Q  = {P.sumar(Q)}")
    print(f"P-Q  = {P.restar(Q)}")
    print(f"P×Q  = {P.multiplicar(Q)}")
    print(f"P'   = {P.derivar()}")
    
    # ---- Conjuntos ----
    print("\n" + "=" * 50)
    print("ADT CONJUNTOS")
    print("=" * 50)
    
    A = Conjunto([1, 2, 3, 4, 5])
    B = Conjunto([3, 4, 5, 6, 7])
    
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"A ∪ B = {A.union(B)}")
    print(f"A ∩ B = {A.interseccion(B)}")
    print(f"A - B = {A.diferencia(B)}")
    print(f"A △ B = {A.diferencia_simetrica(B)}")
    print(f"A ⊆ B = {A.es_subconjunto(B)}")
    
    C = Conjunto([3, 4])
    print(f"\nC = {C}")
    print(f"C ⊆ A = {C.es_subconjunto(A)}")
    
    # ---- Matriz Dispersa ----
    print("\n" + "=" * 50)
    print("ADT MATRIZ DISPERSA")
    print("=" * 50)
    
    m = MatrizDispersa(5, 5)
    m.establecer(0, 2, 5)
    m.establecer(2, 1, 8)
    m.establecer(4, 3, 3)
    
    print(f"\nMatriz 5×5 (solo 3 valores no-cero):")
    m.imprimir()
    print(f"\n{m}")
    
    print(f"\nValor en (0,2): {m.obtener(0,2)}")
    print(f"Valor en (0,0): {m.obtener(0,0)}  ← cero, no almacenado")
    
    # Comparación de memoria
    print(f"\n--- Eficiencia de memoria ---")
    gran = MatrizDispersa(1000, 1000)
    for i in range(0, 1000, 100):
        for j in range(0, 1000, 100):
            gran.establecer(i, j, i * j + 1)
    
    print(f"Matriz 1000×1000:")
    print(f"  Almacenamiento estándar: {1000*1000:,} valores")
    print(f"  Almacenamiento disperso: {gran.no_ceros():,} valores")
    print(f"  Densidad: {gran.densidad():.2f}%")
    print(f"  Ahorro: {(1 - gran.no_ceros()/(1000*1000))*100:.1f}%")
