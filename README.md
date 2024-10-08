# Cápsula 3 - API en FastAPI

Este proyecto es una API creada con **FastAPI**, diseñada para esta ayudantía. A continuación, encontrarás los pasos necesarios para levantar el entorno local y ejecutar la API.

## Requisitos previos

Asegúrate de tener instalados los siguientes componentes:

- **Python 3.6+**: FastAPI requiere Python 3.6 o versiones superiores.
- **Pip**: Administrador de paquetes de Python (normalmente incluido con Python).
- **Git** (opcional): Para clonar el repositorio desde un sistema de control de versiones.

## Instalación

Sigue los siguientes pasos para levantar la API localmente:

### 1. Clonar el repositorio

Clona este repositorio en tu máquina local utilizando el siguiente comando:

```bash
git clone https://github.com/mizook/capsula_3
cd capsula_3
```

### 2. Crear y activar un entorno virtual

Es recomendable crear un entorno virtual para aislar las dependencias del proyecto. Puedes hacerlo de la siguiente manera:

- En **Windows**:

  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

- En **Linux/MacOS**:

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Instalar las dependencias

Con el entorno virtual activado, instala las dependencias del proyecto usando el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Configurar el archivo .env

Copia el archivo .env.example a un nuevo archivo llamado .env y edítalo para incluir tu connection string u otras variables de entorno necesarias. El archivo .env debería verse similar a esto:

```bash
DATABASE_URL=connection_string_to_postgresql
```

Asegúrate de reemplazar connection_string_to_postgresql con la cadena de conexión adecuada para tu base de datos.

### 5. Ejecutar la API

Una vez instaladas las dependencias, puedes levantar el servidor de la API utilizando **Uvicorn**, el servidor ASGI recomendado para FastAPI. Usa el siguiente comando:

```bash
uvicorn main:app --reload
```

Este comando hará lo siguiente:

- Levantará el servidor local de la API en `http://127.0.0.1:8000`.
- Habilitará el modo `--reload` para que la API se recargue automáticamente cuando realices cambios en el código.

### 5. Probar la API

Una vez levantada la API, puedes acceder a la documentación interactiva proporcionada por FastAPI en los siguientes enlaces:

- **Documentación Swagger UI**: `http://127.0.0.1:8000/docs`
- **Documentación Redoc**: `http://127.0.0.1:8000/redoc`

## Dependencias principales

- **FastAPI**: Framework para crear APIs rápidas y eficientes.
- **Uvicorn**: Servidor ASGI recomendado para FastAPI.
