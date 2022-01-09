import sqlite3

def create_table():
    con = sqlite3.connect('lite.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    con.commit()
    con.close()

def insert(item, quantity, price):
    con = sqlite3.connect('lite.db')
    cur = con.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)", (item, quantity, price))
    con.commit()
    con.close()

#insert('Coffe cups', 3, 8.5)


def view():
    con = sqlite3.connect('lite.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    con.close()
    return rows


def delete(item):
    con = sqlite3.connect('lite.db')
    cur = con.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    con.commit()
    con.close()
    
def update(quantity, price,item):
    con = sqlite3.connect('lite.db')
    cur = con.cursor()
    cur.execute("UPDATE store SET quantity =?, price =? WHERE item =?", (quantity, price,item))
    con.commit()
    con.close()
    
update(11, 20.20, 'Wine Glass')
#insert('Cup', 12, 22.50)
print(view())