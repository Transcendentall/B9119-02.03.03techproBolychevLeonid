from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter, Response, HTTPException
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

@router.get("/animals/one")
async def animals_get_one_animal(animal_id: int):
    conn = get_db_connection()
    x = get_one_animal(conn, animal_id)
    if len(x) == 0:
        raise HTTPException(status_code=404, detail="Ошибка: животное с данным ID не найдено.")
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.post("/animals/delete")
async def animals_post_delete(animal_id: int):
    conn = get_db_connection()
    y = get_one_animal(conn, animal_id)
    if len(y) == 0:
        raise HTTPException(status_code=404, detail="Ошибка: животное с данным ID не найдено, потому удалить его невозможно.")
    x = delete_animal(conn, animal_id)
    return Response("{'messdelete':'Животное удалёно.'}", status_code=200)

@router.post("/animals/insert")
async def animals_post_insert(animal_name: str, animal_description: str):
    conn = get_db_connection()
    if ((len(animal_name) < 2) or (len(animal_name) > 30) or (not(animal_name[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: название животного должно иметь длину от 2 до 30 символов (включительно), а его первая буква должна быть заглавной.")
    if ((len(animal_description) < 2) or (len(animal_description) > 3000) or (not(animal_description[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: описание животного должно иметь длину от 2 до 3000 символов (включительно), а его первая буква должна быть заглавной.")
    x = insert_animal(conn, animal_name, animal_description)
    return Response("{'messinsert':'Животное создано.'}", status_code=200)

@router.post("/animals/update/name")
async def animals_post_update_name(animal_id: int, animal_name: str):
    conn = get_db_connection()
    if ((len(animal_name) < 2) or (len(animal_name) > 30) or (not(animal_name[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: название животного должно иметь длину от 2 до 30 символов (включительно), а его первая буква должна быть заглавной.")
    x = update_animal_name(conn, animal_id, animal_name)
    return Response("{'messname':'Название животного обновлено.'}", status_code=200)

@router.post("/animals/update/description")
async def animals_post_update_description(animal_id: int, animal_description: str):
    conn = get_db_connection()
    if ((len(animal_description) < 2) or (len(animal_description) > 3000) or (not(animal_description[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: описание животного должно иметь длину от 2 до 3000 символов (включительно), а его первая буква должна быть заглавной.")
    x = update_animal_description(conn, animal_id, animal_description)
    return Response("{'messdescription':'Описание животного обновлено.'}", status_code=200)

@router.post("/animals/update/kingdom")
async def animals_post_update_kingdom(animal_id: int, animal_kingdom: str):
    conn = get_db_connection()
    if ((len(animal_kingdom) < 2) or (len(animal_kingdom) > 30) or (not(animal_kingdom[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: название царства животного должно иметь длину от 2 до 30 символов (включительно), а его первая буква должна быть заглавной.")
    x = update_animal_kingdom(conn, animal_id, animal_kingdom)
    return Response("{'messkingdom':'Царство животного обновлено.'}", status_code=200)

@router.post("/animals/update/philum")
async def animals_post_update_philum(animal_id: int, animal_philum: str):
    conn = get_db_connection()
    if ((len(animal_philum) < 2) or (len(animal_philum) > 30) or (not(animal_philum[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: название типа животного должно иметь длину от 2 до 30 символов (включительно), а его первая буква должна быть заглавной.")
    x = update_animal_philum(conn, animal_id, animal_philum)
    return Response("{'messphilum':'Тип животного обновлён.'}", status_code=200)

@router.post("/animals/update/class")
async def animals_post_update_class(animal_id: int, animal_class: str):
    conn = get_db_connection()
    if ((len(animal_class) < 2) or (len(animal_class) > 30) or (not(animal_class[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: название класса животного должно иметь длину от 2 до 30 символов (включительно), а его первая буква должна быть заглавной.")
    x = update_animal_class(conn, animal_id, animal_class)
    return Response("{'messclass':'Класс животного обновлён.'}", status_code=200)

@router.post("/animals/update/order")
async def animals_post_update_order(animal_id: int, animal_order: str):
    conn = get_db_connection()
    if ((len(animal_order) < 2) or (len(animal_order) > 30) or (not(animal_order[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: название порядка животного должно иметь длину от 2 до 30 символов (включительно), а его первая буква должна быть заглавной.")
    x = update_animal_order(conn, animal_id, animal_order)
    return Response("{'messorder':'Порядок животного обновлён.'}", status_code=200)

@router.post("/animals/update/family")
async def animals_post_update_family(animal_id: int, animal_family: str):
    conn = get_db_connection()
    if ((len(animal_family) < 2) or (len(animal_family) > 30) or (not(animal_family[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: название семейства животного должно иметь длину от 2 до 30 символов (включительно), а его первая буква должна быть заглавной.")
    x = update_animal_family(conn, animal_id, animal_family)
    return Response("{'messfamily':'Семейство животного обновлено.'}", status_code=200)

@router.post("/animals/update/genus")
async def animals_post_update_genus(animal_id: int, animal_genus: str):
    conn = get_db_connection()
    if ((len(animal_genus) < 2) or (len(animal_genus) > 30) or (not(animal_genus[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: название рода животного должно иметь длину от 2 до 30 символов (включительно), а его первая буква должна быть заглавной.")
    x = update_animal_genus(conn, animal_id, animal_genus)
    return Response("{'messgenus':'Родовая принадлежность животного обновлена.'}", status_code=200)

@router.post("/animals/update/species")
async def animals_post_update_species(animal_id: int, animal_species: str):
    conn = get_db_connection()
    if ((len(animal_species) < 2) or (len(animal_species) > 30) or (not(animal_species[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: название вида животного должно иметь длину от 2 до 30 символов (включительно), а его первая буква должна быть заглавной.")
    x = update_animal_species(conn, animal_id, animal_species)
    return Response("{'messspecies':'Видовая принадлежность животного обновлена.'}", status_code=200)

@router.post("/animals/update/picture")
async def animals_post_update_picture(animal_id: int, animal_picture: str):
    conn = get_db_connection()
    if (len(animal_picture) > 100000):
        raise HTTPException(status_code=400, detail="Ошибка: файл с картинкой животного не должен содержать более 100000 символов.")
    x = update_animal_picture(conn, animal_id, animal_picture)
    return Response("{'messpicture':'Картинка животного обновлена.'}", status_code=200)

