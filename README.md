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
