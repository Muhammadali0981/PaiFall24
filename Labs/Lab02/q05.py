# Name: Muhammad Ali
# Date: 28/8/24
# Desc: factorial


num: int = int(input('enter a number:'))

def fact(n):
    if n == 1: return 1
    return n * fact(n-1)


print(fact(num))