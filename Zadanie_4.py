# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.

with open('hw_4.txt', 'r') as f:
    content = f.read()
    print(f'{content}')

with open('hw_4_new.txt', 'w') as f:
    content = content.replace('One', 'Один')
    content = content.replace('Two', 'Два')
    content = content.replace('Three', 'Три')
    content = content.replace('Four', 'Четыре')
    f.writelines(content)