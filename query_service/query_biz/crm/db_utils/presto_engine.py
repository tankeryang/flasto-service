from flask import current_app, g
from sqlalchemy import create_engine


def get_presto_engine():
    if 'presto_engine' not in g:
        g.presto_engine = create_engine(current_app.config['PRESTO_SERVER_URI'])
        
    return g.presto_engine
