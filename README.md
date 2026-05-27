# API Pastelería - Proyecto CI/CD y Contenedores 

Este repositorio contiene la entrega para la Evaluación 2 de Ingeniería DevOps. El objetivo principal de este proyecto es la creación de un microservicio en Python (Flask) integrado a un pipeline completo de Integración y Entrega Continua (CI/CD) utilizando contenedores.

## Tecnologías Implementadas
- **Backend:** Python 3.9 + Flask
- **Testing:** Pytest
- **Contenedores:** Docker + Docker Compose
- **Automatización:** GitHub Actions
- **Seguridad:** Dependabot

---

##  Cómo levantar el proyecto localmente

Para ejecutar este microservicio, la forma oficial y recomendada es utilizar Docker, ya que garantiza que el entorno sea idéntico al de producción.

1. Clona este repositorio en tu máquina.
2. Abre una terminal en la raíz del proyecto.
3. Ejecuta el siguiente comando para construir la imagen y levantar el servicio en segundo plano:
   ```bash
   docker compose up -d
La API estará disponible en http://localhost:5000

4. Para detener y eliminar los contenedores, ejecuta:
docker compose down

5. El proyecto cuenta con una batería de pruebas unitarias creadas con pytest que validan el correcto funcionamiento de los endpoints de la API (verificación de salud, lectura de productos y creación de productos).
Para correr las pruebas localmente (requiere entorno Python):

pip install -r requirements.txt
pytest test_app.py -v

##  Trazabilidad y Calidad

Para garantizar la **trazabilidad** del proyecto, cada cambio realizado mediante *commits* o *Pull Requests* a la rama `main` dispara automáticamente nuestro pipeline de CI/CD en GitHub Actions. Esto deja un registro histórico e inmutable en la pestaña "Actions", donde se puede trazar exactamente qué versión del código se integró, quién lo hizo, a qué hora, y el resultado detallado de cada etapa del proceso.

La **calidad** y fiabilidad en cada despliegue se asegura mediante múltiples capas en el pipeline:
1. Ejecución automática de pruebas unitarias (Pytest) que cubren el CRUD de la API.
2. Validación de sintaxis y prevención de vulnerabilidades mediante herramientas de análisis estático y de dependencias (Dependabot / SonarCloud).
3. Construcción y orquestación inmutable mediante contenedores (Docker), garantizando que si el entorno falla, el código defectuoso nunca se despliegue.
.