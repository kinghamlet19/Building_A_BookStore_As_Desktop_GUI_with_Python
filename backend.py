import sqlite3

def connect():
    conn = sqlite3.connect('book.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    con = sqlite3.connect('book.db')
    cur = con.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
    con.commit()
    con.close()

def view():
    con = sqlite3.connect('book.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    con.close()
    return rows


def search(title="", author="", year="", isbn=""):
    con = sqlite3.connect('book.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    con.close()
    return rows

def delete(id):
    con = sqlite3.connect('book.db')
    cur = con.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    con.commit()
    con.close()
    
def update(id,title, author, year, isbn):
    con = sqlite3.connect('book.db')
    cur = con.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn,id))
    con.commit()
    con.close()
    


connect()

