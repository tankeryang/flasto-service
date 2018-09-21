from flask import Flask, Blueprint
from flask_restplus import Api
from query_service.query_web.config import config

flasto = Blueprint('flasto', __name__, url_prefix='/flasto/api')
api = Api(flasto, version='1.0', prefix='/v1', title="Presto Api", description="Presto Query Api Service")


def register_api():
    from query_service.query_web.controller.crm_controller import ns as crm_api
    from query_service.query_web import api
    
    api.add_namespace(crm_api)
    api.namespaces.pop(0)


def create_app(config_name):
    app = Flask("Flasto")
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    register_api()
    
    from query_service.query_web import flasto
    app.register_blueprint(flasto)
    
    return app
