# 25. Напишите программу, которая принимает на вход строку, и отслеживает количество повторов каждого символа.
from collections import Counter

# 27. Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки. Определите, сколько различных
# слов содержится в этом тексте.


input_str = input("Введите строку: ") + " "
characters_count = {}
for char in input_str:
    if char in characters_count:
        characters_count[char] += 1
    else:
        characters_count[char] = 1
print(characters_count)



