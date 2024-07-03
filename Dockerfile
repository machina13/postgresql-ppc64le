# Utilizar una imagen base de Python
FROM python:3.9-slim
#prueba
# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo requirements.txt y .env
COPY requirements.txt ./
COPY .env ./

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

# Exponer el puerto en el que correrá la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
