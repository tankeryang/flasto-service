from io import BytesIO
from flask import Flask, send_file, make_response, send_from_directory
from flask_restplus import Api, Resource, fields
import pandas as pd
import numpy as np

app = Flask(__name__)
# web_app.wsgi_app = ProxyFix(web_app.wsgi_app)
api = Api(app, version='1.0', title='Test Export Excel API',
    description='export excel',
)

ns = api.namespace('ex', description='export excel test')

p = ns.model('p', {
    'download': fields.String(example="true")
})

@ns.route('/ExportExcel')
class ExportExcelController(Resource):
    
    @ns.expect(p)
    def post(self):
        if api.payload['download'] == 'true':
            arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', ],
                      ['one', 'two', 'one', 'two', 'one', 'two', ]]
            df = pd.DataFrame(np.random.randn(8, 6), columns=arrays)
            output = BytesIO()
            df.to_csv('df.csv')
            output.seek(0)
            return send_file(output, mimetype='text/csv', attachment_filename="df.csv", as_attachment=True)
        else:
            return None
    
    def get(self):
        arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', ],
                  ['one', 'two', 'one', 'two', 'one', 'two', ]]
        df = pd.DataFrame(np.random.randn(8, 6), columns=arrays)
        df.to_csv('df.csv')
        
        
        # response = make_response(send_from_directory(path, filename, as_attachment=True))
        # response.headers['Content-Type'] = 'text/csv'
        # response.headers['Content-Disposition'] = 'attachment; filename={}'.format(filename.encode().decode('latin-1'))
        #
        # return send_file(output, mimetype='text/csv', attachment_filename="df.csv", as_attachment=True)
    
    
if __name__ == '__main__':
    app.run(debug=True)
