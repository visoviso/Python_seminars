# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести
# с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.



input_a1 = int(input("Введите число a(первый элемент):  "))
input_d = int(input("Введите число (разность):  "))
input_n = int(input("Введите число (кол-во элементов):  "))
def arf_prog(a1, d, n: int):

    arithmetic_progression = []
    an = 0

    for i in range(n):
        an = a1 + i * d
        arithmetic_progression.append(an)
    return arithmetic_progression

print(arf_prog(input_a1, input_d, input_n))
