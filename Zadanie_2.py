# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.

spisok = [66, 67, 54, 56, 5, 90 ,6 ,67]
new_spisok = [spisok[num] for num in range(1, len(spisok)) if spisok[num] > spisok[num - 1]]
print(new_spisok)