import sqlite3

f = "../storybase.db"
db = sqlite3.connect(f)
c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS stories (name TEXT, content TEXT);')

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
    
    
        
def newStory(title, line, content, user):
    c.execute('INSERT INTO stories values(?, ?)', (title, content) )
    c.execute( 'CREATE TABLE "%s" (line INTEGER PRIMARY KEY,content TEXT, author TEXT);' %(title) )
    c.execute('INSERT INTO "%s" VALUES( "%s", "%s");' %(title,content,user) )
    db.commit()
              
newStory('the cult of the oreoss','oreos are delicious','bob')
