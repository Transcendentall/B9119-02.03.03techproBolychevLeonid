import json
from utils import get_db_connection
from flask import Blueprint, current_app, json, request
from models.connection_soils_grounds_model import *
from docs.schemas.connection_soils_grounds_schema import *

blueprint_connection_soils_grounds = Blueprint(name="connection_soils_grounds", import_name=__name__)

@blueprint_connection_soils_grounds.route('/api/connectionsoilsgrounds', methods=['GET'])
def connection_soils_grounds_get_select_all():
    """
      ---
      get:
        summary: Получение всех связей между почвами и грунтами
        responses:
          '200':
            description: Получение списка, какие грунты встречаются на каких почвах
            content:
              application/json:
                schema: ConnectionSoilsGroundsOutputSchema
        tags:
          - СonnectionSoilsGrounds
      """


    conn = get_db_connection()
    x = get_connection_soils_grounds(conn)
    return json.dumps(x.to_dict(orient="records"))

@blueprint_connection_soils_grounds.route('/api/connectionsoilsgrounds/delete', methods=['POST'])
def connection_soils_grounds_post_delete():
    """
      ---
      post:
        summary: Удаление связи между почвой и грунтом
        parameters:
          - in: query
            schema: ConnectionSoilsGroundsInputSchemaDelete
        responses:
          '200':
            description: Удаляет связь между почвой и грунтом по её ID
            content:
              application/json:
                schema: ConnectionSoilsGroundsOutputSchemaDelete
          '400':
            description: Не передан обязательный параметр
            content:
              application/json:
                schema: ConnectionSoilsGroundsErrorSchemaDelete
        tags:
          - СonnectionSoilsGrounds
      """
    conn = get_db_connection()
    x = delete_connection_soils_grounds(conn, request.get_json()['user_connection_soils_grounds_id'])
    return json.dumps({'message': "success"})

@blueprint_connection_soils_grounds.route('/api/connectionsoilsgrounds/insert', methods=['POST'])
def connection_soils_grounds_post_insert():
    """
      ---
      post:
        summary: Добавление связи между почвой и грунтом
        parameters:
          - in: query
            schema: ConnectionSoilsGroundsInputSchemaInsert
        responses:
          '200':
            description: Добавляет связь, какой грунт встречается на данной почве
            content:
              application/json:
                schema: ConnectionSoilsGroundsOutputSchemaInsert
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: ConnectionSoilsGroundsErrorSchemaInsert
        tags:
          - СonnectionSoilsGrounds
      """
    conn = get_db_connection()
    x = insert_connection_soils_grounds(conn, request.get_json()['user_connection_soil_id', 'user_connection_ground_id'])
    return json.dumps({'message': "success"})


@blueprint_connection_soils_grounds.route('/api/connectionsoilsgrounds/update/soilid', methods=['POST'])
def connection_soils_grounds_post_update_soil_id():
    """
      ---
      post:
        summary: Апдейт ID почвы в связи между почвой и грунтом
        parameters:
          - in: query
            schema: ConnectionSoilsGroundsInputSchemaUpdateSoilID
        responses:
          '200':
            description: Изменяет ID почвы в конкретной связи между почвой и грунтом (по ID этой связи)
            content:
              application/json:
                schema: ConnectionSoilsGroundsOutputSchemaUpdateSoilID
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: ConnectionSoilsGroundsErrorSchemaUpdateSoilID
        tags:
          - СonnectionSoilsGrounds
      """
    conn = get_db_connection()
    x = update_connection_soils_grounds_soil_id(conn, request.get_json()['user_connection_soils_grounds_id', 'user_connection_soil_id'])
    return json.dumps({'message': "success"})


@blueprint_connection_soils_grounds.route('/api/connectionsoilsgrounds/update/groundid', methods=['POST'])
def connection_soils_grounds_post_update_ground_id():
    """
      ---
      post:
        summary: Апдейт ID грунта в связи между почвой и грунтом
        parameters:
          - in: query
            schema: ConnectionSoilsGroundsInputSchemaUpdateGroundID
        responses:
          '200':
            description: Изменяет ID грунта в конкретной связи между почвой и грунтом (по ID этой связи)
            content:
              application/json:
                schema: ConnectionSoilsGroundsOutputSchemaUpdateGroundID
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: ConnectionSoilsGroundsErrorSchemaUpdateGroundID
        tags:
          - СonnectionSoilsGrounds
      """
    conn = get_db_connection()
    x = update_connection_soils_grounds_ground_id(conn, request.get_json()['user_connection_soils_grounds_id', 'user_connection_ground_id'])
    return json.dumps({'message': "success"})