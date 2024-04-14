# Задача №31. 
# Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1 , ..., an , ..., где a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

def fibonachi(n):
    if n - 2 <= 1:
        return n
    return fibonachi(n - 1) + fibonachi(n - 2)
print(fibonachi(7))

# Еще простой пример Рекурсии
def investor(rub):
    print(rub)
    if rub >= 10:
        return rub
    return investor(rub + 1)

investor(3)