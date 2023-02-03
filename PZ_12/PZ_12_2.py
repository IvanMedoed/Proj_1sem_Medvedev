#Составить генератор(yield), который переведет символы строки из верхнего регистра в нижний

def strToUp(crs: str):
    for ch in crs:
        yield ch.lower()

uses_str = input('Вставьте текст => ')
print(''.join(strToUp(uses_str)))