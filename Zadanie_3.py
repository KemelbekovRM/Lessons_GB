# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def fun_sum(num_1, num_2, num_3):
    list = [num_1, num_2, num_3]
    try:
        list.remove(min(list))
        return sum(list)
    except TypeError:
        return "Вводите только числа"

print(fun_sum(10, 5, 6))