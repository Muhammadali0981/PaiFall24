# Name: Muhammad Ali
# Date: 23/8/2024
# Description: Reverse String

string: str = str(input("enter a word:\n"))
reversed_string: str = ""
temp: list[str] = []
i: int = 0
for char in string:
    temp.append(char)

i = len(temp)

while i > 0:
    reversed_string += temp.pop(i - 1)
    i -= 1

print(reversed_string)