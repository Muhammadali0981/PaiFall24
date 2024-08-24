# Name: Muhammad Ali
# Date: 23/8/2024
# Description: marks with user input

data: dict[str, int] = {}

total: int = 0
avg: float = 0.0
percentage: float = 0.0
greatest: int = -99999
max_marks_subject: str = ""

for n in range(3):
    key: str = str(input("enter subject name: "))
    value: int = int(input("enter subject marks: "))

    data[key] = value

for key in data:
    total += data[key]
    if data[key] > greatest:
        greatest = data[key]
        max_marks_subject = key

avg = total/len(data)
percentage = total/300 * 100

print(f'Average = {avg} and Percentage = {percentage} greatest marks in {max_marks_subject}')