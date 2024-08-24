# Name: Muhammad Ali
# Date: 22/8/2024
# Description: Marks stored in dictionary


data: dict[str, int] = {
    "Physics": 40,
    "Chemistry": 78,
    "Maths": 82
}

total: int = 0
avg: float = 0.0
greatest: int = -99999
max_marks_subject: str = ""

for key in data:
    total += data[key]
    if data[key] > greatest:
        greatest = data[key]
        max_marks_subject = key

avg = total/len(data)

print(f'Average = {avg} and greatest marks in {max_marks_subject}')