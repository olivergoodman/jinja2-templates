from flask import Flask, render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
   page_title = 'Oliver Goodman' 
   title = 'Home'
   print 'index was called'
   return render_template('index.html',
                          title = title,
                          page_title = page_title)


#how to load new page (contact) ??
@app.route('/contact')
def contact():
	page_title = 'Contact'
	return render_template('contact.html',
							title = 'Oliver Goodman | Contact',
							page_title = page_title)


##example stuff
# def index():
#     user = {'nickname': 'Miguel'}  # fake user
#     posts = [  # fake array of posts
#         { 
#             'author': {'nickname': 'John'}, 
#             'body': 'Beautiful day in Portland!' 
#         },
#         { 
#             'author': {'nickname': 'Susan'}, 
#             'body': 'The Avengers movie was so cool!' 
#         }
#     ]
#     return render_template("index.html",
#                            title='Home',
#                            user=user,
#                            posts=posts)