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

 #Чтобы проверить, что бд правильно создается удалите файл zarplata.db
'''
cur.execute("INSERT INTO anketa VALUES(1, 'Иван', 'Медведев', '2005-08-04', 'мужской', '2023-03-22', 'Программист', 'IT', '100000')")
cur.execute("INSERT INTO anketa VALUES(2, 'Михаил', 'Петров', '1990-03-06', 'мужской', '2020-06-19', 'Менеджер', 'Отдел продаж', '73000')")
cur.execute("INSERT INTO anketa VALUES(3, 'Оксана', 'Селезнева', '1973-12-02', 'женский', '2019-04-12', 'Менеджер', 'Отдел кадров', '68000')")
cur.execute("INSERT INTO anketa VALUES(4, 'Иван', 'Свешников', '1999-05-03', 'мужской', '2022-09-02', 'Программист', 'IT', '110000')")
cur.execute("INSERT INTO anketa VALUES(5, 'Юрий', 'Кобелев', '1976-04-16', 'мужской', '2018-05-13', 'Директор', 'Агротехнический комлпекс', '150000')")
cur.execute("INSERT INTO anketa VALUES(6, 'Евгений', 'Касьянов', '2002-07-13', 'мужской', '2023-03-17', 'Главный Бухгалтер', 'Агротехнический комлпекс', '90000')")
cur.execute("INSERT INTO anketa VALUES(7, 'Макс', 'Зубков', '1999-01-13', 'мужской', '2023-09-12', 'Бухгалтер', 'Агротехнический комлпекс', '70000')")
cur.execute("INSERT INTO anketa VALUES(8, 'Василиса', 'Романова', '1997-07-18', 'женский', '2018-05-18', 'Секретарша', 'Отдел кадров', '83000')")
cur.execute("INSERT INTO anketa VALUES(9, 'Елизавета', 'Романова', '1996-04-23', 'женский', '2019-04-30', 'Бухгалтер', 'Отдел кадров', '86000')")
cur.execute("INSERT INTO anketa VALUES(10, 'Виктория', 'Попова', '2000-11-22', 'женский', '2021-06-27', 'Программист', 'IT', '89000')")



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
#SQL-Запросы на выборку данных
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
for i in cur.execute("SELECT id,id_workers from lists where data_start > '2023-03-01' AND data_start < '2023-03-31'"):
    print(i)
print('\n')

#Задание 8
for i in cur.execute("SELECT AVG(basic_rate) from anketa"):
    print(i)
print('\n')
#Задание 9
for i in cur.execute("SELECT name, last_name, basic_rate from anketa where basic_rate >= '100000'"):
    print(i)
print('\n')
#Задание 10
for i in cur.execute("SELECT name, last_name, data_start, data_end from anketa, lists where anketa.id = lists.id_workers"):
    print(i)
print('\n')
#Задание 11 #Текущий месяц будет 07
for i in cur.execute("SELECT name, last_name, reason, diagnosis, paidf from anketa,lists where anketa.id = lists.id_workers and data_start > '2023-07-01' and data_start < '2023-07-30'"):
    print(i)
#Задание 12

#Задание 13

#Задание 14

#Задание 15


con.commit()
con.close()

# SQL-Запросы на обновление данных
#Результаты смотреть в zarplata_upd.db
con2 = sq.connect('zarplata_upd.db')
cur2 = con2.cursor()
#Задача 1
cur2.execute("UPDATE anketa SET basic_rate='72325' WHERE basic_rate='68000'")
#Задача 2
cur2.execute("UPDATE anketa SET departament='Отдел кадров' WHERE data_birthday <= '1990-01-01'")
#Задача 3
cur2.execute("UPDATE anketa SET date_hiring='2023-04-22' WHERE id='1' ")
#Задача 4
cur2.execute("UPDATE lists SET reason='операция' WHERE id_workers='9' ")

#Задача 5
#cur.execute("UPDATE lists SET reason='операция' WHERE id_workers='9' ")
#Задача 6
#Задача 7 Отдел бухгалтерия заменено на занимающий пост Бухгалтер
#cur.execute("UPDATE lists  INNER JOIN  anketa  ON anketa.id = lists.id_workers SET reason='обед' WHERE post = 'Бухгалтер'")
con2.commit()
con2.close()



#Запросы на  удаление данных MYSQL(результаты смотреть в zarplata_del.db

con1 = sq.connect('zarplata_del.db')
cur1 = con1.cursor()

#Задача 1
cur1.execute("DELETE FROM anketa WHERE name='Иван'")

#Задача 2
cur1.execute("DELETE FROM anketa WHERE last_name='Петров'")

#Задача 3
cur1.execute("DELETE FROM anketa WHERE post='Менеджер'")

#Задача 4
cur1.execute("DELETE FROM anketa WHERE departament='Отдел кадров'")

#Задача 5
cur1.execute("DELETE FROM anketa WHERE sex='женский'")

#Задача 6
cur1.execute("DELETE FROM anketa where data_birthday >= '1973-01-01'")

#Задача 7

con1.commit()
con1.close()
