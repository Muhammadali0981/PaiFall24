n: int = int(input("enter how many numbers you want in the list: "))
nums: list[int] = []
sum: int = 0

for i in range(n):
    nums.append(int(input("enter num: ")))
    sum += nums[i]

print("sum of numbers is =", sum)