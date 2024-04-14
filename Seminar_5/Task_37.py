# Задача №37. 
# Решение в группах
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3


n = int(input("Введите число элементов:"))
def revers_values(n):
    num = input("Введите число:")
    if n == 1:
        return num
    return revers_values(n - 1) + num
    
print(revers_values(n))  
        

# Решение через random
import random
n = int(input("Введите число элементов:"))
lst = []
def revers_values(n):
    num = str(random.randint(1, 10))
    print(num, end= " ")
    if n == 1:
        print("\n") # для наглядности
        return num
    return revers_values(n - 1) + " " + num 
      
print(revers_values(n))  
