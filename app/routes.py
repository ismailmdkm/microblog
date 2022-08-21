from html.entities import html5
from flask import redirect, render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def indes():
    user = {'username':'Ismail2'}
    posts = [ 
        {
        'author': {'username': 'John'},
        'body': 'Beautiful day in Portland!'
        },
    {
        'author': {'username': 'Susan'},
        'body': 'The Avengers movie was so cool!'
    }
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requsted for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect('/index')
    return render_template('login.html', title="Sign In", form=form)