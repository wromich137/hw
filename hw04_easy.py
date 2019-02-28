import random

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

my_list = []
i = 0

while i < 5:
    my_list.append(random.randint(1,99))
    i += 1


print(my_list)
my_list = [x ** 2 for x in my_list]
print(my_list)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits1 = ["яблоко", "банан", "абрикос", "груша", "вишня"]
fruits2 = ["яблоко", "черешня", "абрикос", "апельсин", "вишня"]
my_list = []
for fruit1 in fruits1:
    for fruit2 in fruits2:
        if fruit1 == fruit2:
            my_list.append(fruit1)
        else:
            continue

print(my_list)
    

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

my_list = []
i = 0

while i < 5:
    my_list.append(random.randint(1,99))
    i += 1

my_list = [6, -3, 4, 16, -24, 3]
my_list_new = []
for digit in my_list:
    if digit % 3 == 0 and digit > 0 and digit % 4 != 0:
        my_list_new.append(digit)

print(my_list_new)




