from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter, Response, HTTPException
import json
from base_models import Territorie
from models.territories_model import *
from utils import get_db_connection
router = APIRouter()



@router.get("/territories/all")
async def territories_get_select_all():
    conn = get_db_connection()
    x = get_territories(conn)
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.get("/territories/one")
async def territories_get_one_territorie(territorie_id: int):
    conn = get_db_connection()
    x = get_one_territorie(conn, territorie_id)
    if len(x) == 0:
        raise HTTPException(status_code=404, detail="Ошибка: территория с данным ID не найдена.")
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.get("/territories/bycoord")
async def territories_bycoord(territorie_coord_x: float, territorie_coord_y: float):
    conn = get_db_connection()
    x = bycoord(conn, territorie_coord_x, territorie_coord_y)
    if len(x) == 0:
        raise HTTPException(status_code=404, detail="Ошибка: в данном месте нет никаких почв.")
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.get("/territories/byterritoriesoil")
async def territories_byterritorie_soil(user_territorie_id: int):
    conn = get_db_connection()
    x = byterritorie_soil(conn, user_territorie_id)
    if len(x) == 0:
        raise HTTPException(status_code=404, detail="Ошибка: такой точки нет в базе данных.")
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.get("/territories/byterritorieground")
async def territories_byterritorie_ground(user_territorie_id: int):
    conn = get_db_connection()
    x = byterritorie_ground(conn, user_territorie_id)
    if len(x) == 0:
        raise HTTPException(status_code=404, detail="Ошибка: такой точки нет в базе данных.")
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.get("/territories/byterritorieanimal")
async def territories_byterritorie_animal(user_territorie_id: int):
    conn = get_db_connection()
    x = byterritorie_animal(conn, user_territorie_id)
    if len(x) == 0:
        raise HTTPException(status_code=404, detail="Ошибка: такой точки нет в базе данных.")
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.get("/territories/byterritorieplant")
async def territories_byterritorie_plant(user_territorie_id: int):
    conn = get_db_connection()
    x = byterritorie_plant(conn, user_territorie_id)
    if len(x) == 0:
        raise HTTPException(status_code=404, detail="Ошибка: такой точки нет в базе данных.")
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.post("/territories/insert")
async def territories_post_insert(territorie_coord_x: float, territorie_coord_y: float, territorie_address: str):
    conn = get_db_connection()
    if ((territorie_coord_x < -90) or (territorie_coord_x > 90)):
        raise HTTPException(status_code=400, detail="Ошибка: координата x (широта) точки должна принадлежать интервалу [-90; 90].")
    if ((territorie_coord_y <= -180) or (territorie_coord_y > 180)):
        raise HTTPException(status_code=400, detail="Ошибка: координата y (долгота) точки должна принадлежать полуинтервалу (-180; 180].")
    if (len(territorie_address) > 100):
        raise HTTPException(status_code=400, detail="Ошибка: адрес территории должен быть не длинее 100 символов.")
    x = insert_territorie(conn, territorie_coord_x, territorie_coord_y, territorie_address)
    return Response("{'messinsert':'Территория создана.'}", status_code=200)

@router.post("/territories/delete")
async def territories_post_delete(territorie_id: int):
    conn = get_db_connection()
    y = get_one_territorie(conn, territorie_id)
    if len(y) == 0:
        raise HTTPException(status_code=404, detail="Ошибка: территория с данным ID не найдена, потому удалить его невозможно.")
    x = delete_territorie(conn, territorie_id)
    return Response("{'messdelete':'Территория удалена.'}", status_code=200)

@router.post("/territories/update/coord_x")
async def territories_post_update_coord_x(territorie_id: int, territorie_coord_x: int):
    conn = get_db_connection()
    if ((territorie_coord_x < -90) or (territorie_coord_x > 90)):
        raise HTTPException(status_code=400, detail="Ошибка: координата x (широта) точки должна принадлежать интервалу [-90; 90].")
    x = update_territorie_coord_x(conn, territorie_id, territorie_coord_x)
    return Response("{'messcoordx':'Координата x (широта) территории обновлена.'}", status_code=200)

@router.post("/territories/update/coord_y")
async def territories_post_update_coord_y(territorie_id: int, territorie_coord_y: int):
    conn = get_db_connection()
    if ((territorie_coord_y <= -180) or (territorie_coord_y > 180)):
        raise HTTPException(status_code=400, detail="Ошибка: координата y (долгота) точки должна принадлежать полуинтервалу (-180; 180].")
    x = update_territorie_coord_y(conn, territorie_id, territorie_coord_y)
    return Response("{'messcoordy':'Координата y (долгота) территории обновлена.'}", status_code=200)


@router.post("/territories/update/address")
async def territories_post_update_address(territorie_id: int, territorie_address: str):
    conn = get_db_connection()
    if (len(territorie_address) > 100):
        raise HTTPException(status_code=400, detail="Ошибка: адрес территории должен быть не длинее 100 символов.")
    x = update_territorie_address(conn, territorie_id, territorie_address)
    return Response("{'messaddress':'Адрес территории обновлён.'}", status_code=200)


