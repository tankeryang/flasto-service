from flask import Flask
from flask_restplus import Resource, Api, fields, abort


class Config:
    ERROR_INCLUDE_MESSAGE = False


app = Flask(__name__)
app.config.from_object(Config)
api = Api(app, prefix="/v1", title="Users", description="Users CURD api.")


language = api.model('language', {
    'language': fields.List(fields.String('TheLanguage')),
    'num': fields.Integer(required=True)
})
a_language = api.model('languageList', {
    'data': fields.List(fields.Nested(language)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


languages = list()
python = {'language': 'python'}
languages.append(python)


@api.errorhandler
# @api.marshal_with(a_language, code=400)
def handle_fake_exception_with_header(error):
    return {'data': [], 'message': error.message, 'success': False}, 400


@api.route('/language')
@api.response(400, 'Validation error', a_language)
class Language(Resource):
    
    @api.marshal_with(a_language, envelope='result')
    def get(self):
        """
        get lang
        :return:
        """
        return languages

    @api.marshal_with(a_language, envelope='result')
    @api.expect(language, validate=True)
    # @api.doc(body=a_language)
    def post(self):
        _language = api.payload
        print(_language.keys())
        return {'result': '{} language added'.format(_language)}, 200


if __name__ == '__main__':
    app.run(debug=True)
