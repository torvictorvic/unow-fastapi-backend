# FastAPI/Python Backend (Envío de Correos)

## Descripción

Este proyecto es un servicio backend desarrollado con FastAPI y Python, encargado de gestionar el envío de correos electrónicos. Utiliza diversas librerías para enviar correos de manera eficiente y segura.

## Tabla de Contenidos

- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Prerequisitos](#prerequisitos)
- [Instalación](#instalación-configuración)
- [Tests](#tests)

## Tecnologías-Utilizadas

- **Framework:** FastAPI
- **Lenguaje:** Python 3.9
- **Servidor ASGI:** Uvicorn
- **Librerías:** pydantic, pytest, pytest-cov, aiosmtplib
- **Herramientas de Desarrollo:** PIP, Git

## Prerequisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu sistema:

- **Python:** >= 3.9
- **PIP:** >= 3.9 Para gestionar dependencias
- **Git:** Para clonar el repositorio

## Instalación-configuración

1. **Clonar el Repositorio**

   ```bash
   git clone https://github.com/torvictorvic/unow-fastapi-backend.git
   cd unow-fastapi-backend

2. **Crear un Ambiente Virtual para aislar las dependencias.**

   ```bash
   python3.9 -m venv venv
   source venv/bin/activate


3. **Instalar dependencias.**

   ```bash
   pip3.9 install -r requirements.txt


4. **Exportar variables desde la terminal del sistema operativo.**

   ```bash
   export BACKEND_SHARED_TOKEN_PHP_PY="xx"
   export BACKEND_EMAIL_SENDER_PY="xxx@gmail.com"
   export BACKEND_EMAIL_TOKEN_PY=""

5. **Correr aplicacion en local.**
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 5000


## tests

1. **Correr Test unitarios**
   ```bash
   pytest test_app.py
