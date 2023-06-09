from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter, Response, HTTPException
import json
from base_models import Soil
from models.soils_model import *
from utils import get_db_connection
router = APIRouter()



@router.get("/soils/all")
async def soils_get_select_all():
    conn = get_db_connection()
    x = get_soils(conn)
    return Response(json.dumps(x.to_dict(orient="records")).replace("NaN", "null"), status_code=200)

@router.get("/soils/one")
async def soils_get_one_soil(soil_id: int):
    """
      Описание: получение данных об одной почве по её ID (кроме картинки).
    """
    conn = get_db_connection()
    x = get_one_soil(conn, soil_id)
    if len(x) == 0:
        raise HTTPException(status_code=404, detail="Ошибка: почва с данным ID не найдена.")
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.get("/soils/bysoilgrounds")
async def soils_bysoil_grounds(soil_id: int):
    conn = get_db_connection()
    y = get_one_soil(conn, soil_id)
    if len(y) == 0:
        raise HTTPException(status_code=404, detail="Ошибка: почва с данным ID не найдена, потому получить перечень характерных для неё грунтов невозможно.")
    x = bysoil_grounds(conn, soil_id)
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.get("/soils/bysoilgroundsnoused")
async def soils_bysoil_grounds_noused(soil_id: int):
    conn = get_db_connection()
    y = get_one_soil(conn, soil_id)
    if len(y) == 0:
        raise HTTPException(status_code=404, detail="Ошибка: почва с данным ID не найдена, потому получить перечень нехарактерных для неё грунтов невозможно.")
    x = bysoil_grounds_noused(conn, soil_id)
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.get("/soils/bysoilplants")
async def soils_bysoil_plants(soil_id: int):
    conn = get_db_connection()
    y = get_one_soil(conn, soil_id)
    if len(y) == 0:
        raise HTTPException(status_code=404, detail="Ошибка: почва с данным ID не найдена, потому получить перечень хорошо и плохо растущих на ней растений невозможно.")
    x = bysoil_plants(conn, soil_id)
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.get("/soils/bysoilplantsnoused")
async def soils_bysoil_plants_noused(soil_id: int):
    conn = get_db_connection()
    y = get_one_soil(conn, soil_id)
    if len(y) == 0:
        raise HTTPException(status_code=404, detail="Ошибка: почва с данным ID не найдена, потому получить перечень нерастущих на ней растений невозможно.")
    x = bysoil_plants_noused(conn, soil_id)
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.post("/soils/delete")
async def soils_post_delete(soil_id: int):
    conn = get_db_connection()
    y = get_one_soil(conn, soil_id)
    if len(y) == 0:
        raise HTTPException(status_code=404, detail="Ошибка: почва с данным ID не найдена, потому удалить её невозможно.")
    x = delete_soil(conn, soil_id)
    return Response("{'messdelete':'Почва удалена.'}", status_code=200)

@router.post("/soils/insert")
async def soils_post_insert(soil_name: str, soil_description: str):
    conn = get_db_connection()
    if ((len(soil_name) < 2) or (len(soil_name) > 40) or (not(soil_name[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: название почвы должно иметь длину от 2 до 40 символов (включительно), а его первая буква должна быть заглавной.")
    if ((len(soil_description) < 2) or (len(soil_description) > 3000) or (not(soil_description[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: описание почвы должно иметь длину от 2 до 3000 символов (включительно), а его первая буква должна быть заглавной.")
    x = insert_soil(conn, soil_name, soil_description)
    return Response("{'messinsert':'Почва создана.'}", status_code=200)

@router.post("/soils/update/name")
async def soils_post_update_name(soil_id: int, soil_name: str):
    conn = get_db_connection()
    if ((len(soil_name) < 2) or (len(soil_name) > 40) or (not(soil_name[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: название почвы должно иметь длину от 2 до 40 символов (включительно), а его первая буква должна быть заглавной.")
    x = update_soil_name(conn, soil_id, soil_name)
    return Response("{'messname':'Название почвы обновлено.'}", status_code=200)

@router.post("/soils/update/description")
async def soils_post_update_description(soil_id: int, soil_description: str):
    conn = get_db_connection()
    if ((len(soil_description) < 2) or (len(soil_description) > 3000) or (not(soil_description[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: описание почвы должно иметь длину от 2 до 3000 символов (включительно), а его первая буква должна быть заглавной.")
    x = update_soil_description(conn, soil_id, soil_description)
    return Response("{'messdescription':'Описание почвы обновлено.'}", status_code=200)

@router.post("/soils/update/acidity")
async def soils_post_update_acidity(soil_id: int, soil_acidity: float):
    conn = get_db_connection()
    if ((soil_acidity <= 0) or (soil_acidity > 20)):
        raise HTTPException(status_code=400, detail="Ошибка: кислотность почвы в pH должна принадлежать полуинтервалу (0; 20].")
    x = update_soil_acidity(conn, soil_id, soil_acidity)
    return Response("{'messacidity':'Кислотность почвы в pH обновлена.'}", status_code=200)

@router.post("/soils/update/minerals")
async def soils_post_update_minerals(soil_id: int, soil_minerals: str):
    conn = get_db_connection()
    if ((len(soil_minerals) < 2) or (len(soil_minerals) > 500)):
        raise HTTPException(status_code=400, detail="Ошибка: минеральный состав почвы должен иметь длину от 2 до 500 символов (включительно).")
    x = update_soil_minerals(conn, soil_id, soil_minerals)
    return Response("{'messminerals':'Минеральный состав почвы обновлён.'}", status_code=200)

@router.post("/soils/update/profile")
async def soils_post_update_profile(soil_id: int, soil_profile: str):
    conn = get_db_connection()
    if ((len(soil_profile) < 2) or (len(soil_profile) > 250)):
        raise HTTPException(status_code=400, detail="Ошибка: профиль почвы должен иметь длину от 2 до 250 символов (включительно).")
    x = update_soil_profile(conn, soil_id, soil_profile)
    return Response("{'messprofile':'Профиль почвы обновлён.'}", status_code=200)

@router.post("/soils/update/picture")
async def soils_post_update_picture(soil: Soil.SoilPicture):
    """
      Описание: изменение картинки почвы.
    """
    conn = get_db_connection()
    x = update_soil_picture(conn, soil.soil_id, soil.soil_picture)
    return Response("{'messpicture':'Картинка почвы обновлена.'}", status_code=200)

@router.get("/soils/get/picture")
async def soils_get_picture(soil_id: int):
    """
      Описание: получение картинки почвы.
    """
    conn = get_db_connection()
    x = get_soil_picture(conn, soil_id)
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)