n: int = int(input("enter how many numbers you want in the list: "))
nums: list[int] = []
even: int = 0

for i in range(n):
    nums.append(int(input("enter num: ")))
    if nums[i]%2 == 0:
        even += 1

print("even numbers are =", even)



