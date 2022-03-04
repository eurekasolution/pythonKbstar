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

def insertBooks():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()

    sql = "insert into book_table (title, year, company, pages, exist_flag, price) " \
          "values (?, ?, ?, ?, ?, ? )"
    #cur.execute(sql, ('자바', '2020', '하나은행', '300', '1', '12000') )

    #cur.execute("insert into book_table (title, year, company, pages, exist_flag, price) "
    #            "values ('파이썬', '2022', '국민은행', '1234', '1', '12000'  )")

    books = [
        ('책제목1', '2020', '국민은행', '3456', '0', '8000'),
        ('책제목2', '2010', '국민은행', '356', '1', '7000'),
        ('책제목3', '2021', '국민출판', '656', '0', '18000'),
        ('책제목4', '2020', '하나출판', '340', '1', '12000'),
        ('책제목5', '2018', '신한출판', '956', '1', '23000')
    ]

    cur.executemany(sql, books)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    #createTable()
    print("Insert...")
    insertBooks()
