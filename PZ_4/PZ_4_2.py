#Даны положительные числа А И В(A<B). На отрезке длины А размещено максимально возможное количество отрезков длины Б (без наложений)
#Не используя операции умножения и деления, найти длину незанятой части отрезка А.

a = input('Введите длину отрезка А=>')
b = input('Введите длину отрезка B=>')


while (type(a) != int) & (type(b) != int): #обработка исключений
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Неправильно ввели")
        a = input("Введите длину отрезка А=>")
        b = input("Введите длину отрезка B=>")

while a>=b:
    a-=b
print(a)