from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter, Response
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

@router.post("/grounds/delete")
async def grounds_post_delete(ground_id: int):
    conn = get_db_connection()
    x = delete_ground(conn, ground_id)
    return Response("{'messname':'Грунт удалён.'}", status_code=200)

@router.post("/grounds/insert")
async def grounds_post_insert(ground_name: str, ground_description: str):
    conn = get_db_connection()
    x = insert_ground(conn, ground_name, ground_description)
    return Response("{'message':'Грунт создан.'}", status_code=200)

@router.post("/grounds/update/name")
async def grounds_post_update_name(ground_id: int, ground_name: str):
    conn = get_db_connection()
    x = update_ground_name(conn, ground_id, ground_name)
    return Response("{'messname':'Название грунта обновлено.'}", status_code=200)

@router.post("/grounds/update/description")
async def grounds_post_update_description(ground_id: int, ground_description: str):
    conn = get_db_connection()
    x = update_ground_description(conn, ground_id, ground_description)
    return Response("{'messdescription':'Описание грунта обновлено.'}", status_code=200)

@router.post("/grounds/update/density")
async def grounds_post_update_density(ground_id: int, ground_density: str):
    conn = get_db_connection()
    x = update_ground_density(conn, ground_id, ground_density)
    return Response("{'messdensity':'Плотность грунта обновлена.'}", status_code=200)

@router.post("/grounds/update/humidity")
async def grounds_post_update_humidity(ground_id: int, ground_humidity: str):
    conn = get_db_connection()
    x = update_ground_humidity(conn, ground_id, ground_humidity)
    return Response("{'messhumidity':'Влажность грунта обновлена.'}", status_code=200)

@router.post("/grounds/update/hardness_Moos")
async def grounds_post_update_hardness_Moos(ground_id: int, ground_hardness_Moos: str):
    conn = get_db_connection()
    x = update_ground_hardness_Moos(conn, ground_id, ground_hardness_Moos)
    return Response("{'messhardness_Moos':'Твёрдость грунта по шкале Мооса обновлена.'}", status_code=200)

@router.post("/grounds/update/picture")
async def grounds_post_update_picture(ground_id: int, ground_picture: str):
    conn = get_db_connection()
    x = update_ground_picture(conn, ground_id, ground_picture)
    return Response("{'messpicture':'Картинка грунта обновлена.'}", status_code=200)

