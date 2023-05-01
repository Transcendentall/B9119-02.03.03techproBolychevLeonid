from flask import Flask, json
from flask_cors import CORS
from utilities.api_spec import get_apispec
from controllers.users_controller import blueprint_user
from controllers.territories_controller import blueprint_territorie
from controllers.grounds_controller import blueprint_ground
from controllers.soils_controller import blueprint_soil
from controllers.animals_controller import blueprint_animal
from controllers.plants_controller import blueprint_plant
from utilities.swagger import swagger_ui_blueprint, SWAGGER_URL

app = Flask(__name__)

app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)
app.register_blueprint(blueprint_user)
app.register_blueprint(blueprint_territorie)
app.register_blueprint(blueprint_ground)
app.register_blueprint(blueprint_soil)
app.register_blueprint(blueprint_animal)
app.register_blueprint(blueprint_plant)


@app.route('/swagger')
def create_swagger_spec():
    return json.dumps(get_apispec(app).to_dict())

CORS(app)