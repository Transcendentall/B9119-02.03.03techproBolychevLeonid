from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter, Response
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

@router.post("/territories/insert")
async def territories_post_insert(territorie_coord_x: float, territorie_coord_y: float, territorie_coord_z: float):
    conn = get_db_connection()
    x = insert_territorie(conn, territorie_coord_x, territorie_coord_y, territorie_coord_z)
    return Response("{'message':'Территория создана.'}", status_code=200)

@router.post("/territories/delete")
async def territories_post_delete(territorie_id: int):
    conn = get_db_connection()
    x = delete_territorie(conn, territorie_id)
    return Response("{'messname':'Территория удалена.'}", status_code=200)

@router.post("/territories/update/coord_x")
async def territories_post_update_coord_x(territorie_id: int, territorie_coord_x: str):
    conn = get_db_connection()
    x = update_territorie_coord_x(conn, territorie_id, territorie_coord_x)
    return Response("{'messname':'Координата x (широта) территории обновлена.'}", status_code=200)

@router.post("/territories/update/coord_y")
async def territories_post_update_coord_y(territorie_id: int, territorie_coord_y: str):
    conn = get_db_connection()
    x = update_territorie_coord_y(conn, territorie_id, territorie_coord_y)
    return Response("{'messname':'Координата y (долгота) территории обновлена.'}", status_code=200)

@router.post("/territories/update/coord_z")
async def territories_post_update_coord_z(territorie_id: int, territorie_coord_z: str):
    conn = get_db_connection()
    x = update_territorie_coord_z(conn, territorie_id, territorie_coord_z)
    return Response("{'messname':'Координата z (высота над уровнем моря в метрах) территории обновлена.'}", status_code=200)

