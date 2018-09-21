class Config:
    SECRET_KEY = 'hard to guess string'
    FLASKY_ADMIN = 'Flasto'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True
    
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "presto://crm@10.10.22.5:10300/dev_hive/cdm_crm"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "presto://crm@10.10.22.5:10300/dev_hive/cdm_crm"


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "presto://crm@10.10.22.8:10300/prod_hive/cdm_crm"


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
