# Name: Muhammad Ali
# Date: 28/8/24
# Desc: functions to check if last alphabet is vowel


vowels: list[str] = ['a','e','i','o','u']
string: str = str(input("enter word: "))

def vowel(a:str):
    for i in vowels:
        if a.endswith(i):
            print("vowel")
            return
    print("not vowel")




vowel(string)