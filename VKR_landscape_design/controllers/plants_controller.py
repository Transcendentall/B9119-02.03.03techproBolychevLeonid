import json
from utils import get_db_connection
from flask import Blueprint, current_app, json, request
from models.plants_model import *
from docs.schemas.plant_schema import *

blueprint_plant = Blueprint(name="plant", import_name=__name__)

@blueprint_plant.route('/api/plants', methods=['GET'])
def plants_get_select_all():
    """
      ---
      get:
        summary: Получение всех растений
        responses:
          '200':
            description: Получение списка всех растений
            content:
              application/json:
                schema: PlantOutputSchema
        tags:
          - Plants
      """
    conn = get_db_connection()
    x = get_plants(conn)
    return json.dumps(x.to_dict(orient="records"))


@blueprint_plant.route('/api/plants/isFodder', methods=['GET'])
def plants_get_select_all_isFodder():
    """
      ---
      get:
        summary: Получение всех кормовых растений
        responses:
          '200':
            description: Получение списка всех кормовых (т.е. пригодных для выпаса скота) растений
            content:
              application/json:
                schema: PlantOutputSchema
        tags:
          - Plants
      """
    conn = get_db_connection()
    x = get_plants_isFodder(conn)
    return json.dumps(x.to_dict(orient="records"))

@blueprint_plant.route('/api/plants/isNoFodder', methods=['GET'])
def plants_get_select_all_isNoFodder():
    """
      ---
      get:
        summary: Получение всех некормовых растений
        responses:
          '200':
            description: Получение списка всех некормовых (т.е. непригодных для выпаса скота) растений
            content:
              application/json:
                schema: PlantOutputSchema
        tags:
          - Plants
      """
    conn = get_db_connection()
    x = get_plants_isNoFodder(conn)
    return json.dumps(x.to_dict(orient="records"))


@blueprint_plant.route('/api/plants/delete', methods=['POST'])
def plants_post_delete():
    """
      ---
      post:
        summary: Удаление растения
        parameters:
          - in: query
            schema: PlantInputSchemaDelete
        responses:
          '200':
            description: Удаляет растение по его ID
            content:
              application/json:
                schema: PlantOutputSchemaDelete
          '400':
            description: Не передан обязательный параметр
            content:
              application/json:
                schema: PlantErrorSchemaDelete
        tags:
          - Plants
      """
    conn = get_db_connection()
    x = delete_plant(conn, request.get_json()['user_plant_id'])
    return json.dumps({'message': "success"})

@blueprint_plant.route('/api/plants/insert', methods=['POST'])
def plants_post_insert():
    """
      ---
      post:
        summary: Добавление растения
        parameters:
          - in: query
            schema: PlantInputSchemaInsert
        responses:
          '200':
            description: Растение добавлено
            content:
              application/json:
                schema: PlantOutputSchemaInsert
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: PlantErrorSchemaInsert
        tags:
          - Plants
      """
    conn = get_db_connection()
    x = insert_plant(conn, request.get_json()['user_plant_name', 'user_plant_description'])
    return json.dumps({'message': "success"})


@blueprint_plant.route('/api/plants/update/name', methods=['POST'])
def plants_post_update_name():
    """
      ---
      post:
        summary: Апдейт названия растения
        parameters:
          - in: query
            schema: PlantInputSchemaUpdateName
        responses:
          '200':
            description: Изменяет название растения
            content:
              application/json:
                schema: PlantOutputSchemaUpdateName
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: PlantErrorSchemaUpdateName
        tags:
          - Plants
      """
    conn = get_db_connection()
    x = update_plant_name(conn, request.get_json()['user_plant_id', 'user_plant_name'])
    return json.dumps({'message': "success"})


@blueprint_plant.route('/api/plants/update/description', methods=['POST'])
def plants_post_update_description():
    """
      ---
      post:
        summary: Апдейт описания растения
        parameters:
          - in: query
            schema: PlantInputSchemaUpdateDescription
        responses:
          '200':
            description: Изменяет описание растения
            content:
              application/json:
                schema: PlantOutputSchemaUpdateDescription
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: PlantErrorSchemaUpdateDescription
        tags:
          - Plants
      """
    conn = get_db_connection()
    x = update_plant_description(conn, request.get_json()['user_plant_id', 'user_plant_description'])
    return json.dumps({'message': "success"})

@blueprint_plant.route('/api/plants/update/isFodder', methods=['POST'])
def plants_post_update_isFodder():
    """
      ---
      post:
        summary: Апдейт кормовости растения
        parameters:
          - in: query
            schema: PlantInputSchemaUpdateIsFodder
        responses:
          '200':
            description: Изменяет, является ли растение кормовым
            content:
              application/json:
                schema: PlantOutputSchemaUpdateIsFodder
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: PlantErrorSchemaUpdateIsFodder
        tags:
          - Plants
      """
    conn = get_db_connection()
    x = update_plant_isFodder(conn, request.get_json()['user_plant_id', 'user_plant_isFodder'])
    return json.dumps({'message': "success"})

