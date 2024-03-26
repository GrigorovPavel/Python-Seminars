"""
Задача №11.
Решение в группах
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6
"""
# числа Фибоначи: 0, 1, 1, 2, 3, 5, 8, 13 ...
n = int(input("Введите число Фибоначи: "))

fibo_previous = 0
fibo_nex = 1
count = 2
while(n > fibo_nex):
    fibo_previous, fibo_nex = fibo_nex, fibo_nex + fibo_previous # если записать в раздельных строках, неполучится!(изменится fibo_previous)
    count += 1
if(n == fibo_nex):
    print(count)
else:
    print(-1)