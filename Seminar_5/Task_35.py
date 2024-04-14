# Задача №35. 
# Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)

# Input: 5
# Output: yes 


n = int(input("Введите число: "))
if n == 2 or n == 3 or n == 5 or n == 7:
    print("Число 'Простое' ")
elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
    print("Число 'Сложное' ")
else:
    print("Число 'Простое' ")


# Решение через функцию (более правильное)
def digit(n):
    n = int(input("Введите число: "))
    for i in range(2, n //2 ): # n//2 для сокращения повторов цикла
        print(i)
        if n % i == 0:
            return "no"
    return "yes"
       
print(digit(n))   
