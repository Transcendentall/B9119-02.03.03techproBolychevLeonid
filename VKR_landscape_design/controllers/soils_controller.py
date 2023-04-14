import json
from utils import get_db_connection
from app import app
from flask import request
from models.soils_model import *

@app.route('/api/soils', methods=['GET'])
def selectallsoils():
    conn = get_db_connection()
    x = get_soils(conn)
    return json.dumps(x.to_dict(orient="records"))

@app.route('/api/soils/delete', methods=['POST'])
def deletesoil():
    conn = get_db_connection()
    x = delete_soil(conn, request.get_json()['soil_user_id'])
    return json.dumps({'message': "success"})