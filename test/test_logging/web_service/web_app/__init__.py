from flask import Flask

from test.test_logging.web_service.web_app.config import config


def create_app(config_name):
    from test.test_logging.web_service.web_app.controller.test import test
    
    app = Flask("Flasto")
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.register_blueprint(test)
    
    return app