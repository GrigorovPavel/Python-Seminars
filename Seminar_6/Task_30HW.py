# Задача 30: 
# Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Ввод: 7 2 5 (с какого значения начать, с каким шагом идем, сколько элементов в массиве)
# Вывод: 7 9 11 13 15


# def progres():
start_elem = int(input("Введите зеачение первого элемента: "))
difference = int(input("Введите зеачение разности: "))
arr = int(input("Введите количество элементов в массиве: "))
result_arr = []
for i in range(arr + 1):
    if i > 0:
        result_arr.append(start_elem)
        start_elem += difference
print(result_arr)

# progres()

# Решение для автотестов
# a1 = зеачение первого элемента
# d = зеачение разности
# n = количество элементов в массиве

a1 = 2
d = 3
n = 4
for i in range(n):
    if i > 0:
        a1 += d
    print(a1)    
