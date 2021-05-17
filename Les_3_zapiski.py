# функция
# def my_function(num_1, num_2):
#     print("lalanum_1")
#     print(num_1 + num_2)
#     #return num_1 + num_2
#
# a = my_function(10, 56)
# print(a)
# a = my_function(20, 50)
# print(type(a))

# def fun_2(num1, num2, *args, c=55, **kwargs):     #можно задать по умолчанию
#     print(f'num1 - {num1}')
#     print(f'num2 - {num2}')
#
# fun_2(num2=100, num1=30)

# Функция Print
# print("hello", 1123, sep="РАЗДЕЛИТЕЛЬ", end=" перенос строки ")
# print("hello", 1123, sep="РАЗДЕЛИТЕЛЬ", end=" перенос строки ")

# Анонимные функции
# f = lambda a, b: a + b
# res = f(10, 3)
# print(res)

#
# def func(a, b):
#     c = a+ b
#     return c
# x = func
# print(x(10, 50))

#
a = ["10", "20", "30"]
new = list(map(lambda x: int(x) ** 2, a))
print(new)

