import sqlite3

f = "../storybase.db"
db = sqlite3.connect(f)
c = db.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT);')

def addUser(username, password):
    if getPass(username) == None:
        c.execute('INSERT INTO users VALUES(\'%s\', \'%s\');' %(username, password) )
        db.commit()
        return True
    else:
        return False

def getPass(user):
    c.execute('SELECT password FROM users WHERE username=\'%s\';' %(user) )
    result = c.fetchall()
    if result == []:
        return None
    else:
        return result[0][0]

#note: cookies will be created and deleted in the file that does the flask stuff
def login(username,password): #returns 1 if successful, 0 if not successful, and -1 if account does not exist
    p = getPass(username)
    if(p == None):
        return -1
    elif(p == password):
        makeCookie(username,password)
        return 1
    else:
        return 0

def makeLoginCookie(username,password): #call this function after login is successful
    session['username'] = username
	session['password'] = password
	

def deleteLoginCookie(): #call this function if logging out or logging in with cookie is unsuccessful
    if('username' in session):
		session.pop('username')
	if('password') in session):
		session.pop('password')

def hasCookie():
	if('user' in session and 'password' in session):
		return True
	else:
		return False