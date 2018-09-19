from flask import Flask, Blueprint
from flask_restplus import Api
from config import config


flasto = Blueprint('flasto', __name__, url_prefix='/flasto/api')
api = Api(flasto, version='1.0', prefix='/v1', title="Presto Api", description="Presto Query Api Service")


def register_api():
    from query_api.crm.service.crm_service import ns as crm_api
    from query_api import api
    
    api.add_namespace(crm_api)


def create_app(config_name):
    app = Flask("Flasto")
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    register_api()
    
    from query_api import flasto
    app.register_blueprint(flasto)

    return app
