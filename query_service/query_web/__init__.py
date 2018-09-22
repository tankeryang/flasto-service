from flask import Flask, Blueprint
from flask_restplus import Api
from query_service.query_web.config import config


flasto = Blueprint('flasto', __name__, url_prefix='/flasto/api')
api = Api(flasto, version='1.0', prefix='/query', title="Presto Query Api", description="Presto 查询服务")


class ReverseProxy(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        script_name = environ.get('HTTP_X_SCRIPT_NAME', '')
        if script_name:
            environ['SCRIPT_NAME'] = script_name
            path_info = environ['PATH_INFO']
            if path_info.startswith(script_name):
                environ['PATH_INFO'] = path_info[len(script_name):]

        scheme = environ.get('HTTP_X_SCHEME', '')
        if scheme:
            environ['wsgi.url_scheme'] = scheme
        return self.app(environ, start_response)


def register_api():
    from query_service.query_web.controller.crm_controller import ns_1 as crm_daily_report
    from query_service.query_web.controller.crm_controller import ns_2 as crm_sales_analyse
    from query_service.query_web import api
    
    api.add_namespace(crm_daily_report)
    api.add_namespace(crm_sales_analyse)
    api.namespaces.pop(0)


def create_app(config_name):
    app = Flask("Flasto")
    app.config.from_object(config[config_name])
    app.wsgi_app = ReverseProxy(app.wsgi_app)
    config[config_name].init_app(app)
    
    register_api()
    
    from query_service.query_web import flasto
    app.register_blueprint(flasto)
    
    return app
