# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# # *Пример:*
# # 5
#     1 2 3 4 5
#     6
#     -> 5
import random

input_list = list(set([random.randint(1, 20) for _ in range(20)]))
print(input_list)

first_max = input_list[0]
second_max = input_list[1]

for i in input_list:
    if i > first_max:
        second_max = first_max
        first_max = i
    elif i > second_max and i != first_max:
        second_max = i

print(second_max)

