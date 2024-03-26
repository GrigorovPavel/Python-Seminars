#  Примеры

lst = [1, 3, 6, 22]
for item in lst: # если необходимо пройти по всем элементам
    print(item)

for i in range(1, len(lst)): # если необходимо пройти по определенным элементая
    print(lst[i])

count = 0
while (count < len(lst)):
    print(lst[count])
    count += 1

# Операторы break и continue
a = 0
while(a >= 0):
    a += 1
    if(a == 10):
        break # если выполняется условие, то цикл завершается
    if(a % 2 != 0):
        continue # если выполняется условие то цикл начинается заново (указанное ниже, не выполняется)
    print(a)