# Guía de Contribución — INF-220

Gracias por aportar al repositorio del curso **INF-220**.

## 1) Antes de empezar
- Revisa el `README.md` general y el `README.md` de la unidad correspondiente.
- Mantén el estilo de código claro y nombres descriptivos.
- Evita mezclar varios temas en un mismo cambio.

## 2) Flujo recomendado (Git)
```bash
git checkout main
git pull origin main
git checkout -b feature/descripcion-corta
```

Realiza tus cambios y verifica que el código ejecute correctamente.

```bash
git add .
git commit -m "feat: descripción breve del cambio"
git push -u origin feature/descripcion-corta
```

Luego abre un **Pull Request** desde tu rama hacia `main`.

## 3) Convención de commits
Usa mensajes claros. Ejemplos:
- `feat: agrega ejemplo de cola dinámica`
- `fix: corrige inserción en pila estática`
- `docs: mejora explicación de unidad 2`

## 4) Pull Requests
- Describe el objetivo del cambio.
- Indica en qué unidad/carpeta impacta.
- Si aplica, agrega salida de ejecución o captura breve.
- Mantén PRs pequeños y enfocados.

## 5) Issues
Al reportar un problema, incluye:
- archivo o ruta afectada,
- pasos para reproducir,
- comportamiento esperado y actual.

## 6) Alcance del repositorio
Este repositorio es académico; prioriza:
- claridad didáctica,
- consistencia con contenidos de clase,
- ejemplos ejecutables y fáciles de leer.
