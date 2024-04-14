def degree(a, b, c=1):
    if b==0:
        return c
    c=c*a
    return degree(a, b-1, c)

print(degree(2, 3))




def sign(b):
   if (b>0):
      return 1
   elif (b<0):
      return -1
   else:
      return 0


def sum(a, b):
    sign_b=sign(b)
   # sign_b = int(math.copysign(1, b))
    if b==0:
        return a
    a+=sign_b
    b-=sign_b
    return sum(a, b)

print(sum(2,2))



def factorial(end):
    if end == 1:
        return 1
    return factorial(end - 1) * end





# Задача 26:

def degree(a, b, c=1):
    if b==0:
        return c
    c=c*a
    return degree(a, b-1, c)

print(degree(2, 3))



# Задача 27:

# import math

def sign(b):
   if (b>0):
      return 1
   elif (b<0):
      return -1
   else:
      return 0


def sum(a, b):
    sign_b=sign(b)
   # sign_b = int(math.copysign(1, b))
    if b==0:
        return a
    a+=sign_b
    b-=sign_b
    return sum(a, b)

print(sum(2,2))


# Фибоначи
def fibanachy(n):
    if n < 2:
        return 1
    return fibanachy (n-2) + fibanachy (n-1) 
print (fibanachy(7))


def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)
list_1 = []
for i in range(1, 10):
    list_1.append(fib(i - 2))
    print(list_1)