# Name: Muhammad Ali
# Date: 23/8/2024
# Description: Prints integers from 1 til 5 For multiples of three prints "Fizz"
#              instead of the number and for multiples of five prints "Buzz". For numbers that are multiples
#              of three and five, prints "FizzBuzz".


for n in range(1, 51):
    if (n % 5 == 0) and (n % 3 == 0):
        print("FizzBuzz")
    elif n % 5 == 0:
        print("Buzz")
    elif n % 3 == 0:
        print("Fizz")
    else:
        print(n)