from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter, Response, HTTPException
import json
from base_models import Ground
from models.grounds_model import *
from utils import get_db_connection
router = APIRouter()



@router.get("/grounds/all")
async def grounds_get_select_all():
    conn = get_db_connection()
    x = get_grounds(conn)
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.get("/grounds/one")
async def grounds_get_one_ground(ground_id: int):
    conn = get_db_connection()
    x = get_one_ground(conn, ground_id)
    if len(x) == 0:
        raise HTTPException(status_code=404, detail="Ошибка: грунт с данным ID не найден.")
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.post("/grounds/delete")
async def grounds_post_delete(ground_id: int):
    conn = get_db_connection()
    y = get_one_ground(conn, ground_id)
    if len(y) == 0:
        raise HTTPException(status_code=404, detail="Ошибка: грунт с данным ID не найден, потому удалить его невозможно.")
    x = delete_ground(conn, ground_id)
    return Response("{'messdelete':'Грунт удалён.'}", status_code=200)

@router.post("/grounds/insert")
async def grounds_post_insert(ground_name: str, ground_description: str):
    conn = get_db_connection()
    if ((len(ground_name) < 2) or (len(ground_name) > 30) or (not(ground_name[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: название грунта должно иметь длину от 2 до 30 символов (включительно), а его первая буква должна быть заглавной.")
    if ((len(ground_description) < 2) or (len(ground_description) > 3000) or (not(ground_description[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: описание грунта должно иметь длину от 2 до 3000 символов (включительно), а его первая буква должна быть заглавной.")
    x = insert_ground(conn, ground_name, ground_description)
    return Response("{'messinsert':'Грунт создан.'}", status_code=200)

@router.post("/grounds/update/name")
async def grounds_post_update_name(ground_id: int, ground_name: str):
    conn = get_db_connection()
    if ((len(ground_name) < 2) or (len(ground_name) > 30) or (not(ground_name[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: название грунта должно иметь длину от 2 до 30 символов (включительно), а его первая буква должна быть заглавной.")
    x = update_ground_name(conn, ground_id, ground_name)
    return Response("{'messname':'Название грунта обновлено.'}", status_code=200)

@router.post("/grounds/update/description")
async def grounds_post_update_description(ground_id: int, ground_description: str):
    conn = get_db_connection()
    if ((len(ground_description) < 2) or (len(ground_description) > 3000) or (not(ground_description[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: описание грунта должно иметь длину от 2 до 3000 символов (включительно), а его первая буква должна быть заглавной.")
    x = update_ground_description(conn, ground_id, ground_description)
    return Response("{'messdescription':'Описание грунта обновлено.'}", status_code=200)

@router.post("/grounds/update/density")
async def grounds_post_update_density(ground_id: int, ground_density: float):
    conn = get_db_connection()
    if ((ground_density <= 0) or (ground_density > 23)):
        raise HTTPException(status_code=400, detail="Ошибка: плотность грунта в г/см^3 должна принадлежать полуинтервалу (0; 23].")
    x = update_ground_density(conn, ground_id, ground_density)
    return Response("{'messdensity':'Плотность грунта в г/см^3 обновлена.'}", status_code=200)

@router.post("/grounds/update/humidity")
async def grounds_post_update_humidity(ground_id: int, ground_humidity: float):
    conn = get_db_connection()
    if ((ground_humidity <= 0) or (ground_humidity >= 100)):
        raise HTTPException(status_code=400, detail="Ошибка: относительная влажность грунта (в процентах) должна принадлежать отрезку (0; 100).")
    x = update_ground_humidity(conn, ground_id, ground_humidity)
    return Response("{'messhumidity':'Относительная влажность грунта (в процентах) обновлена.'}", status_code=200)

@router.post("/grounds/update/hardness_Moos")
async def grounds_post_update_hardness_Moos(ground_id: int, ground_hardness_Moos: int):
    conn = get_db_connection()
    if ((ground_hardness_Moos < 0) or (ground_hardness_Moos > 10)):
        raise HTTPException(status_code=400, detail="Ошибка: твёрдость грунта по шкале Мооса должна быть целым числом от 0 до 10 (включительно).")
    x = update_ground_hardness_Moos(conn, ground_id, ground_hardness_Moos)
    return Response("{'messhardness_Moos':'Твёрдость грунта по шкале Мооса обновлена.'}", status_code=200)

@router.post("/grounds/update/picture")
async def grounds_post_update_picture(ground_id: int, ground_picture: str):
    conn = get_db_connection()
    if (len(ground_picture) > 100000):
        raise HTTPException(status_code=400, detail="Ошибка: файл с картинкой грунта не должен содержать более 100000 символов.")
    x = update_ground_picture(conn, ground_id, ground_picture)
    return Response("{'messpicture':'Картинка грунта обновлена.'}", status_code=200)

