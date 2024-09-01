# Name: Muhammad Ali
# Date: 1/9/24
# Desc: dict through lis


length:int = int(input("Enter total number of elements of list 1 and 2: "))
names:list[str] = []
ages:list[int] = []

for i in range(length):
    names.append(str(input(f"Enter element {i+1} of list 1: ")))
    ages.append(int(input(f"Enter element {i+1} of list 2: ")))

data = {}

for i in range (length):
    data[i] = {names[i]:ages[i]}

print(data)