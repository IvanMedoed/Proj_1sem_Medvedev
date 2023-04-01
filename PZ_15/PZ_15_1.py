import sqlite3 as sq

con = sq.connect('zarplata.db')
cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS  anketa(
    id INTEGER PRIMARY KEY,
    name VARCHAR,
    last_name VARCHAR,
    data_birthday DATE,
    sex VARCHAR,
    date_hiring DATE,
    post VARCHAR,
    departament VARCHAR,
    basic_rate DECIMAL
    )""")


cur.execute("""
    CREATE TABLE IF NOT EXISTS  lists(
    id INTEGER PRIMARY KEY,
    id_workers INTEGER,
    data_start DATE,
    data_end DATE,
    reason VARCHAR,
    diagnosis VARCHAR,
    paidf BOOLEAN,
    FOREIGN KEY(id_workers) REFERENCES anketa(id) 
    )""")
con.commit()

con.close()
