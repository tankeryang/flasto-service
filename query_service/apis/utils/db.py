from flask import g, current_app
from sqlalchemy import create_engine


def engine():
    if 'presto_engine' not in g:
        g.presto_engine = create_engine(current_app.config['PRESTO_SERVER_URI'], encoding='utf8')
    
    return g.presto_engine
