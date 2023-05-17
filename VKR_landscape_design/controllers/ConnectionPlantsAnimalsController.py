from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter, Response
import json
from base_models import ConnectionPlantsAnimals
from models.connection_plants_animals_model import *
from utils import get_db_connection
router = APIRouter()



@router.get("/connectionplantsanimals/all")
async def connection_plants_animals_get_select_all():
    conn = get_db_connection()
    x = get_connection_plants_animals(conn)
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.post("/connectionplantsanimals/insert")
async def connection_plants_animals_post_insert(connection_plant_id: int, connection_animal_id: int):
    conn = get_db_connection()
    x = insert_connection_plants_animals(conn, connection_plant_id, connection_animal_id)
    return Response("{'message':'Связь между растением и животным (какое животное ест это растение) добавлена.'}", status_code=200)

@router.post("/connectionplantsanimals/delete")
async def connection_plants_animals_post_delete(connection_plants_animals_id: int):
    conn = get_db_connection()
    x = delete_connection_plants_animals(conn, connection_plants_animals_id)
    return Response("{'messname':'Связь между растением и животным (какое животное ест это растение) удалена.'}", status_code=200)

@router.post("/connectionplantsanimals/update/plantid")
async def connection_plants_animals_post_update_plant_id(connection_plants_animals_id: int, connection_plants_animals_plant_id: str):
    conn = get_db_connection()
    x = update_connection_plants_animals_plant_id(conn, connection_plants_animals_id, connection_plants_animals_plant_id)
    return Response("{'messname':'ID растения в связи между растением и животным (какое животное ест это растение) обновлён.'}", status_code=200)

@router.post("/connectionplantsanimals/update/animalid")
async def connection_plants_animals_post_update_animal_id(connection_plants_animals_id: int, connection_plants_animals_animal_id: str):
    conn = get_db_connection()
    x = update_connection_plants_animals_animal_id(conn, connection_plants_animals_id, connection_plants_animals_animal_id)
    return Response("{'messname':'ID животного в связи между растением и животным (какое животное ест это растение) обновлён.'}", status_code=200)
