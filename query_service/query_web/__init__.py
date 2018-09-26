from flask import Flask, Blueprint
from flask_restplus import Api
from jsonschema import FormatChecker
from query_service.query_web.config import config


flasto = Blueprint('flasto', __name__, url_prefix='/flasto/api')
api = Api(
    flasto,
    version='1.0',
    prefix='/query',
    title="Presto Query Api",
    description="Presto 查询服务",
    validate=True,
    format_checker=FormatChecker(formats=("date-time", "date",))
)


def register_api():
    from query_service.query_web.controller.crm_controller import ns_1 as crm_daily_report
    from query_service.query_web.controller.crm_controller import ns_2 as crm_sales_analyse
    from query_service.query_web.controller.crm_controller import ns_3 as crm_asset_analyse
    from query_service.query_web import api
    
    api.add_namespace(crm_daily_report)
    api.add_namespace(crm_sales_analyse)
    api.add_namespace(crm_asset_analyse)
    api.namespaces.pop(0)


def create_app(config_name):
    app = Flask("Flasto")
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    register_api()
    
    from query_service.query_web import flasto
    app.register_blueprint(flasto)
    
    return app
