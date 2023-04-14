import json
from utils import get_db_connection
from app import app
from flask import request
from models.animals_model import get_animals, delete_animal

@app.route('/api/animals', methods=['GET'])
def selectallanimals():
    conn = get_db_connection()
    x = get_animals(conn)
    return json.dumps(x.to_dict(orient="records"))

@app.route('/api/animals/delete', methods=['POST'])
def deleteanimal():
    conn = get_db_connection()
    x = delete_animal(conn, request.get_json()['animal_user_id'])
    return json.dumps({'message': "success"})