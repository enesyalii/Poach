import sqlite3 

con = sqlite3.connect("bans.db")
cur = con.cursor()

def badword(person):
    cur.execute('INSERT INTO bans (person, count) VALUES (?, 1)', (person,))
    con.commit()