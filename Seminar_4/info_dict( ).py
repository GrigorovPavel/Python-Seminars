
# Словарь
# Как взаимодействовать с данными в словаре

contacts = {
    "Вася": 540510,
    "Петя": 253012,
    "Дима": 351178,
    "Коля": 545079
} # Создали словарь

for i in  contacts: # Проходим 'i' по словарю и выводим КЛЮЧИ
    print(i)

for key in contacts.keys(): # Проходим 'key' по КЛЮЧАМ словаря с помощю функции .keys
    print(key)

print(contacts.keys())  # -> dict_keys(['Вася', 'Петя', 'Дима', 'Коля'])

for number in contacts.values(): # Проходим 'number' по ЗНАЧЕНИЯМ словаря с помощю функции .values
    print(number)

for cont, number in contacts.items(): # Создаем два значения
    # # Проходим 'cont' и 'number' по КЛЮЧАМ и ЗНАЧЕНИЯМ словаря с помощю функции .items()
    print(cont)
    print(number)

