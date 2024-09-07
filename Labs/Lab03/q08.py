try:
    num1:int = int(input("enter a number: "))
    num2:int = int(input("enter another number: "))
    print(num1/num2)
except ValueError:
    print('value error')
except ZeroDivisionError:
    print('division by zero not possible')
except:
    print('some other error')