a: list[str] = ["He", "th", "i", "sal"]
b: list[str] = ["llo", "is", "s", "man"]

c: list[str] = zip(a, b)
d: list[str] = []

for i,j in c:
    d += [i + j]

print(d)
