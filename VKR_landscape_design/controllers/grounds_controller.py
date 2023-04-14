import json
from utils import get_db_connection
from app import app
from flask import request
from models.grounds_model import get_grounds, delete_ground

@app.route('/api/grounds', methods=['GET'])
def selectallgrounds():
    conn = get_db_connection()
    x = get_grounds(conn)
    return json.dumps(x.to_dict(orient="records"))

@app.route('/api/grounds/delete', methods=['POST'])
def deleteground():
    conn = get_db_connection()
    x = delete_ground(conn, request.get_json()['ground_user_id'])
    return json.dumps({'message': "success"})