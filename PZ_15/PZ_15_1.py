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

cur.execute("INSERT INTO anketa VALUES(1, 'Иван', 'Медведев', '08.04.2005', 'мужской', '22.02.2023', 'Программист', 'IT', '100000')")

cur.execute("INSERT INTO lists VALUES('100', '1', '12.03.2023', '19.03.2023', 'болезнь', 'простуда', 'YES')")
con.commit()

con.close()
