filename: str = str(input('enter file name: '))

try:
    f = open(filename, 'w')
    name: str = str(input("Enter your name: "))
    cnic: str = str(input("Enter your cnic number: "))
    age: str = str(input("Enter your age: "))
    salary: str = str(input("Enter your salary: "))
    f.write(name + " " + cnic + " " + age + " " + salary + " ")
    f.close()
    f = open(filename, 'a')
    contact: str = str(input("Enter your contact number: "))
    f.write(contact)
except FileNotFoundError:
    print("file with this name doesnt exist")