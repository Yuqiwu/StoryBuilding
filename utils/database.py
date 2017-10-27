import sqlite3

f = "../storybase.db"
db = sqlite3.connect(f)
c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS stories (title TEXT);')
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

def newStory(title, content, user):
    c.execute('INSERT INTO stories values(?);', (title) )
    c.execute( 'CREATE TABLE "%s" (show INTEGER,content TEXT, author TEXT);' %(title) )
    addToStory(title, content, user)
    
def addToStory(title, content, user):
    c.execute('INSERT INTO "%s" VALUES("%s", "%s");' %(title,content,user) )
    db.commit()

def getStory(story,name):
    c.execute('SELECT author FROM "%s" WHERE author=\'%s\';' %(story,name) )
    result = c.fetchall()
    if result == []:
        c.execute('SELECT content FROM "%s"' %(story) )
        result = c.fetchall()
        return result[-1][0]
    else:
        c.execute('SELECT content FROM "%s"' %(story) )
        result = c.fetchall()
        s = ""
        for content in result:
            s = s + content[0] + ' '
        return s
