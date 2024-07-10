# Demo DB PostgreSQL - Migracion desde x86 a IBM Power
R
Este repositorio contiene una aplicación Flask que utiliza Docker para su ejecución. La aplicación permite gestionar direcciones y realizar consultas a una base de datos PostgreSQL x86 y luego a la DB PostgreSQL en IBM Power.

## Requisitos

- Docker instalado en tu sistema.

## Instrucciones de Uso

### Paso 1: Clonar el Repositorio

Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/machina13/postgresql-ppc64le
cd postgresql-ppc64le
```

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
    docker build -t postgresql-ppc64le .
    ```

### Paso 4: Ejecutar el Contenedor Docker

1. Ejecuta el contenedor Docker:

    ```bash
    docker run -d -p 5000:5000 --env-file .env --name web postgresql-ppc64le
    ```

    - `-d`: Ejecuta el contenedor en segundo plano.
    - `-p 5000:5000`: Mapea el puerto 5000 del contenedor al puerto 5000 del host.
    - `--env-file .env`: Utiliza las variables de entorno definidas en el archivo `.env`.
    - `--name web`: Asigna un nombre al contenedor.

### Paso 5: Acceder a la Aplicación

1. Abre un navegador web y accede a la aplicación Flask en `http://ip:5000`.

### Detener y Eliminar el Contenedor

1. Si necesitas detener o eliminar el contenedor en algún momento, puedes usar los siguientes comandos:

    ```bash
    docker stop web  # Detener el contenedor
    docker rm web    # Eliminar el contenedor
    ```

    Donde `web` es el nombre que le diste a tu contenedor al ejecutarlo.



    ## Instalación y Configuración de PostgreSQL en CentOS 9

    ### Paso 1: Instalar PostgreSQL

    ```sudo dnf install postgresql-server postgresql-contrib -y```

    ### Paso 2: Modificar el archivo pg_hba.conf

    ```sudo vi /var/lib/pgsql/data/pg_hba.conf```

    Agregar la siguiente línea bajo ```IPv4 local connections:``` y comentar la línea anterior:

    ```host    all             all             0.0.0.0/0            md5

    #host    all             all             127.0.0.1/32            ident```

    ### Paso 3: Cambiar la contraseña del usuario postgres

    ```sudo passwd postgres```

    ### Paso 4: Reiniciar PostgreSQL

    ```sudo systemctl restart postgresql```

    ### Paso 5: Importar la base de datos dvdrental

    1. Descarga el archivo dvdrental.tar.gz desde [aquí](https://www.postgresqltutorial.com/wp-content/uploads/2019/05/dvdrental.zip) y cópialo a tu servidor CentOS.

    2. Descomprime el archivo:

    ```tar -xvf dvdrental.tar.gz```

    3. Ingresa a la consola de PostgreSQL como el usuario postgres:

    ```sudo -i -u postgres```

    4. Crea una nueva base de datos llamada dvdrental:

    ```createdb dvdrental```

    5. Restaura el archivo de respaldo dentro de la base de datos dvdrental:

    ```pg_restore -U postgres -d dvdrental dvdrental.tar```

    6. Sal de la consola de PostgreSQL:

    ```\q```

    ### Paso 6: Configurar Firewalld

    ```sudo firewall-cmd --permanent --add-port=5432/tcp```

    ```sudo firewall-cmd --reload```

    ### Paso 7: Configurar SELinux

    ```sudo setsebool -P httpd_can_network_connect_db 1```

    ### Paso 8: Iniciar y habilitar PostgreSQL

    ```sudo systemctl start postgresql```

    ```sudo systemctl enable postgresql```
