# Ejercicios — Unidad I

## Objetivo
Comprender y aplicar los modelos de representación de datos: abstracto, estático, dinámico y persistente.

## Ejercicios

### 1) ADT de Pila
Diseña una interfaz abstracta `ADTPila` y crea dos implementaciones:
- `PilaArray`
- `PilaLista`

Muestra que el código cliente funciona sin cambiar cuando intercambias implementación.

### 2) Estático vs dinámico
Implementa:
- `ArrayEstatico(capacidad)` con control de desbordamiento,
- `ListaDinamica` enlazada con inserción al inicio y al final.

Compara complejidades de:
- inserción,
- acceso por índice,
- eliminación.

### 3) Simulación de datos
Genera 50 registros simulados de estudiantes (nombre, nota, grupo).
Carga los datos en ambas estructuras y reporta:
- tiempo de inserción,
- facilidad de búsqueda,
- memoria aproximada.

### 4) Persistencia
Guarda y recupera la estructura de estudiantes en:
- JSON,
- Pickle.

Explica en un párrafo cuándo usar cada formato.

## Desafío
Implementa una capa de repositorio (`RepositorioEstudiantes`) con métodos:
- `guardar`, `cargar`, `agregar`, `listar`.

La implementación debe permitir cambiar de JSON a Pickle sin cambiar el código cliente.

## Criterios de evaluación
- Diseño ADT y encapsulamiento: 30%
- Implementación correcta de estructuras: 35%
- Persistencia y pruebas: 25%
- Claridad de análisis comparativo: 10%
