from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'Matt'}
    posts = [
      {
        'author': {'name': 'Bridget'},
        'body': 'Sammy likes scrimps!'
      },
      {
        'author': {'name': 'Sammy'},
        'body': 'I like the salmon'
      }
    ]
    return render_template('index.html', title='Home',
                            user=user, posts=posts)