import json
from utils import get_db_connection
from app import app
from flask import request
from models.users_model import get_users, delete_user

@app.route('/api/users', methods=['GET'])
def selectallusers():
    conn = get_db_connection()
    x = get_users(conn)
    return json.dumps(x.to_dict(orient="records"))

@app.route('/api/users/delete', methods=['POST'])
def deleteuser():
    conn = get_db_connection()
    x = delete_user(conn, request.get_json()['user_user_id'])
    return json.dumps({'message': "success"})