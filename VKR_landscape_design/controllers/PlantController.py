from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter, Response, HTTPException
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
    """
      Описание: получение данных об одном растении по его ID (кроме картинки).
    """
    conn = get_db_connection()
    x = get_one_plant(conn, plant_id)
    if len(x) == 0:
        raise HTTPException(status_code=404, detail="Ошибка: растение с данным ID не найдено.")
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

@router.get("/plants/byplantanimals")
async def plants_byplant_animals(plant_id: int):
    conn = get_db_connection()
    y = get_one_plant(conn, plant_id)
    if len(y) == 0:
        raise HTTPException(status_code=404, detail="Ошибка: растение с данным ID не найдено, потому получить перечень животных, которые им питаются, невозможно.")
    x = byplant_animals(conn, plant_id)
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.get("/plants/byplantanimalsnoused")
async def plants_byplant_animals_noused(plant_id: int):
    conn = get_db_connection()
    y = get_one_plant(conn, plant_id)
    if len(y) == 0:
        raise HTTPException(status_code=404, detail="Ошибка: растение с данным ID не найдено, потому получить перечень животных, которые им не питаются, невозможно.")
    x = byplant_animals_noused(conn, plant_id)
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.post("/plants/delete")
async def plants_post_delete(plant_id: int):
    conn = get_db_connection()
    y = get_one_plant(conn, plant_id)
    if len(y) == 0:
        raise HTTPException(status_code=404, detail="Ошибка: растение с данным ID не найдено, потому удалить его невозможно.")
    x = delete_plant(conn, plant_id)
    return Response("{'messdelete':'Растение удалёно.'}", status_code=200)

