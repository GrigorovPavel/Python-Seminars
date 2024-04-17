# Задача №39. 
# Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: 
# 7 
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 
# (каждое число вводится с новой строки)
# Вывод:3 3 2 12


import random

# n1 = int(input("Введите количество элементов в первом массиве: "))
# lst1 = []
# for i in range(n1):
#     if n1 > 0:
#         n1_elem = input("Введите элементы первого массива: ")
#         lst1.append(n1_elem)

# n2 = int(input("Введите количество элементов в первом массиве: "))
# lst2 = []
# for i in range(n2):
#     if n2 > 0:
#         n2_elem = input("Введите элементы первого массива: ")
#         lst2.append(n2_elem)

# print(lst1)        
# print(lst2)

# result_lst = []
# for i in range(len(lst1)):
#     if lst1[i] not in lst2:
#         result_lst.append(lst1[i])

# print(result_lst)


#  Решение с random
import random

n1 = random.randint(3, 10)
lst1 = []
for i in range(n1):
    if n1 > 0:
        n1_elem = random.randint(1, 10)
        lst1.append(n1_elem)

n2 = random.randint(3, 10)
lst2 = []
for i in range(n2):
    if n2 > 0:
        n2_elem = random.randint(1, 10)
        lst2.append(n2_elem)

print(lst1)        
print(lst2)

result_lst = []
for i in range(len(lst1)):
    if lst1[i] not in lst2:
        result_lst.append(lst1[i])

print(result_lst)