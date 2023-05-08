import json
from utils import get_db_connection
from flask import Blueprint, current_app, json, request
from models.soils_model import *
from docs.schemas.soil_schema import *

blueprint_soil = Blueprint(name="soil", import_name=__name__)

@blueprint_soil.route('/api/soils', methods=['GET'])
def soils_get_select_all():
    """
      ---
      get:
        summary: Получение всех почв
        responses:
          '200':
            description: Получение списка всех почв
            content:
              application/json:
                schema: SoilOutputSchema
        tags:
          - Soils
      """
    conn = get_db_connection()
    x = get_soils(conn)
    return json.dumps(x.to_dict(orient="records"))


@blueprint_soil.route('/api/soils/delete', methods=['POST'])
def soils_post_delete():
    """
      ---
      post:
        summary: Удаление почвы
        parameters:
          - in: query
            schema: SoilInputSchemaDelete
        responses:
          '200':
            description: Удаляет почву по её ID
            content:
              application/json:
                schema: SoilOutputSchemaDelete
          '400':
            description: Не передан обязательный параметр
            content:
              application/json:
                schema: SoilErrorSchemaDelete
        tags:
          - Soils
      """
    conn = get_db_connection()
    x = delete_soil(conn, request.get_json()['user_soil_id'])
    return json.dumps({'message': "success"})

@blueprint_soil.route('/api/soils/insert', methods=['POST'])
def soils_post_insert():
    """
      ---
      post:
        summary: Добавление почвы
        parameters:
          - in: query
            schema: SoilInputSchemaInsert
        responses:
          '200':
            description: Добавляет почву
            content:
              application/json:
                schema: SoilOutputSchemaInsert
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: SoilErrorSchemaInsert
        tags:
          - Soils
      """
    conn = get_db_connection()
    x = insert_soil(conn, request.get_json()['user_soil_name', 'user_soil_description'])
    return json.dumps({'message': "success"})


@blueprint_soil.route('/api/soils/update/name', methods=['POST'])
def soils_post_update_name():
    """
      ---
      post:
        summary: Апдейт названия почвы
        parameters:
          - in: query
            schema: SoilInputSchemaUpdateName
        responses:
          '200':
            description: Изменяет название почвы
            content:
              application/json:
                schema: SoilOutputSchemaUpdateName
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: SoilErrorSchemaUpdateName
        tags:
          - Soils
      """
    conn = get_db_connection()
    x = update_soil_name(conn, request.get_json()['user_soil_id', 'user_soil_name'])
    return json.dumps({'message': "success"})


@blueprint_soil.route('/api/soils/update/description', methods=['POST'])
def soils_post_update_description():
    """
      ---
      post:
        summary: Апдейт описания почвы
        parameters:
          - in: query
            schema: SoilInputSchemaUpdateDescription
        responses:
          '200':
            description: Изменяет описание почвы
            content:
              application/json:
                schema: SoilOutputSchemaUpdateDescription
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: SoilErrorSchemaUpdateDescription
        tags:
          - Soils
      """
    conn = get_db_connection()
    x = update_soil_description(conn, request.get_json()['user_soil_id', 'user_soil_description'])
    return json.dumps({'message': "success"})

@blueprint_soil.route('/api/soils/update/acidity', methods=['POST'])
def soils_post_update_acidity():
    """
      ---
      post:
        summary: Апдейт кислотности почвы
        parameters:
          - in: query
            schema: SoilInputSchemaUpdateAcidity
        responses:
          '200':
            description: Изменяет кислотность почвы
            content:
              application/json:
                schema: SoilOutputSchemaUpdateAcidity
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: SoilErrorSchemaUpdateAcidity
        tags:
          - Soils
      """
    conn = get_db_connection()
    x = update_soil_acidity(conn, request.get_json()['user_soil_id', 'user_soil_acidity'])
    return json.dumps({'message': "success"})


@blueprint_soil.route('/api/soils/update/minerals', methods=['POST'])
def soils_post_update_minerals():
    """
      ---
      post:
        summary: Апдейт минерального состава почвы
        parameters:
          - in: query
            schema: SoilInputSchemaUpdateMinerals
        responses:
          '200':
            description: Изменяет минеральный состав почвы
            content:
              application/json:
                schema: SoilOutputSchemaUpdateMinerals
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: SoilErrorSchemaUpdateMinerals
        tags:
          - Soils
      """
    conn = get_db_connection()
    x = update_soil_minerals(conn, request.get_json()['user_soil_id', 'user_soil_minerals'])
    return json.dumps({'message': "success"})


@blueprint_soil.route('/api/soils/update/profile', methods=['POST'])
def soils_post_update_profile():
    """
      ---
      post:
        summary: Апдейт профиля почвы
        parameters:
          - in: query
            schema: SoilInputSchemaUpdateProfile
        responses:
          '200':
            description: Изменяет профиль почвы
            content:
              application/json:
                schema: SoilOutputSchemaUpdateProfile
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: SoilErrorSchemaUpdateProfile
        tags:
          - Soils
      """
    conn = get_db_connection()
    x = update_soil_profile(conn, request.get_json()['user_soil_id', 'user_soil_profile'])
    return json.dumps({'message': "success"})


@blueprint_soil.route('/api/soils/update/picture', methods=['POST'])
def soils_post_update_picture():
    """
      ---
      post:
        summary: Апдейт картинки почвы
        parameters:
          - in: query
            schema: SoilInputSchemaUpdatePicture
        responses:
          '200':
            description: Изменяет картинку почвы
            content:
              application/json:
                schema: SoilOutputSchemaUpdatePicture
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: SoilErrorSchemaUpdatePicture
        tags:
          - Soils
      """
    conn = get_db_connection()
    x = update_soil_picture(conn, request.get_json()['user_soil_id', 'user_soil_picture'])
    return json.dumps({'message': "success"})