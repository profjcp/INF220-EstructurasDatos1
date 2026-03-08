# Unidad 0 · Estándares y Buenas Prácticas de Codificación

## 🎯 Objetivo

Aplicar estándares y buenas prácticas de codificación en Python para escribir código limpio, mantenible y profesional desde el primer día del curso.

---

## 1. Estructuras de Codificación

### 1.1 Convenciones de nombres (PEP 8)

Python tiene una guía de estilo oficial llamada **PEP 8**. Seguirla hace que tu código sea legible para cualquier programador Python.

| Elemento | Convención | ✅ Correcto | ❌ Incorrecto |
|----------|-----------|------------|--------------|
| Variables | `snake_case` | `mi_lista` | `MiLista`, `miLista` |
| Funciones | `snake_case` | `calcular_suma()` | `CalcularSuma()` |
| Clases | `PascalCase` | `ListaEnlazada` | `lista_enlazada` |
| Constantes | `UPPER_SNAKE` | `MAX_SIZE = 100` | `maxSize = 100` |
| Privados | prefijo `_` | `_cabeza` | `cabeza` |
| Muy privados | prefijo `__` | `__nodo` | — |

### 1.2 Reglas de formato

```python
# ✅ BIEN: espacios alrededor de operadores
resultado = a + b
lista[i] = valor

# ✅ BIEN: líneas no superan 79 caracteres
# ✅ BIEN: 4 espacios para indentar (nunca tabs)
def mi_funcion():
    if condicion:
        hacer_algo()

# ✅ BIEN: dos líneas en blanco entre clases y funciones de nivel superior
class ClaseA:
    pass


class ClaseB:
    pass
```

### 1.3 Docstrings

Todo módulo, clase y función pública debe tener un docstring:

```python
def insertar(self, dato: any) -> None:
    """
    Inserta un elemento al inicio de la lista.
    
    Args:
        dato: El valor a insertar. Puede ser de cualquier tipo.
    
    Raises:
        MemoryError: Si no hay memoria disponible.
    
    Ejemplo:
        >>> lista = ListaEnlazada()
        >>> lista.insertar(10)
        >>> lista.insertar(20)
    """
    nuevo_nodo = self._Nodo(dato)
    nuevo_nodo.siguiente = self._cabeza
    self._cabeza = nuevo_nodo
```

### 1.4 Type Hints (tipado estático)

```python
from typing import Optional, List, Any

class Pila:
    def apilar(self, dato: Any) -> None: ...
    def desapilar(self) -> Any: ...
    def tope(self) -> Optional[Any]: ...
    def esta_vacia(self) -> bool: ...
    def __len__(self) -> int: ...
```

---

## 2. Manejo de Interfaces (Clases Abstractas)

En Python usamos el módulo `abc` para simular interfaces:

```python
from abc import ABC, abstractmethod
from typing import Any

class EstructuraLineal(ABC):
    """
    Interfaz base para todas las estructuras lineales del curso:
    Lista, Pila, Cola, Bicola.
    """
    
    @abstractmethod
    def insertar(self, dato: Any) -> None:
        """Inserta un elemento en la estructura."""
        pass
    
    @abstractmethod
    def eliminar(self) -> Any:
        """Elimina y retorna el elemento según política de la estructura."""
        pass
    
    @abstractmethod
    def esta_vacia(self) -> bool:
        """Retorna True si la estructura no tiene elementos."""
        pass
    
    @abstractmethod
    def __len__(self) -> int:
        """Retorna la cantidad de elementos."""
        pass
    
    def __bool__(self) -> bool:
        """Permite usar la estructura en condiciones if."""
        return not self.esta_vacia()
```

---

## 3. Arquitectura de un Proyecto

Una buena organización de archivos para este curso:

```
mi_proyecto/
├── README.md
├── estructuras/
│   ├── __init__.py
│   ├── nodo.py           ← Clase Nodo base
│   ├── lista.py          ← ListaEnlazada
│   ├── pila.py           ← Pila
│   └── cola.py           ← Cola
├── utils/
│   ├── __init__.py
│   └── visualizacion.py  ← Funciones para imprimir estructuras
├── tests/
│   └── test_lista.py     ← Pruebas
└── main.py
```

### Manejo de errores

```python
# Define excepciones propias cuando sea necesario
class EstructuraVaciaError(Exception):
    """Se lanza al intentar eliminar de una estructura vacía."""
    pass

class DesbordamientoError(Exception):
    """Se lanza al intentar insertar en una estructura llena (estática)."""
    pass

# Uso:
def desapilar(self):
    if self.esta_vacia():
        raise EstructuraVaciaError("No se puede desapilar: la pila está vacía")
    ...
```

### El patrón `if __name__ == "__main__"`

```python
# Siempre en el módulo principal
def main():
    lista = ListaEnlazada()
    lista.insertar(10)
    print(lista)

if __name__ == "__main__":
    main()
```

---

## ✅ Checklist antes de entregar código

- [ ] ¿Cada clase y función tiene docstring?
- [ ] ¿Los nombres son descriptivos (no `x`, `n`, `temp`)?
- [ ] ¿Se manejan los casos borde (estructura vacía, índice inválido)?
- [ ] ¿Se usan excepciones en lugar de `print("Error...")`?
- [ ] ¿Las líneas tienen menos de 79 caracteres?
- [ ] ¿Se usa `if __name__ == "__main__"`?
- [ ] ¿El código tiene type hints en los métodos públicos?

---

## 📁 Archivos de esta unidad

| Archivo | Descripción |
|---------|-------------|
| [`ejemplos/01_pep8_y_docstrings.py`](./ejemplos/01_pep8_y_docstrings.py) | Convenciones PEP8 aplicadas |
| [`ejemplos/02_interfaces_abc.py`](./ejemplos/02_interfaces_abc.py) | Interfaces con ABC |
| [`ejercicios/enunciados.md`](./ejercicios/enunciados.md) | Ejercicios de la unidad |