@blueprint_plant.route('/api/plants/update/isExactingToTheLight', methods=['POST'])
def plants_post_update_isExactingToTheLight():
    """
      ---
      post:
        summary: Апдейт требовательности к свету растения
        parameters:
          - in: query
            schema: PlantInputSchemaUpdateIsExactingToTheLight
        responses:
          '200':
            description: Изменяет требовательность к свету растения
            content:
              application/json:
                schema: PlantOutputSchemaUpdateIsExactingToTheLight
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: PlantErrorSchemaUpdateIsExactingToTheLight
        tags:
          - Plants
      """
    conn = get_db_connection()
    x = update_plant_isExactingToTheLight(conn, request.get_json()['user_plant_id', 'user_plant_isExactingToTheLight'])
    return json.dumps({'message': "success"})

@blueprint_plant.route('/api/plants/update/isOneYear', methods=['POST'])
def plants_post_update_isOneYear():
    """
      ---
      post:
        summary: Апдейт однолетнести растения
        parameters:
          - in: query
            schema: PlantInputSchemaUpdateIsOneYear
        responses:
          '200':
            description: Изменяет, является ли растение однолетним
            content:
              application/json:
                schema: PlantOutputSchemaUpdateIsOneYear
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: PlantErrorSchemaUpdateIsOneYear
        tags:
          - Plants
      """
    conn = get_db_connection()
    x = update_plant_isOneYear(conn, request.get_json()['user_plant_id', 'user_plant_isOneYear'])
    return json.dumps({'message': "success"})

@blueprint_plant.route('/api/plants/update/isTwoYears', methods=['POST'])
def plants_post_update_isTwoYears():
    """
      ---
      post:
        summary: Апдейт двухлетнести растения
        parameters:
          - in: query
            schema: PlantInputSchemaUpdateIsTwoYears
        responses:
          '200':
            description: Изменяет, является ли растение двухлетним
            content:
              application/json:
                schema: PlantOutputSchemaUpdateIsTwoYears
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: PlantErrorSchemaUpdateIsTwoYears
        tags:
          - Plants
      """
    conn = get_db_connection()
    x = update_plant_isTwoYears(conn, request.get_json()['user_plant_id', 'user_plant_isTwoYears'])
    return json.dumps({'message': "success"})

@blueprint_plant.route('/api/plants/update/isManyYears', methods=['POST'])
def plants_post_update_isManyYears():
    """
      ---
      post:
        summary: Апдейт многолетнести растения
        parameters:
          - in: query
            schema: PlantInputSchemaUpdateIsManyYears
        responses:
          '200':
            description: Изменяет, является ли растение многолетним
            content:
              application/json:
                schema: PlantOutputSchemaUpdateIsManyYears
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: PlantErrorSchemaUpdateIsManyYears
        tags:
          - Plants
      """
    conn = get_db_connection()
    x = update_plant_isManyYears(conn, request.get_json()['user_plant_id', 'user_plant_isManyYears'])
    return json.dumps({'message': "success"})


@blueprint_plant.route('/api/plants/update/climat', methods=['POST'])
def plants_post_update_climat():
    """
      ---
      post:
        summary: Апдейт названия растения
        parameters:
          - in: query
            schema: PlantInputSchemaUpdateClimat
        responses:
          '200':
            description: Изменяет название растения
            content:
              application/json:
                schema: PlantOutputSchemaUpdateClimat
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: PlantErrorSchemaUpdateClimat
        tags:
          - Plants
      """
    conn = get_db_connection()
    x = update_plant_climat(conn, request.get_json()['user_plant_id', 'user_plant_climat'])
    return json.dumps({'message': "success"})

@blueprint_plant.route('/api/plants/update/RequiredMineralsAndTraceElements', methods=['POST'])
def plants_post_update_required_minerals_and_trace_elements():
    """
      ---
      post:
        summary: Апдейт названия растения
        parameters:
          - in: query
            schema: PlantInputSchemaUpdateRequiredMineralsAndTraceElements
        responses:
          '200':
            description: Изменяет название растения
            content:
              application/json:
                schema: PlantOutputSchemaUpdateRequiredMineralsAndTraceElements
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: PlantErrorSchemaUpdateRequiredMineralsAndTraceElements
        tags:
          - Plants
      """
    conn = get_db_connection()
    x = update_plant_required_minerals_and_trace_elements(conn, request.get_json()['user_plant_id', 'user_plant_required_minerals_and_trace_elements'])
    return json.dumps({'message': "success"})

