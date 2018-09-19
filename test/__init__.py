from flask import Blueprint, Flask
from flask_restplus import Api


api_blueprint = Blueprint("open_api", __name__, url_prefix="/api")
api = Api(api_blueprint, version="1.0", prefix="/v1", title="OpenApi", description="The Open Api Service")


def register_api():
    from test.test_apis.user_api import ns as user_api
    from test import api
    api.add_namespace(user_api)


def create_app():
    app = Flask("Flask-Web-Demo")

    # register api namespace
    register_api()

    # register blueprint
    from test import api_blueprint
    app.register_blueprint(api_blueprint)

    return app
