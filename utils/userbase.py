import sqlite3

f = "../storybase.db"
db = sqlite3.connect(f)
c = db.cursor()

# Adds a username/password combination to the user table
def addUser(username, password):
    if getPass(username) == None:
        c.execute('INSERT INTO users VALUES(\'%s\', \'%s\');' %(username, password))
        db.commit()
        return True
    else:
        return False

# Get the password of a user
def getPass(username):
    c.execute('SELECT password FROM users WHERE username=\'%s\';' %(username))
    result = c.fetchall()
    if result == []:
        return None
    else:
        return result[0][0]

# Login function
#note: cookies will be created and deleted in the file that does the flask stuff
def login(username, password): #returns 1 if successful, 0 if not successful, and -1 if account does not exist
    p = getPass(username)
    if(p == None):
        return -1
    elif(p == password):
        makeCookie(username,password)
        return 1
    else:
        return 0

# Stores the login in a cookie
def makeLoginCookie(username, password): #call this function after login is successful
    session['username'] = username
	session['password'] = password
	
# Deletes the cookie that stores user login
def deleteLoginCookie(): #call this function if logging out or logging in with cookie is unsuccessful
    if('username' in session):
		session.pop('username')
	if('password') in session):
		session.pop('password')

# Checks if a user login cookie exists
def hasCookie():
	if('username' in session and 'password' in session):
		return True
	else:
		return False