@blueprint_plant.route('/api/plants/update/kingdom', methods=['POST'])
def plants_post_update_kingdom():
    """
      ---
      post:
        summary: Апдейт царства растения
        parameters:
          - in: query
            schema: PlantInputSchemaUpdateKingdom
        responses:
          '200':
            description: Изменяет царство растения
            content:
              application/json:
                schema: PlantOutputSchemaUpdateKingdom
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: PlantErrorSchemaUpdateKingdom
        tags:
          - Plants
      """
    conn = get_db_connection()
    x = update_plant_kingdom(conn, request.get_json()['user_plant_id', 'user_plant_kingdom'])
    return json.dumps({'message': "success"})

@blueprint_plant.route('/api/plants/update/philum', methods=['POST'])
def plants_post_update_philum():
    """
      ---
      post:
        summary: Апдейт типа растения
        parameters:
          - in: query
            schema: PlantInputSchemaUpdatePhilum
        responses:
          '200':
            description: Изменяет тип растения
            content:
              application/json:
                schema: PlantOutputSchemaUpdatePhilum
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: PlantErrorSchemaUpdatePhilum
        tags:
          - Plants
      """
    conn = get_db_connection()
    x = update_plant_philum(conn, request.get_json()['user_plant_id', 'user_plant_philum'])
    return json.dumps({'message': "success"})

@blueprint_plant.route('/api/plants/update/class', methods=['POST'])
def plants_post_update_class():
    """
      ---
      post:
        summary: Апдейт класса растения
        parameters:
          - in: query
            schema: PlantInputSchemaUpdateClass
        responses:
          '200':
            description: Изменяет класс растения
            content:
              application/json:
                schema: PlantOutputSchemaUpdateClass
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: PlantErrorSchemaUpdateClass
        tags:
          - Plants
      """
    conn = get_db_connection()
    x = update_plant_class(conn, request.get_json()['user_plant_id', 'user_plant_class'])
    return json.dumps({'message': "success"})

@blueprint_plant.route('/api/plants/update/order', methods=['POST'])
def plants_post_update_order():
    """
      ---
      post:
        summary: Апдейт порядка растения
        parameters:
          - in: query
            schema: PlantInputSchemaUpdateOrder
        responses:
          '200':
            description: Изменяет порядок растения
            content:
              application/json:
                schema: PlantOutputSchemaUpdateOrder
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: PlantErrorSchemaUpdateOrder
        tags:
          - Plants
      """
    conn = get_db_connection()
    x = update_plant_order(conn, request.get_json()['user_plant_id', 'user_plant_order'])
    return json.dumps({'message': "success"})

@blueprint_plant.route('/api/plants/update/family', methods=['POST'])
def plants_post_update_family():
    """
      ---
      post:
        summary: Апдейт семейства растения
        parameters:
          - in: query
            schema: PlantInputSchemaUpdateFamily
        responses:
          '200':
            description: Изменяет семейство растения
            content:
              application/json:
                schema: PlantOutputSchemaUpdateFamily
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: PlantErrorSchemaUpdateFamily
        tags:
          - Plants
      """
    conn = get_db_connection()
    x = update_plant_family(conn, request.get_json()['user_plant_id', 'user_plant_family'])
    return json.dumps({'message': "success"})

@blueprint_plant.route('/api/plants/update/genus', methods=['POST'])
def plants_post_update_genus():
    """
      ---
      post:
        summary: Апдейт рода растения
        parameters:
          - in: query
            schema: PlantInputSchemaUpdateGenus
        responses:
          '200':
            description: Изменяет род растения
            content:
              application/json:
                schema: PlantOutputSchemaUpdateGenus
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: PlantErrorSchemaUpdateGenus
        tags:
          - Plants
      """
    conn = get_db_connection()
    x = update_plant_genus(conn, request.get_json()['user_plant_id', 'user_plant_genus'])
    return json.dumps({'message': "success"})

@blueprint_plant.route('/api/plants/update/species', methods=['POST'])
def plants_post_update_species():
    """
      ---
      post:
        summary: Апдейт вида растения
        parameters:
          - in: query
            schema: PlantInputSchemaUpdateSpecies
        responses:
          '200':
            description: Изменяет видовую принадлежность растения
            content:
              application/json:
                schema: PlantOutputSchemaUpdateSpecies
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: PlantErrorSchemaUpdateSpecies
        tags:
          - Plants
      """
    conn = get_db_connection()
    x = update_plant_species(conn, request.get_json()['user_plant_id', 'user_plant_species'])
    return json.dumps({'message': "success"})

@blueprint_plant.route('/api/plants/update/picture', methods=['POST'])
def plants_post_update_picture():
    """
      ---
      post:
        summary: Апдейт картинки растения
        parameters:
          - in: query
            schema: PlantInputSchemaUpdatePicture
        responses:
          '200':
            description: Изменяет картинку растения
            content:
              application/json:
                schema: PlantOutputSchemaUpdatePicture
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: PlantErrorSchemaUpdatePicture
        tags:
          - Plants
      """
    conn = get_db_connection()
    x = update_plant_picture(conn, request.get_json()['user_plant_id', 'user_plant_picture'])
    return json.dumps({'message': "success"})