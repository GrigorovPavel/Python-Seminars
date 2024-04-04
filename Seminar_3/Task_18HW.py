# Задача 18: 
# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 6
# -> 5

# Решение из интернета
list_1 = [1, 2, 3, 4, 5]
k = 6
find_num = list_1[1]
for i in range(len(list_1)):
    if list_1[i] >= k and list_1[i] - k <= find_num - k:
        find_num = list_1[i]
    elif list_1[i] <= k and find_num - k <= list_1[i] - k:
        find_num = list_1[i]
print(find_num)

#  Решение из разбора домашнего задания
import random

list_1 = [random.randint(1, 10) for i in range(10)]
print(list_1)
k = int(input("Введите число: "))

# функция abs() выводит значение по модулю (убирает минус если значение отрицательное)
distance = abs(list_1[0] - k) # это наша минимальная (стартовая) дистанция до указанного элемента 'k'
max_num = list_1[0]

# Пройти по элементам списка
for num in list_1:
    if distance > abs(num - k):
        distance = abs(num -k)
        max_num = num
print(max_num)


# Пройти по индексам списка
for i in range(len(list_1)):
    if distance > abs(list_1[i] - k):
        distance = abs(list_1[i] - k)
        max_num = list_1[i]
print(max_num)