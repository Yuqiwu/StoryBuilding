import sqlite3

f = "storybase.db"
db = sqlite3.connect(f)
c = db.cursor()

def addUser(username, password):
    if getPass == None:
        c.execute('INSERT INTO user values(%s, %s)' %(username, password) )

def getPass(user):
    result = c.execute('SELECT password FROM users WHERE username = %s' %(user) )
    if result == "":
        print none
    else:
        print result[0]
    
    
        
#def newStory(title, line, user, content):
#    c.execute('INSERT INTO stories values(?)', (title) )
#    c.execute( 'CREATE TABLE %s (line INTEGER PRIMARY KEY,content TEXT, author TEXT);' %(title) )
#    c.execute('INSERT INTO %s
getPass('Bob')