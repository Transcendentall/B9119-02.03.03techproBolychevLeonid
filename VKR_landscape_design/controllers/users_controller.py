import json
from utils import get_db_connection
from flask import Blueprint, current_app, json, request
from models.users_model import *
from docs.schemas.user_schema import *

blueprint_user = Blueprint(name="user", import_name=__name__)

@blueprint_user.route('/api/users', methods=['GET'])
def users_get_select_all():
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


@blueprint_user.route('/api/users/withoutpassword', methods=['GET'])
def users_get_select_all_without_password():
    """
      ---
      get:
        summary: Получение всех пользователей без паролей
        responses:
          '200':
            description: Получение списка всех пользователей без паролей
            content:
              application/json:
                schema: UserOutputSchema
        tags:
          - Users
      """
    conn = get_db_connection()
    x = get_users_without_password(conn)
    return json.dumps(x.to_dict(orient="records"))

@blueprint_user.route('/api/users/withoutpasswordadmins', methods=['GET'])
def users_get_select_all_without_password_admins():
    """
      ---
      get:
        summary: Получение всех администраторов без паролей
        responses:
          '200':
            description: Получение списка всех администраторов без паролей
            content:
              application/json:
                schema: UserOutputSchema
        tags:
          - Users
      """
    conn = get_db_connection()
    x = get_users_without_password_admins(conn)
    return json.dumps(x.to_dict(orient="records"))


@blueprint_user.route('/api/users/withoutpasswordnoadmins', methods=['GET'])
def users_get_select_all_without_password_noadmins():
    """
      ---
      get:
        summary: Получение всех пользователей, не являющихся администраторами, без паролей
        responses:
          '200':
            description: Получение списка всех, не являющихся администраторами, без паролей
            content:
              application/json:
                schema: UserOutputSchema
        tags:
          - Users
      """
    conn = get_db_connection()
    x = get_users_without_password_noadmins(conn)
    return json.dumps(x.to_dict(orient="records"))


@blueprint_user.route('/api/users/delete', methods=['POST'])
def users_post_delete():
    """
      ---
      post:
        summary: Удаление пользователя
        parameters:
          - in: body
            schema: UserInputSchemaDelete
        responses:
          '200':
            description: Удаляет пользователя по его ID
            content:
              application/json:
                schema: UserOutputSchemaDelete
          '400':
            description: Не передан обязательный параметр
            content:
              application/json:
                schema: UserErrorSchemaDelete
        tags:
          - Users
      """
    conn = get_db_connection()
    x = delete_user(conn, request.get_json()['user_id'])
    return json.dumps({'message': "success"})


@blueprint_user.route('/api/users/insert', methods=['POST'])
def users_post_insert():
    """
      ---
      post:
        summary: Добавление пользователя
        parameters:
          - in: query
            schema: UserInputSchemaInsert
        responses:
          '200':
            description: Добавляет пользователя
            content:
              application/json:
                schema: UserOutputSchemaInsert
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: UserErrorSchemaInsert
        tags:
          - Users
      """
    conn = get_db_connection()
    x = insert_user(conn, request.get_json()['user_user_login', 'user_user_password', 'user_user_email'])
    return json.dumps({'message': "success"})


@blueprint_user.route('/api/users/update/login', methods=['POST'])
def users_post_update_login():
    """
      ---
      post:
        summary: Апдейт логина пользователя
        parameters:
          - in: query
            schema: UserInputSchemaUpdateLogin
        responses:
          '200':
            description: Изменяет логин пользователя
            content:
              application/json:
                schema: UserOutputSchemaUpdateLogin
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: UserErrorSchemaUpdateLogin
        tags:
          - Users
      """
    conn = get_db_connection()
    x = update_user_login(conn, request.get_json()['user_user_id', 'user_user_login'])
    return json.dumps({'message': "success"})


@blueprint_user.route('/api/users/update/password', methods=['POST'])
def users_post_update_password():
    """
      ---
      post:
        summary: Апдейт пароля пользователя
        parameters:
          - in: query
            schema: UserInputSchemaUpdatePassword
        responses:
          '200':
            description: Изменяет пароль пользователя
            content:
              application/json:
                schema: UserOutputSchemaUpdatePassword
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: UserErrorSchemaUpdatePassword
        tags:
          - Users
      """
    conn = get_db_connection()
    x = update_user_password(conn, request.get_json()['user_user_id', 'user_user_password'])
    return json.dumps({'message': "success"})

@blueprint_user.route('/api/users/update/email', methods=['POST'])
def users_post_update_email():
    """
      ---
      post:
        summary: Апдейт электронной почты пользователя
        parameters:
          - in: query
            schema: UserInputSchemaUpdateEmail
        responses:
          '200':
            description: Изменяет электронную почту пользователя
            content:
              application/json:
                schema: UserOutputSchemaUpdateEmail
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: UserErrorSchemaUpdateEmail
        tags:
          - Users
      """
    conn = get_db_connection()
    x = update_user_email(conn, request.get_json()['user_user_id', 'user_user_email'])
    return json.dumps({'message': "success"})

