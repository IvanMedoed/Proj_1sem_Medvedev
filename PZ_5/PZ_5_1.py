# Составить программу, в которой функция построит изображение в котором в первой строке 1 звездочка, во второй  - 2
# в третьей -3, ..., в строке с номером m - m звездочек.


def Star(n):  #Функция Star  строит изображение, в котором в первой строке 1 звездочка, во второй - 2 и т.д
    i = 0
    while type(n) != int:  # обработка исключений
        try:
            n = int(n)
        except ValueError:
            print("Неправильно ввели ")
            n = input("Введите число => ")
    while i < n:
        i += 1
        c = i * '*'
        print(c)
Star(input('Введите число =>'))

