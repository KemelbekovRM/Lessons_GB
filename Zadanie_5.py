# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('hw_5.txt', 'w') as f:
    print(input('Вводите числа, через пробел: '), file=f)

with open('hw_5.txt', 'r') as f:
    content = f.read()
    summa = 0
    for i in content.split(' '):
        if i.isdigit():
            summa = summa + int(i)

    print(f"Сумма числе в файле: {summa}")