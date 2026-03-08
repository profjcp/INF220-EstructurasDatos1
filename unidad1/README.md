# Unidad I · Modelos de Representación de Datos

## 🎯 Objetivo

Comprender las distintas formas en que los datos pueden ser representados y organizados en la memoria, como fundamento para elegir la estructura adecuada para cada problema.

---

## 1. ¿Qué es un Dato?

Un **dato** es cualquier valor que puede almacenarse y procesarse por un programa. La forma en que un dato se representa afecta directamente la **eficiencia** del programa.

```
Problema: administrar una lista de 1000 alumnos
¿Cómo los represento en memoria?

Opción A: Lista de Python → simple pero menos eficiente
Opción B: Array estático → rápido pero tamaño fijo
Opción C: Lista enlazada → flexible pero más lenta en acceso
Opción D: Archivo en disco → persiste pero lento
```

---

## 2. Datos Abstractos (ADT)

Un **Tipo de Dato Abstracto (ADT)** es la descripción de un tipo de dato desde el punto de vista del **usuario**: qué operaciones se pueden hacer, **sin importar cómo** están implementadas internamente.

```
ADT Pila (Stack)
════════════════
Operaciones:
  apilar(dato)  → agrega un elemento arriba
  desapilar()   → quita y retorna el elemento de arriba
  tope()        → retorna el elemento de arriba sin quitarlo
  esta_vacia()  → True si no hay elementos

El usuario NO sabe si la pila usa un array o nodos enlazados.
Eso es abstracción.
```

### Ventajas del ADT

- **Encapsulamiento**: el usuario solo ve la interfaz, no la implementación.
- **Mantenibilidad**: puedes cambiar la implementación sin cambiar el código cliente.
- **Reusabilidad**: el mismo ADT puede usarse en distintos programas.

```python
# En Python, ADT = clase abstracta con ABC
from abc import ABC, abstractmethod

class ADTPila(ABC):
    @abstractmethod
    def apilar(self, dato): pass
    
    @abstractmethod
    def desapilar(self): pass
    
    @abstractmethod
    def tope(self): pass
    
    @abstractmethod
    def esta_vacia(self) -> bool: pass
```

---

## 3. Datos Estáticos

Los **datos estáticos** tienen un **tamaño fijo** definido en tiempo de compilación (o al crearse). No pueden crecer ni reducirse en ejecución.

### Características

| Característica | Valor |
|---------------|-------|
| Tamaño | Fijo, definido al crear |
| Acceso | O(1) por índice |
| Inserción | O(n) si requiere desplazar elementos |
| Memoria | Bloque contiguo |

### En Python: arrays con tamaño fijo

```python
# Simulación de array estático en Python
class ArrayEstatico:
    def __init__(self, capacidad: int):
        self._datos = [None] * capacidad   # bloque fijo de memoria
        self._capacidad = capacidad
        self._tamanio = 0
    
    def agregar(self, dato):
        if self._tamanio >= self._capacidad:
            raise OverflowError("Array lleno")
        self._datos[self._tamanio] = dato
        self._tamanio += 1
    
    def obtener(self, indice):
        if indice < 0 or indice >= self._tamanio:
            raise IndexError("Índice fuera de rango")
        return self._datos[indice]  # O(1) acceso directo
```

**Cuándo usar:** cuando el tamaño es conocido y fijo, y se necesita acceso rápido por índice.

---

## 4. Datos Dinámicos

Los **datos dinámicos** crecen y se reducen en tiempo de ejecución según las necesidades. Usan **nodos enlazados** en memoria heap.

### Características

| Característica | Valor |
|---------------|-------|
| Tamaño | Variable, crece/reduce en ejecución |
| Acceso | O(n) (requiere recorrer enlaces) |
| Inserción al inicio | O(1) |
| Memoria | Nodos dispersos en heap |

### Representación con nodos

```
Nodo A    Nodo B    Nodo C
┌──────┐  ┌──────┐  ┌──────┐
│ dato │→ │ dato │→ │ dato │→ None
│  10  │  │  20  │  │  30  │
└──────┘  └──────┘  └──────┘
```

```python
class Nodo:
    def __init__(self, dato):
        self.dato = dato        # el valor
        self.siguiente = None   # enlace al siguiente nodo
```

