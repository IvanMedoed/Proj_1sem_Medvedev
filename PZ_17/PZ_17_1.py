#Создайте класс "Матрица", который имеет атрибуты количества строк и столбцов.
#Добавьте методы для вычисления процентных начислений и снятия денег
class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

    def percent_increase(self, amount, percentage):
        increase = amount * percentage / 100
        return amount + increase

    def withdraw_money(self, amount):
        if amount > 0:
            print(f"Снятие {amount}  долларов")
        else:
            print("Введите цифры")


# Пример использования класса:

account_balance = Matrix(1, 1)
print(account_balance.percent_increase(100, 10))  # Выведет 110.0
account_balance.withdraw_money(50)  # Выведет "Вывод 50 долларов"
account_balance.withdraw_money(-10)  # Выведет "Пожалуйста, введите действительную сумму"