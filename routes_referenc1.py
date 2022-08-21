from html.entities import html5
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def indes():
    user = {'username':'Ismail2'}
    return render_template('index.html', title="Home", user=user)
    #return 'Hi, ' + user["username"]
    #return f'Hi, {user["username"]}'
    # return '''
    # <html>
    #     <head>
    #         <title>Microblog</title>
    #     </head>
    #     <body>
    #         <h1>Hi, ''' + user['username'] + '''</h1>
    #     </body>
    # </html>
    # '''