**Cuándo usar:** cuando el tamaño no se conoce de antemano y hay muchas inserciones/eliminaciones.

---

## 5. Datos Simulados

Los **datos simulados** son datos que imitan o modelan situaciones del mundo real dentro de un programa. Se usan para **testing**, **simulaciones** y **prototipado**.

### Técnicas de simulación en Python

```python
import random
from datetime import datetime, timedelta

# Generador de datos simulados para pruebas
def generar_alumno_random():
    nombres = ["Ana", "Luis", "María", "Carlos", "Sofia"]
    apellidos = ["García", "Perez", "López", "Mamani", "Quispe"]
    return {
        "nombre": random.choice(nombres),
        "apellido": random.choice(apellidos),
        "ci": random.randint(5_000_000, 9_999_999),
        "nota": round(random.uniform(0, 100), 1),
        "fecha_nac": datetime.now() - timedelta(days=random.randint(6570, 9125))
    }

# Generar 10 alumnos simulados
alumnos = [generar_alumno_random() for _ in range(10)]
```

### Datos simulados con Faker (librería)

```python
# pip install faker
from faker import Faker
fake = Faker('es_ES')

alumno = {
    "nombre": fake.name(),
    "email": fake.email(),
    "telefono": fake.phone_number()
}
```

**Cuándo usar:** en pruebas unitarias, para demostrar el funcionamiento de una estructura sin datos reales.

---

## 6. Datos Persistentes

Los **datos persistentes** sobreviven al cierre del programa. Se almacenan en disco (archivos, bases de datos) y se cargan de vuelta cuando el programa inicia.

### 6.1 Persistencia con archivos de texto (CSV)

```python
import csv

# Guardar lista en CSV
def guardar_csv(lista, archivo):
    with open(archivo, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['valor'])     # encabezado
        for item in lista:
            writer.writerow([item])

# Cargar desde CSV
def cargar_csv(archivo):
    datos = []
    with open(archivo, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for fila in reader:
            datos.append(fila['valor'])
    return datos
```

### 6.2 Persistencia con JSON

```python
import json

# Guardar
def guardar_json(datos, archivo):
    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)

# Cargar
def cargar_json(archivo):
    with open(archivo, 'r', encoding='utf-8') as f:
        return json.load(f)
```

### 6.3 Persistencia con Pickle (objetos Python)

```python
import pickle

# Guardar un objeto Python completo
def guardar_estructura(estructura, archivo):
    with open(archivo, 'wb') as f:
        pickle.dump(estructura, f)

# Cargar
def cargar_estructura(archivo):
    with open(archivo, 'rb') as f:
        return pickle.load(f)
```

### Comparación de formatos

| Formato | Legible por humanos | Interoperable | Velocidad | Objetos Python |
|---------|-------------------|---------------|-----------|---------------|
| CSV | ✅ Sí | ✅ Sí | Medio | ❌ No |
| JSON | ✅ Sí | ✅ Sí | Medio | Parcial |
| Pickle | ❌ No | ❌ No | ✅ Rápido | ✅ Sí |

---

## 7. Resumen comparativo

| Tipo | Tamaño | Acceso | Persiste | Ejemplo |
|------|--------|--------|----------|---------|
| **Estático** | Fijo | O(1) | No | Array, Pila sobre array |
| **Dinámico** | Variable | O(n) | No | Lista enlazada, Árbol |
| **Simulado** | Variable | Según impl. | No | Datos de prueba random |
| **Persistente** | Variable | Lento | ✅ Sí | CSV, JSON, BD |

---

## 📁 Archivos de esta unidad

| Archivo | Descripción |
|---------|-------------|
| [`ejemplos/01_adt_concepto.py`](./ejemplos/01_adt_concepto.py) | ADT: abstracción vs implementación |
| [`ejemplos/02_estatico_dinamico.py`](./ejemplos/02_estatico_dinamico.py) | Array estático vs estructura dinámica |
| [`ejemplos/03_persistencia.py`](./ejemplos/03_persistencia.py) | Guardar y cargar estructuras con JSON y Pickle |
| [`ejercicios/enunciados.md`](./ejercicios/enunciados.md) | Ejercicios propuestos |
