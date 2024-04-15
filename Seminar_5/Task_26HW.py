# Задача 26: 
# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def exponentiat(a, b):
    if b == 0:
        return 1 
    return a * exponentiat(a, b-1)

print(exponentiat(3, 5))  


# Для автотестов
def f(a, b):
    if b == 0:
        return 1 
    return a * f(a, b-1)

a = 2
b = 3
print(f(a, b))