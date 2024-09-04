length:int = int(input("Enter total number of elements of list 1 and 2: "))
names:list[str] = []
ages:list[int] = []

for i in range(length):
    names.append(str(input(f"Enter element {i+1} of list 1: ")))
    ages.append(int(input(f"Enter element {i+1} of list 2: ")))

data = {}


for i in range(length):
    data[names[i]] = ages[i]

filename: str = str(input('enter file name:'))

try:
    f = open(filename, 'w')
    f.write(str(data))
    f.close()

except FileNotFoundError:
    print("file with this name doesnt exist")