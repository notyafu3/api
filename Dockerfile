# Imagen base oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY . .

# Instala dependencias necesarias
RUN pip install --no-cache-dir flask

# Expone el puerto que usará Flask
EXPOSE 5000

# Ejecuta el script para crear la base de datos (opcional si no está precargada)
RUN python crear_db.py

# Comando para iniciar la aplicación Flask
CMD ["python", "api.py"]
