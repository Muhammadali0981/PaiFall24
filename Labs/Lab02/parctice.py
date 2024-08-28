#Practice 1
def greeting():
    print('hello')


greeting()

#Practice 2
def cal_area(a: int, b: int):
    return a * b


length: float = int(input("enter length of rectangle: "))
width: float = int(input("enter width of rectangle: "))

print(f'area is : {cal_area(length,width)}')

#Practice 3
def cal_max(*numbers):
    max = numbers[0]
    for num in numbers:
        if num > max:
            max = num
    print(max)

cal_max(1,20,8)

# Practice 4
def print_details(**details):
    print(f'{details["name"]}, {details["age"]}')


print_details(name ="ali", age = 19)