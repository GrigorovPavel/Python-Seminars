# Задача №41. 
# Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

# Ввод: 5 
# 1 2 3 4 5
# Вывод: 0

# Ввод:5
# 1 5 1 5 1
# Вывод:2

def creat_arr(): # Создание массива
    num_elem = int(input("Введите количество элементов:"))
    for i in range(num_elem):
        if num_elem > 0:
            elem = input("Введите элемент: ")
            arr.append(elem)
    return arr

def num_elements(arr): # Проверка соседних элемента меньше данного
    counter = 0
    for i in range(1, len(arr) - 1):
        if arr[i - 1] < arr[i] > arr[i + 1]:
            counter += 1
    return print(counter)

arr = []

creat_arr()
print(arr)
num_elements(arr)



