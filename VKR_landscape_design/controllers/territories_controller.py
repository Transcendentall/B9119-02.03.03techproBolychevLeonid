import json
from utils import get_db_connection
from flask import Blueprint, current_app, json, request
from models.territories_model import *
from docs.schemas.territorie_schema import *

blueprint_territorie = Blueprint(name="territorie", import_name=__name__)

@blueprint_territorie.route('/api/territories', methods=['GET'])
def territories_get_select_all():
    """
      ---
      get:
        summary: Получение всех территорий
        responses:
          '200':
            description: Получение списка всех территорий
            content:
              application/json:
                schema: TerritorieOutputSchema
        tags:
          - Territories
      """
    conn = get_db_connection()
    x = get_territories(conn)
    return json.dumps(x.to_dict(orient="records"))


@blueprint_territorie.route('/api/territories/delete', methods=['POST'])
def territories_post_delete():
    """
      ---
      post:
        summary: Удаление территории
        parameters:
          - in: query
            schema: TerritorieInputSchemaDelete
        responses:
          '200':
            description: Удаляет территорию по её ID
            content:
              application/json:
                schema: TerritorieOutputSchemaDelete
          '400':
            description: Не передан обязательный параметр
            content:
              application/json:
                schema: TerritorieErrorSchemaDelete
        tags:
          - Territories
      """
    conn = get_db_connection()
    x = delete_territorie(conn, request.get_json()['user_territorie_id'])
    return json.dumps({'message': "success"})

@blueprint_territorie.route('/api/territories/insert', methods=['POST'])
def territories_post_insert():
    """
      ---
      post:
        summary: Добавление территории
        parameters:
          - in: query
            schema: TerritorieInputSchemaInsert
        responses:
          '200':
            description: Территория добавлена
            content:
              application/json:
                schema: TerritorieOutputSchemaInsert
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: TerritorieErrorSchemaInsert
        tags:
          - Territories
      """
    conn = get_db_connection()
    x = insert_territorie(conn, request.get_json()['user_territorie_coord_x', 'user_territorie_coord_y', 'user_territorie_coord_z'])
    return json.dumps({'message': "success"})


@blueprint_territorie.route('/api/territories/update/coordx', methods=['POST'])
def territories_post_update_coord_x():
    """
      ---
      post:
        summary: Апдейт координаты X территории
        parameters:
          - in: query
            schema: TerritorieInputSchemaUpdateCoordX
        responses:
          '200':
            description: Изменяет координату X территории
            content:
              application/json:
                schema: TerritorieOutputSchemaUpdateCoordX
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: TerritorieErrorSchemaUpdateCoordX
        tags:
          - Territories
      """
    conn = get_db_connection()
    x = update_territorie_coord_x(conn, request.get_json()['user_territorie_id', 'user_territorie_coord_x'])
    return json.dumps({'message': "success"})


@blueprint_territorie.route('/api/territories/update/coordy', methods=['POST'])
def territories_post_update_coord_y():
    """
      ---
      post:
        summary: Апдейт координаты Y территории
        parameters:
          - in: query
            schema: TerritorieInputSchemaUpdateCoordY
        responses:
          '200':
            description: Изменяет координату Y территории
            content:
              application/json:
                schema: TerritorieOutputSchemaUpdateCoordY
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: TerritorieErrorSchemaUpdateCoordY
        tags:
          - Territories
      """
    conn = get_db_connection()
    x = update_territorie_coord_y(conn, request.get_json()['user_territorie_id', 'user_territorie_coord_y'])
    return json.dumps({'message': "success"})

@blueprint_territorie.route('/api/territories/update/coordz', methods=['POST'])
def territories_post_update_coord_z():
    """
      ---
      post:
        summary: Апдейт координаты Z территории
        parameters:
          - in: query
            schema: TerritorieInputSchemaUpdateCoordZ
        responses:
          '200':
            description: Изменяет координату Z территории
            content:
              application/json:
                schema: TerritorieOutputSchemaUpdateCoordZ
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: TerritorieErrorSchemaUpdateCoordZ
        tags:
          - Territories
      """
    conn = get_db_connection()
    x = update_territorie_coord_z(conn, request.get_json()['user_territorie_id', 'user_territorie_coord_z'])
    return json.dumps({'message': "success"})
