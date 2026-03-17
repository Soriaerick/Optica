nano README.md

## Guía Rápida para el Equipo de Desarrollo

Para evitar conflictos en el código y trabajar de forma ordenada en este Sprint, sigan estos pasos todos los días:

### 1. ¿Cómo descargar el proyecto por primera vez? (Solo una vez)
Abre tu terminal en WSL (Ubuntu) y escribe:
`git clone https://github.com/Soriaerick/Optica.git`
`cd Optica`

### 2. ¿Cómo encender el proyecto?
Asegúrate de tener Docker Desktop abierto y ejecuta:
`docker compose up --build`

Paral servidor está levantado correctamente, abre tu navegador web y entra a: http://localhost:8000

### 3. El Ciclo de Trabajo Diario... "¡IMPORTANTE!"
Cada vez que te sientes a programar, sigue este orden exacto:

1. **Actualizar tu código antes de empezar:**
   `git pull origin main`
   *(Esto descarga lo que hicieron los demás mientras no estabas).*

2. **Trabaja en VS Code y guarda tus archivos.**

3. **Empacar tus cambios:**
   `git add .`

4. **Etiquetar lo que hiciste (Ej. "Agregué el carrusel"):**
   `git commit -m "Describe aquí lo que hiciste"`

5. **Subir los cambios a GitHub:**
   `git push origin main`
