#24BookDB.py

import sqlite3

def createTable():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE book_table (
            idx     integer primary key,
            title   text,
            year    integer,
            company text,
            pages   integer,
            exist_flag integer,
            price   integer            
        )  '''
    )

    conn.commit()
    conn.close()

if __name__ == "__main__":
    createTable()