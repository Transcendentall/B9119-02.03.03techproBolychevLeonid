import json
from utils import get_db_connection
from flask import Blueprint, current_app, json, request
from models.connection_territories_soils_model import *
from docs.schemas.connection_territories_soils_schema import *

blueprint_connection_territories_soils = Blueprint(name="connection_territories_soils", import_name=__name__)

@blueprint_connection_territories_soils.route('/api/connectionterritoriessoils', methods=['GET'])
def connection_territories_soils_get_select_all():
    """
      ---
      get:
        summary: Получение всех связей между территориями и почвами
        responses:
          '200':
            description: Получение списка, какие почвы встречаются на каких территориях
            content:
              application/json:
                schema: ConnectionTerritoriesSoilsOutputSchema
        tags:
          - СonnectionTerritoriesSoils
      """


    conn = get_db_connection()
    x = get_connection_territories_soils(conn)
    return json.dumps(x.to_dict(orient="records"))

@blueprint_connection_territories_soils.route('/api/connectionterritoriessoils/delete', methods=['POST'])
def connection_territories_soils_post_delete():
    """
      ---
      post:
        summary: Удаление связи между территориями и почвами
        parameters:
          - in: query
            schema: ConnectionTerritoriesSoilsInputSchemaDelete
        responses:
          '200':
            description: Удаляет связь между территорией и почвой по её ID
            content:
              application/json:
                schema: ConnectionTerritoriesSoilsOutputSchemaDelete
          '400':
            description: Не передан обязательный параметр
            content:
              application/json:
                schema: ConnectionTerritoriesSoilsErrorSchemaDelete
        tags:
          - СonnectionTerritoriesSoils
      """
    conn = get_db_connection()
    x = delete_connection_territories_soils(conn, request.get_json()['user_connection_territories_soils_id'])
    return json.dumps({'message': "success"})

@blueprint_connection_territories_soils.route('/api/connectionterritoriessoils/insert', methods=['POST'])
def connection_territories_soils_post_insert():
    """
      ---
      post:
        summary: Добавление связи между территорией и почвой
        parameters:
          - in: query
            schema: ConnectionTerritoriesSoilsInputSchemaInsert
        responses:
          '200':
            description: Добавляет связь, какая почва встречается на данной территории
            content:
              application/json:
                schema: ConnectionTerritoriesSoilsOutputSchemaInsert
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: ConnectionTerritoriesSoilsErrorSchemaInsert
        tags:
          - СonnectionTerritoriesSoils
      """
    conn = get_db_connection()
    x = insert_connection_territories_soils(conn, request.get_json()['user_connection_territorie_id', 'user_connection_soil_id'])
    return json.dumps({'message': "success"})


@blueprint_connection_territories_soils.route('/api/connectionterritoriessoils/update/territorieid', methods=['POST'])
def connection_territories_soils_post_update_territorie_id():
    """
      ---
      post:
        summary: Апдейт ID территории в связи между территорией и почвой
        parameters:
          - in: query
            schema: ConnectionTerritoriesSoilsInputSchemaUpdateTerritorieID
        responses:
          '200':
            description: Изменяет ID территории в конкретной связи между территорией и почвой (по ID этой связи)
            content:
              application/json:
                schema: ConnectionTerritoriesSoilsOutputSchemaUpdateTerritorieID
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: ConnectionTerritoriesSoilsErrorSchemaUpdateTerritorieID
        tags:
          - СonnectionTerritoriesSoils
      """
    conn = get_db_connection()
    x = update_connection_territories_soils_territorie_id(conn, request.get_json()['user_connection_territories_soils_id', 'user_connection_territorie_id'])
    return json.dumps({'message': "success"})


@blueprint_connection_territories_soils.route('/api/connectionterritoriessoils/update/soilid', methods=['POST'])
def connection_territories_soils_post_update_soil_id():
    """
      ---
      post:
        summary: Апдейт ID почвы в связи между территорией и почвой
        parameters:
          - in: query
            schema: ConnectionTerritoriesSoilsInputSchemaUpdateSoilID
        responses:
          '200':
            description: Изменяет ID почвы в конкретной связи между территорией и почвой (по ID этой связи)
            content:
              application/json:
                schema: ConnectionTerritoriesSoilsOutputSchemaUpdateSoilID
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: ConnectionTerritoriesSoilsErrorSchemaUpdateSoilID
        tags:
          - СonnectionTerritoriesSoils
      """
    conn = get_db_connection()
    x = update_connection_territories_soils_soil_id(conn, request.get_json()['user_connection_territories_soils_id', 'user_connection_soil_id'])
    return json.dumps({'message': "success"})