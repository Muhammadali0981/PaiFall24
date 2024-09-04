filename: str = str(input('enter file name:'))

try:
    f = open(filename, 'r')
    data: str = f.read()
    print('number of characters are:', len(data))
except FileNotFoundError:
    print("file with this name doesnt exist")
