import json
from utils import get_db_connection
from app import app
from flask import request
from models.users_model import *

@app.route('/api/users', methods=['GET'])
def select_all_users():
    conn = get_db_connection()
    x = get_users(conn)
    return json.dumps(x.to_dict(orient="records"))

@app.route('/api/users', methods=['GET'])
def select_all_users_without_password():
    conn = get_db_connection()
    x = get_users_without_password(conn)
    return json.dumps(x.to_dict(orient="records"))

@app.route('/api/users', methods=['GET'])
def select_all_users_without_password_admins():
    conn = get_db_connection()
    x = get_users_without_password_admins(conn)
    return json.dumps(x.to_dict(orient="records"))

@app.route('/api/users', methods=['GET'])
def select_all_users_without_password_noadmins():
    conn = get_db_connection()
    x = get_users_without_password_noadmins(conn)
    return json.dumps(x.to_dict(orient="records"))


@app.route('/api/users/delete', methods=['POST'])
def delete_user():
    conn = get_db_connection()
    x = delete_user(conn, request.get_json()['user_user_id'])
    return json.dumps({'message': "success"})