@blueprint_user.route('/api/users/update/surname', methods=['POST'])
def users_post_update_surname():
    """
      ---
      post:
        summary: Апдейт фамилии пользователя
        parameters:
          - in: query
            schema: UserInputSchemaUpdateSurname
        responses:
          '200':
            description: Изменяет фамилию пользователя
            content:
              application/json:
                schema: UserOutputSchemaUpdateSurname
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: UserErrorSchemaUpdateSurname
        tags:
          - Users
      """
    conn = get_db_connection()
    x = update_user_surname(conn, request.get_json()['user_user_id', 'user_user_surname'])
    return json.dumps({'message': "success"})

@blueprint_user.route('/api/users/update/name', methods=['POST'])
def users_post_update_name():
    """
      ---
      post:
        summary: Апдейт имени пользователя
        parameters:
          - in: query
            schema: UserInputSchemaUpdateName
        responses:
          '200':
            description: Изменяет имя пользователя
            content:
              application/json:
                schema: UserOutputSchemaUpdateName
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: UserErrorSchemaUpdateName
        tags:
          - Users
      """
    conn = get_db_connection()
    x = update_user_name(conn, request.get_json()['user_user_id', 'user_user_name'])
    return json.dumps({'message': "success"})

@blueprint_user.route('/api/users/update/fathername', methods=['POST'])
def users_post_update_fathername():
    """
      ---
      post:
        summary: Апдейт отчества пользователя
        parameters:
          - in: query
            schema: UserInputSchemaUpdateFathername
        responses:
          '200':
            description: Изменяет отчество пользователя
            content:
              application/json:
                schema: UserOutputSchemaUpdateFathername
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: UserErrorSchemaUpdateFathername
        tags:
          - Users
      """
    conn = get_db_connection()
    x = update_user_fathername(conn, request.get_json()['user_user_id', 'user_user_fathername'])
    return json.dumps({'message': "success"})


@blueprint_user.route('/api/users/update/age', methods=['POST'])
def users_post_update_age():
    """
      ---
      post:
        summary: Апдейт возраста пользователя
        parameters:
          - in: query
            schema: UserInputSchemaUpdateAge
        responses:
          '200':
            description: Изменяет возраст пользователя
            content:
              application/json:
                schema: UserOutputSchemaUpdateAge
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: UserErrorSchemaUpdateAge
        tags:
          - Users
      """
    conn = get_db_connection()
    x = update_user_age(conn, request.get_json()['user_user_id', 'user_user_age'])
    return json.dumps({'message': "success"})


@blueprint_user.route('/api/users/update/isFemale', methods=['POST'])
def users_post_update_isFemale():
    """
      ---
      post:
        summary: Апдейт пола пользователя
        parameters:
          - in: query
            schema: UserInputSchemaUpdateIsFemale
        responses:
          '200':
            description: Изменяет, является ли пользователь женщиной
            content:
              application/json:
                schema: UserOutputSchemaUpdateIsFemale
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: UserErrorSchemaUpdateIsFemale
        tags:
          - Users
      """
    conn = get_db_connection()
    x = update_user_isFemale(conn, request.get_json()['user_user_id', 'user_user_isFemale'])
    return json.dumps({'message': "success"})

@blueprint_user.route('/api/users/update/picture', methods=['POST'])
def users_post_update_picture():
    """
      ---
      post:
        summary: Апдейт картинки пользователя
        parameters:
          - in: query
            schema: UserInputSchemaUpdatePicture
        responses:
          '200':
            description: Изменяет картинку (аватарку) пользователя
            content:
              application/json:
                schema: UserOutputSchemaUpdatePicture
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: UserErrorSchemaUpdatePicture
        tags:
          - Users
      """
    conn = get_db_connection()
    x = update_user_picture(conn, request.get_json()['user_user_id', 'user_user_picture'])
    return json.dumps({'message': "success"})

@blueprint_user.route('/api/users/update/isAdmin', methods=['POST'])
def users_post_update_isAdmin():
    """
      ---
      post:
        summary: Апдейт прав администратора пользователя
        parameters:
          - in: query
            schema: UserInputSchemaUpdateIsAdmin
        responses:
          '200':
            description: Изменяет, является ли пользователь администратором
            content:
              application/json:
                schema: UserOutputSchemaUpdateIsAdmin
          '400':
            description: Не переданы обязательные параметры
            content:
              application/json:
                schema: UserErrorSchemaUpdateIsAdmin
        tags:
          - Users
      """
    conn = get_db_connection()
    x = update_user_isAdmin(conn, request.get_json()['user_user_id', 'user_user_isAdmin'])
    return json.dumps({'message': "success"})
