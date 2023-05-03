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


@blueprint_animal.route('/api/animals/update/kingdom', methods=['POST'])
def animals_post_update_kingdom():
    """
      ---
      post:
        summary: Апдейт царства животного
        parameters:
          - in: query
            schema: AnimalInputSchemaUpdateKingdom
        responses:
          '200':
            description: Изменяет царство животного
            content:
              application/json:
                schema: AnimalOutputSchemaUpdateKingdom
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: AnimalErrorSchemaUpdateKingdom
        tags:
          - Animals
      """
    conn = get_db_connection()
    x = update_animal_kingdom(conn, request.get_json()['user_animal_id', 'user_animal_kingdom'])
    return json.dumps({'message': "success"})

@blueprint_animal.route('/api/animals/update/philum', methods=['POST'])
def animals_post_update_philum():
    """
      ---
      post:
        summary: Апдейт типа животного
        parameters:
          - in: query
            schema: AnimalInputSchemaUpdatePhilum
        responses:
          '200':
            description: Изменяет тип животного
            content:
              application/json:
                schema: AnimalOutputSchemaUpdatePhilum
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: AnimalErrorSchemaUpdatePhilum
        tags:
          - Animals
      """
    conn = get_db_connection()
    x = update_animal_philum(conn, request.get_json()['user_animal_id', 'user_animal_philum'])
    return json.dumps({'message': "success"})

@blueprint_animal.route('/api/animals/update/class', methods=['POST'])
def animals_post_update_class():
    """
      ---
      post:
        summary: Апдейт класса животного
        parameters:
          - in: query
            schema: AnimalInputSchemaUpdateClass
        responses:
          '200':
            description: Изменяет класс животного
            content:
              application/json:
                schema: AnimalOutputSchemaUpdateClass
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: AnimalErrorSchemaUpdateClass
        tags:
          - Animals
      """
    conn = get_db_connection()
    x = update_animal_class(conn, request.get_json()['user_animal_id', 'user_animal_class'])
    return json.dumps({'message': "success"})

@blueprint_animal.route('/api/animals/update/order', methods=['POST'])
def animals_post_update_order():
    """
      ---
      post:
        summary: Апдейт порядка животного
        parameters:
          - in: query
            schema: AnimalInputSchemaUpdateOrder
        responses:
          '200':
            description: Изменяет порядок животного
            content:
              application/json:
                schema: AnimalOutputSchemaUpdateOrder
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: AnimalErrorSchemaUpdateOrder
        tags:
          - Animals
      """
    conn = get_db_connection()
    x = update_animal_order(conn, request.get_json()['user_animal_id', 'user_animal_order'])
    return json.dumps({'message': "success"})

@blueprint_animal.route('/api/animals/update/family', methods=['POST'])
def animals_post_update_family():
    """
      ---
      post:
        summary: Апдейт семейства животного
        parameters:
          - in: query
            schema: AnimalInputSchemaUpdateFamily
        responses:
          '200':
            description: Изменяет семейство животного
            content:
              application/json:
                schema: AnimalOutputSchemaUpdateFamily
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: AnimalErrorSchemaUpdateFamily
        tags:
          - Animals
      """
    conn = get_db_connection()
    x = update_animal_family(conn, request.get_json()['user_animal_id', 'user_animal_family'])
    return json.dumps({'message': "success"})

@blueprint_animal.route('/api/animals/update/genus', methods=['POST'])
def animals_post_update_genus():
    """
      ---
      post:
        summary: Апдейт рода животного
        parameters:
          - in: query
            schema: AnimalInputSchemaUpdateGenus
        responses:
          '200':
            description: Изменяет род животного
            content:
              application/json:
                schema: AnimalOutputSchemaUpdateGenus
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: AnimalErrorSchemaUpdateGenus
        tags:
          - Animals
      """
    conn = get_db_connection()
    x = update_animal_genus(conn, request.get_json()['user_animal_id', 'user_animal_genus'])
    return json.dumps({'message': "success"})

@blueprint_animal.route('/api/animals/update/species', methods=['POST'])
def animals_post_update_species():
    """
      ---
      post:
        summary: Апдейт вида животного
        parameters:
          - in: query
            schema: AnimalInputSchemaUpdateSpecies
        responses:
          '200':
            description: Изменяет видовую принадлежность животного
            content:
              application/json:
                schema: AnimalOutputSchemaUpdateSpecies
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: AnimalErrorSchemaUpdateSpecies
        tags:
          - Animals
      """
    conn = get_db_connection()
    x = update_animal_species(conn, request.get_json()['user_animal_id', 'user_animal_species'])
    return json.dumps({'message': "success"})

@blueprint_animal.route('/api/animals/update/picture', methods=['POST'])
def animals_post_update_picture():
    """
      ---
      post:
        summary: Апдейт картинки животного
        parameters:
          - in: query
            schema: AnimalInputSchemaUpdatePicture
        responses:
          '200':
            description: Изменяет картинку животного
            content:
              application/json:
                schema: AnimalOutputSchemaUpdatePicture
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: AnimalErrorSchemaUpdatePicture
        tags:
          - Animals
      """
    conn = get_db_connection()
    x = update_animal_picture(conn, request.get_json()['user_animal_id', 'user_animal_picture'])
    return json.dumps({'message': "success"})
