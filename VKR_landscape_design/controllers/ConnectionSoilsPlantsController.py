from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter, Response
import json
from base_models import ConnectionSoilsPlants
from models.connection_soils_plants_model import *
from utils import get_db_connection
router = APIRouter()



@router.get("/connectionsoilsplants/all")
async def connection_soils_plants_get_select_all():
    conn = get_db_connection()
    x = get_connection_soils_plants(conn)
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.get("/connectionsoilsplants/one")
async def connection_soils_plants_get_one(connection_soils_plants_id: int):
    conn = get_db_connection()
    x = get_one_connection_soils_plants(conn, connection_soils_plants_id)
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.post("/connectionsoilsplants/insert")
async def connection_soils_plants_post_insert(connection_soil_id: int, connection_plant_id: int, connection_soils_plants_isGood: bool):
    conn = get_db_connection()
    x = insert_connection_soils_plants(conn, connection_soil_id, connection_plant_id, connection_soils_plants_isGood)
    return Response("{'messinsert':'Связь между почвой и растением (какое растение как растёт на данной почве) добавлена.'}", status_code=200)

@router.post("/connectionsoilsplants/delete")
async def connection_soils_plants_post_delete(connection_soils_plants_id: int):
    conn = get_db_connection()
    x = delete_connection_soils_plants(conn, connection_soils_plants_id)
    return Response("{'messdelete':'Связь между почвой и растением (какое растение как растёт на данной почве) удалена.'}", status_code=200)

@router.post("/connectionsoilsplants/update/soilid")
async def connection_soils_plants_post_update_soil_id(connection_soils_plants_id: int, connection_soils_plants_soil_id: int):
    conn = get_db_connection()
    x = update_connection_soils_plants_soil_id(conn, connection_soils_plants_id, connection_soils_plants_soil_id)
    return Response("{'messsoilid':'ID почвы в связи между почвой и растением (какое растение как растёт на данной почве) обновлён.'}", status_code=200)

@router.post("/connectionsoilsplants/update/plantid")
async def connection_soils_plants_post_update_plant_id(connection_soils_plants_id: int, connection_soils_plants_plant_id: int):
    conn = get_db_connection()
    x = update_connection_soils_plants_plant_id(conn, connection_soils_plants_id, connection_soils_plants_plant_id)
    return Response("{'messplantid':'ID растения в связи между почвой и растением (какое растение как растёт на данной почве) обновлён.'}", status_code=200)

@router.post("/connectionsoilsplants/update/isGood")
async def connection_soils_plants_post_update_isGood(connection_soils_plants_id: int, connection_soils_plants_isGood: bool):
    conn = get_db_connection()
    x = update_connection_soils_plants_isGood(conn, connection_soils_plants_id, connection_soils_plants_isGood)
    return Response("{'messplantid':'Обновлено, хорошо ли растёт растение на почве в связи между почвой и растением (какое растение как растёт на данной почве).'}", status_code=200)
