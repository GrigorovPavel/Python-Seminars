# Задача №25. 
# Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

lst = input("Введите строку через пробел: ").split() # запрашиваем у пользователя ввод строки через пробел с помощю ф-ии .split()
print(lst)
# Чтобы хранить для каждого элемента свой счетчик (count) будем использовать СЛОВАРИ
# Тоесть 'буква' - КЛЮЧ а количество повторений - ЗНАЧЕНИЕ
result = dict()
for i in lst:
    if i in result.keys():
        print(f"{i}_{result[i]}", end = " ") # ,end = " " - для вывода в одну строку через пробел. Или указать символ ","
        result[i] += 1
    else:
        print(i, end = " ")
        result[i] = 1


# Решение через строку
result = dict()
new_result = ""
for i in lst:
    if i in result.keys():
        new_result += f"{i}_{result[i]}"
        result[i] += 1
    else:
        new_result += i
        result[i] = 1
    new_result += " "
print("\n")
print(new_result)


# Решение через список
result = dict()
new_result = []
for i in lst:
    if i in result.keys():
        new_result.append(f"{i}_{result[i]}")
        result[i] += 1
    else:
        new_result.append(i)
        result[i] = 1
    # new_result += " "
# print("\n")
print(" ".join(new_result)) # .join добавляет пробел между элементами
