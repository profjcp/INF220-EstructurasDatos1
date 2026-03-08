# ejemplos/06_persistencia_estructuras.py
# Unidad III: Guardar y Cargar Estructuras desde Disco
# =====================================================
# Las estructuras de datos en memoria se pierden al cerrar el programa.
# La persistencia permite guardarlas en disco y restaurarlas después.

import json
import pickle
import csv
import os
from typing import Any


# ==============================================================
# PILA PERSISTENTE (con JSON)
# ==============================================================

class PilaPersistente:
    """
    Pila dinámica que puede guardarse y cargarse desde disco (JSON).
    
    El archivo JSON guarda la lista de elementos desde base hasta tope.
    """
    
    def __init__(self):
        self._elementos = []  # lista Python como estructura interna
    
    def apilar(self, dato: Any) -> None:
        self._elementos.append(dato)
    
    def desapilar(self) -> Any:
        if self.esta_vacia():
            raise IndexError("Pila vacía")
        return self._elementos.pop()
    
    def tope(self) -> Any:
        if self.esta_vacia():
            raise IndexError("Pila vacía")
        return self._elementos[-1]
    
    def esta_vacia(self) -> bool:
        return len(self._elementos) == 0
    
    def __len__(self) -> int:
        return len(self._elementos)
    
    # --- Persistencia ---
    
    def guardar(self, archivo: str) -> None:
        """Guarda la pila en un archivo JSON."""
        datos = {
            "tipo": "PilaPersistente",
            "version": 1,
            "elementos": self._elementos
        }
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)
        print(f"  ✓ Pila guardada en '{archivo}' ({len(self)} elementos)")
    
    @classmethod
    def cargar(cls, archivo: str) -> 'PilaPersistente':
        """Carga la pila desde un archivo JSON."""
        with open(archivo, 'r', encoding='utf-8') as f:
            datos = json.load(f)
        
        if datos.get("tipo") != "PilaPersistente":
            raise ValueError("El archivo no contiene una PilaPersistente")
        
        pila = cls()
        pila._elementos = datos["elementos"]
        print(f"  ✓ Pila cargada desde '{archivo}' ({len(pila)} elementos)")
        return pila
    
    def __str__(self) -> str:
        if self.esta_vacia():
            return "Pila(vacía)"
        elementos_str = " | ".join(str(e) for e in reversed(self._elementos))
        return f"Pila(tope→ {elementos_str} ←base)"


# ==============================================================
# COLA PERSISTENTE (con CSV para datos tabulares)
# ==============================================================

