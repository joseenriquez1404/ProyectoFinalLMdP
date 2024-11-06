# Dockerfile

FROM python:3.9-slim

# Actualizar y agregar dependencias de compilación y bibliotecas necesarias
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libdbus-1-dev \
    libglib2.0-dev \
    meson \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Actualizar pip antes de instalar las dependencias
RUN pip install --upgrade pip

# Copiar el archivo requirements.txt y luego instalar las dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente de Django al contenedor
COPY . /app/

EXPOSE 8000

ENV PYTHONUNBUFFERED 1

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

