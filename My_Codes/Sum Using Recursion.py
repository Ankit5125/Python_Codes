import random

ls = [random.randint(1,10) for _ in range(10)]
print(ls)

def s(ls):
    if len(ls) == 1:
        return ls[0]
    return ls[0] + s(ls[1:])

print(s(ls))