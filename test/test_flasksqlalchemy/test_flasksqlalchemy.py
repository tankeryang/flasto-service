from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class CicMainPage(db.Model):
    
    brand = db.Column(db.String())
    register_member_amount = db.Column(db.Integer, primary_key=True)
    rma_compared_with_ydst = db.Column(db.DECIMAL(18, 4))
    rma_compared_with_lwst = db.Column(db.DECIMAL(18, 4))
    rma_compared_with_lmst = db.Column(db.DECIMAL(18, 4))


class Config:
    SQLALCHEMY_DATABASE_URI = 'presto://api@10.4.21.169:9090/hive/ads_crm'


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app=app)


@app.route('/test')
def test():
    print(CicMainPage.query.all())


if __name__ == '__main__':
    app.run(debug=True)
