import logging
from flask import current_app, g
from logging.handlers import RotatingFileHandler


def get_logger():
    if 'flasto_logger' not in g:
        
        flasto_logger = {}
        
        info_logger = logging.getLogger('flasto-service-info')
        error_logger = logging.getLogger('flasto-service-error')
        formatter = logging.Formatter(current_app.config['LOG_FORMAT'], current_app.config['DATE_FORMAT'])
    
        # set info handler
        info_handler = RotatingFileHandler(filename=current_app.config['LOG_PATH_INFO'])
        info_handler.setFormatter(formatter)
        info_handler.setLevel(logging.INFO)
    
        # set error handler
        error_handler = RotatingFileHandler(filename=current_app.config['LOG_PATH_ERROR'])
        error_handler.setFormatter(formatter)
        error_handler.setLevel(logging.ERROR)
    
        # add handler
        info_logger.addHandler(info_handler)
        error_logger.addHandler(error_handler)
        
        flasto_logger['flasto-service-info'] = info_logger
        flasto_logger['flasto-service-error'] = error_logger
        
        g.flasto_logger = flasto_logger
    
    return g.flasto_logger
