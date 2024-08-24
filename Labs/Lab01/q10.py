# Name: Muhammad Ali
# Date: 23/8/2024
# Description: program to get the largest number from a list input from user.


n: int = int(input("enter how many numbers you want in the list: "))
nums: list[int] = []
maximum: int = -99999

for i in range(n):
    nums.append(int(input("enter num: ")))

for num in nums:
    if num > maximum:
        maximum = num
print(f"Greatest number is = {maximum}")