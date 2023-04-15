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

'''cur.execute("INSERT INTO anketa VALUES(1, 'Иван', 'Медведев', '08.04.2005', 'мужской', '2023-03-22', 'Программист', 'IT', '100000')")
cur.execute("INSERT INTO anketa VALUES(2, 'Михаил', 'Петров', '03.06.1990', 'мужской', '2020-06-19', 'Менеджер', 'Отдел продаж', '73000')")
cur.execute("INSERT INTO anketa VALUES(3, 'Оксана', 'Селезнева', '09.12.1973', 'женский', '2019-04-12', 'Менеджер', 'Отдел кадров', '68000')")
cur.execute("INSERT INTO anketa VALUES(4, 'Иван', 'Свешников', '03.05.1999', 'мужской', '2022-09-02', 'Программист', 'IT', '110000')")
cur.execute("INSERT INTO anketa VALUES(5, 'Юрий', 'Кобелев', '16.04.1976', 'мужской', '2018-05-13', 'Директор', 'Агротехнический комлпекс', '150000')")
cur.execute("INSERT INTO anketa VALUES(6, 'Евгений', 'Касьянов', '12.07.2002', 'мужской', '2023-03-17', 'Главный Бухгалтер', 'Агротехнический комлпекс', '90000')")
cur.execute("INSERT INTO anketa VALUES(7, 'Макс', 'Зубков', '13.01.1999', 'мужской', '2023-09-12', 'Бухгалтер', 'Агротехнический комлпекс', '70000')")
cur.execute("INSERT INTO anketa VALUES(8, 'Василиса', 'Романова', '18.07.1997', 'женский', '2018-05-18', 'Секретарша', 'Отдел кадров', '83000')")
cur.execute("INSERT INTO anketa VALUES(9, 'Елизавета', 'Романова', '23.04.1996', 'женский', '2019-04-30', 'Бухгалтер', 'Отдел кадров', '86000')")
cur.execute("INSERT INTO anketa VALUES(10, 'Виктория', 'Попова', '22.11.2000', 'женский', '2021-06-27', 'Программист', 'IT', '89000')")


cur.execute("INSERT INTO lists VALUES('100', '1', '2023-03-12', '2023-03-19', 'болезнь', 'простуда', 'YES')")
cur.execute("INSERT INTO lists VALUES('101', '1', '2023-07-14', '2023-07-16', 'болезнь', 'ОРВИ', 'NO')")
cur.execute("INSERT INTO lists VALUES('102', '2', '2020-09-10', '2020-09-30', 'болезнь', 'простуда', 'YES')")
cur.execute("INSERT INTO lists VALUES('103', '5', '2023-07-18', '2023-07-27', 'болезнь', 'COVID', 'YES')")
cur.execute("INSERT INTO lists VALUES('104', '3', '2021-05-13', '2021-05-21', 'болезнь', 'ангина', 'YES')")
cur.execute("INSERT INTO lists VALUES('105', '4', '2017-03-10', '2017-03-23', 'болезнь', 'простуда', 'NO')")
cur.execute("INSERT INTO lists VALUES('106', '6', '2017-01-04', '2021-04-07', 'болезнь', 'тонзиллит', 'YES')")
cur.execute("INSERT INTO lists VALUES('107', '7', '2023-08-03', '2023-08-11', 'болезнь', 'простуда', 'YES')")
cur.execute("INSERT INTO lists VALUES('108', '8', '2019-12-05', '2019-12-10', 'болезнь', 'бронхит', 'YES')")
cur.execute("INSERT INTO lists VALUES('109', '8', '2020-01-01', '2020-01-09', 'болезнь', 'простуда', 'NO')")
cur.execute("INSERT INTO lists VALUES('110', '9', '2021-04-12', '2021-12-02', 'болезнь', 'туберкулез', 'YES')")
'''
#Выборка данных
#Задание 1
for result in cur.execute("SELECT name, last_name , post  from anketa"):
    print(result)
print('\n')
#Задание 2
for result in cur.execute("SELECT name, last_name, basic_rate from anketa"):
    print(result)
print('\n')
#Задание 3
for i in cur.execute("SELECT name, last_name, departament from anketa where departament='IT'"):
    print(i)
print('\n')
#Задание 4
for i in cur.execute("SELECT name, last_name, date_hiring from anketa where date_hiring  >= '2022-01-01'"):
   print(i)
print('\n')
#Задание 5  id сотрудника заменено на 8
for i in cur.execute("SELECT * from lists where id_workers='8'"):
    print(i)
print('\n')
#Задание 6
for res in cur.execute("SELECT * from lists where paidf='YES'"):
    print(res)
print('\n')
#Задание 7
'''for res in cur.execute("SELECT id_workers, data_start='2023-03-01' between data_start='2023-03-31' from lists"):
    print(res)'''
print('\n')
#Задание 8
for i in cur.execute("SELECT AVG(basic_rate) from anketa"):
    print(i)
print('\n')
#Задание 9
for i in cur.execute("SELECT name, last_name, basic_rate from anketa where basic_rate >= '100000'"):
    print(i)
#Задание 10

#Задание 11

#Задание 12

#Задание 13

#Задание 14

#Задание 15


con.commit()
con.close()

