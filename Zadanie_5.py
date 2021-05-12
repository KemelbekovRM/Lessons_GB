
my_rating = [1, 9, 5, 4, 8]
new_number = int(input('Введите новое натуральное число для добавления в рейтиг - '))
i = 0
for n in my_rating:
    if new_number <= n:
        i += 1
my_rating.insert(i, int(new_number))
print(my_rating)