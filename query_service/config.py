import os
import datetime


class Config:
    basedir = os.path.abspath(os.path.dirname(__file__))
    today = datetime.date.today().strftime('%Y-%m-%d')
    # Flask
    SECRET_KEY = 'Trendy_Crm123'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True
    # log
    LOG_PATH = os.path.join(basedir, 'log')
    LOG_PATH_INFO = os.path.join(LOG_PATH, 'info-from_' + today)
    LOG_PATH_ERROR = os.path.join(LOG_PATH, 'error-from_' + today)
    LOG_FORMAT = '%(asctime)s %(levelname) 8s: [%(pathname)s - %(funcName)s:%(lineno)d] [%(processName)s:%(process)d ' \
                 '%(threadName)s] - %(message)s '
    DATE_FORMAT = '[%Y-%m-%d %H:%M:%S]'
    # tmp file
    TMP_PATH = '/opt/flasto-service/query_service/tmp/'
    
    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG = True
    PRESTO_SERVER_URI = "presto://api@emr-header-1:9090/hive/cdm_crm"
    TMP_PATH = '/Users/yang/workspace/PycharmProjects/Fp-project/flasto-service/query_service/tmp/'
    FILE_SERVER_URL_PREFIX = 'http://ftp.emr.trendygroup-it.com/crm-test/'

    # cache
    CACHE_TYPE = 'redis'
    CACHE_REDIS_HOST = 'localhost'
    CACHE_REDIS_PORT = 18879
    CACHE_REDIS_DB = 2

    @classmethod
    def init_app(cls, app):
        import logging
        from logging.handlers import TimedRotatingFileHandler
    
        Config.init_app(app)
        formatter = logging.Formatter(cls.LOG_FORMAT, cls.DATE_FORMAT)
        # set info handler
        info_handler = TimedRotatingFileHandler(
            filename=cls.LOG_PATH_INFO,
            when='midnight',
            interval=1,
            backupCount=30,
            encoding='utf8'
        )
        info_handler.setFormatter(formatter)
        info_handler.setLevel(logging.INFO)
        info_handler.suffix = 'to_%Y-%m-%d.log'
        # set error handler
        error_handler = TimedRotatingFileHandler(
            filename=cls.LOG_PATH_ERROR,
            when='midnight',
            interval=1,
            backupCount=30,
            encoding='utf8'
        )
        error_handler.setFormatter(formatter)
        error_handler.setLevel(logging.ERROR)
        error_handler.suffix = 'to_%Y-%m-%d.log'
        # add handler
        app.logger.addHandler(info_handler)
        app.logger.addHandler(error_handler)
        app.logger.setLevel(logging.DEBUG)


class TestConfig(Config):
    TESTING = True
    PRESTO_SERVER_URI = "presto://dev@10.10.22.8:10300/dev_hive/cdm_crm"


class PreProdConfig(Config):
    PRESTO_SERVER_URI = "presto://api@emr-header-1:9090/hive/cdm_crm"
    FILE_SERVER_URL_PREFIX = 'http://ftp.emr.trendygroup-it.com/crm-test/'
    
    # cache
    CACHE_TYPE = 'redis'
    CACHE_REDIS_HOST = 'redis'
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = 2

    @classmethod
    def init_app(cls, app):
        import logging
        from logging.handlers import TimedRotatingFileHandler
        
        Config.init_app(app)
        formatter = logging.Formatter(cls.LOG_FORMAT, cls.DATE_FORMAT)
        # set info handler
        info_handler = TimedRotatingFileHandler(
            filename=cls.LOG_PATH_INFO,
            when='midnight',
            interval=1,
            backupCount=30,
            encoding='utf8'
        )
        info_handler.setFormatter(formatter)
        info_handler.setLevel(logging.INFO)
        info_handler.suffix = 'to_%Y-%m-%d.log'
        # set error handler
        error_handler = TimedRotatingFileHandler(
            filename=cls.LOG_PATH_ERROR,
            when='midnight',
            interval=1,
            backupCount=30,
            encoding='utf8'
        )
        error_handler.setFormatter(formatter)
        error_handler.setLevel(logging.ERROR)
        error_handler.suffix = 'to_%Y-%m-%d.log'
        # add handler
        app.logger.addHandler(info_handler)
        app.logger.addHandler(error_handler)
        app.logger.setLevel(logging.DEBUG)


class ProdConfig(Config):
    PRESTO_SERVER_URI = "presto://api@emr-header-1:9090/hive/cdm_crm"
    FILE_SERVER_URL_PREFIX = 'http://ftp.emr.trendygroup-it.com/crm/'
    
    # cache
    CACHE_TYPE = 'redis'
    CACHE_REDIS_HOST = 'redis'
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = 4
    
    @classmethod
    def init_app(cls, app):
        import logging
        from logging.handlers import TimedRotatingFileHandler
        Config.init_app(app)
        formatter = logging.Formatter(cls.LOG_FORMAT, cls.DATE_FORMAT)
        # set info handler
        info_handler = TimedRotatingFileHandler(
            filename=cls.LOG_PATH_INFO,
            when='midnight',
            interval=1,
            backupCount=30,
            encoding='utf8'
        )
        info_handler.setFormatter(formatter)
        info_handler.setLevel(logging.INFO)
        info_handler.suffix = 'to_%Y-%m-%d.log'
        # set error handler
        error_handler = TimedRotatingFileHandler(
            filename=cls.LOG_PATH_ERROR,
            when='midnight',
            interval=1,
            backupCount=30,
            encoding='utf8'
        )
        error_handler.setFormatter(formatter)
        error_handler.setLevel(logging.ERROR)
        error_handler.suffix = 'to_%Y-%m-%d.log'
        # add handler
        app.logger.addHandler(info_handler)
        app.logger.addHandler(error_handler)
        app.logger.setLevel(logging.DEBUG)


config = {
    'default': DevConfig,
    'dev': DevConfig,
    'test': TestConfig,
    'preprod': PreProdConfig,
    'prod': ProdConfig,
}
