#Дана строка, состоящая из русских слов, набранных заглавными буквами и разделенных пробелами(одним или несколькими)
# Вывести строку, содержащую эти же слова, разделенные одним пробелом и расположенные в алфавитном порядке.
b = 'О Б В Е  А Е Д'.split()
b.sort()
print(' '.join(b))
