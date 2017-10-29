import sqlite3
from flask import session

f = "./storybase.db"
db = sqlite3.connect(f)
c = db.cursor()

# Adds a username/password combination to the user table
def add_user(username, password):
    db = sqlite3.connect(f)
    c = db.cursor()
    if get_pass(username) is None:
        c.execute('INSERT INTO users VALUES(\'%s\', \'%s\');' %(username, password))
        db.commit()
        return True
    else:
        return False

# Get the password of a user
def get_pass(username):
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute('SELECT password FROM users WHERE username=\'%s\';' %(username))
    result = c.fetchall()
    if result == []:
        return None
    else:
        return result[0][0]

# Login function
#note: cookies will be created and deleted in the file that does the flask stuff
def login(username, password): #returns 1 if successful, 0 if not successful, and -1 if account does not exist
    p = get_pass(username)
    if p is None:
        return -1
    elif p is password:
        make_login_cookie(username, password)
        return 1
    else:
        return 0

#checks to see if user is in a session
def in_session():
    return has_cookie() and session.get('password') == get_pass(session.get('username'))

# Stores the login in a cookie
def make_login_cookie(username, password):
    session['username'] = username
    session['password'] = password

# Deletes the cookie that stores user login
def delete_login_cookie():
    if 'username' in session:
        session.pop('username')
    if 'password' in session:
        session.pop('password')

# Checks if a user login cookie exists
def has_cookie():
    if 'username' in session and 'password' in session:
        return True
    else:
        return False
