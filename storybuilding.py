import os
from flask import Flask, render_template, request, session, redirect, url_for, flash
from utils import storybase, userbase

storybuilding = Flask(__name__)
storybuilding.secret_key = os.urandom(32)

# Home/Root route
@storybuilding.route('/')
def homepage():
    ran_story = storybase.get_ran_story()
    return render_template('home.html', ran_title = ran_story[0][0][0], ran_content = ran_story[1][-1][0])

# Login route - Displays login page
@storybuilding.route('/login')
def loginpage():
    if 'username' not in session:
        return render_template('login.html')
    else:
        return redirect(url_for('homepage'))

# Logout route - Deletes login session cookie and redirects to home
@storybuilding.route('/logout')
def logout():
    if userbase.has_cookie() is True:
        userbase.delete_login_cookie()
    return redirect(url_for('homepage'))

# Logs the user in / Registers them. Redirects to login page
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

# List of stories
@storybuilding.route('/stories')
def stories():
    storylist = storybase.get_stories()
    return render_template('stories.html', storylist = storylist)

# Create a new story page
@storybuilding.route('/newstory')
def newstory():
    return render_template('newstory.html')

# Creates a new story and return to homepage afterwards
@storybuilding.route('/createstory', methods=["POST"])
def createstory():
    story_title = request.form['inputTitle']
    story_line = request.form['inputLine']
    username_i = session.get('username')
    storybase.new_story(story_title, story_line, username_i)
    return redirect(url_for('homepage'))

# Edit story page
@storybuilding.route('/edit', methods=["POST"])
def edit():
    story_title = request.form['story_title']
    story_line = storybase.get_story(story_title, session.get('username'))
    story_state = storybase.edited(story_title, session.get('username'))
    return render_template('edit.html', story_title=story_title, story_line=story_line, story_state=story_state)

# Edit story function
@storybuilding.route('/addline', methods=["POST"])
def addline():
    story_title = request.form['title']
    story_line = request.form['line']
    username_i = session.get('username')
    storybase.add_to_story(story_title, story_line, username_i)
    session['title'] = story_title
    return redirect(url_for('story'))

# Story page
@storybuilding.route('/story')
def story():
    story_title = session.get('title')
    story_line = storybase.get_story(story_title, session.get('username'))
    return render_template('story.html', story_title=story_title, story_content=story_line)

# Function to go to a specific story
@storybuilding.route('/gostory/<title>')
def getstory(title):
    session['title'] = title
    return redirect(url_for('story'))

if __name__ == '__main__':
    storybuilding.debug = True
    storybuilding.run()
