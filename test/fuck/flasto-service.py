from flask import Flask
from flask_restplus import Resource, Api, fields


app = Flask(__name__)
api = Api(app, prefix="/v1", title="Users", description="Users CURD api.")


a_language = api.model('language', {
    'language': fields.List(fields.String('TheLanguage'))
})


languages = list()
python = {'language': 'python'}
languages.append(python)


@api.route('/language')
class Language(Resource):
    
    @api.marshal_with(a_language)
    def get(self):
        return languages

    @api.expect(a_language)
    def post(self):
        language = api.payload
        print(language.keys())
        languages.append(language)
        return {'result': '{} language added'.format(language)}, 200


if __name__ == '__main__':
    app.run(debug=True)
