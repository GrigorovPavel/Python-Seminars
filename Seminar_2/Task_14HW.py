"""
Задача 14: 
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
10 -> 1 2 4 8
"""

n = 10
k = 1
print(k) # топорное решение (перемудрил!)
while k*2 < n:
    k *= 2
    print(k)

# нормальное решение
n = 10
a = 1
while n >= a:
    print(a)
    a *=2