import os
from flask import Flask, render_template, request, session, redirect, url_for, flash
from utils import storybase, userbase

in_session = userbase.in_session

storybuilding = Flask(__name__)
storybuilding.secret_key = os.urandom(32)

@storybuilding.route('/')
def homepage():
    ran_story = storybase.get_ran_story()
    return render_template('home.html', ran_title = ran_story[0][0][0], ran_content = ran_story[1][0][0])

@storybuilding.route('/login')
def loginpage():
    if not in_session():
        return render_template('login.html')
    else:
        return redirect(url_for('homepage'))

@storybuilding.route('/logout')
def logout():
    if userbase.has_cookie() is True:
        userbase.delete_login_cookie()
    return redirect(url_for('homepage'))

@storybuilding.route('/auth', methods=["POST"])
def auth():
    username_i = request.form['inputUsername']
    password_i = request.form['inputPassword']
    if userbase.get_pass(username_i) is None:
        userbase.add_user(username_i, password_i)
        userbase.make_login_cookie(username_i, password_i)
    elif userbase.get_pass(username_i) == password_i:
        userbase.make_login_cookie(username_i, password_i)
    else:
        flash("Incorrect Password")
    return redirect(url_for('loginpage'))

@storybuilding.route('/stories')
def stories():
    storylist = storybase.get_stories()
    return render_template('stories.html', storylist = storylist)

@storybuilding.route('/newstory')
def newstory():
    return render_template('newstory.html')

@storybuilding.route('/createstory', methods=["POST"])
def createstory():
    story_title = request.form['inputTitle']
    story_line = request.form['inputLine']
    username_i = session.get('username')
    storybase.new_story(story_title, story_line, username_i)
    return redirect(url_for('homepage'))

@storybuilding.route('/search')
def search():
    return render_template('search.html')

@storybuilding.route('/edit', methods=["POST"])
def edit():
    story_title = request.form['story_title']
    story_line = storybase.get_story(story_title, session.get('username'))
    return render_template('edit.html', story_title=story_title, story_line=story_line)

@storybuilding.route('/addline', methods=["POST"])
def addline():
    if(not in_session()):
        return redirect(url_for('loginpage'))
    story_title = request.form['title']
    story_line = request.form['line']
    username_i = session.get('username')
    storybase.add_to_story(story_title, story_line, username_i)
    session['title'] = story_title
    return redirect(url_for('story'))

@storybuilding.route('/story')
def story():
    if(not in_session ()):
        return redirect(url_for('loginpage'))
    story_title=session.get('title')
    story_line=storybase.get_story(story_title, session.get('username'))
    return render_template('story.html', story_title=story_title, story_content=story_line)

if __name__ == '__main__':
    storybuilding.debug = True
    storybuilding.run()
