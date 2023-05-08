import json
from utils import get_db_connection
from flask import Blueprint, current_app, json, request
from models.connection_plants_animals_model import *
from docs.schemas.connection_plants_animals_schema import *

blueprint_connection_plants_animals = Blueprint(name="connection_plants_animals", import_name=__name__)

@blueprint_connection_plants_animals.route('/api/connectionplantsanimals', methods=['GET'])
def connection_plants_animals_get_select_all():
    """
      ---
      get:
        summary: Получение всех связей между растениями и животными
        responses:
          '200':
            description: Получение списка, какие растения подходят для выпаса каких животных
            content:
              application/json:
                schema: ConnectionPlantsAnimalsOutputSchema
        tags:
          - СonnectionPlantsAnimals
      """


    conn = get_db_connection()
    x = get_connection_plants_animals(conn)
    return json.dumps(x.to_dict(orient="records"))

@blueprint_connection_plants_animals.route('/api/connectionplantsanimals/delete', methods=['POST'])
def connection_plants_animals_post_delete():
    """
      ---
      post:
        summary: Удаление связи между растением и животным
        parameters:
          - in: query
            schema: ConnectionPlantsAnimalsInputSchemaDelete
        responses:
          '200':
            description: Удаляет связь между растением и животным по её ID
            content:
              application/json:
                schema: ConnectionPlantsAnimalsOutputSchemaDelete
          '400':
            description: Не передан обязательный параметр
            content:
              application/json:
                schema: ConnectionPlantsAnimalsErrorSchemaDelete
        tags:
          - СonnectionPlantsAnimals
      """
    conn = get_db_connection()
    x = delete_connection_plants_animals(conn, request.get_json()['user_connection_plants_animals_id'])
    return json.dumps({'message': "success"})

@blueprint_connection_plants_animals.route('/api/connectionplantsanimals/insert', methods=['POST'])
def connection_plants_animals_post_insert():
    """
      ---
      post:
        summary: Добавление связи между растением и животным
        parameters:
          - in: query
            schema: ConnectionPlantsAnimalsInputSchemaInsert
        responses:
          '200':
            description: Добавляет связь, какое растение подходит для выпаса данного животного
            content:
              application/json:
                schema: ConnectionPlantsAnimalsOutputSchemaInsert
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: ConnectionPlantsAnimalsErrorSchemaInsert
        tags:
          - СonnectionPlantsAnimals
      """
    conn = get_db_connection()
    x = insert_connection_plants_animals(conn, request.get_json()['user_connection_plant_id', 'user_connection_animal_id'])
    return json.dumps({'message': "success"})


@blueprint_connection_plants_animals.route('/api/connectionplantsanimals/update/plantid', methods=['POST'])
def connection_plants_animals_post_update_plant_id():
    """
      ---
      post:
        summary: Апдейт ID растения в связи между растением и животным
        parameters:
          - in: query
            schema: ConnectionPlantsAnimalsInputSchemaUpdatePlantID
        responses:
          '200':
            description: Изменяет ID растения в конкретной связи между растением и животным (по ID этой связи)
            content:
              application/json:
                schema: ConnectionPlantsAnimalsOutputSchemaUpdatePlantID
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: ConnectionPlantsAnimalsErrorSchemaUpdatePlantID
        tags:
          - СonnectionPlantsAnimals
      """
    conn = get_db_connection()
    x = update_connection_plants_animals_plant_id(conn, request.get_json()['user_connection_plants_animals_id', 'user_connection_plant_id'])
    return json.dumps({'message': "success"})


@blueprint_connection_plants_animals.route('/api/connectionplantsanimals/update/animalid', methods=['POST'])
def connection_plants_animals_post_update_animal_id():
    """
      ---
      post:
        summary: Апдейт ID животного в связи между растением и животным
        parameters:
          - in: query
            schema: ConnectionPlantsAnimalsInputSchemaUpdateAnimalID
        responses:
          '200':
            description: Изменяет ID животного в конкретной связи между растением и животным (по ID этой связи)
            content:
              application/json:
                schema: ConnectionPlantsAnimalsOutputSchemaUpdateAnimalID
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: ConnectionPlantsAnimalsErrorSchemaUpdateAnimalID
        tags:
          - СonnectionPlantsAnimals
      """
    conn = get_db_connection()
    x = update_connection_plants_animals_animal_id(conn, request.get_json()['user_connection_plants_animals_id', 'user_connection_animal_id'])
    return json.dumps({'message': "success"})