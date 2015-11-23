from flask import Flask, render_template
from app import app
from flask.ext.sqlalchemy import SQLAlchemy

#---------------------DB-------------------------
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Page(db.Model):
    page_name = db.Column(db.String(80), unique=True)
    page_hits = db.Column(db.Integer, primary_key=True)

    def __init__(self, page_hits, page_name):
        self.page_name = page_name
        self.page_hits = page_hits

    def __repr__(self):
        return '<Page Title %r>' % self.page_name
#----------------------------------------------
  
@app.route('/')
@app.route('/index')

def index():
  page_name = 'Oliver Goodman' 
  title = 'Home'
  print 'index was called'
  return render_template('index.html',
                          title = title,
                          page_name = page_name)

@app.route('/contact')
def contact(): 
  page_name = 'Contact'
  return render_template('contact.html',
							title = 'Oliver Goodman | Contact',
							page_name = page_name)

