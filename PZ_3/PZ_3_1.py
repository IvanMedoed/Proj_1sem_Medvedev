#Разработать программу, выводящее на экран строку «Данное число является четным двузначным», если вводимое число является четным двузначным
t = input('Введите целое число =>')

while type(t) != int: # обработка исключений
    try:
        t = int(t)
    except ValueError:
        print('Неправильно значение')
        t = input('Введите целое число =>')

if ((t >= 10 and t <= 99) or (t <= -10 and t >= -99)) and (t % 2 == 0):
     print('Данное число является четным двузначным ')
else:
    print('Неверно')