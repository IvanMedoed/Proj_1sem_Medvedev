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
cur.execute("INSERT INTO anketa VALUES(2, 'Михаил', 'Петров', '03.06.1990', 'мужской', '19.06.2020', 'Менеджер', 'Отдел продаж', '73000')")
cur.execute("INSERT INTO anketa VALUES(3, 'Оксана', 'Селезнева', '09.12.1973', 'женский', '12.04.2019', 'Менеджер', 'Отдел кадров', '68000')")
cur.execute("INSERT INTO anketa VALUES(4, 'Иван', 'Свешников', '03.05.1999', 'мужской', '02.09.2022', 'Программист', 'IT', '110000')")
cur.execute("INSERT INTO anketa VALUES(5, 'Юрий', 'Кобелев', '16.04.1976', 'мужской', '13.05.2018', 'Директор', 'Агротехнический комлпекс', '150000')")
cur.execute("INSERT INTO anketa VALUES(6, 'Евгений', 'Касьянов', '12.07.2002', 'мужской', '17.03.2023', 'Главный Бухгалтер', 'Агротехнический комлпекс', '90000')")
cur.execute("INSERT INTO anketa VALUES(7, 'Макс', 'Зубков', '13.01.1999', 'мужской', '12.09.2023', 'Бухгалтер', 'Агротехнический комлпекс', '70000')")
cur.execute("INSERT INTO anketa VALUES(8, 'Василиса', 'Романова', '18.07.1997', 'женский', '28.05.2018', 'Секретарша', 'Отдел кадров', '83000')")
cur.execute("INSERT INTO anketa VALUES(9, 'Елизавета', 'Романова', '23.04.1996', 'женский', '30.04.2019', 'Бухгалтер', 'Отдел кадров', '86000')")
cur.execute("INSERT INTO anketa VALUES(10, 'Виктория', 'Попова', '22.11.2000', 'женский', '06.03.2021', 'Программист', 'IT', '89000')")


cur.execute("INSERT INTO lists VALUES('100', '1', '12.03.2023', '19.03.2023', 'болезнь', 'простуда', 'YES')")
cur.execute("INSERT INTO lists VALUES('101', '1', '14.07.2023', '20.07.2023', 'болезнь', 'ОРВИ', '')")
cur.execute("INSERT INTO lists VALUES('102', '2', '10.09.2020', '30.09.2020', 'болезнь', 'простуда', 'YES')")
cur.execute("INSERT INTO lists VALUES('103', '5', '18.07.2023', '27.07.2023', 'болезнь', 'COVID', 'YES')")
cur.execute("INSERT INTO lists VALUES('104', '3', '13.05.2021', '20.05.2021', 'болезнь', 'ангина', 'YES')")
cur.execute("INSERT INTO lists VALUES('105', '4', '10.03.2017', '23.03.2017', 'болезнь', 'простуда', '')")
cur.execute("INSERT INTO lists VALUES('106', '6', '01.04.2017', '7.04.2021', 'болезнь', 'тонзиллит', 'YES')")
cur.execute("INSERT INTO lists VALUES('107', '7', '03.08.2023', '11.08.2023', 'болезнь', 'простуда', 'YES')")
cur.execute("INSERT INTO lists VALUES('108', '8', '05.12.2019', '10.12.2019', 'болезнь', 'бронхит', 'YES')")
cur.execute("INSERT INTO lists VALUES('109', '8', '01.01.2020', '9.01.2020', 'болезнь', 'простуда', '')")
cur.execute("INSERT INTO lists VALUES('110', '9', '04.02.2021', '12.02.2021', 'болезнь', 'туберкулез', 'YES')")


cur.execute("SELECT name, last_name , post  from anketa")
for result in cur:
    print(result)

con.commit()

con.close()

