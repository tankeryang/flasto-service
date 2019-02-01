import os


class Config:
    SECRET_KEY = 'Trendy_Crm123'
    FLASK_ADMIN = 'Flasto'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True

    basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    LOG_PATH = os.path.join(basedir, 'log')
    LOG_PATH_ERROR = os.path.join(LOG_PATH, 'error')
    LOG_PATH_INFO = os.path.join(LOG_PATH, 'info')
    LOG_FORMAT = '%(asctime)s %(levelname) 8s: [%(filename)s - %(funcName)s:%(lineno)d] [%(processName)s:%(process)d %(threadName)s] - %(message)s'
    DATE_FORMAT = '[%Y-%m-%d %H:%M:%S]'
    
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    PRESTO_SERVER_URI = "presto://dev@10.10.22.5:10300/dev_hive/cdm_crm"


class TestingConfig(Config):
    TESTING = True
    PRESTO_SERVER_URI = "presto://dev@10.10.22.5:10300/dev_hive/cdm_crm"


class PreProductionConfig(Config):
    PRESTO_SERVER_URI = "presto://crm@10.10.22.8:10300/prod_hive/cdm_crm"


class ProductionConfig(Config):

    PRESTO_SERVER_URI = "presto://api@10.4.21.169:9090/hive/cdm_crm"
    
    @classmethod
    def init_app(cls, app):
        import logging
        from logging.handlers import TimedRotatingFileHandler
        
        Config.init_app(app)
        
        formatter = logging.Formatter(cls.LOG_FORMAT, cls.DATE_FORMAT)
    
        # set info handler
        info_handler = TimedRotatingFileHandler(filename=cls.LOG_PATH_INFO, when='D', interval=1, backupCount=30, encoding='utf8')
        info_handler.setFormatter(formatter)
        info_handler.setLevel(logging.INFO)
        info_handler.suffix = '_%Y-%m-%d.log'
    
        # set error handler
        error_handler = TimedRotatingFileHandler(filename=cls.LOG_PATH_ERROR, when='D', interval=1, backupCount=30, encoding='utf8')
        error_handler.setFormatter(formatter)
        error_handler.setLevel(logging.ERROR)
        error_handler.suffix = '_%Y-%m-%d.log'
        
        # add handler
        app.logger.addHandler(info_handler)
        app.logger.addHandler(error_handler)
        app.logger.setLevel(logging.DEBUG)
        


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'preproduction': PreProductionConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
