import sqlite3 as sq
from values import *
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


#cur.executemany('INSERT INTO anketa VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', (data))
#cur.executemany('INSERT INTO lists VALUES (?, ?, ?, ?, ?, ?, ?)', (lists))
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
print('\n')
#Задание 12 #В Python в библиотеке SQL нет функций для вычисления среднего кол-во дней,
# поэтому в последующем будет показываться просто data_start и data_end
# а так было бы AVG(DATEDIFF(data_start,data_end))
for i in cur.execute("""SELECT departament, data_start, data_end from anketa,lists where anketa.id = lists.id_workers"""):
    print(i)
print('\n')
#Задание 13

#Задание 14

#Задание 15
for i in cur.execute("SELECT name, last_name, data_start, data_end from anketa, lists where anketa.id = lists.id_workers and data_start > '2023-01-01' and data_start < '2023-12-31' and data_end> '2023-01-01' and data_end < '2023-12-31'"):
    print(i)

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


#Библиотека SQLite не поддерживает INNERJOIN в UPDATE, поэтому это задание невозможно выполнить
#Задача 5
#cur.execute("UPDATE lists SET reason='операция' WHERE id_workers='9' ")
#Задача 6
#Задача 7 Отдел бухгалтерия заменено на занимающий пост Бухгалтер
#cur2.execute("UPDATE lists SET reason='обед' WHERE post = 'Бухгалтер' FROM lists AS a INNER JOIN anketa AS b ON a.id = b.id_workers")
con2.commit()
con2.close()



#Запросы на  удаление данных MYSQL(результаты смотреть в zarplata_del.db

con1 = sq.connect('zarplata_del.db')
cur1 = con1.cursor()

#Задача 1
cur1.execute('DELETE FROM lists WHERE id_workers = (SELECT DISTINCT id FROM anketa WHERE name = "Иван")')

#Задача 2
cur1.execute('DELETE FROM lists WHERE id_workers = (SELECT DISTINCT id FROM anketa WHERE last_name = "Петров")')

#Задача 3
cur1.execute('DELETE FROM lists WHERE id_workers = (SELECT id FROM anketa WHERE post = "Менеджер")')
#Задача  4
cur1.execute('DELETE FROM lists WHERE id_workers = (SELECT id FROM anketa WHERE departament = "Отдел продаж")')
#Задача 5
cur1.execute('DELETE FROM lists WHERE id_workers = (SELECT id FROM anketa WHERE sex = "женский")')
#Задача 6
cur1.execute('DELETE FROM lists WHERE id_workers = (SELECT id FROM anketa WHERE data_birthday > "1973-01-01")')
#Задача 7
cur1.execute('DELETE FROM lists WHERE  paidf = "NO"')
#Задача 8
cur1.execute('DELETE FROM lists WHERE  data_start < "2023-01-01"')
#9
cur1.execute('DELETE FROM lists WHERE  data_start > "2022-07-07"')
#10
cur1.execute('DELETE FROM lists WHERE  data_end > "2022-07-07"')
#12
cur1.execute('DELETE FROM lists WHERE id_workers = (SELECT id FROM anketa WHERE last_name LIKE "С%")')

#13
cur1.execute('DELETE FROM lists WHERE id_workers = (SELECT id FROM anketa WHERE post = "Менеджер" AND paidf = "NO")')

#14
cur1.execute('DELETE FROM lists WHERE id_workers = (SELECT id FROM anketa WHERE departament = "IT" AND data_end > "2023-01-01")')

con1.commit()
con1.close()
