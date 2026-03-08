# Ejercicios — Unidad II

## Objetivo
Implementar ADT para polinomios, conjuntos y matrices dispersas.

## Ejercicios

### 1) ADT Polinomio
Implementa la clase `Polinomio` con:
- `agregar_termino(coef, exp)`,
- `evaluar(x)`,
- `sumar(otro)`,
- `restar(otro)`,
- `derivar()`,
- representación legible en texto.

Prueba con al menos 3 polinomios distintos.

### 2) ADT Conjunto
Implementa `ConjuntoADT` con:
- `union`,
- `interseccion`,
- `diferencia`,
- `diferencia_simetrica`,
- `es_subconjunto`.

Incluye al menos dos casos de prueba con datos numéricos y uno con cadenas.

### 3) Matriz dispersa
Implementa `MatrizDispersa(filas, columnas)` usando diccionario de coordenadas.
Debe soportar:
- `establecer(i, j, valor)`,
- `obtener(i, j)`,
- `transponer()`,
- `densidad()`.

Evalúa su eficiencia contra una matriz densa para un caso con pocos no-cero.

### 4) Integración
Resuelve un problema aplicado (por ejemplo, inventario por sucursal y producto) usando:
- conjunto para categorías,
- polinomio para estimación simple,
- matriz dispersa para datos faltantes/cero.

## Desafío
Implementa multiplicación de polinomios y suma de matrices dispersas con validación de dimensiones.

## Criterios de evaluación
- Correctitud de operaciones ADT: 45%
- Diseño y estructura del código: 25%
- Casos de prueba y validaciones: 20%
- Presentación de resultados: 10%
