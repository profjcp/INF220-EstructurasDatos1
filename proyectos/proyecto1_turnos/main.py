# proyecto1/main.py
# Proyecto 1: Sistema de Gestión de Turnos
# =========================================
# ARCHIVO INICIAL (starter code) - completa los métodos marcados con TODO

import json
from collections import deque
from datetime import datetime
from typing import Optional


class Turno:
    """Representa un turno en el sistema."""
    
    def __init__(self, numero: str, nombre: str, prioritario: bool):
        self.numero = numero
        self.nombre = nombre
        self.prioritario = prioritario
        self.hora = datetime.now().strftime("%H:%M:%S")
    
    def to_dict(self) -> dict:
        return {
            "numero": self.numero,
            "nombre": self.nombre,
            "prioritario": self.prioritario,
            "hora": self.hora
        }
    
    @classmethod
    def from_dict(cls, d: dict) -> 'Turno':
        t = cls(d["numero"], d["nombre"], d["prioritario"])
        t.hora = d["hora"]
        return t
    
    def __str__(self):
        tipo = "⚡PRIORITARIO" if self.prioritario else "normal"
        return f"[{self.numero}] {self.nombre} ({tipo}) - {self.hora}"


class SistemaGestionTurnos:
    """
    Sistema de turnos con cola normal, cola prioritaria e historial.
    
    Los turnos prioritarios siempre se atienden antes que los normales.
    """
    
    def __init__(self, nombre_servicio: str):
        self.nombre_servicio = nombre_servicio
        self._cola_normal = deque()
        self._cola_prioritaria = deque()
        self._historial = []         # actúa como pila (append/pop)
        self._contador_normal = 0
        self._contador_prioritario = 0
    
    def tomar_turno(self, nombre: str, prioritario: bool = False) -> str:
        """
        Asigna turno. Retorna número asignado.
        
        TODO: implementar la lógica completa
        - Normal: "N-001", "N-002", ...
        - Prioritario: "P-001", "P-002", ...
        """
        if prioritario:
            self._contador_prioritario += 1
            numero = f"P-{self._contador_prioritario:03d}"
            turno = Turno(numero, nombre, prioritario=True)
            self._cola_prioritaria.append(turno)
        else:
            self._contador_normal += 1
            numero = f"N-{self._contador_normal:03d}"
            turno = Turno(numero, nombre, prioritario=False)
            self._cola_normal.append(turno)
        
        return numero
    
    def atender_siguiente(self) -> Optional[dict]:
        """
        Atiende al siguiente cliente (prioritarios primero).
        
        TODO: completar para actualizar el historial
        """
        turno = None
        if self._cola_prioritaria:
            turno = self._cola_prioritaria.popleft()
        elif self._cola_normal:
            turno = self._cola_normal.popleft()
        
        if turno:
            turno_dict = turno.to_dict()
            turno_dict["hora_atencion"] = datetime.now().strftime("%H:%M:%S")
            self._historial.append(turno_dict)  # push al historial
            return turno_dict
        return None
    
    def ver_cola(self) -> list:
        """Retorna todos los turnos pendientes (prioritarios primero)."""
        resultado = []
        for t in self._cola_prioritaria:
            resultado.append(str(t))
        for t in self._cola_normal:
            resultado.append(str(t))
        return resultado
    
    def historial(self, n: int = 10) -> list:
        """
        Retorna los últimos n atendidos (los más recientes primero).
        El historial actúa como pila: el último atendido es el primero.
        
        TODO: implementar retornando los últimos n elementos
        """
        return list(reversed(self._historial[-n:]))
    
    def turnos_pendientes(self) -> int:
        return len(self._cola_prioritaria) + len(self._cola_normal)
    
    def guardar_estado(self, archivo: str) -> None:
        """
        Persiste el estado completo en JSON.
        
        TODO: guardar cola_normal, cola_prioritaria, historial, contadores
        """
        estado = {
            "nombre_servicio": self.nombre_servicio,
            "contador_normal": self._contador_normal,
            "contador_prioritario": self._contador_prioritario,
            "cola_normal": [t.to_dict() for t in self._cola_normal],
            "cola_prioritaria": [t.to_dict() for t in self._cola_prioritaria],
            "historial": self._historial,
            "guardado_en": datetime.now().isoformat()
        }
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(estado, f, indent=2, ensure_ascii=False)
        print(f"  Estado guardado en '{archivo}'")
    
    @classmethod
    def cargar_estado(cls, archivo: str) -> 'SistemaGestionTurnos':
        """
        Restaura el estado desde JSON.
        
        TODO: cargar todos los campos guardados
        """
        with open(archivo, 'r', encoding='utf-8') as f:
            estado = json.load(f)
        
        sistema = cls(estado["nombre_servicio"])
        sistema._contador_normal = estado["contador_normal"]
        sistema._contador_prioritario = estado["contador_prioritario"]
        sistema._cola_normal = deque(Turno.from_dict(t) for t in estado["cola_normal"])
        sistema._cola_prioritaria = deque(Turno.from_dict(t) for t in estado["cola_prioritaria"])
        sistema._historial = estado["historial"]
        print(f"  Estado cargado desde '{archivo}'")
        return sistema


