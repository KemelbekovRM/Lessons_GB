# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def function(num_1, num_2):
    try:
        num_1, num_2 = int(num_1), int(num_2)
        div_num = num_1 / num_2
    except ValueError:
        return "Ошибка, введено неверное значение."
    except ZeroDivisionError:
        return "Ошибка деления на 0"
    return round(div_num, 4)

print(function(input("Введите первое число: "), input("Введите второе число: ")))