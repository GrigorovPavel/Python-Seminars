# Задача №33. 
# Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.

# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

lst = [1, 3, 3, 3, 4]
print(lst)
min = 5
max = 1
for i in range(len(lst)):
    if lst[i] > max:
        max = lst[i]
    if lst[i] < min:
        min = lst[i]
# Выбираем любой вариант
# Проходим по элементам списка
for elem in lst:
    if lst[elem] == max:
        lst[elem] = min
# Проходим по индексам элементов
for i in range(len(lst)):
    if lst[i] == max:
        lst[i] = min

print(f"min -> {min}")
print(f"max -> {max}")
print(lst)
