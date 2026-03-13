# Plan de Gestión del Proyecto (PMP) - Sistema Web para Óptica
**Basado en el Estándar IEEE 16326 para la Gestión de Proyectos de Software**

---

## 1. Alcance del Proyecto (Project Overview)
**Propósito:** Desarrollar una plataforma web funcional y responsiva para una Óptica. El sistema permitirá a 
los clientes visualizar un catálogo de productos,conocer la ubicación de la sucursal, los horarios de atención
y agendar citas para servicios de reparación.

**Alcance Actual:** El proyecto abarca el desarrollo del Frontend (vistas principales: Inicio, Productos, Reparación, Ubicación)
y la configuración de la infraestructura backend inicial mediante contenedores para asegurar la estandarización del entorno de desarrollo.

---

## 2. Organización del Proyecto (Project Organization)
El equipo de trabajo opera bajo el marco de trabajo ágil **Scrum**, distribuyendo las responsabilidades de la siguiente manera:

* **Scrum Master:** Erick Soria
  * *Responsabilidades:* Facilitar las ceremonias Scrum, administrar el tablero Kanban en GitHub Projects, remover impedimentos técnicos y vigilar el cumplimiento de la metodología y del presente plan.
* **Product Owner:** María
  * *Responsabilidades:* Definir la visión del producto, diseñar la interfaz de usuario (UI/UX) y asegurar que las características entregadas aporten valor al negocio.
* **Development Team (Equipo de Desarrollo):** Daniel, Fernando y Aaron
  * *Responsabilidades:* Programación de vistas, integración de componentes, conexión con la base de datos (Django) y despliegue local en contenedores Docker.

---

## 3. Procesos Técnicos y Entorno (Technical Processes)
Para garantizar la calidad y homogeneidad del código, el equipo utilizará las siguientes herramientas estandarizadas:

* **Control de Versiones:** Git y GitHub. Estrategia de integración continua mediante repositorios centralizados y comandos `push/pull`.
* **Entorno de Desarrollo Subyacente:** Windows Subsystem for Linux (WSL2) y Visual Studio Code.
* **Infraestructura y Despliegue:** Contenedores de Docker (mediante `docker compose`) para asegurar que el proyecto se ejecute de manera idéntica en los equipos de todos los desarrolladores.

---

## 4. Control del Trabajo y Cronograma (Work Control / Schedule)
El control del progreso se llevará a cabo mediante iteraciones cortas y supervisión constante:

* **Metodología de Control:** Desarrollo Ágil (Scrum).
* **Gestión de Tareas:** Tablero Kanban implementado en *GitHub Projects* con estados: `Todo` (Por hacer), `In Progress` (En curso) y `Done` (Terminado).
* **Ciclos de Trabajo (Sprints):** Iteraciones predefinidas. 
  * *Sprint 1:* Del 17 al 26 de febrero (Enfoque: Vistas base y Setup del entorno).
* **Ceremonias de Control (Daily Scrum):** Reuniones de sincronización los días **martes, miércoles y jueves**. 
  * *Regla de control:* Duración máxima de 15 minutos respondiendo exclusivamente a: ¿Qué hice ayer?, ¿Qué haré hoy?, ¿Qué me bloquea?

---

## 5. Gestión de Riesgos (Risk Management)
Identificación de obstáculos y planes de mitigación activa:

* **Riesgo 1: Desincronización del código fuente y conflictos (Merge Conflicts).**
  * *Mitigación:* Obligación técnica de ejecutar el comando `git pull origin main` al inicio de cada jornada de programación y subir cambios mediante `commits` descriptivos.
* **Riesgo 2: Retrasos por problemas de compatibilidad de software en diferentes laptops.**
  * *Mitigación:* Implementación estricta de Docker. Ningún desarrollo se probará fuera del contenedor oficial del proyecto.
* **Riesgo 3: Falta de comunicación / Reuniones excesivamente largas.**
  * *Mitigación:* Intervención del Scrum Master usando un cronómetro para los Daily Scrums. Cualquier problema técnico profundo se discutirá solo entre los involucrados al finalizar los 15 minutos reglamentarios.

---

## Historial de Control del Documento
| Versión | Fecha | Autor | Descripción de los Cambios |
|---------|-------|-------|----------------------------|
| 1.0     | [Fecha de hoy] |  (Scrum Master) | Creación inicial del PMP basado en IEEE 16326. |
