#Из предложенного текстового файла(text18-17.txt) вывести на экран его содержимое, количество знаков препинания. Сформировать новый файл,
# в который поместить текст в стихотворной форме предварительно поставив последнюю строку между первой и второй.

li = [',', '—', ':', '.', '!']
d = 0
t = 0
for i in open('text18-17.txt', encoding='UTF-16'):
    print(i)
    for j in i:
        if j == li[0] or j == li[1] or j == li[2] or j == li[3] or j == li[4]:
            d += 1
print(end='\n')
print('Количество знаков препинания:  ', d, end='\n')
f1 = open('text18-17.txt', encoding='UTF-16')
l = f1.readlines()
l[6] = 'Не отдали б Москвы!\n'
l.insert(1, l[6])
print(end='\n')
f1.close()

f2 = open('text18-17_2.txt', 'w')
f2.writelines(l)
f2.close()