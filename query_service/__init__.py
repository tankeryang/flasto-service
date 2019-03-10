from flask import Flask
from query_service.apis.crm import (
    cic_static,
    report_center,
    income_analyse,
    asset_analyse,
    recruit_analyse,
    coupon,
    grouping,
)
from query_service.config import config
from query_service.exts import api_bp, api, cache


def register_bps(app):
    """
    注册蓝图
    :param app:
    :return:
    """
    app.register_blueprint(api_bp)


def register_apis():
    """
    注册 api namespace
    :return:
    """
    api.add_namespace(cic_static.views.ns)
    api.add_namespace(report_center.views.ns)
    api.add_namespace(income_analyse.views.ns)
    api.add_namespace(asset_analyse.views.ns)
    api.add_namespace(recruit_analyse.views.ns)
    api.add_namespace(coupon.views.ns)
    api.add_namespace(grouping.views.ns)
    api.namespaces.pop(0)


def register_exts(app):
    """
    注册插件
    :param app:
    :return:
    """
    cache.init_app(app)


def create_app(config_name):
    """
    app工厂
    :param config_name:
    :return:
    """
    app = Flask("flasto-service")
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    # 要先注册api, 再注册上级蓝图, 不然api的prefix路由不生效
    register_apis()
    register_bps(app)
    register_exts(app)
    
    return app
