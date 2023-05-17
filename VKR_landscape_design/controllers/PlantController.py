from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter, Response
import json
from base_models import Animal
from models.animals_model import *
from utils import get_db_connection
router = APIRouter()



@router.get("/animals/all")
async def animals_get_select_all():
    conn = get_db_connection()
    x = get_animals(conn)
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.post("/animals/delete")
async def animals_post_delete(animal_id: int):
    conn = get_db_connection()
    x = delete_animal(conn, animal_id)
    return Response("{'messdelete':'Животное удалёно.'}", status_code=200)

@router.post("/animals/insert")
async def animals_post_insert(animal_name: str, animal_description: str):
    conn = get_db_connection()
    x = insert_animal(conn, animal_name, animal_description)
    return Response("{'messinsert':'Животное создано.'}", status_code=200)

@router.post("/animals/update/name")
async def animals_post_update_name(animal_id: int, animal_name: str):
    conn = get_db_connection()
    x = update_animal_name(conn, animal_id, animal_name)
    return Response("{'messname':'Название животного обновлено.'}", status_code=200)

@router.post("/animals/update/description")
async def animals_post_update_description(animal_id: int, animal_description: str):
    conn = get_db_connection()
    x = update_animal_description(conn, animal_id, animal_description)
    return Response("{'messdescription':'Описание животного обновлено.'}", status_code=200)

@router.post("/animals/update/kingdom")
async def animals_post_update_kingdom(animal_id: int, animal_kingdom: str):
    conn = get_db_connection()
    x = update_animal_kingdom(conn, animal_id, animal_kingdom)
    return Response("{'messkingdom':'Царство животного обновлено.'}", status_code=200)

@router.post("/animals/update/philum")
async def animals_post_update_philum(animal_id: int, animal_philum: str):
    conn = get_db_connection()
    x = update_animal_philum(conn, animal_id, animal_philum)
    return Response("{'messphilum':'Тип животного обновлён.'}", status_code=200)

@router.post("/animals/update/class")
async def animals_post_update_class(animal_id: int, animal_class: str):
    conn = get_db_connection()
    x = update_animal_class(conn, animal_id, animal_class)
    return Response("{'messclass':'Класс животного обновлён.'}", status_code=200)

@router.post("/animals/update/order")
async def animals_post_update_order(animal_id: int, animal_order: str):
    conn = get_db_connection()
    x = update_animal_order(conn, animal_id, animal_order)
    return Response("{'messorder':'Порядок животного обновлён.'}", status_code=200)

@router.post("/animals/update/family")
async def animals_post_update_family(animal_id: int, animal_family: str):
    conn = get_db_connection()
    x = update_animal_family(conn, animal_id, animal_family)
    return Response("{'messfamily':'Семейство животного обновлено.'}", status_code=200)

@router.post("/animals/update/genus")
async def animals_post_update_genus(animal_id: int, animal_genus: str):
    conn = get_db_connection()
    x = update_animal_genus(conn, animal_id, animal_genus)
    return Response("{'messgenus':'Родовая принадлежность животного обновлена.'}", status_code=200)

@router.post("/animals/update/species")
async def animals_post_update_species(animal_id: int, animal_species: str):
    conn = get_db_connection()
    x = update_animal_species(conn, animal_id, animal_species)
    return Response("{'messspecies':'Видовая принадлежность животного обновлена.'}", status_code=200)

@router.post("/animals/update/picture")
async def animals_post_update_picture(animal_id: int, animal_picture: str):
    conn = get_db_connection()
    x = update_animal_picture(conn, animal_id, animal_picture)
    return Response("{'messpicture':'Картинка животного обновлена.'}", status_code=200)

