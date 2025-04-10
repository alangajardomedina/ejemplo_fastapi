#Librería que nos permite crear una api:
#FastAPI es la función para crear la API:
from fastapi import FastAPI

#acabamos de crear una variable app, del tipo FastAPI
api = FastAPI()

#Vamos a crear algunos métodos de la API:
#get, post, put, patch, delete
@api.get("/")
def root():
    return {"mensaje": "Hola mundo desde API 2"}

@api.get("/{id}")
def getAuto(id: int):
    autos = {
        1: {"marca": "Toyota", "modelo": "Supra"},
        2: {"marca": "Nissan", "modelo": "V16"}
    }
    return autos.get(id)