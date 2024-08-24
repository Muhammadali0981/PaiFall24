# Name: Muhammad Ali
# Date: 23/8/2024
# Description: program to print a dictionary where the keys are numbers between 1 and 15
#              and the values are the square of the keys.

squares: dict[int, int] = {}

for n in range(1,16):
    key: int = n
    value: int = n*n
    squares[key] = value

print(squares)