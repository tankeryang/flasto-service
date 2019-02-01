import os


class ProductionConfig:
    # PRESTO_SERVER_URI = "presto://api@10.4.21.169:9090/hive/cdm_crm"
    
    @classmethod
    def init_app(cls, app):
        
        import logging
        from logging import StreamHandler
        from logging.handlers import RotatingFileHandler
        

        basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        print(basedir)
        LOG_PATH = os.path.join(basedir, 'log')
        LOG_PATH_INFO = os.path.join(LOG_PATH, 'info.log')
        LOG_PATH_ERROR = os.path.join(LOG_PATH, 'error.log')
        LOG_FORMAT = '%(asctime)s %(levelname) 8s: [%(filename)s:%(lineno)d] [%(processName)s:%(process)d %(threadName)s] - %(message)s'
        DATE_FORMAT = '[%Y-%m-%d %H:%M:%S]'
        
        formatter = logging.Formatter(LOG_FORMAT, DATE_FORMAT)
        
        file_handler_info = RotatingFileHandler(filename=LOG_PATH_INFO)
        file_handler_info.setLevel(logging.INFO)
        file_handler_info.setFormatter(formatter)
        app.logger.addHandler(file_handler_info)
        
        file_handler_error = RotatingFileHandler(filename=LOG_PATH_ERROR)
        file_handler_error.setFormatter(formatter)
        file_handler_error.setLevel(logging.ERROR)
        app.logger.addHandler(file_handler_error)

        app.logger.setLevel(logging.DEBUG)


config = {
    'production': ProductionConfig
}