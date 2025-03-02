# app/main.py
from fastapi import FastAPI, HTTPException
from app.database import get_db_connection
from app.models import Item
from app.crud import get_items, create_item

# Crear instancia de FastAPI
app = FastAPI()

# Inicializar la base de datos
@app.on_event("startup")
def startup():
    connection = get_db_connection()
    if connection is None:
        raise RuntimeError("No se pudo conectar a la base de datos")

# Leer todos los items
@app.get("/items", response_model=list[Item])
def read_items():
    try:
        return get_items()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al leer items: {e}")

# Crear un nuevo item
@app.post("/items", response_model=Item)
def add_item(item: Item):
    try:
        created_item = create_item(item)
        if not created_item:
            raise HTTPException(status_code=400, detail="Error al crear el item")
        return created_item
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno al crear el item: {e}")