@router.post("/plants/insert")
async def plants_post_insert(plant_name: str, plant_description: str, plant_isFodder: int):
    conn = get_db_connection()
    if ((len(plant_name) < 2) or (len(plant_name) > 50) or (not(plant_name[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: название грунта должно иметь длину от 2 до 50 символов (включительно), а его первая буква должна быть заглавной.")
    if ((len(plant_description) < 2) or (len(plant_description) > 3000) or (not(plant_description[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: описание грунта должно иметь длину от 2 до 3000 символов (включительно), а его первая буква должна быть заглавной.")
    x = insert_plant(conn, plant_name, plant_description, plant_isFodder)
    return Response("{'messinsert':'Растение создано.'}", status_code=200)

@router.post("/plants/update/name")
async def plants_post_update_name(plant_id: int, plant_name: str):
    conn = get_db_connection()
    if ((len(plant_name) < 2) or (len(plant_name) > 50) or (not(plant_name[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: название грунта должно иметь длину от 2 до 50 символов (включительно), а его первая буква должна быть заглавной.")
    x = update_plant_name(conn, plant_id, plant_name)
    return Response("{'messname':'Название растения обновлено.'}", status_code=200)

@router.post("/plants/update/description")
async def plants_post_update_description(plant_id: int, plant_description: str):
    conn = get_db_connection()
    if ((len(plant_description) < 2) or (len(plant_description) > 3000) or (not(plant_description[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: описание грунта должно иметь длину от 2 до 3000 символов (включительно), а его первая буква должна быть заглавной.")
    x = update_plant_description(conn, plant_id, plant_description)
    return Response("{'messdescription':'Описание растения обновлено.'}", status_code=200)

@router.post("/plants/update/isFodder")
async def plants_post_update_isFodder(plant_id: int, plant_isFodder: int):
    conn = get_db_connection()
    if ((plant_isFodder < 0) or (plant_isFodder > 1)):
        raise HTTPException(status_code=400, detail="Ошибка: растение может быть только или некормовым (0), или кормовым (1).")
    x = update_plant_isFodder(conn, plant_id, plant_isFodder)
    return Response("{'messisFodder':'Обновлено, является ли растение кормовым.'}", status_code=200)

@router.post("/plants/update/isExactingToTheLight")
async def plants_post_update_isExactingToTheLight(plant_id: int, plant_isExactingToTheLight: int):
    conn = get_db_connection()
    if ((plant_isExactingToTheLight < 0) or (plant_isExactingToTheLight > 1)):
        raise HTTPException(status_code=400, detail="Ошибка: растение может быть только или нетребовательным к свету (0), или требовательным к свету (1).")
    x = update_plant_isExactingToTheLight(conn, plant_id, plant_isExactingToTheLight)
    return Response("{'messisExactingToTheLight':'Обновлено, является ли растение требовательным к свету.'}", status_code=200)

@router.post("/plants/update/isOneYear")
async def plants_post_update_isOneYear(plant_id: int, plant_isOneYear: int):
    conn = get_db_connection()
    if ((plant_isOneYear < 0) or (plant_isOneYear > 1)):
        raise HTTPException(status_code=400, detail="Ошибка: растение может быть только или неоднолетним (0), или однолетним (1).")
    x = update_plant_isOneYear(conn, plant_id, plant_isOneYear)
    return Response("{'messisOneYear':'Обновлено, является ли растение однолетним.'}", status_code=200)

@router.post("/plants/update/isTwoYears")
async def plants_post_update_isTwoYears(plant_id: int, plant_isTwoYears: int):
    conn = get_db_connection()
    if ((plant_isTwoYears < 0) or (plant_isTwoYears > 1)):
        raise HTTPException(status_code=400, detail="Ошибка: растение может быть только или недвухлетним (0), или двухлетним (1).")
    x = update_plant_isTwoYears(conn, plant_id, plant_isTwoYears)
    return Response("{'messisTwoYears':'Обновлено, является ли растение двухлетним.'}", status_code=200)

@router.post("/plants/update/isManyYears")
async def plants_post_update_isManyYears(plant_id: int, plant_isManyYears: int):
    conn = get_db_connection()
    if ((plant_isManyYears < 0) or (plant_isManyYears > 1)):
        raise HTTPException(status_code=400, detail="Ошибка: растение может быть только или немноголетним (0), или многолетним (1).")
    x = update_plant_isManyYears(conn, plant_id, plant_isManyYears)
    return Response("{'messisManyYears':'Обновлено, является ли растение многолетним.'}", status_code=200)

@router.post("/plants/update/climat")
async def plants_post_update_climat(plant_id: int, plant_climat: str):
    conn = get_db_connection()
    if ((len(plant_climat) < 2) or (len(plant_climat) > 50)):
        raise HTTPException(status_code=400, detail="Ошибка: краткое описание подходящего для растения климата должно иметь длину от 2 до 50 символов (включительно).")
    x = update_plant_climat(conn, plant_id, plant_climat)
    return Response("{'messclimat':'Подходящий для растения климат обновлён.'}", status_code=200)

@router.post("/plants/update/requiredmineralsandtraceelements")
async def plants_post_update_required_minerals_and_trace_elements(plant_id: int, plant_required_minerals_and_trace_elements: str):
    conn = get_db_connection()
    if ((len(plant_required_minerals_and_trace_elements) < 2) or (len(plant_required_minerals_and_trace_elements) > 300)):
        raise HTTPException(status_code=400, detail="Ошибка: перечень требуемых для растения минералов и микроэлементов должен иметь длину от 2 до 300 символов (включительно).")
    x = update_plant_required_minerals_and_trace_elements(conn, plant_id, plant_required_minerals_and_trace_elements)
    return Response("{'messrequiredmineralsandtraceelements':'Перечень требуемых для растения минералов и микроэлементов обновлён.'}", status_code=200)

@router.post("/plants/update/temperaturemin")
async def plants_post_update_temperature_min(plant_id: int, plant_temperature_min: int):
    conn = get_db_connection()
    if ((plant_temperature_min < -100) or (plant_temperature_min > 100)):
        raise HTTPException(status_code=400, detail="Ошибка: минимальная подходящая для растения температура должна принадлежать интервалу [-100; 100].")
    y = check_one_plants_temperature_min_max_min(conn, plant_id, plant_temperature_min)
    if len(y) == 0:
        raise HTTPException(status_code=400, detail="Ошибка: минимальная подходящая для растения температура всегда должна быть меньше или равна максимальной.")
    x = update_plant_temperature_min(conn, plant_id, plant_temperature_min)
    return Response("{'messtemperaturemin':'Минимальная подходящая для растения температура обновлена.'}", status_code=200)

@router.post("/plants/update/temperaturemax")
async def plants_post_update_temperature_max(plant_id: int, plant_temperature_max: int):
    conn = get_db_connection()
    if ((plant_temperature_max < -100) or (plant_temperature_max > 100)):
        raise HTTPException(status_code=400, detail="Ошибка: максимальная подходящая для растения температура должна принадлежать интервалу [-100; 100].")
    y = check_one_plants_temperature_min_max_max(conn, plant_id, plant_temperature_max)
    if len(y) == 0:
        raise HTTPException(status_code=400, detail="Ошибка: максимальная подходящая для растения температура всегда должна быть больше или равна минимальной.")
    x = update_plant_temperature_max(conn, plant_id, plant_temperature_max)
    return Response("{'messtemperaturemax':'Максимальная подходящая для растения температура обновлена.'}", status_code=200)

@router.post("/plants/update/kingdom")
async def plants_post_update_kingdom(plant_id: int, plant_kingdom: str):
    conn = get_db_connection()
    if ((len(plant_kingdom) < 2) or (len(plant_kingdom) > 30) or (not(plant_kingdom[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: название царства растения должно иметь длину от 2 до 30 символов (включительно), а его первая буква должна быть заглавной.")
    x = update_plant_kingdom(conn, plant_id, plant_kingdom)
    return Response("{'messkingdom':'Царство растения обновлено.'}", status_code=200)

@router.post("/plants/update/philum")
async def plants_post_update_philum(plant_id: int, plant_philum: str):
    conn = get_db_connection()
    if ((len(plant_philum) < 2) or (len(plant_philum) > 30) or (not(plant_philum[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: название типа растения должно иметь длину от 2 до 30 символов (включительно), а его первая буква должна быть заглавной.")
    x = update_plant_philum(conn, plant_id, plant_philum)
    return Response("{'messphilum':'Тип растения обновлён.'}", status_code=200)

@router.post("/plants/update/class")
async def plants_post_update_class(plant_id: int, plant_class: str):
    if ((len(plant_class) < 2) or (len(plant_class) > 30) or (not(plant_class[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: название класса растения должно иметь длину от 2 до 30 символов (включительно), а его первая буква должна быть заглавной.")
    conn = get_db_connection()
    x = update_plant_class(conn, plant_id, plant_class)
    return Response("{'messclass':'Класс растения обновлён.'}", status_code=200)

@router.post("/plants/update/order")
async def plants_post_update_order(plant_id: int, plant_order: str):
    conn = get_db_connection()
    if ((len(plant_order) < 2) or (len(plant_order) > 30) or (not(plant_order[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: название порядка растения должно иметь длину от 2 до 30 символов (включительно), а его первая буква должна быть заглавной.")
    x = update_plant_order(conn, plant_id, plant_order)
    return Response("{'messorder':'Порядок растения обновлён.'}", status_code=200)

@router.post("/plants/update/family")
async def plants_post_update_family(plant_id: int, plant_family: str):
    conn = get_db_connection()
    if ((len(plant_family) < 2) or (len(plant_family) > 30) or (not(plant_family[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: название семейства растения должно иметь длину от 2 до 30 символов (включительно), а его первая буква должна быть заглавной.")
    x = update_plant_family(conn, plant_id, plant_family)
    return Response("{'messfamily':'Семейство растения обновлено.'}", status_code=200)

@router.post("/plants/update/genus")
async def plants_post_update_genus(plant_id: int, plant_genus: str):
    conn = get_db_connection()
    if ((len(plant_genus) < 2) or (len(plant_genus) > 30) or (not(plant_genus[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: название рода растения должно иметь длину от 2 до 30 символов (включительно), а его первая буква должна быть заглавной.")
    x = update_plant_genus(conn, plant_id, plant_genus)
    return Response("{'messgenus':'Родовая принадлежность растения обновлена.'}", status_code=200)

@router.post("/plants/update/species")
async def plants_post_update_species(plant_id: int, plant_species: str):
    conn = get_db_connection()
    if ((len(plant_species) < 2) or (len(plant_species) > 30) or (not(plant_species[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: название вида растения должно иметь длину от 2 до 30 символов (включительно), а его первая буква должна быть заглавной.")
    x = update_plant_species(conn, plant_id, plant_species)
    return Response("{'messspecies':'Видовая принадлежность растения обновлена.'}", status_code=200)

@router.post("/plants/update/picture")
async def plants_post_update_picture(plant: Plant.PlantPicture):
    """
      Описание: изменение картинки растения.
    """
    conn = get_db_connection()
    x = update_plant_picture(conn, plant.plant_id, plant.plant_picture)
    return Response("{'messpicture':'Картинка растения обновлена.'}", status_code=200)

@router.get("/plants/get/picture")
async def plants_get_picture(plant_id: int):
    """
      Описание: получение картинки растения.
    """
    conn = get_db_connection()
    x = get_plant_picture(conn, plant_id)
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)
