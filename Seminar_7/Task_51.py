# Задача №51. 
# Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его характеристику.

# Ввод: 
# values = [0, 2, 10, 6] 
# if same_by(lambda x: x % 2, values):
#     print(‘same’)
# else:
#     print(‘different’)

# Вывод:
# same

def same_by(characteristic, objects): # функция принимает два аргумента(функцию и список)
    res = list(map(characteristic, objects)) # создаем новый список, в котором применили функцию к значениям списка
    for i in range(len(res)): # проходим по элементам нового списка
        if res[i] == res[i -1]: # Если элементы равны (True)
            return True # То возвращаем True
        return False # Иначе возвращаем False


values = [0, 2, 10, 6, ]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')

   

