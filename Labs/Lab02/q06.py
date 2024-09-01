# Name: Muhammad Ali
# Date: 1/9/24
# Desc: multiply all numbers in a list

def multiply(data):
    ans:int = 1

    for n in data:
        ans *= n
    return ans


nums:list[int] = [2,4,6,8]
print(multiply(nums))




