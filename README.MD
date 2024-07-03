# Mi Proyecto Flask con Docker

Este repositorio contiene una aplicación Flask que utiliza Docker para su ejecución. La aplicación permite gestionar direcciones y realizar consultas a una base de datos PostgreSQL.

## Requisitos

- Docker instalado en tu sistema.

## Instrucciones de Uso

### Paso 1: Clonar el Repositorio

Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/tu_usuario/mi-proyecto-flask.git
cd mi-proyecto-flask

## Instrucciones de Uso

### Paso 2: Configurar Variables de Entorno

1. Crea un archivo `.env` en la raíz del proyecto con la configuración de tu base de datos PostgreSQL. Sustituye los valores de ejemplo con los adecuados para tu entorno:

    ```plaintext
    DB_NAME=nombre_base_datos
    DB_USER=usuario
    DB_PASSWORD=password
    DB_HOST=nombre_host
    DB_PORT=5432
    ```

### Paso 3: Construir la Imagen Docker

1. Construye la imagen Docker utilizando el Dockerfile proporcionado:

    ```bash
    docker build -t mi_proyecto_flask .
    ```

### Paso 4: Ejecutar el Contenedor Docker

1. Ejecuta el contenedor Docker:

    ```bash
    docker run -d -p 5000:5000 --env-file .env --name mi_proyecto_flask_container mi_proyecto_flask
    ```

    - `-d`: Ejecuta el contenedor en segundo plano.
    - `-p 5000:5000`: Mapea el puerto 5000 del contenedor al puerto 5000 del host.
    - `--env-file .env`: Utiliza las variables de entorno definidas en el archivo `.env`.
    - `--name mi_proyecto_flask_container`: Asigna un nombre al contenedor.

### Paso 5: Acceder a la Aplicación

1. Abre un navegador web y accede a la aplicación Flask en `http://localhost:5000`.

### Detener y Eliminar el Contenedor

1. Si necesitas detener o eliminar el contenedor en algún momento, puedes usar los siguientes comandos:

    ```bash
    docker stop mi_proyecto_flask_container  # Detener el contenedor
    docker rm mi_proyecto_flask_container    # Eliminar el contenedor
    ```

    Donde `mi_proyecto_flask_container` es el nombre que le diste a tu contenedor al ejecutarlo.
Estos pasos están ahora organizados en formato Markdown, lo que facilita su lectura y comprensión dentro del archivo README.md.

ahora muetra todos los pasos en un archivo readme.me
ChatGPT
Aquí tienes el archivo README.md completo con todos los pasos organizados en formato Markdown:

markdown
Copy code
# Mi Proyecto Flask con Docker

Este repositorio contiene una aplicación Flask que utiliza Docker para su ejecución. La aplicación permite gestionar direcciones y realizar consultas a una base de datos PostgreSQL.

## Requisitos

- Docker instalado en tu sistema.

## Instrucciones de Uso

### Paso 1: Clonar el Repositorio

Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/tu_usuario/mi-proyecto-flask.git
cd mi-proyecto-flask
