nano README.md

# Sistema Óptica - Punto de Venta

Sistema web desarrollado en Django para la gestión de productos, servicios y ventas en una óptica.

---

# Equipo de Desarrollo

* Erick Soria
* Mari
* Fernando Herrera
* Daniel Dominguez
* Aaron

---

# Tecnologías

* Python
* Django
* SQLite
* Docker
* HTML / CSS

---
## Ciclo de Vida del Proyecto (DevOps & Administración)

Para cumplir con los estándares de ingeniería, este proyecto implementa las 8 fases del ciclo de vida DevOps:
1. Planificación (Plan)
   * Metodología: Ágil (Scrum/Kanban).
   * Backlog: Gestionado mediante Sprints (ver Wiki - Sprints).
   * Seguridad: Planificación de roles de usuario y protección de rutas críticas.
2. Codificación (Code)
   * Control de Versiones: Git con flujo de trabajo colaborativo.
   * Commits Atómicos: Cada entrega representa una funcionalidad lógica única.
   * Entorno: Aislamiento mediante entornos virtuales (venv) para evitar conflictos de dependencias.
3. Construcción (Build)
   * Contenedorización: Uso de Docker para garantizar que el artefacto sea idéntico en desarrollo y producción.
   * Gestión de Dependencias: Automatizada vía requirements.txt.
4. Pruebas (Test)
  * Validación Funcional: Pruebas manuales de flujo de caja, stock y agendamiento de citas antes de cada push.
  * Integridad: Verificación de migraciones de base de datos en entornos limpios.
5. Lanzamiento (Release)
  * Versionado: Control de versiones basado en tags de Git (v0.5, v1.0).
  * Changelog: Registro de cambios disponible en la sección de Sprints.
6. Despliegue (Deploy)
  * Infraestructura: Despliegue basado en contenedores mediante docker-compose.
  * Variables de Entorno: Gestión de secretos y configuraciones de Django (SECRET_KEY, DEBUG).
7. Operación (Operate)
  * Persistencia: Gestión de base de datos SQLite con planes de migración a PostgreSQL para escalabilidad.
  * Mantenimiento: Limpieza periódica de archivos estáticos y optimización de imágenes.
8. Monitorización (Monitor)
  * Logs: Seguimiento de peticiones y errores mediante la consola de Django y logs de Docker.
  * Feedback: Análisis de la experiencia de usuario para el reabastecimiento de stock en el catálogo.
---

# Instalación del Proyecto

## 1. Clonar repositorio

```bash
git clone https://github.com/Soriaerick/Optica.git
cd Optica/Op_Mar
```

---

# USO CON DOCKER (RECOMENDADO)

## 2. Levantar el proyecto

```bash
docker compose up --build
```

Abrir en navegador:

```
http://localhost:8000
```

---

## Detener contenedores

```bash
docker compose down
```

---

## Reconstruir contenedores (cuando hay cambios)

```bash
docker compose up --build
```

---

## Aplicar migraciones dentro de Docker

```bash
docker compose exec web python manage.py migrate
```

---

## Crear superusuario

```bash
docker compose exec web python manage.py createsuperuser
```

---

# USO SIN DOCKER (ALTERNATIVO)

## Crear entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

## Migraciones

```bash
python manage.py migrate
```

## Ejecutar servidor

```bash
python manage.py runserver
```

---

# FLUJO DE TRABAJO EN EQUIPO (MUY IMPORTANTE)

## TODOS LOS DÍAS seguir este orden:

### 1. Actualizar proyecto

```bash
git pull origin main
```

---

### 2. Trabajar en el código

* Editar archivos en VS Code
* Guardar cambios

---

### 3. Preparar cambios

```bash
git add .
```

---

### 4. Crear commit

```bash
git commit -m "Descripción clara del cambio"
```

Ejemplo:

```bash
git commit -m "Agregado carrusel en página de inicio"
```

---

### 5. Subir cambios

```bash
git push origin main
```

---

# REGLAS DEL EQUIPO

* ❌ No trabajar sin hacer `git pull`
* ❌ No subir código roto
* ✔ Hacer commits claros
* ✔ Probar antes de subir

---

# ESTRUCTURA DEL PROYECTO

```
Optica/
│
├── Op_Mar/                # Proyecto Django
│   ├── Optica/           # App principal
│   ├── templates/
│   ├── static/
│   ├── db.sqlite3
│   └── manage.py
│
├── docker-compose.yml
├── Dockerfile
└── README.md
```
