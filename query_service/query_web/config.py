class Config:
    SECRET_KEY = 'caonima'
    FLASKY_ADMIN = 'Flasto'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True
    
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    PRESTO_SERVER_URI = "presto://dev@10.10.22.5:10300/dev_hive/cdm_crm"


class TestingConfig(Config):
    TESTING = True
    PRESTO_SERVER_URI = "presto://dev@10.10.22.5:10300/dev_hive/cdm_crm"


class ProductionConfig(Config):
    PRESTO_SERVER_URI = "presto://crm@10.10.22.8:10300/prod_hive/cdm_crm"


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
