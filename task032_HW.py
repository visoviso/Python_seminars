# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)


import random

min_elem = int(input("Введите минимальное значение диапазона вывода:  "))
max_elem = int(input("Введите максимальное значение диапазона вывода:  "))

elem_list = [random.randint(1, 20) for i in range(20)]
print(elem_list)

for i in range(len(elem_list)):
    if min_elem <= elem_list[i] <= max_elem:
        print(f'Индекс {i}: Значение {elem_list[i]}')
