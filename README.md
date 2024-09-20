# sobre_ruedas

Este es un proyecto desarrollado con Django para la gestión de vehículos en un CMS personalizado.

## Requisitos previos

Asegúrate de tener instalados los siguientes requisitos antes de continuar:

- Python 3.12.4
- pip

## Instalación

Sigue estos pasos para poner en marcha el proyecto:

### 1. Clonar el repositorio

Clona este repositorio en tu máquina local:
 
    git clone https://github.com/tebyboho/sobre_ruedas.git


### 2. Crear y activar un entorno virtual (opcional, recomendado)

En macOS/Linux:

Crea el entorno virtual:

    python3 -m venv env

Activa el entorno virtual:

    source env/bin/activate

En Windows:

Crea el entorno virtual:

    python -m venv env

Activa el entorno virtual:

    .\env\Scripts\activate


Tu estructura de carpetas debería verse así:

**Carpeta Raiz**

- _env_
- _sobre_ruedas_


### 3. Instalar dependencias 

    pip install -r requirements.txt


### 4. Aplicar migraciones

Asegurarse de estar posicionado dentro de sobre_ruedas y ejecutar el siguiente comando

    python manage.py migrate

### 5. Levantar el servidor de desarrollo:

Dentro de sobre_ruedas, ejecutar

    python manage.py runserver

### 6. Acceder al sitio:

http://127.0.0.1:8000/


### 7. Para desactivar el entorno virtual:

Desde cualquier parte del sistema, ejecutar:

    deactivate
