import os
from flask import Flask, render_template, request, session, redirect, url_for

storybuilding = Flask(__name__)
storybuilding.secret_key = os.urandom(32)

@storybuilding.route('/')
def homepage():
    return render_template('frame.html')

if __name__ == '__main__':
    storybuilding.debug = True
    storybuilding.run()