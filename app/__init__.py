from flask import Flask

app = Flask(__name__)
from app import views

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)