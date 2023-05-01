import json
from utils import get_db_connection
from flask import Blueprint, current_app, json, request
from models.animals_model import *
from docs.schemas.animal_schema import *

blueprint_animal = Blueprint(name="animal", import_name=__name__)

@blueprint_animal.route('/api/animals', methods=['GET'])
def animals_get_select_all():
    """
      ---
      get:
        summary: Получение всех животных
        responses:
          '200':
            description: Получение списка всех животных
            content:
              application/json:
                schema: AnimalOutputSchema
        tags:
          - Animals
      """
    conn = get_db_connection()
    x = get_animals(conn)
    return json.dumps(x.to_dict(orient="records"))


@blueprint_animal.route('/api/animals/delete', methods=['POST'])
def animals_post_delete():
    """
      ---
      post:
        summary: Удаление животного
        parameters:
          - in: query
            schema: AnimalInputSchemaDelete
        responses:
          '200':
            description: Удаляет животное по его ID
            content:
              application/json:
                schema: AnimalOutputSchemaDelete
          '400':
            description: Не передан обязательный параметр
            content:
              application/json:
                schema: AnimalErrorSchemaDelete
        tags:
          - Animals
      """
    conn = get_db_connection()
    x = delete_animal(conn, request.get_json()['user_animal_id'])
    return json.dumps({'message': "success"})

@blueprint_animal.route('/api/animals/insert', methods=['POST'])
def animals_post_insert():
    """
      ---
      post:
        summary: Добавление животного
        parameters:
          - in: query
            schema: AnimalInputSchemaInsert
        responses:
          '200':
            description: Животное добавлена
            content:
              application/json:
                schema: AnimalOutputSchemaInsert
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: AnimalErrorSchemaInsert
        tags:
          - Animals
      """
    conn = get_db_connection()
    x = insert_animal(conn, request.get_json()['user_animal_name', 'user_animal_description'])
    return json.dumps({'message': "success"})


@blueprint_animal.route('/api/animals/update/name', methods=['POST'])
def animals_post_update_name():
    """
      ---
      post:
        summary: Апдейт названия животного
        parameters:
          - in: query
            schema: AnimalInputSchemaUpdateName
        responses:
          '200':
            description: Изменяет название животного
            content:
              application/json:
                schema: AnimalOutputSchemaUpdateName
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: AnimalErrorSchemaUpdateName
        tags:
          - Animals
      """
    conn = get_db_connection()
    x = update_animal_name(conn, request.get_json()['user_animal_id', 'user_animal_name'])
    return json.dumps({'message': "success"})


@blueprint_animal.route('/api/animals/update/description', methods=['POST'])
def animals_post_update_description():
    """
      ---
      post:
        summary: Апдейт описания животного
        parameters:
          - in: query
            schema: AnimalInputSchemaUpdateDescription
        responses:
          '200':
            description: Изменяет описание животного
            content:
              application/json:
                schema: AnimalOutputSchemaUpdateDescription
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: AnimalErrorSchemaUpdateDescription
        tags:
          - Animals
      """
    conn = get_db_connection()
    x = update_animal_description(conn, request.get_json()['user_animal_id', 'user_animal_description'])
    return json.dumps({'message': "success"})

