# Задача №43. 
# Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных строках.

# Ввод: 1 2 3 2 3 

# Вывод: 2

import random

# lst = input("Введите числа через пробел:").split
# lst = [1, 2, 3, 2, 3]
# Для рандомного создания списка
lst = list()
len_lst = int(random.randint(5, 10))
for i in range(len_lst):
    if len_lst > 0:
        elem = random.randint(1, 10)
        lst.append(elem)
print(lst)

counter = 0
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] == lst[j]:
            counter += 1
            # print(counter)
print(counter)


