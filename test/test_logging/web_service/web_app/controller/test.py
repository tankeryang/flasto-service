from flask import Blueprint, current_app

test = Blueprint('test', __name__, url_prefix='/test')

@test.route('/')
def root():
    current_app.logger.info('info log')
    current_app.logger.error('error log')
    current_app.logger.warning('warning log')
    
    return 'hello'