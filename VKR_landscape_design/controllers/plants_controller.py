import json
from utils import get_db_connection
from app import app
from flask import request
from models.plants_model import *

@app.route('/api/plant', methods=['GET'])
def selectallplant():
    conn = get_db_connection()
    x = get_plant(conn)
    return json.dumps(x.to_dict(orient="records"))

@app.route('/api/plant/delete', methods=['POST'])
def deleteplant():
    conn = get_db_connection()
    x = delete_plant(conn, request.get_json()['plant_user_id'])
    return json.dumps({'message': "success"})