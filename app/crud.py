# app/crud.py
from app.database import get_db_connection
from app.models import Item

# Obtener todos los items
def get_items():
    connection = get_db_connection()
    if connection is None:
        raise RuntimeError("No se pudo conectar a la base de datos")
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT name, description, price, tax FROM items;")
            items = cursor.fetchall()
        return [Item(name=row[0], description=row[1], price=row[2], tax=row[3]) for row in items]
    except Exception as e:
        print(f"Error al obtener items: {e}")
        raise
    finally:
        if connection:
            connection.close()
# Crear un nuevo item
def create_item(item: Item):
    connection = get_db_connection()
    if connection is None:
        raise RuntimeError("No se pudo conectar a la base de datos")
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """INSERT INTO items (name, description, price, tax) 
                VALUES (%s, %s, %s, %s) RETURNING name, description, price, tax;""",
                (item.name, item.description, item.price, item.tax)
            )
            connection.commit()
            created_item = cursor.fetchone()
            return Item(name=created_item[0], description=created_item[1], price=created_item[2], tax=created_item[3])
    except Exception as e:
        if connection:
            connection.rollback()
        print(f"Error al crear el item: {e}")
        raise
    finally:
        if connection:
            connection.close()