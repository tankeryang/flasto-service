from io import BytesIO
from flask import Flask, send_file, make_response
from flask_restplus import Api, Resource, fields
import pandas as pd
import numpy as np

app = Flask(__name__)
# app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='Test Export Excel API',
    description='export excel',
)

ns = api.namespace('ex', description='export excel test')

@ns.route('/ExportExcel')
class ExportExcelController(Resource):
    
    def get(self):
        arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', ],
                  ['one', 'two', 'one', 'two', 'one', 'two', ]]
        df = pd.DataFrame(np.random.randn(8, 6), columns=arrays)
        output = BytesIO()
        df.to_excel('df.xlsx')
        output.seek(0)
        return send_file(output, attachment_filename="df.xlsx", as_attachment=True)
    
    
if __name__ == '__main__':
    app.run(debug=True)
