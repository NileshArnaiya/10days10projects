# basic sql commands 
import sqlite3

# self explanatory
def createTable():

    query = "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)"
    connect(query, False, [])


def connect(query, details,  inserta=False):
    conn = sqlite3.connect("books.db")
    curr = conn.cursor()
    if inserta == False:
        curr.execute(query)
        conn.commit()
        conn.close()

    if inserta == True:
        curr.execute(query, (details[0], details[1], details[2], details[3]))
        conn.commit()
        return curr

    return curr


def insert(title, author, year, isbn):

    query = "INSERT INTO book VALUES (NULL,?,?,?,?)"
    details = [title, author, year, isbn]
    curr = connect(query,  details, True)
    curr.close()


def view():

    conn = sqlite3.connect("books.db")
    curr = conn.cursor()
    curr.execute("SELECT * FROM book")
    rows = curr.fetchall()
    curr.close()
    return rows


def search(title="", author="", year="", isbn=""):

    query = "SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?"
    details = [title, author, year, isbn]
    aws = connect(query,  details, True) #connect with the query only if insert operation
    return aws.fetchall()  # get all rows 


def delete(id):
    conn = sqlite3.connect("books.db")
    curr = conn.cursor()
    curr.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    curr = conn.cursor()
    curr.execute("UPDATE book SET title=?,author=? ,year=? ,isbn=? WHERE id=?",
                 (title, author, year, isbn, id))
    conn.commit()
    conn.close()


#call your operations
createTable()
#insert("Sunner","Stormasas of the Devil",1498,223363127)
delete(10)
update(9, "Mallory", "Geroge Mallory", 1850, 18281)
print(view())
print("Search is", search("Faithful"))
