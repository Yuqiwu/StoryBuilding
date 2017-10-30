import sqlite3

f = "./storybase.db"
db = sqlite3.connect(f)
c = db.cursor()

# Ensures the stories database exists
c.execute('CREATE TABLE IF NOT EXISTS stories (title TEXT);')
# Ensures the user database exists
c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT);')
db.close()
# Creates a new table containing the first line of the new story
def new_story(title, content, user):
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute('SELECT * FROM stories WHERE title = "%s";' %(title))
    result = c.fetchall()
    if result == []:
        c.execute('INSERT INTO stories VALUES(?);', (title,))
        c.execute('CREATE TABLE "%s" (content TEXT, user TEXT);' %(title))
    add_to_story(title, content, user)
    db.close()

# Adds a line to the existing story
def add_to_story(title, content, user):
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute('SELECT * FROM "%s" WHERE user = "%s";' %(title,user))
    result = c.fetchall()
    if result == []:
        c.execute('INSERT INTO "%s" VALUES("%s", "%s");' %(title,content,user))
    else:
        return "You have already added to this story."
    db.commit()
    db.close()

def edited(title, user):
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute('SELECT * FROM "%s" WHERE user = "%s";' %(title,user))
    result = c.fetchall()
    if result == []:
        return False
    else:
        return True

def get_stories():
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute('SELECT * FROM stories')
    result = c.fetchall()
    db.close()
    return result

# Returns the latest line of the story if the user has not added
# Returns the entire story if the user has added
def get_story(title, user):
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute('SELECT * FROM "%s" WHERE user=\'%s\';' %(title, user))
    result = c.fetchall()
    if result == []:
        c.execute('SELECT content FROM "%s"' %(title))
        result = c.fetchall()
        db.close()
        return result[-1][0]
    else:
        c.execute('SELECT content FROM "%s"' %(title))
        result = c.fetchall()
        s = ""
        for content in result:
            s = s + content[0] + ' '
        db.close()
        return s

def get_ran_story():
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute('SELECT * FROM stories ORDER BY RANDOM() LIMIT 1;')
    resultt = c.fetchall()
    c.execute('SELECT * FROM "%s"' %(resultt[0]))
    resultl = c.fetchall()
    db.close()
    return resultt, resultl
