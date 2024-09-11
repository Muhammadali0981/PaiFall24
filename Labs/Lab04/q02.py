list1: list[str] = ["Hello ", "take "]
list2: list[str] = ["Dear", "Sir"]

print([i + j for i in list1 for j in list2])
