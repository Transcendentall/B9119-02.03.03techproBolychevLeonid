import json
from utils import get_db_connection
from flask import Blueprint, current_app, json, request
from models.connection_soils_plants_model import *
from docs.schemas.connection_soils_plants_schema import *

blueprint_connection_soils_plants = Blueprint(name="connection_soils_plants", import_name=__name__)

@blueprint_connection_soils_plants.route('/api/connectionsoilsplants', methods=['GET'])
def connection_soils_plants_get_select_all():
    """
      ---
      get:
        summary: Получение всех связей между почвами и растениями
        responses:
          '200':
            description: Получение списка, на каких почвах какие растения растут хорошо, а какие - плохо
            content:
              application/json:
                schema: ConnectionSoilsPlantsOutputSchema
        tags:
          - СonnectionSoilsPlants
      """


    conn = get_db_connection()
    x = get_connection_soils_plants(conn)
    return json.dumps(x.to_dict(orient="records"))

@blueprint_connection_soils_plants.route('/api/connectionsoilsplants/delete', methods=['POST'])
def connection_soils_plants_post_delete():
    """
      ---
      post:
        summary: Удаление связи между почвой и растением
        parameters:
          - in: query
            schema: ConnectionSoilsPlantsInputSchemaDelete
        responses:
          '200':
            description: Удаляет связь между почвой и растением по её ID
            content:
              application/json:
                schema: ConnectionSoilsPlantsOutputSchemaDelete
          '400':
            description: Не передан обязательный параметр
            content:
              application/json:
                schema: ConnectionSoilsPlantsErrorSchemaDelete
        tags:
          - СonnectionSoilsPlants
      """
    conn = get_db_connection()
    x = delete_connection_soils_plants(conn, request.get_json()['user_connection_soils_plants_id'])
    return json.dumps({'message': "success"})

@blueprint_connection_soils_plants.route('/api/connectionsoilsplants/insert', methods=['POST'])
def connection_soils_plants_post_insert():
    """
      ---
      post:
        summary: Добавление связи между почвой и растением
        parameters:
          - in: query
            schema: ConnectionSoilsPlantsInputSchemaInsert
        responses:
          '200':
            description: Добавляет связь между почвой и растением
            content:
              application/json:
                schema: ConnectionSoilsPlantsOutputSchemaInsert
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: ConnectionSoilsPlantsErrorSchemaInsert
        tags:
          - СonnectionSoilsPlants
      """
    conn = get_db_connection()
    x = insert_connection_soils_plants(conn, request.get_json()['user_connection_soil_id', 'user_connection_plant_id'])
    return json.dumps({'message': "success"})


@blueprint_connection_soils_plants.route('/api/connectionsoilsplants/update/soilid', methods=['POST'])
def connection_soils_plants_post_update_soil_id():
    """
      ---
      post:
        summary: Апдейт ID почвы в связи между почвой и растением
        parameters:
          - in: query
            schema: ConnectionSoilsPlantsInputSchemaUpdateSoilID
        responses:
          '200':
            description: Изменяет ID почвы в конкретной связи между почвой и растением (по ID этой связи)
            content:
              application/json:
                schema: ConnectionSoilsPlantsOutputSchemaUpdateSoilID
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: ConnectionSoilsPlantsErrorSchemaUpdateSoilID
        tags:
          - СonnectionSoilsPlants
      """
    conn = get_db_connection()
    x = update_connection_soils_plants_soil_id(conn, request.get_json()['user_connection_soils_plants_id', 'user_connection_soil_id'])
    return json.dumps({'message': "success"})


@blueprint_connection_soils_plants.route('/api/connectionsoilsplants/update/plantid', methods=['POST'])
def connection_soils_plants_post_update_plant_id():
    """
      ---
      post:
        summary: Апдейт ID растения в связи между почвой и растением
        parameters:
          - in: query
            schema: ConnectionSoilsPlantsInputSchemaUpdatePlantID
        responses:
          '200':
            description: Изменяет ID растения в конкретной связи между почвой и растением (по ID этой связи)
            content:
              application/json:
                schema: ConnectionSoilsPlantsOutputSchemaUpdatePlantID
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: ConnectionSoilsPlantsErrorSchemaUpdatePlantID
        tags:
          - СonnectionSoilsPlants
      """
    conn = get_db_connection()
    x = update_connection_soils_plants_plant_id(conn, request.get_json()['user_connection_soils_plants_id', 'user_connection_plant_id'])
    return json.dumps({'message': "success"})


@blueprint_connection_soils_plants.route('/api/connectionsoilsplants/update/isGood', methods=['POST'])
def connection_soils_plants_post_update_isGood():
    """
      ---
      post:
        summary: Апдейт, хорошо ли растёт растение на данной почве
        parameters:
          - in: query
            schema: ConnectionSoilsPlantsInputSchemaUpdateIsGood
        responses:
          '200':
            description: Изменяет то, хорошо (True) или плохо (False) растёт данное растение на данной почве
            content:
              application/json:
                schema: ConnectionSoilsPlantsOutputSchemaUpdateIsGood
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: ConnectionSoilsPlantsErrorSchemaUpdateIsGood
        tags:
          - СonnectionSoilsPlants
      """
    conn = get_db_connection()
    x = update_connection_soils_plants_isGood(conn, request.get_json()['user_connection_soils_plants_id', 'user_connection_soils_plants_isGood'])
    return json.dumps({'message': "success"})