"""
Задача 10: 
На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.
"""

coins = [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1]
count1 = 0
count2 = 0

for item in coins:
    if coins[item] == 0:
        count1 += 1
    else:
        count2 += 1

if count1 > count2:
    print(count2)
else:
    print(count1)


