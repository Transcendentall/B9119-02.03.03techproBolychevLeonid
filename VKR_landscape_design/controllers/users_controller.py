import json
from utils import get_db_connection
from flask import Blueprint, current_app, json, request
from models.users_model import get_users, delete_user

blueprint_user = Blueprint(name="user", import_name=__name__)

@blueprint_user.route('/api/users', methods=['GET'])
def selectallusers():
    """
      ---
      get:
        summary: Получение всех пользователей
        responses:
          '200':
            description: Получение списка всех пользователей
            content:
              application/json:
                schema: UserOutputSchema
        tags:
          - Users
      """
    conn = get_db_connection()
    x = get_users(conn)
    return json.dumps(x.to_dict(orient="records"))

@blueprint_user.route('/api/users/delete', methods=['POST'])
def deleteuser():
    """
      ---
      get:
        summary: Возводит число в степень
        parameters:
          - in: query
            schema: UserInputSchema
        responses:
          '200':
            description: Польхлваьедб удален
            content:
              application/json:
                schema: UserOutputSchema
          '400':
            description: Не передан обязательный параметр
            content:
              application/json:
                schema: UserErrorSchema
        tags:
          - Users
      """
    conn = get_db_connection()
    x = delete_user(conn, request.get_json()['user_user_id'])
    return json.dumps({'message': "success"})