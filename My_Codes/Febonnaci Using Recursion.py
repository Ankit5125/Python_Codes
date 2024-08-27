l = int(input("Enter Last Number : "))

def febo(l):
    if l <= 2:
        return 1
    return febo(l-1) + febo(l-2)

print(febo(5))