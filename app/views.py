from flask import Flask, render_template
from app import app, db
from app.models import Page
from flask.ext.sqlalchemy import SQLAlchemy

#app = Flask(__name__)

@app.route('/page_title/<page_title>')
def page_title(page_title):
  target_page = Page.query.filter_by(page_name = page_title).first()
  target_page.pageVisit()
  db.session.add(target_page)
  db.session.commit()
  
@app.route('/')
@app.route('/index')

def index():
  page_name = 'Oliver Goodman' 
  print 'index was called'
  return render_template('index.html',
                          title = "Home",
                          page_name = page_name)

@app.route('/contact')
def contact(): 
  page_name = 'Contact'
  return render_template('contact.html',
						            	title = 'Contact',
						            	page_name = page_name)

