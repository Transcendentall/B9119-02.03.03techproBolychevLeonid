import json
from utils import get_db_connection
from app import app
from flask import request
from models.territories_model import get_territories, delete_territorie

@app.route('/api/territories', methods=['GET'])
def selectallterritories():
    conn = get_db_connection()
    x = get_territories(conn)
    return json.dumps(x.to_dict(orient="records"))

@app.route('/api/territories/delete', methods=['POST'])
def deleteterritorie():
    conn = get_db_connection()
    x = delete_territorie(conn, request.get_json()['territorie_user_id'])
    return json.dumps({'message': "success"})