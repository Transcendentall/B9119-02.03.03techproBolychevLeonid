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

