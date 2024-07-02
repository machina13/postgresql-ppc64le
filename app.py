from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import platform
import socket
import os
from dotenv import load_dotenv

load_dotenv()  # Cargar las variables de entorno desde el archivo .env

app = Flask(__name__)

# Configuración inicial de la base de datos desde las variables de entorno
db_config = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),  # Valor inicial desde la variable de entorno
    'port': os.getenv('DB_PORT')
}

def get_db_connection():
    conn = psycopg2.connect(**db_config)
    return conn

def get_db_info():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT inet_server_addr(), version();")
    result = cur.fetchone()
    cur.close()
    conn.close()

    host_ip = result[0]
    version_info = result[1]

    if 'IBM' in version_info or 'Power' in version_info:
        architecture = 'ppc'
    else:
        architecture = 'x86'

    # Información adicional del sistema
    system_info = {
        'hostname': socket.gethostname(),
        'ip_address': host_ip,
        'os': platform.system(),
        'os_version': platform.version(),
        'cpu': platform.processor(),
        'cpu_architecture': platform.machine()
    }
    
    return system_info

@app.route('/')
def index():
    db_info = get_db_info()
    return render_template('index.html', db_info=db_info)

@app.route('/consultar', methods=['POST'])
def consultar():
    query = "SELECT * FROM address"
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query)
    columns = [desc[0] for desc in cur.description]
    result = cur.fetchall()
    cur.close()
    conn.close()
    db_info = get_db_info()
    return render_template('index.html', query=query, result=result, columns=columns, db_info=db_info)

@app.route('/agregar', methods=['POST'])
def agregar():
    conn = get_db_connection()
    cur = conn.cursor()

    address = request.form['address']
    address2 = request.form['address2']
    district = request.form['district']
    city_id = request.form['city_id']
    postal_code = request.form['postal_code']
    phone = request.form['phone']
    db_host = request.form['db_host']  # Nueva variable para la dirección IP del host

    # Actualizamos la configuración de la base de datos con la nueva dirección IP
    db_config['host'] = db_host

    # Ejemplo de inserción, ajusta según tus necesidades
    query = "INSERT INTO address (address, address2, district, city_id, postal_code, phone, last_update) VALUES (%s, %s, %s, %s, %s, %s, NOW())"
    data = (address, address2, district, city_id, postal_code, phone)
    cur.execute(query, data)
    conn.commit()

    cur.close()
    conn.close()

    return redirect(url_for('index'))  # Redirige a la página principal

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

