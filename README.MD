Demo DB PostgreSQL - Migration from x86 to IBM Power
====================================================

This repository contains a Flask application that uses Docker for its execution. The application allows managing addresses and querying a PostgreSQL x86 database and then the PostgreSQL database on IBM Power.

Requirements
------------

-   Docker installed on your system.

Usage Instructions
------------------

### Step 1: Clone the Repository

Clone this repository to your local machine:

bash

Copy code

`git clone https://github.com/machina13/postgresql-ppc64le
cd postgresql-ppc64le`

### Step 2: Configure Environment Variables

1.  Create a `.env` file in the root of the project with your PostgreSQL database configuration. Replace the example values with those appropriate for your environment:

    plaintext

    Copy code

    `DB_NAME=database_name
    DB_USER=user
    DB_PASSWORD=password
    DB_HOST=host_name
    DB_PORT=5432`

### Step 3: Build the Docker Image

1.  Build the Docker image using the provided Dockerfile:

    bash

    Copy code

    `docker build -t postgresql-ppc64le .`

### Step 4: Run the Docker Container

1.  Run the Docker container:

    bash

    Copy code

    `docker run -d -p 5000:5000 --env-file .env --name web postgresql-ppc64le`

    -   `-d`: Run the container in the background.
    -   `-p 5000:5000`: Map port 5000 of the container to port 5000 of the host.
    -   `--env-file .env`: Use the environment variables defined in the `.env` file.
    -   `--name web`: Assign a name to the container.

### Step 5: Access the Application

1.  Open a web browser and access the Flask application at `http://ip:5000`.

### Stop and Remove the Container

1.  If you need to stop or remove the container at any point, you can use the following commands:

    bash

    Copy code

    `docker stop web  # Stop the container
    docker rm web    # Remove the container`

    Where `web` is the name you assigned to your container when you ran it.

Installation and Configuration of PostgreSQL on CentOS 9
--------------------------------------------------------

### Step 1: Install PostgreSQL

bash

Copy code

`sudo dnf install postgresql-server postgresql-contrib -y`

### Step 2: Modify the pg_hba.conf File

bash

Copy code

`sudo vi /var/lib/pgsql/data/pg_hba.conf`

Add the following line under `IPv4 local connections:` and comment out the previous line:

plaintext

Copy code

`host    all             all             0.0.0.0/0            md5
#host    all             all             127.0.0.1/32            ident`

### Step 3: Change the postgres User Password

bash

Copy code

`sudo passwd postgres`

### Step 4: Restart PostgreSQL

bash

Copy code

`sudo systemctl restart postgresql`

### Step 5: Import the dvdrental Database

1.  Download the dvdrental.tar.gz file from [here](https://www.postgresqltutorial.com/wp-content/uploads/2019/05/dvdrental.zip) and copy it to your CentOS server.

2.  Extract the file:

    bash

    Copy code

    `tar -xvf dvdrental.tar.gz`

3.  Enter the PostgreSQL console as the postgres user:

    bash

    Copy code

    `sudo -i -u postgres`

4.  Create a new database called dvdrental:

    bash

    Copy code

    `createdb dvdrental`

5.  Restore the backup file into the dvdrental database:

    bash

    Copy code

    `pg_restore -U postgres -d dvdrental dvdrental.tar`

6.  Exit the PostgreSQL console:

    bash

    Copy code

    `\q`

### Step 6: Configure Firewalld

bash

Copy code

`sudo firewall-cmd --permanent --add-port=5432/tcp
sudo firewall-cmd --reload`

### Step 7: Configure SELinux

bash

Copy code

`sudo setsebool -P httpd_can_network_connect_db 1`

### Step 8: Start and Enable PostgreSQL

bash

Copy code

`sudo systemctl start postgresql
sudo systemctl enable postgresql`
