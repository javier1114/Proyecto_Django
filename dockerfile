# Obtener imagen base
FROM --platform=linux/amd64 python:3.11.4-slim-bullseye

#Definir variables de entorno
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Definir directorio de trabajo
WORKDIR /code

#Instalacion de dependencias
COPY ./requerimientos.txt .
RUN pip install -r requerimientos.txt

#Copiar el proyecto
COPY . .