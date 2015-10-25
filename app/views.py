from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'firstname': 'Olly', 'lastname' : 'Goodman'}  # fake user
    return '''
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Hello, ''' + user['lastname'] + '''</h1>
  </body>
</html>
'''