import os
from flask import Flask, render_template, request, session, redirect, url_for
from utils import database

storybuilding = Flask(__name__)
storybuilding.secret_key = os.urandom(32)

@storybuilding.route('/')
@storybuilding.route('/home')
def homepage():
    return render_template('home.html')

@storybuilding.route('/login')
def login():
    return render_template('login.html')

@storybuilding.route('/stories')
def stories():
    return render_template('stories.html')

@storybuilding.route('/search')
def search():
    return render_template('search.html')

if __name__ == '__main__':
    storybuilding.debug = True
    storybuilding.run()