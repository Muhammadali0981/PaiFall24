# Name: Muhammad Ali
# Date: 22/8/2024
# Description: program to take a list and a number input from user and then delete all elements in the list
#              less than that number


nums: list[int] = []
num: int = int(input("enter number: "))

n: int = int(input("enter how many numbers you want in the list: "))

for i in range(n):
    nums.append(int(input(f"enter num {i+1}: " )))
    
j: int = 0
while j < len(nums):
    if nums[j] < num:
        del nums[j]
    else:
        j += 1
print("Final list is: ", nums)