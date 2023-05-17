from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter, Response
import json
from base_models import Soil
from models.soils_model import *
from utils import get_db_connection
router = APIRouter()



@router.get("/soils/all")
async def soils_get_select_all():
    conn = get_db_connection()
    x = get_soils(conn)
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.post("/soils/delete")
async def soils_post_delete(soil_id: int):
    conn = get_db_connection()
    x = delete_soil(conn, soil_id)
    return Response("{'messname':'Почва удалена.'}", status_code=200)

@router.post("/soils/insert")
async def soils_post_insert(soil_name: str, soil_description: str):
    conn = get_db_connection()
    x = insert_soil(conn, soil_name, soil_description)
    return Response("{'message':'Почва создана.'}", status_code=200)

@router.post("/soils/update/name")
async def soils_post_update_name(soil_id: int, soil_name: str):
    conn = get_db_connection()
    x = update_soil_name(conn, soil_id, soil_name)
    return Response("{'messname':'Название почвы обновлено.'}", status_code=200)

@router.post("/soils/update/description")
async def soils_post_update_description(soil_id: int, soil_description: str):
    conn = get_db_connection()
    x = update_soil_description(conn, soil_id, soil_description)
    return Response("{'messdescription':'Описание почвы обновлено.'}", status_code=200)

@router.post("/soils/update/acidity")
async def soils_post_update_acidity(soil_id: int, soil_density: str):
    conn = get_db_connection()
    x = update_soil_acidity(conn, soil_id, soil_density)
    return Response("{'messacidity':'Кислотность почвы обновлена.'}", status_code=200)

@router.post("/soils/update/minerals")
async def soils_post_update_minerals(soil_id: int, soil_humidity: str):
    conn = get_db_connection()
    x = update_soil_minerals(conn, soil_id, soil_humidity)
    return Response("{'messminerals':'Минеральный состав почвы обновлён.'}", status_code=200)

@router.post("/soils/update/profile")
async def soils_post_update_profile(soil_id: int, soil_hardness_Moos: str):
    conn = get_db_connection()
    x = update_soil_profile(conn, soil_id, soil_hardness_Moos)
    return Response("{'messprofile':'Профиль почвы обновлён.'}", status_code=200)

@router.post("/soils/update/picture")
async def soils_post_update_picture(soil_id: int, soil_picture: str):
    conn = get_db_connection()
    x = update_soil_picture(conn, soil_id, soil_picture)
    return Response("{'messpicture':'Картинка почвы обновлена.'}", status_code=200)
