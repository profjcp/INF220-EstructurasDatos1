# Unidad III · Estructuras Lineales: Listas, Pilas, Colas y Bicolas

## 🎯 Objetivo

Implementar y dominar las estructuras de datos lineales fundamentales en sus tres variantes: estática (array), dinámica (nodos enlazados) y persistente (disco).

---

## 1. Listas Enlazadas

Una **lista enlazada** es una secuencia de nodos donde cada nodo contiene un dato y un enlace al siguiente.

### 1.1 Lista Simple

```
cabeza
  ↓
[10] → [20] → [30] → None
```

Operaciones principales:
- `insertar_inicio(dato)` → O(1)
- `insertar_final(dato)` → O(n)
- `insertar_en(indice, dato)` → O(n)
- `eliminar_inicio()` → O(1)
- `eliminar(dato)` → O(n)
- `buscar(dato)` → O(n)

### 1.2 Lista Doble

Cada nodo tiene enlace al **siguiente** y al **anterior**:

```
None ← [10] ⟺ [20] ⟺ [30] → None
        ↑                      ↑
      cabeza                  cola
```

Ventaja: eliminación del último es O(1) (en lista simple es O(n)).

### 1.3 Lista Circular

El último nodo apunta de regreso al primero:

```
   ┌─────────────────┐
   ↓                 |
 [10] → [20] → [30] ─┘
```

Uso: planificadores de procesos (round-robin), listas de reproducción.

---

## 2. Pila (Stack)

Una **pila** sigue la política **LIFO** (Last In, First Out): el último en entrar es el primero en salir.

```
   TOPE
    ↓
  [30]   ← última en entrar, primera en salir
  [20]
  [10]   ← primera en entrar
```

| Operación | Descripción | Complejidad |
|-----------|-------------|-------------|
| `apilar(dato)` | Agrega en el tope | O(1) |
| `desapilar()` | Quita y retorna el tope | O(1) |
| `tope()` | Consulta el tope sin quitar | O(1) |
| `esta_vacia()` | Verifica si está vacía | O(1) |

### Aplicaciones de la Pila

- **Deshacer/Rehacer** en editores de texto (Ctrl+Z)
- **Llamadas a funciones**: la pila de llamadas del sistema
- **Evaluación de expresiones**: `2 + 3 * 4` con notación postfija
- **Verificar paréntesis balanceados**: `{[()]}` → válido

### Pila estática vs dinámica

```
ESTÁTICA (array)          DINÁMICA (lista enlazada)
┌───────────────┐         cabeza
│  30  ← tope  │           ↓
│  20           │         [30] → [20] → [10] → None
│  10           │         (el inicio de la lista ES el tope)
│  ___          │
│  ___          │
└───────────────┘
Tamaño: fijo              Tamaño: ilimitado
```

---

## 3. Cola (Queue)

Una **cola** sigue la política **FIFO** (First In, First Out): el primero en entrar es el primero en salir.

```
FRENTE                           FONDO
  ↓                                ↓
[10] ← [20] ← [30] ← [40] ← [50]
  ↑                                ↑
sale por aquí              entra por aquí
```

| Operación | Descripción | Complejidad |
|-----------|-------------|-------------|
| `encolar(dato)` | Agrega al fondo | O(1) |
| `desencolar()` | Quita y retorna el frente | O(1) |
| `frente()` | Consulta el frente sin quitar | O(1) |
| `esta_vacia()` | Verifica si está vacía | O(1) |

### Cola Circular (sobre array)

Soluciona el problema de "desperdiciar" espacio al desencolar:

```
Array de tamaño 5:

Inicial: [_, _, _, _, _]  frente=0, fondo=0
Encolar 10,20,30: [10,20,30,_, _]  frente=0, fondo=3
Desencolar → 10:  [__, 20, 30, _, _]  frente=1
Encolar 40,50:    [__, 20, 30, 40, 50]  fondo=0 (vuelve al inicio!)
Encolar 60:       [60, 20, 30, 40, 50]  fondo=1 (circular!)
```

### Aplicaciones de la Cola

- **Impresoras**: trabajos de impresión en orden de llegada
- **BFS** (búsqueda en anchura en grafos)
- **Buffers** de teclado, redes, streaming
- **Planificación de procesos** del sistema operativo

---

## 4. Bicola (Deque - Double-Ended Queue)

Una **bicola** permite insertar y eliminar en **ambos extremos**.

```
FRENTE                      FONDO
  ↓                           ↓
[10] ⟺ [20] ⟺ [30] ⟺ [40]
  ↑                           ↑
insertar/eliminar       insertar/eliminar
```

| Operación | Descripción |
|-----------|-------------|
| `insertar_frente(dato)` | Agrega al frente |
| `insertar_fondo(dato)` | Agrega al fondo |
| `eliminar_frente()` | Quita del frente |
| `eliminar_fondo()` | Quita del fondo |

La bicola es una **generalización**: una pila y una cola son casos especiales de bicola.

---

## 5. Tabla Hash (Hash Table)

Una **tabla hash** mapea claves a valores usando una **función hash** para calcular el índice de almacenamiento.

```
clave: "Bolivia"
hash("Bolivia") % 10 = 3

tabla:
  0: []
  1: []
  2: []
  3: [("Bolivia", "Sucre")]   ← aquí se guarda
  4: []
  ...
```

### Resolución de colisiones

**Encadenamiento (chaining):** cada celda tiene una lista de pares (clave, valor).

```python
tabla[hash(clave) % capacidad].append((clave, valor))
```

**Dirección abierta (open addressing):** si hay colisión, busca la siguiente celda libre.

| Operación | Caso promedio | Peor caso |
|-----------|--------------|-----------|
| `insertar` | O(1) | O(n) |
| `buscar` | O(1) | O(n) |
| `eliminar` | O(1) | O(n) |

---

## 📁 Archivos de esta unidad

| Archivo | Descripción |
|---------|-------------|
| [`ejemplos/01_lista_simple.py`](./ejemplos/01_lista_simple.py) | Lista simple y doble con todas las operaciones |
| [`ejemplos/02_pila_estatica_dinamica.py`](./ejemplos/02_pila_estatica_dinamica.py) | Pila estática y dinámica |
| [`ejemplos/03_cola_circular.py`](./ejemplos/03_cola_circular.py) | Cola estática circular y dinámica |
| [`ejemplos/04_bicola.py`](./ejemplos/04_bicola.py) | Bicola dinámica |
| [`ejemplos/05_tabla_hash.py`](./ejemplos/05_tabla_hash.py) | Tabla hash con encadenamiento |
| [`ejemplos/06_persistencia_estructuras.py`](./ejemplos/06_persistencia_estructuras.py) | Guardar y cargar estructuras desde disco |
| [`ejercicios/enunciados.md`](./ejercicios/enunciados.md) | Ejercicios propuestos |
