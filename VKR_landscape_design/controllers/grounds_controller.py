import json
from utils import get_db_connection
from flask import Blueprint, current_app, json, request
from models.grounds_model import *
from docs.schemas.ground_schema import *

blueprint_ground = Blueprint(name="ground", import_name=__name__)

@blueprint_ground.route('/api/grounds', methods=['GET'])
def grounds_get_select_all():
    """
      ---
      get:
        summary: Получение всех грунтов
        responses:
          '200':
            description: Получение списка всех грунтов
            content:
              application/json:
                schema: GroundOutputSchema
        tags:
          - Grounds
      """
    conn = get_db_connection()
    x = get_grounds(conn)
    return json.dumps(x.to_dict(orient="records"))


@blueprint_ground.route('/api/grounds/delete', methods=['POST'])
def grounds_post_delete():
    """
      ---
      post:
        summary: Удаление грунта
        parameters:
          - in: query
            schema: GroundInputSchemaDelete
        responses:
          '200':
            description: Удаляет грунт по его ID
            content:
              application/json:
                schema: GroundOutputSchemaDelete
          '400':
            description: Не передан обязательный параметр
            content:
              application/json:
                schema: GroundErrorSchemaDelete
        tags:
          - Grounds
      """
    conn = get_db_connection()
    x = delete_ground(conn, request.get_json()['user_ground_id'])
    return json.dumps({'message': "success"})

@blueprint_ground.route('/api/grounds/insert', methods=['POST'])
def grounds_post_insert():
    """
      ---
      post:
        summary: Добавление грунта
        parameters:
          - in: query
            schema: GroundInputSchemaInsert
        responses:
          '200':
            description: Грунт добавлен
            content:
              application/json:
                schema: GroundOutputSchemaInsert
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: GroundErrorSchemaInsert
        tags:
          - Grounds
      """
    conn = get_db_connection()
    x = insert_ground(conn, request.get_json()['user_ground_name', 'user_ground_description'])
    return json.dumps({'message': "success"})


@blueprint_ground.route('/api/grounds/update/name', methods=['POST'])
def grounds_post_update_name():
    """
      ---
      post:
        summary: Апдейт названия грунта
        parameters:
          - in: query
            schema: GroundInputSchemaUpdateName
        responses:
          '200':
            description: Изменяет название грунта
            content:
              application/json:
                schema: GroundOutputSchemaUpdateName
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: GroundErrorSchemaUpdateName
        tags:
          - Grounds
      """
    conn = get_db_connection()
    x = update_ground_name(conn, request.get_json()['user_ground_id', 'user_ground_name'])
    return json.dumps({'message': "success"})


@blueprint_ground.route('/api/grounds/update/description', methods=['POST'])
def grounds_post_update_description():
    """
      ---
      post:
        summary: Апдейт описания грунта
        parameters:
          - in: query
            schema: GroundInputSchemaUpdateDescription
        responses:
          '200':
            description: Изменяет описание грунта
            content:
              application/json:
                schema: GroundOutputSchemaUpdateDescription
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: GroundErrorSchemaUpdateDescription
        tags:
          - Grounds
      """
    conn = get_db_connection()
    x = update_ground_description(conn, request.get_json()['user_ground_id', 'user_ground_description'])
    return json.dumps({'message': "success"})

@blueprint_ground.route('/api/grounds/update/density', methods=['POST'])
def grounds_post_update_density():
    """
      ---
      post:
        summary: Апдейт плотности грунта
        parameters:
          - in: query
            schema: GroundInputSchemaUpdateDensity
        responses:
          '200':
            description: Изменяет плотность грунта
            content:
              application/json:
                schema: GroundOutputSchemaUpdateDensity
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: GroundErrorSchemaUpdateDensity
        tags:
          - Grounds
      """
    conn = get_db_connection()
    x = update_ground_density(conn, request.get_json()['user_ground_id', 'user_ground_density'])
    return json.dumps({'message': "success"})


@blueprint_ground.route('/api/grounds/update/humidity', methods=['POST'])
def grounds_post_update_humidity():
    """
      ---
      post:
        summary: Апдейт влажности грунта
        parameters:
          - in: query
            schema: GroundInputSchemaUpdateHumidity
        responses:
          '200':
            description: Изменяет влажность грунта
            content:
              application/json:
                schema: GroundOutputSchemaUpdateHumidity
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: GroundErrorSchemaUpdateHumidity
        tags:
          - Grounds
      """
    conn = get_db_connection()
    x = update_ground_humidity(conn, request.get_json()['user_ground_id', 'user_ground_humidity'])
    return json.dumps({'message': "success"})


@blueprint_ground.route('/api/grounds/update/hardnessMoos', methods=['POST'])
def grounds_post_update_hardness_Moos():
    """
      ---
      post:
        summary: Апдейт твёрдости грунта по Моосу
        parameters:
          - in: query
            schema: GroundInputSchemaUpdateHardnessMoos
        responses:
          '200':
            description: Изменяет твёрдость грунта по шкале Мооса
            content:
              application/json:
                schema: GroundOutputSchemaUpdateHardnessMoos
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: GroundErrorSchemaUpdateHardnessMoos
        tags:
          - Grounds
      """
    conn = get_db_connection()
    x = update_ground_hardness_Moos(conn, request.get_json()['user_ground_id', 'user_ground_hardness_Moos'])
    return json.dumps({'message': "success"})


@blueprint_ground.route('/api/grounds/update/picture', methods=['POST'])
def grounds_post_update_picture():
    """
      ---
      post:
        summary: Апдейт картинки грунта
        parameters:
          - in: query
            schema: GroundInputSchemaUpdatePicture
        responses:
          '200':
            description: Изменяет картинку грунта
            content:
              application/json:
                schema: GroundOutputSchemaUpdatePicture
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: GroundErrorSchemaUpdatePicture
        tags:
          - Grounds
      """
    conn = get_db_connection()
    x = update_ground_picture(conn, request.get_json()['user_ground_id', 'user_ground_picture'])
    return json.dumps({'message': "success"})
