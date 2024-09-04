s:str = str(input("enter word to replace:"))
replace:str = str(input("enter word to replace by:"))

filename: str = str(input('enter file name:'))

try:
    f = open(filename, 'r')
    data: str = f.read()
    f.close()
    if s in data:
        data = data.replace(s, replace)
        f = open(filename, 'w')
        f.write(data)
    else:
        print("word not found")
except FileNotFoundError:
    print("file with this name doesnt exist")

