num = int(input("Enter Number : "))

def fact(num):
    if num < 2 :
        return num
    return num * fact(num-1)

print(fact(num))