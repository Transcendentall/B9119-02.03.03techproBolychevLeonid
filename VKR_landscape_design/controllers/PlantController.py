from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter, Response
import json
from base_models import Plant
from models.plants_model import *
from utils import get_db_connection
router = APIRouter()



@router.get("/plants/all")
async def plants_get_select_all():
    conn = get_db_connection()
    x = get_plants(conn)
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.get("/plants/one")
async def plants_get_one_plant(plant_id: int):
    conn = get_db_connection()
    x = get_one_plant(conn, plant_id)
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.get("/plants/allisFodder")
async def plants_get_select_isFodder():
    conn = get_db_connection()
    x = get_plants_isFodder(conn)
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.get("/plants/allisNoFodder")
async def plants_get_select_isNoFodder():
    conn = get_db_connection()
    x = get_plants_isNoFodder(conn)
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.get("/plants/animalsforplant")
async def plants_get_animals_for_plant(plant_id: int):
    conn = get_db_connection()
    x = get_animals_for_plant(conn, plant_id)
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.post("/plants/delete")
async def plants_post_delete(plant_id: int):
    conn = get_db_connection()
    x = delete_plant(conn, plant_id)
    return Response("{'messdelete':'Растение удалёно.'}", status_code=200)

@router.post("/plants/insert")
async def plants_post_insert(plant_name: str, plant_description: str, plant_isFodder: bool):
    conn = get_db_connection()
    x = insert_plant(conn, plant_name, plant_description, plant_isFodder)
    return Response("{'messinsert':'Растение создано.'}", status_code=200)

@router.post("/plants/update/name")
async def plants_post_update_name(plant_id: int, plant_name: str):
    conn = get_db_connection()
    x = update_plant_name(conn, plant_id, plant_name)
    return Response("{'messname':'Название растения обновлено.'}", status_code=200)

@router.post("/plants/update/description")
async def plants_post_update_description(plant_id: int, plant_description: str):
    conn = get_db_connection()
    x = update_plant_description(conn, plant_id, plant_description)
    return Response("{'messdescription':'Описание растения обновлено.'}", status_code=200)

@router.post("/plants/update/isFodder")
async def plants_post_update_isFodder(plant_id: int, plant_isFodder: bool):
    conn = get_db_connection()
    x = update_plant_isFodder(conn, plant_id, plant_isFodder)
    return Response("{'messisFodder':'Обновлено, является ли растение кормовым.'}", status_code=200)

@router.post("/plants/update/isExactingToTheLight")
async def plants_post_update_isExactingToTheLight(plant_id: int, plant_isExactingToTheLight: bool):
    conn = get_db_connection()
    x = update_plant_isExactingToTheLight(conn, plant_id, plant_isExactingToTheLight)
    return Response("{'messisExactingToTheLight':'Обновлено, является ли растение требовательным к свету.'}", status_code=200)

@router.post("/plants/update/isOneYear")
async def plants_post_update_isOneYear(plant_id: int, plant_isOneYear: bool):
    conn = get_db_connection()
    x = update_plant_isOneYear(conn, plant_id, plant_isOneYear)
    return Response("{'messisOneYear':'Обновлено, является ли растение однолетним.'}", status_code=200)

@router.post("/plants/update/isTwoYears")
async def plants_post_update_isTwoYears(plant_id: int, plant_isTwoYears: bool):
    conn = get_db_connection()
    x = update_plant_isTwoYears(conn, plant_id, plant_isTwoYears)
    return Response("{'messisTwoYears':'Обновлено, является ли растение двухлетним.'}", status_code=200)

@router.post("/plants/update/isManyYears")
async def plants_post_update_isManyYears(plant_id: int, plant_isManyYears: bool):
    conn = get_db_connection()
    x = update_plant_isManyYears(conn, plant_id, plant_isManyYears)
    return Response("{'messisManyYears':'Обновлено, является ли растение многолетним.'}", status_code=200)

@router.post("/plants/update/climat")
async def plants_post_update_climat(plant_id: int, plant_climat: str):
    conn = get_db_connection()
    x = update_plant_climat(conn, plant_id, plant_climat)
    return Response("{'messclimat':'Подходящий для растения климат обновлён.'}", status_code=200)

@router.post("/plants/update/requiredmineralsandtraceelements")
async def plants_post_update_required_minerals_and_trace_elements(plant_id: int, plant_required_minerals_and_trace_elements: str):
    conn = get_db_connection()
    x = update_plant_required_minerals_and_trace_elements(conn, plant_id, plant_required_minerals_and_trace_elements)
    return Response("{'messrequiredmineralsandtraceelements':'Перечень требуемых для растения минералов и микроэлементов обновлён.'}", status_code=200)

@router.post("/plants/update/temperaturemin")
async def plants_post_update_temperature_min(plant_id: int, plant_temperature_min: int):
    conn = get_db_connection()
    x = update_plant_temperature_min(conn, plant_id, plant_temperature_min)
    return Response("{'messtemperaturemin':'Минимальная подходящая для растения температура обновлена.'}", status_code=200)

@router.post("/plants/update/temperaturemax")
async def plants_post_update_temperature_max(plant_id: int, plant_temperature_max: int):
    conn = get_db_connection()
    x = update_plant_temperature_max(conn, plant_id, plant_temperature_max)
    return Response("{'messtemperaturemax':'Максимальная подходящая для растения температура обновлена.'}", status_code=200)

@router.post("/plants/update/kingdom")
async def plants_post_update_kingdom(plant_id: int, plant_kingdom: str):
    conn = get_db_connection()
    x = update_plant_kingdom(conn, plant_id, plant_kingdom)
    return Response("{'messkingdom':'Царство растения обновлено.'}", status_code=200)

@router.post("/plants/update/philum")
async def plants_post_update_philum(plant_id: int, plant_philum: str):
    conn = get_db_connection()
    x = update_plant_philum(conn, plant_id, plant_philum)
    return Response("{'messphilum':'Тип растения обновлён.'}", status_code=200)

@router.post("/plants/update/class")
async def plants_post_update_class(plant_id: int, plant_class: str):
    conn = get_db_connection()
    x = update_plant_class(conn, plant_id, plant_class)
    return Response("{'messclass':'Класс растения обновлён.'}", status_code=200)

@router.post("/plants/update/order")
async def plants_post_update_order(plant_id: int, plant_order: str):
    conn = get_db_connection()
    x = update_plant_order(conn, plant_id, plant_order)
    return Response("{'messorder':'Порядок растения обновлён.'}", status_code=200)

@router.post("/plants/update/family")
async def plants_post_update_family(plant_id: int, plant_family: str):
    conn = get_db_connection()
    x = update_plant_family(conn, plant_id, plant_family)
    return Response("{'messfamily':'Семейство растения обновлено.'}", status_code=200)

@router.post("/plants/update/genus")
async def plants_post_update_genus(plant_id: int, plant_genus: str):
    conn = get_db_connection()
    x = update_plant_genus(conn, plant_id, plant_genus)
    return Response("{'messgenus':'Родовая принадлежность растения обновлена.'}", status_code=200)

@router.post("/plants/update/species")
async def plants_post_update_species(plant_id: int, plant_species: str):
    conn = get_db_connection()
    x = update_plant_species(conn, plant_id, plant_species)
    return Response("{'messspecies':'Видовая принадлежность растения обновлена.'}", status_code=200)

@router.post("/plants/update/picture")
async def plants_post_update_picture(plant_id: int, plant_picture: str):
    conn = get_db_connection()
    x = update_plant_picture(conn, plant_id, plant_picture)
    return Response("{'messpicture':'Картинка растения обновлена.'}", status_code=200)

