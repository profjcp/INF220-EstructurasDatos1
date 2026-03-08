# Ejercicios — Unidad III

## Objetivo
Implementar y comparar estructuras lineales: listas, pilas, colas, bicolas y tablas hash.

## Ejercicios

### 1) Lista enlazada simple
Implementa `ListaSimple` con:
- insertar al inicio y al final,
- buscar,
- eliminar por valor,
- recorrido/impresión.

Incluye control de lista vacía.

### 2) Pila estática y dinámica
Implementa dos pilas:
- `PilaEstatica` (capacidad fija),
- `PilaDinamica` (nodos enlazados).

Compara comportamiento ante desbordamiento y bajo uso intensivo de `apilar/desapilar`.

### 3) Cola circular
Implementa `ColaCircular` sobre arreglo con índices circulares.
Demuestra que reutiliza espacios liberados al desencolar.

### 4) Bicola
Implementa `Bicola` con operaciones en ambos extremos y muestra cómo simular:
- una pila,
- una cola.

### 5) Tabla hash
Implementa `TablaHash` con encadenamiento.
Incluye:
- insertar,
- buscar,
- eliminar,
- actualización de clave existente.

## Desafío
Construye un mini sistema de turnos:
- cola para atención,
- hash para búsqueda rápida de turno por código,
- persistencia opcional al finalizar.

## Criterios de evaluación
- Implementación de estructuras: 40%
- Complejidad y eficiencia: 25%
- Manejo de casos borde: 20%
- Claridad del código y pruebas: 15%
