#Librería que nos permite crear una api:
#FastAPI es la función para crear la API:
from fastapi import FastAPI, HTTPException
#librería para realizar conexión con oracle:
import cx_Oracle
from pydantic import BaseModel

#acabamos de crear una variable app, del tipo FastAPI
api = FastAPI()

#Conexión con oracle:
def get_conexion():
    try:
        dsn = cx_Oracle.makedsn(
            "localhost",
            1521,
            service_name="orcl.duoc.com.cl"
        )
        conexion = cx_Oracle.connect(
            user="ejemplo_fastapi",
            password="ejemplo_fastapi",
            dsn=dsn
        )
        return conexion
    except Exception as e:
        print("Error al conectar con Oracle:",e)
        raise

#Vamos a crear un modelo para Usuarios:
class Usuario(BaseModel):
    rut: int
    pnombre: str
    apaterno: str
    amaterno: str
    email: str

@api.get("/usuarios")
def get_usuarios():
    try:
        cone = get_conexion()
        cursor = cone.cursor()
        cursor.execute("SELECT rut, pnombre, apaterno, amaterno, email FROM usuario")
        rows = cursor.fetchall()
        usuarios = [Usuario(rut=u[0], pnombre=u[1], apaterno=u[2], amaterno=u[3], email=u[4]) for u in rows]        
        return usuarios
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al obtener usuario: {e}"
        )
    
