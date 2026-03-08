# Ejercicios — Unidad 0

## Objetivo
Aplicar buenas prácticas de codificación (PEP 8, docstrings, type hints y clases abstractas).

## Ejercicios

### 1) Refactor de estilo
Dado un archivo con funciones y variables mal nombradas, refactoriza para cumplir PEP 8:
- variables y funciones en `snake_case`,
- clases en `PascalCase`,
- líneas de hasta 79 caracteres,
- separación correcta de bloques.

### 2) Docstrings completos
Implementa una clase `Pila` con métodos públicos:
- `apilar`, `desapilar`, `tope`, `esta_vacia`, `__len__`.

Cada método debe incluir docstring con:
- descripción,
- argumentos,
- retorno,
- excepciones (si aplica),
- ejemplo de uso.

### 3) Type hints y validaciones
Agrega type hints a un módulo que contenga funciones para operar una lista enlazada.
Incluye validación de índices y excepciones claras.

### 4) Interfaz con ABC
Define una interfaz abstracta `EstructuraLineal` con:
- `insertar`, `eliminar`, `esta_vacia`, `__len__`.

Implementa dos clases concretas (`Pila` y `Cola`) y demuestra polimorfismo con una función que consuma la interfaz.

## Desafío
Configura una lista de verificación automática (script propio) que revise:
- docstrings faltantes,
- nombres no válidos,
- funciones públicas sin type hints.

## Criterios de evaluación
- Corrección funcional: 40%
- Estilo y legibilidad: 30%
- Documentación (docstrings): 20%
- Manejo de errores: 10%
