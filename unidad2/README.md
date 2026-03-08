# Unidad II · ADT Polinomio, Conjuntos y Matriz Dispersa

## 🎯 Objetivo

Diseñar e implementar estructuras de datos para representar eficientemente conjuntos matemáticos complejos: polinomios, conjuntos y matrices dispersas.

---

## 1. ADT Polinomio

### ¿Qué es un polinomio?

Un polinomio es una expresión matemática de la forma:

```
P(x) = aₙxⁿ + aₙ₋₁xⁿ⁻¹ + ... + a₁x + a₀
```

Ejemplo: `3x⁴ - 2x² + 5x - 1`

### Representación computacional

**Opción A: Array de coeficientes (estática)**

El índice i representa el exponente, y `coefs[i]` el coeficiente:

```
3x⁴ - 2x² + 5x - 1

coefs = [-1, 5, -2, 0, 3]
índice:  0   1   2   3  4
         ↑           ↑
         x⁰          x⁴
```

Ventaja: acceso O(1) al término i-ésimo.  
Desventaja: ineficiente para polinomios dispersos (ej: `x¹⁰⁰⁰`).

**Opción B: Lista enlazada de términos (dinámica)**

Solo almacena términos con coeficiente distinto de cero:

```
3x⁴ - 2x² + 5x - 1

[coef=3, exp=4] → [coef=-2, exp=2] → [coef=5, exp=1] → [coef=-1, exp=0] → None
```

Ventaja: eficiente para polinomios dispersos.

### Operaciones del ADT Polinomio

| Operación | Descripción |
|-----------|-------------|
| `evaluar(x)` | Calcular P(x) para un valor de x |
| `sumar(Q)` | Retornar P(x) + Q(x) |
| `restar(Q)` | Retornar P(x) - Q(x) |
| `multiplicar(Q)` | Retornar P(x) × Q(x) |
| `grado()` | Retornar el exponente más alto |
| `derivar()` | Retornar P'(x) |

---

## 2. ADT Conjuntos

### ¿Qué es un conjunto?

Un **conjunto** es una colección de elementos **sin orden** y **sin duplicados**.

```
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
```

### Operaciones del ADT Conjunto

| Operación | Notación | Resultado con A y B |
|-----------|----------|---------------------|
| `union(B)` | A ∪ B | {1,2,3,4,5,6,7} |
| `interseccion(B)` | A ∩ B | {3,4,5} |
| `diferencia(B)` | A - B | {1,2} |
| `diferencia_simetrica(B)` | A △ B | {1,2,6,7} |
| `subconjunto(B)` | A ⊆ B | False |
| `contiene(x)` | x ∈ A | True/False |
| `agregar(x)` | A ∪ {x} | nuevo conjunto |
| `eliminar(x)` | A - {x} | nuevo conjunto |

### Representación

- **Usando `set` de Python**: lo más práctico para la mayoría de casos.
- **Usando BitVector**: muy eficiente para conjuntos de enteros pequeños.
- **Usando Lista ordenada**: permite operaciones de conjunto en O(n).

---

## 3. ADT Matriz Dispersa (Sparse Matrix)

### ¿El problema?

Una **matriz dispersa** tiene la mayoría de sus elementos iguales a cero.

```
Matriz 5×5 con solo 3 valores no-cero:

[ 0  0  5  0  0 ]
[ 0  0  0  0  0 ]
[ 0  8  0  0  0 ]
[ 0  0  0  0  0 ]
[ 0  0  0  3  0 ]

¿Tiene sentido guardar 25 valores si 22 son cero?
```

**Con representación estándar:** guardar 25 valores (ineficiente).  
**Con representación dispersa:** guardar solo los 3 valores no-cero.

### Representaciones de Matriz Dispersa

**Opción A: Lista de tripletas (fila, columna, valor)**

```python
# Solo los no-ceros:
[(0,2,5), (2,1,8), (4,3,3)]
```

**Opción B: Diccionario de coordenadas**

```python
{(0,2): 5, (2,1): 8, (4,3): 3}
```

**Opción C: Lista de listas enlazadas (por filas)**

Cada fila es una lista enlazada de nodos (columna, valor) no-ceros.

### Operaciones del ADT Matriz Dispersa

| Operación | Descripción |
|-----------|-------------|
| `obtener(i, j)` | Retorna el valor en (i,j) |
| `establecer(i, j, valor)` | Establece el valor en (i,j) |
| `sumar(B)` | Suma dos matrices dispersas |
| `transponer()` | Transpone la matriz |
| `multiplicar(B)` | Multiplica dos matrices |
| `densidad()` | % de elementos no-cero |

---

## 📁 Archivos de esta unidad

| Archivo | Descripción |
|---------|-------------|
| [`ejemplos/01_polinomio.py`](./ejemplos/01_polinomio.py) | ADT Polinomio completo |
| [`ejemplos/02_conjuntos.py`](./ejemplos/02_conjuntos.py) | ADT Conjunto con operaciones |
| [`ejemplos/03_matriz_dispersa.py`](./ejemplos/03_matriz_dispersa.py) | Matriz dispersa eficiente |
| [`ejercicios/enunciados.md`](./ejercicios/enunciados.md) | Ejercicios propuestos |
