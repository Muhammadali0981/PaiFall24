sentence: str = str(input("Enter a sentence:"))


try:
    f = open('question.txt', 'w')
    data: str = sentence
    if sentence.endswith('?'):
        f.write(data)

except FileNotFoundError:
    print("file with this name doesnt exist")