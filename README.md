# Config Service API - Práctica 3

Servicio de gestión de configuración dinámica implementado con Django REST Framework.

## 🚀 Características

- ✅ API RESTful para gestión de entornos y variables
- ✅ Endpoints para consumo masivo en formato JSON
- ✅ Paginación en listados
- ✅ Autenticación Basic Auth
- ✅ Esquemas de datos validados
- ✅ Códigos de estado HTTP apropiados

## 📦 Estructura del Proyecto
practica3-config-service/
├── configservice/ # Configuración principal Django
├── environments/ # App para gestión de entornos
├── variables/ # App para gestión de variables
├── manage.py # Script de gestión Django
├── docker-compose.yml # Orquestación con PostgreSQL
├── Dockerfile # Contenedor de la aplicación
└── requirements.txt # Dependencias del proyecto


## 🛠️ Instalación y Uso

### Desarrollo Local (SQLite)

1. **Clonar el repositorio:**
   ```bash
   git clone [url-del-repositorio]
   cd practica3-config-service

Instalar dependencias:
bash

pip install -r requirements.txt

Configurar variables de entorno:
bash

# El archivo .env ya está configurado para desarrollo

Ejecutar migraciones:
bash

python manage.py migrate

Crear superusuario:
bash

python manage.py createsuperuser

Ejecutar servidor:
bash

python manage.py runserver


Producción (Docker + PostgreSQL)

    Ejecutar con Docker Compose:
    bash

docker-compose up --build

Ejecutar migraciones en el contenedor:
bash

docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser

📡 Endpoints de la API
Health Check

    GET /status/ - Verificar estado del servicio

Entornos

    GET /api/environments/ - Listar entornos (paginado)

    POST /api/environments/ - Crear nuevo entorno

    GET /api/environments/{env_name}/ - Obtener entorno específico

    PUT /api/environments/{env_name}/ - Actualizar entorno

    PATCH /api/environments/{env_name}/ - Actualización parcial

    DELETE /api/environments/{env_name}/ - Eliminar entorno

Variables

    GET /api/environments/{env_name}/variables/ - Listar variables (paginado)

    POST /api/environments/{env_name}/variables/ - Crear nueva variable

    GET /api/environments/{env_name}/variables/{var_name}/ - Obtener variable

    PUT /api/environments/{env_name}/variables/{var_name}/ - Actualizar variable

    DELETE /api/environments/{env_name}/variables/{var_name}/ - Eliminar variable

Consumo Masivo

    GET /api/environments/{env_name}.json - Configuración completa en JSON

🔐 Autenticación

La API utiliza autenticación Basic Auth. Incluye credenciales en las peticiones:
bash

curl -u username:password http://localhost:8000/api/environments/

🗃️ Esquemas de Datos
Entorno
json

{
  "name": "production",
  "description": "Entorno de producción",
  "created_at": "2025-10-25T00:00:00Z",
  "updated_at": "2025-10-25T00:00:00Z"
}

Variable
json

{
  "name": "database_url",
  "value": "postgresql://user:pass@host/db",
  "description": "URL de base de datos",
  "environment": "production",
  "is_sensitive": true,
  "created_at": "2025-10-25T00:00:00Z",
  "updated_at": "2025-10-25T00:00:00Z"
}

👥 Integrantes del Equipo

    Jhony Mijares 25574530 - Desarrollo y documentación

📝 Notas Técnicas

    Base de datos: SQLite para desarrollo, PostgreSQL para producción

    Framework: Django 4.2.7 + Django REST Framework

    Contenedores: Docker + Docker Compose

    Autenticación: Basic Auth integrada en REST Framework