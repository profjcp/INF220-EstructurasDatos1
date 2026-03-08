# Proyectos · INF-220 Estructuras de Datos I

Los proyectos son instancias de evaluación que integran los contenidos de múltiples unidades. Todos deben implementarse en **Python**, siguiendo las buenas prácticas de la Unidad 0.

---

## 📋 Proyecto 1 · Sistema de Gestión de Turnos

**Unidades integradas:** Unidad 0, Unidad I, Unidad III (Cola, Pila)

### Descripción

Implementar un **sistema de gestión de turnos** para una clínica, banco o cualquier institución con atención al público. El sistema debe:

- Asignar turnos a clientes (cola FIFO)
- Permitir turnos prioritarios (cola de prioridad)
- Mantener historial de atendidos (pila)
- Guardar y cargar el estado (persistencia JSON)

### Especificaciones técnicas

```python
class SistemaGestionTurnos:
    """
    Sistema de turnos con cola normal y cola prioritaria.
    
    La cola prioritaria siempre se atiende antes que la normal.
    """
    
    def __init__(self, nombre_servicio: str):
        ...
    
    def tomar_turno(self, nombre: str, prioritario: bool = False) -> str:
        """
        Asigna un número de turno al cliente.
        Retorna el número asignado (ej: 'T-001' o 'P-001' para prioritario).
        """
        ...
    
    def atender_siguiente(self) -> dict | None:
        """
        Atiende al siguiente cliente (prioritario primero).
        Retorna datos del cliente atendido, o None si no hay turnos.
        """
        ...
    
    def ver_cola(self) -> list:
        """Retorna la lista de turnos pendientes."""
        ...
    
    def historial(self, n: int = 10) -> list:
        """Retorna los últimos n atendidos (desde la pila de historial)."""
        ...
    
    def guardar_estado(self, archivo: str) -> None:
        """Persiste el estado completo en JSON."""
        ...
    
    @classmethod
    def cargar_estado(cls, archivo: str) -> 'SistemaGestionTurnos':
        """Restaura el estado desde JSON."""
        ...
```

### Interfaz de texto esperada

```
=== Sistema de Turnos - Banco XYZ ===
1. Tomar turno normal
2. Tomar turno prioritario
3. Atender siguiente
4. Ver cola actual
5. Ver historial
6. Guardar estado
7. Salir
```

### Criterios de evaluación

| Criterio | Puntos |
|----------|--------|
| Cola funciona correctamente (FIFO) | 20 |
| Prioridad correcta | 15 |
| Historial con pila | 15 |
| Persistencia JSON (guardar/cargar) | 20 |
| Buenas prácticas (docstrings, manejo de errores) | 15 |
| Menú e interfaz de texto | 15 |
| **Total** | **100** |

---

## 📋 Proyecto 2 · Agenda de Contactos con Búsqueda

**Unidades integradas:** Unidad 0, Unidad I, Unidad II (Conjuntos), Unidad III (Lista, Hash), Unidad IV (búsqueda)

### Descripción

Implementar una **agenda de contactos** que use una tabla hash para búsqueda rápida y una lista enlazada para mantener el orden alfabético.

### Especificaciones técnicas

```python
class Contacto:
    """Representa un contacto en la agenda."""
    
    def __init__(self, nombre: str, telefono: str, email: str = "", grupos: set = None):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.grupos = grupos or set()  # ← Conjunto de grupos (Unidad II)
    
    def to_dict(self) -> dict: ...
    
    @classmethod
    def from_dict(cls, datos: dict) -> 'Contacto': ...


class AgendaContactos:
    """
    Agenda de contactos con doble indexación:
    - Tabla hash para búsqueda rápida por nombre O(1)
    - Lista ordenada para recorrido alfabético O(n)
    """
    
    def agregar(self, contacto: Contacto) -> None: ...
    def buscar(self, nombre: str) -> Contacto | None: ...
    def eliminar(self, nombre: str) -> bool: ...
    def buscar_por_grupo(self, grupo: str) -> list: ...
    def listar_alfabetico(self) -> list: ...
    def buscar_prefijo(self, prefijo: str) -> list: ...  # busca por inicio del nombre
    def estadisticas_grupos(self) -> dict: ...  # usa operaciones de conjuntos
    def guardar(self, archivo: str) -> None: ...
    def cargar(self, archivo: str) -> None: ...
```

### Funcionalidades requeridas

- CRUD completo (Crear, Leer, Actualizar, Eliminar)
- Búsqueda por nombre (exacta y por prefijo)
- Filtrar contactos por grupo (amigos, trabajo, familia)
- Operaciones de conjunto entre grupos (¿quién está en 'amigos' AND 'trabajo'?)
- Persistencia en JSON
- Listado alfabético

---

## 📋 Proyecto 3 · Simulador de Proceso de Datos

**Unidades integradas:** Todas las unidades

### Descripción

Implementar un **simulador de pipeline de procesamiento de datos** donde:

- Los datos llegan en un flujo (cola de entrada)
- Se procesan en etapas (cada etapa es una cola)
- Los errores se apilan para revisión posterior
- Los resultados se almacenan en una tabla hash
- Todo el estado persiste en disco

### Diagrama del sistema

```
Datos de entrada
       ↓
[Cola de entrada] → Etapa 1: Validación
                            ↓
                    [Cola validados] → Etapa 2: Transformación
                         ↓ (errores)            ↓
                    [Pila de errores]    [Cola transformados] → Etapa 3: Almacenamiento
                                                                         ↓
                                                                  [Tabla Hash]
                                                                  (resultado final)
```

### Estructura de datos de entrada

Cada elemento es un registro de alumno:
```python
{
    "nombre": "Ana García",
    "ci": "7654321",
    "nota_1": 85,
    "nota_2": 78,
    "nota_3": 91
}
```

### Transformaciones requeridas

- **Validación:** CI válido (7 dígitos), notas entre 0-100, nombre no vacío
- **Transformación:** calcular promedio, determinar estado (aprobado/reprobado)
- **Almacenamiento:** tabla hash indexada por CI

### Entregables

- Código fuente documentado
- Archivo de datos de prueba (mínimo 20 registros simulados)
- Informe de resultados en JSON
- `README.md` explicando cómo ejecutar el proyecto

---

## 📁 Estructura de entrega

Cada proyecto debe entregarse como una carpeta con:

```
proyectoN_apellido_nombre/
├── README.md          ← instrucciones de ejecución
├── main.py            ← punto de entrada principal
├── estructuras/       ← tus implementaciones
│   ├── __init__.py
│   └── *.py
├── datos/             ← archivos de datos de prueba
│   └── *.json
└── tests/             ← pruebas (opcional, puntos extra)
    └── test_*.py
```
