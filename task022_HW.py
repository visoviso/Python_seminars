# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random
first_list = [random.randint(1,20) for i in range(10)]
second_list = [random.randint(1,20) for i in range(10)]
cross_list = {}
for i in first_list:
    for j in second_list:
        if i == j:
            cross_list[i] = i

print(f"Для множеств N: {first_list}")
print(f"Для множеств М: {second_list}")
print("в обоих множествах встречаются числа: ")
print(sorted(cross_list))
