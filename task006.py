# 6. описание числа
# пользователь вводит целове число. введите его строку -описание вида " отрицательное четное число, ноль
# положительное нечетное число, например численным описание числа 190 является строка положительное четное число"
number = int(input("введите число : "))
if number % 2 == 0 and number < 0:
    print("отрицательное четное число")
elif number == 0:
    print("Ноль")
elif number % 2 != 0 and number < 0:
    print("отрицательное нечетное число")
elif number % 2 == 0 and number > 0:
    print("положительное четное число")
else :
    print("положительное нечетное число")