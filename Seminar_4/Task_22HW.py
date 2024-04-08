# Задача 22: 
# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6 # количество элементов первого и второго множества
# 2 4 6 8 10 12 10 8 6 4 2 # элементы первого множества через пробел
# 3 6 9 12 15 18 # элементы второго множества через пробел
# 6 12 

# Решение через множество и список
nums1 = {2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2}
nums2 = {3, 6, 9, 12, 15, 18}
result_set = nums1.intersection(nums2)

result_str = list(result_set)
result_str.sort()

print(result_str)
print(type(result_str))



#  Решение через строку
var1 ='5 4'
var2 = '1 5 3 7 9'
var3 = '2 3 4 5'
var1 = var1.split()
# for i in range(len(var1)): # проходим по списку
#     var1[i] = int(var1[i]) # и присваиваем значениям элементов 'int' (переводив в число)
# # len1, len2 = var1 # присвоили переменным len1 и len2 значение длинны их списков (len1 - var2, len2 - var3)

# Коротко можно записать так: 
var2 = [int(num) for num in var2.split()] # для каждого числа в числах списка использоват функцию .split()
var3 = [int(num) for num in var3.split()]

result = []
for i in range(len(var2)):  # range(len1): - 31строка
    for j in range(len(var3)):  # range(len2): - 31строка
        if var2[i] == var3[j]:
            result.append(var3[j])
# print(result)
result.sort()
print(*result)
print(type(result))
# print(sorted(result)) # сортирует любые типы данных

# Можно сортировать так:
for i in range(len(result) - 1):
    if result[i] > result[i + 1]:
        result[i], result[i + 1] = result[i + 1], result[i]
print(result)