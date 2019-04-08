from flask import Blueprint
from flask_caching import Cache
from flask_restplus import Api

api_bp = Blueprint('flasto-api', 'flasto-api', url_prefix='/api')
api = Api(
    api_bp,
    version='1.2.1',
    prefix='/v1',
    title="Presto Query Api",
    description="Presto 查询服务 - by Flask, Flask-RESTPlus",
    contact="@Yang.Yang",
    contact_email="yang.yang@trendy-global.com",
    contact_url="https://tankeryang.github.io",
    authorizations=dict(key={'type': 'apiKey', 'in': 'Header', 'name': 'X-API-KEY'}),
    serve_challenge_on_401=True,
)
cache = Cache()
