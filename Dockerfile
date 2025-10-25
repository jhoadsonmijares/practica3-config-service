# Imagen base de Python
FROM python:3.9

# Establecer directorio de trabajo en el contenedor
WORKDIR /app

# Copiar archivos de requisitos primero (para cache de Docker)
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . .

# Exponer el puerto que usa Django
EXPOSE 8000

# Comando por defecto (puede ser sobrescrito en docker-compose)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]