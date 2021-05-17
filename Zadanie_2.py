# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры
# как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def polsovatel(**kwargs):
    return " ".join(kwargs.values())


name = input("Введите имя: ")
surname = input("Введите фамилия: ")
birtday = input("Введите дат у рождения: ")
city = input("Введите город проживания: ")
email = input("Введите адрес электронной почты: ")
telephone = input("Введите телефон: ")

print(polsovatel(name=name, surname=surname, birtday=birtday, city=city, email=email, telephone=telephone))