class ColaPersistenteCSV:
    """
    Cola dinámica que puede guardarse y cargarse desde CSV.
    Útil cuando los datos son registros tabulares (nombre, edad, etc).
    """
    
    def __init__(self, campos: list):
        """
        Args:
            campos: Lista de nombres de columnas, ej: ['nombre', 'nota']
        """
        self._campos = campos
        self._datos = []  # lista de diccionarios
    
    def encolar(self, **kwargs) -> None:
        """
        Encola un registro.
        
        Ejemplo: cola.encolar(nombre='Ana', nota=85.5)
        """
        registro = {campo: kwargs.get(campo) for campo in self._campos}
        self._datos.append(registro)
    
    def desencolar(self) -> dict:
        if not self._datos:
            raise IndexError("Cola vacía")
        return self._datos.pop(0)
    
    def frente(self) -> dict:
        if not self._datos:
            raise IndexError("Cola vacía")
        return self._datos[0]
    
    def esta_vacia(self) -> bool:
        return len(self._datos) == 0
    
    def __len__(self) -> int:
        return len(self._datos)
    
    # --- Persistencia CSV ---
    
    def guardar_csv(self, archivo: str) -> None:
        """Guarda la cola en un archivo CSV."""
        with open(archivo, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=self._campos)
            writer.writeheader()
            writer.writerows(self._datos)
        print(f"  ✓ Cola guardada en '{archivo}' ({len(self)} registros)")
    
    @classmethod
    def cargar_csv(cls, archivo: str, campos: list) -> 'ColaPersistenteCSV':
        """Carga la cola desde un archivo CSV."""
        cola = cls(campos)
        with open(archivo, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for fila in reader:
                cola._datos.append(dict(fila))
        print(f"  ✓ Cola cargada desde '{archivo}' ({len(cola)} registros)")
        return cola
    
    def __str__(self) -> str:
        if self.esta_vacia():
            return "Cola(vacía)"
        return f"Cola({self._datos})"


# ==============================================================
# TABLA HASH PERSISTENTE (con Pickle para objeto completo)
# ==============================================================

class TablaHashPersistente:
    """
    Tabla hash simple que puede persistir su estado completo con Pickle.
    Pickle serializa el objeto Python entero (incluyendo su tipo).
    """
    
    def __init__(self):
        self._datos = {}
    
    def insertar(self, clave: str, valor: Any) -> None:
        self._datos[clave] = valor
    
    def buscar(self, clave: str) -> Any:
        return self._datos.get(clave)
    
    def eliminar(self, clave: str) -> bool:
        if clave in self._datos:
            del self._datos[clave]
            return True
        return False
    
    def __len__(self) -> int:
        return len(self._datos)
    
    # --- Persistencia Pickle ---
    
    def guardar(self, archivo: str) -> None:
        """Serializa el objeto completo con Pickle."""
        with open(archivo, 'wb') as f:
            pickle.dump(self, f)
        size = os.path.getsize(archivo)
        print(f"  ✓ TablaHash guardada en '{archivo}' ({size} bytes)")
    
    @staticmethod
    def cargar(archivo: str) -> 'TablaHashPersistente':
        """Deserializa desde archivo Pickle."""
        with open(archivo, 'rb') as f:
            obj = pickle.load(f)
        print(f"  ✓ TablaHash cargada desde '{archivo}' ({len(obj)} entradas)")
        return obj
    
    def __str__(self) -> str:
        return f"TablaHash({self._datos})"


# ==============================================================
# DEMO
# ==============================================================

if __name__ == "__main__":
    ARCHIVO_PILA = "/tmp/pila_ed1.json"
    ARCHIVO_COLA = "/tmp/cola_ed1.csv"
    ARCHIVO_HASH = "/tmp/hash_ed1.pkl"
    
    # ---- Pila Persistente ----
    print("=" * 50)
    print("1. PILA PERSISTENTE (JSON)")
    print("=" * 50)
    
    pila = PilaPersistente()
    for v in ["tarea1.py", "tarea2.py", "proyecto_final.py"]:
        pila.apilar(v)
    print(f"Pila original: {pila}")
    pila.guardar(ARCHIVO_PILA)
    
    # Simular cierre y reapertura del programa
    del pila
    pila_restaurada = PilaPersistente.cargar(ARCHIVO_PILA)
    print(f"Pila restaurada: {pila_restaurada}")
    print(f"Desapilar: {pila_restaurada.desapilar()}")
    
    # ---- Cola Persistente ----
    print("\n" + "=" * 50)
    print("2. COLA PERSISTENTE (CSV)")
    print("=" * 50)
    
    cola = ColaPersistenteCSV(['nombre', 'ci', 'nota'])
    cola.encolar(nombre='Ana García', ci='7654321', nota='88.5')
    cola.encolar(nombre='Luis Mamani', ci='8123456', nota='75.0')
    cola.encolar(nombre='María López', ci='9234567', nota='92.0')
    cola.guardar_csv(ARCHIVO_COLA)
    
    # Mostrar el CSV generado
    print("\n  Contenido del archivo CSV:")
    with open(ARCHIVO_COLA, 'r') as f:
        print("  " + f.read().replace('\n', '\n  '))
    
    cola_restaurada = ColaPersistenteCSV.cargar_csv(ARCHIVO_COLA, ['nombre','ci','nota'])
    primer_alumno = cola_restaurada.desencolar()
    print(f"  Primer alumno en la cola: {primer_alumno}")
    
    # ---- Tabla Hash Persistente ----
    print("\n" + "=" * 50)
    print("3. TABLA HASH PERSISTENTE (Pickle)")
    print("=" * 50)
    
    th = TablaHashPersistente()
    th.insertar("admin", {"pass": "1234", "rol": "administrador"})
    th.insertar("profe", {"pass": "abcd", "rol": "docente"})
    th.insertar("alumno1", {"pass": "pass1", "rol": "estudiante"})
    th.guardar(ARCHIVO_HASH)
    
    th_restaurada = TablaHashPersistente.cargar(ARCHIVO_HASH)
    usuario = th_restaurada.buscar("profe")
    print(f"  Usuario 'profe': {usuario}")
