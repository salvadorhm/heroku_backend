import fastapi
import sqlite3
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Crea la base de datos
conn = sqlite3.connect("sql/contactos.db")

app = fastapi.FastAPI()

origins = [
    "http://localhost:8080",
    "https://shm-frontend-c3f2dc0fa89c.herokuapp.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Contacto(BaseModel):
    email : str
    nombre : str
    telefono : str

@app.get("/contactos")
async def obtener_contactos():
    """Obtiene todos los contactos."""
    # DONE Consulta todos los contactos de la base de datos y los envia en un JSON
    c = conn.cursor()
    c.execute('SELECT * FROM contactos')
    response = []
    for row in c:
        contacto = {"email":row[0], "nombre":row[1], "telefono":row[2]}
        response.append(contacto)
    return response