def menu_principal(sistema: SistemaGestionTurnos) -> None:
    """Menú interactivo por consola."""
    
    while True:
        print(f"\n{'='*45}")
        print(f"  {sistema.nombre_servicio}")
        print(f"  Turnos pendientes: {sistema.turnos_pendientes()}")
        print(f"{'='*45}")
        print("  1. Tomar turno normal")
        print("  2. Tomar turno prioritario")
        print("  3. Atender siguiente")
        print("  4. Ver cola actual")
        print("  5. Ver historial")
        print("  6. Guardar estado")
        print("  7. Salir")
        print(f"{'='*45}")
        
        opcion = input("  Opción: ").strip()
        
        if opcion == "1":
            nombre = input("  Nombre del cliente: ").strip()
            if nombre:
                num = sistema.tomar_turno(nombre, prioritario=False)
                print(f"  ✓ Turno asignado: {num}")
        
        elif opcion == "2":
            nombre = input("  Nombre del cliente: ").strip()
            if nombre:
                num = sistema.tomar_turno(nombre, prioritario=True)
                print(f"  ✓ Turno prioritario asignado: {num}")
        
        elif opcion == "3":
            atendido = sistema.atender_siguiente()
            if atendido:
                print(f"  ✓ Atendiendo: [{atendido['numero']}] {atendido['nombre']}")
            else:
                print("  No hay turnos pendientes.")
        
        elif opcion == "4":
            cola = sistema.ver_cola()
            if cola:
                print("  Cola actual:")
                for t in cola:
                    print(f"    {t}")
            else:
                print("  Cola vacía.")
        
        elif opcion == "5":
            hist = sistema.historial(5)
            if hist:
                print("  Últimos 5 atendidos:")
                for t in hist:
                    print(f"    [{t['numero']}] {t['nombre']} - {t.get('hora_atencion','')}")
            else:
                print("  Historial vacío.")
        
        elif opcion == "6":
            sistema.guardar_estado("/tmp/turnos_estado.json")
        
        elif opcion == "7":
            print("  ¡Hasta luego!")
            break
        
        else:
            print("  Opción no válida.")


def demo_automatica():
    """Demo sin interacción del usuario."""
    print("=== DEMO AUTOMÁTICA - Sistema de Turnos ===\n")
    
    sistema = SistemaGestionTurnos("Banco del Estado - Sucursal Norte")
    
    # Clientes tomando turnos
    turnos = [
        ("Ana García", False),
        ("Luis Mamani", False),
        ("Dr. Peña (médico)", True),   # prioritario
        ("María López", False),
        ("Adulto mayor", True),        # prioritario
    ]
    
    print("Asignando turnos:")
    for nombre, prior in turnos:
        num = sistema.tomar_turno(nombre, prioritario=prior)
        print(f"  → {num}: {nombre}")
    
    print(f"\nCola actual ({sistema.turnos_pendientes()} pendientes):")
    for t in sistema.ver_cola():
        print(f"  {t}")
    
    print("\nAtendiendo en orden:")
    while sistema.turnos_pendientes() > 0:
        atendido = sistema.atender_siguiente()
        print(f"  ✓ Atendido: [{atendido['numero']}] {atendido['nombre']}")
    
    print("\nHistorial completo:")
    for t in sistema.historial():
        print(f"  [{t['numero']}] {t['nombre']}")
    
    # Guardar y recargar
    sistema.guardar_estado("/tmp/turnos_demo.json")
    sistema2 = SistemaGestionTurnos.cargar_estado("/tmp/turnos_demo.json")
    print(f"\n✓ Estado restaurado. Servicio: {sistema2.nombre_servicio}")


if __name__ == "__main__":
    import sys
    if "--demo" in sys.argv:
        demo_automatica()
    else:
        sistema = SistemaGestionTurnos("Mi Servicio")
        menu_principal(sistema)
