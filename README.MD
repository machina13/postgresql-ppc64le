Demo DB PostgreSQL - Migration from x86 to IBM Power
====================================================

Project Overview
------------
This project demonstrates the migration of a PostgreSQL database from an x86 server to an IBM Power server. The objective is to showcase the seamless transfer of data and the compatibility between different architectures, highlighting the benefits and capabilities of IBM Power systems for database management. The following steps will guide you through the process of setting up the environment, performing the migration, and verifying the success of the transfer.

Resume
------------
This repository contains a Flask application that uses Docker for its execution. The application allows managing addresses and querying a PostgreSQL x86 database and then the PostgreSQL database on IBM Power.

Architecture
------------

![alt text](https://github.com/machina13/postgresql-ppc64le/blob/main/CPT2408061128-1237x544.gif)


Requirements
------------

-   1 server or VM on x86 architecture
-   1 server or LPAR on IBM Power architecture
-   1 VM with docker

Usage Instructions
------------------

### Step 1: Clone the Repository

Clone this repository to your local machine:


```
git clone https://github.com/machina13/postgresql-ppc64le
cd postgresql-ppc64le
```

### Step 2: Configure Environment Variables

1.  Create a `.env` file in the root of the project with your PostgreSQL database configuration. Replace the example values with those appropriate for your environment:


    `DB_NAME=database_name
    DB_USER=user
    DB_PASSWORD=password
    DB_HOST=host_name
    DB_PORT=5432`

### Step 3: Build the Docker Image

1.  Build the Docker image using the provided Dockerfile:


    `docker build -t postgresql-ppc64le .`

### Step 4: Run the Docker Container

1.  Run the Docker container:

```
docker run -d -p 5000:5000 --env-file .env --name web postgresql-ppc64le
```

    -   -d: Run the container in the background.
    -   -p 5000:5000: Map port 5000 of the container to port 5000 of the host.
    -   `--env-file .env`: Use the environment variables defined in the `.env` file.
    -   `--name web`: Assign a name to the container.

### Step 5: Access the Application

1.  Open a web browser and access the Flask application at `http://ip:5000`.

### Stop and Remove the Container

1.  If you need to stop or remove the container at any point, you can use the following commands:

```
docker stop web  # Stop the container
docker rm web    # Remove the container
```

Where `web` is the name you assigned to your container when you ran it.

Installation and Configuration of PostgreSQL on CentOS 9
--------------------------------------------------------

### Step 1: Install PostgreSQL


`sudo dnf install postgresql-server postgresql-contrib -y`

### Step 2: Modify the pg_hba.conf File


`sudo vi /var/lib/pgsql/data/pg_hba.conf`

Add the following line under `IPv4 local connections:` and comment out the previous line:


```
host    all             all             0.0.0.0/0            md5
#host    all             all             127.0.0.1/32            ident
```

### Step 3: Change the postgres User Password


`sudo passwd postgres`

### Step 4: Restart PostgreSQL


`sudo systemctl restart postgresql`

### Step 5: Import the dvdrental Database

1.  Download the dvdrental.tar.gz file from [here](https://www.postgresqltutorial.com/wp-content/uploads/2019/05/dvdrental.zip) and copy it to your CentOS server.

2.  Extract the file:


    `tar -xvf dvdrental.tar.gz`

3.  Enter the PostgreSQL console as the postgres user:


    `sudo -i -u postgres`

4.  Create a new database called dvdrental:


    `createdb dvdrental`

5.  Restore the backup file into the dvdrental database:


    `pg_restore -U postgres -d dvdrental dvdrental.tar`

6.  Exit the PostgreSQL console:


    `\q`

### Step 6: Configure Firewalld


```
sudo firewall-cmd --permanent --add-port=5432/tcp
sudo firewall-cmd --reload
```

### Step 7: Configure SELinux

```
sudo setsebool -P httpd_can_network_connect_db 1
```

### Step 8: Start and Enable PostgreSQL

```
sudo systemctl start postgresql
sudo systemctl enable postgresql
```
