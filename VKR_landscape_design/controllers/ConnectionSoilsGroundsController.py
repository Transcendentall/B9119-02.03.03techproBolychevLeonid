from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter, Response
import json
from base_models import ConnectionSoilsGrounds
from models.connection_soils_grounds_model import *
from utils import get_db_connection
router = APIRouter()



@router.get("/connectionsoilsgrounds/all")
async def connection_soils_grounds_get_select_all():
    conn = get_db_connection()
    x = get_connection_soils_grounds(conn)
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.get("/connectionsoilsgrounds/one")
async def connection_soils_grounds_get_one(connection_soils_grounds_id: int):
    conn = get_db_connection()
    x = get_one_connection_soils_grounds(conn, connection_soils_grounds_id)
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.post("/connectionsoilsgrounds/insert")
async def connection_soils_grounds_post_insert(connection_soil_id: int, connection_ground_id: int):
    conn = get_db_connection()
    x = insert_connection_soils_grounds(conn, connection_soil_id, connection_ground_id)
    return Response("{'messinsert':'Связь между почвой и грунтом (какой грунт характерен для данной почвы) добавлена.'}", status_code=200)

@router.post("/connectionsoilsgrounds/delete")
async def connection_soils_grounds_post_delete(connection_soils_grounds_id: int):
    conn = get_db_connection()
    x = delete_connection_soils_grounds(conn, connection_soils_grounds_id)
    return Response("{'messdelete':'Связь между почвой и грунтом (какой грунт характерен для данной почвы) удалена.'}", status_code=200)

@router.post("/connectionsoilsgrounds/update/soilid")
async def connection_soils_grounds_post_update_soil_id(connection_soils_grounds_id: int, connection_soils_grounds_soil_id: int):
    conn = get_db_connection()
    x = update_connection_soils_grounds_soil_id(conn, connection_soils_grounds_id, connection_soils_grounds_soil_id)
    return Response("{'messsoilid':'ID почвы в связи между почвой и грунтом (какой грунт характерен для данной почвы) обновлён.'}", status_code=200)

@router.post("/connectionsoilsgrounds/update/groundid")
async def connection_soils_grounds_post_update_ground_id(connection_soils_grounds_id: int, connection_soils_grounds_ground_id: int):
    conn = get_db_connection()
    x = update_connection_soils_grounds_ground_id(conn, connection_soils_grounds_id, connection_soils_grounds_ground_id)
    return Response("{'messgroundid':'ID грунта в связи между почвой и грунтом (какой грунт характерен для данной почвы) обновлён.'}", status_code=200)
