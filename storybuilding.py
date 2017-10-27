import os
from flask import Flask, render_template, request, session, redirect, url_for
from utils import storybase, userbase

storybuilding = Flask(__name__)
storybuilding.secret_key = os.urandom(32)

@storybuilding.route('/')
@storybuilding.route('/home')
def homepage():
    ran_story = storybase.get_ran_story()
    return render_template('home.html', ran_title = "TEST", ran_content = "TEST")

@storybuilding.route('/login')
def auth():
    if 'username' not in session:
        return render_template('login.html')
    else:
        return redirect(url_for('homepage'))

@storybuilding.route('/stories')
def stories():
    return render_template('stories.html')

@storybuilding.route('/search')
def search():
    return render_template('search.html')

@storybuilding.route('/edit')
def edit():
    return render_template('edit.html')

if __name__ == '__main__':
    storybuilding.debug = True
    storybuilding.run()
