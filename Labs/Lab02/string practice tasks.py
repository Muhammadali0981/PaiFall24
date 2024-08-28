#task 1

name: str = str(input("your good name!\n"))
print(f'hello! {name.title()}')
c: str = str(input("I hope you are fine, let me know how I can help you!\n"))
if c == 'yes':
    input('share your problem with us\n')
    print('Thanks for your feedback,we will resolve your problem')

print('Okay! Good to see you , stay connected'.center(50))

#task 2
username: str = str(input("enter your full name\n"))
names = username.split(" ")
firstname = names[0]
lastname = names[1]
cast = names[2]

print(f'First Name: {firstname}\nLast name:{lastname}\nCast:{cast}')
