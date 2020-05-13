import sqlite3
from os import path

ROOT = path.dirname(path.relpath((__file__)))

def create_post(name, content):
    con = sqlite3.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('INSERT INTO posts (name, content) VALUES(?, ?)', (name, content))
    con.commit()
    con.close()

def get_posts():
    con = sqlite3.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('SELECT * FROM posts')
    posts = cur.fetchall()
    return posts
