# app/database.py
import psycopg2
from psycopg2 import sql

# Función para obtener la conexión a la base de datos
def get_db_connection():
    try:
        connection = psycopg2.connect(
            dbname="luis",
            user="postgres",
            password="123",
            host="localhost",
            port="5432"
        )
        print("Conexión exitosa a la base de datos")
        return connection
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None