import json

name:str = input("Enter name: ")
age:int = int(input("Enter age: "))
max:int = 0
maxName:str = ""
try:
    with open("q05.json", "r") as file:
        data = json.load(file)
        data[name] = age
    with open("q05.json", 'w') as file:
        file.seek(0)
        json.dump(data, file)
        for i in data:
            if int(data[i]) > max:
                maxName = i
                max = data[i]
except FileNotFoundError:
    print("file with this name doesnt exist")
print(f"Max Age is of {maxName} which is {max}")