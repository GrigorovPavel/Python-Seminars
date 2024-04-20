# Квиз - интелектуальная игра

import random
# 1. Есть код:
numbers = []
for i in range(5):
    numbers.append(random.randint(1, 100))
print(numbers)  
# как записать этот код короче с помощю 'list comprehension'-(генератора списков)
numbers = [random.randint(1, 100) for i in range(5)]
print(numbers)

# 2. Есть код:
def is__odd(number: int):  # int - подсказка типа данных, не обязательно
    if number % 2 == 1:
        return False
    return True
print(is__odd(12))
# как написать эту функцию в lambda виде?
is_odd = lambda number: number % 2 == 1
print(is__odd(7))

# 3. Есть код:
numbers = [random.randint(1, 100)for i in range(5)]
print(numbers)
# как вывести только четные числа использая нашу функцию is_odd
print(list(filter(is__odd, numbers)))

# 4. Есть код:
lst = ['a', 'b']
lst2 = list(enumerate(lst, 1)) # enumerate - добавляет нумерацию к элементам списка
print(lst2) # [(1, 'a'), (2, 'b')]

# 5. Есть код:
num1 = [2, 4, 6, 8, 10, 12]
num2 = [58, 46, 34, 22, 10, 8]
# как сложить элементы списков и вывести новый список
res_lst = list(map(lambda a, b : a + b, num1, num2))
print(res_lst)
# Или таким способом, с помощю функции zip
res_lst = []
for num1, num2 in zip(num1, num2):
    res_lst.append(num1 + num2)
print(res_lst) 

# 6. Есть код:
from math import factorial
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# как применить функцию factorial к каждому элементу списка
res_lst = list(map(factorial, numbers))
print(res_lst)
