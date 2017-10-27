import sqlite3

f = "../storybase.db"
db = sqlite3.connect(f)
c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS stories (title TEXT);')

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
